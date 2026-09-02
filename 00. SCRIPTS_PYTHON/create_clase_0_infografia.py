import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        
        # Header banner
        self.setFillColor(colors.HexColor("#0F172A"))
        self.rect(0, letter[1] - 38, letter[0], 38, stroke=0, fill=1)
        
        self.setFillColor(colors.white)
        self.setFont("Helvetica-Bold", 10)
        self.drawString(30, letter[1] - 24, "CURSO DE INTELIGENCIA ARTIFICIAL EN EL AULA — CLASE 0 (INTRODUCCIÓN)")
        
        # Footer banner
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(30, 42, letter[0] - 30, 42)
        
        self.setFillColor(colors.HexColor("#64748B"))
        self.setFont("Helvetica", 9)
        self.drawString(30, 26, "Vídeo Analizado: 5 Profesiones que Sobrevivirán a la IA (y por qué son imposibles de automatizar)")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(letter[0] - 30, 26, page_str)
        self.restoreState()

def build_clase_0_pdf():
    output_dir = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF"
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, "CLASE_0_Infografia_Resumen_5_Profesiones_IA.pdf")
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=35,
        rightMargin=35,
        topMargin=50,
        bottomMargin=55
    )
    
    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15.5,
        leading=20,
        textColor=colors.HexColor('#0F172A'),
        alignment=TA_CENTER,
        spaceAfter=10
    )
    
    style_subtitle = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14.5,
        textColor=colors.HexColor('#334155'),
        alignment=TA_LEFT,
        spaceAfter=8
    )
    
    style_section_h = ParagraphStyle(
        'SectionH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15.5,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=12,
        spaceAfter=6
    )
    
    style_body = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=8
    )
    
    style_prompt = ParagraphStyle(
        'PromptStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor('#0F172A')
    )
    
    style_reto = ParagraphStyle(
        'RetoStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#4A154B')
    )

    story = []
    
    # Title
    story.append(Paragraph("🎯 CLASE 0: LAS 5 PROFESIONES INAUTOMATIZABLES Y LAS FRONTERAS DE LA IA", style_title))
    story.append(Paragraph("<b>Vídeo analizado:</b> <i>\"5 Profesiones que Sobrevivirán a la IA (y por qué son imposibles de automatizar)\"</i> (URL: https://youtu.be/D4W9DguTKUk)", style_subtitle))
    story.append(Spacer(1, 4))
    
    intro_txt = (
        "En esta Ficha Oficial de la <b>Clase 0</b>, clarificamos las claves del vídeo introductorio. "
        "El objetivo es entender con precisión técnica qué puede automatizar la Inteligencia Artificial y qué es privativo del ser humano: "
        "mientras que la IA es imbatible en el <b>cálculo, procesamiento y transmisión de datos (incluyendo impartir clases teóricas)</b>, "
        "jamás podrá sustituir el <b>juicio clínico y la empatía hospitalaria</b>, la <b>improvisación en el caos físico</b>, "
        "la <b>responsabilidad legal/moral ante la sociedad</b>, el <b>acompañamiento pedagógico y mentoría humana</b>, ni la <b>gestión de crisis bajo incertidumbre</b>."
    )
    story.append(Paragraph(intro_txt, style_body))
    story.append(Spacer(1, 4))
    
    # Summary Table of the 5 Professions
    story.append(Paragraph("📌 Síntesis Exacta y Corregida de las 5 Áreas Inautomatizables", style_section_h))
    
    th_style = ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=8.5, leading=11.5, textColor=colors.white)
    td_style = ParagraphStyle('TD', fontName='Helvetica', fontSize=8, leading=11, textColor=colors.HexColor('#1E293B'))
    td_bold = ParagraphStyle('TDB', fontName='Helvetica-Bold', fontSize=8, leading=11, textColor=colors.HexColor('#0F172A'))
    
    table_data = [
        [Paragraph("Área / Profesión", th_style), Paragraph("Qué Hace la IA vs. Qué Hace el Humano", th_style), Paragraph("Pilar Infranqueable (Por qué no se automatiza)", th_style)],
        [
            Paragraph("<b>1. Salud y Cuidados Clínicos</b><br/>(Médicos, Enfermeros, Psicólogos)", td_bold),
            Paragraph("La IA analiza analíticas y sugiere diagnósticos. El humano aporta <b>trato cálido, empatía profunda, escucha activa</b> y juicio crítico en urgencias.", td_style),
            Paragraph("<b>Empatía e Inteligencia Emocional:</b> Un paciente en crisis necesita consuelo y confianza de otro ser humano que comprende el sufrimiento real.", td_style)
        ],
        [
            Paragraph("<b>2. Oficios Técnicos Físicos</b><br/>(Electricistas, Fontaneros, Soldadores)", td_bold),
            Paragraph("La IA calcula planos. El obrero/técnico trabaja en <b>edificios reales, antiguos y caóticos</b> donde nada sigue un estándar predecible.", td_style),
            Paragraph("<b>Caos Físico e Improvisación:</b> Requieren 'geometría corporal' y destreza milimétrica para adaptar reparaciones en el mundo real.", td_style)
        ],
        [
            Paragraph("<b>3. Justicia, Derecho y Ética</b><br/>(Jueces, Magistrados, Abogados)", td_bold),
            Paragraph("La IA redacta contratos o busca jurisprudencia. El humano evalúa la equidad moral, delibera y <b>asume las consecuencias legales</b>.", td_style),
            Paragraph("<b>Responsabilidad Legal e Indellegable:</b> Un algoritmo no tiene responsabilidad penal ni patrimonio; la sociedad exige rendición de cuentas humana.", td_style)
        ],
        [
            Paragraph("<b>4. Orientación y Mentoría Pedagógica</b><br/>(Guías, Tutores y Mentores)", td_bold),
            Paragraph("<b>¡ATENCIÓN! La IA SÍ impartirá el temario teóricamente.</b> El docente/mentor se enfoca en <b>cuidar, guiar, motivar, detectar crisis emocionales y formar valores</b>.", td_style),
            Paragraph("<b>Conexión Afectiva y Cuidado Pedagógico:</b> El alumno aprende y madura gracias al vínculo de confianza y el apoyo emocional humana.", td_style)
        ],
        [
            Paragraph("<b>5. Liderazgo y Gestión de Crisis</b><br/>(Directivos y Estrategias ante lo Incierto)", td_bold),
            Paragraph("La IA procesa estadísticas pasadas. El líder toma decisiones en <b>crisis inéditas y situaciones de alta incertidumbre</b> con datos ambiguos.", td_style),
            Paragraph("<b>Juicio bajo Incertidumbre Extrema:</b> Decidir cuando no hay datos suficientes asumiendo el peso ético y social de la estrategia.", td_style)
        ]
    ]
    
    t_prof = Table(table_data, colWidths=[140, 205, 197])
    t_prof.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')])
    ]))
    story.append(t_prof)
    story.append(Spacer(1, 8))
    
    # Prompt Maestro Corregido Section
    story.append(Paragraph("✍️ Prompt Maestro V2 Corregido para tu IA / Gemini (Cero Errores de Diseño)", style_section_h))
    
    prompt_text = (
        "ROL Y TAREA\n"
        "Actúa como un Ilustrador de Enciclopedia Científica de clase mundial y Arquitecto de Diseños de Información Clara.\n"
        "Tu tarea es generar una \"Infografía de Enciclopedia Científica Ilustrada\" altamente rigurosa, limpia, perfectamente ordenada en paneles separados y visualmente impecable, en estilo clásico editorial de lujo (\"Museum-Grade\"), sin ninguna marca de agua, sin logos y sin agencias de stock, que sintetiza con exactitud el vídeo: \"Las 5 Profesiones Inautomatizables y la Frontera de la IA\".\n\n"
        "REGLA DE ORO DE IDIOMA PARA LA IA:\n"
        "Es absolutamente obligatorio que todo título, texto, rótulo o leyenda que aparezca dentro de la imagen generada esté ESCRITO EXCLUSIVAMENTE EN ESPAÑOL CASTELLANO, con ortografía perfecta y sin repetir palabras. CERO INGLÉS y CERO REPETICIONES DE TEXTO.\n\n"
        "ARQUITECTURA VISUAL DE LA LÁMINA (ESTRUCTURA EN RECUADROS INDEPENDIENTES):\n"
        "• Fondo: Papel pergamino crema suave y limpio, con marcos de enciclopedia clásica.\n"
        "• Separación estricta de módulos: La lámina debe tener exactamente 5 recuadros de profesiones bien separados alrededor (2 a la izquierda, 2 a la derecha, 1 abajo) más 1 FIGURA CENTRAL DUAL en el medio. NINGUNA profesión ni ilustración debe mezclarse dentro del recuadro de otra.\n\n"
        "ILUSTRACIONES Y TEXTOS BREVES EXACTOS POR RECUADRO:\n\n"
        "FIGURA CENTRAL DUAL (\"POP-OUT\" 3D): En el centro de la lámina, una ilustración dual dividida verticalmente: a la izquierda, una mano robótica futurista con circuitos procesando flujos de datos (simbolizando \"Cálculo y Automatización\"); a la derecha, una mano humana biológica, realista y cálida (simbolizando \"Juicio Crítico y Responsabilidad Moral\").\n"
        "• Rótulo Central Breve: \"PROCESAMIENTO ALGORÍTMICO vs. JUICIO Y RESPONSABILIDAD HUMANA\".\n\n"
        "RECUADRO 1 (Arriba Izquierda) - SALUD Y CUIDADOS CLÍNICOS:\n"
        "• Ilustración realista y respetuosa (CERO CORTES ANATÓMICOS, CERO MÚSCULOS AL DESCUBIERTO) de un médico o enfermera sentada en una consulta hablando con un paciente, transmitiendo calidez, compasión y escucha activa.\n"
        "• Texto exacto en 2 líneas cortas (sin repetir): \"1. SALUD Y CUIDADOS / Empatía y Juicio en Crisis\".\n\n"
        "RECUADRO 2 (Abajo Izquierda) - OFICIOS TÉCNICOS FÍSICOS:\n"
        "• Ilustración de un técnico electricista/soldador con arnés o herramientas trabajando en la pared o tuberías de un edificio antiguo y caótico.\n"
        "• Texto exacto en 2 líneas cortas (sin repetir): \"2. OFICIOS TÉCNICOS / Caos Físico e Improvisación\".\n\n"
        "RECUADRO 3 (Arriba Derecha) - JUSTICIA, DERECHO Y ÉTICA:\n"
        "• Ilustración de una balanza judicial de bronce sobre un estrado de madera en un tribunal. CERO OBREROS ni herramientas aquí; exclusivamente elementos judiciales.\n"
        "• Texto exacto en 2 líneas cortas (sin repetir): \"3. JUSTICIA Y DERECHO / Responsabilidad Legal Indellegable\".\n\n"
        "RECUADRO 4 (Abajo Derecha) - ORIENTACIÓN Y MENTORÍA PEDAGOGÍA:\n"
        "• Ilustración de un aula cálida donde un profesor/mentor no está dando clase magistral en la pizarra (eso lo hace la IA), sino sentado o charlando en grupo apoyando y motivando emocionalmente a los alumnos.\n"
        "• Texto exacto en 2 líneas cortas (sin repetir): \"4. MENTORÍA Y CUIDADO PEDAGÓGICO / Acompañamiento y Valores\".\n\n"
        "RECUADRO 5 (Centro Abajo) - LIDERAZGO Y GESTIÓN DE CRISIS:\n"
        "• Ilustración de un directivo o líder evaluando variables éticas en un tablero ante una situación imprevista y compleja.\n"
        "• Texto exacto en 2 líneas cortas (sin repetir): \"5. LIDERAZGO ESTRATÉGICO / Decisiones bajo Incertidumbre\".\n\n"
        "PROHIBICIÓN DE REPETICIÓN TIPOGRÁFICA Y MARCAS:\n"
        "Escribe cada rótulo de recuadro UNA SOLA VEZ con letra limpia y legible. CERO marcas de agua, CERO logos de stock y CERO textos duplicados."
    )
    
    raw_blocks = re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', prompt_text)
    table_rows = []
    table_rows.append([Paragraph("<b>• Prompt maestro V2 Corregido listo para copiar y pegar:</b>", style_prompt)])
    for blk in raw_blocks:
        if not blk.strip(): continue
        if len(blk) > 600:
            sub_blks = re.split(r'\n', blk)
            for sb in sub_blks:
                if sb.strip(): table_rows.append([Paragraph(sb.strip(), style_prompt)])
        else:
            table_rows.append([Paragraph(blk.strip().replace('\n', '<br/>'), style_prompt)])
            
    prompt_table = Table(table_rows, colWidths=[letter[0] - 70], splitByRow=1, repeatRows=0)
    prompt_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F8F0')),
        ('BORDER', (0,0), (-1,-1), 1.5, colors.HexColor('#0B6623')),
        ('PADDING', (0,0), (-1,-1), 5.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(prompt_table)
    story.append(Spacer(1, 8))
    
    # Reto Práctico
    story.append(Paragraph("🧪 El Reto Práctico / Aplicación en Aula con Gemini", style_section_h))
    
    reto_text = (
        "<b>Dinámica para la Clase 0 (Debate sobre Educación e IA):</b><br/>"
        "1. Pega este Prompt Maestro V2 Corregido en <b>Gemini</b> para generar la nueva Infografía limpia y proyectarla en la pizarra.<br/>"
        "2. Enfócate con los alumnos en el <b>Punto 4 (Educación)</b>: explícales que la IA ya es capaz de impartir temario y resolver dudas teóricas a cualquier hora. ¿Qué papel le queda entonces al maestro y a la escuela? (Debatir sobre el acompañamiento emocional, el desarrollo del criterio crítico, la motivación social y los valores humanos).<br/><br/>"
        "<b>👉 Ahora te toca a ti: ¡Haz tú una modificación que se te ocurra y sorpréndenos!</b> Pídele a Gemini en el chat: <i>\"Modifica la ilustración de la figura central para que las dos manos (la robótica y la humana) sostengan juntas una pequeña planta que germina, simbolizando que la IA automatiza el cálculo para que el humano se concentre en el cuidado de la vida.\"</i>"
    )
    
    r_rows = [ [Paragraph(reto_text, style_reto)] ]
    reto_table = Table(r_rows, colWidths=[letter[0] - 70], splitByRow=1, repeatRows=0)
    reto_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FAF5FF')),
        ('BORDER', (0,0), (-1,-1), 1, colors.HexColor('#8B008B')),
        ('PADDING', (0,0), (-1,-1), 6.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(reto_table)
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Ficha PDF corregida y creada en:", pdf_path)

if __name__ == "__main__":
    build_clase_0_pdf()
