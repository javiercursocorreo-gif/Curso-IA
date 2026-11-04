#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_excel_autofit.py
Ajuste integral de tamaño, anchos de columna, altos de fila y wrapText con applyAlignment="1"
para visualización perfecta y sin cortes en Microsoft Excel (Mac y Windows).
"""

import os
import zipfile
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_RESUMEN = os.path.join(BASE_DIR, "Seguimiento cistitis resumen.xlsx")
EXCEL_DETALLE = os.path.join(BASE_DIR, "Seguimiento cistitis.xlsx")

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
ET.register_namespace('', NS)

def patch_resumen():
    print("--> Ajustando Seguimiento cistitis resumen.xlsx...")
    temp_zip = EXCEL_RESUMEN + ".tmp"
    
    with zipfile.ZipFile(EXCEL_RESUMEN, 'r') as zin, zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            
            # 1. Parchear styles.xml
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
                
            # 2. Parchear sheet1.xml (anchos y altos de fila)
            elif item.filename == 'xl/worksheets/sheet1.xml':
                root = ET.fromstring(content)
                
                # Actualizar anchos de columna
                cols = root.find(f'{{{NS}}}cols')
                if cols is None:
                    cols = ET.Element(f'{{{NS}}}cols')
                    root.insert(1, cols)
                cols.clear()
                
                widths = {
                    1: 22.0,  # A: Episodios / Fechas
                    2: 28.0,  # B: Germen
                    3: 52.0,  # C: Medicamento / Vacuna
                    4: 40.0,  # D: Duración / Profilaxis
                    5: 42.0,  # E: Doctor / Urgencias
                    6: 110.0, # F: Causa / Comentarios extensos
                }
                for c_idx, w in widths.items():
                    col_el = ET.SubElement(cols, f'{{{NS}}}col', {
                        'min': str(c_idx),
                        'max': str(c_idx),
                        'width': str(w),
                        'customWidth': '1',
                        'bestFit': '1'
                    })
                # Columna extra por seguridad
                ET.SubElement(cols, f'{{{NS}}}col', {
                    'min': '7',
                    'max': '16384',
                    'width': '12.0',
                    'customWidth': '1'
                })
                
                # Actualizar altos de fila generosos
                custom_hts = {
                    1: 35.0,
                    2: 38.0,
                    3: 34.0,
                    4: 55.0,
                    6: 34.0,
                    7: 55.0,
                    11: 65.0,
                    12: 65.0,
                    15: 34.0,
                    16: 55.0,
                    18: 34.0,
                    19: 65.0,
                    21: 34.0,
                    23: 65.0,
                    25: 55.0,
                    27: 34.0,
                    28: 65.0,
                    29: 55.0,
                    31: 75.0,
                    32: 60.0,
                    33: 55.0,
                    34: 60.0,
                    35: 55.0,
                    37: 65.0,
                    39: 34.0,
                    40: 85.0,
                    41: 135.0, # Comentario de 230 caracteres
                    43: 36.0,
                    44: 42.0,
                    45: 42.0,
                    46: 42.0,
                    47: 80.0,  # Conclusión ecográfica
                }
                
                sheetData = root.find(f'{{{NS}}}sheetData')
                if sheetData is not None:
                    for row in sheetData:
                        r_idx = int(row.attrib.get('r', 0))
                        ht = custom_hts.get(r_idx, 46.0 if r_idx > 2 else 32.0)
                        row.attrib['ht'] = str(ht)
                        row.attrib['customHeight'] = '1'
                        
                content = ET.tostring(root, encoding='utf-8', xml_declaration=True)
                
            zout.writestr(item, content)
            
    os.replace(temp_zip, EXCEL_RESUMEN)
    print("  ✓ Seguimiento cistitis resumen.xlsx ajustado al 100%.")

def patch_detalle():
    print("--> Ajustando Seguimiento cistitis.xlsx...")
    temp_zip = EXCEL_DETALLE + ".tmp"
    
    with zipfile.ZipFile(EXCEL_DETALLE, 'r') as zin, zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            
            # 1. Parchear styles.xml
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
                
            # 2. Parchear sheet1.xml
            elif item.filename == 'xl/worksheets/sheet1.xml':
                root = ET.fromstring(content)
                
                # Actualizar anchos de columna
                cols = root.find(f'{{{NS}}}cols')
                if cols is None:
                    cols = ET.Element(f'{{{NS}}}cols')
                    root.insert(1, cols)
                cols.clear()
                
                widths = {
                    1: 16.0,  # A: Fecha
                    2: 26.0,  # B: Causa
                    3: 32.0,  # C: Síntoma
                    4: 16.0,  # D: Infección
                    5: 32.0,  # E: Urgencias
                    6: 55.0,  # F: Resultados / Cultivo
                    7: 16.0,  # G: Antibiotico
                    8: 40.0,  # H: Posología
                    9: 18.0,  # I: Especialista
                    10: 75.0, # J: Observaciones
                }
                for c_idx, w in widths.items():
                    col_el = ET.SubElement(cols, f'{{{NS}}}col', {
                        'min': str(c_idx),
                        'max': str(c_idx),
                        'width': str(w),
                        'customWidth': '1',
                        'bestFit': '1'
                    })
                ET.SubElement(cols, f'{{{NS}}}col', {
                    'min': '11',
                    'max': '16384',
                    'width': '12.0',
                    'customWidth': '1'
                })
                
                # Actualizar altos de fila
                sheetData = root.find(f'{{{NS}}}sheetData')
                if sheetData is not None:
                    for row in sheetData:
                        r_idx = int(row.attrib.get('r', 0))
                        current_ht = float(row.attrib.get('ht', 35.0))
                        # Si es fila con texto largo o filas 61-64, garantizar holgura
                        if r_idx in [61, 62, 63, 64]:
                            row.attrib['ht'] = '85.0'
                        elif r_idx in [8, 45, 48, 49]:
                            row.attrib['ht'] = str(max(current_ht, 95.0))
                        elif r_idx > 1:
                            row.attrib['ht'] = str(max(current_ht, 42.0))
                        row.attrib['customHeight'] = '1'
                        
                content = ET.tostring(root, encoding='utf-8', xml_declaration=True)
                
            zout.writestr(item, content)
            
    os.replace(temp_zip, EXCEL_DETALLE)
    print("  ✓ Seguimiento cistitis.xlsx ajustado al 100%.")

if __name__ == '__main__':
    patch_resumen()
    patch_detalle()
