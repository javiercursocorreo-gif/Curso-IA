#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_029.py
Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-029_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
Sesión 29: Experimento de la Doble Rendija y Dualidad Onda-Partícula 3D (Young / Davisson-Germer)
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/29_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-029_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/29_COD-029_Taller_Simulador_Doble_Rendija_3D.pdf"

def build_cod_029_taller_3d_pdf(output_path=PDF_PATH):
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
        Paragraph("<b>[COD-029] Taller: Crea tu propio simulador 3D de la Doble Rendija Cuántica</b>", style_title),
        Paragraph("💡 <b>Misión Didáctica • Dualidad Onda-Partícula y el Colapso de la Función de Onda:</b>", style_section_h),
        Paragraph("En este taller ordenarás a Gemini construir un simulador de física cuántica 3D del legendario <b>Experimento de la Doble Rendija de Thomas Young</b> (1801) y su demostración cuántica con electrones individuales (Davisson-Germer, 1927). Descubrirás el misterio del <b>efecto observador</b>: sin detector, cada fotón/electrón actúa como onda y forma franjas de interferencia; con detector activo, la onda colapsa y se comporta como partículas clásicas. <b>No requieres saber programar:</b> copia el prompt y ejecútalo.", style_body)
    ]

    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> Abre Gemini (<i>gemini.google.com</i>). Copia el Prompt Maestro inferior, pégalo y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado:</b> Pulsa <b>«Copiar código»</b> en la esquina superior del bloque HTML de Gemini.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller de Pruebas (Pestaña 2):</b> En el mapa de la Sesión 29, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y ejecuta:</b> Pega el código con <b>Ctrl+V</b> y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Verás el cañón de partículas y la pantalla!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Prueba la Demo Oficial:</b> Pulsa <b>«🔬 Abrir Doble Rendija 3D ↗»</b> en el mapa para activar el detector cuántico y escuchar la síntesis de voz.", style_task)]
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
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo del Experimento de la Doble Rendija y Dualidad Onda-Partícula (Registro Hitachi de Akira Tonomura 1989).<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Modela con precisión física: cañón de emisión de campo de 50 kV (λ de De Broglie = 0.0054 nm), biprisma electrostático con dos rendijas, detector microcanal de fósforo y muestreo Monte Carlo de impactos discretos según P(y) = |Ψ₁ + Ψ₂|².<br/>"
        "3. Incluye modos de disparo cuántico: individual 1 a 1, ráfaga continua y saltos a N=100, 3000, 20000 y 70000 impactos para reproducir exactamente la emergencia gradual de las franjas de Young.<br/>"
        "4. Añade conmutador de detector de trayectoria ('Which-Way'): al activarlo, colapsa la función de onda y transforma las franjas de interferencia en dos distribuciones gaussianas clásicas.<br/>"
        "5. Integra botón de telemetría histórica con las micrografías originales de Tonomura (1989) y perfil de intensidad |Ψ|² en tiempo real.<br/>"
        "6. Aplica diseño en modo oscuro (#01040a) con tipografía grande (16-18px), KPIs de conteo N y síntesis de voz en español.<br/>"
        "7. Escribe exclusivamente el código sin texto explicativo.\"</i>"
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
    story.append(Paragraph("👉 <b>¡Pídele a Gemini que modifique tu código!</b> En la misma conversación dile: <i>«Cambia la longitud de onda de 532 nm (verde) a 650 nm (rojo) y aumenta la separación de rendijas a 0.5 mm para ver cómo se ensanchan las franjas de interferencia»</i>. ¡Copia el código y compruébalo en tu Taller!", style_body))
    story.append(Spacer(1, 2))

    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Física cuántica y registro histórico (<i>Akira Tonomura, Hitachi 1989 / Longitud de onda de De Broglie</i>):</b> Cada electrón individual se difracta consigo mismo con longitud de onda λ = h/p = 5.4 pm (a 50 kV).<br/>"
        "• <b>Simulación Estocástica y Acumulación de Impactos:</b> Muestreo de Monte Carlo por rechazo sobre la función de onda |Ψ₁ + Ψ₂|² para acumular hasta 70,000 impactos discretos sobre la placa de fósforo y colapso de von Neumann al encender el detector."
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
    print(f"✅ PDF COD-029 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try: build_cod_029_taller_3d_pdf()
    except Exception as e: print(f"❌ Error al generar PDF COD-029: {e}"); sys.exit(1)

