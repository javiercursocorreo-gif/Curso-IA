#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_028.py
Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-028_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
Sesión 28: Tabla Periódica Interactiva y Enlaces Químicos 3D (IUPAC / VSEPR)
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/28_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-028_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/28_COD-028_Taller_Simulador_Tabla_Periodica_3D.pdf"

def build_cod_028_taller_3d_pdf(output_path=PDF_PATH):
    dest_path = output_path
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as _: pass
    except Exception:
        dest_path = LOCAL_BACKUP
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(dest_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=22, bottomMargin=20)
    styles = getSampleStyleSheet()

    style_header = ParagraphStyle('HStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.0, textColor=colors.HexColor('#059669'), alignment=1, spaceAfter=1)
    style_block = ParagraphStyle('BStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.8, textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4)
    style_title = ParagraphStyle('TStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=11.6, leading=14.0, textColor=colors.HexColor('#0F172A'), spaceAfter=3)
    style_section_h = ParagraphStyle('SecStyle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=8.8, leading=11.2, textColor=colors.HexColor('#047857'), spaceBefore=3, spaceAfter=2)
    style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=7.8, leading=10.4, textColor=colors.HexColor('#1E293B'), spaceAfter=2)
    style_task = ParagraphStyle('TaskStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=7.6, leading=10.0, textColor=colors.HexColor('#0F172A'))
    style_prompt = ParagraphStyle('PromptStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=7.3, leading=9.7, textColor=colors.HexColor('#0F172A'))

    story = [
        Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header),
        Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block),
        HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#059669'), spaceAfter=4),
        Paragraph("<b>[COD-028] Taller: Crea tu propio simulador 3D de la Tabla Periódica & Enlaces</b>", style_title),
        Paragraph("💡 <b>Misión Didáctica • Geometría Molecular VSEPR y Enlaces Químicos con Gemini:</b>", style_section_h),
        Paragraph("En este taller ordenarás a Gemini construir un simulador químico en 3D de la <b>Tabla Periódica oficial de la IUPAC</b> y los tres grandes tipos de enlaces moleculares: el enlace <b>covalente polar del agua (H2O, ángulo 104.5°)</b>, el enlace <b>covalente apolar tetraédrico del metano (CH4, 109.5°)</b> y la <b>red iónica cristalina del cloruro de sodio (NaCl)</b>, junto a la espiral periódica continua de los 118 elementos. <b>No requieres saber programar:</b> copia el prompt y ejecútalo.", style_body)
    ]

    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> Abre Gemini (<i>gemini.google.com</i>). Copia el Prompt Maestro inferior, pégalo y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado:</b> Pulsa <b>«Copiar código»</b> en la esquina superior del bloque HTML de Gemini.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller de Pruebas (Pestaña 2):</b> En el mapa de la Sesión 28, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y ejecuta:</b> Pega el código con <b>Ctrl+V</b> y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Las moléculas 3D girarán en pantalla!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Prueba la Demo Oficial:</b> Pulsa <b>«🧪 Abrir Tabla Periódica 3D ↗»</b> en el mapa para inspeccionar la red cúbica del NaCl y los 118 elementos.", style_task)]
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#34D399')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(t_table)
    story.append(Spacer(1, 3))

    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_text = (
        "<b>Copia exactamente este texto en Gemini:</b><br/>"
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un visor interactivo 3D de Cristalografía, Enlaces Químicos y Redes Moleculares IUPAC.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Modela con Canvas 2D/3D fotorrealista PBR interactivo: red cúbica FCC de NaCl (27 iones Na+/Cl- con plano Miller 001), molécula de agua H2O polar (104.5° con nubes de pares libres sp³), metano CH4 (tetraedro 109.5°), red de diamante C tridimensional, CO2 lineal (180°) y NH3 piramidal (107.8°).<br/>"
        "3. Incluye botones interactivos para alternar entre estructuras químicas, rotación orbital 3D con ratón y conmutadores de planos cristalográficos y dipolos.<br/>"
        "4. Integra un botón modal de telemetría analítica con difractograma XRD de polvo (Ley de Bragg nλ = 2d·sen θ) y escala periódica de electronegatividad de Pauling (IUPAC).<br/>"
        "5. Aplica un diseño en modo oscuro (#02040a) con tipografía grande (16-18px), KPIs de tipo de enlace, ángulo, distancia y diferencia Pauling Δχ, y síntesis de voz en español.<br/>"
        "6. Escribe exclusivamente el código sin texto explicativo.\"</i>"
    )
    p_table = Table([[Paragraph(prompt_text, style_prompt)]], colWidths=[letter[0] - 72])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5), ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(p_table)
    story.append(Spacer(1, 3))

    story.append(Paragraph("🌟 <b>El Reto Extra (Para Alumnos Curiosos):</b>", style_section_h))
    story.append(Paragraph("👉 <b>¡Pídele a Gemini que modifique tu código!</b> En la misma conversación dile: <i>«Añade una molécula de Dióxido de Carbono (CO2) lineal a 180° y explica por qué no tiene polaridad a pesar de tener enlaces polares»</i>. ¡Copia el código y compruébalo en tu Taller!", style_body))
    story.append(Spacer(1, 2))

    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de las estructuras químicas (<i>IUPAC / Teoría VSEPR de Gillespie-Nyholm</i>):</b> Las posiciones atómicas, distancias (d = 2.82 Å) y ángulos de enlace (104.5° y 109.5°) proceden de la cristalografía de rayos X y repulsión electrostática de pares de electrones.<br/>"
        "• <b>Motor Gráfico y Cristalografía Computacional:</b> Proyección tridimensional interactiva con sombreado esférico fotorrealista PBR, rotación Euler, planos de Miller (001), nubes de pares solitarios sp³ y espectrograma XRD con picos Bragg."
    )
    tech_table = Table([[Paragraph(tech_text, style_task)]], colWidths=[letter[0] - 72])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#059669')),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(tech_table)

    doc.build(story)
    if dest_path != LOCAL_BACKUP:
        try:
            import shutil
            os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
            shutil.copy2(dest_path, LOCAL_BACKUP)
        except Exception: pass
    print(f"✅ PDF COD-028 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try: build_cod_028_taller_3d_pdf()
    except Exception as e: print(f"❌ Error al generar PDF COD-028: {e}"); sys.exit(1)

