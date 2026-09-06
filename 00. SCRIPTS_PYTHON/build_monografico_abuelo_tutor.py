# -*- coding: utf-8 -*-
"""
Generador de la Ficha Didáctica del Monográfico 5:
«EDUCANIETOS IA: Tutor de Ciencias, Física, Química y Matemáticas con Gemini y Sesiones en Pantalla de Historia con NotebookLM»
Genera exclusivamente:
- FICHA_MONOGRAFICO_EDUCANIETOS_IA.docx y .pdf
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
TARGET_DOCX = os.path.join(TARGET_DIR, "FICHA_MONOGRAFICO_EDUCANIETOS_IA.docx")
TARGET_PDF = os.path.join(TARGET_DIR, "FICHA_MONOGRAFICO_EDUCANIETOS_IA.pdf")

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
    print("📝 Generando Ficha Didáctica en DOCX...")
    doc = docx.Document()

    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)

    C_NAVY = RGBColor(11, 37, 69)      # #0B2545
    C_BLUE = RGBColor(0, 102, 161)     # #0066A1
    C_PURPLE = RGBColor(109, 40, 217)  # #6D28D9
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
    r_main = p_main.add_run("MONOGRÁFICO 5: EDUCANIETOS IA")
    r_main.font.name = "Calibri"
    r_main.font.size = Pt(22)
    r_main.font.bold = True
    r_main.font.color.rgb = C_NAVY

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("Tutor de Ciencias, Física, Química y Matemáticas (Gemini) y Sesiones en Pantalla de Historia (NotebookLM)")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = C_MUTED

    # Cuadro de enfoque pedagógico
    add_callout_box(
        doc,
        "🎯 Metodología Diferenciada: Ciencias en 1 Clic con Gemini + Historia en Pantalla con NotebookLM",
        [
            "1. Todas las materias de Ciencias: Sirve para Matemáticas, Física, Química, Biología, Geología y Tecnología. El abuelo escribe cualquier duda en lenguaje cotidiano (desde por qué flotan los barcos o la fórmula del etanol, hasta una integral o el ciclo del agua).",
            "2. Calibración cognitiva por edad (Botones táctiles): Se adapta radicalmente al nieto mediante 3 botones: 👶 8-11 años (juegos, bolitas LEGO, sin tecnicismos), 🧒 12-14 años (ciencias prácticas de la ESO) y 🧑 15-18 años (rigor oficial, nomenclatura IUPAC, unidades SI y Selectividad).",
            "3. Conexión directa con Google Gemini en 1 Clic: La app genera un prompt maestro optimizado, lo copia al portapapeles y abre Gemini sincronizadamente. Con Ctrl+V / Cmd+V y Enter, Gemini responde con ilustraciones visuales a color (prohibidos cuadros feos en texto ASCII).",
            "4. Historia y Letras en Directo con NotebookLM: Abuelo y nieto se sientan juntos frente a la pantalla para explorar el mapa mental, concursar con tarjetas de memoria y resolver cuestionarios dinámicos con citas directas al libro escolar."
        ],
        border_color="6D28D9",
        bg_color="F5F3FF"
    )

    # Sección 1
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(12)
    p_h1.paragraph_format.space_after = Pt(6)
    r = p_h1.add_run("1. Módulo de Ciencias, Física, Química y Matemáticas: Estructura en 5 Partes")
    r.font.name = "Calibri"
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.add_run("Cuando el nieto no entiende una fórmula o concepto científico, casi siempre es porque se lo explican de forma abstracta y fría. Al pulsar el botón ")
    p.add_run("«🚀 Preguntar a Google Gemini»").bold = True
    p.add_run(", la IA genera una ficha didáctica impecable estructurada en 5 partes clave:")

    partes_ciencias = [
        ("🌟 1. Comprensión Intuitiva (Analogía cotidiana)", "Una metáfora visual tomada de la vida diaria (la cocina, el deporte, juguetes o anécdotas históricas) para entender la idea sin miedo antes de ver fórmulas ni números."),
        ("🧠 2. El Paso a Paso Razonado (Sin saltos)", "La explicación ordenada de la lógica de cada paso, eliminando los 'saltos mágicos' que desorientan al estudiante."),
        ("🎨 3. Imagen Ilustrada o Gráfica Didáctica a Color", "Gemini genera una ilustración visual limpia y a todo color con su generador de imágenes. Está estrictamente prohibido dibujar cuadros en texto plano (ASCII/guiones) en blanco y negro."),
        ("📝 4. El Nivel para su Examen (Rigor según la edad)", "Las fórmulas oficiales, la notación estándar y el desarrollo analítico adaptado exactamente a su curso escolar para sacar la máxima nota."),
        ("🎯 5. El Reto Gemelo (Para el cuaderno)", "Un ejercicio idéntico con datos cambiados para que el nieto lo resuelva a solas a lápiz en su cuaderno y consolide su seguridad.")
    ]

    for tit, desc in partes_ciencias:
        p_item = doc.add_paragraph()
        p_item.paragraph_format.left_indent = Inches(0.2)
        p_item.paragraph_format.space_after = Pt(3)
        r_t = p_item.add_run(tit + ": ")
        r_t.bold = True
        r_t.font.color.rgb = C_BLUE
        p_item.add_run(desc).font.color.rgb = C_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Sección 2: Calibración por Edades
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(12)
    p_h1.paragraph_format.space_after = Pt(6)
    r = p_h1.add_run("2. Calibración Cognitiva: Los 3 Niveles Escolares")
    r.font.name = "Calibri"
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.add_run("Una misma pregunta (por ejemplo: ")
    p.add_run("«¿Cuál es la fórmula del etanol?»").bold = True
    p.add_run(") exige explicaciones totalmente distintas según la edad del nieto:")

    edades = [
        ("👶 8 a 11 años (Primaria)", "Prohibidas fórmulas químicas complejas y enlaces covalentes. Se explica como una 'receta mágica de bolitas LEGO' (2 de carbono, 6 de hidrógeno y 1 de oxígeno dándose la mano) y su utilidad en el botiquín de casa para curar heridas."),
        ("🧒 12 a 14 años (1º y 2º ESO)", "Notación elemental de secundaria (C₂H₆O / CH₃-CH₂-OH), átomos y enlaces sencillos, explicando la fermentación de la fruta y los desinfectantes cotidianos."),
        ("🧑 15 a 18 años (3º ESO y Bachillerato)", "Máximo rigor pre-universitario: grupo funcional alcohol (-OH), fórmula semidesarrollada, polaridad, nomenclatura IUPAC oficial y unidades del Sistema Internacional (SI) para examen y Selectividad/EBAU.")
    ]

    for tit, desc in edades:
        p_item = doc.add_paragraph()
        p_item.paragraph_format.left_indent = Inches(0.2)
        p_item.paragraph_format.space_after = Pt(3)
        r_t = p_item.add_run(tit + ": ")
        r_t.bold = True
        r_t.font.color.rgb = C_PURPLE
        p_item.add_run(desc).font.color.rgb = C_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Sección 3: Historia con NotebookLM
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(12)
    p_h1.paragraph_format.space_after = Pt(6)
    r = p_h1.add_run("3. Módulo de Historia y Ciencias: La Sesión en Vivo con NotebookLM")
    r.font.name = "Calibri"
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    add_callout_box(
        doc,
        "💻 Dinámica de Estudio Abuelo-Nieto en Pantalla",
        [
            "1. Subir los apuntes: El nieto hace 2 fotos de las páginas del libro con el móvil y se suben a Fuentes de NotebookLM. NLM extrae el texto exacto sin inventar nada.",
            "2. Mapa Mental interactivo: En Studio, pulsáis «Mapa mental». Desplegáis juntos los nodos en pantalla para entender las causas y consecuencias visualmente.",
            "3. Concurso de Tarjetas (Flashcards): Pulsáis «Tarjetas». El abuelo lee la pregunta en voz alta, el nieto piensa la respuesta y hacen clic en la tarjeta para comprobar si acierta.",
            "4. Cuestionario con Citas directas: Contestáis juntos el test pantalla a pantalla. Si el nieto duda, pulsa el número de cita y NLM resalta el renglón exacto del libro donde está la prueba documental."
        ],
        border_color="0066A1",
        bg_color="F0F7FC"
    )

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
    c_col_widths = [Inches(1.2), Inches(3.8), Inches(1.5)]

    c_headers = ["Materia / Módulo", "Competencia del Abuelo Tutor", "¿Superado?"]
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
        ("Ciencias / Mates", "Sé escribir dudas de Matemáticas, Física o Química y seleccionar el botón de edad de mi nieto.", "[  ] SÍ  /  [  ] DUDAS"),
        ("Ciencias / Mates", "Sé pulsar 'Preguntar a Gemini', pegar en la ventana abierta y revisar la ilustración a color generada.", "[  ] SÍ  /  [  ] DUDAS"),
        ("Ciencias / Mates", "Sé proponerle el Reto Gemelo para que mi nieto lo resuelva a solas a lápiz en su cuaderno.", "[  ] SÍ  /  [  ] DUDAS"),
        ("Historia / Letras", "Sé subir fotos de los apuntes o libros del nieto a Google NotebookLM como fuentes fiables.", "[  ] SÍ  /  [  ] DUDAS"),
        ("Historia / Letras", "Sé explorar el Mapa Mental y jugar al concurso de Tarjetas y Cuestionarios interactivos en pantalla.", "[  ] SÍ  /  [  ] DUDAS")
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
    print(f"✅ Documento Word generado en:\n   {TARGET_DOCX}")

# ---------------------------------------------------------------------------
# GENERADOR PDF
# ---------------------------------------------------------------------------
def generate_pdf():
    print("\n📄 Generando Ficha Didáctica en PDF (ReportLab)...")
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
    c_purple = colors.HexColor('#6D28D9')
    c_dark = colors.HexColor('#1E293B')
    c_bg_box = colors.HexColor('#F5F3FF')

    p_header = ParagraphStyle('Head', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, textColor=c_blue, alignment=1, spaceAfter=2)
    p_title = ParagraphStyle('Title', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=17, leading=20, textColor=c_primary, alignment=1, spaceAfter=4)
    p_sub = ParagraphStyle('Sub', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=10, leading=13, textColor=colors.HexColor('#64748B'), alignment=1, spaceAfter=10)
    
    p_h1 = ParagraphStyle('H1', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=11.5, leading=14.5, textColor=c_primary, spaceBefore=7, spaceAfter=3)
    p_body = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=8.3, leading=11.3, textColor=c_dark, spaceAfter=2.5)
    p_prompt = ParagraphStyle('Prompt', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=c_purple)
    p_box = ParagraphStyle('Box', parent=styles['Normal'], fontName='Helvetica', fontSize=8.1, leading=11.2, textColor=c_dark)
    p_cell = ParagraphStyle('Cell', parent=styles['Normal'], fontName='Helvetica', fontSize=7.8, leading=10.2, textColor=c_dark)
    p_cell_b = ParagraphStyle('CellB', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.8, leading=10.2, textColor=c_primary)
    p_th = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.0, leading=10.5, textColor=colors.white)

    story = []

    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", p_header))
    story.append(Paragraph("MONOGRÁFICO 5: EDUCANIETOS IA", p_title))
    story.append(Paragraph("Tutor de Ciencias, Física, Química y Matemáticas (Gemini) y Sesiones en Pantalla de Historia (NotebookLM)", p_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=7))

    # Caja Enfoque
    obj_rows = [
        [Paragraph("<b>🎯 Metodología Diferenciada: Ciencias con Gemini + Historia con NotebookLM</b>", p_prompt)],
        [Paragraph("• <b>En Ciencias, Física, Química y Matemáticas:</b> Usamos la app <b>«Educanietos IA»</b>. Escribes la duda (fotosíntesis, leyes de Newton, derivadas o fórmula del etanol) y seleccionas la edad de tu nieto. En 1 clic se genera el prompt optimizado, se abre Gemini y este responde con analogías intuitivas, explicaciones paso a paso e ilustraciones a todo color (sin cuadros feos en texto plano ASCII).<br/>• <b>En Historia y Ciencias Sociales:</b> Nos sentamos juntos abuelo y nieto frente a la pantalla de <b>NotebookLM</b> para explorar el Mapa Mental interactivo, jugar al concurso de Tarjetas y resolver Cuestionarios con citas directas al libro escolar.", p_box)]
    ]
    t_obj = Table(obj_rows, colWidths=[17.4*cm], splitByRow=1)
    t_obj.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_bg_box),
        ('BOX', (0,0), (-1,-1), 1.2, c_purple),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_obj)
    story.append(Spacer(1, 5))

    # MÓDULO CIENCIAS Y MATES
    story.append(Paragraph("1. Módulo de Ciencias y Matemáticas: Ficha Didáctica en 5 Partes", p_h1))
    story.append(Paragraph("Al pulsar <b>«🚀 Preguntar a Google Gemini»</b>, la IA redacta una respuesta pedagógica de 5 niveles:", p_body))
    story.append(Paragraph("• <b>1. Comprensión Intuitiva:</b> Analogía visual de la vida real (cocina, deportes, juguetes) para entender la idea sin miedo.", p_body))
    story.append(Paragraph("• <b>2. El Paso a Paso Razonado:</b> Lógica de cada movimiento renglón por renglón sin saltos inexplicables.", p_body))
    story.append(Paragraph("• <b>3. Imagen Ilustrada a Color:</b> Ilustración visual generada con IA a todo color (prohibidos cuadros ASCII/texto plano).", p_body))
    story.append(Paragraph("• <b>4. Nivel para su Examen:</b> Fórmulas oficiales, notación IUPAC y rigor formal adecuado al curso del estudiante.", p_body))
    story.append(Paragraph("• <b>5. El Reto Gemelo:</b> Ejercicio espejo con datos cambiados para que el nieto lo resuelva a solas a lápiz en su cuaderno.", p_body))
    story.append(Spacer(1, 5))

    # CALIBRACIÓN POR EDADES
    story.append(Paragraph("2. Calibración Cognitiva por Edades (Botones Táctiles en Pantalla)", p_h1))
    story.append(Paragraph("• 👶 <b>8 a 11 años (Primaria):</b> Prohibidas fórmulas abstractas o enlaces covalentes. Explicación como bolitas LEGO de colores y recetas mágicas.", p_body))
    story.append(Paragraph("• 🧒 <b>12 a 14 años (1º-2º ESO):</b> Notación molecular básica (C₂H₆O), enlaces simples y conexión con la ciencia cotidiana.", p_body))
    story.append(Paragraph("• 🧑 <b>15 a 18 años (3º ESO-Bachillerato):</b> Rigor pre-universitario, grupo funcional (-OH), nomenclatura IUPAC y unidades del SI.", p_body))
    story.append(Spacer(1, 5))

    # MÓDULO HISTORIA
    story.append(Paragraph("3. Módulo de Historia: Sesión en Vivo con NotebookLM (En Pantalla)", p_h1))
    story.append(Paragraph("• <b>Fotos de Apuntes:</b> Sube fotos del libro a Fuentes de NotebookLM sin transcribir nada a mano.", p_body))
    story.append(Paragraph("• <b>Mapa Mental en Vivo:</b> Exploráis juntos el árbol visual de causas y consecuencias.", p_body))
    story.append(Paragraph("• <b>Concurso de Tarjetas (Flashcards):</b> El abuelo lee la pregunta y el nieto adivina antes de voltear la tarjeta.", p_body))
    story.append(Paragraph("• <b>Cuestionario con Citas:</b> Resuelven el test y usan las citas para comprobar la prueba documental del texto.", p_body))
    story.append(Spacer(1, 5))

    # TABLA EVALUACIÓN
    story.append(Paragraph("📋 Checklist de Autoevaluación del Abuelo Tutor", p_h1))
    chk_rows = [
        [Paragraph("Módulo", p_th), Paragraph("Habilidad / Competencia Práctica", p_th), Paragraph("Autoevaluación", p_th)],
        [Paragraph("Ciencias / Mates", p_cell_b), Paragraph("Sé escribir dudas de Ciencias o Matemáticas y seleccionar el botón de edad de mi nieto.", p_cell), Paragraph("[  ] SÍ  /  [  ] DUDAS", p_cell)],
        [Paragraph("Ciencias / Mates", p_cell_b), Paragraph("Sé pulsar 'Preguntar a Gemini', pegar en la ventana abierta y revisar la ilustración a color.", p_cell), Paragraph("[  ] SÍ  /  [  ] DUDAS", p_cell)],
        [Paragraph("Ciencias / Mates", p_cell_b), Paragraph("Sé proponerle el Reto Gemelo para que mi nieto lo resuelva a lápiz en su cuaderno.", p_cell), Paragraph("[  ] SÍ  /  [  ] DUDAS", p_cell)],
        [Paragraph("Historia / Letras", p_cell_b), Paragraph("Sé subir fotos de los apuntes o libros del nieto a Google NotebookLM como fuentes fiables.", p_cell), Paragraph("[  ] SÍ  /  [  ] DUDAS", p_cell)],
        [Paragraph("Historia / Letras", p_cell_b), Paragraph("Sé explorar el Mapa Mental y jugar al concurso de Tarjetas y Cuestionarios en pantalla.", p_cell), Paragraph("[  ] SÍ  /  [  ] DUDAS", p_cell)],
    ]
    t_chk = Table(chk_rows, colWidths=[2.4*cm, 11.4*cm, 3.6*cm], splitByRow=1)
    t_chk.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
    ]))
    story.append(t_chk)

    doc.build(story)
    print(f"✅ Documento PDF generado en:\n   {TARGET_PDF}")

def main():
    print("=" * 70)
    print("🚀 GENERANDO FICHA DIDÁCTICA ACTUALIZADA DE EDUCANIETOS IA")
    print("=" * 70)
    generate_docx()
    generate_pdf()
    print("\n🎉 ¡FICHA ACTUALIZADA COMPLETADA CON ÉXITO!")

if __name__ == "__main__":
    main()
