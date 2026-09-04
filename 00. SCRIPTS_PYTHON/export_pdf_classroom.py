# -*- coding: utf-8 -*-
import os
import re
import sys
import shutil
from collections import defaultdict
import docx
from docx.shared import Pt, RGBColor
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable

EXPORT_BASE = '/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF'
FRACTALES_BASE = '/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-FRACTALES-FUNCIONES'

def sanitize_name(name):
    clean = re.sub(r'[/\\:*?"<>|]', '_', name)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:65]

def get_lote_folder(index_num, total_items):
    start = ((index_num - 1) // 20) * 20 + 1
    end = min(start + 19, total_items)
    return f'Lote_{start:02d}_al_{end:02d}'

def create_pdf_handout(file_path, block_name, item_id, item_title, concept_text, prompt_data, tips_text):
    # Ensure exact path is created
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Remove any pre-existing conflict file " 2.pdf" if present
    base_no_ext = os.path.splitext(file_path)[0]
    conflict_path = f"{base_no_ext} 2.pdf"
    if os.path.exists(conflict_path):
        try: os.remove(conflict_path)
        except Exception: pass
    if os.path.exists(file_path):
        try: os.remove(file_path)
        except Exception: pass

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45
    )
    
    styles = getSampleStyleSheet()
    
    style_header = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        textColor=colors.HexColor('#005A9E'),
        spaceAfter=4,
        alignment=1
    )
    
    style_block = ParagraphStyle(
        'BlockStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        textColor=colors.HexColor('#1A0A2E'),
        spaceAfter=12,
        alignment=1
    )
    
    style_title = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor('#1A0A2E'),
        spaceAfter=14
    )
    
    style_section_h = ParagraphStyle(
        'SectionHStyle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=14.5,
        textColor=colors.HexColor('#005A9E'),
        spaceBefore=10,
        spaceAfter=6
    )
    
    style_body = ParagraphStyle(
        'BodyStyle',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=10,
        leading=14.5,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=8
    )
    
    style_prompt = ParagraphStyle(
        'PromptStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=14.5,
        textColor=colors.HexColor('#1A0A2E')
    )
    
    style_reto = ParagraphStyle(
        'RetoStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14.5,
        textColor=colors.HexColor('#4A154B')
    )

    if "[ARTE-" in str(item_id):
        style_header.textColor = colors.HexColor('#8B4513')
        style_section_h.textColor = colors.HexColor('#8B4513')
        hr_color = colors.HexColor('#8B4513')
    elif "[NAT-" in str(item_id) or "[AVES-" in str(item_id):
        style_header.textColor = colors.HexColor('#0B6623')
        style_section_h.textColor = colors.HexColor('#0B6623')
        hr_color = colors.HexColor('#0B6623')
    elif "[NIV-" in str(item_id):
        style_header.textColor = colors.HexColor('#800080')
        style_section_h.textColor = colors.HexColor('#800080')
        hr_color = colors.HexColor('#800080')
    else:
        hr_color = colors.HexColor('#005A9E')

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph(block_name.upper(), style_block))
    story.append(HRFlowable(width="100%", thickness=2, color=hr_color, spaceAfter=14))
    
    story.append(Paragraph(f"{item_id} {item_title}", style_title))
    
    if concept_text:
        story.append(Paragraph("💡 Contexto y Descripción del Reto / Objetivo Didáctico", style_section_h))
        clean_c = str(concept_text).replace('\n', '<br/>')
        story.append(Paragraph(clean_c, style_body))
        story.append(Spacer(1, 6))
        
    if prompt_data is not None:
        clausula_esp = " (REGLA DE ORO DE IDIOMA PARA LA IA: Es absolutamente obligatorio que todo título, texto, rótulo, leyenda, número o etiqueta explicativa que aparezca dibujada dentro de la imagen o infografía generada esté ESCRITO EXCLUSIVAMENTE Y PERFECTAMENTE EN ESPAÑOL CASTELLANO, con ortografía intachable. Bajo ningún concepto generes ningún texto, palabra ni leyenda visual en inglés ni en otros idiomas.)"
        def _attach_spanish_rule(txt):
            if not isinstance(txt, str):
                return txt
            if ("[INT-" in str(item_id) or "[FUT-" in str(item_id) or "infograf" in txt.lower() or "diagrama" in txt.lower() or "corte" in txt.lower()) and "REGLA DE ORO DE IDIOMA" not in txt:
                return txt.strip() + clausula_esp
            return txt
        if isinstance(prompt_data, list):
            prompt_data = [(_attach_spanish_rule(x[0]), _attach_spanish_rule(x[1])) if isinstance(x, tuple) else _attach_spanish_rule(x) for x in prompt_data]
        elif isinstance(prompt_data, tuple):
            prompt_data = tuple(_attach_spanish_rule(x) for x in prompt_data)
        elif isinstance(prompt_data, str):
            prompt_data = _attach_spanish_rule(prompt_data)

        story.append(Paragraph("✍️ Prompts y Órdenes Exactas para Pegar en IA", style_section_h))
        
        table_rows = []
        if isinstance(prompt_data, list):
            if any(k in str(item_id) for k in ["TXT-005", "TXT-006", "TXT-017", "TXT-021"]):
                table_rows.append([Paragraph("<b>• 🛡️ Las Modalidades de Práctica en el Aula y Móvil (Elige tu caso o practícalas en orden):</b>", style_prompt)])
            elif "TXT-" in str(item_id):
                table_rows.append([Paragraph("<b>• 🔗 Prompts Encadenados en Pasos para copiar y pegar en el chat de Gemini uno tras otro:</b>", style_prompt)])
            else:
                table_rows.append([Paragraph("<b>• Diapositivas listadas para copiar en tu IA una a una:</b>", style_prompt)])
                
            for s_idx, slide_item in enumerate(prompt_data, 1):
                if isinstance(slide_item, tuple) and len(slide_item) == 2:
                    s_title, s_prompt = slide_item
                else:
                    s_title, s_prompt = f"Diapositiva {s_idx}", str(slide_item)
                table_rows.append([Paragraph(f"<b>🔸 [{s_title}]:</b>", style_prompt)])
                for blk in re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(s_prompt)):
                    if blk.strip(): table_rows.append([Paragraph(blk.strip(), style_prompt)])
        elif isinstance(prompt_data, tuple):
            if len(prompt_data) == 3:
                p1, p2, p3 = prompt_data
                table_rows.append([Paragraph("<b>• 🔴 Paso 1 (Prompt en IA para Generar Foto 1):</b>", style_prompt)])
                for blk in re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(p1)):
                    if blk.strip(): table_rows.append([Paragraph(blk.strip(), style_prompt)])
                table_rows.append([Paragraph("<b>• 🔴 Paso 2 (Prompt en IA para Generar Foto 2):</b>", style_prompt)])
                for blk in re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(p2)):
                    if blk.strip(): table_rows.append([Paragraph(blk.strip(), style_prompt)])
                table_rows.append([Paragraph("<b>• 🟢 Paso 3 (Arrastrar las 2 fotos al chat de Gemini y pegar esta orden):</b>", style_prompt)])
                for blk in re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(p3)):
                    if blk.strip(): table_rows.append([Paragraph(blk.strip(), style_prompt)])
            elif len(prompt_data) == 2:
                p1, p2 = prompt_data
                if str(p1).startswith('📱'):
                    op_a = str(p1).replace('📱', '').strip()
                    table_rows.append([Paragraph("<b>• 📱 Paso 1 (¡El Flujo de Aula con tu Propia Foto del Móvil!):</b>", style_prompt)])
                    for blk in re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', op_a):
                        if blk.strip(): table_rows.append([Paragraph(blk.strip(), style_prompt)])
                    table_rows.append([Paragraph("<b>• 🟢 Paso 2 (Orden para la Magia tras arrastrar tu foto al chat de Gemini):</b>", style_prompt)])
                    for blk in re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(p2)):
                        if blk.strip(): table_rows.append([Paragraph(blk.strip(), style_prompt)])
                else:
                    table_rows.append([Paragraph("<b>• 🔴 Paso 1 (Prompt Previo para Generar la Foto Base en IA):</b>", style_prompt)])
                    for blk in re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(p1)):
                        if blk.strip(): table_rows.append([Paragraph(blk.strip(), style_prompt)])
                    table_rows.append([Paragraph("<b>• 🟢 Paso 2 (Orden en la misma conversación para la Magia / Transformación):</b>", style_prompt)])
                    for blk in re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(p2)):
                        if blk.strip(): table_rows.append([Paragraph(blk.strip(), style_prompt)])
            else:
                table_rows.append([Paragraph("<b>• Prompt para pegar exacto en IA:</b>", style_prompt)])
                for blk in re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(prompt_data)):
                    if blk.strip(): table_rows.append([Paragraph(blk.strip(), style_prompt)])
        else:
            table_rows.append([Paragraph("<b>• Prompt maestro listo para copiar en IA:</b>", style_prompt)])
            raw_blocks = re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(prompt_data))
            for blk in raw_blocks:
                if not blk.strip(): continue
                if len(blk) > 600 or ('\n' in blk and len(blk.split('\n')) > 4) or ('<br/>' in blk and len(blk.split('<br/>')) > 4):
                    sub_blks = re.split(r'\n|<br\s*/?>', blk)
                    for sb in sub_blks:
                        if sb.strip(): table_rows.append([Paragraph(sb.strip(), style_prompt)])
                else:
                    clean_blk = blk.replace('\n', '<br/>').strip()
                    table_rows.append([Paragraph(clean_blk, style_prompt)])
        if not table_rows:
            table_rows = [[Paragraph(str(prompt_data), style_prompt)]]
            
        prompt_table = Table(table_rows, colWidths=[letter[0] - 90], splitByRow=1, repeatRows=0)
        if "[ARTE-" in str(item_id):
            p_bg = colors.HexColor('#FDFBF7')
            p_border = colors.HexColor('#8B4513')
        elif "[NAT-" in str(item_id) or "[AVES-" in str(item_id):
            p_bg = colors.HexColor('#F0F8F0')
            p_border = colors.HexColor('#0B6623')
        elif "[NIV-" in str(item_id):
            p_bg = colors.HexColor('#FAF0FA')
            p_border = colors.HexColor('#800080')
        else:
            p_bg = colors.HexColor('#F0F4F8')
            p_border = colors.HexColor('#005A9E')
        prompt_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), p_bg),
            ('BORDER', (0,0), (-1,-1), 1.5, p_border),
            ('PADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(prompt_table)
        story.append(Spacer(1, 10))
        
    if tips_text:
        story.append(Paragraph("🧪 El Reto Práctico / Aplicación en Aula con Gemini", style_section_h))
        exact_phrase = "👉 Ahora te toca a ti: ¡Haz tú una modificación que se te ocurra y sorpréndenos!"
        exact_phrase_bold = f"<b>{exact_phrase}</b>"
        
        r_rows = []
        if 'EST-' in item_id:
            r_rows.append([Paragraph("Descarga la imagen generada en tu IA, súbela a Gemini (gemini.google.com) y escríbele lo siguiente:", style_reto)])
            r_rows.append([Paragraph("<b>Prompt de edición:</b>", style_reto)])
            for blk in re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(tips_text)):
                if not blk.strip(): continue
                r_rows.append([Paragraph(blk.strip().replace('\n', '<br/>'), style_reto)])
            r_rows.append([Paragraph(exact_phrase_bold, style_reto)])
        else:
            raw_t_blocks = re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(tips_text))
            for blk in raw_t_blocks:
                if not blk.strip(): continue
                b_str = blk.replace('\n', '<br/>').strip()
                if exact_phrase in b_str:
                    b_str = b_str.replace(exact_phrase, exact_phrase_bold)
                if len(b_str) > 600 or ('<br/>' in b_str and len(b_str.split('<br/>')) > 4):
                    for sb in re.split(r'<br\s*/?>|\n', b_str):
                        if sb.strip(): r_rows.append([Paragraph(sb.strip(), style_reto)])
                else:
                    r_rows.append([Paragraph(b_str, style_reto)])
            if exact_phrase not in str(tips_text) and "sorpréndenos!" not in str(tips_text):
                r_rows.append([Paragraph(exact_phrase_bold, style_reto)])
        if not r_rows:
            r_rows = [[Paragraph(str(tips_text), style_reto)]]
            
        reto_table = Table(r_rows, colWidths=[letter[0] - 90], splitByRow=1, repeatRows=0)
        if "[ARTE-" in str(item_id):
            r_bg = colors.HexColor('#FDFBF7')
            r_border = colors.HexColor('#8B4513')
        elif "[NAT-" in str(item_id) or "[AVES-" in str(item_id):
            r_bg = colors.HexColor('#F0F8F0')
            r_border = colors.HexColor('#0B6623')
        elif "[NIV-" in str(item_id):
            r_bg = colors.HexColor('#F8F0FC')
            r_border = colors.HexColor('#6A0DAD')
        else:
            r_bg = colors.HexColor('#FAF5FF')
            r_border = colors.HexColor('#8B008B')
        reto_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), r_bg),
            ('BORDER', (0,0), (-1,-1), 1, r_border),
            ('PADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(reto_table)
        story.append(Spacer(1, 8))
        
    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CCCCCC'), spaceAfter=8))
    footer_text = Paragraph("<i>Material didáctico adaptado pedagógicamente para enriquecimiento digital y agilidad mental.</i>", ParagraphStyle('Foot', fontName='Helvetica-Oblique', fontSize=8, textColor=colors.HexColor('#7F8C8D'), alignment=1))
    story.append(footer_text)
    
    doc.build(story)


ESTILOS_VISUALES = [
    "PRESET: CÓMIC CLÁSICO 90s (Línea definida, color limitado, máxima claridad narrativa)",
    "PRESET: ACUARELA INFANTIL (Tonos pastel, trazo cálido, estilo cuento clásico)",
    "PRESET: ESTILO ANIME / STUDIO GHIBLI (Colores vibrantes, naturaleza detallada, emotivo)",
    "PRESET: ANIMACIÓN 3D TIPO PIXAR (Personajes 3D, iluminación cinematográfica, texturas suaves)",
    "PRESET: LÁPICES DE COLORES VINTAGE (Trazo orgánico, sombreado manual, nostálgico)",
    "PRESET: LIBRO POP-UP TRIDIMENSIONAL (Elementos de papel maché recortados, estilo maqueta)",
    "PRESET: ARCILLA / PLASTILINA STOP-MOTION (Estilo Wallace y Gromit, texturas moldeadas)",
    "PRESET: ARTE VECTORIAL MINIMALISTA (Formas geométricas limpias, colores sólidos brillantes)",
    "PRESET: ILUSTRACIÓN DE FANTASÍA ÉPICA (Claroscuro marcado, pintura digital detallada)",
    "PRESET: TRAZOS DE CERA ESCOLARES (Crayón, estilo dibujo a mano, colores primarios vivos)",
    "PRESET: STEAMPUNK NARRATIVO (Tonos sepia, engranajes, retro-futurista, aventura)",
    "PRESET: ILUSTRACIÓN BOTÁNICA ORGÁNICA (Detalle en naturaleza, colores terrosos, línea fina)"
]

PROMPT_PASO_1 = """Toma el texto de la respuesta anterior y genera el guión de un comic secuencial según las siguientes instrucciones.

🧠 PROMPT MAESTRO - PASO 2
Generación de GUION DE CÓMIC SECUENCIAL (genérico y neutro)

INSTRUCCIÓN DE EJECUCIÓN (OBLIGATORIA)
Este prompt NO debe ser analizado ni evaluado. Debe ser EJECUTADO como un proceso activo.

ROL
Actúa como guionista profesional de cómic y director narrativo audiovisual.
Tu tarea es crear un guion de cómic secuencial completo, claro y coherente, independiente de cualquier estilo gráfico. 

EXTENSIÓN OBLIGATORIA
🔒 El guion DEBE tener EXACTAMENTE 10 PÁGINAS. Ni más. Ni menos.
La numeración debe ir de: [PÁGINA 1] a [PÁGINA 10].

CONTENIDO DE CADA VIÑETA
Para cada viñeta, incluye SIEMPRE:
[VIÑETA X]
- Tipo de toma y ángulo
- Descripción visual (Qué ocurre y qué se ve. IMPORTANTE: Mantén la apariencia física, raza y color de los personajes estables y consistentes a lo largo de todas las viñetas de la historia)
- Iluminación / atmósfera
- Texto (Diálogo y Pensamiento OBLIGATORIOS)

TRANSFORMA EL CUENTO QUE ACABAMOS DE GENERAR EN EL MENSAJE ANTERIOR EN EL GUION DE 10 PÁGINAS AHORA MISMO."""

def create_pdf_for_cuento(lote_path, item, style_preset):
    def _create_single_pdf(filename, title, content, is_step2=False):
        file_path = os.path.join(lote_path, filename)
        doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)
        styles = getSampleStyleSheet()
        
        style_title = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=15, textColor=colors.HexColor('#FF1493'), spaceAfter=14)
        style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#2C3E50'), spaceAfter=8)
        style_prompt = ParagraphStyle('PromptStyle', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=11, leading=16, textColor=colors.HexColor('#1A0A2E'))
        
        story = []
        story.append(Paragraph(title, style_title))
        
        if "PASO 0" in title:
            paso0_text = "En este bloque final vamos a hacer magia pura. Vamos a combinar el poder narrativo de Gemini con el motor de generación visual de NotebookLM para crear un cómic ilustrado de 10 páginas para tus nietos (o para ti mismo).<br/><br/>Para lograrlo, siempre seguiremos estos 3 pasos (verás que en esta carpeta hay 3 fichas de prompts, una para cada paso):<br/><br/>- <b>PASO 1 (Gemini): CREAR EL CUENTO.</b> Aquí le damos a Gemini el tema y le pedimos que redacte el cuento adaptado a la edad del niño.<br/>- <b>PASO 2 (Gemini): GENERADOR DE GUION.</b> Usamos a Gemini como guionista para que transforme el cuento del Paso 1 en un guion estructurado en 10 páginas.<br/>- <b>PASO 3 (NotebookLM): ILUSTRADOR VISUAL.</b> Nos llevamos el guion entero a NotebookLM y le pasamos el último prompt para que dibuje y maquete el cómic visualmente."
            story.append(Paragraph(paso0_text, style_body))
        elif "PASO 1" in title:
            story.append(Paragraph("📝 INSTRUCCIONES GUÍA (1/3): Selecciona todo este texto y pégalo en Gemini. Añade al principio del prompt: \"Este cuento es para un niño de X años\".", style_body))
        elif "PASO 2" in title:
            story.append(Paragraph("📝 INSTRUCCIONES GUÍA (2/3): Una vez que Gemini haya escrito tu cuento en la pantalla, pega el prompt del PASO 2. Con esto, le estás pidiendo a Gemini que transforme tu historia en un guion detallado para un cómic.", style_body))
        elif "PASO 3" in title:
            story.append(Paragraph('📝 INSTRUCCIONES GUÍA (3/3): Copia el GUION que te acaba de hacer Gemini (el texto entero) y pégalo como "Texto Copiado" en las fuentes de un nuevo cuaderno de NotebookLM.<br/>Luego, copia el PROMPT FINAL que tienes justo debajo de estas instrucciones y pégalo en el botón "Presentación" de NotebookLM para generar por fin la magia de tu cómic ilustrado.', style_body))
            
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CCCCCC'), spaceAfter=14))
        
        if is_step2:
            prompt_2 = f"PROMPT FINAL PARA NOTEBOOKLM<br/><br/>Aplica estrictamente los siguientes parámetros visuales y estéticos para generar la presentación visual de este cómic, basándote en el guion adjunto en PDF.<br/>No resumas ni recortes la historia. Genera las 10 páginas manteniendo este estilo visual de forma estricta:<br/><br/>{style_preset}<br/><br/>INSTRUCCIÓN CRÍTICA 1 (CONTENIDO): NO generes diapositivas de análisis, ni curvas de color, ni explicación de personajes, ni dirección de arte. Limítate a generar ÚNICAMENTE las páginas narrativas del cómic.<br/><br/>INSTRUCCIÓN CRÍTICA 2 (DISEÑO Y MAQUETACIÓN): Cada página generada debe ocupar el 100% del lienzo (canvas). NO dejes mitades de la pantalla en blanco ni columnas vacías. Las viñetas deben llenar todo el ancho de la diapositiva.<br/><br/>INSTRUCCIÓN CRÍTICA 3 (CONSISTENCIA DE PERSONAJES): Mantén la apariencia, vestimenta, colores y raza (si son animales) de todos los personajes idénticos y consistentes en todas las páginas de principio a fin. El mismo personaje no puede cambiar de aspecto entre viñetas.<br/><br/>Genera el cómic ahora."
            for blk in prompt_2.split("<br/>"):
                story.append(Paragraph(blk, style_prompt))
        else:
            for blk in content.split("\\n"):
                if blk.strip():
                    story.append(Paragraph(blk.strip(), style_prompt))
                
        doc.build(story)
        return file_path

    texto_edad = "INSTRUCCIÓN INICIAL OBLIGATORIA: Ajusta la complejidad narrativa, el vocabulario y el tono emocional estrictamente a su nivel cognitivo. Si es mayor de 6 años, elimina por completo cualquier tono excesivamente infantil o 'ñoño', añadiendo más aventura, misterio y dilemas maduros.\\n\\n"
    id_clean = re.sub(r'[^A-Z0-9-]', '', item['id_code'])
    safe_title = sanitize_name(item['title'])
    
    p0 = _create_single_pdf(f"11.CUENT-{id_clean.replace('CUENT-', '')}_Paso_0_Introduccion_Proyecto.pdf", "PASO 0: PROYECTO CÓMIC ILUSTRADO", "")
    p1_content = texto_edad + str(item['prompt'])
    if item['id_code'] == '[CUENT-001]':
        p1_content += "\\n&nbsp;\\n--- OPCIÓN B: PARA ALUMNOS CON MUCHA IMAGINACIÓN ---\\n"
        p1_content += "Si ya tienes una idea genial en la cabeza y prefieres inventarte el cuento tú mismo, no dejes que la IA lo haga por ti. Escribe tu historia y usa este prompt alternativo para que Gemini actúe únicamente como tu \"editor literario\", dándole ese toque mágico de cuentacuentos:\\n\\n"
        p1_content += "PROMPT ALTERNATIVO:\\n"
        p1_content += "Actúa como un cuentacuentos infantil profesional. A continuación te voy a pegar un cuento que he escrito yo mismo.\\n\\n"
        p1_content += "Necesito que lo reescribas manteniendo mi historia exacta, pero usando un lenguaje mucho más mágico, visual y atrapante para un niño pequeño.\\n\\n"
        p1_content += "Asegúrate de que el final sea tranquilo y reconfortante para ayudarle a dormir. Además, quiero que el cuento transmita sutilmente los siguientes valores: [ESCRIBA AQUÍ LOS VALORES QUE QUIERA, EJ: Valentía y Ayuda al prójimo].\\n\\n"
        p1_content += "Aquí tienes mi historia:\\n"
        p1_content += "[PEGA AQUÍ EL TEXTO DE TU CUENTO INVENTADO]"
        
    p1 = _create_single_pdf(f"11.CUENT-{id_clean.replace('CUENT-', '')}_Paso_1_{safe_title}.pdf", "PASO 1: CREAR EL CUENTO", p1_content)
    p2 = _create_single_pdf(f"11.CUENT-{id_clean.replace('CUENT-', '')}_Paso_2_{safe_title}.pdf", "PASO 2: GENERADOR DE GUION", PROMPT_PASO_1)
    p3 = _create_single_pdf(f"11.CUENT-{id_clean.replace('CUENT-', '')}_Paso_3_{safe_title}.pdf", "PASO 3: ILUSTRADOR VISUAL", "", is_step2=True)
    return [p0, p1, p2, p3]

