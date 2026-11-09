#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_pdf_guia_nlm.py
Genera 'GUIA_COMPLETA_ALUMNO_NOTEBOOKLM_Y_PRACTICAS.pdf' con diseño amplio, espaciado,
cero solapamientos, interlineado holgado para personas mayores y casos de prueba
exhaustivos botón a botón para el panel Studio (con prompts de estilo, infografías y fuentes reales).
100% Python nativo estándar (sin ReportLab, sin pip, sin dependencias externas).
"""

import os
import sys

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_OUTPUT = os.path.join(OUTPUT_DIR, "GUIA_COMPLETA_ALUMNO_NOTEBOOKLM_Y_PRACTICAS.pdf")

def escape_pdf_text(text):
    text = str(text)
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
    return lines or ['']

class RobustPDFWriter:
    def __init__(self, page_width=595.28, page_height=841.89): # A4
        self.w = page_width
        self.h = page_height
        self.pages = []
        self.current_stream = []

    def start_page(self):
        self.current_stream = []

    def end_page(self):
        self.pages.append("".join(self.current_stream))
        self.current_stream = []

    def set_fill_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} rg\n")

    def set_stroke_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} RG\n")

    def set_line_width(self, width):
        self.current_stream.append(f"{width:.2f} w\n")

    def rect(self, x, y, width, height, fill=True, stroke=True):
        op = "B" if (fill and stroke) else ("f" if fill else "S")
        self.current_stream.append(f"{x:.2f} {y:.2f} {width:.2f} {height:.2f} re {op}\n")

    def line(self, x1, y1, x2, y2):
        self.current_stream.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S\n")

    def draw_text(self, x, y, text, font="F1", size=9.5, r=0, g=0, b=0):
        self.set_fill_color(r, g, b)
        escaped = escape_pdf_text(text)
        self.current_stream.append(f"BT /{font} {size} Tf {x:.2f} {y:.2f} Td ({escaped}) Tj ET\n")

    def write_to_file(self, filename):
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

        with open(filename, 'wb') as f:
            f.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
            xref_positions = [0]
            pos = f.tell()
            for idx, obj_bytes in enumerate(all_objs, start=1):
                xref_positions.append(pos)
                header = f"{idx} 0 obj\n".encode('ascii')
                footer = b"\nendobj\n"
                f.write(header + obj_bytes + footer)
                pos = f.tell()

            xref_start = pos
            f.write(f"xref\n0 {len(all_objs) + 1}\n".encode('ascii'))
            f.write(b"0000000000 65535 f \n")
            for p in xref_positions[1:]:
                f.write(f"{p:010d} 00000 n \n".encode('ascii'))

            trailer = f"trailer\n<< /Size {len(all_objs) + 1} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF\n".encode('ascii')
            f.write(trailer)

class FlowLayoutPDF:
    def __init__(self, writer):
        self.w = writer
        self.margin_x = 40
        self.content_w = self.w.w - (self.margin_x * 2)
        self.top_y = self.w.h - 55
        self.bottom_y = 50
        self.y = self.top_y
        self.page_num = 1
        self.w.start_page()

    def check_space(self, height_needed):
        if self.y - height_needed < self.bottom_y:
            self.w.end_page()
            self.page_num += 1
            self.w.start_page()
            self.y = self.top_y

    def add_section_header(self, title, color_rgb=(0.12, 0.25, 0.55)):
        self.check_space(38)
        self.y -= 10
        self.w.set_fill_color(color_rgb[0], color_rgb[1], color_rgb[2])
        self.w.rect(self.margin_x, self.y - 4, self.content_w, 20, fill=True, stroke=False)
        self.w.draw_text(self.margin_x + 10, self.y + 2, title.upper(), "F2", 9.2, 1, 1, 1)
        self.y -= 26

    def add_paragraph(self, text, font="F1", size=8.5, color=(0.2, 0.22, 0.26), line_spacing=13, max_chars=84):
        lines = wrap_text(text, max_chars)
        h = len(lines) * line_spacing
        self.check_space(h + 6)
        for l in lines:
            self.w.draw_text(self.margin_x, self.y, l, font, size, color[0], color[1], color[2])
            self.y -= line_spacing
        self.y -= 4

    def add_card_box(self, title, items, badge_text=None, border_color=(0.85, 0.88, 0.92), bg_color=(0.98, 0.98, 0.99), title_color=(0.12, 0.25, 0.55)):
        # Calcular altura total
        line_spacing = 13.5
        total_lines = 0
        rendered_items = []
        for it in items:
            it_lines = wrap_text(it, max_chars=80)
            rendered_items.append(it_lines)
            total_lines += len(it_lines)

        h_box = 24 + (total_lines * line_spacing) + 10
        self.check_space(h_box + 12)

        # Dibujar fondo y borde
        self.w.set_fill_color(bg_color[0], bg_color[1], bg_color[2])
        self.w.set_stroke_color(border_color[0], border_color[1], border_color[2])
        self.w.set_line_width(0.7)
        self.w.rect(self.margin_x, self.y - h_box + 14, self.content_w, h_box, fill=True, stroke=True)

        # Título y Badge
        self.w.draw_text(self.margin_x + 12, self.y - 2, title, "F2", 9, title_color[0], title_color[1], title_color[2])
        if badge_text:
            badge_x = self.margin_x + self.content_w - 90
            self.w.set_fill_color(title_color[0], title_color[1], title_color[2])
            self.w.rect(badge_x, self.y - 4, 80, 13, fill=True, stroke=False)
            self.w.draw_text(badge_x + 6, self.y - 1, badge_text, "F2", 7.2, 1, 1, 1)

        ty = self.y - 17
        for it_lines in rendered_items:
            for idx_l, line in enumerate(it_lines):
                prefix = "- " if idx_l == 0 else "  "
                fnt = "F2" if (idx_l == 0 and ":" in line) else "F1"
                self.w.draw_text(self.margin_x + 16, ty, prefix + line, fnt, 8.2, 0.20, 0.22, 0.26)
                ty -= line_spacing

        self.y = self.y - h_box - 4

    def add_prompt_box(self, label, prompt_text):
        lines = wrap_text(prompt_text, max_chars=78)
        line_spacing = 12.5
        h = len(lines) * line_spacing + 24
        self.check_space(h + 10)

        # Caja de código / prompt con borde suave
        self.w.set_fill_color(0.96, 0.98, 0.97)
        self.w.set_stroke_color(0.20, 0.60, 0.40)
        self.w.set_line_width(0.8)
        self.w.rect(self.margin_x + 8, self.y - h + 14, self.content_w - 16, h, fill=True, stroke=True)

        self.w.draw_text(self.margin_x + 18, self.y - 1, label, "F2", 8, 0.10, 0.45, 0.25)
        ty = self.y - 15
        for l in lines:
            self.w.draw_text(self.margin_x + 22, ty, l, "F3", 7.8, 0.12, 0.16, 0.20)
            ty -= line_spacing

        self.y = self.y - h - 6

def generar_pdf_completo():
    writer = RobustPDFWriter()
    flow = FlowLayoutPDF(writer)

    # -------------------------------------------------------------
    # PÁGINA 1: CABECERA & FUNDAMENTOS
    # -------------------------------------------------------------
    # Barra azul superior decorativa
    flow.w.set_fill_color(0.12, 0.25, 0.55)
    flow.w.rect(flow.margin_x, flow.y, flow.content_w, 5, fill=True, stroke=False)
    flow.y -= 20

    # Badge de cabecera
    flow.w.set_fill_color(0.90, 0.94, 0.99)
    flow.w.set_stroke_color(0.70, 0.82, 0.95)
    flow.w.rect(flow.margin_x, flow.y - 10, 310, 16, fill=True, stroke=True)
    flow.w.draw_text(flow.margin_x + 8, flow.y - 7, "CURSO DE IA PARA PERSONAS MAYORES (60+) • MONOGRÁFICO 2", "F2", 7.8, 0.12, 0.35, 0.70)
    flow.y -= 28

    # Título Principal
    flow.w.draw_text(flow.margin_x, flow.y, "MANUAL VISUAL COMPLETO Y TALLER: GEMINI NOTEBOOK", "F2", 15.5, 0.10, 0.18, 0.38)
    flow.y -= 16
    flow.w.draw_text(flow.margin_x, flow.y, "Tu Cuaderno Inteligente, Archivador Privado y Estudio Activo para Hijos y Nietos", "F3", 9.8, 0.35, 0.40, 0.48)
    flow.y -= 16
    flow.w.set_stroke_color(0.85, 0.88, 0.92)
    flow.w.line(flow.margin_x, flow.y, flow.margin_x + flow.content_w, flow.y)
    flow.y -= 16

    # SECCIÓN 1: DE LO PÚBLICO A LO PRIVADO
    flow.add_section_header("1. EL GRAN CAMBIO: DE LO PÚBLICO (BUSCADORES) A TU ARCHIVADOR PRIVADO", (0.15, 0.35, 0.65))

    flow.add_paragraph(
        "A diferencia del Gemini abierto o ChatGPT (que leen todo internet y pueden especular o inventar datos), "
        "Gemini Notebook funciona como un ARCHIVADOR CERRADO CON CANDADO. Solo lee estrictamente los papeles, textos y vídeos "
        "que tú decides subirle. Seguridad absoluta y rigor documental para personas mayores."
    )

    # Tabla comparativa
    tabla_datos = [
        ("Concepto", "Gemini Público / ChatGPT Abierto", "Gemini Notebook"),
        ("Origen de datos", "Rastrea millones de webs no verificadas.", "SOLO lee tus propios documentos subidos."),
        ("Riesgo de invención", "Puede tener 'alucinaciones' o inventar datos.", "Cero alucinaciones: se ciñe a la verdad de tus papeles."),
        ("Regla de la Verdad", "Rellena lagunas con suposiciones.", "Si no figura, responde: 'No aparece en las fuentes'."),
        ("Privacidad", "Modelos públicos abiertos.", "Privado: tus datos jamás se usan para entrenar la IA.")
    ]
    col_w = [115, 195, 205]
    flow.check_space(len(tabla_datos) * 16 + 10)
    for idx_f, (c1, c2, c3) in enumerate(tabla_datos):
        bg = (0.92, 0.95, 0.99) if idx_f == 0 else ((0.98, 0.98, 0.99) if idx_f % 2 == 1 else (1, 1, 1))
        flow.w.set_fill_color(bg[0], bg[1], bg[2])
        flow.w.set_stroke_color(0.85, 0.88, 0.92)
        flow.w.rect(flow.margin_x, flow.y - 10, flow.content_w, 14, fill=True, stroke=True)

        fnt = "F2" if idx_f == 0 else "F1"
        col_t = (0.12, 0.25, 0.55) if idx_f == 0 else (0.15, 0.18, 0.22)
        flow.w.draw_text(flow.margin_x + 6, flow.y - 6.5, c1, "F2" if idx_f > 0 else fnt, 7.8, col_t[0], col_t[1], col_t[2])
        flow.w.draw_text(flow.margin_x + 125, flow.y - 6.5, c2, fnt, 7.8, 0.40, 0.45, 0.50 if idx_f > 0 else col_t[2])
        flow.w.draw_text(flow.margin_x + 325, flow.y - 6.5, c3, "F2" if idx_f > 0 else fnt, 7.8, 0.10, 0.45, 0.30 if idx_f > 0 else col_t[2])
        flow.y -= 14
    flow.y -= 12

    # Callout acceso
    flow.add_card_box(
        "ACCESO DIRECTO Y CAPACIDAD DOCUMENTAL",
        [
            "Dirección web: Entrar en Chrome.",
            "Tu llave habitual: Inicia sesión con tu correo Gmail. No necesitas contraseñas nuevas ni registros complejos.",
            "Capacidad enorme: Admite hasta 50 fuentes por cuaderno y hasta 500.000 palabras por fuente individual (PDF, Word, TXT, YouTube, Audio)."
        ],
        badge_text="ACCESO FÁCIL",
        border_color=(0.35, 0.70, 0.50),
        bg_color=(0.95, 0.98, 0.96),
        title_color=(0.08, 0.45, 0.28)
    )

    # -------------------------------------------------------------
    # SECCIÓN 2: EL MAPA DE LA PANTALLA REAL (3 ZONAS)
    # -------------------------------------------------------------
    flow.add_section_header("2. EL MAPA DE LA PANTALLA REAL: LAS TRES COLUMNAS PRINCIPALES", (0.30, 0.20, 0.55))

    flow.add_paragraph("La pantalla de Gemini Notebook está dividida en 3 columnas limpias y organizadas de izquierda a derecha:")

    flow.add_card_box(
        "ZONA 1 (IZQUIERDA): EL ARCHIVADOR (PANEL DE FUENTES)",
        [
            "Botón '+ Añadir fuentes': Carga documentos PDF, Word (.docx), textos planos (.txt), enlaces de YouTube y audios MP3. Además, ahora cuenta con un botón directo para cargar tus propias grabaciones hechas por ti.",
            "Casillas de Verificación [v]: Cada fuente tiene un recuadro a su izquierda para activarla o desactivarla.",
            "Regla de Aislamiento: Gemini Notebook SOLO lee las fuentes con la casilla marcada. Si dejas una sola marcada, la IA 'olvida' temporalmente las demás. Permite analizar un papel sin mezclar datos."
        ],
        badge_text="COLUMNA 1",
        border_color=(0.15, 0.35, 0.65),
        bg_color=(0.94, 0.96, 0.99),
        title_color=(0.15, 0.35, 0.65)
    )

    flow.add_card_box(
        "ZONA 2 (CENTRAL): CONVERSACIÓN, RESUMEN Y CITAS EXACTAS",
        [
            "Guía del Cuaderno: Resumen general automático estructurado nada más subir tus papeles, sin tener que escribir nada.",
            "Chips de preguntas sugeridas: Botones interactivos con preguntas inteligentes listas para pulsar con un solo clic.",
            "Campo de Pregunta (Prompt): Escribe con naturalidad cotidiana, como a un bibliotecario amigo que se ha leído tus textos.",
            "Citas Exactas [1], [2]: Al pulsar el número al final de una frase, la pantalla salta al documento original y subraya en amarillo brillante el párrafo exacto de donde sacó la información. Verificación al 100%."
        ],
        badge_text="COLUMNA 2",
        border_color=(0.08, 0.48, 0.35),
        bg_color=(0.93, 0.97, 0.94),
        title_color=(0.08, 0.48, 0.35)
    )

    flow.add_card_box(
        "ZONA 3 (DERECHA): EL PANEL STUDIO (LA FÁBRICA DE IDEAS)",
        [
            "Icono Chincheta (Pin): Pasa el ratón sobre cualquier respuesta útil del chat y pulsa la chincheta para anclarla como Nota fija en el corcho permanente.",
            "Fábrica Creativa en 1 Clic: Genera presentaciones completas, resúmenes de vídeo, infografías, podcasts y guías de estudio sin escribir instrucciones largas."
        ],
        badge_text="COLUMNA 3",
        border_color=(0.75, 0.42, 0.10),
        bg_color=(0.99, 0.96, 0.91),
        title_color=(0.75, 0.42, 0.10)
    )

    # -------------------------------------------------------------
    # SECCIÓN 3: CASO DE ESTUDIO (LA LLEGADA A LA LUNA 1969)
    # -------------------------------------------------------------
    flow.add_section_header("3. CASO DE ESTUDIO: LA LLEGADA A LA LUNA (20 DE JULIO DE 1969)", (0.08, 0.48, 0.35))

    flow.add_paragraph("Para realizar las prácticas del taller, disponemos en la carpeta de 3 fuentes reales complementarias:")

    flow.add_card_box(
        "FUENTE 1: RECUERDO FAMILIAR EN MADRID (TEXTO TXT - COPIAR Y PEGAR)",
        [
            "Archivo: EJEMPLO_A_FUENTE_TEXTO_RECUERDO_LUNA_1969.txt",
            "Cómo cargarla: No hace falta descargar el archivo; simplemente abre el texto, cópialo entero y en Gemini Notebook pulsa '+ Añadir fuentes > Texto copiado' para pegarlo directamente.",
            "Contenido humano: La noche calurosa de julio en Madrid, la televisión Telefunken en blanco y negro, la voz inolvidable de Jesús Hermida y las lágrimas del abuelo que nació viajando en carro de mulas y vio al hombre pisar la Luna."
        ],
        badge_text="PEGAR TEXTO",
        border_color=(0.70, 0.30, 0.30),
        bg_color=(0.99, 0.95, 0.95),
        title_color=(0.60, 0.15, 0.20)
    )

    flow.add_card_box(
        "FUENTE 2: HISTORIA TÉCNICA DEL PROGRAMA APOLO 11 (DOCUMENTO PDF)",
        [
            "Archivo: EJEMPLO_A_FUENTE_HISTORIA_APOLO_11.pdf",
            "Cómo cargarla: Haz clic para descargar el PDF a tu ordenador y arrástralo directamente a Gemini Notebook o súbelo con '+ Añadir fuentes > Subir archivos'.",
            "Contenido científico: La hazaña de 400.000 ingenieros de la NASA, el cohete Saturno V, el ordenador de navegación AGC con solo 4 KB de memoria RAM y el papel decisivo de la estación española de Fresnedillas de la Oliva (Madrid)."
        ],
        badge_text="SUBIR PDF",
        border_color=(0.15, 0.35, 0.65),
        bg_color=(0.94, 0.96, 0.99),
        title_color=(0.15, 0.35, 0.65)
    )

    flow.add_card_box(
        "FUENTE 3: CONMEMORACIÓN DE LOS 50 AÑOS (VÍDEO DE YOUTUBE)",
        [
            "Enlace web: https://www.youtube.com/watch?v=Wbh9VAuZcUM (Euronews en español)",
            "Contenido audiovisual: Reportaje conmemorativo de los 50 años del alunizaje, declaraciones de historiadores y la mirada hacia el programa Artemis."
        ],
        badge_text="VÍDEO",
        border_color=(0.80, 0.45, 0.10),
        bg_color=(0.99, 0.96, 0.91),
        title_color=(0.80, 0.45, 0.10)
    )

    # -------------------------------------------------------------
    # SECCIÓN 4: FASE 1 DEL TALLER (ZONA CENTRAL, CITAS Y CHINCHETA)
    # -------------------------------------------------------------
    flow.add_section_header("4. TALLER PRÁCTICO: FASE 1 (ZONA CENTRAL, CITAS Y CHINCHETA)", (0.15, 0.35, 0.65))

    flow.add_card_box(
        "PASO 1.1: OBSERVACIÓN DE LA GUÍA DEL CUADERNO AUTOMÁTICA",
        [
            "Acción: Con las 3 fuentes marcadas [v], dirige la mirada al centro de la pantalla.",
            "Qué observar: Gemini Notebook ha generado por sí mismo un resumen general sin que hayas escrito nada, reconociendo el tema común y ofreciendo botones interactivos (chips) de preguntas sugeridas para empezar."
        ],
        badge_text="OBSERVACIÓN",
        border_color=(0.85, 0.88, 0.92),
        bg_color=(1, 1, 1),
        title_color=(0.12, 0.25, 0.55)
    )

    flow.add_card_box(
        "PASO 1.2: PRÁCTICA DE AISLAMIENTO CON CASILLAS DE VERIFICACIÓN",
        [
            "Ejercicio A (Solo TXT): Desmarca el PDF y el vídeo. Deja marcado ÚNICAMENTE el TXT de recuerdos. Escribe en el chat: 'Resume en 3 líneas la emoción familiar vivida en el salón madrileño'. Observa cómo solo habla del salón.",
            "Ejercicio B (Solo PDF): Desmarca el TXT y marca ÚNICAMENTE el PDF técnico. Escribe en el chat: 'Resume en 3 puntos técnicos los datos más asombrosos del Saturno V y el ordenador AGC'. Observa cómo responde sin mezclar recuerdos personales."
        ],
        badge_text="AISLAMIENTO",
        border_color=(0.85, 0.88, 0.92),
        bg_color=(1, 1, 1),
        title_color=(0.12, 0.25, 0.55)
    )

    flow.add_card_box(
        "PASO 1.3: BÚSQUEDA QUIRÚRGICA Y COMPROBACIÓN DE CITAS [1]",
        [
            "Acción: Marca las 3 fuentes a la vez [v]. Escribe en el campo de preguntas: '¿Qué marca era la televisión familiar y cuánta memoria RAM tenía el ordenador de la nave Apolo 11?'.",
            "Comprobación obligatoria: Haz clic sobre el número [1] o [2] al final de la respuesta. Verás cómo la pantalla salta sola al documento original y subraya en amarillo brillante 'Telefunken' y '4 kilobytes de memoria RAM'. Comprobación directa sin dudas."
        ],
        badge_text="CITAS [1]",
        border_color=(0.85, 0.88, 0.92),
        bg_color=(1, 1, 1),
        title_color=(0.12, 0.25, 0.55)
    )

    flow.add_card_box(
        "PASO 1.4: FIJAR COMO NOTA PERMANENTE EN EL CORCHO DE STUDIO (PIN)",
        [
            "Acción: Escribe en el chat: 'Compara en una tabla la vivencia humana del salón con la frialdad técnica de los 4 KB de RAM'.",
            "Paso de la Chincheta: Pasa el ratón sobre la tabla de respuesta y haz clic en el icono de la Chincheta (Pin).",
            "Resultado: La tabla viaja al panel derecho (Studio) y se convierte en una Nota permanente. No se borrará aunque salgas del navegador."
        ],
        badge_text="CHINCHETA",
        border_color=(0.85, 0.88, 0.92),
        bg_color=(1, 1, 1),
        title_color=(0.12, 0.25, 0.55)
    )

    # -------------------------------------------------------------
    # SECCIÓN 5: CASOS DE PRUEBA EXHAUSTIVOS EN EL PANEL STUDIO
    # -------------------------------------------------------------
    flow.add_section_header("5. PANEL STUDIO: CASOS DE PRUEBA EXHAUSTIVOS BOTÓN A BOTÓN", (0.75, 0.42, 0.10))

    flow.add_paragraph(
        "El Panel Studio es la fábrica de productos terminados. A continuación probaremos cada uno de sus botones "
        "principales con ejemplos prácticos reales, enseñando cómo usarlos en modo automático o guiados con prompts de estilo:"
    )

    # BOTÓN 1: PRESENTACIONES
    flow.add_card_box(
        "BOTÓN 1: PRESENTACIÓN (SLIDES) CON PROMPT DE ESTILO Y REVISIÓN EN VIVO",
        [
            "Para qué sirve: Genera una presentación completa en diapositivas con un visor interactivo slide por slide.",
            "Nueva función paso a paso: Ahora puedes crear presentaciones y vídeos paso a paso; la herramienta te saca un esquema línea por línea antes de hacer la presentación final, permitiéndote revisar y validar el contenido diapositiva a diapositiva.",
            "Fuentes a marcar: Marca en la izquierda [v] TXT de recuerdos + [v] PDF de la NASA (deja desmarcado el vídeo).",
            "Cómo usar el Prompt de Estilo: Pulsa el botón 'Presentación'. En la casilla de personalización escribe el prompt editorial (que tienes disponible más abajo en el recuadro verde):",
            "La función 'Revisar' en vivo: Abre la presentación. Con las flechas hojeas cada diapositiva. Pulsa el botón 'Revisar' (o Ajustar) dentro de la presentación para pedir cambios sobre la marcha (ej. 'haz la letra más grande' o 'destaca la frase del carro de mulas'). El control pedagógico siempre es tuyo."
        ],
        badge_text="PRESENTACIÓN",
        border_color=(0.15, 0.35, 0.65),
        bg_color=(0.95, 0.97, 0.99),
        title_color=(0.15, 0.35, 0.65)
    )
    flow.add_prompt_box(
        "PROMPT RECOMENDADO PARA PRESENTACIÓN SOBRIA Y ELEGANTE:",
        "Crea una presentación con un estilo visual sobrio, elegante y de crónica documental histórica. "
        "Utiliza una paleta espacial limpia (azul marino profundo, gris grafito y blanco de alto contraste), "
        "con tipografía grande y muy legible para personas mayores. Estructura las diapositivas equilibrando el rigor técnico "
        "de la NASA con la emoción humana del recuerdo familiar en Madrid, incorporando frases textuales entrecomilladas y "
        "evitando totalmente ilustraciones infantiles o colores estridentes."
    )

    # BOTÓN 2: INFOGRAFÍAS
    flow.add_card_box(
        "BOTÓN 2: INFOGRAFÍAS VISUALES (AUTOMÁTICAS, ESTILOS PREESTABLECIDOS Y PROMPTS)",
        [
            "Para qué sirve: Convierte textos densos en esquemas gráficos visuales con iconos, cifras grandes y cajas de resumen.",
            "Práctica de estilos visuales: Haz al menos dos infografías de prueba con estilos diferentes de los que vienen preestablecidos; prueba obligatoriamente el estilo 'Científico' y el estilo 'Anime' para comparar cómo transforma los datos y la estética.",
            "Modo Automático vs Personalizado: Deja marcada una fuente para generar una infografía en 1 clic, o escribe en la casilla de estilo el prompt estructurado:",
            "Ver los resultados en carpeta: En la carpeta '4. RESULTADOS DEL EJEMPLO' puedes comparar las distintas infografías generadas."
        ],
        badge_text="INFOGRAFÍA",
        border_color=(0.10, 0.50, 0.40),
        bg_color=(0.94, 0.98, 0.96),
        title_color=(0.10, 0.50, 0.40)
    )
    flow.add_prompt_box(
        "PROMPT RECOMENDADO PARA INFOGRAFÍA DIDÁCTICA:",
        "Genera una infografía estructurada tipo panel resumen con tres bloques visuales conectados: "
        "1. La Noche en el Salón Madrileño (cifras humanas). 2. El Desafío de la NASA y Fresnedillas (400.000 ingenieros y 4 KB). "
        "3. El Legado 50 Años Después. Utiliza recuadros limpios, viñetas claras y tipografía nítida."
    )

    # BOTÓN 3: RESUMEN DE VÍDEO
    flow.add_card_box(
        "BOTÓN 3: RESUMEN DE VÍDEO (FUSIÓN MULTIMEDIA EN 1 CLIC Y PASO A PASO)",
        [
            "Para qué sirve: Transforma tus documentos y notas en una pieza audiovisual dinámica con voz en off y transiciones.",
            "Creación guiada paso a paso: Al igual que en las presentaciones, ahora puedes crear vídeos paso a paso visualizando previamente un esquema línea por línea para revisar el guión antes de generar el vídeo definitivo.",
            "Práctica del taller: Marca las 3 fuentes a la vez [v] (TXT + PDF + YouTube).",
            "Acción: Pulsa directamente el botón 'Resumen de vídeo' en Studio (sin necesidad de escribir ningún prompt en el chat).",
            "Qué hace la IA: Lee al mismo tiempo la vivencia del salón, los datos de Fresnedillas y el reportaje de Euronews, fundiéndolos en un vídeo conmemorativo listo para proyectar en clase (disponible en la carpeta de resultados)."
        ],
        badge_text="VÍDEO",
        border_color=(0.65, 0.20, 0.25),
        bg_color=(0.99, 0.95, 0.95),
        title_color=(0.65, 0.20, 0.25)
    )

    # BOTÓN 4: AUDIO OVERVIEW
    flow.add_card_box(
        "BOTÓN 4: AUDIO OVERVIEW (LA TERTULIA DE RADIO / PODCAST A 2 VOCES)",
        [
            "Para qué sirve: Genera un programa de radio conversacional donde dos locutores en español discuten tus documentos.",
            "Práctica del taller: Con las 3 fuentes marcadas, pulsa 'Generar Audio' en la parte superior de Studio.",
            "La experiencia del alumno: En un par de minutos tienes un archivo de audio MP3 (disponible en '4. RESULTADOS DEL EJEMPLO'). Pulsas Play y escuchas a los locutores debatir con humor y cercanía sobre cómo un abuelo que nació en carro de mulas vio la Luna por la tele Telefunken."
        ],
        badge_text="PODCAST",
        border_color=(0.75, 0.42, 0.10),
        bg_color=(0.99, 0.96, 0.91),
        title_color=(0.75, 0.42, 0.10)
    )

    # BOTÓN 5: ESTUDIO ACTIVO PARA HIJOS Y NIETOS (TARJETAS FLASHCARDS Y MAPAS)
    flow.add_card_box(
        "BOTÓN 5: ESTUDIO ACTIVO PARA HIJOS Y NIETOS (TARJETAS FLASHCARDS Y MAPAS)",
        [
            "Para qué sirve: Ayudar a hijos y nietos a estudiar temarios de colegio, instituto o universidad de forma interactiva.",
            "Tarjetas de Repaso (Flashcards): Pulsa 'Guía de estudio' o pídele en el chat: 'Genera 5 tarjetas de memoria con pregunta por delante y respuesta oculta'. El alumno puede preguntar a sus nietos para que adivinen y giren la tarjeta.",
            "Mapas Mentales de Estudio: Pídele a la IA que organice temas densos de historia o biología en un esquema visual ramificado: Causas -> Desarrollo -> Consecuencias.",
            "Grabadora Móvil en Vivo: En la app de móvil puedes grabar hasta 1 hora continua (incluso con la pantalla apagada) para registrar una clase, una consulta médica o dictar recuerdos familiares que se archivan solos como fuentes."
        ],
        badge_text="FAMILIA",
        border_color=(0.35, 0.20, 0.60),
        bg_color=(0.97, 0.95, 0.99),
        title_color=(0.35, 0.20, 0.60)
    )

    # BOTÓN 6: INFORME (NUEVA FUNCIÓN OFICIAL)
    flow.add_card_box(
        "BOTÓN 6: INFORME (NUEVA FUNCIÓN OFICIAL DE DOCUMENTO ESTRUCTURADO)",
        [
            "Nueva función Informe: Las antiguas opciones de preguntas frecuentes y cronología han sido sustituidas por la función oficial 'Informe'.",
            "Para qué sirve: Genera un informe documental riguroso, formal y estructurado de todas tus fuentes seleccionadas, organizando antecedentes, análisis detallado y conclusiones.",
            "Cómo utilizarlo: Pulsa directamente el botón 'Informe' en el panel Studio. Obtendrás un texto ejecutivo completo, listo para estudiar, imprimir o compartir con hijos, nietos o colegas."
        ],
        badge_text="INFORME",
        border_color=(0.20, 0.35, 0.50),
        bg_color=(0.95, 0.97, 0.98),
        title_color=(0.15, 0.25, 0.40)
    )

    # -------------------------------------------------------------
    # SECCIÓN 6: CHECKLIST DE AUTOEVALUACIÓN DEL ALUMNO
    # -------------------------------------------------------------
    flow.add_section_header("6. CHECKLIST DE AUTOEVALUACIÓN Y COMPETENCIAS DEL ALUMNO", (0.12, 0.25, 0.55))

    checklist_items = [
        ("Paso 1", "Sé entrar en Chrome con mi cuenta Gmail y pulsar 'Nuevo cuaderno'."),
        ("Paso 2", "Sé añadir archivos PDF, Word, TXT, YouTube y grabaciones propias con '+ Añadir fuentes'."),
        ("Paso 3", "Sé observar la 'Guía del cuaderno' central con el resumen automático y preguntas sugeridas."),
        ("Paso 4", "Sé marcar y desmarcar las casillas [v] para aislar una sola fuente y analizarla sin mezclar."),
        ("Paso 5", "Sé hacer preguntas en el chat y pulsar las citas [1] para verificar el texto subrayado en amarillo."),
        ("Paso 6", "Sé guardar respuestas clave en el corcho permanente de Studio con el icono de la Chincheta (Pin)."),
        ("Paso 7", "Sé generar Presentaciones paso a paso con esquema previo y usar 'Revisar' en vivo."),
        ("Paso 8", "Sé crear Infografías probando al menos 2 estilos distintos (Científico y Anime)."),
        ("Paso 9", "Sé crear un Resumen de vídeo paso a paso fundiendo fuentes en una pieza audiovisual."),
        ("Paso 10", "Sé escuchar la tertulia de radio Audio Overview y generar un Informe estructurado en Studio."),
        ("Paso 11", "Sé usar Gemini Notebook para crear tarjetas de repaso (flashcards) y mapas de estudio para hijos y nietos.")
    ]

    flow.check_space(len(checklist_items) * 16 + 20)
    for paso, desc_c in checklist_items:
        flow.w.draw_text(flow.margin_x + 4, flow.y, f"[  ] {paso}:", "F2", 7.6, 0.12, 0.25, 0.55)
        flow.w.draw_text(flow.margin_x + 85, flow.y, desc_c, "F1", 7.6, 0.18, 0.22, 0.26)
        flow.w.draw_text(flow.margin_x + flow.content_w - 95, flow.y, "[  ] SÍ  /  [  ] DUDAS", "F2", 7.2, 0.45, 0.50, 0.55)
        flow.y -= 14.5

    flow.y -= 10
    # Reglas de oro finales
    flow.add_card_box(
        "LAS TRES REGLAS DE ORO EN CLASE",
        [
            "1ª Regla (La Materia Prima): La calidad de las respuestas dependerá siempre de la claridad de los papeles que subas.",
            "2ª Regla (Comprobación Obligatoria): Pulsa siempre las citas [1] para ver el subrayado amarillo con tus propios ojos.",
            "3ª Regla (Exploración sin Miedo): Prueba todos los botones de Studio. En el ordenador no se puede romper nada."
        ],
        badge_text="RECUERDA",
        border_color=(0.75, 0.42, 0.10),
        bg_color=(0.99, 0.97, 0.93),
        title_color=(0.75, 0.42, 0.10)
    )

    flow.w.end_page()

    # DIBUJAR HEADER Y FOOTER EN CADA PÁGINA
    total_pages = len(writer.pages)
    for i in range(total_pages):
        p_num = i + 1
        footer_stream = (
            f"\nBT /F1 7.5 Tf {flow.margin_x:.2f} 22.00 Td (Guia Didactica Oficial - Manual Visual y Taller Practico Gemini Notebook) Tj ET\n"
            f"BT /F2 8.0 Tf {flow.margin_x + flow.content_w - 95:.2f} 22.00 Td (Pagina {p_num} de {total_pages}) Tj ET\n"
            f"0.850 0.880 0.920 RG\n0.50 w\n{flow.margin_x:.2f} 32.00 m {flow.margin_x + flow.content_w:.2f} 32.00 l S\n"
        )
        if p_num > 1:
            header_stream = (
                f"\nBT /F2 8.0 Tf {flow.margin_x:.2f} {writer.h - 30:.2f} Td (MONOGRAFICO 2: MANUAL VISUAL Y TALLER GEMINI NOTEBOOK) Tj ET\n"
                f"BT /F1 8.0 Tf {flow.margin_x + flow.content_w - 180:.2f} {writer.h - 30:.2f} Td (Curso de IA para Adultos Mayores) Tj ET\n"
                f"0.850 0.880 0.920 RG\n0.50 w\n{flow.margin_x:.2f} {writer.h - 34:.2f} m {flow.margin_x + flow.content_w:.2f} {writer.h - 34:.2f} l S\n"
            )
        else:
            header_stream = ""

        writer.pages[i] += footer_stream + header_stream

    writer.write_to_file(PDF_OUTPUT)
    print(f"✅ PDF generado exitosamente: {PDF_OUTPUT} ({total_pages} páginas, diseño holgado y sin solapamientos)")

if __name__ == "__main__":
    generar_pdf_completo()
