#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_pdf_retos_vida_real.py
Compila las 6 fichas didácticas oficiales de Retos de Vida Real y Skills
en Gemini Notebook con:
- Fondos blancos en recuadros (100% amigables para imprimir en papel).
- Terminología canónica: 'Gemini Notebook' (eliminado 'NotebookLM').
- Página 2 limpia SIN repetición de cabecera de título.
- Ficha 0 con explicación de Skills y tablas comparativas.
- Retos 1 a 5 con texto de Fuente Ficticia / Modelo de ejemplo para practicar en clase.
- Explicación de guardado de prompts como Notas fijas en Studio.
100% Python nativo estándar.
"""

import os
import sys

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

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


class RetoPDFBuilder:
    def __init__(self, filename, title_badge, title_main, subtitle_main, border_color=(0.15, 0.35, 0.65)):
        self.filename = filename
        self.pdf = RobustPDFWriter()
        self.title_badge = title_badge
        self.title_main = title_main
        self.subtitle_main = subtitle_main
        self.border_color = border_color
        self.margin_x = 36
        self.content_w = 523
        self.cur_y = 800

    def draw_banner_p1(self):
        # Fondo blanco para no gastar tinta al imprimir
        self.pdf.set_fill_color(1.0, 1.0, 1.0)
        self.pdf.set_stroke_color(self.border_color[0], self.border_color[1], self.border_color[2])
        self.pdf.set_line_width(1.4)
        self.pdf.rect(self.margin_x, 742, self.content_w, 66, fill=True, stroke=True)

        self.pdf.draw_text(self.margin_x + 12, 790, self.title_badge.upper(), font="F2", size=8.5, r=self.border_color[0], g=self.border_color[1], b=self.border_color[2])
        self.pdf.draw_text(self.margin_x + 12, 770, self.title_main, font="F2", size=13.0, r=0.10, g=0.15, b=0.25)
        self.pdf.draw_text(self.margin_x + 12, 752, self.subtitle_main, font="F1", size=8.4, r=0.30, g=0.35, b=0.45)
        self.cur_y = 726

    def draw_header_p2(self, p2_label):
        # Cabecera sutil en página 2 sin repetir el banner grande
        self.pdf.set_fill_color(0.96, 0.97, 0.99)
        self.pdf.set_stroke_color(self.border_color[0], self.border_color[1], self.border_color[2])
        self.pdf.set_line_width(0.8)
        self.pdf.rect(self.margin_x, 792, self.content_w, 20, fill=True, stroke=True)
        self.pdf.draw_text(self.margin_x + 10, 798, p2_label.upper(), font="F2", size=8.5, r=self.border_color[0], g=self.border_color[1], b=self.border_color[2])
        self.pdf.draw_text(self.margin_x + self.content_w - 180, 798, "GEMINI NOTEBOOK • CURSO IA (+65)", font="F1", size=7.5, r=0.4, g=0.45, b=0.55)
        self.cur_y = 776

    def draw_footer(self, p_num):
        self.pdf.set_stroke_color(0.80, 0.82, 0.85)
        self.pdf.set_line_width(0.5)
        self.pdf.line(self.margin_x, 34, self.margin_x + self.content_w, 34)
        self.pdf.draw_text(self.margin_x, 22, f"Curso de IA - Monografico 2: Gemini Notebook - {self.title_main}", font="F1", size=7.5, r=0.4, g=0.45, b=0.5)
        self.pdf.draw_text(self.margin_x + self.content_w - 70, 22, f"Pagina {p_num} de 2", font="F2", size=8.0, r=0.2, g=0.25, b=0.35)

    def add_section_title(self, title, color_rgb=(0.15, 0.35, 0.65)):
        self.pdf.set_fill_color(color_rgb[0], color_rgb[1], color_rgb[2])
        self.pdf.rect(self.margin_x, self.cur_y - 2, self.content_w, 17, fill=True, stroke=False)
        self.pdf.draw_text(self.margin_x + 8, self.cur_y + 3, title.upper(), font="F2", size=8.2, r=1.0, g=1.0, b=1.0)
        self.cur_y -= 25

    def add_card_white(self, title, lines_list, badge=None, border_color=(0.75, 0.78, 0.85), title_color=(0.15, 0.35, 0.65)):
        line_spacing = 13.0
        rendered_lines = []
        for it in lines_list:
            it_wrapped = wrap_text(it, max_chars=76)
            rendered_lines.append(it_wrapped)

        total_lines = sum(len(l) for l in rendered_lines)
        h_box = 22 + (total_lines * line_spacing) + 12

        # Fondo blanco para imprimir
        self.pdf.set_fill_color(1.0, 1.0, 1.0)
        self.pdf.set_stroke_color(border_color[0], border_color[1], border_color[2])
        self.pdf.set_line_width(0.8)
        self.pdf.rect(self.margin_x, self.cur_y - h_box + 14, self.content_w, h_box, fill=True, stroke=True)

        self.pdf.draw_text(self.margin_x + 10, self.cur_y - 1, title, font="F2", size=8.8, r=title_color[0], g=title_color[1], b=title_color[2])
        if badge:
            badge_w = 75
            bx = self.margin_x + self.content_w - badge_w - 8
            self.pdf.set_fill_color(title_color[0], title_color[1], title_color[2])
            self.pdf.rect(bx, self.cur_y - 3, badge_w, 13, fill=True, stroke=False)
            self.pdf.draw_text(bx + 5, self.cur_y, badge, font="F2", size=7.0, r=1.0, g=1.0, b=1.0)

        ty = self.cur_y - 16
        for group in rendered_lines:
            for idx_l, line in enumerate(group):
                prefix = "- " if (idx_l == 0 and not line.startswith(" ")) else "  "
                fnt = "F2" if (idx_l == 0 and ":" in line) else "F1"
                self.pdf.draw_text(self.margin_x + 14, ty, prefix + line, font=fnt, size=7.8, r=0.15, g=0.18, b=0.22)
                ty -= line_spacing

        self.cur_y -= (h_box + 8)

    def add_table_white(self, title, headers, rows, col_widths, border_color=(0.75, 0.78, 0.85)):
        line_spacing = 13.0
        # Medir altura de cada fila
        row_heights = []
        wrapped_rows = []
        for row in rows:
            max_lines_in_row = 1
            cur_wrapped_row = []
            for idx, text in enumerate(row):
                # max chars aprox según ancho de col
                c_chars = int(col_widths[idx] / 5.2)
                lines = wrap_text(text, max_chars=c_chars)
                cur_wrapped_row.append(lines)
                if len(lines) > max_lines_in_row:
                    max_lines_in_row = len(lines)
            row_heights.append(max_lines_in_row * line_spacing + 8)
            wrapped_rows.append(cur_wrapped_row)

        total_table_h = 24 + 18 + sum(row_heights) + 6

        # Fondo blanco exterior
        self.pdf.set_fill_color(1.0, 1.0, 1.0)
        self.pdf.set_stroke_color(border_color[0], border_color[1], border_color[2])
        self.pdf.set_line_width(0.8)
        self.pdf.rect(self.margin_x, self.cur_y - total_table_h + 14, self.content_w, total_table_h, fill=True, stroke=True)

        self.pdf.draw_text(self.margin_x + 10, self.cur_y - 1, title, font="F2", size=8.8, r=0.15, g=0.35, b=0.65)

        # Cabecera de tabla
        ty = self.cur_y - 18
        self.pdf.set_fill_color(0.92, 0.94, 0.98)
        self.pdf.rect(self.margin_x + 4, ty - 12, self.content_w - 8, 16, fill=True, stroke=False)
        cx = self.margin_x + 8
        for idx, h in enumerate(headers):
            self.pdf.draw_text(cx, ty - 1, h, font="F2", size=7.8, r=0.10, g=0.25, b=0.50)
            cx += col_widths[idx]

        ty -= 18
        for r_idx, w_row in enumerate(wrapped_rows):
            r_h = row_heights[r_idx]
            # Línea horizontal separadora
            self.pdf.set_stroke_color(0.88, 0.90, 0.94)
            self.pdf.line(self.margin_x + 6, ty + 4, self.margin_x + self.content_w - 6, ty + 4)
            
            # Dibujar celdas
            for c_idx, lines in enumerate(w_row):
                cx = self.margin_x + 8 + sum(col_widths[:c_idx])
                sub_y = ty - 8
                for l in lines:
                    fnt = "F2" if c_idx == 0 else "F1"
                    self.pdf.draw_text(cx, sub_y, l, font=fnt, size=7.6, r=0.15, g=0.18, b=0.22)
                    sub_y -= line_spacing

            ty -= r_h

        self.cur_y -= (total_table_h + 8)

    def add_prompt_card_white(self, label, prompt_str, target_note="Guárdalo como 'Nota fija' en Studio o úsalo en el chat"):
        prompt_lines = wrap_text(prompt_str, max_chars=74)
        line_spacing = 12.5
        n_lines = len(prompt_lines)
        b_h = 16 + 16 + (n_lines * line_spacing) + 20

        # Fondo blanco con borde de color
        self.pdf.set_fill_color(1.0, 1.0, 1.0)
        self.pdf.set_stroke_color(self.border_color[0], self.border_color[1], self.border_color[2])
        self.pdf.set_line_width(0.9)
        self.pdf.rect(self.margin_x, self.cur_y - b_h + 14, self.content_w, b_h, fill=True, stroke=True)

        # Header bar interior claro
        self.pdf.set_fill_color(0.95, 0.96, 0.99)
        self.pdf.rect(self.margin_x + 1, self.cur_y - 2, self.content_w - 2, 16, fill=True, stroke=False)
        self.pdf.draw_text(self.margin_x + 8, self.cur_y + 2, label.upper(), font="F2", size=7.8, r=self.border_color[0], g=self.border_color[1], b=self.border_color[2])
        self.pdf.draw_text(self.margin_x + self.content_w - 230, self.cur_y + 2, target_note, font="F3", size=7.0, r=0.35, g=0.40, b=0.50)

        ty = self.cur_y - 17
        for l in prompt_lines:
            self.pdf.draw_text(self.margin_x + 12, ty, l, font="F3", size=7.8, r=0.10, g=0.15, b=0.25)
            ty -= line_spacing

        self.cur_y -= (b_h + 8)


# =========================================================================
# COMPILACIÓN DE LAS 6 FICHAS REVISADAS
# =========================================================================

def compilar_reto_00():
    b = RetoPDFBuilder(
        os.path.join(OUTPUT_DIR, "FICHA_RETO_00_COMPARATIVA_GEMINI_VS_NOTEBOOKLM.pdf"),
        "Monografico 2 - Ficha 0: Fundamentos y Skills",
        "Que son las Skills y Comparativa con Gemini",
        "Tus cuadernos de Gemini Notebook como asistentes especializados con cero alucinacion",
        border_color=(0.75, 0.42, 0.10)
    )

    # ---------------- PAGINA 1 ----------------
    b.pdf.start_page()
    b.draw_banner_p1()

    b.add_section_title("1. ¿QUE ES UNA SKILL EN GEMINI NOTEBOOK?", (0.75, 0.42, 0.10))
    # Tabla 1: Qué es una Skill con los cuadernos
    headers_t1 = ["Asistente (Cuaderno)", "Papeles que guarda", "Regla de trato fija", "Ventaja inmediata"]
    rows_t1 = [
        ["Mi Medico Amigo", "Analiticas, recetas, prospectos", "Explica sin alarmar, prepara preguntas", "Responde citas medicas en 1 linea"],
        ["Auditor de Facturas", "Factura luz, poliza del hogar", "Detecta cobros extra y exclusiones", "Audita 40 pags de contrato al instante"],
        ["Mi Biografo 70/80", "Audios de voz, recuerdos familiares", "Redacta cronica emotiva para nietos", "Crea libros y podcasts de radio"]
    ]
    b.add_table_white("TABLA 1: CADA CUADERNO DE GEMINI NOTEBOOK ES UNA SKILL A TU MEDIDA", headers_t1, rows_t1, [115, 125, 140, 135])

    b.add_section_title("2. TABLA COMPARATIVA: GEMINI NORMAL VS GEMINI NOTEBOOK", (0.15, 0.35, 0.65))
    headers_t2 = ["Caracteristica", "Gemini Normal (Abierto)", "Gemini Notebook (Cuaderno Privado)"]
    rows_t2 = [
        ["Origen de datos", "Todo Internet y su entrenamiento masivo", "Solo los papeles que tu subes a la mesa"],
        ["Riesgo de error", "Puede alucinar o inventar con elocuencia", "Cero alucinacion: cita [1] con subrayado amarillo"],
        ["Privacidad", "Conversacion abierta en la nube", "Entorno privado: tus documentos no entrenan la IA"],
        ["Formatos de salida", "Texto, imagenes generadas y codigo", "Tertulia de radio (podcast), informes e infografias"]
    ]
    b.add_table_white("TABLA 2: RADIOGRAFIA FRENTE A FRENTE PARA EL ALUMNO SENIOR", headers_t2, rows_t2, [110, 195, 210])

    b.draw_footer(1)
    b.pdf.end_page()

    # ---------------- PAGINA 2 (SIN CABECERA REPETIDA) ----------------
    b.pdf.start_page()
    b.draw_header_p2("Ficha 0 · Guia de Decision y Mandamientos de las Skills")

    b.add_section_title("3. ¿CUANDO USAR CADA HERRAMIENTA EN TU DIA A DIA?", (0.10, 0.48, 0.35))
    b.add_card_white(
        "GUIA DE DECISION RAPIDA PARA MAYORES DE 65 ANOS",
        [
            "USA GEMINI NORMAL CUANDO:",
            "  - Quieres redactar una poesia, felicitar un aniversario o pedir ideas de regalos familiares.",
            "  - Buscas un menu de cocina con lo que tienes en el frigorifico o pedir un itinerario de viaje.",
            "  - Quieres traducir una carta o aprender conceptos generales de ciencia y cultura.",
            "USA GEMINI NOTEBOOK CUANDO:",
            "  - Tienes analiticas de sangre, informes medicos o prospectos y necesitas saber que dicen sin rodeos.",
            "  - Tienes la factura de la luz, el contrato del seguro o una carta del banco.",
            "  - Quieres dictar tus recuerdos de los anos 70 y 80 y transformarlos en un capitulo o un podcast de radio.",
            "  - Necesitas que cada afirmacion tenga su cita exacta [1] verificable con tus propios ojos."
        ],
        badge="DECISION",
        border_color=(0.3, 0.7, 0.45),
        title_color=(0.10, 0.48, 0.35)
    )

    b.add_section_title("4. LOS TRES MANDAMIENTOS DE LAS SKILLS EN GEMINI NOTEBOOK", (0.45, 0.20, 0.65))
    b.add_card_white(
        "REGLAS DE ORO DE LA METODOLOGIA OFICIAL",
        [
            "1. Cada Cuaderno es tu Asistente Permanente: Una vez que subes tus documentos, nunca mas tienes que",
            "   volver a cargarlos. El cuaderno los recuerda siempre y te responde preguntas en una sola linea.",
            "2. Las Analiticas y Facturas van a Gemini Notebook, NUNCA a Gemini Abierto: En temas de salud y dinero",
            "   no podemos permitirnos alucinaciones. Gemini Notebook es tu notario privado con cero error.",
            "3. Las Reglas de Trato se guardan en Studio como Nota Fija: No necesitas un Word externo. Anades una",
            "   Nota en Studio con tus preferencias y tu asistente sabra siempre como hablarte y como resumirte."
        ],
        badge="REGLAS",
        border_color=(0.6, 0.4, 0.8),
        title_color=(0.45, 0.20, 0.65)
    )

    b.draw_footer(2)
    b.pdf.end_page()
    b.pdf.write_to_file(b.filename)
    print(f"✅ Generado: {b.filename}")


def compilar_reto_01():
    b = RetoPDFBuilder(
        os.path.join(OUTPUT_DIR, "FICHA_RETO_01_HISTORIAL_SALUD_INTELIGENTE.pdf"),
        "Reto 1 de Vida Real - Gemini Notebook (+65)",
        "Historial de Salud Inteligente y Citas Medicas",
        "Organiza analiticas, prospectos y consultas con el especialista con maximo rigor",
        border_color=(0.15, 0.55, 0.35)
    )

    # ---------------- PAGINA 1 ----------------
    b.pdf.start_page()
    b.draw_banner_p1()

    b.add_section_title("1. EL PROBLEMA Y EL OBJETIVO DEL ASISTENTE CUADERNO", (0.15, 0.55, 0.35))
    b.add_card_white(
        "DE LA CARPETA CAOTICA AL ASISTENTE DE SALUD PERMANENTE",
        [
            "El problema: Acumulamos analisis, informes y prospectos en carpetas de plastico.",
            "  Cuando llegamos a la consulta medica, apenas tenemos 10 minutos y olvidamos dudas clave.",
            "La solucion: Crear el cuaderno 'Salud y Analiticas'. Alimenta este cuaderno con tus informes reales.",
            "El cuaderno funcionara como tu asistente de salud personal: responde en 1 linea y cita tus analisis [1]."
        ],
        badge="SALUD",
        border_color=(0.3, 0.7, 0.45),
        title_color=(0.15, 0.55, 0.35)
    )

    b.add_section_title("2. PREPARACION Y FUENTE FICTICIA DE EJEMPLO PARA CLASE", (0.15, 0.35, 0.65))
    b.add_card_white(
        "COMO PREPARAR EL CUADERNO EN 2 MINUTOS",
        [
            "1. Abre Gemini Notebook y pulsa '+ Nuevo cuaderno'. Titulalo 'Salud y Analiticas'.",
            "2. Pulsa '+ Anadir fuentes': puedes subir tus analisis reales o pegar el texto de ejemplo de abajo.",
            "3. Guarda las reglas de trato en el panel Studio como una 'Nota fija' (chincheta)."
        ],
        badge="PASOS",
        border_color=(0.4, 0.6, 0.8),
        title_color=(0.15, 0.35, 0.65)
    )

    b.add_card_white(
        "TEXTO MODELO DE EJEMPLO (COPIA Y PEGA SI NO LLEVAS ANALITICA EN CLASE)",
        [
            "«INFORME DE ANALITICA CLINICA - Paciente: 66 anos. Fecha: 10/11/2026.",
            "  Glucosa: 104 mg/dL (Normal: 70-100) *. Leve elevacion en ayunas.",
            "  Colesterol Total: 218 mg/dL (Normal: < 200) *. Colesterol LDL: 135 mg/dL *.",
            "  Trigliceridos: 140 mg/dL (Normal: < 150). Creatinina: 0.9 mg/dL (Normal: 0.6-1.1).",
            "  Tratamiento actual: Atorvastatina 10 mg (1 comprimido en la cena). Adiro 100 mg (almuerzo).",
            "  Observacion: Dolores articulares leves por la manana en rodilla derecha.»"
        ],
        badge="EJEMPLO",
        border_color=(0.2, 0.6, 0.4),
        title_color=(0.15, 0.50, 0.30)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # ---------------- PAGINA 2 (SIN CABECERA REPETIDA) ----------------
    b.pdf.start_page()
    b.draw_header_p2("Reto 1 · Consultas en 1 Linea y Producto Final en Studio")

    b.add_section_title("3. CONSULTAS EN 1 LINEA EN EL CHAT DE TU CUADERNO", (0.15, 0.55, 0.35))
    b.add_prompt_card_white(
        "CONSULTA 1: TRADUCTOR DE VALORES CON ASTERISCO",
        "«¿Que significan los valores que tienen asterisco (*) en mi analitica y que consejos me das?»",
        target_note="Escribelo en el chat central del cuaderno"
    )

    b.add_prompt_card_white(
        "CONSULTA 2: RESUMEN EN 4 PUNTOS PARA LLEVAR A LA CONSULTA MEDICA",
        (
            "«Genera un resumen en 4 puntos para llevar impreso a mi doctor:\n"
            "1. Medicacion que tomo y dosis.\n"
            "2. Valores desviados del analisis.\n"
            "3. Molestias comunicadas.\n"
            "4. Tres preguntas claras para hacerle al doctor en los 10 minutos de consulta.»"
        ),
        target_note="Guardalo con la Chincheta en Studio como nota fija"
    )

    b.add_section_title("4. PRODUCTO FINAL EN PANEL STUDIO Y SALVAGUARDA", (0.75, 0.42, 0.10))
    b.add_card_white(
        "INFOGRAFIA VISUAL Y RECUERDA",
        [
            "En el panel derecho Studio, pulsa 'Infografia' (Estilo Cientifico):",
            "  Prompt: 'Dibuja un horario visual con mis pastillas de manana y cena'.",
            "Salvaguarda medica obligatoria: Gemini Notebook no receta farmacos ni sustituye a tu medico.",
            "Su objetivo es darte tranquilidad y prepararte para que aproveches cada minuto en la consulta."
        ],
        badge="RECUERDA",
        border_color=(0.8, 0.6, 0.3),
        title_color=(0.75, 0.42, 0.10)
    )

    b.draw_footer(2)
    b.pdf.end_page()
    b.pdf.write_to_file(b.filename)
    print(f"✅ Generado: {b.filename}")


def compilar_reto_02():
    b = RetoPDFBuilder(
        os.path.join(OUTPUT_DIR, "FICHA_RETO_02_CAZADOR_BULOS_WHATSAPP.pdf"),
        "Reto 2 de Vida Real - Gemini Notebook (+65)",
        "El Cazador de Bulos y Desinformacion de WhatsApp",
        "Desmonta alarmas falsas, remedios milagrosos y timos virales con rigor cientifico",
        border_color=(0.80, 0.20, 0.20)
    )

    # ---------------- PAGINA 1 ----------------
    b.pdf.start_page()
    b.draw_banner_p1()

    b.add_section_title("1. EL PROBLEMA: CADENAS VIRALES EN LOS GRUPOS FAMILIARES", (0.80, 0.20, 0.20))
    b.add_card_white(
        "EL MIEDO Y LA URGENCIA COMO ARMA DE ENGANO",
        [
            "El problema: Cada semana recibimos mensajes alarmistas de familiares bienintencionados.",
            "  '¡Nuevo virus en WhatsApp!', '¡Cura la artrosis con bicarbonato hervido!', '¡Te van a cobrar!'.",
            "La solucion: Crear el cuaderno 'Cazador de Bulos'. Ponemos frente a frente el mensaje viral",
            "contra comunicados oficiales de la Policia Nacional o Sanidad para comprobar hechos con citas [1]."
        ],
        badge="ALERTA",
        border_color=(0.9, 0.4, 0.4),
        title_color=(0.80, 0.20, 0.20)
    )

    b.add_section_title("2. PREPARACION Y FUENTE FICTICIA DE EJEMPLO PARA CLASE", (0.15, 0.35, 0.65))
    b.add_card_white(
        "COMO MONTAR EL CASO EN GEMINI NOTEBOOK",
        [
            "1. Crea el cuaderno 'Cazador de Bulos WhatsApp'.",
            "2. Fuente A (El Sospechoso): Pega el mensaje viral recibido (puedes usar el ejemplo de abajo).",
            "3. Fuente B (La Verdad): Sube un comunicado de verificacion o desmentido oficial."
        ],
        badge="PASOS",
        border_color=(0.4, 0.6, 0.8),
        title_color=(0.15, 0.35, 0.65)
    )

    b.add_card_white(
        "TEXTO MODELO DE MENSAJE VIRAL (COPIA Y PEGA COMO FUENTE A)",
        [
            "«¡¡URGENTE!! AVISO DE LA POLICIA: A partir de esta noche no respondas a llamadas que empiecen por +34 919.",
            "  Hay una banda internacional que solo con descolgar te clona la cuenta del banco y la tarjeta sanitaria.",
            "  Ya hay 4.000 jubilados afectados en Madrid. ¡¡REVIALO A TODOS TUS CONTACTOS Y GRUPOS YA!!»"
        ],
        badge="MENSAJE",
        border_color=(0.9, 0.4, 0.4),
        title_color=(0.80, 0.20, 0.20)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # ---------------- PAGINA 2 (SIN CABECERA REPETIDA) ----------------
    b.pdf.start_page()
    b.draw_header_p2("Reto 2 · Auditoria en 1 Linea y Respuesta Diplomatica")

    b.add_section_title("3. CONSULTAS EN 1 LINEA EN EL CHAT DE TU CUADERNO", (0.80, 0.20, 0.20))
    b.add_prompt_card_white(
        "CONSULTA 1: AUDITORIA DE VERACIDAD",
        "«Analiza este mensaje viral y dime si tiene senales de bulo (mayusculas, urgencia falsa, sin fuentes).»",
        target_note="Escribelo en el chat central de tu cuaderno"
    )

    b.add_prompt_card_white(
        "CONSULTA 2: RESPUESTA DIPLOMATICA PARA EL GRUPO FAMILIAR",
        (
            "«Redacta un mensaje breve y carinono para reenviar al grupo familiar de WhatsApp explicando por que "
            "la cadena no es cierta, agradeciendo la buena intencion de quien lo envio para no ofender.»"
        ),
        target_note="Guardalo como Nota fija en Studio para tenerlo a mano"
    )

    b.add_section_title("4. PRODUCTO FINAL EN PANEL STUDIO: ALERTA VISUAL", (0.10, 0.48, 0.35))
    b.add_card_white(
        "INFOGRAFIA Y REGLE DE ORO",
        [
            "En Studio, pulsa 'Infografia' (Estilo Pizarron): '3 senales para detectar un bulo antes de reenviar'.",
            "Regla de Oro: Ante la duda en WhatsApp, ¡frena! Nunca reenvies sin contrastar en tu propio cuaderno."
        ],
        badge="EXITO",
        border_color=(0.3, 0.7, 0.45),
        title_color=(0.10, 0.48, 0.35)
    )

    b.draw_footer(2)
    b.pdf.end_page()
    b.pdf.write_to_file(b.filename)
    print(f"✅ Generado: {b.filename}")


def compilar_reto_03():
    b = RetoPDFBuilder(
        os.path.join(OUTPUT_DIR, "FICHA_RETO_03_MAQUINA_TIEMPO_FAMILIAR_ANOS_70_80.pdf"),
        "Reto 3 de Vida Real - Gemini Notebook (+65)",
        "La Maquina del Tiempo Familiar (Anos 70 y 80)",
        "Digitaliza anecdotas de juventud, la Transicion, cassettes y recuerdos en un legado vivo",
        border_color=(0.55, 0.25, 0.75)
    )

    # ---------------- PAGINA 1 ----------------
    b.pdf.start_page()
    b.draw_banner_p1()

    b.add_section_title("1. EL VALOR DE TU MEMORIA: UNA EPOCA UNICA DE ESPANA", (0.55, 0.25, 0.75))
    b.add_card_white(
        "NUESTRA JUVENTUD VIVIO EL GRAN CAMBIO",
        [
            "Nacidos hacia 1960: no vivimos la posguerra, fuimos la juventud de los anos 70 y 80.",
            "  La epoca del Seat 127, los cassettes rebobinados con boli Bic, guateques y la Transicion democratica.",
            "El problema: Estas vivencias se pierden en sobremesas y los nietos no conocen como era la vida.",
            "La solucion: Crear el cuaderno 'Memorias de Juventud'. Convierte tus relatos en capitulos y en radio."
        ],
        badge="MEMORIA",
        border_color=(0.7, 0.4, 0.8),
        title_color=(0.55, 0.25, 0.75)
    )

    b.add_section_title("2. PREPARACION Y FUENTE FICTICIA DE EJEMPLO PARA CLASE", (0.15, 0.35, 0.65))
    b.add_card_white(
        "COMO PREPARAR TU CUADERNO BIOGRAFICO",
        [
            "1. Crea el cuaderno 'Memorias de Juventud (70 y 80)'.",
            "2. Dicta por voz en tu movil o PC una anecdota real, o copia el texto de ejemplo de abajo como Fuente 1.",
            "3. Anade canciones de la epoca como Fuente 2 (Duo Dinamico, Camilo Sesto, Triana, Mecano)."
        ],
        badge="PASOS",
        border_color=(0.4, 0.6, 0.8),
        title_color=(0.15, 0.35, 0.65)
    )

    b.add_card_white(
        "TEXTO MODELO DE RECUERDO FAMILIAR (COPIA Y PEGA COMO FUENTE 1)",
        [
            "«El verano de 1978 nos fuimos cuatro amigos a Torrevieja en un Seat 127 blanco.",
            "  Llevabamos la baca cargada hasta arriba y una cinta de casete de Triana que sonaba sin parar.",
            "  No habia aire acondicionado: bajabamos las ventanillas y el aire caliente olia a pinos y asfalto.",
            "  Tardamos 8 horas por carreteras secundarias. Nos banamos en la playa al anochecer con una ilusion enorme.»"
        ],
        badge="RELATO",
        border_color=(0.7, 0.4, 0.8),
        title_color=(0.55, 0.25, 0.75)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # ---------------- PAGINA 2 (SIN CABECERA REPETIDA) ----------------
    b.pdf.start_page()
    b.draw_header_p2("Reto 3 · Cronica Novelada y el Gran Regalo en Audio Overview")

    b.add_section_title("3. CONSULTAS EN 1 LINEA EN EL CHAT DE TU CUADERNO", (0.55, 0.25, 0.75))
    b.add_prompt_card_white(
        "CONSULTA 1: CRONICA NOVELADA DE NUESTRA JUVENTUD (PARA NIETOS)",
        "«Con mis recuerdos subidos, escribe un capitulo literario y emotivo titulado 'Nuestra Juventud en el 78'.»",
        target_note="Guardalo con la Chincheta en Studio como nota permanente"
    )

    b.add_prompt_card_white(
        "CONSULTA 2: CUESTIONARIO BIOGRAFICO PARA SEGUIR ESCRIBIENDO",
        "«Hazme 4 preguntas sugerentes sobre momentos que mencione de pasada para que yo pueda dictar nuevos audios.»",
        target_note="Escribelo en el chat central"
    )

    b.add_section_title("4. EL GRAN REGALO FAMILIAR EN STUDIO: LA RADIO FAMILIAR", (0.10, 0.48, 0.35))
    b.add_card_white(
        "AUDIO OVERVIEW: ESCUCHAR TUS RECUERDOS EN UN PROGRAMA DE RADIO",
        [
            "En el panel derecho Studio, pulsa 'Audio Overview (Resumen de Audio)':",
            "  Dos periodistas conversaran con fascinacion y carino sobre como era la juventud en los 70 y 80.",
            "Descarga el archivo MP3 y compártelo por WhatsApp con tus hijos y nietos. ¡Sera un regalo inolvidable!"
        ],
        badge="LEGADO",
        border_color=(0.3, 0.7, 0.45),
        title_color=(0.10, 0.48, 0.35)
    )

    b.draw_footer(2)
    b.pdf.end_page()
    b.pdf.write_to_file(b.filename)
    print(f"✅ Generado: {b.filename}")


def compilar_reto_04():
    b = RetoPDFBuilder(
        os.path.join(OUTPUT_DIR, "FICHA_RETO_04_AUDITOR_CONTRATOS_SEGUROS_LETRAS.pdf"),
        "Reto 4 de Vida Real - Gemini Notebook (+65)",
        "El Auditor de Contratos, Facturas y Letra Pequena",
        "Desentrana la factura de la luz, el seguro del hogar y clausulas bancarias confusas",
        border_color=(0.10, 0.50, 0.80)
    )

    # ---------------- PAGINA 1 ----------------
    b.pdf.start_page()
    b.draw_banner_p1()

    b.add_section_title("1. EL RETO: DEFENDERSE DE LA COMPLEJIDAD Y COBROS EXTRA", (0.10, 0.50, 0.80))
    b.add_card_white(
        "ADIOS A LA LETRA PEQUENA INCOMPRENSIBLE",
        [
            "El problema: Facturas de la luz con terminos fijos, peajes y seguros de mantenimiento sorpresa.",
            "  Polizas de hogar de 40 paginas donde no sabemos que gotera o rotura de electrodomestico esta cubierta.",
            "La solucion: Crear el cuaderno 'Auditor Facturas y Seguros'. Subes el PDF real y te responde en segundos.",
            "Garantia de oro: Te cita la pagina y articulo exacto del contrato [1] sin inventar nada."
        ],
        badge="AUDITORIA",
        border_color=(0.3, 0.6, 0.85),
        title_color=(0.10, 0.50, 0.80)
    )

    b.add_section_title("2. PREPARACION Y FUENTE FICTICIA DE EJEMPLO PARA CLASE", (0.15, 0.35, 0.65))
    b.add_card_white(
        "COMO CARGAR TU FACTURA EN EL CUADERNO",
        [
            "1. Abre Gemini Notebook y crea el cuaderno 'Auditor Facturas y Seguros'.",
            "2. Pulsa '+ Anadir fuentes' y sube tu recibo de la luz en PDF o copia el texto modelo de abajo.",
            "3. En 3 segundos tendras el resumen ejecutivo central listo."
        ],
        badge="PASOS",
        border_color=(0.4, 0.6, 0.8),
        title_color=(0.15, 0.35, 0.65)
    )

    b.add_card_white(
        "TEXTO MODELO DE FACTURA ELECTRICA (COPIA Y PEGA SI NO LLEVAS RECIBO)",
        [
            "«FACTURA DE ENERGIA ELECTRICA - Periodo: 01/10/2026 al 31/10/2026 (31 dias).",
            "  Potencia contratada: Punta 4.6 kW / Valle 4.6 kW. Importe potencia fija: 18.20 euros.",
            "  Energia consumida: 210 kWh a 0.178 eur/kWh. Importe energia: 37.38 euros.",
            "  Servicios adicionales: Servicio Proteccion Pagos 4.90 euros. Mantenimiento Urgencias 24h: 7.50 euros *.",
            "  Impuesto electricidad: 1.82 euros. Alquiler de contador: 0.84 euros. IVA 21%: 14.83 euros.",
            "  TOTAL FACTURA A PAGAR: 85.47 euros.»"
        ],
        badge="FACTURA",
        border_color=(0.3, 0.6, 0.85),
        title_color=(0.10, 0.50, 0.80)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # ---------------- PAGINA 2 (SIN CABECERA REPETIDA) ----------------
    b.pdf.start_page()
    b.draw_header_p2("Reto 4 · Radiografia de Gastos y Reclamacion en Studio")

    b.add_section_title("3. CONSULTAS EN 1 LINEA EN EL CHAT DE TU CUADERNO", (0.10, 0.50, 0.80))
    b.add_prompt_card_white(
        "CONSULTA 1: RADIOGRAFIA DE LA FACTURA Y COBROS SORPRESA",
        "«¿Que conceptos de mantenimiento o servicios extra me estan cobrando y cuanto suman en total?»",
        target_note="Escribelo en el chat central de tu cuaderno"
    )

    b.add_prompt_card_white(
        "CONSULTA 2: SIMULACRO DE POLIZA DE SEGURO DEL HOGAR",
        "«Si se me rompe la lavadora o hay gotera con el vecino, ¿mi seguro lo cubre? Citame la clausula exacta.»",
        target_note="Guardalo como Nota fija en Studio con la Chincheta"
    )

    b.add_section_title("4. PRODUCTO FINAL EN PANEL STUDIO: INFORME DE AHORRO", (0.10, 0.48, 0.35))
    b.add_card_white(
        "INFORME FORMAL Y CARTA DE BAJA DE SERVICIOS",
        [
            "Boton 'Informe' en Studio: Genera un documento estructurado de ahorro listo para imprimir.",
            "Prompt de reclamacion: 'Escribe una carta formal solicitando la baja del mantenimiento que no solicite'.",
            "Poder en tus manos: Nunca mas pagaras por conceptos que no entiendes."
        ],
        badge="AHORRO",
        border_color=(0.3, 0.7, 0.45),
        title_color=(0.10, 0.48, 0.35)
    )

    b.draw_footer(2)
    b.pdf.end_page()
    b.pdf.write_to_file(b.filename)
    print(f"✅ Generado: {b.filename}")


def compilar_reto_05():
    b = RetoPDFBuilder(
        os.path.join(OUTPUT_DIR, "FICHA_RETO_05_TERTULIA_RADIO_MODO_DEBATE.pdf"),
        "Reto 5 de Vida Real - Gemini Notebook (+65)",
        "La Tertulia de Radio Personalizada (Modo Debate)",
        "Pon a dos periodistas a debatir a fondo sobre cualquier tema con Audio Overview",
        border_color=(0.85, 0.50, 0.10)
    )

    # ---------------- PAGINA 1 ----------------
    b.pdf.start_page()
    b.draw_banner_p1()

    b.add_section_title("1. EL PODER DE LA VOZ: DE LA LECTURA AL PROGRAMA DE RADIO", (0.85, 0.50, 0.10))
    b.add_card_white(
        "COMO FUNCIONA EL MILAGRO AUDIO OVERVIEW DE GEMINI NOTEBOOK",
        [
            "El problema: Leer textos largos en pantalla cansa la vista de los alumnos mayores.",
            "La magia: Audio Overview convierte cualquier documento en una tertulia viva de radio profesional.",
            "Dos periodistas debaten, usan humor y metaforas, exponiendo pros y contras con agilidad.",
            "La clave: Tu puedes darles instrucciones para enfocar el debate antes de que graben el programa."
        ],
        badge="RADIO",
        border_color=(0.9, 0.6, 0.3),
        title_color=(0.85, 0.50, 0.10)
    )

    b.add_section_title("2. PREPARACION Y FUENTE FICTICIA DE EJEMPLO PARA CLASE", (0.15, 0.35, 0.65))
    b.add_card_white(
        "COMO PREPARAR EL CUADERNO DE DEBATE",
        [
            "1. Crea el cuaderno 'Tertulia de Debate'.",
            "2. Sube un articulo de actualidad o copia el texto de ejemplo de abajo como Fuente 1.",
            "3. En la columna derecha Studio, haz clic en el boton 'Personalizar' de Audio Overview."
        ],
        badge="PASOS",
        border_color=(0.4, 0.6, 0.8),
        title_color=(0.15, 0.35, 0.65)
    )

    b.add_card_white(
        "TEXTO MODELO DE NOTICIA PARA DEBATE (COPIA Y PEGA COMO FUENTE 1)",
        [
            "«INFORME DEBATE: Digitalizacion bancaria y mayores en 2026.",
            "  Por un lado, la banca digital permite pagar recibos y revisar movimientos desde el sofa sin colas.",
            "  Por otro lado, el cierre de sucursales y la retirada de cajeros genera soledad y exclusion en seniors.",
            "  Se debate si debe ser obligatorio por ley mantener atencion humana presencial sin cita previa.»"
        ],
        badge="NOTICIA",
        border_color=(0.9, 0.6, 0.3),
        title_color=(0.85, 0.50, 0.10)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # ---------------- PAGINA 2 (SIN CABECERA REPETIDA) ----------------
    b.pdf.start_page()
    b.draw_header_p2("Reto 5 · Personalizacion de la Radio y Descarga a tu Movil")

    b.add_section_title("3. INSTRUCCION DE PERSONALIZACION EN STUDIO > AUDIO OVERVIEW", (0.85, 0.50, 0.10))
    b.add_prompt_card_white(
        "PEGA ESTA INSTRUCCION EN 'PERSONALIZAR' ANTES DE GENERAR EL AUDIO",
        (
            "«Haz que los dos presentadores mantengan una tertulia de radio dinamica en formato debate:\n"
            "• El primer presentador defiende las ventajas de la tecnologia para la comodidad de los mayores.\n"
            "• La segunda presentadora plantea las dificultades de la brecha digital y la necesidad de atencion humana.\n"
            "• Ambos deben usar un tono ameno, con humor, sin tecnicismos y cerrando con una conclusion util.»"
        ),
        target_note="Pulsalo en Studio > Audio Overview > Personalizar"
    )

    b.add_section_title("4. COMO DISFRUTARLO: TU PODCAST PARA EL PASEO DIARIO", (0.10, 0.48, 0.35))
    b.add_card_white(
        "DESCARGA EL ARCHIVO MP3 EN 3 PASOS",
        [
            "1. Pulsa 'Generar' y espera de 3 a 5 minutos mientras se graba la tertulia de radio.",
            "2. En el reproductor, pulsa los 3 puntitos y dale a 'Descargar' para guardar el archivo MP3.",
            "3. Pasatelo al telefono movil para escucharlo con auriculares mientras das tu paseo matutino."
        ],
        badge="MOVIL",
        border_color=(0.3, 0.7, 0.45),
        title_color=(0.10, 0.48, 0.35)
    )

    b.draw_footer(2)
    b.pdf.end_page()
    b.pdf.write_to_file(b.filename)
    print(f"✅ Generado: {b.filename}")


def main():
    print("Iniciando compilacion de las 6 Fichas Didacticas con fondos blancos y Gemini Notebook...")
    compilar_reto_00()
    compilar_reto_01()
    compilar_reto_02()
    compilar_reto_03()
    compilar_reto_04()
    compilar_reto_05()
    print("✅ Todas las 6 Fichas Didacticas compiladas exitosamente en PDF para impresion.")

if __name__ == "__main__":
    main()