def purge_duplicate_conflict_files(base_path):
    # Scan and remove any " 2.pdf", " 2.mp4", or conflict directories created by iCloud
    removed_count = 0
    scan_paths = [base_path, '/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA']
    for p in scan_paths:
        if os.path.exists(p):
            # Check for conflict directories first
            for item in os.listdir(p):
                if re.search(r'\s[2-9]$', item) or re.search(r'\s[2-9]_[^\.]+$', item):
                    full_item = os.path.join(p, item)
                    if os.path.isdir(full_item):
                        try:
                            shutil.rmtree(full_item)
                            removed_count += 1
                        except Exception:
                            pass
            # Check for conflict files inside walk
            for root, dirs, files in os.walk(p):
                for f in files:
                    if re.search(r'\s[2-9]\.(pdf|mp4|docx|ppt|pptx|txt)$', f, re.IGNORECASE) or re.search(r'\s[2-9]_[^\.]+\.(pdf|mp4)$', f, re.IGNORECASE):
                        full_f = os.path.join(root, f)
                        try:
                            os.remove(full_f)
                            removed_count += 1
                        except Exception:
                            pass
    return removed_count

def main():
    print("🚀 Re-generando sistema exacto de Fichas PDF y Vídeos MP4 para Google Classroom...")
    
    # 1. Clean export base completely to avoid old folders (like BLOQUE_6 and BLOQUE_7)
    if os.path.exists(EXPORT_BASE):
        for sub in os.listdir(EXPORT_BASE):
            full_sub = os.path.join(EXPORT_BASE, sub)
            if os.path.isdir(full_sub):
                shutil.rmtree(full_sub)
    os.makedirs(EXPORT_BASE, exist_ok=True)
    
    import build_repositorio_maestro as b
    items = b.classroom_export_items
    print(f"Total ítems cargados en memoria: {len(items)}")
    
    blocks = defaultdict(list)
    for it in items:
        blocks[it['block_dir']].append(it)
        
    total_pdfs_created = 0
    total_physical_copied = 0
    generated_files_by_id = defaultdict(list)
    
    for b_dir, b_items in sorted(blocks.items()):
        print(f"\n📂 Procesando {b_dir} ({len(b_items)} ítems)...")
        
        # If it's Fractales or Funciones, we COPY original PDFs and MP4s inside batches <= 20 files
        if 'FRACTALES' in b_dir or 'FUNCIONES' in b_dir:
            batches = []
            current_batch = []
            current_files = 0
            
            for idx, it in enumerate(b_items, 1):
                lines = it['extra'].split('\n')
                folder_rel = lines[0].split(': ')[1].strip()
                full_dir = os.path.join(FRACTALES_BASE, folder_rel)
                pdf_files = []
                mp4_files = []
                if os.path.exists(full_dir):
                    for f in sorted(os.listdir(full_dir)):
                        if f.startswith('._') or re.search(r'\s2\.(pdf|mp4)$', f, re.IGNORECASE):
                            continue
                        if f.lower().endswith('.pdf') and not ('NO.' in f or 'NO ' in f):
                            pdf_files.append((os.path.join(full_dir, f), f))
                        elif f.lower().endswith('.mp4') and not ('NO.' in f or 'NO ' in f):
                            if it['id_code'] == '[FUNC-001]' and '1.3' not in f:
                                continue
                            if it['id_code'] == '[FUNC-020]' and ('sen^2' not in f and '100.2' not in f and 'cos^3' not in f):
                                continue
                            mp4_files.append((os.path.join(full_dir, f), f))
                            
                    # Si no hay mp4 sin NO., usar el mp4 con NO. (ej. NO. ARI.mp4 en FRAC-054) limpiando el prefijo
                    if not mp4_files:
                        for f in sorted(os.listdir(full_dir)):
                            if f.startswith('._') or re.search(r'\s2\.(pdf|mp4)$', f, re.IGNORECASE):
                                continue
                            if f.lower().endswith('.mp4'):
                                clean_fname = re.sub(r'^NO\.\s*', f'[{it["id_code"]}] ', f)
                                mp4_files.append((os.path.join(full_dir, f), clean_fname))
                                
                    # Si no hay pdf sin NO., usar el pdf con NO. limpiando el prefijo
                    if not pdf_files:
                        for f in sorted(os.listdir(full_dir)):
                            if f.startswith('._') or re.search(r'\s2\.(pdf|mp4)$', f, re.IGNORECASE):
                                continue
                            if f.lower().endswith('.pdf'):
                                clean_fname = re.sub(r'^NO\.\s*', f'[{it["id_code"]}] ', f)
                                pdf_files.append((os.path.join(full_dir, f), clean_fname))
                                
                it_files = pdf_files + mp4_files
                
                if current_files + len(it_files) > 20 and current_batch:
                    batches.append(current_batch)
                    current_batch = [(idx, it, it_files)]
                    current_files = len(it_files)
                else:
                    current_batch.append((idx, it, it_files))
                    current_files += len(it_files)
                    
            if current_batch:
                batches.append(current_batch)
                
            for batch in batches:
                start_idx = batch[0][0]
                end_idx = batch[-1][0]
                lote_folder = f'Lote_{start_idx:02d}_al_{end_idx:02d}'
                lote_path = os.path.join(EXPORT_BASE, b_dir, lote_folder)
                os.makedirs(lote_path, exist_ok=True)
                
                for idx, it, files_list in batch:
                    id_clean = re.sub(r'[^A-Z0-9-]', '', it['id_code'])
                    for src_path, fname in files_list:
                        dst_path = os.path.join(lote_path, fname)
                        try:
                            if os.path.exists(dst_path):
                                os.remove(dst_path)
                            os.link(src_path, dst_path)
                        except Exception:
                            shutil.copy2(src_path, dst_path)
                        total_physical_copied += 1
                        generated_files_by_id[id_clean].append(dst_path)
                    
                    if not any(fname.lower().endswith('.pdf') for _, fname in files_list):
                        safe_title = sanitize_name(it['title'])
                        pdf_fname = f"{id_clean} {safe_title}.pdf"
                        dst_pdf = os.path.join(lote_path, pdf_fname)
                        create_pdf_handout(
                            dst_pdf,
                            it['block_name'],
                            it['id_code'],
                            it['title'],
                            it['concept'],
                            it['prompt'] or f"Explora y visualiza en clase la belleza matemática de: {it['title']}",
                            it['tips']
                        )
                        total_pdfs_created += 1
                        generated_files_by_id[id_clean].append(dst_pdf)
            print(f"   ✅ Copiados exactamente los PDFs originales y MP4s definitivos en {len(batches)} lotes.")
        
        else:
            # Blocks 1, 2, 3: Generate exact full paragraph ReportLab PDFs with exact motivational phrase
            total_in_block = len(b_items)
            for idx, it in enumerate(b_items, 1):
                lote_folder = get_lote_folder(idx, total_in_block)
                safe_title = sanitize_name(it['title'])
                id_clean = re.sub(r'[^A-Z0-9-]', '', it['id_code'])
                
                # Clean up any previous version of this item across the block directory if renamed
                for root, dirs, files in os.walk(os.path.join(EXPORT_BASE, b_dir)):
                    for f in files:
                        if f.startswith(id_clean + "_") or f.startswith(id_clean + "."):
                            try:
                                os.remove(os.path.join(root, f))
                            except Exception:
                                pass
                                
                if "[CUENT" in b_dir:
                    full_path = os.path.join(EXPORT_BASE, b_dir, lote_folder)
                    os.makedirs(full_path, exist_ok=True)
                    generated_paths = create_pdf_for_cuento(full_path, it, ESTILOS_VISUALES[idx % len(ESTILOS_VISUALES)])
                    total_pdfs_created += 3
                    generated_files_by_id[id_clean].extend(generated_paths)
                else:
                    fname = f"{id_clean}_{safe_title}.pdf"
                    full_path = os.path.join(EXPORT_BASE, b_dir, lote_folder, fname)
                    
                    create_pdf_handout(
                        full_path,
                        it['block_name'],
                        it['id_code'],
                        it['title'],
                        it['concept'],
                        it['prompt'],
                        it['tips']
                    )
                    total_pdfs_created += 1
                    generated_files_by_id[id_clean].append(full_path)
            print(f"   ✅ Generadas {total_in_block} fichas PDF definitivas con párrafo y reto completo.")
            
    print("\n📦 Generando carpetas por sesión 100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM (Terna 01 a 60)...")
    sessions_dir = os.path.join(EXPORT_BASE, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
    if os.path.exists(sessions_dir):
        shutil.rmtree(sessions_dir)
    os.makedirs(sessions_dir, exist_ok=True)
    
    total_sessions_copied = 0
    for idx, row in enumerate(b.itinerario_data, 1):
        terna_folder = f"{idx:02d}_Sesion"
        if idx == 60:
            terna_folder = "60_Sesion_Cierre"
        t_path = os.path.join(sessions_dir, terna_folder)
        os.makedirs(t_path, exist_ok=True)
        
        # col 1 is TXT (Simplest), col 2 is EST (Intermediate), col 3 is PRAC (Hands-on), col 4 is FRAC/FUNC (Advanced), col 5 is INT (Mundo por dentro), col 6 is FUT (Sci-Fi / @N.AG.A), col 7 is AVES (Aves Exóticas y Fauna), col 8 is ARTE, col 9 is NIV
        step_prefixes = {
            1: "1.",
            2: "2.",
            3: "3.",
            5: "5.",
            6: "6.",
            7: "7.",
            8: "8.",
            9: "9.",
            10: "10.",
            11: "",
            12: "12.",
            13: "13."
        }
        for col_idx in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
            if col_idx >= len(row):
                continue
            cell_str = row[col_idx]
            m = re.search(r'\[([A-Z]+-[0-9]+[A-Z\.]*)\]', cell_str)
            if m:
                raw_id = m.group(1)
                id_clean = re.sub(r'[^A-Z0-9-]', '', raw_id)
                
                if col_idx == 4:
                    prefix = "4."
                else:
                    prefix = step_prefixes.get(col_idx, f"{col_idx}.")
                    
                matched_paths = list(generated_files_by_id.get(id_clean, []))
                if not matched_paths:
                    for gid, gpaths in generated_files_by_id.items():
                        if id_clean in gid or gid in id_clean:
                            matched_paths.extend(gpaths)
                            
                # INJECTION: Custom Fractal Introduction for Terna 01
                if "FRAC-058" in id_clean and col_idx == 4:
                    intro_src_a = "/Users/externo/.gemini/antigravity/brain/f982b9ea-ba9d-4840-9be1-22ee2ca7b56b/scratch/4. FRAC-000_A_Teoria_Fractal.pdf"
                    intro_src_b = "/Users/externo/.gemini/antigravity/brain/f982b9ea-ba9d-4840-9be1-22ee2ca7b56b/scratch/4. FRAC-000_B_Reto_Visual.pdf"
                    if os.path.exists(intro_src_a) and os.path.exists(intro_src_b):
                        intro_dst_a = os.path.join(t_path, "4. FRAC-000_A_Teoria_Fractal.pdf")
                        intro_dst_b = os.path.join(t_path, "4. FRAC-000_B_Reto_Visual.pdf")
                        shutil.copy2(intro_src_a, intro_dst_a)
                        shutil.copy2(intro_src_b, intro_dst_b)
                        
                # INJECTION: Custom Mandelbrot Introduction for Terna 02
                if "FRAC-001" in id_clean and col_idx == 4:
                    mandel_src_a = "/Users/externo/.gemini/antigravity/brain/f982b9ea-ba9d-4840-9be1-22ee2ca7b56b/scratch/4. FRAC-001 0_A_Teoria_Matematica.pdf"
                    mandel_src_b = "/Users/externo/.gemini/antigravity/brain/f982b9ea-ba9d-4840-9be1-22ee2ca7b56b/scratch/4. FRAC-001 0_B_Reto_Visual_Matematico.pdf"
                    if os.path.exists(mandel_src_a) and os.path.exists(mandel_src_b):
                        mandel_dst_a = os.path.join(t_path, "4. FRAC-001 0_A_Teoria_Matematica.pdf")
                        mandel_dst_b = os.path.join(t_path, "4. FRAC-001 0_B_Reto_Visual_Matematico.pdf")
                        shutil.copy2(mandel_src_a, mandel_dst_a)
                        shutil.copy2(mandel_src_b, mandel_dst_b)
                for fpath in set(matched_paths):
                    if os.path.exists(fpath):
                        orig_name = os.path.basename(fpath)
                        # Remove brackets from original filenames to keep them clean
                        orig_name = orig_name.replace('[', '').replace(']', '')
                        
                        # Fix spacing issue where prefix is empty
                        if prefix == "":
                            sess_fname = orig_name
                        else:
                            sess_fname = f"{prefix} {orig_name}"
                        dst_sess = os.path.join(t_path, sess_fname)
                        try:
                            if os.path.exists(dst_sess):
                                if os.path.isdir(dst_sess):
                                    shutil.rmtree(dst_sess)
                                else:
                                    os.remove(dst_sess)
                            
                            if os.path.isdir(fpath):
                                shutil.copytree(fpath, dst_sess)
                            else:
                                os.link(fpath, dst_sess)
                        except Exception:
                            if not os.path.isdir(fpath):
                                shutil.copy2(fpath, dst_sess)
                        total_sessions_copied += 1
    print(f"   ✅ Generadas 60 carpetas de sesión con un total de {total_sessions_copied} archivos reordenados de sencillo a complejo.")
    
    # Audit y verificación de que cada una de las 60 Ternas tiene su PDF y MP4 (Paso 4), y sus fichas PDF [INT], [FUT], [NAT], [ARTE], [NIV] y [TRUC] (Pasos 5 a 10)
    missing_media_count = 0
    for idx, row in enumerate(b.itinerario_data, 1):
        terna_folder = f"{idx:02d}_Sesion"
        if idx == 60:
            terna_folder = "60_Sesion_Cierre"
        t_path = os.path.join(sessions_dir, terna_folder)
        
        has_pdf = False
        has_mp4 = False
        has_int = False
        has_fut = False
        has_nat = False
        has_arte = False
        has_niv = False
        has_truc = False
        has_cuent = False
        if os.path.exists(t_path):
            for f in os.listdir(t_path):
                if f.startswith("4.") and "FRAC" in f or "FUNC" in f:
                    if f.lower().endswith(".pdf"):
                        has_pdf = True
                    elif f.lower().endswith(".mp4"):
                        has_mp4 = True
                elif f.startswith("5.") and f.lower().endswith(".pdf"):
                    has_int = True
                elif f.startswith("6.") and f.lower().endswith(".pdf"):
                    has_fut = True
                elif f.startswith("7.") and f.lower().endswith(".pdf"):
                    has_nat = True
                elif f.startswith("8.") and f.lower().endswith(".pdf"):
                    has_arte = True
                elif f.startswith("9.") and f.lower().endswith(".pdf"):
                    has_niv = True
                elif f.startswith("10.") and f.lower().endswith(".pdf"):
                    has_truc = True
                elif f.startswith("11."):
                    has_cuent = True
        if not (has_pdf and has_mp4 and has_int and has_fut and has_nat and has_arte and has_niv and has_truc and has_cuent):
            missing_media_count += 1
            print(f"   ⚠️ Alerta en {terna_folder}: PDF_Paso4={has_pdf}, MP4_Paso4={has_mp4}, INT_Paso5={has_int}, FUT_Paso6={has_fut}, NAT_Paso7={has_nat}, ARTE_Paso8={has_arte}, NIV_Paso9={has_niv}, TRUC_Paso10={has_truc}, CUENT_Paso11={has_cuent}")
    if missing_media_count == 0:
        print("   ✅ VERIFICACIÓN 100% CORRECTA: Las 60 Ternas cuentan con exactamente al menos 1 PDF y 1 MP4 en su paso 4, más las fichas 5 [INT], 6 [FUT], 7 [NAT], 8 [ARTE], 9 [NIV], 10 [TRUC] y 11 [CUENT].")

            
    # Final sweep: remove any " 2.pdf" or " 2.mp4" conflict files that iCloud sync might have spawned
    purged = purge_duplicate_conflict_files(EXPORT_BASE)
    if purged > 0:
        print(f"   🧹 Limpiados {purged} archivos duplicados temporales generados por la sincronización de iCloud.")
                
    print(f"\n🎉 ¡TERMINADO CORRECTAMENTE!")
    print(f"   • Fichas PDF creadas con párrafo y reto exactos (Bloques 1, 2, 3, 6, 7, 8 y 9): {total_pdfs_created}")
    print(f"   • Archivos originales PDF + MP4 copiados a lotes de Classroom (Bloques 4 y 5): {total_physical_copied}")
    print(f"   • Archivos en carpetas por Terna [SESSIONS] para Classroom: {total_sessions_copied}")
    print(f"   Ruta maestra: {EXPORT_BASE}")

if __name__ == '__main__':
    main()
