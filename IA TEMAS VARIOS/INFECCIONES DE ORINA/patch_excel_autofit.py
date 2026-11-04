#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_excel_autofit.py
Ajuste integral de tamaño y formato para Microsoft Excel (Mac y Windows):
- 'Seguimiento cistitis resumen.xlsx': Anchos compactos (no exagerados),
  cálculo dinámico automático de altura de fila para que ningún comentario quede cortado,
  applyAlignment=1 y wrapText=1 en todas las celdas.
- 'Seguimiento cistitis.xlsx': Anchos originales compactos (sin ensanchar columnas),
  cálculo dinámico automático de altura de fila según el número de líneas envueltas.
"""

import os
import zipfile
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_RESUMEN = os.path.join(BASE_DIR, "Seguimiento cistitis resumen.xlsx")
EXCEL_DETALLE = os.path.join(BASE_DIR, "Seguimiento cistitis.xlsx")

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
ET.register_namespace('', NS)

def patch_resumen(target_path=None):
    xlsx_path = target_path or EXCEL_RESUMEN
    if not os.path.exists(xlsx_path):
        return
    print(f"--> Ajustando {os.path.basename(xlsx_path)} (anchos compactos y alturas dinámicas)...")
    temp_zip = xlsx_path + ".tmp"
    
    with zipfile.ZipFile(xlsx_path, 'r') as zin, zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            
            # 1. Parchear styles.xml (wrapText y applyAlignment)
            if item.filename == 'xl/styles.xml':
                root = ET.fromstring(content)
                cell_xfs = root.find(f'{{{NS}}}cellXfs')
                if cell_xfs is not None:
                    for xf in cell_xfs:
                        xf.attrib['applyAlignment'] = '1'
                        num_fmt = xf.attrib.get('numFmtId', '0')
                        if num_fmt != '0':
                            xf.attrib['applyNumberFormat'] = '1'
                        al = xf.find(f'{{{NS}}}alignment')
                        if al is None:
                            al = ET.SubElement(xf, f'{{{NS}}}alignment')
                        al.attrib['wrapText'] = '1'
                        al.attrib['vertical'] = 'center'
                content = ET.tostring(root, encoding='utf-8', xml_declaration=True)
                
            # 2. Parchear sheet1.xml (anchos compactos no exagerados y alturas dinámicas)
            elif item.filename == 'xl/worksheets/sheet1.xml':
                root = ET.fromstring(content)
                
                # Anchos compactos equilibrados (no tan anchos)
                cols = root.find(f'{{{NS}}}cols')
                if cols is None:
                    cols = ET.Element(f'{{{NS}}}cols')
                    root.insert(1, cols)
                cols.clear()
                
                compact_widths = {
                    1: 18.0,  # A: Episodios / Fechas
                    2: 22.0,  # B: Germen
                    3: 38.0,  # C: Medicamento / Vacuna
                    4: 20.0,  # D: Duración / Profilaxis (cabe '0-0-1, 6 meses')
                    5: 30.0,  # E: Doctor / Urgencias
                    6: 52.0,  # F: Causa / Comentarios compactos
                }
                for c_idx, w in compact_widths.items():
                    ET.SubElement(cols, f'{{{NS}}}col', {
                        'min': str(c_idx),
                        'max': str(c_idx),
                        'width': str(w),
                        'customWidth': '1',
                        'bestFit': '1'
                    })
                ET.SubElement(cols, f'{{{NS}}}col', {
                    'min': '7',
                    'max': '16384',
                    'width': '10.8',
                    'customWidth': '1'
                })
                
                # Capacidad aprox de caracteres por línea a 16pt Calibri
                col_chars = {'A': 14, 'B': 18, 'C': 30, 'D': 16, 'E': 24, 'F': 40}
                
                sheetData = root.find(f'{{{NS}}}sheetData')
                if sheetData is not None:
                    for row in sheetData:
                        r_idx = int(row.attrib.get('r', 0))
                        if r_idx in [3, 6, 15, 18, 21, 27, 39]: # Años divisores
                            row.attrib['ht'] = '34.0'
                            row.attrib['customHeight'] = '1'
                            continue
                            
                        max_lines = 1
                        for c in row.findall(f'{{{NS}}}c'):
                            ref = c.attrib.get('r', '')
                            col_letter = ''.join([ch for ch in ref if ch.isalpha()])
                            limit = col_chars.get(col_letter, 25)
                            txt = ''.join(c.itertext()).strip()
                            if txt and not txt.isdigit():
                                words = txt.split()
                                lines = 1
                                curr_len = 0
                                for word in words:
                                    add_len = len(word) + (1 if curr_len else 0)
                                    if curr_len + add_len <= limit:
                                        curr_len += add_len
                                    else:
                                        lines += 1
                                        curr_len = len(word)
                                if lines > max_lines:
                                    max_lines = lines
                        
                        # A 16pt Calibri, cada línea mide ~22pt + 14pt de margen
                        calc_ht = max(38.0, max_lines * 22.0 + 14.0)
                        
                        # Ajustes finos específicos para asegurar holgura perfecta
                        if r_idx == 41:
                            calc_ht = max(calc_ht, 175.0) # Comentario de 230 chars (7 líneas)
                        elif r_idx == 40:
                            calc_ht = max(calc_ht, 105.0) # Comentario de 115 chars (4 líneas)
                        elif r_idx == 47:
                            calc_ht = max(calc_ht, 85.0)  # Conclusión eco
                        elif r_idx in [28, 31]:
                            calc_ht = max(calc_ht, 80.0)  # 3 líneas
                        elif r_idx in [1, 4, 9, 11, 12, 16, 19, 23, 32, 33, 34, 37]:
                            calc_ht = max(calc_ht, 60.0)  # 2 líneas
                        elif r_idx > 47:
                            calc_ht = 32.0               # Filas vacías finales
                            
                        row.attrib['ht'] = f"{calc_ht:.1f}"
                        row.attrib['customHeight'] = '1'
                        
                content = ET.tostring(root, encoding='utf-8', xml_declaration=True)
                
            zout.writestr(item, content)
            
    os.replace(temp_zip, xlsx_path)
    print(f"  ✓ {os.path.basename(xlsx_path)} ajustado al 100% (anchos compactos y alturas calculadas).")

def patch_detalle(target_path=None):
    xlsx_path = target_path or EXCEL_DETALLE
    if not os.path.exists(xlsx_path):
        return
    print(f"--> Ajustando {os.path.basename(xlsx_path)} (altura dinámica sin ensanchar columnas)...")
    temp_zip = xlsx_path + ".tmp"
    
    with zipfile.ZipFile(xlsx_path, 'r') as zin, zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            
            # 1. Parchear styles.xml (wrapText en todas las celdas)
            if item.filename == 'xl/styles.xml':
                root = ET.fromstring(content)
                cell_xfs = root.find(f'{{{NS}}}cellXfs')
                if cell_xfs is not None:
                    for xf in cell_xfs:
                        xf.attrib['applyAlignment'] = '1'
                        num_fmt = xf.attrib.get('numFmtId', '0')
                        if num_fmt != '0':
                            xf.attrib['applyNumberFormat'] = '1'
                        al = xf.find(f'{{{NS}}}alignment')
                        if al is None:
                            al = ET.SubElement(xf, f'{{{NS}}}alignment')
                        al.attrib['wrapText'] = '1'
                        al.attrib['vertical'] = 'center'
                content = ET.tostring(root, encoding='utf-8', xml_declaration=True)
                
            # 2. Parchear sheet1.xml: Restaurar anchos originales compactos y calcular alto exacto
            elif item.filename == 'xl/worksheets/sheet1.xml':
                root = ET.fromstring(content)
                
                # Restaurar anchos originales compactos (sin ensanchar columnas)
                cols = root.find(f'{{{NS}}}cols')
                if cols is None:
                    cols = ET.Element(f'{{{NS}}}cols')
                    root.insert(1, cols)
                cols.clear()
                
                orig_widths = {
                    1: 13.5,  # A: Fecha
                    2: 20.8,  # B: Causa
                    3: 11.5,  # C: Síntoma
                    4: 10.8,  # D: Infección
                    5: 13.8,  # E: Urgencias
                    6: 16.5,  # F: Resultados / Cultivo
                    7: 12.5,  # G: Tiras
                    8: 28.2,  # H: Posología / Medicamento
                    9: 10.5,  # I: Se pasa / Especialista
                    10: 44.5, # J: Observaciones
                }
                for c_idx, w in orig_widths.items():
                    ET.SubElement(cols, f'{{{NS}}}col', {
                        'min': str(c_idx),
                        'max': str(c_idx),
                        'width': str(w),
                        'customWidth': '1',
                        'bestFit': '1'
                    })
                ET.SubElement(cols, f'{{{NS}}}col', {
                    'min': '11',
                    'max': '16384',
                    'width': '10.8',
                    'customWidth': '1'
                })
                
                col_letter_map = {'A': 13.5, 'B': 20.8, 'C': 11.5, 'D': 10.8, 'E': 13.8, 'F': 16.5, 'G': 12.5, 'H': 28.2, 'I': 10.5, 'J': 44.5}
                
                sheetData = root.find(f'{{{NS}}}sheetData')
                if sheetData is not None:
                    for row in sheetData:
                        r_idx = int(row.attrib.get('r', 0))
                        if r_idx == 1:
                            row.attrib['ht'] = '32.0'
                            row.attrib['customHeight'] = '1'
                            continue
                            
                        max_lines = 1
                        for c in row.findall(f'{{{NS}}}c'):
                            ref = c.attrib.get('r', '')
                            col_letter = ''.join([ch for ch in ref if ch.isalpha()])
                            w = col_letter_map.get(col_letter, 15.0)
                            txt = ''.join(c.itertext()).strip()
                            if txt and not txt.isdigit():
                                words = txt.split()
                                lines = 1
                                curr_len = 0
                                for word in words:
                                    add_len = len(word) + (1 if curr_len else 0)
                                    if curr_len + add_len <= w:
                                        curr_len += add_len
                                    else:
                                        lines += 1
                                        curr_len = len(word)
                                if lines > max_lines:
                                    max_lines = lines
                        
                        calc_ht = max(26.0, max_lines * 16.0 + 8.0)
                        
                        if r_idx == 64:
                            calc_ht = max(calc_ht, 250.0)
                        elif r_idx == 63:
                            calc_ht = max(calc_ht, 220.0)
                        elif r_idx == 62:
                            calc_ht = max(calc_ht, 235.0)
                        elif r_idx == 61:
                            calc_ht = max(calc_ht, 140.0)
                        elif r_idx == 8:
                            calc_ht = max(calc_ht, 170.0)
                        elif r_idx in [5, 45]:
                            calc_ht = max(calc_ht, 105.0)
                        elif r_idx in [48, 49]:
                            calc_ht = max(calc_ht, 90.0)
                            
                        row.attrib['ht'] = f"{calc_ht:.1f}"
                        row.attrib['customHeight'] = '1'
                        
                content = ET.tostring(root, encoding='utf-8', xml_declaration=True)
                
            zout.writestr(item, content)
            
    os.replace(temp_zip, xlsx_path)
    print(f"  ✓ {os.path.basename(xlsx_path)} ajustado al 100% (alturas dinámicas sin ensanchar columnas).")

if __name__ == '__main__':
    patch_resumen()
    patch_detalle()
