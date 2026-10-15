#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_002b.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-002B_Taller_Mainframe_COBOL_CICS_DB2_3270.pdf
para la Sesión 02 del Curso de IA (Core Bancario Mainframe COBOL, CICS y DB2 con Terminal 3270).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/02_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-002B_Taller_Mainframe_COBOL_CICS_DB2_3270.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/02B_COD-002B_Taller_Simulador_Mainframe_COBOL_CICS.pdf"

def build_cod_002b_taller_mainframe_pdf(output_path=PDF_PATH):
    dest_path = output_path
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as _:
            pass
    except Exception:
        dest_path = LOCAL_BACKUP
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(
        dest_path,
        pagesize=letter,
        rightMargin=36, leftMargin=36, topMargin=20, bottomMargin=18
    )
    styles = getSampleStyleSheet()
    
    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0,
        textColor=colors.HexColor('#0284C7'), alignment=1, spaceAfter=1
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=3
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=11.2, leading=13.5,
        textColor=colors.HexColor('#0F172A'), spaceAfter=2
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=8.5, leading=10.8,
        textColor=colors.HexColor('#0369A1'), spaceBefore=2, spaceAfter=2
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=7.6, leading=9.8,
        textColor=colors.HexColor('#1E293B'), spaceAfter=2
    )
    style_task = ParagraphStyle(
        'TaskStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.4, leading=9.6,
        textColor=colors.HexColor('#0F172A')
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.1, leading=9.1,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0284C7'), spaceAfter=3))

    story.append(Paragraph("<b>[COD-002B] Taller Especial: Core Bancario Mainframe COBOL, CICS y DB2</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Cómo Funciona la Banca Real por Dentro y el Poder de la IA:</b>", style_section_h))
    story.append(Paragraph(
        "Más del 70% de las transacciones bancarias del planeta se ejecutan sobre sistemas <b>Mainframe IBM z/OS</b> en lenguaje <b>COBOL</b>. "
        "En esta práctica experimentarás con una arquitectura bancaria crítica completa: el terminal verde <b>IBM 3270</b>, el servidor transaccional <b>CICS</b> y la base de datos <b>DB2</b>. "
        "Comprobarás cómo la IA genera en 10 segundos soluciones empresariales que antes requerían días de compilaciones, y podrás <b>modificar el código COBOL en vivo</b> para alterar las reglas de negocio.",
        style_body
    ))

    # Lista de Tareas
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en el Simulador y en Gemini):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Abre el Simulador Mainframe en el Mapa:</b> En el mapa de la Sesión 02, pulsa <b>«🖥️ Abrir Simulador Mainframe 3270 & COBOL ↗»</b> para acceder al laboratorio.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Ejecuta una Transacción Bancaria Real:</b> En la pantalla 3270, selecciona una cuenta bancaria (Solvente, En Descubierto o Bloqueada) y pulsa <b>«⚡ ENTER (Transmitir)»</b>. Observa cómo viaja el paquete por la red hasta CICS y DB2.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Modifica las Reglas en el Playground COBOL:</b> En el editor COBOL de la derecha, cambia el literal de <i>WS-MENSAJE-RESPUESTA</i> o altera el límite de saldo. Pulsa <b>«⚙️ Compilar & Transmitir a CICS»</b> y observa cómo el terminal verde refleja tus cambios.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • El Guiño para Expertos (Provocar un ABEND):</b> Carga el Preset 4 <i>«Provocar ABEND ASRA»</i>. Pulsa Compilar y comprueba cómo CICS intercepta la excepción de datos decimales empaquetados en tiempo real.", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Genera tu propia transacción con Gemini:</b> Pulsa el botón <b>«✨ Ver Prompt Maestro»</b>, copia el texto y pégalo en Gemini (<i>gemini.google.com</i>). ¡Obtendrás el mapa BMS y el código COBOL completo al instante!", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0284C7')),
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_table)
    story.append(Spacer(1, 2))

    # Prompt Maestro
    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini / Claude:</b>", style_section_h))
    prompt_text = (
        "<b>Copia exactamente este texto en Gemini:</b><br/>"
        "<i>\"Actúa como un Ingeniero Principal de Sistemas Mainframe IBM z/OS experto en COBOL, CICS Transaction Server y DB2.<br/>"
        "Genera una solución bancaria completa para la transacción de consulta de saldo 'INQS' (Inquire Account Balance):<br/>"
        "1. MAPA BMS (Basic Mapping Support): Pantalla 3270 (24x80) con campos de cabecera protegidos, campo de entrada de 14 dígitos para NUM_CUENTA (desprotegido, alta intensidad), campos de salida para NOMBRE_TITULAR, SALDO_DISPONIBLE, MENSAJE_ERROR y teclas PF/ENTER.<br/>"
        "2. PROGRAMA COBOL CICS + SQL DB2 (INQSALDO.cbl): Estructura ANSI 85 con IDENTIFICATION, ENVIRONMENT, DATA y PROCEDURE DIVISION. LINKAGE y WORKING-STORAGE con SQLCA. Lógica pseudo-conversacional evaluando EIBCALEN y EIBAID. Consulta EXEC SQL SELECT ... INTO ... FROM TB_CUENTAS WHERE NUM_CUENTA = :WS-CUENTA. Tratamiento de SQLCODE = 0 (Éxito), +100 (No encontrado) y &lt; 0 (Error). Envío con EXEC CICS SEND MAP.<br/>"
        "3. EXPLICACIÓN DIDÁCTICA: Resumen en 3 viñetas del ciclo de vida de la transacción para explicarlo a personas que nunca han visto un Mainframe.\"</i>"
    )
    p_table = Table([[Paragraph(prompt_text, style_prompt)]], colWidths=[letter[0] - 72])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 2))

    # Apartado Técnico
    story.append(Paragraph("🔬 <b>Arquitectura Empresarial • ¿Por qué los Bancos siguen usando Mainframes y COBOL?</b>", style_section_h))
    tech_text = (
        "• <b>Fiabilidad insuperable y latencia cero:</b> Los Mainframes IBM z16 procesan más de 30.000 transacciones CICS por segundo con una disponibilidad del 99.99999% (menos de 3 segundos de parada por año). COBOL maneja aritmética decimal exacta sin errores de redondeo de coma flotante.<br/>"
        "• <b>El papel de la Inteligencia Artificial:</b> La IA generativa no busca reemplazar estos sistemas críticos, sino documentarlos, asistir en su modernización, generar interfaces API REST sobre CICS y permitir a cualquier programador comprender y mantener décadas de lógica financiera de misión crítica en cuestión de segundos."
    )
    tech_table = Table([[Paragraph(tech_text, style_task)]], colWidths=[letter[0] - 72])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#059669')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(tech_table)

    doc.build(story)
    if dest_path != LOCAL_BACKUP:
        try:
            import shutil
            os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
            shutil.copy2(dest_path, LOCAL_BACKUP)
        except Exception:
            pass
    print(f"✅ PDF COD-002B generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_002b_taller_mainframe_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-002B: {e}")
        sys.exit(1)

