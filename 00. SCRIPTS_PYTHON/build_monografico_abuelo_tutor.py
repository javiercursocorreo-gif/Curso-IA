# -*- coding: utf-8 -*-
"""
Generador de la Ficha Didáctica del Monográfico 5:
«EL ABUELO TUTOR: Ayuda a tus Nietos en Matemáticas e Historia con IA y NotebookLM»
Genera:
- FICHA_MONOGRAFICO_EL_ABUELO_TUTOR.docx
- FICHA_MONOGRAFICO_EL_ABUELO_TUTOR.pdf
en CLASES/5. EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import cm

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(ROOT_DIR, "CLASES", "5. EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA")
TARGET_DOCX = os.path.join(TARGET_DIR, "FICHA_MONOGRAFICO_EL_ABUELO_TUTOR.docx")
TARGET_PDF = os.path.join(TARGET_DIR, "FICHA_MONOGRAFICO_EL_ABUELO_TUTOR.pdf")

os.makedirs(TARGET_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# UTILIDADES DOCX
# ---------------------------------------------------------------------------
def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_callout_box(doc, title_text, body_paragraphs, border_color="0B4F6C", bg_color="F0F7FA"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)

    cell = table.cell(0, 0)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=160, bottom=160, left=220, right=220)

    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:top w:val="none"/>'
        f'  <w:left w:val="single" w:sz="30" w:space="0" w:color="{border_color}"/>'
        f'  <w:bottom w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

    p_title = cell.paragraphs[0]
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    run_t = p_title.add_run(title_text)
    run_t.bold = True
    run_t.font.name = "Calibri"
    run_t.font.size = Pt(11)
    run_t.font.color.rgb = RGBColor.from_string(border_color)

    for body_text in body_paragraphs:
        p_body = cell.add_paragraph()
        p_body.paragraph_format.space_before = Pt(0)
        p_body.paragraph_format.space_after = Pt(3)
        run_b = p_body.add_run(body_text)
        run_b.font.name = "Calibri"
        run_b.font.size = Pt(10)
        run_b.font.color.rgb = RGBColor(40, 50, 60)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

# ---------------------------------------------------------------------------
# GENERADOR DOCX
# ---------------------------------------------------------------------------
def generate_docx():
    print("📝 Generando Ficha del Monográfico 5 en DOCX...")
    doc = docx.Document()

    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)

    C_NAVY = RGBColor(11, 37, 69)      # #0B2545
    C_BLUE = RGBColor(0, 102, 161)     # #0066A1
    C_DARK = RGBColor(33, 37, 41)
    C_MUTED = RGBColor(100, 116, 139)

    # Cabecera
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(9.5)
    r_inst.font.bold = True
    r_inst.font.color.rgb = C_BLUE

    p_main = doc.add_paragraph()
    p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main.paragraph_format.space_after = Pt(4)
    r_main = p_main.add_run("MONOGRÁFICO 5: EL ABUELO TUTOR")
    r_main.font.name = "Calibri"
    r_main.font.size = Pt(20)
    r_main.font.bold = True
    r_main.font.color.rgb = C_NAVY

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("Cómo Explicar Matemáticas con Claridad y Transformar Apuntes de Historia en Fichas Escolares Imprimibles")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = C_MUTED

    # Cuadro de enfoque
    add_callout_box(
        doc,
        "🎯 El Nuevo Rol del Abuelo en la Era Digital",
        [
            "Muchos nietos se atascan con las matemáticas o se aburren con la historia porque los libros son áridos o sus profesores van demasiado rápido.",
            "Los abuelos tienen el ingrediente pedagógico más valioso del mundo: paciencia, tiempo libre y cariño sin la presión del día a día.",
            "En este taller aprenderás a usar la IA y nuestra aplicación interactiva «El Abuelo Tutor» para resolver dudas de matemáticas paso a paso y convertir fotos de libros en cuadernillos y tarjetas de juego impresas en papel."
        ],
        border_color="0066A1",
        bg_color="F0F7FC"
    )

    # Sección 1
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(12)
    p_h1.paragraph_format.space_after = Pt(6)
    r = p_h1.add_run("1. Módulo de Matemáticas: La Técnica de las 4 Capas Pedagógicas")
    r.font.name = "Calibri"
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.add_run("Cuando un niño dice «no entiendo las matemáticas», casi nunca es falta de inteligencia, sino que le han soltado la fórmula antes de que entienda la idea. En la aplicación ")
    p.add_run("«El Abuelo Tutor»").bold = True
    p.add_run(", cualquier problema introducido en el cuadro libre se descompone automáticamente en 4 niveles:")

    pasos_mates = [
        ("🌟 Nivel 1: Para comprenderlo (La analogía cotidiana)", "Una metáfora sencilla sin números que despierta la intuición (por ejemplo, una balanza en equilibrio o dos amigos caminando en una cinta métrica)."),
        ("🧠 Nivel 2: El paso a paso razonado (El puente lógico)", "La explicación detallada de cada movimiento sin dar nada por sentado, eliminando los 'saltos mágicos' que confunden a los alumnos."),
        ("📝 Nivel 3: Para el examen del colegio (El rigor formal)", "El desarrollo algebraico estricto con las fórmulas del currículo escolar para que el profesor le ponga la máxima calificación."),
        ("🎯 Nivel 4: El Reto Gemelo (Problema espejo)", "Un problema exactamente igual pero con números cambiados para que el nieto lo resuelva a solas a lápiz y demuestre que lo ha asimilado.")
    ]

    for tit, desc in pasos_mates:
        p_item = doc.add_paragraph()
        p_item.paragraph_format.left_indent = Inches(0.2)
        p_item.paragraph_format.space_after = Pt(3)
        r_t = p_item.add_run(tit + ": ")
        r_t.bold = True
        r_t.font.color.rgb = C_BLUE
        p_item.add_run(desc).font.color.rgb = C_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Sección 2
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(12)
    p_h1.paragraph_format.space_after = Pt(6)
    r = p_h1.add_run("2. Módulo de Historia y Ciencias: El Puente NotebookLM a Ficha Escolar")
    r.font.name = "Calibri"
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.add_run("Google NotebookLM es el archivador más potente del mundo: tu nieto te pasa por WhatsApp 2 fotos de las páginas de su libro de Historia o de sus apuntes manuscritos, las subes a Fuentes y NotebookLM las analiza con rigor absoluto sin inventar nada. ").font.color.rgb = C_DARK
    p.add_run("Pero tiene un defecto: ¡no permite guardar ni imprimir un PDF bonito con formato escolar!").bold = True

    add_callout_box(
        doc,
        "🖨️ CÓMO SOLUCIONA ESTO LA APP «EL ABUELO TUTOR»",
        [
            "1. En NotebookLM: En Studio, pulsa los botones «Preguntas frecuentes» (FAQ), «Guía de estudio» y «Línea de tiempo».",
            "2. Copias esos textos y los pegas en el Módulo 2 de nuestra App.",
            "3. Pulsas «Generar Cuadernillo Escolar»: La aplicación genera automáticamente:",
            "   • Un Examen con líneas punteadas para que el nieto responda a mano con bolígrafo o lápiz.",
            "   • Un juego de Tarjetas de Memoria Recortables (Flashcards) para jugar al trivial de preguntas y respuestas en el salón.",
            "   • Una Hoja de Soluciones oficial y privada para que el abuelo corrija con total seguridad."
        ],
        border_color="0B7285",
        bg_color="E6FCF5"
    )

    # Sección 3
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(12)
    p_h1.paragraph_format.space_after = Pt(6)
    r = p_h1.add_run("3. Guía Paso a Paso para usar la Aplicación Web en Clase")
    r.font.name = "Calibri"
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    p_s1 = doc.add_paragraph()
    p_s1.paragraph_format.left_indent = Inches(0.2)
    p_s1.paragraph_format.space_after = Pt(3)
    p_s1.add_run("[  ] Paso 1: Abrir la App en el Navegador: ").bold = True
    p_s1.add_run("Ve a la carpeta del monográfico y haz doble clic sobre ").font.color.rgb = C_DARK
    p_s1.add_run("index.html").bold = True
    p_s1.add_run(" (o abre el enlace en tu navegador Google Chrome o Edge). Funciona de forma inmediata y sin necesidad de instalar nada.")

    p_s2 = doc.add_paragraph()
    p_s2.paragraph_format.left_indent = Inches(0.2)
    p_s2.paragraph_format.space_after = Pt(3)
    p_s2.add_run("[  ] Paso 2: Probar el Módulo de Matemáticas: ").bold = True
    p_s2.add_run("Pulsa el botón de ejemplo ").font.color.rgb = C_DARK
    p_s2.add_run("«Dos coches que se cruzan (Madrid - Barcelona)»").bold = True
    p_s2.add_run(" o teclea tu propio problema. Escribe el nombre de tu nieto y pulsa «Explicar el Problema con Pedagogía». Revisa la explicación de 4 capas.")

    p_s3 = doc.add_paragraph()
    p_s3.paragraph_format.left_indent = Inches(0.2)
    p_s3.paragraph_format.space_after = Pt(3)
    p_s3.add_run("[  ] Paso 3: Probar el Módulo de Historia y Ciencias: ").bold = True
    p_s3.add_run("Cambia a la pestaña de Historia. Pulsa el botón de ejemplo ").font.color.rgb = C_DARK
    p_s3.add_run("«Los Reyes Católicos»").bold = True
    p_s3.add_run(" para cargar datos de muestra procedentes de NotebookLM. Pulsa «Generar Cuadernillo Escolar».")

    p_s4 = doc.add_paragraph()
    p_s4.paragraph_format.left_indent = Inches(0.2)
    p_s4.paragraph_format.space_after = Pt(6)
    p_s4.add_run("[  ] Paso 4: Exportar / Imprimir en PDF: ").bold = True
    p_s4.add_run("Pulsa el botón verde superior ").font.color.rgb = C_DARK
    p_s4.add_run("«Imprimir Cuadernillo y Tarjetas en PDF»").bold = True
    p_s4.add_run(". En la ventana de tu navegador, elige como destino «Guardar como PDF» o selecciona tu impresora física. ¡Tendrás el material de estudio listo en tus manos!")

    # Tabla de Autoevaluación
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(12)
    p_h1.paragraph_format.space_after = Pt(6)
    r = p_h1.add_run("📋 Tabla de Autoevaluación del Abuelo Tutor")
    r.font.name = "Calibri"
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    t_check = doc.add_table(rows=6, cols=3)
    t_check.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_check.autofit = False
    c_col_widths = [Inches(1.0), Inches(3.8), Inches(1.7)]

    c_headers = ["Paso", "Competencia del Abuelo Tutor", "¿Superado?"]
    for j, h in enumerate(c_headers):
        c = t_check.cell(0, j)
        c.width = c_col_widths[j]
        set_cell_background(c, "0B2545")
        set_cell_margins(c, top=100, bottom=100, left=120, right=120)
        p_h = c.paragraphs[0]
        r = p_h.add_run(h)
        r.bold = True
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    checklist_data = [
        ("Módulo 1", "Sé meter cualquier problema de mates y explicárselo a mi nieto con una analogía.", "[  ] SÍ  /  [  ] DUDAS"),
        ("Módulo 1", "Sé imprimir la ficha de matemáticas con el problema resuelto y el reto gemelo.", "[  ] SÍ  /  [  ] DUDAS"),
        ("Módulo 2", "Sé subir fotos de apuntes o del libro de mi nieto a Google NotebookLM.", "[  ] SÍ  /  [  ] DUDAS"),
        ("Módulo 2", "Sé copiar el resumen y el cuestionario de NLM y pegarlos en la aplicación.", "[  ] SÍ  /  [  ] DUDAS"),
        ("Módulo 2", "Sé generar e imprimir el examen con huecos en blanco y las tarjetas recortables.", "[  ] SÍ  /  [  ] DUDAS")
    ]

    for i, (p_num, p_desc, p_eval) in enumerate(checklist_data, start=1):
        bg = "FFFFFF" if i % 2 != 0 else "F8FAFC"
        row_vals = [p_num, p_desc, p_eval]
        for j, val in enumerate(row_vals):
            c = t_check.cell(i, j)
            c.width = c_col_widths[j]
            set_cell_background(c, bg)
            set_cell_margins(c, top=70, bottom=70, left=100, right=100)
            p_cell = c.paragraphs[0]
            p_cell.paragraph_format.space_after = Pt(0)
            r = p_cell.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(9)
            if j == 0:
                r.bold = True
            r.font.color.rgb = C_DARK

    doc.save(TARGET_DOCX)
    print(f"✅ Documento Word generado con éxito en:\n   {TARGET_DOCX}")

# ---------------------------------------------------------------------------
# GENERADOR PDF
# ---------------------------------------------------------------------------
def generate_pdf():
    print("\n📄 Generando Ficha del Monográfico 5 en PDF (ReportLab)...")
    if os.path.exists(TARGET_PDF):
        try: os.remove(TARGET_PDF)
        except Exception: pass

    doc = SimpleDocTemplate(
        TARGET_PDF,
        pagesize=A4,
        leftMargin=1.8*cm,
        rightMargin=1.8*cm,
        topMargin=1.8*cm,
        bottomMargin=1.8*cm
    )

    styles = getSampleStyleSheet()

    c_primary = colors.HexColor('#0B2545')
    c_blue = colors.HexColor('#0066A1')
    c_dark = colors.HexColor('#1E293B')
    c_bg_box = colors.HexColor('#F0F7FC')

    p_header = ParagraphStyle('Head', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, textColor=c_blue, alignment=1, spaceAfter=2)
    p_title = ParagraphStyle('Title', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=16, leading=19, textColor=c_primary, alignment=1, spaceAfter=4)
    p_sub = ParagraphStyle('Sub', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=10, leading=13, textColor=colors.HexColor('#64748B'), alignment=1, spaceAfter=10)
    
    p_h1 = ParagraphStyle('H1', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=15, textColor=c_primary, spaceBefore=8, spaceAfter=4)
    p_body = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=c_dark, spaceAfter=3)
    p_prompt = ParagraphStyle('Prompt', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=c_primary)
    p_box = ParagraphStyle('Box', parent=styles['Normal'], fontName='Helvetica', fontSize=8.2, leading=11.5, textColor=c_dark)
    p_cell = ParagraphStyle('Cell', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=10.5, textColor=c_dark)
    p_cell_b = ParagraphStyle('CellB', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=10.5, textColor=c_primary)
    p_th = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.2, leading=11, textColor=colors.white)

    story = []

    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", p_header))
    story.append(Paragraph("MONOGRÁFICO 5: EL ABUELO TUTOR", p_title))
    story.append(Paragraph("Ayuda a tus Nietos en Matemáticas e Historia con IA y NotebookLM", p_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_blue, spaceAfter=8))

    # Caja Enfoque
    obj_rows = [
        [Paragraph("<b>🎯 El Nuevo Rol del Abuelo en la Era Digital:</b>", p_prompt)],
        [Paragraph("Los abuelos disponen del mayor valor pedagógico del mundo: paciencia, tiempo y empatía sin la prisa del día a día. En este taller aprenderás a usar la IA y la aplicación web interactiva <b>«El Abuelo Tutor»</b> para resolver dudas de matemáticas en 4 capas intuitivas y convertir fotos de libros en cuadernillos escolares imprimibles y tarjetas recortables.", p_box)]
    ]
    t_obj = Table(obj_rows, colWidths=[17.4*cm], splitByRow=1)
    t_obj.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_bg_box),
        ('BOX', (0,0), (-1,-1), 1.2, c_blue),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_obj)
    story.append(Spacer(1, 6))

    # MÓDULO MATES
    story.append(Paragraph("1. Módulo de Matemáticas: La Técnica de las 4 Capas Pedagógicas", p_h1))
    story.append(Paragraph("Cualquier problema introducido libremente en la aplicación se desglosa en 4 niveles:", p_body))
    story.append(Paragraph("• <b>1. Para comprenderlo (Analogía cotidiana):</b> Metáfora sin números para perder el miedo.", p_body))
    story.append(Paragraph("• <b>2. El paso a paso razonado (El puente lógico):</b> Explicación ordenada sin saltos.", p_body))
    story.append(Paragraph("• <b>3. Para el examen del colegio (Rigor formal):</b> Fórmulas y desarrollo algebraico formal.", p_body))
    story.append(Paragraph("• <b>4. El Reto Gemelo (Problema espejo):</b> Ejercicio idéntico con cifras cambiadas para el nieto.", p_body))
    story.append(Spacer(1, 6))

    # MÓDULO HISTORIA
    story.append(Paragraph("2. Módulo de Historia y Ciencias: El Puente NotebookLM a Cuadernillo Imprimible", p_h1))
    story.append(Paragraph("Google NotebookLM analiza con precisión las fotos de los libros y apuntes del nieto. Como NLM no permite exportar a papel, nuestra App convierte el texto pegado en:", p_body))
    story.append(Paragraph("• <b>Examen con líneas punteadas:</b> Espacio en blanco para que el nieto responda a lápiz.", p_body))
    story.append(Paragraph("• <b>Tarjetas recortables (Flashcards):</b> Pregunta por delante y respuesta por detrás para jugar al trivial escolar en el salón.", p_body))
    story.append(Paragraph("• <b>Hoja de soluciones oficial:</b> Para que el abuelo corrija con total seguridad sin dudar.", p_body))
    story.append(Spacer(1, 6))

    # CÓMO USAR LA APP
    story.append(Paragraph("3. Guía Paso a Paso para Usar la Aplicación en Clase", p_h1))
    story.append(Paragraph("<b>[  ] Paso 1:</b> Abre el archivo <code>index.html</code> en tu navegador (Google Chrome o Edge).", p_body))
    story.append(Paragraph("<b>[  ] Paso 2:</b> En Matemáticas, pulsa un ejemplo rápido o teclea el problema del libro de tu nieto.", p_body))
    story.append(Paragraph("<b>[  ] Paso 3:</b> En Historia, pega el texto de NLM o carga el ejemplo de 'Los Reyes Católicos'.", p_body))
    story.append(Paragraph("<b>[  ] Paso 4:</b> Pulsa 'Imprimir / Guardar en PDF' para obtener la ficha física para tu nieto.", p_body))
    story.append(Spacer(1, 6))

    # TABLA EVALUACIÓN
    story.append(Paragraph("📋 Checklist de Autoevaluación del Abuelo Tutor", p_h1))
    chk_rows = [
        [Paragraph("Paso", p_th), Paragraph("Habilidad / Competencia Práctica", p_th), Paragraph("Autoevaluación", p_th)],
        [Paragraph("1", p_cell_b), Paragraph("Sé meter cualquier problema de mates y explicárselo a mi nieto con una analogía.", p_cell), Paragraph("[  ] SÍ  /  [  ] DUDAS", p_cell)],
        [Paragraph("2", p_cell_b), Paragraph("Sé imprimir la ficha de matemáticas con el problema resuelto y el reto gemelo.", p_cell), Paragraph("[  ] SÍ  /  [  ] DUDAS", p_cell)],
        [Paragraph("3", p_cell_b), Paragraph("Sé subir fotos de apuntes o del libro de mi nieto a Google NotebookLM.", p_cell), Paragraph("[  ] SÍ  /  [  ] DUDAS", p_cell)],
        [Paragraph("4", p_cell_b), Paragraph("Sé copiar el resumen y el cuestionario de NLM y pegarlos en la aplicación.", p_cell), Paragraph("[  ] SÍ  /  [  ] DUDAS", p_cell)],
        [Paragraph("5", p_cell_b), Paragraph("Sé generar e imprimir el examen con huecos en blanco y las tarjetas recortables.", p_cell), Paragraph("[  ] SÍ  /  [  ] DUDAS", p_cell)],
    ]
    t_chk = Table(chk_rows, colWidths=[1.8*cm, 12.0*cm, 3.6*cm], splitByRow=1)
    t_chk.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 3.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
    ]))
    story.append(t_chk)

    doc.build(story)
    print(f"✅ Documento PDF generado con éxito en:\n   {TARGET_PDF}")

def main():
    print("=" * 70)
    print("🚀 GENERANDO FICHA MONOGRÁFICO 5 (EL ABUELO TUTOR) EN DOCX Y PDF")
    print("=" * 70)
    generate_docx()
    generate_pdf()
    print("\n🎉 ¡PROCESO COMPLETADO AL 100%!")

if __name__ == "__main__":
    main()
