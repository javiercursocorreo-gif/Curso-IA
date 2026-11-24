#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_fichas_talleres_nlm.py
Genera las dos fichas pedagógicas oficiales para Monográfico 2:
1. FICHA_TALLER_VIDEOJUEGOS_EDUCATIVOS_NOTEBOOKLM.pdf
2. FICHA_TALLER_PROFESOR_CORRECTOR_DE_APUNTES_NOTEBOOKLM.pdf

Diseño 100% calibrado, tipografía sobria y elegante (tamaño 12-13pt máximo en título, 
cero letras gigantescas, fondos limpios amigables con impresión y estructura de 2 páginas).
100% Python nativo estándar (sin dependencias externas).
"""

import os
import sys

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def escape_pdf_text(text):
    text = str(text)
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

def wrap_text(text, max_chars=78):
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
    return lines or ['']

class RobustPDFWriter:
    def __init__(self, w=595, h=842):
        self.w = w
        self.h = h
        self.pages = []
        self.current_stream = []

    def new_page(self):
        if self.current_stream:
            self.pages.append("".join(self.current_stream))
            self.current_stream = []

    def set_fill_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} rg\n")

    def set_stroke_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} RG\n")

    def set_line_width(self, w):
        self.current_stream.append(f"{w:.2f} w\n")

    def rect(self, x, y, w, h, fill=True, stroke=True):
        op = "B\n" if (fill and stroke) else ("f\n" if fill else "S\n")
        self.current_stream.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}")

    def line(self, x1, y1, x2, y2):
        self.current_stream.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S\n")

    def draw_text(self, x, y, text, font="F1", size=9.0, r=0.0, g=0.0, b=0.0):
        escaped = escape_pdf_text(text)
        self.current_stream.append(f"BT /{font} {size:.1f} Tf {x:.2f} {y:.2f} Td {r:.3f} {g:.3f} {b:.3f} rg ({escaped}) Tj ET\n")

    def save(self, filename):
        if self.current_stream:
            self.pages.append("".join(self.current_stream))
            self.current_stream = []

        f1_idx, f2_idx, f3_idx = 3, 4, 5
        page_obj_indices = []
        content_obj_indices = []
        cur_obj_idx = 6

        for _ in self.pages:
            page_obj_indices.append(cur_obj_idx)
            cur_obj_idx += 1
            content_obj_indices.append(cur_obj_idx)
            cur_obj_idx += 1

        kids_str = " ".join([f"{idx} 0 R" for idx in page_obj_indices])
        pages_dict = f"<< /Type /Pages /Kids [{kids_str}] /Count {len(self.pages)} >>".encode('ascii')

        all_objs = [
            b"<< /Type /Catalog /Pages 2 0 R >>",
            pages_dict,
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>"
        ]

        for p_idx, c_idx in zip(page_obj_indices, content_obj_indices):
            p_obj = f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.w} {self.h}] /Contents {c_idx} 0 R /Resources << /Font << /F1 {f1_idx} 0 R /F2 {f2_idx} 0 R /F3 {f3_idx} 0 R >> >> >>".encode('ascii')
            p_stream = self.pages[(p_idx - 6) // 2]
            c_bytes = p_stream.encode('latin-1', errors='replace')
            c_obj = f"<< /Length {len(c_bytes)} >>\nstream\n".encode('ascii') + c_bytes + b"\nendstream"
            all_objs.append(p_obj)
            all_objs.append(c_obj)

        with open(filename, "wb") as f:
            f.write(b"%PDF-1.4\n")
            offsets = []
            for obj in all_objs:
                offsets.append(f.tell())
                obj_id = len(offsets)
                f.write(f"{obj_id} 0 obj\n".encode('ascii'))
                f.write(obj)
                f.write(b"\nendobj\n")

            xref_start = f.tell()
            f.write(f"xref\n0 {len(offsets) + 1}\n0000000000 65535 f \n".encode('ascii'))
            for off in offsets:
                f.write(f"{off:010d} 00000 n \n".encode('ascii'))

            f.write(f"trailer\n<< /Size {len(offsets) + 1} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF\n".encode('ascii'))
        print(f"Ficha generada con éxito ({len(self.pages)} págs): {filename}")

class RetoPDFBuilder:
    def __init__(self, filename, title_badge, title_main, subtitle_main, border_color=(0.15, 0.35, 0.65)):
        self.filename = filename
        self.pdf = RobustPDFWriter()
        self.title_badge = title_badge
        self.title_main = title_main
        self.subtitle_main = subtitle_main
        self.border_color = border_color
        self.margin_x = 40
        self.content_w = 515
        self.cur_y = 800

    def draw_banner_p1(self):
        # Cabecera sobria y limpia (Fondo blanco, caja con borde elegante, tipografía 12.5pt)
        self.pdf.set_fill_color(1.0, 1.0, 1.0)
        self.pdf.set_stroke_color(self.border_color[0], self.border_color[1], self.border_color[2])
        self.pdf.set_line_width(1.2)
        self.pdf.rect(self.margin_x, 744, self.content_w, 64, fill=True, stroke=True)

        self.pdf.draw_text(self.margin_x + 14, 792, self.title_badge.upper(), font="F2", size=8.2, r=self.border_color[0], g=self.border_color[1], b=self.border_color[2])
        self.pdf.draw_text(self.margin_x + 14, 772, self.title_main, font="F2", size=12.5, r=0.10, g=0.15, b=0.25)
        self.pdf.draw_text(self.margin_x + 14, 754, self.subtitle_main, font="F1", size=8.2, r=0.35, g=0.40, b=0.48)
        self.cur_y = 730

    def draw_header_p2(self, p2_label):
        self.pdf.set_fill_color(0.97, 0.98, 0.99)
        self.pdf.set_stroke_color(self.border_color[0], self.border_color[1], self.border_color[2])
        self.pdf.set_line_width(0.8)
        self.pdf.rect(self.margin_x, 794, self.content_w, 20, fill=True, stroke=True)
        self.pdf.draw_text(self.margin_x + 10, 800, p2_label.upper(), font="F2", size=8.2, r=self.border_color[0], g=self.border_color[1], b=self.border_color[2])
        self.pdf.draw_text(self.margin_x + self.content_w - 200, 800, "GEMINI NOTEBOOK • CURSO DE IA SENIOR", font="F1", size=7.5, r=0.4, g=0.45, b=0.55)
        self.cur_y = 778

    def draw_footer(self, p_num):
        self.pdf.set_stroke_color(0.82, 0.84, 0.88)
        self.pdf.set_line_width(0.5)
        self.pdf.line(self.margin_x, 32, self.margin_x + self.content_w, 32)
        self.pdf.draw_text(self.margin_x, 21, f"Curso de IA - Monografico 2: Gemini Notebook - {self.title_main[:55]}", font="F1", size=7.5, r=0.4, g=0.45, b=0.5)
        self.pdf.draw_text(self.margin_x + self.content_w - 75, 21, f"Pagina {p_num} de 2", font="F2", size=8.0, r=0.2, g=0.25, b=0.35)

    def add_major_section_header(self, num_str, title, subtitle=None, color_rgb=None, force_new_page=False):
        if force_new_page and self.cur_y < 760:
            self.pdf.new_page()
            self.cur_y = 794

        c = color_rgb or self.border_color
        
        # Barra superior de acento
        self.pdf.set_fill_color(c[0], c[1], c[2])
        self.pdf.rect(self.margin_x, self.cur_y - 2, self.content_w, 3, fill=True, stroke=False)
        self.cur_y -= 12

        # Caja destacada para el título grande (13.5pt)
        h_box = 30 if subtitle else 24
        bg_r = c[0] * 0.12 + 0.88
        bg_g = c[1] * 0.12 + 0.88
        bg_b = c[2] * 0.12 + 0.88
        self.pdf.set_fill_color(bg_r, bg_g, bg_b)
        self.pdf.set_stroke_color(c[0], c[1], c[2])
        self.pdf.set_line_width(1.0)
        self.pdf.rect(self.margin_x, self.cur_y - h_box + 14, self.content_w, h_box, fill=True, stroke=True)

        full_title = f"{num_str}. {title.upper()}"
        self.pdf.draw_text(self.margin_x + 10, self.cur_y, full_title, font="F2", size=13.0, r=c[0], g=c[1], b=c[2])
        if subtitle:
            self.pdf.draw_text(self.margin_x + 10, self.cur_y - 13, subtitle, font="F1", size=8.2, r=0.25, g=0.30, b=0.38)
            self.cur_y -= (h_box + 8)
        else:
            self.cur_y -= (h_box + 6)

    def add_section_title(self, title, color_rgb=None):
        c = color_rgb or self.border_color
        self.pdf.set_fill_color(c[0], c[1], c[2])
        self.pdf.rect(self.margin_x, self.cur_y - 2, self.content_w, 16, fill=True, stroke=False)
        self.pdf.draw_text(self.margin_x + 8, self.cur_y + 3, title.upper(), font="F2", size=8.0, r=1.0, g=1.0, b=1.0)
        self.cur_y -= 23

    def add_card_white(self, title, lines_list, border_color=(0.78, 0.82, 0.88), title_color=None):
        tc = title_color or self.border_color
        line_spacing = 12.8
        rendered_lines = []
        for it in lines_list:
            it_wrapped = wrap_text(it, max_chars=78)
            rendered_lines.append(it_wrapped)

        total_lines = sum(len(l) for l in rendered_lines)
        h_box = 20 + (total_lines * line_spacing) + 8

        self.pdf.set_fill_color(1.0, 1.0, 1.0)
        self.pdf.set_stroke_color(border_color[0], border_color[1], border_color[2])
        self.pdf.set_line_width(0.8)
        self.pdf.rect(self.margin_x, self.cur_y - h_box + 14, self.content_w, h_box, fill=True, stroke=True)

        self.pdf.draw_text(self.margin_x + 10, self.cur_y, title, font="F2", size=8.8, r=tc[0], g=tc[1], b=tc[2])
        
        y_text = self.cur_y - 14
        for block in rendered_lines:
            for l in block:
                self.pdf.draw_text(self.margin_x + 10, y_text, l, font="F1", size=8.5, r=0.20, g=0.25, b=0.30)
                y_text -= line_spacing
            y_text -= 1.0

        self.cur_y -= (h_box + 8)

    def add_prompt_card(self, title, prompt_lines):
        line_spacing = 12.2
        rendered_lines = []
        for it in prompt_lines:
            it_wrapped = wrap_text(it, max_chars=76)
            rendered_lines.append(it_wrapped)

        total_lines = sum(len(l) for l in rendered_lines)
        h_box = 20 + (total_lines * line_spacing) + 8

        self.pdf.set_fill_color(0.98, 0.98, 0.99)
        self.pdf.set_stroke_color(0.70, 0.74, 0.80)
        self.pdf.set_line_width(0.8)
        self.pdf.rect(self.margin_x, self.cur_y - h_box + 14, self.content_w, h_box, fill=True, stroke=True)

        self.pdf.draw_text(self.margin_x + 10, self.cur_y, title, font="F2", size=8.6, r=0.15, g=0.20, b=0.30)
        
        y_text = self.cur_y - 14
        for block in rendered_lines:
            for l in block:
                self.pdf.draw_text(self.margin_x + 10, y_text, l, font="F1", size=8.2, r=0.08, g=0.12, b=0.20)
                y_text -= line_spacing
            y_text -= 1.0

        self.cur_y -= (h_box + 8)

    def save(self):
        self.pdf.save(self.filename)

def build_videojuegos_pdf_clean():
    pdf_path = os.path.join(OUTPUT_DIR, "FICHA_TALLER_VIDEOJUEGOS_EDUCATIVOS_NOTEBOOKLM.pdf")
    builder = RetoPDFBuilder(
        filename=pdf_path,
        title_badge="TALLER PRÁCTICO 1 • GEMINI NOTEBOOK & STUDIO",
        title_main="Taller: Creación de Videojuegos Educativos con Gemini Notebook",
        subtitle_main="Transformación de fuentes documentales en minijuegos interactivos mediante la instrucción 'Hazme un sitio:'",
        border_color=(0.85, 0.25, 0.20)
    )

    # === PÁGINA 1 ===
    builder.draw_banner_p1()

    builder.add_major_section_header("1", "CONCEPTO CLAVE: ¿QUÉ SIGNIFICA 'HAZME UN SITIO:'?", "El comando de activación del motor web interactivo de Google", color_rgb=(0.85, 0.25, 0.20))
    builder.add_card_white(
        title="El comando del sistema que activa el motor web de Gemini",
        lines_list=[
            "- 'Hazme un sitio:' NO es el título del videojuego ni aparece en la pantalla del alumno.",
            "- Es el 'prompt de activación' interno (trigger) de Google para indicarle a Gemini que no responda con texto plano ni con un resumen escrito, sino que compile una página web completa (sitio HTML/JS/CSS interactivo).",
            "- Al anteponer 'Hazme un sitio:', el motor genera directamente la vista previa en Studio con botones táctiles, contador de vidas y lógica interactiva sin que el alumno tenga que programar.",
            "- El juego se nutre exclusivamente de las fuentes activas (PDFs y apuntes), garantizando rigor y cero inventos."
        ],
        border_color=(0.85, 0.40, 0.35),
        title_color=(0.80, 0.20, 0.15)
    )

    builder.add_major_section_header("2", "CASO REAL APLICADO: MISIÓN APOLO 11 (HISTORIA Y CIENCIA)", "Simulador interactivo del alunizaje con fuentes de la NASA", color_rgb=(0.85, 0.25, 0.20))
    builder.add_card_white(
        title="Objetivo pedagógico en el aula senior",
        lines_list=[
            "- Fuentes activas: Crónicas oficiales de la NASA y manual del módulo lunar Eagle de la Clase 2.",
            "- Misión del alumno: Responder preguntas técnicas e históricas para lograr el alunizaje en el Mar de la Tranquilidad.",
            "- Las 4 reglas de oro: 3 vidas (corazones), 60 segundos de tiempo, gráficos SVG vectoriales y citas documentales [1] al fallar."
        ],
        border_color=(0.85, 0.50, 0.45),
        title_color=(0.75, 0.20, 0.15)
    )

    builder.add_major_section_header("3", "PROMPT MAESTRO PARA COPIAR Y PEGAR EN STUDIO", "Instrucciones de diseño y ergonomía senior listas para ejecutar", color_rgb=(0.85, 0.25, 0.20))
    builder.add_prompt_card(
        title="Prompt estructurado (pegar en la barra inferior de Gemini Notebook con fuentes activas):",
        prompt_lines=[
            "Hazme un sitio: un videojuego educativo interactivo sobre la Misión Apolo 11 basado estrictamente en mis fuentes.",
            "Reglas y diseño obligatorio para alumnos mayores (+65):",
            "1. Portada: Título 'Misión Apolo 11: Rumbo a la Luna' y botón grande 'Iniciar Descenso Lunar'.",
            "2. Mecánica: 3 vidas (corazones) y contador de 60 segundos. Cada acierto desciende la nave hacia la superficie.",
            "3. Batería de 5 preguntas sobre la alarma 1202, combustible restante, Armstrong, Aldrin y Collins.",
            "4. Retroalimentación con rigor [1]: Al fallar, muestra una ventana con la cita exacta de la fuente.",
            "5. Gráfico SVG: Ilustración vectorial del Módulo Lunar Eagle sobrevolando los cráteres lunares.",
            "6. Ergonomía senior: Letra grande (18px), botones de alto contraste y pantalla completa táctil."
        ]
    )

    builder.draw_footer(1)

    # === PÁGINA 2 ===
    builder.pdf.new_page()
    builder.draw_header_p2("GUÍA DE EJECUCIÓN, PRUEBA Y COMPARTICIÓN")

    builder.add_major_section_header("4", "PASO A PASO DIDÁCTICO EN EL AULA (FLUJO EN 4 ETAPAS)", "De la selección de fuentes a la publicación en WhatsApp", color_rgb=(0.85, 0.25, 0.20))
    builder.add_card_white(
        title="Procedimiento en el ordenador o tablet del alumno",
        lines_list=[
            "Paso 1 (Marcar fuentes): Comprobar en el panel izquierdo que los documentos del Apolo 11 están seleccionados.",
            "Paso 2 (Pegar prompt): Copiar el texto del recuadro anterior y pegarlo en la barra de Studio.",
            "Paso 3 (Generación en directo): Gemini compilará el juego interactivo en modo vista previa sin mostrar código.",
            "Paso 4 (Probar y compartir): Jugar la partida y usar el botón superior 'Compartir / Publicar' para enviar el enlace a WhatsApp."
        ],
        border_color=(0.85, 0.50, 0.45),
        title_color=(0.75, 0.20, 0.15)
    )

    builder.add_major_section_header("5", "PREGUNTAS DE REFLEXIÓN TRAS LA PARTIDA", "Diálogo guiado con el profesor sobre rigor y aprendizaje", color_rgb=(0.85, 0.25, 0.20))
    builder.add_card_white(
        title="Diálogo guiado con el profesor",
        lines_list=[
            "1. Rigor vs. Alucinación: ¿Pudo el juego inventar alguna pregunta que no figurase en el manual de la NASA?",
            "2. Accesibilidad: ¿Resultó legible la tipografía de 18px y comprensible el marcador de tiempo y vidas?",
            "3. Ampliación a otros temas: ¿Cómo adaptar este mismo prompt a la historia familiar, recetas o viajes?"
        ],
        border_color=(0.80, 0.82, 0.88),
        title_color=(0.20, 0.25, 0.35)
    )

    builder.draw_footer(2)
    builder.save()

def build_corrector_pdf_clean():
    pdf_path = os.path.join(OUTPUT_DIR, "FICHA_TALLER_PROFESOR_CORRECTOR_DE_APUNTES_NOTEBOOKLM.pdf")
    builder = RetoPDFBuilder(
        filename=pdf_path,
        title_badge="TALLER PRÁCTICO 2 • GEMINI NOTEBOOK & AUDITORÍA",
        title_main="Taller: El Profesor que Corrige tus Apuntes (Con el Libro Delante)",
        subtitle_main="Auditoría cruzada de notas personales frente a los Libros de Texto Gratuitos integrados en Gemini Notebook",
        border_color=(0.15, 0.55, 0.30)
    )

    # === PÁGINA 1 ===
    builder.draw_banner_p1()

    builder.add_major_section_header("1", "LA REVOLUCIÓN DE LAS FUENTES: LIBROS DE TEXTO GRATUITOS", "Biblioteca académica abierta integrada (OpenStax y Open Textbook Library)", color_rgb=(0.15, 0.55, 0.30))
    builder.add_card_white(
        title="Biblioteca académica abierta integrada (OpenStax y Open Textbook Library)",
        lines_list=[
            "- Al pulsar sobre '+ Añadir fuentes', Gemini Notebook ofrece un catálogo de 'Libros de texto' gratuitos precargados.",
            "- El alumno no necesita escanear manuales pesados: dispone del libro universitario oficial de la materia en 1 clic.",
            "- Al cruzar tus notas personales contra el libro, Gemini actúa como un tutor implacable con citas exactas [1]."
        ],
        border_color=(0.35, 0.70, 0.45),
        title_color=(0.10, 0.45, 0.25)
    )

    builder.add_major_section_header("2", "PROCEDIMIENTO METODOLÓGICO EN 3 FASES", "De la fuente canónica al informe de auditoría con citas [1]", color_rgb=(0.15, 0.55, 0.30))
    builder.add_card_white(
        title="Fases de trabajo",
        lines_list=[
            "Fase 1 (La Fuente Canónica): Activar el libro de texto oficial gratuito de la materia (Biología, Historia o Economía).",
            "Fase 2 (Subir tus Apuntes): Subir tus notas de clase (documento Word, PDF o fotografía de tu libreta manuscrita).",
            "Fase 3 (Lanzar la Auditoría): Ejecutar el prompt cruzado para que evalúe precisión, omisiones y conceptos erróneos."
        ],
        border_color=(0.35, 0.70, 0.45),
        title_color=(0.10, 0.45, 0.25)
    )

    builder.add_major_section_header("3", "PROMPT MAESTRO 1: AUDITORÍA DE ERRORES Y CITAS [1]", "Instrucción de corrección pedagógica estructurada con citas", color_rgb=(0.15, 0.55, 0.30))
    builder.add_prompt_card(
        title="Prompt de corrección cruzada (copiar y pegar en Gemini Notebook):",
        prompt_lines=[
            "Actúa como un profesor riguroso pero pedagógico. Tengo dos fuentes activas:",
            "- Fuente 1: El libro de texto oficial de referencia.",
            "- Fuente 2: Mis notas y apuntes personales de clase.",
            "Compara mis apuntes con el libro de texto y redacta un informe estructurado:",
            "1. Errores o imprecisiones: Señala frases de mis notas que contradigan lo que afirma el libro.",
            "2. Citas textuales [1]: Cita exactamente la página y párrafo del libro oficial que aclara el punto.",
            "3. Versión corregida: Redacta la frase correcta con lenguaje claro para que pueda actualizar mi libreta."
        ]
    )

    builder.draw_footer(1)

    # === PÁGINA 2 ===
    builder.pdf.new_page()
    builder.draw_header_p2("PROMPTS COMPLEMENTARIOS Y AUDITORÍA PROFUNDA")

    builder.add_major_section_header("4", "PROMPT MAESTRO 2: EL MAPA DE VACÍOS (LO QUE OLVIDÉ ANOTAR)", "Detección de omisiones críticas frente al manual oficial", color_rgb=(0.15, 0.55, 0.30))
    builder.add_prompt_card(
        title="Prompt para detectar omisiones críticas:",
        prompt_lines=[
            "Analiza el tema cubierto en mis apuntes y compáralo con el capítulo correspondiente del libro de texto oficial.",
            "Identifica los 3 conceptos fundamentales que el libro explica con detalle pero que yo he omitido por completo en mis notas.",
            "Redáctalos como una ficha de ampliación con lenguaje comprensible y citas de página [1] para enriquecer mi estudio."
        ]
    )

    builder.add_major_section_header("5", "PROMPT MAESTRO 3: SIMULACRO DE TEST PERSONALIZADO", "Autoevaluación sobre los puntos débiles detectados", color_rgb=(0.15, 0.55, 0.30))
    builder.add_prompt_card(
        title="Prompt para autoevaluación en clase:",
        prompt_lines=[
            "Diseña un examen tipo test de 5 preguntas centrado en los puntos más débiles de mis apuntes detectados en la auditoría.",
            "Cada pregunta debe tener 3 opciones (A, B, C) y una explicación detallada indicando por qué la opción correcta coincide con el libro."
        ]
    )

    builder.add_major_section_header("6", "VALOR EDUCATIVO PARA PERSONAS MAYORES", "Tranquilidad cognitiva, rigor y aprendizaje guiado", color_rgb=(0.15, 0.55, 0.30))
    builder.add_card_white(
        title="Tranquilidad cognitiva y aprendizaje guiado",
        lines_list=[
            "- Elimina la inseguridad de dudar si los apuntes tomados a mano contienen errores.",
            "- Enseña a apoyarse en fuentes canónicas validadas en lugar de buscar respuestas dudosas en internet.",
            "- Desarrolla el pensamiento crítico comparativo y la precisión conceptual a cualquier edad."
        ],
        border_color=(0.80, 0.82, 0.88),
        title_color=(0.20, 0.25, 0.35)
    )

    builder.draw_footer(2)
    builder.save()

if __name__ == "__main__":
    build_videojuegos_pdf_clean()
    build_corrector_pdf_clean()
