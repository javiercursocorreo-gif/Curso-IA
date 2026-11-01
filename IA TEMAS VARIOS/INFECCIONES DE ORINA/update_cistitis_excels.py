#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_cistitis_excels.py
Actualiza automáticamente las dos hojas Excel de seguimiento en:
'IA TEMAS VARIOS/INFECCIONES DE ORINA/':
1. 'Seguimiento cistitis.xlsx' (Diario detallado con el episodio completo de octubre 2026).
2. 'Seguimiento cistitis resumen.xlsx' (Ficha ejecutiva para médicos, rescatando 2013-2014 y añadiendo 2026).
"""

import os
import sys

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
except ImportError:
    print("Instalando openpyxl...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/IA TEMAS VARIOS/INFECCIONES DE ORINA"
EXCEL_DETALLE = os.path.join(BASE_DIR, "Seguimiento cistitis.xlsx")
EXCEL_RESUMEN = os.path.join(BASE_DIR, "Seguimiento cistitis resumen.xlsx")

def update_resumen():
    print(f"--> Actualizando {EXCEL_RESUMEN}...")
    wb = openpyxl.load_workbook(EXCEL_RESUMEN)
    ws = wb.active
    
    # 1. Corregir y completar los primeros episodios (2013 - 2014)
    # Comprobar fila 4: tenía 41648 vacío
    # Añadir episodio 2013 antes de 2014 si no está
    # Vamos a leer todas las filas existentes
    rows_data = []
    for r in range(1, ws.max_row + 1):
        row_vals = [ws.cell(row=r, column=c).value for c in range(1, 9)]
        rows_data.append((r, row_vals))
    
    # Comprobar si 2013 ya existe
    has_2013 = any(r[1][0] == '2013' or r[1][0] == 2013 for r in rows_data)
    if not has_2013:
        # Insertar 2013 justo antes de la fila de 2014 (fila 3)
        ws.insert_rows(3, amount=2)
        # Fila 3: Cabecera 2013
        ws.cell(row=3, column=1, value="2013")
        ws.cell(row=3, column=1).font = Font(bold=True)
        # Fila 4: Episodio 01/07/2013 (41456)
        ws.cell(row=4, column=1, value=41456)
        ws.cell(row=4, column=2, value="Sin filiar")
        ws.cell(row=4, column=3, value="Monurol")
        ws.cell(row=4, column=4, value="—")
        ws.cell(row=4, column=5, value="Urgencias")
        ws.cell(row=4, column=6, value="Coito sin condón. Dolor e infección en urgencias")
    
    # Recalcular filas tras posible inserción
    # Buscar fila de 41648 que estaba vacía en medicamento/doctor y corregir con 01/01/2014 (41640)
    for r in range(1, ws.max_row + 1):
        val_a = ws.cell(row=r, column=1).value
        if val_a in [41648, "41648", 41640, "41640"]:
            ws.cell(row=r, column=1, value=41640)
            ws.cell(row=r, column=2, value="> 1.000.000 UFC")
            ws.cell(row=r, column=3, value="Monurol y luego Levofloxacino")
            ws.cell(row=r, column=4, value="1 semana")
            ws.cell(row=r, column=5, value="Urgencias")
            ws.cell(row=r, column=6, value="Coito sin condón. Nitritos negativo")
            break

    # 2. Localizar dónde empieza 'PRUEBAS REALIZADAS'
    pruebas_row = None
    for r in range(1, ws.max_row + 1):
        val = str(ws.cell(row=r, column=1).value or "").strip()
        if "PRUEBAS REALIZADAS" in val.upper():
            pruebas_row = r
            break
            
    if not pruebas_row:
        pruebas_row = ws.max_row + 1
        
    # Comprobar si 2026 ya está añadido
    has_2026 = False
    for r in range(1, ws.max_row + 1):
        if str(ws.cell(row=r, column=1).value or "").strip() == "2026":
            has_2026 = True
            break
            
    if not has_2026:
        # Insertar 4 filas antes de PRUEBAS REALIZADAS
        # Fila vacía, Cabecera 2026, Episodio 1 (14/10/2026), Episodio 2 (28/10/2026)
        insert_pos = pruebas_row
        ws.insert_rows(insert_pos, amount=4)
        
        # Fila separadora vacía
        # Fila 2026:
        r2026 = insert_pos + 1
        ws.cell(row=r2026, column=1, value="2026")
        ws.cell(row=r2026, column=1).font = Font(bold=True)
        
        # Fila Episodio 1 (14/10/2026 - Proteus):
        r_ep1 = r2026 + 1
        ws.cell(row=r_ep1, column=1, value=46309) # 14/10/2026
        ws.cell(row=r_ep1, column=2, value="Proteus mirabilis")
        ws.cell(row=r_ep1, column=3, value="1º Furantoína (petición propia) -> Ciprofloxacino")
        ws.cell(row=r_ep1, column=4, value="7días")
        ws.cell(row=r_ep1, column=5, value="Urg. La Moraleja / Dr. Membrillo")
        ws.cell(row=r_ep1, column=6, value="Dolor y escozor. Cultivo >100.000 UFC Proteus (resistencia natural a Furantoina). Dr. Membrillo receta Cipro 7d.")
        
        # Fila Episodio 2 (28/10/2026 - E. Coli):
        r_ep2 = r_ep1 + 1
        ws.cell(row=r_ep2, column=1, value=46323) # 28/10/2026
        ws.cell(row=r_ep2, column=2, value="E. Coli")
        ws.cell(row=r_ep2, column=3, value="Cefixima")
        ws.cell(row=r_ep2, column=4, value="7días")
        ws.cell(row=r_ep2, column=5, value="Urg. La Moraleja / Uróloga / Dr. Membrillo")
        ws.cell(row=r_ep2, column=6, value="Nuevo dolor. Uróloga receta Cefixima. Eco urológica Virgen del Mar. Cultivo cambia a E. Coli sensible Ceftazidima. Dr. Membrillo ratifica Cefixima 7d.")

    # 3. Añadir la Ecografía en PRUEBAS REALIZADAS si no está
    has_eco_2026 = False
    for r in range(1, ws.max_row + 1):
        val_a = str(ws.cell(row=r, column=1).value or "").strip()
        val_c = str(ws.cell(row=r, column=3).value or "").strip()
        val_d = str(ws.cell(row=r, column=4).value or "").strip()
        if "46323" in val_a and "ECO" in val_c.upper():
            has_eco_2026 = True
            break
            
    if not has_eco_2026:
        last_r = ws.max_row + 1
        ws.cell(row=last_r, column=1, value=46323)
        ws.cell(row=last_r, column=2, value="")
        ws.cell(row=last_r, column=3, value="ECO Urológica (Hosp. Virgen del Mar)")
        ws.cell(row=last_r, column=4, value="Pendiente resultado")
        ws.cell(row=last_r, column=5, value="Uróloga La Moraleja")
        ws.cell(row=last_r, column=6, value="Realizada el 28/10/2026 tras consulta")

    wb.save(EXCEL_RESUMEN)
    print(f"✅ {EXCEL_RESUMEN} guardado y actualizado con éxito.")


def update_detalle():
    print(f"--> Actualizando {EXCEL_DETALLE}...")
    wb = openpyxl.load_workbook(EXCEL_DETALLE)
    ws = wb.active
    
    # Columnas:
    # A: Fecha (serial)
    # B: causa
    # C: síntoma
    # D: Infección
    # E: vamos a urgencias
    # F: Resultados
    # G: Positivo en las tiras de casa
    # H: medicación
    # I: se pasa en
    # J: Observaciones

    # Buscar las filas recientes de octubre 2026 (46309 en adelante)
    rows_to_clean = []
    for r in range(1, ws.max_row + 1):
        val_a = ws.cell(row=r, column=1).value
        if val_a in [46309, 46312, 46313, 46323, 46326, "46309", "46312", "46313", "46323", "46326"]:
            rows_to_clean.append(r)
            
    # Si existen filas parciales al final, las ajustamos de forma ordenada
    start_r = rows_to_clean[0] if rows_to_clean else ws.max_row + 1
    
    # Escribimos los registros cronológicos completos del brote de octubre 2026:
    registros = [
        # 14/10/2026 - Inicio Episodio 1
        {
            "fecha": 46309,
            "causa": "desconocida",
            "sintoma": "dolor, escozor y muchas ganas de orinar",
            "infeccion": "si",
            "urgencias": "si. Hospital La Moraleja (Dra. García Ron)",
            "resultados": "Sistemático de orina positivo (pH 8.5, Nitritos +, Leucocitos 3+, piuria, bacteriuria). Se encarga cultivo",
            "tiras": "si",
            "medicacion": "Furantoina por petición nuestra (en urgencias querían Cefixima)",
            "se_pasa": "mejora en 3-4 días",
            "obs": "Escribimos por email al Dr. Membrillo (Medicina Interna) que lleva el seguimiento de cistitis de repetición. Dice que OK y que le escribamos cuando esté el cultivo."
        },
        # 17/10/2026 - Cultivo Proteus y prescripción Dr. Membrillo
        {
            "fecha": 46312,
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
        # 28/10/2026 - Recurrencia y Segundo Episodio
        {
            "fecha": 46323,
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
        # 31/10/2026 - Cultivo E. Coli y Ratificación Dr. Membrillo
        {
            "fecha": 46326,
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
    
    # Escribir registros en start_r en adelante
    curr_r = start_r
    for reg in registros:
        ws.cell(row=curr_r, column=1, value=reg["fecha"])
        ws.cell(row=curr_r, column=2, value=reg["causa"])
        ws.cell(row=curr_r, column=3, value=reg["sintoma"])
        ws.cell(row=curr_r, column=4, value=reg["infeccion"])
        ws.cell(row=curr_r, column=5, value=reg["urgencias"])
        ws.cell(row=curr_r, column=6, value=reg["resultados"])
        ws.cell(row=curr_r, column=7, value=reg["tiras"])
        ws.cell(row=curr_r, column=8, value=reg["medicacion"])
        ws.cell(row=curr_r, column=9, value=reg["se_pasa"])
        ws.cell(row=curr_r, column=10, value=reg["obs"])
        curr_r += 1
        
    wb.save(EXCEL_DETALLE)
    print(f"✅ {EXCEL_DETALLE} guardado y actualizado con éxito.")

if __name__ == '__main__':
    update_resumen()
    update_detalle()
    print("🎉 Ambas hojas de cálculo han sido sincronizadas y actualizadas correctamente.")

