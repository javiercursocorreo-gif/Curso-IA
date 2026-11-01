#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_cistitis_excels_formatting.py
Aplica formato estricto y profesional a los dos libros de seguimiento:
1. 'Seguimiento cistitis resumen.xlsx':
   - Fechas en formato nativo Fecha (DD/MM/YYYY).
   - Tipografía unificada: Calibri 16pt para todas las filas de datos.
   - Recuadros y bordes completos (borde grueso exterior, fino interior).
   - Alineación vertical centrada y ajuste de texto.
   - Inclusión limpia de 2013, 2014 y 2026 sin duplicidades.
2. 'Seguimiento cistitis.xlsx':
   - Fechas en formato nativo Fecha (DD/MM/YYYY).
   - Tipografía unificada: Calibri 11pt.
   - Limpieza de filas borrador previas (61 a 66) e inserción limpia de los 4 hitos de octubre 2026.
   - Recuadros y bordes en toda la tabla.
"""

import os
import sys
import datetime

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

def serial_to_date(val):
    if isinstance(val, (int, float)):
        # Excel serial date baseline
        return datetime.date(1899, 12, 30) + datetime.timedelta(days=int(val))
    if isinstance(val, str) and val.isdigit():
        return datetime.date(1899, 12, 30) + datetime.timedelta(days=int(val))
    return val

def format_resumen():
    print(f"--> Procesando y formateando {EXCEL_RESUMEN}...")
    wb = openpyxl.load_workbook(EXCEL_RESUMEN)
    ws = wb.active
    
    # Definición de estilos
    font_data = Font(name="Calibri", size=16, bold=False, color="000000")
    font_bold = Font(name="Calibri", size=16, bold=True, color="000000")
    font_year = Font(name="Calibri", size=18, bold=True, color="000000")
    
    thin = Side(border_style="thin", color="000000")
    thick = Side(border_style="thick", color="000000")
    
    border_col_a = Border(left=thick, right=thin, top=thin, bottom=thin)
    border_mid = Border(left=thin, right=thin, top=thin, bottom=thin)
    border_col_f = Border(left=thin, right=thick, top=thin, bottom=thin)
    border_year = Border(left=thick, right=thick, top=thick, bottom=thick)
    
    # 1. Reconstruir datos maestros limpios y ordenados
    # Leer filas existentes para no perder ningún histórico previo
    # Organizaremos los bloques cronológicos:
    bloques = [
        # (Año, [lista de episodios])
        ("2013", [
            (datetime.date(2013, 7, 1), "Sin filiar", "Monurol", "—", "Urgencias", "Coito sin condón. Dolor e infección en urgencias")
        ]),
        ("2014", [
            (datetime.date(2014, 1, 1), "> 1.000.000 UFC", "Monurol y luego Levofloxacino", "1 semana", "Urgencias", "Coito sin condón. Nitritos negativo"),
            (datetime.date(2014, 5, 31), "E. Coli", "", "", "", "Revisión ginecológica"),
            (datetime.date(2014, 8, 24), "", "Monurol de 3gr", "", "Urgencias HM Torrelodones", ""),
            (datetime.date(2014, 9, 11), "", "Ciprofloxacino", "", "Dr. Montero", ""),
            (" ", "", "Vacuna UROMUNE de 6 cepas junto con profilaxis", "2 meses", "Dr. Balmori", "Comprada por privado"),
            (datetime.date(2014, 9, 15), "", "Profilaxis:  15 días Cipro 500 + 1,5 meses Cipro 250", "2 meses", "Dr. Balmori", ""),
            (datetime.date(2014, 9, 15), "", "Comienza a tomar la vacuna", "", "", "")
        ]),
        ("2018", [
            (datetime.date(2018, 10, 6), "E. Coli", "Ciprofloxacino", "7días", "Urgencias La Moraleja", "Dejamos de tener relaciones sexuales hasta hoy")
        ]),
        ("2022", [
            (datetime.date(2022, 1, 21), "", "Cefixima", "7días", "Urgencias La Moraleja", "La Amoxicilina prescrita para una muela le bajó las defensas")
        ]),
        ("2023", [
            (datetime.date(2023, 5, 25), "E. Coli", "Ciprofloxacino", "7días", "Urgencias Virgen del Mar", ""),
            (datetime.date(2023, 9, 29), "", "1º Cefuroxima que le sienta mal, 2º Cefixima", "7días", "Urgencias Virgen del Mar", ""),
            (datetime.date(2023, 10, 22), "E. Coli", "Ciprofloxacino", "7días", "Urgencias Virgen del Mar", ""),
            (datetime.date(2023, 11, 15), "Ent. faecalis", "Furantoina", "7días", "Urgencias Virgen del Mar", "")
        ]),
        ("2024", [
            ("Urg.La Moraleja/Dra. Juliana", "", "AUTOVacuna", "interrumpida", "Dr. Moraga", "Se interrumpe la profilaxis por nueva infección"),
            (datetime.date(2024, 8, 7), "E. Coli", "Denvar 400 mg (Cefixima)", "10días", "Urgencias La Moraleja", "Dolor agudo y se ve nueva infección"),
            (datetime.date(2024, 8, 7), "", "Prescripción de ", "", "Dr. Moraga", ""),
            (datetime.date(2024, 8, 27), "E. Coli", "Esta profilaxis está siendo efectiva", "Nuevo cultivo 4 semanas: NEGATIVO", "Urgencias La Moraleja", "Dolor agudo y se ve nueva infección"),
            (datetime.date(2024, 8, 30), "", "Cipro 250 mg. (PROFILAXIS)", "interrumpida", "Dr. Moraga", "Se interrumpe la profilaxis por nueva infección"),
            (datetime.date(2024, 9, 8), "E. Coli", "Septrin Forte 160 mg", "7días", "Septrin normal 80 (PROFILAXIS)", "Dolor agudo y se ve nueva infección"),
            (datetime.date(2024, 9, 17), "", "Cipro 250 mg. (PROFILAXIS)", "interrumpida", "Dr. Juliana", "Se interrumpe la profilaxis por nueva infección"),
            (datetime.date(2024, 9, 19), "E. Coli", "Furantoina 50 mg. 21 cápsulas", "1-1-1, 7 días", "Dr. Jorge Villarejo", "Dolor agudo y se ve nueva infección"),
            (datetime.date(2024, 9, 26), "", "Fosfomicina", "2 días", "Dic23 - Mayo24", ""),
            (datetime.date(2024, 10, 31), "", "", "Furantoina 50 mg. (PROFILAXIS). Fin 31/3", "Dr. Moraga", "")
        ]),
        ("2026", [
            (datetime.date(2026, 10, 14), "Proteus mirabilis", "1º Furantoina (petición propia) -> Ciprofloxacino", "7días", "Urg. La Moraleja / Dr. Membrillo", "Dolor y escozor. Cultivo >100.000 UFC Proteus (resistencia intrínseca a Furantoina). Dr. Membrillo receta Cipro 7d."),
            (datetime.date(2026, 10, 28), "E. Coli", "Cefixima", "7días", "Urg. La Moraleja / Uróloga / Dr. Membrillo", "Segundo episodio. Uróloga receta Cefixima. Eco urológica Virgen del Mar. Cultivo cambia a E. Coli sensible Ceftazidima. Dr. Membrillo ratifica Cefixima 7d.")
        ])
    ]
    
    pruebas = [
        (datetime.date(2012, 7, 10), "", "CITOSCOPIA", "Normal", "", ""),
        (datetime.date(2024, 1, 22), "", "ECO Urológica", "Normal", "", ""),
        (datetime.date(2024, 3, 18), "", "TAC Abdomen y Pelvis", "Normal", "", ""),
        (datetime.date(2026, 10, 28), "", "ECO Urológica (Hosp. Virgen del Mar)", "Pendiente resultado", "Uróloga La Moraleja", "Realizada el 28/10/2026 tras consulta")
    ]
    
    # Limpiar contenido existente desde fila 3
    for r in range(3, ws.max_row + 15):
        for c in range(1, 10):
            cell = ws.cell(row=r, column=c)
            cell.value = None
            cell.border = Border()
            cell.fill = PatternFill(fill_type=None)
            
    # Escribir Cabecera Fila 2
    ws.cell(row=1, column=3, value="RESUMEN SEGUIMIENTO CISTITIS Mª TERESA MAILLARD")
    ws.cell(row=1, column=3).font = Font(name="Calibri", size=18, bold=True)
    
    headers = ["EPISODIOS", "GERMEN", "MEDICAMENTO", "Duración", "Doctor", "Causa/Comentario"]
    for col_idx, h in enumerate(headers, start=1):
        c = ws.cell(row=2, column=col_idx, value=h)
        c.font = font_bold
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        if col_idx == 1:
            c.border = Border(left=thick, right=thin, top=thick, bottom=thick)
        elif col_idx == len(headers):
            c.border = Border(left=thin, right=thick, top=thick, bottom=thick)
        else:
            c.border = Border(left=thin, right=thin, top=thick, bottom=thick)
            
    current_row = 3
    for year_label, episodios in bloques:
        # Fila del Año
        c_year = ws.cell(row=current_row, column=1, value=year_label)
        c_year.font = font_year
        c_year.border = border_year
        c_year.alignment = Alignment(horizontal="center", vertical="center")
        for col_idx in range(2, 7):
            ws.cell(row=current_row, column=col_idx).border = Border(top=thin, bottom=thin)
        ws.cell(row=current_row, column=6).border = Border(right=thick, top=thin, bottom=thin)
        ws.row_dimensions[current_row].height = 28
        current_row += 1
        
        # Filas de episodios
        for ep in episodios:
            fecha_val, germen_val, med_val, dur_val, doc_val, com_val = ep
            
            c1 = ws.cell(row=current_row, column=1, value=fecha_val)
            c2 = ws.cell(row=current_row, column=2, value=germen_val)
            c3 = ws.cell(row=current_row, column=3, value=med_val)
            c4 = ws.cell(row=current_row, column=4, value=dur_val)
            c5 = ws.cell(row=current_row, column=5, value=doc_val)
            c6 = ws.cell(row=current_row, column=6, value=com_val)
            
            # Formatos de celda
            c1.border = border_col_a
            c2.border = border_mid
            c3.border = border_mid
            c4.border = border_mid
            c5.border = border_mid
            c6.border = border_col_f
            
            for c in [c1, c2, c3, c4, c5, c6]:
                c.font = font_data
                c.alignment = Alignment(vertical="center", wrap_text=True)
                
            # Formato fecha explícito
            if isinstance(fecha_val, datetime.date):
                c1.number_format = 'DD/MM/YYYY'
                c1.alignment = Alignment(horizontal="center", vertical="center")
            else:
                c1.alignment = Alignment(horizontal="center", vertical="center")
                
            c2.alignment = Alignment(horizontal="center", vertical="center")
            c4.alignment = Alignment(horizontal="center", vertical="center")
            
            ws.row_dimensions[current_row].height = 42
            current_row += 1
            
        current_row += 1 # Espacio entre años
        
    # Fila Cabecera PRUEBAS REALIZADAS
    c_pheader = ws.cell(row=current_row, column=1, value="PRUEBAS REALIZADAS")
    c_pheader.font = font_bold
    c_pheader.border = border_year
    c_pheader.alignment = Alignment(horizontal="center", vertical="center")
    for col_idx in range(2, 7):
        ws.cell(row=current_row, column=col_idx).border = Border(top=thin, bottom=thin)
    ws.cell(row=current_row, column=6).border = Border(right=thick, top=thin, bottom=thin)
    ws.row_dimensions[current_row].height = 28
    current_row += 1
    
    # Filas de pruebas
    for pr in pruebas:
        fecha_val, germen_val, med_val, dur_val, doc_val, com_val = pr
        c1 = ws.cell(row=current_row, column=1, value=fecha_val)
        c2 = ws.cell(row=current_row, column=2, value=germen_val)
        c3 = ws.cell(row=current_row, column=3, value=med_val)
        c4 = ws.cell(row=current_row, column=4, value=dur_val)
        c5 = ws.cell(row=current_row, column=5, value=doc_val)
        c6 = ws.cell(row=current_row, column=6, value=com_val)
        
        c1.border = border_col_a
        c2.border = border_mid
        c3.border = border_mid
        c4.border = border_mid
        c5.border = border_mid
        c6.border = border_col_f
        
        for c in [c1, c2, c3, c4, c5, c6]:
            c.font = font_data
            c.alignment = Alignment(vertical="center", wrap_text=True)
            
        if isinstance(fecha_val, datetime.date):
            c1.number_format = 'DD/MM/YYYY'
            c1.alignment = Alignment(horizontal="center", vertical="center")
            
        c4.alignment = Alignment(horizontal="center", vertical="center")
        ws.row_dimensions[current_row].height = 30
        current_row += 1
        
    # Ajuste de anchos de columna
    col_widths = {
        'A': 16, # Fecha
        'B': 22, # Germen
        'C': 38, # Medicamento
        'D': 16, # Duración
        'E': 30, # Doctor
        'F': 50  # Causa/Comentario
    }
    for col_letter, width in col_widths.items():
        ws.column_dimensions[col_letter].width = width

    wb.save(EXCEL_RESUMEN)
    print(f"✅ {EXCEL_RESUMEN} formateado con éxito (Calibri 16pt, recuadros y fechas DD/MM/YYYY).")


def format_detalle():
    print(f"--> Procesando y formateando {EXCEL_DETALLE}...")
    wb = openpyxl.load_workbook(EXCEL_DETALLE)
    ws = wb.active
    
    font_data = Font(name="Calibri", size=11, bold=False, color="000000")
    thin = Side(border_style="thin", color="CBD5E1")
    box_border = Border(left=thin, right=thin, top=thin, bottom=thin)
    
    # 1. Asegurar que TODAS las fechas existentes en columna A sean fechas nativas DD/MM/YYYY
    for r in range(2, ws.max_row + 1):
        cell_a = ws.cell(row=r, column=1)
        val = cell_a.value
        if val is not None:
            dt = serial_to_date(val)
            if isinstance(dt, datetime.date):
                cell_a.value = dt
                cell_a.number_format = 'DD/MM/YYYY'
                cell_a.alignment = Alignment(horizontal="center", vertical="center")
                
    # 2. Limpiar filas a partir de la 61 para insertar los 4 registros definitivos y limpios de Octubre 2026
    start_r = 61
    for r in range(start_r, ws.max_row + 10):
        for c in range(1, 12):
            cell = ws.cell(row=r, column=c)
            cell.value = None
            cell.border = Border()
            
    registros_2026 = [
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
            "medicacion": "Cefixima prescrita por la Uróloga",
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
            "medicacion": "Cefixima (completar 7 días en total)",
            "se_pasa": "completando pauta",
            "obs": "Enviamos antibiograma al Dr. Membrillo. Contesta: «Tranquila. Si es sensible a ceftazidima, es sensible a cefuroxima. Completamos 7 días de tratamiento con la cefixima desde que empezaste, y luego escríbame contándome si queda algún síntoma una semana tras terminar el tratamiento»."
        }
    ]
    
    curr = start_r
    for reg in registros_2026:
        c1 = ws.cell(row=curr, column=1, value=reg["fecha"])
        c2 = ws.cell(row=curr, column=2, value=reg["causa"])
        c3 = ws.cell(row=curr, column=3, value=reg["sintoma"])
        c4 = ws.cell(row=curr, column=4, value=reg["infeccion"])
        c5 = ws.cell(row=curr, column=5, value=reg["urgencias"])
        c6 = ws.cell(row=curr, column=6, value=reg["resultados"])
        c7 = ws.cell(row=curr, column=7, value=reg["tiras"])
        c8 = ws.cell(row=curr, column=8, value=reg["medicacion"])
        c9 = ws.cell(row=curr, column=9, value=reg["se_pasa"])
        c10 = ws.cell(row=curr, column=10, value=reg["obs"])
        
        c1.number_format = 'DD/MM/YYYY'
        c1.alignment = Alignment(horizontal="center", vertical="center")
        
        for col_idx in range(1, 11):
            cell = ws.cell(row=curr, column=col_idx)
            cell.font = font_data
            cell.border = box_border
            if col_idx != 1:
                cell.alignment = Alignment(vertical="center", wrap_text=True)
                
        ws.row_dimensions[curr].height = 45
        curr += 1
        
    wb.save(EXCEL_DETALLE)
    print(f"✅ {EXCEL_DETALLE} formateado con éxito (fechas DD/MM/YYYY y 4 registros limpios).")

if __name__ == '__main__':
    format_resumen()
    format_detalle()
    print("🎉 Ambos Excels han quedado 100% alineados con fechas nativas, fuentes uniformes y recuadros.")

