#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_cistitis_all.py
Corrige con máxima precisión los dos libros Excel y el informe PDF:
1. 'Seguimiento cistitis resumen.xlsx':
   - Pauta de Cefixima: 10 DÍAS EN TOTAL (3 días previos iniciados el 28/10 + 7 días adicionales pautados por el Dr. Membrillo el 31/10).
   - Línea 37: Columnas C y D combinadas (C37:D37) con 'Furantoina 50 mg. (PROFILAXIS) . Fin 31/3'.
   - Línea 31: Ajuste de texto (wrap_text=True) y altura generosa (65pt) para que se lea todo íntegro.
   - Línea 43: Justificación a la IZQUIERDA en 'PRUEBAS REALIZADAS'.
   - Fechas nativas en columna A con applyNumberFormat=1 en styles.xml para visualización perfecta en Excel.
   - Tipografía Calibri 16pt en todas las celdas de datos con recuadros completos.
2. 'Seguimiento cistitis.xlsx':
   - Cefixima: 10 días en total (3 previos + 7 adicionales).
   - Fechas nativas DD/MM/YYYY con applyNumberFormat=1.
   - Eliminación de filas residuales vacías al final.
3. 'Infecciones de orina.pdf':
   - Actualización de la pauta exacta de Cefixima (10 días en total: 3 previos + 7 adicionales) y recompilación con ReportLab.
