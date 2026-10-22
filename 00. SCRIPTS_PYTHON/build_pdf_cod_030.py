#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_030.py
Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-030_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
Sesión 30: Computación Cuántica, Qubits y Esfera de Bloch 3D (Félix Bloch / IBM Quantum)
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/30_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-030_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/30_COD-030_Taller_Simulador_Computacion_Cuantica_3D.pdf"

def build_cod_030_taller_3d_pdf(output_path=PDF_PATH):
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
        Paragraph("<b>[COD-030] Taller: Crea tu propio simulador 3D de Computación Cuántica y Qubits</b>", style_title),
        Paragraph("💡 <b>Misión Didáctica • Superposición, Puertas Lógicas Cuánticas y Esfera de Bloch:</b>", style_section_h),
        Paragraph("En este taller ordenarás a Gemini construir un simulador de computación cuántica en 3D basado en la <b>Esfera de Bloch</b> (Premio Nobel Félix Bloch). A diferencia de un bit tradicional que solo vale 0 o 1, un <b>qubit</b> vive en superposición cuántica |ψ⟩ = α|0⟩ + β|1⟩ como un vector tridimensional sobre la superficie de una esfera. Aplicarás puertas cuánticas como <b>Hadamard (H)</b>, <b>Pauli-X (NOT)</b> y <b>Pauli-Z</b>, y ejecutarás mediciones proyectivas con colapso probabilístico. <b>No requieres saber programar:</b> copia el prompt y ejecútalo.", style_body)
    ]

    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> Abre Gemini (<i>gemini.google.com</i>). Copia el Prompt Maestro inferior, pégalo y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado:</b> Pulsa <b>«Copiar código»</b> en la esquina superior del bloque HTML de Gemini.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller de Pruebas (Pestaña 2):</b> En el mapa de la Sesión 30, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y ejecuta:</b> Pega el código con <b>Ctrl+V</b> y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Verás el vector de estado en 3D!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Prueba la Demo Oficial:</b> Pulsa <b>«⚛️ Abrir Computador Cuántico 3D ↗»</b> en el mapa para colapsar qubits con medición y audio.", style_task)]
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
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D de Computación Cuántica y Esfera de Bloch.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Incluye en la cabecera el script con las matrices cuánticas oficiales de IBM Quantum:<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/bloch_sphere_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Modela con Babylon.js una Esfera de Bloch semitransparente con rejilla de paralelos/meridianos, ejes cartesianos X, Y, Z con flechas direccionales, polos |0⟩ (Zenit) y |1⟩ (Nadir), estados ecuatoriales |+⟩, |-⟩, |i⟩, |-i⟩, y un vector de estado cuántico animado (flecha PBR luminiscente).<br/>"
        "4. Incluye un panel de control interactivo con puertas lógicas cuánticas: Hadamard (H para entrar en superposición 50/50), Pauli-X (NOT cuántico), Pauli-Y, Pauli-Z, y botón 'Medir Qubit' que proyecta el estado a |0⟩ o |1⟩ según probabilidades Born |α|² y |β|².<br/>"
        "5. Aplica diseño en modo oscuro (#030614) con tipografía grande (16-18px), probabilidades |0⟩ y |1⟩ en KPIs en tiempo real y síntesis de voz en español.<br/>"
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
    story.append(Paragraph("👉 <b>¡Pídele a Gemini que modifique tu código!</b> En la misma conversación dile: <i>«Añade una puerta de fase S (rotación de 90° alrededor del eje Z) y un circuito de entrelazamiento cuántico (Bell State |Φ+⟩ = (|00⟩+|11⟩)/√2)»</i>. ¡Copia el código y compruébalo en tu Taller!", style_body))
    story.append(Spacer(1, 2))

    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Mecánica cuántica y álgebra lineal (<i>Félix Bloch 1946 / IBM Quantum Qiskit</i>):</b> El estado puro |ψ⟩ se mapea como punto sobre S² con coordenadas (sinθ·cosφ, sinθ·sinφ, cosθ). La regla de Born fija P(0)=cos²(θ/2) y P(1)=sin²(θ/2).<br/>"
        "• <b>Montaje en Babylon.js:</b> Se construye una esfera PBR translúcida con líneas geodésicas. Las puertas operan sobre el vector de estado aplicando cuaterniones de rotación continua interpolada (Slerp), ofreciendo animación suave sin saltos bruscos."
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
    print(f"✅ PDF COD-030 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try: build_cod_030_taller_3d_pdf()
    except Exception as e: print(f"❌ Error al generar PDF COD-030: {e}"); sys.exit(1)

