#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_fichas_talleres_nlm.py
Genera las dos fichas pedagógicas oficiales para Monográfico 2:
1. FICHA_TALLER_VIDEOJUEGOS_EDUCATIVOS_NOTEBOOKLM.pdf
2. FICHA_TALLER_PROFESOR_CORRECTOR_DE_APUNTES_NOTEBOOKLM.pdf
100% Python nativo estándar (sin dependencias externas).
"""

import os
import sys

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def escape_pdf_text(text):
    text = str(text)
    # Strip emojis and high unicode to avoid latin1 issues
    clean_chars = []
    for ch in text:
        if ord(ch) < 256:
            clean_chars.append(ch)
        else:
            clean_chars.append(' ')
    text = ''.join(clean_chars)
    text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    replacements = {
        'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
        'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
        'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
        '«': '<<', '»': '>>', '•': '-', '—': '-', '–': '-',
        'º': 'o', 'ª': 'a', '¿': '\xbf', '¡': '\xa1',
        '“': '"', '”': '"', '’': "'", '‘': "'"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def wrap_text(text, max_chars):
    paragraphs = str(text).split('\n')
    lines = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        words = p.split(' ')
        cur = []
        cur_len = 0
        for w in words:
            if not w:
                continue
            if cur_len + len(w) + 1 <= max_chars:
                cur.append(w)
                cur_len += len(w) + 1
            else:
                if cur:
                    lines.append(' '.join(cur))
                cur = [w]
                cur_len = len(w)
        if cur:
            lines.append(' '.join(cur))
    return lines

class SimplePDFBuilder:
    def __init__(self, title, doc_tag="MONOGRÁFICO 2"):
        self.title = title
        self.doc_tag = doc_tag
        self.pages = []
        self.cur_page_ops = []
        self.page_num = 1
        self.page_width = 595.28  # A4
        self.page_height = 841.89
        self.margin_left = 50
        self.margin_right = 50
        self.margin_top = 50
        self.margin_bottom = 50
        self.content_width = self.page_width - self.margin_left - self.margin_right
        self.cursor_y = self.page_height - self.margin_top
        self.start_new_page(first=True)

    def start_new_page(self, first=False):
        if not first:
            self.finalize_page()
            self.page_num += 1
        self.cur_page_ops = []
        self.cursor_y = self.page_height - self.margin_top
        self.draw_header_footer()

    def finalize_page(self):
        self.pages.append(list(self.cur_page_ops))

    def draw_header_footer(self):
        # Header banner
        ops = self.cur_page_ops
        ops.append("q")
        ops.append("0.05 0.08 0.15 rg") # Dark blue top bar
        ops.append("0 815 595.28 27 re f")
        ops.append("1 1 1 rg")
        ops.append("BT /F1 9 Tf 50 824 Td (%s - %s) Tj ET" % (
            escape_pdf_text(self.doc_tag), escape_pdf_text(self.title[:55])
        ))
        # Gold accent line
        ops.append("0.9 0.7 0.2 rg")
        ops.append("0 812 595.28 3 re f")
        # Footer
        ops.append("0.6 0.6 0.6 rg")
        ops.append("BT /F2 8 Tf 50 25 Td (Curso de Inteligencia Artificial para Alumnos Senior | Material Didactico Oficial) Tj ET")
        ops.append("BT /F1 8 Tf 520 25 Td (Pagina %d) Tj ET" % self.page_num)
        ops.append("Q")
        self.cursor_y = 780

    def check_space(self, needed_pt):
        if self.cursor_y - needed_pt < self.margin_bottom + 20:
            self.start_new_page()

    def add_title_block(self, main_title, subtitle, badge_text, badge_color=(0.14, 0.45, 0.9)):
        self.check_space(110)
        ops = self.cur_page_ops
        ops.append("q")
        # Badge
        r, g, b = badge_color
        ops.append(f"{r} {g} {b} rg")
        ops.append(f"50 {self.cursor_y - 18} 140 18 re f")
        ops.append("1 1 1 rg")
        ops.append(f"BT /F1 9 Tf 58 {self.cursor_y - 13} Td ({escape_pdf_text(badge_text)}) Tj ET")
        self.cursor_y -= 26

        # Main Title
        ops.append("0.08 0.12 0.25 rg")
        ops.append(f"BT /F1 18 Tf 50 {self.cursor_y - 16} Td ({escape_pdf_text(main_title)}) Tj ET")
        self.cursor_y -= 26

        # Subtitle
        ops.append("0.35 0.4 0.5 rg")
        lines = wrap_text(subtitle, 85)
        for line in lines:
            ops.append(f"BT /F2 10 Tf 50 {self.cursor_y - 10} Td ({escape_pdf_text(line)}) Tj ET")
            self.cursor_y -= 14

        ops.append("0.85 0.88 0.92 rg")
        ops.append(f"50 {self.cursor_y - 4} {self.content_width} 1 re f")
        ops.append("Q")
        self.cursor_y -= 16

    def add_section_header(self, text, icon=""):
        full_text = f"{icon} {text}".strip()
        self.check_space(40)
        ops = self.cur_page_ops
        ops.append("q")
        ops.append("0.1 0.2 0.45 rg")
        ops.append(f"BT /F1 13 Tf 50 {self.cursor_y - 12} Td ({escape_pdf_text(full_text)}) Tj ET")
        ops.append("0.2 0.45 0.85 rg")
        ops.append(f"50 {self.cursor_y - 16} 220 2 re f")
        ops.append("Q")
        self.cursor_y -= 26

    def add_paragraph(self, text, size=9.5, color=(0.15, 0.18, 0.22)):
        lines = wrap_text(text, 82)
        self.check_space(len(lines) * 14 + 8)
        ops = self.cur_page_ops
        ops.append("q")
        r, g, b = color
        ops.append(f"{r} {g} {b} rg")
        for line in lines:
            ops.append(f"BT /F2 {size} Tf 50 {self.cursor_y - 9} Td ({escape_pdf_text(line)}) Tj ET")
            self.cursor_y -= 13.5
        ops.append("Q")
        self.cursor_y -= 6

    def add_callout_box(self, title, text, bg_color=(0.94, 0.97, 1.0), border_color=(0.25, 0.5, 0.9)):
        lines = wrap_text(text, 78)
        box_h = 24 + len(lines) * 13 + 10
        self.check_space(box_h + 10)
        ops = self.cur_page_ops
        ops.append("q")
        br, bg, bb = bg_color
        ops.append(f"{br} {bg} {bb} rg")
        ops.append(f"50 {self.cursor_y - box_h} {self.content_width} {box_h} re f")
        dr, dg, db = border_color
        ops.append(f"{dr} {dg} {db} RG 1.5 w")
        ops.append(f"50 {self.cursor_y - box_h} {self.content_width} {box_h} re S")
        ops.append(f"{dr} {dg} {db} rg")
        ops.append(f"BT /F1 10.5 Tf 62 {self.cursor_y - 16} Td ({escape_pdf_text(title)}) Tj ET")
        ops.append("0.1 0.15 0.2 rg")
        cur_y = self.cursor_y - 30
        for line in lines:
            ops.append(f"BT /F2 9.2 Tf 62 {cur_y} Td ({escape_pdf_text(line)}) Tj ET")
            cur_y -= 13
        ops.append("Q")
        self.cursor_y -= (box_h + 10)

    def add_prompt_box(self, prompt_title, prompt_text):
        lines = wrap_text(prompt_text, 76)
        box_h = 24 + len(lines) * 12.5 + 12
        self.check_space(box_h + 10)
        ops = self.cur_page_ops
        ops.append("q")
        ops.append("0.97 0.98 0.99 rg") # Very light grey
        ops.append(f"50 {self.cursor_y - box_h} {self.content_width} {box_h} re f")
        ops.append("0.4 0.45 0.5 RG 1 w")
        ops.append(f"50 {self.cursor_y - box_h} {self.content_width} {box_h} re S")
        # Header strip
        ops.append("0.2 0.25 0.35 rg")
        ops.append(f"50 {self.cursor_y - 20} {self.content_width} 20 re f")
        ops.append("1 1 1 rg")
        ops.append(f"BT /F1 9 Tf 60 {self.cursor_y - 14} Td ({escape_pdf_text(prompt_title)}) Tj ET")
        # Text
        ops.append("0.05 0.1 0.18 rg")
        cur_y = self.cursor_y - 34
        for line in lines:
            ops.append(f"BT /F2 8.8 Tf 60 {cur_y} Td ({escape_pdf_text(line)}) Tj ET")
            cur_y -= 12.5
        ops.append("Q")
        self.cursor_y -= (box_h + 12)

    def add_table_row(self, col1, col2, is_header=False):
        self.check_space(26)
        ops = self.cur_page_ops
        ops.append("q")
        if is_header:
            ops.append("0.15 0.25 0.45 rg")
            ops.append(f"50 {self.cursor_y - 20} {self.content_width} 20 re f")
            ops.append("1 1 1 rg")
            ops.append(f"BT /F1 9 Tf 58 {self.cursor_y - 14} Td ({escape_pdf_text(col1)}) Tj ET")
            ops.append(f"BT /F1 9 Tf 230 {self.cursor_y - 14} Td ({escape_pdf_text(col2)}) Tj ET")
        else:
            ops.append("0.96 0.97 0.98 rg")
            ops.append(f"50 {self.cursor_y - 20} {self.content_width} 20 re f")
            ops.append("0.8 0.85 0.9 RG 0.5 w")
            ops.append(f"50 {self.cursor_y - 20} {self.content_width} 20 re S")
            ops.append("0.1 0.2 0.35 rg")
            ops.append(f"BT /F1 8.8 Tf 58 {self.cursor_y - 14} Td ({escape_pdf_text(col1)}) Tj ET")
            ops.append("0.2 0.25 0.3 rg")
            ops.append(f"BT /F2 8.5 Tf 230 {self.cursor_y - 14} Td ({escape_pdf_text(col2[:75])}) Tj ET")
        ops.append("Q")
        self.cursor_y -= 22

    def save_pdf(self, output_path):
        self.finalize_page()
        # Build raw PDF structure
        objs = []
        def add_obj(data):
            objs.append(data)
            return len(objs)

        # 1. Catalog
        # 2. Outlines
        # 3. Pages
        # 4. Font 1 (Helvetica-Bold)
        # 5. Font 2 (Helvetica)
        add_obj("<< /Type /Catalog /Pages 3 0 R >>")
        add_obj("<< /Type /Outlines /Count 0 >>")

        # Will update obj 3 after pages are created
        page_refs = []
        font_bold_id = 4
        font_reg_id = 5
        add_obj("<< /Type /Font /Subtype /Type1 /Name /F1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
        add_obj("<< /Type /Font /Subtype /Type1 /Name /F2 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")

        content_ids = []
        for p_ops in self.pages:
            content_str = "\n".join(p_ops)
            content_id = add_obj(f"<< /Length {len(content_str)} >>\nstream\n{content_str}\nendstream")
            content_ids.append(content_id)

        for cid in content_ids:
            page_id = add_obj(f"<< /Type /Page /Parent 3 0 R /MediaBox [0 0 {self.page_width} {self.page_height}] /Contents {cid} 0 R /Resources << /Font << /F1 {font_bold_id} 0 R /F2 {font_reg_id} 0 R >> >> >>")
            page_refs.append(f"{page_id} 0 R")

        objs[2] = f"<< /Type /Pages /Kids [{' '.join(page_refs)}] /Count {len(page_refs)} >>"

        # Write xref and trailer
        with open(output_path, 'wb') as f:
            f.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
            offsets = []
            for i, o in enumerate(objs):
                offsets.append(f.tell())
                f.write(f"{i+1} 0 obj\n{o}\nendobj\n".encode('latin1'))

            xref_pos = f.tell()
            f.write(f"xref\n0 {len(objs)+1}\n0000000000 65535 f \n".encode('latin1'))
            for off in offsets:
                f.write(f"{off:010d} 00000 n \n".encode('latin1'))

            f.write(f"trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode('latin1'))
        print(f"PDF generado con éxito ({len(self.pages)} págs): {output_path}")

def build_videojuegos_pdf():
    pdf = SimplePDFBuilder(
        title="Taller Videojuegos Educativos en Gemini Notebook (Hazme un sitio)",
        doc_tag="MONOGRÁFICO 2: GEMINI NOTEBOOK & STUDIO"
    )
    pdf.add_title_block(
        main_title="Creación de Videojuegos Educativos con Gemini Notebook",
        subtitle="Metodología paso a paso para transformar fuentes documentales en minijuegos interactivos de aprendizaje mediante la instrucción 'Hazme un sitio:' en el panel Studio.",
        badge_text="TALLER PRÁCTICO 1 • STUDIO INTERACTIVO",
        badge_color=(0.9, 0.25, 0.2)
    )

    pdf.add_section_header("1. Concepto y Funcionamiento de 'Hazme un sitio'", "🎮")
    pdf.add_paragraph(
        "En la nueva versión de Gemini Notebook, la pestaña 'Studio' (o la barra de prompts con fuentes activas) "
        "permite compilar aplicaciones web completas e interactivas sin necesidad de que el alumno programe una sola línea. "
        "Al comenzar el encargo con las palabras mágicas 'Hazme un sitio:', Gemini Notebook activa su motor de generación de interfaces interactivas "
        "y empaqueta el contenido directamente en un simulador visual con lógica en JavaScript, gráficos SVG limpios y un diseño adaptado a seniors."
    )
    pdf.add_paragraph(
        "El videojuego se nutre EXCLUSIVAMENTE de los documentos que el alumno ha marcado como fuentes activas (PDFs, apuntes, libros de texto o páginas web). "
        "Esto garantiza rigor científico absoluto: las preguntas, retos y respuestas correctas se fundamentan al 100% en los textos subidos, sin inventos ni alucinaciones."
    )

    pdf.add_callout_box(
        "Las 4 Reglas de Oro del Minijuego Educativo Senior",
        "1. Preguntas Directas con Retroalimentación: 3 a 5 preguntas basadas en las fuentes con explicación al fallar.\n"
        "2. Mecánica Dinámica Amigable: Marcador de tiempo (60 seg) y vidas (3 corazones) para generar emoción sin frustración.\n"
        "3. Ilustración SVG de Alta Calidad: Elementos visuales vectoriales integrados que representan la temática de la misión.\n"
        "4. Citas Rigurosas [1]: Cada explicación tras un fallo debe indicar la página y fuente de donde procede el dato verificado.",
        bg_color=(0.98, 0.95, 0.92),
        border_color=(0.9, 0.45, 0.1)
    )

    pdf.add_section_header("2. Caso Real Aplicado: Misión Apolo 11 (Historia y Ciencia)", "🚀")
    pdf.add_paragraph(
        "Para este taller utilizamos las fuentes oficiales del Apolo 11 (crónicas de la NASA, manuales del módulo lunar Eagle y datos históricos). "
        "El objetivo es que el alumno deba tomar decisiones de vuelo y responder preguntas técnicas y humanas para lograr el alunizaje en el Mar de la Tranquilidad."
    )

    pdf.add_prompt_box(
        "PROMPT MAESTRO PARA GEMINI NOTEBOOK (Copiar y pegar en Studio):",
        "Hazme un sitio: un videojuego educativo interactivo sobre la Misión Apolo 11 basado estrictamente en mis fuentes.\n"
        "Estructura y reglas obligatorias:\n"
        "1. Pantalla de Bienvenida: Título 'Misión Apolo 11: Rumbo a la Luna', botón grande 'Iniciar Descenso Lunar' y resumen de la misión.\n"
        "2. Mecánica de Juego: 3 vidas (corazones) y contador de 60 segundos de combustible. Cada respuesta correcta te acerca a la superficie.\n"
        "3. Batería de 5 Preguntas: Preguntas con 3 opciones sobre la alarma 1202, combustible restante, Armstrong, Aldrin y Collins.\n"
        "4. Explicación Didáctica al Fallar: Si el jugador falla, muestra una ventana con la explicación exacta y la cita documental [1].\n"
        "5. Gráficos Visuales: Incorpora un dibujo SVG elegante del Módulo Lunar Eagle sobrevolando los cráteres lunares con estrellas de fondo.\n"
        "6. Ergonomía Senior: Tipografía grande (mínimo 18px), botones con alto contraste y diseño adaptable a pantalla completa."
    )

    pdf.add_section_header("3. Cómo Probar y Compartir el Videojuego", "📲")
    pdf.add_table_row("Paso", "Acción Recomendada en Gemini Notebook", is_header=True)
    pdf.add_table_row("Paso 1: Pegar", "Pega el prompt en la barra inferior de Studio teniendo marcadas las fuentes del Apolo 11.")
    pdf.add_table_row("Paso 2: Generar", "Gemini Notebook procesará las fuentes y compilará el juego interactivo en la vista previa.")
    pdf.add_table_row("Paso 3: Jugar", "Pulsa 'Iniciar' y responde las preguntas observando cómo desciende el módulo lunar.")
    pdf.add_table_row("Paso 4: Compartir", "Pulsa el botón 'Compartir / Publicar' en la esquina superior para enviar el enlace a tus compañeros.")

    pdf.save_pdf(os.path.join(OUTPUT_DIR, "FICHA_TALLER_VIDEOJUEGOS_EDUCATIVOS_NOTEBOOKLM.pdf"))

def build_corrector_pdf():
    pdf = SimplePDFBuilder(
        title="Taller El Profesor que Corrige tus Apuntes en Gemini Notebook",
        doc_tag="MONOGRÁFICO 2: GEMINI NOTEBOOK & LIBROS DE TEXTO"
    )
    pdf.add_title_block(
        main_title="El Profesor que Corrige tus Apuntes (Con el Libro Delante)",
        subtitle="Cómo utilizar la nueva biblioteca de libros de texto integrados y gratuitos de Gemini Notebook para auditar, corregir y completar tus propios resúmenes con citas directas.",
        badge_text="TALLER PRÁCTICO 2 • AUDITORÍA DE CONOCIMIENTO",
        badge_color=(0.15, 0.65, 0.35)
    )

    pdf.add_section_header("1. La Revolución de las Fuentes: Libros de Texto Gratuitos", "📚")
    pdf.add_paragraph(
        "Una de las mayores innovaciones de la última versión de Gemini Notebook es la incorporación directa de libros de texto oficiales y gratuitos "
        "procedentes de bibliotecas académicas abiertas (como OpenStax y Open Textbook Library). "
        "Al pulsar sobre '+ Añadir fuentes', el alumno dispone de un selector directo de 'Libros de texto' ordenados por materias (Biología, Historia, Física, Economía, Anatomía). "
        "Ya no es necesario escanear cientos de páginas ni buscar archivos piratas: el libro completo de referencia queda precargado como fuente de verdad absoluta."
    )

    pdf.add_callout_box(
        "¿Por qué auditar apuntes con un Libro de Texto Oficial?",
        "• Detección Inmediata de Errores Conceptuales: Señala si confundiste un término o una cifra clave.\n"
        "• Omisiones Críticas: Te avisa de puntos fundamentales que el libro explica y tú olvidaste anotar.\n"
        "• Citas de Página [1]: Cada corrección incluye el número de página exacto del libro oficial para consultar.\n"
        "• Cero Alucinaciones: La corrección se circunscribe únicamente al texto académico validado.",
        bg_color=(0.93, 0.98, 0.94),
        border_color=(0.2, 0.7, 0.35)
    )

    pdf.add_section_header("2. Metodología de Trabajo en 3 Fases", "🔬")
    pdf.add_paragraph(
        "Para convertir a Gemini Notebook en tu tutor privado implacable, se sigue un procedimiento estructurado en 3 pasos:"
    )
    pdf.add_table_row("Fase", "Descripción de la Tarea Didáctica", is_header=True)
    pdf.add_table_row("1. La Fuente Canónica", "Selecciona y activa en '+ Añadir fuentes' el libro de texto oficial de la materia.")
    pdf.add_table_row("2. Subir tus Apuntes", "Sube tus notas (en texto, documento Word, PDF o fotografía de tu libreta manuscrita).")
    pdf.add_table_row("3. Ejecutar la Auditoría", "Lanza el prompt de corrección cruzada para que compare punto por punto ambos textos.")

    pdf.add_section_header("3. Los 3 Prompts Maestros del Profesor Corrector", "✍️")
    pdf.add_prompt_box(
        "PROMPT 1: AUDITORÍA DE ERRORES Y CONFUSIONES (Cruzar mis notas con el libro)",
        "Actúa como un profesor universitario riguroso pero pedagógico. Tengo dos fuentes activas:\n"
        "- Fuente 1: El libro de texto oficial de referencia.\n"
        "- Fuente 2: Mis notas y apuntes personales de clase.\n\n"
        "Compara mis apuntes con el libro de texto y redacta un informe con 3 apartados:\n"
        "1. Errores o imprecisiones en mis notas: Frases de mis apuntes que contradicen o distorsionan lo que dice el libro.\n"
        "2. Citas textuales del libro [1]: Indica exactamente la página y el párrafo donde el libro aclara cada punto.\n"
        "3. Nivel de gravedad: Califica cada fallo como (Leve, Moderado o Crítico) y redacta la versión corregida de mi frase."
    )

    pdf.add_prompt_box(
        "PROMPT 2: EL MAPA DE VACÍOS (Lo que olvidé anotar)",
        "Analiza el tema cubierto en mis apuntes y compáralo con el capítulo correspondiente del libro de texto oficial.\n"
        "Identifica los 3 conceptos o datos fundamentales que el libro explica detalladamente pero que yo he omitido por completo en mis notas.\n"
        "Redáctalos en forma de ficha de ampliación con lenguaje claro y citas [1] para que pueda incorporarlos a mi libreta."
    )

    pdf.add_prompt_box(
        "PROMPT 3: EL EXAMEN DE SIMULACRO PERSONALIZADO",
        "Diseña un test de 5 preguntas sobre los puntos más débiles de mis apuntes detectados en la auditoría anterior.\n"
        "Por cada pregunta, incluye 3 opciones (A, B, C) y explica por qué la correcta coincide con la doctrina del libro de texto."
    )

    pdf.save_pdf(os.path.join(OUTPUT_DIR, "FICHA_TALLER_PROFESOR_CORRECTOR_DE_APUNTES_NOTEBOOKLM.pdf"))

if __name__ == "__main__":
    build_videojuegos_pdf()
    build_corrector_pdf()