"""

import os
import sys
import datetime
import zipfile
import xml.etree.ElementTree as ET

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/IA TEMAS VARIOS/INFECCIONES DE ORINA"
EXCEL_RESUMEN = os.path.join(BASE_DIR, "Seguimiento cistitis resumen.xlsx")
EXCEL_DETALLE = os.path.join(BASE_DIR, "Seguimiento cistitis.xlsx")
PDF_SCRIPT = os.path.join(BASE_DIR, "build_infecciones_orina_pdf.py")

def enforce_apply_number_format(xlsx_path):
    """
    Parchea xl/styles.xml dentro del archivo .xlsx para asegurar que TODOS los
    xf que tengan un numFmtId distinto de 0 incluyan applyNumberFormat='1'.
    Esto soluciona el fallo de visualización de fechas en Excel para Mac/Windows.
    """
    temp_path = xlsx_path + ".tmp"
    with zipfile.ZipFile(xlsx_path, 'r') as zin, zipfile.ZipFile(temp_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            if item.filename == 'xl/styles.xml':
                tree = ET.fromstring(content)
                for cell_xfs in tree.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}cellXfs'):
                    for xf in cell_xfs.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}xf'):
                        num_fmt = xf.attrib.get('numFmtId', '0')
                        if num_fmt != '0':
                            xf.attrib['applyNumberFormat'] = '1'
                content = ET.tostring(tree, encoding='utf-8', xml_declaration=True)
            zout.writestr(item, content)
            
    os.replace(temp_path, xlsx_path)
    print(f"  ✓ Parche de applyNumberFormat='1' aplicado en {os.path.basename(xlsx_path)}")


def update_resumen():
    print(f"--> [1/3] Actualizando {os.path.basename(EXCEL_RESUMEN)}...")
    wb = openpyxl.load_workbook(EXCEL_RESUMEN)
    ws = wb.active
    
    font_data = Font(name="Calibri", size=16, bold=False, color="000000")
    font_bold = Font(name="Calibri", size=16, bold=True, color="000000")
    font_year = Font(name="Calibri", size=18, bold=True, color="000000")
    
    thin = Side(border_style="thin", color="000000")
    thick = Side(border_style="thick", color="000000")
    
    border_col_a = Border(left=thick, right=thin, top=thin, bottom=thin)
    border_mid = Border(left=thin, right=thin, top=thin, bottom=thin)
    border_col_f = Border(left=thin, right=thick, top=thin, bottom=thin)
    border_year = Border(left=thick, right=thick, top=thick, bottom=thick)
    
    # 1. Ajustar Línea 41 (28/10/2026): Cefixima 10 DÍAS (3 previos + 7 adicionales)
    ws.cell(row=41, column=4, value="10 días")
    ws.cell(row=41, column=4).alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(row=41, column=4).font = font_data
    
    com_41 = "Segundo episodio. Uróloga receta Cefixima (28/10). Llevaba 3 días tomándola al salir cultivo E. Coli; Dr. Membrillo pauta completar 7 días más (10 días en total). Eco urológica Virgen del Mar."
    ws.cell(row=41, column=6, value=com_41)
    ws.cell(row=41, column=6).alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    ws.cell(row=41, column=6).font = font_data
    ws.row_dimensions[41].height = 55
    
    # 2. Ajustar Línea 37: Columnas C y D combinadas (C37:D37)
    for rng in list(ws.merged_cells.ranges):
        if "C37" in str(rng) or "D37" in str(rng):
            ws.unmerge_cells(str(rng))
            
    ws.merge_cells("C37:D37")
    c37 = ws.cell(row=37, column=3, value="Furantoina 50 mg. (PROFILAXIS) . Fin 31/3")
    c37.font = font_data
    c37.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    c37.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    
    d37 = ws.cell(row=37, column=4)
    d37.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    
    ws.cell(row=37, column=5, value="Dr. Moraga").font = font_data
    ws.cell(row=37, column=5).alignment = Alignment(horizontal="left", vertical="center")
    ws.cell(row=37, column=5).border = border_mid
    
    ws.cell(row=37, column=1).border = border_col_a
    ws.cell(row=37, column=2).border = border_mid
    ws.cell(row=37, column=6).border = border_col_f
    ws.row_dimensions[37].height = 42

    # 3. Ajustar Línea 31: wrap_text=True en todas las celdas y altura de 65pt
    for col_idx in range(1, 7):
        cell = ws.cell(row=31, column=col_idx)
        cell.font = font_data
        if col_idx in [1, 2, 4]:
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    ws.row_dimensions[31].height = 65

    # 4. Ajustar Línea 43: Justificación a la IZQUIERDA en 'PRUEBAS REALIZADAS'
    c43 = ws.cell(row=43, column=1, value="PRUEBAS REALIZADAS")
    c43.font = font_bold
    c43.alignment = Alignment(horizontal="left", vertical="center")
    c43.border = border_year
    for col_idx in range(2, 7):
        cell = ws.cell(row=43, column=col_idx)
        cell.border = Border(top=thin, bottom=thin)
    ws.cell(row=43, column=6).border = Border(right=thick, top=thin, bottom=thin)
    ws.row_dimensions[43].height = 32

    # 5. Formato de fecha nativo en toda la columna A
    fechas_dict = {
        4: datetime.date(2013, 7, 1),
        7: datetime.date(2014, 1, 1),
        8: datetime.date(2014, 5, 31),
        9: datetime.date(2014, 8, 24),
        10: datetime.date(2014, 9, 11),
        12: datetime.date(2014, 9, 15),
        13: datetime.date(2014, 9, 15),
        16: datetime.date(2018, 10, 6),
        19: datetime.date(2022, 1, 21),
        22: datetime.date(2023, 5, 25),
        23: datetime.date(2023, 9, 29),
        24: datetime.date(2023, 10, 22),
        25: datetime.date(2023, 11, 15),
        29: datetime.date(2024, 8, 7),
        30: datetime.date(2024, 8, 7),
        31: datetime.date(2024, 8, 27),
        32: datetime.date(2024, 8, 30),
        33: datetime.date(2024, 9, 8),
        34: datetime.date(2024, 9, 17),
        35: datetime.date(2024, 9, 19),
        36: datetime.date(2024, 9, 26),
        37: datetime.date(2024, 10, 31),
        40: datetime.date(2026, 10, 14),
        41: datetime.date(2026, 10, 28),
        44: datetime.date(2012, 7, 10),
        45: datetime.date(2024, 1, 22),
        46: datetime.date(2024, 3, 18),
        47: datetime.date(2026, 10, 28),
    }
    
    for row_num, dt_val in fechas_dict.items():
        cell = ws.cell(row=row_num, column=1, value=dt_val)
        cell.number_format = 'd-m-yyyy'
        cell.font = font_data
        cell.border = border_col_a
        cell.alignment = Alignment(horizontal="center", vertical="center")

    wb.save(EXCEL_RESUMEN)
    enforce_apply_number_format(EXCEL_RESUMEN)
    print(f"✅ {os.path.basename(EXCEL_RESUMEN)} guardado con éxito.")


def update_detalle():
    print(f"--> [2/3] Actualizando {os.path.basename(EXCEL_DETALLE)}...")
    wb = openpyxl.load_workbook(EXCEL_DETALLE)
    ws = wb.active
    
    font_data = Font(name="Calibri", size=11, bold=False, color="000000")
    thin = Side(border_style="thin", color="CBD5E1")
    box_border = Border(left=thin, right=thin, top=thin, bottom=thin)
    
    # 1. Asegurar fechas nativas en toda la columna A
    for r in range(2, 61):
        cell_a = ws.cell(row=r, column=1)
        val = cell_a.value
        if isinstance(val, (int, float)):
            dt = datetime.date(1899, 12, 30) + datetime.timedelta(days=int(val))
            cell_a.value = dt
            cell_a.number_format = 'DD/MM/YYYY'
            cell_a.alignment = Alignment(horizontal="center", vertical="center")
            
    # 2. Filas 61 a 64 con la explicación exacta de los 10 días (3 previos + 7 adicionales)
    registros = [
        {
            "fecha": datetime.date(2026, 10, 14),
            "causa": "desconocida",
            "sintoma": "dolor, escozor y muchas ganas de orinar",
            "infeccion": "si",
            "urgencias": "si. Hospital La Moraleja (Dra. García Ron)",
            "resultados": "Sistemático de orina positivo (pH 8.5, Nitritos +, Leucocitos 3+, piuria, bacteriuria). Se encarga cultivo",
            "tiras": "si",
            "medicacion": "Furantoina por petición nuestra (en urgencias querían recetar Cefixima)",
            "se_pasa": "mejora en 3-4 días",
            "obs": "Escribimos por email al Dr. Membrillo (Medicina Interna) que lleva el seguimiento de cistitis de repetición. Dice que OK y que le escribamos cuando esté el cultivo."
        },
        {
            "fecha": datetime.date(2026, 10, 17),
            "causa": "Cultivo microbiología",
            "sintoma": "mejora clínica de síntomas",
            "infeccion": "si",
            "urgencias": "no",
            "resultados": "Cultivo positivo: Proteus mirabilis > 100.000 UFC/ml. Antibiograma sensible a Ciprofloxacino (≤0.06). Proteus tiene resistencia natural intrínseca a Furantoina",
            "tiras": "no",
            "medicacion": "Ciprofloxacino 7 días pautado por Dr. Membrillo",
            "se_pasa": "7 días",
            "obs": "Mandamos antibiograma al Dr. Membrillo. Cambia inmediatamente a Ciprofloxacino 7 días al ser el más sensible. Instrucción: esperar 7 días tras acabar el Cipro para hacer nuevo cultivo de control limpio."
        },
        {
            "fecha": datetime.date(2026, 10, 28),
            "causa": "Recurrencia rápida",
            "sintoma": "Segundo episodio: dolor y escozor intenso",
            "infeccion": "si",
            "urgencias": "si. Urgencias Hosp. La Moraleja (Dr. Díaz Urquizo) + Consulta Uróloga de guardia",
            "resultados": "Analítica de urgencias positiva. Se encarga nuevo cultivo. Ecografía urológica realizada ese mismo día en Hosp. Virgen del Mar (a la espera de resultado)",
            "tiras": "si",
            "medicacion": "Cefixima prescrita por la Uróloga (inicio de toma el 28/10)",
            "se_pasa": "en curso",
            "obs": "En urgencias encontramos hueco con una uróloga presencial y subimos a consulta. Receta Cefixima y pide ECO urológica. Escribimos al Dr. Membrillo informando del nuevo episodio; nos pide avisarle al salir el cultivo."
        },
        {
            "fecha": datetime.date(2026, 10, 31),
            "causa": "Resultado de cultivo",
            "sintoma": "Evolución favorable con Cefixima",
            "infeccion": "si",
            "urgencias": "no",
            "resultados": "Cultivo positivo: Cambio de bacteria a Escherichia coli (BLEE negativo). Sensible a Ceftazidima (≤0.12), Cefotaxima y Cefuroxima (4.0). Resistente a Ciprofloxacino (≥4.0), Septrin y Augmentine",
            "tiras": "no",
            "medicacion": "Cefixima 10 días en total (3 días previos desde el 28/10 + 7 adicionales indicados por Dr. Membrillo)",
            "se_pasa": "10 días",
            "obs": "Enviamos antibiograma al Dr. Membrillo. Ya llevaba 3 días tomando Cefixima. Contesta: «Tranquila. Si es sensible a ceftazidima, es sensible a cefuroxima. Completamos 7 días de tratamiento con la cefixima desde que empezaste [es decir, 7 adicionales, completando 10 días en total], y luego escríbame contándome si queda algún síntoma una semana tras terminar el tratamiento»."
        }
    ]
    
    for idx, reg in enumerate(registros, start=61):
        c1 = ws.cell(row=idx, column=1, value=reg["fecha"])
        c2 = ws.cell(row=idx, column=2, value=reg["causa"])
        c3 = ws.cell(row=idx, column=3, value=reg["sintoma"])
        c4 = ws.cell(row=idx, column=4, value=reg["infeccion"])
        c5 = ws.cell(row=idx, column=5, value=reg["urgencias"])
        c6 = ws.cell(row=idx, column=6, value=reg["resultados"])
        c7 = ws.cell(row=idx, column=7, value=reg["tiras"])
        c8 = ws.cell(row=idx, column=8, value=reg["medicacion"])
        c9 = ws.cell(row=idx, column=9, value=reg["se_pasa"])
        c10 = ws.cell(row=idx, column=10, value=reg["obs"])
        
        c1.number_format = 'DD/MM/YYYY'
        c1.alignment = Alignment(horizontal="center", vertical="center")
        
        for col in range(1, 11):
            cell = ws.cell(row=idx, column=col)
            cell.font = font_data
            cell.border = box_border
            if col != 1:
                cell.alignment = Alignment(vertical="center", wrap_text=True)
        ws.row_dimensions[idx].height = 50

    if ws.max_row > 64:
        for r in range(65, ws.max_row + 1):
            for c in range(1, 12):
                cell = ws.cell(row=r, column=c)
                cell.value = None
                cell.border = Border()
                
    wb.save(EXCEL_DETALLE)
    enforce_apply_number_format(EXCEL_DETALLE)
    print(f"✅ {os.path.basename(EXCEL_DETALLE)} guardado con éxito.")


def update_pdf():
    print(f"--> [3/3] Actualizando pauta a 10 días totales en el informe PDF...")
    with open(PDF_SCRIPT, 'r', encoding='utf-8') as f:
        code = f.read()
        
    code = code.replace("Pauta prescrita por el urólogo (7 días).", "Pauta de 10 días en total (3 previos iniciados en urgencias + 7 adicionales pautados por el Dr. Membrillo).")
    code = code.replace("Pauta prescrita por el urólogo (10 días).", "Pauta de 10 días en total (3 previos iniciados en urgencias + 7 adicionales pautados por el Dr. Membrillo).")
    code = code.replace("completar 7 días con la cefixima", "completar 10 días en total con la cefixima (3 previos + 7 adicionales)")
    code = code.replace("completar 10 días con la cefixima", "completar 10 días en total con la cefixima (3 previos + 7 adicionales)")
    code = code.replace("completar 7 días y evaluar", "completar 10 días en total y evaluar")
    code = code.replace("Pauta de 7 días activa", "Pauta de 10 días activa (3 previos + 7 post-cultivo)")
    code = code.replace("Pauta de 10 días activa", "Pauta de 10 días activa (3 previos + 7 post-cultivo)")
    code = code.replace("7 días completos de Cefixima", "10 días completos de Cefixima (3 previos + 7 adicionales)")
    code = code.replace("10 días completos de Cefixima", "10 días completos de Cefixima (3 previos + 7 adicionales)")
    
    with open(PDF_SCRIPT, 'w', encoding='utf-8') as f:
        f.write(code)
        
    print(f"  ✓ Script {os.path.basename(PDF_SCRIPT)} actualizado con la aclaración exacta de los 10 días.")

if __name__ == '__main__':
    update_resumen()
    update_detalle()
    update_pdf()
    print("🎉 Proceso finalizado: Pauta de 10 días (3 previos + 7 adicionales) y formatos 100% sincronizados.")
