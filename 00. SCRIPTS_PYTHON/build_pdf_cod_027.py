#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_027.py
Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-027_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
Sesión 27: Estructura del Átomo & Orbitales Cuánticos 3D
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/27_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-027_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/27_COD-027_Taller_Simulador_Atomo_Cuantico_3D.pdf"

def build_cod_027_taller_3d_pdf(output_path=PDF_PATH):
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

    style_header = ParagraphStyle('HStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.0, textColor=colors.HexColor('#0284C7'), alignment=1, spaceAfter=1)
    style_block = ParagraphStyle('BStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.8, textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4)
    style_title = ParagraphStyle('TStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=11.6, leading=14.0, textColor=colors.HexColor('#0F172A'), spaceAfter=3)
    style_section_h = ParagraphStyle('SecStyle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=8.8, leading=11.2, textColor=colors.HexColor('#0369A1'), spaceBefore=3, spaceAfter=2)
    style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=7.8, leading=10.4, textColor=colors.HexColor('#1E293B'), spaceAfter=2)
    style_task = ParagraphStyle('TaskStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=7.6, leading=10.0, textColor=colors.HexColor('#0F172A'))
    style_prompt = ParagraphStyle('PromptStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=7.3, leading=9.7, textColor=colors.HexColor('#0F172A'))

    story = [
        Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header),
        Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block),
        HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0284C7'), spaceAfter=4),
        Paragraph("<b>[COD-027] Taller: Crea tu propio simulador 3D del Átomo & Orbitales Cuánticos</b>", style_title),
        Paragraph("💡 <b>Misión Didáctica • Nubes de Probabilidad |ψ|² y Ecuación de Schrödinger con Gemini:</b>", style_section_h),
        Paragraph("En este taller ordenarás a Gemini crear un simulador 3D de la <b>estructura cuántica del átomo</b>: desmitificarás el modelo planetario obsoleto de órbitas rígidas y explorarás las verdaderas <b>nubes de densidad de probabilidad |ψ|²</b> y armónicos esféricos. Visualizarás el orbital esférico <b>1s</b>, el orbital <b>2s</b> con nodo radial interno, los lóbulos de <b>2px/2pz</b> y los orbitales complejos <b>3d</b>. <b>No requieres saber programar:</b> copia el prompt y ejecútalo.", style_body)
    ]

    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> Abre Gemini (<i>gemini.google.com</i>). Copia el Prompt Maestro inferior, pégalo y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado:</b> Pulsa <b>«Copiar código»</b> en la esquina superior del bloque HTML de Gemini.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller de Pruebas (Pestaña 2):</b> En el mapa de la Sesión 27, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y ejecuta:</b> Pega el código con <b>Ctrl+V</b> y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Los orbitales cuánticos aparecerán en 3D!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Prueba la Demo Oficial:</b> Pulsa <b>«⚛️ Abrir Átomo Cuántico 3D ↗»</b> en el mapa para alternar entre orbitales 1s, 2s, 2p y 3d.", style_task)]
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#38BDF8')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(t_table)
    story.append(Spacer(1, 3))

    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_text = (
        "<b>Copia exactamente este texto en Gemini:</b><br/>"
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un visor interactivo 3D de la Estructura del Átomo y Orbitales Cuánticos con la Ecuación de Schrödinger.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Incluye en la cabecera el script con los datos cuánticos reales:<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/quantum_atom_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Modela con Babylon.js un núcleo atómico central de protones (rojos) y neutrones (grises), rodeado por nubes de probabilidad cuántica semitransparentes PBR con código de fases (fase positiva cian, fase negativa ámbar).<br/>"
        "4. Incluye botones para seleccionar y renderizar dinámicamente los orbitales 1s (esférico), 2s (con nodo interno), 2pz, 2px, 3d z² (con toroide ecuatorial) y 3d xy (trébol).<br/>"
        "5. Aplica un diseño en modo oscuro (#030612) con tipografía grande (16-18px), números cuánticos en KPIs (n, l, m, s) y síntesis de voz en español.<br/>"
        "6. Escribe exclusivamente el código sin explicaciones añadidas.\"</i>"
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
    story.append(Paragraph("👉 <b>¡Pídele a Gemini que modifique tu código!</b> En la misma conversación dile: <i>«Añade una tarjeta que explique el Principio de Incertidumbre de Heisenberg: por qué jamás podemos saber a la vez la posición exacta y la velocidad de un electrón»</i>. ¡Copia el código y compruébalo en tu Taller!", style_body))
    story.append(Spacer(1, 2))

    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de las funciones de onda (<i>Erwin Schrödinger / Max Born</i>):</b> Las formas de los orbitales son los armónicos esféricos Y_lm(θ, φ) calculados analíticamente para el potencial electrostático del átomo de hidrógeno.<br/>"
        "• <b>Montaje en Babylon.js:</b> Los parámetros cuánticos se importan de <i>quantum_atom_b64.js</i>. Babylon.js instancia elipsóides y toroides PBR con valores alfa de translucidez para representar la nube volumétrica de densidad |ψ|²."
    )
    tech_table = Table([[Paragraph(tech_text, style_task)]], colWidths=[letter[0] - 72])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0284C7')),
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
    print(f"✅ PDF COD-027 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try: build_cod_027_taller_3d_pdf()
    except Exception as e: print(f"❌ Error al generar PDF COD-027: {e}"); sys.exit(1)

