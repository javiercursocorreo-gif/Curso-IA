#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_pdf_retos_vida_real.py
Compila las 6 fichas didácticas oficiales de Retos de Vida Real y Comparativa
para Gemini Notebook (NotebookLM), cada una con 2 páginas A4 holgadas, sin solapamientos
y con cálculo dinámico de cajas de texto. 100% Python nativo estándar.
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
    def __init__(self, filename, title_badge, title_main, subtitle_main, primary_color=(0.22, 0.74, 0.97)):
        self.filename = filename
        self.pdf = RobustPDFWriter()
        self.title_badge = title_badge
        self.title_main = title_main
        self.subtitle_main = subtitle_main
        self.primary_color = primary_color
        self.margin_x = 36
        self.content_w = 523
        self.cur_y = 800

    def draw_banner(self, p_num):
        self.pdf.set_fill_color(0.06, 0.09, 0.16)
        self.pdf.set_stroke_color(self.primary_color[0], self.primary_color[1], self.primary_color[2])
        self.pdf.set_line_width(1.4)
        self.pdf.rect(self.margin_x, 742, self.content_w, 66, fill=True, stroke=True)

        self.pdf.draw_text(self.margin_x + 12, 790, self.title_badge.upper(), font="F2", size=8.5, r=self.primary_color[0], g=self.primary_color[1], b=self.primary_color[2])
        self.pdf.draw_text(self.margin_x + 12, 770, self.title_main, font="F2", size=13.0, r=1.0, g=1.0, b=1.0)
        self.pdf.draw_text(self.margin_x + 12, 752, self.subtitle_main, font="F1", size=8.4, r=0.82, g=0.86, b=0.92)
        self.cur_y = 726

    def draw_footer(self, p_num):
        self.pdf.set_stroke_color(0.85, 0.88, 0.92)
        self.pdf.set_line_width(0.5)
        self.pdf.line(self.margin_x, 34, self.margin_x + self.content_w, 34)
        self.pdf.draw_text(self.margin_x, 22, f"Curso de IA - Monografico 2: Gemini Notebook - {self.title_main}", font="F1", size=7.5, r=0.4, g=0.45, b=0.5)
        self.pdf.draw_text(self.margin_x + self.content_w - 70, 22, f"Pagina {p_num} de 2", font="F2", size=8.0, r=0.2, g=0.25, b=0.35)

    def add_section_title(self, title, color_rgb=(0.15, 0.35, 0.65)):
        self.pdf.set_fill_color(color_rgb[0], color_rgb[1], color_rgb[2])
        self.pdf.rect(self.margin_x, self.cur_y - 3, self.content_w, 18, fill=True, stroke=False)
        self.pdf.draw_text(self.margin_x + 8, self.cur_y + 2, title.upper(), font="F2", size=8.5, r=1.0, g=1.0, b=1.0)
        self.cur_y -= 26

    def add_card(self, title, lines_list, badge=None, border_color=(0.85, 0.88, 0.92), bg_color=(0.98, 0.98, 0.99), title_color=(0.12, 0.25, 0.55)):
        line_spacing = 13.0
        rendered_lines = []
        for it in lines_list:
            it_wrapped = wrap_text(it, max_chars=80)
            rendered_lines.append(it_wrapped)

        total_lines = sum(len(l) for l in rendered_lines)
        h_box = 22 + (total_lines * line_spacing) + 8

        self.pdf.set_fill_color(bg_color[0], bg_color[1], bg_color[2])
        self.pdf.set_stroke_color(border_color[0], border_color[1], border_color[2])
        self.pdf.set_line_width(0.7)
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
                prefix = "- " if idx_l == 0 else "  "
                fnt = "F2" if (idx_l == 0 and ":" in line) else "F1"
                self.pdf.draw_text(self.margin_x + 14, ty, prefix + line, font=fnt, size=8.0, r=0.20, g=0.22, b=0.26)
                ty -= line_spacing

        self.cur_y -= (h_box + 8)

    def add_prompt_card(self, label, prompt_str, target_note="Pegar en el chat central o panel Studio"):
        prompt_lines = wrap_text(prompt_str, max_chars=78)
        line_spacing = 12.0
        n_lines = len(prompt_lines)
        b_h = 16 + 16 + (n_lines * line_spacing) + 18

        self.pdf.set_fill_color(0.04, 0.07, 0.12)
        self.pdf.set_stroke_color(self.primary_color[0], self.primary_color[1], self.primary_color[2])
        self.pdf.set_line_width(0.8)
        self.pdf.rect(self.margin_x, self.cur_y - b_h + 14, self.content_w, b_h, fill=True, stroke=True)

        # Header bar dentro
        self.pdf.set_fill_color(0.09, 0.14, 0.22)
        self.pdf.rect(self.margin_x + 1, self.cur_y - 2, self.content_w - 2, 15, fill=True, stroke=False)
        self.pdf.draw_text(self.margin_x + 8, self.cur_y + 2, label.upper(), font="F2", size=7.6, r=self.primary_color[0], g=self.primary_color[1], b=self.primary_color[2])
        self.pdf.draw_text(self.margin_x + self.content_w - 210, self.cur_y + 2, target_note, font="F3", size=7.0, r=0.7, g=0.75, b=0.82)

        ty = self.cur_y - 16
        for l in prompt_lines:
            self.pdf.draw_text(self.margin_x + 12, ty, l, font="F3", size=7.6, r=0.74, g=0.90, b=1.0)
            ty -= line_spacing

        self.cur_y -= (b_h + 8)


# =========================================================================
# COMPILADORES ESPECÍFICOS DE LAS 6 FICHAS
# =========================================================================

def compilar_reto_00():
    b = RetoPDFBuilder(
        os.path.join(OUTPUT_DIR, "FICHA_RETO_00_COMPARATIVA_GEMINI_VS_NOTEBOOKLM.pdf"),
        "Monografico 2 - Ficha de Sintesis y Comparativa",
        "Comparativa Clave: Gemini Abierto vs Gemini Notebook",
        "El Creador Creativo del Mundo frente al Notario Privado con Cero Alucinacion",
        primary_color=(0.75, 0.42, 0.10)
    )

    # PAGINA 1
    b.pdf.start_page()
    b.draw_banner(1)

    b.add_section_title("1. EL GRAN DILEMA: ¿CUANDO ABRIR GEMINI Y CUANDO GEMINI NOTEBOOK?", (0.75, 0.42, 0.10))
    b.add_card(
        "LA METAFORA FUNDAMENTAL: EL INVENTOR FRENTE AL NOTARIO",
        [
            "Gemini Normal (El Creador Abierto): Es como un gran inventor y bibliotecario universal que ha leido todo Internet.",
            "  Sabe escribir poesias, idear viajes, traducir idiomas y redactar cartas creativas con chispa y soltura.",
            "  Su gran debilidad: Alucinacion. Si no sabe un dato exacto, puede inventarlo con total elocuencia.",
            "Gemini Notebook (El Notario Privado): Es un archivero con candado riguroso que solo sabe lo que tu le pones encima de la mesa.",
            "  No opina sobre el mundo exterior ni inventa nada: responde exclusivamente con tus papeles.",
            "  Su gran fortaleza: Cero alucinacion y cita obligatoria [1] con subrayado amarillo verificable al instante."
        ],
        badge="METAFORA",
        border_color=(0.90, 0.80, 0.65),
        bg_color=(0.99, 0.98, 0.95),
        title_color=(0.75, 0.42, 0.10)
    )

    b.add_section_title("2. TABLA COMPARATIVA: RADIOGRAFIA FRENTE A FRENTE", (0.15, 0.35, 0.65))
    b.add_card(
        "DIFERENCIAS ESENCIALES PARA TU DIA A DIA",
        [
            "1. Origen de la Informacion: Gemini consulta todo Internet publico; NotebookLM solo tus archivos subidos.",
            "2. Fiabilidad de Datos: En Gemini debes dudar de datos exactos; en NotebookLM cada palabra viene de tu papel.",
            "3. Privacidad y Seguridad: Tus documentos en NotebookLM no se usan para entrenar la IA de Google.",
            "4. Aislamiento de Fuentes: En NotebookLM puedes marcar o desmarcar [v] para interrogar un unico documento.",
            "5. Salidas Multimedia: NotebookLM genera audios de debate con dos periodistas, infografias y webs de un clic."
        ],
        badge="TABLA",
        border_color=(0.70, 0.82, 0.95),
        bg_color=(0.95, 0.97, 1.00),
        title_color=(0.15, 0.35, 0.65)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # PAGINA 2
    b.pdf.start_page()
    b.draw_banner(2)

    b.add_section_title("3. CUANDO USAR CADA HERRAMIENTA (GUIA DE DECISION RAPIDA)", (0.10, 0.48, 0.35))
    b.add_card(
        "EJEMPLOS PRACTICOS PARA NO EQUIVOCARSE EN CLASE",
        [
            "USA GEMINI NORMAL CUANDO:",
            "  - Quieres una idea para felicitar un cumpleanos o un itinerario para un viaje el proximo mes.",
            "  - Buscas aprender que es la fotosintesis o pedirle que te explique como funciona la computacion cuantica.",
            "  - Quieres redactar una poesia, un menu de cocina con lo que tienes en la nevera o practicar ingles.",
            "USA GEMINI NOTEBOOK CUANDO:",
            "  - Tienes informes medicos, analiticas o prospectos y quieres saber que significan sin confusiones.",
            "  - Quieres auditar la factura de la luz, el contrato del seguro o una clausula bancaria.",
            "  - Tienes apuntes de clase, documentos historicos o un libro en PDF y quieres estudiarlo a fondo.",
            "  - Quieres convertir varios textos familiares en una tertulia de radio (podcast) o en una infografia."
        ],
        badge="DECISION",
        border_color=(0.70, 0.88, 0.78),
        bg_color=(0.94, 0.98, 0.95),
        title_color=(0.10, 0.48, 0.35)
    )

    b.add_section_title("4. EL FLUJO DE TRABAJO PERFECTO DEL ALUMNO SENIOR", (0.45, 0.20, 0.65))
    b.add_prompt_card(
        "PROMPT MAESTRO PARA GEMINI NORMAL ANTES DE ENTRAR A NOTEBOOKLM",
        (
            "«Actua como un documentalista riguroso. Voy a investigar sobre las energias renovables para mayores. "
            "Redacta un documento claro de 3 paginas con hechos comprobados, datos de coste medio y comparativas, "
            "listo para que yo lo descargue en texto y lo analice en mi cuaderno privado de Gemini Notebook.»"
        ),
        target_note="Gemini Normal -> Genera el documento -> Subelo a NotebookLM"
    )

    b.add_card(
        "LOS TRES MANDAMIENTOS FINALES",
        [
            "1. La Creatividad nace en Gemini; la Rigurosidad y el Notariado se ejercen en NotebookLM.",
            "2. Nunca tomes una decision legal o medica con Gemini abierto sin verificar con tus fuentes en el Cuaderno.",
            "3. Ambos comparten tu cuenta de Google: los cuadernos que creas se complementan mutuamente."
        ],
        badge="REGLAS",
        border_color=(0.85, 0.75, 0.95),
        bg_color=(0.98, 0.95, 1.00),
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
        primary_color=(0.20, 0.70, 0.45)
    )

    # PAGINA 1
    b.pdf.start_page()
    b.draw_banner(1)

    b.add_section_title("1. EL PROBLEMA COTIDIANO Y EL OBJETIVO DEL RETO", (0.10, 0.48, 0.35))
    b.add_card(
        "DE LA CARPETA CAOTICA AL EXPEDIENTE MEDICO EN SEGUNDOS",
        [
            "El problema: Acumulamos analiticas, informes de especialistas y prospectos en cajones o carpetas de plastico.",
            "  Cuando llegamos a la consulta medica, apenas tenemos 10 minutos y olvidamos los antecedentes clave.",
            "La solucion con NotebookLM: Crear el cuaderno privado 'Mi Historial de Salud Familiar'.",
            "  Subir fotos de analiticas (PDF o JPG), informes de altas o recetas escaneadas y prospectos oficiales.",
            "Garantia de Oro: NotebookLM no inventara patologias: solo explicara lo que tus analisis reales dictaminan."
        ],
        badge="SALUD",
        border_color=(0.70, 0.88, 0.78),
        bg_color=(0.94, 0.98, 0.95),
        title_color=(0.10, 0.48, 0.35)
    )

    b.add_section_title("2. PREPARACION DE FUENTES: PASO A PASO EN CLASE", (0.15, 0.35, 0.65))
    b.add_card(
        "COMO CARGAR TUS PAPELES DE SALUD CON SEGURIDAD",
        [
            "1. Abre Gemini Notebook y pulsa '+ Nuevo cuaderno'. Titulalo 'Salud - Mi Expediente y Consultas'.",
            "2. En el panel izquierdo '+ Anadir fuentes', sube tu analitica reciente y un informe medico en PDF.",
            "3. Enlace web adicional: Puedes anadir el enlace oficial del prospecto de tu medicacion desde CIMA (AEMPS).",
            "4. Comprueba que las casillas de verificacion [v] estan marcadas para que el cuaderno cruce la informacion."
        ],
        badge="PASOS",
        border_color=(0.70, 0.82, 0.95),
        bg_color=(0.95, 0.97, 1.00),
        title_color=(0.15, 0.35, 0.65)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # PAGINA 2
    b.pdf.start_page()
    b.draw_banner(2)

    b.add_section_title("3. PROMPTS MAESTROS PARA PREPARAR LA CONSULTA MEDICA", (0.10, 0.45, 0.65))
    b.add_prompt_card(
        "PROMPT 1: RESUMEN CRONOLOGICO PARA LLEVAR IMPRESO AL ESPECIALISTA",
        (
            "«Lee todos los informes medicos subidos y genera un resumen ejecutivo cronologico en 5 puntos:\n"
            "1. Antecedentes relevantes diagnosticados.\n"
            "2. Medicacion activa que tomo y dosis.\n"
            "3. Valores de la ultima analitica que se desvian del rango normal.\n"
            "4. Sintomas o dudas pendientes comunicadas en consultas anteriores.\n"
            "5. Tres preguntas concretas para formularle hoy al doctor en los 10 minutos de consulta.»"
        ),
        target_note="Chat central de NotebookLM"
    )

    b.add_prompt_card(
        "PROMPT 2: TRADUCTOR DE ANALITICAS A LENGUAJE CLARO Y TRANQUILIZADOR",
        (
            "«Explicame en lenguaje sencillo, para una persona de 65 anos sin conocimientos medicos, "
            "que significan los valores que tienen asterisco en mi ultima analitica. "
            "Indica en que pagina del analisis aparece cada dato con su cita [1] y aclara si son leves desviaciones.»"
        ),
        target_note="Chat central de NotebookLM"
    )

    b.add_section_title("4. PRODUCTO FINAL EN PANEL STUDIO", (0.75, 0.42, 0.10))
    b.add_card(
        "INFOGRAFIA Y ADVERTENCIA VITAL",
        [
            "En el panel derecho Studio, pulsa 'Infografia' (estilo Cientifico) con el prompt: 'Dibuja mi rutina diaria de medicacion con horarios'.",
            "Salvaguarda medica obligatoria: NotebookLM no sustituye a tu medico de cabecera ni receta farmacos.",
            "  Su funcion es darte claridad mental y empoderarte para que aproveches al maximo tus visitas al ambulatorio."
        ],
        badge="RECUERDA",
        border_color=(0.90, 0.80, 0.65),
        bg_color=(0.99, 0.98, 0.95),
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
        primary_color=(0.85, 0.25, 0.20)
    )

    # PAGINA 1
    b.pdf.start_page()
    b.draw_banner(1)

    b.add_section_title("1. EL PROBLEMA: LA PLAGA DE LAS CADENAS FALSAS EN EL TELEFONO", (0.80, 0.20, 0.20))
    b.add_card(
        "EL MIEDO Y LA URGENCIA COMO ARMA DE ENGANO",
        [
            "El problema: Cada semana recibimos en WhatsApp mensajes alarmistas de familiares bienintencionados:",
            "  '¡No comas limones hervidos!', '¡Nuevo virus que borra el banco!', '¡Cierra tu cuenta antes de medianoche!'.",
            "La vulnerabilidad: Los bulos juegan con las emociones, la salud y el dinero, imitando comunicados oficiales.",
            "El metodo del detective con NotebookLM: Poner frente a frente el texto dudoso contra la fuente oficial acreditada."
        ],
        badge="ALERTA",
        border_color=(0.95, 0.75, 0.75),
        bg_color=(0.99, 0.95, 0.95),
        title_color=(0.80, 0.20, 0.20)
    )

    b.add_section_title("2. PREPARACION DE FUENTES EN EL CUADERNO", (0.15, 0.35, 0.65))
    b.add_card(
        "COMO CARGAR EL CASO PARA AUDITARLO",
        [
            "1. Crea un cuaderno titulado 'Cazador de Bulos WhatsApp'.",
            "2. Fuente A (El Sospechoso): Pega como archivo de texto o copia el mensaje viral recibido en el chat.",
            "3. Fuente B (La Verdad Oficial): Sube un comunicado del Ministerio de Sanidad, Policía Nacional o desmentido verificado.",
            "4. Marca ambas fuentes [v] para que NotebookLM las compare linea por linea."
        ],
        badge="METODO",
        border_color=(0.70, 0.82, 0.95),
        bg_color=(0.95, 0.97, 1.00),
        title_color=(0.15, 0.35, 0.65)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # PAGINA 2
    b.pdf.start_page()
    b.draw_banner(2)

    b.add_section_title("3. PROMPTS MAESTROS DEL DETECTIVE DIGITAL", (0.80, 0.20, 0.20))
    b.add_prompt_card(
        "PROMPT 1: AUDITORIA DE VERACIDAD Y DETECCION DE TRAMPAS",
        (
            "«Compara el mensaje viral de la Fuente A con la documentacion oficial de la Fuente B y responde:\n"
            "1. ¿Que afirmaciones del mensaje son completamente falsas o carecen de respaldo cientifico?\n"
            "2. ¿Que tecnicas de manipulacion utiliza (urgencia artificial, mayusculas excesivas, pedir reenviar)?\n"
            "3. Dictamen final: ¿Es Bulo Puro, Noticia Manipulada o Verdad?»"
        ),
        target_note="Chat central de NotebookLM"
    )

    b.add_prompt_card(
        "PROMPT 2: MENSAJE CARINOSO Y DIPLOMATICO PARA EL GRUPO FAMILIAR",
        (
            "«Redacta un mensaje breve, educado y muy afectuoso para reenviar al grupo familiar de WhatsApp. "
            "Debe explicar por que la cadena recibida no es cierta, citar la fuente oficial con serenidad "
            "y agradecer a quien lo envio su buena intencion para que nadie se sienta ofendido.»"
        ),
        target_note="Chat central de NotebookLM"
    )

    b.add_section_title("4. TRABAJO EN STUDIO: CREAR ALERTA VISUAL", (0.10, 0.48, 0.35))
    b.add_card(
        "INFOGRAFIA Y PODCAST EXPLICATIVO",
        [
            "En Studio, pulsa 'Infografia' con el prompt: 'Crea un cartel de advertencia con las 3 senales para detectar un bulo de salud'.",
            "Audio Overview: Puedes generar la tertulia de radio donde dos presentadores explican de forma amena el desmentido.",
            "Regla de Oro: Ante la duda en WhatsApp, ¡nunca reenvies hasta verificar en tu propio cuaderno!"
        ],
        badge="EXITO",
        border_color=(0.70, 0.88, 0.78),
        bg_color=(0.94, 0.98, 0.95),
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
        primary_color=(0.55, 0.25, 0.75)
    )

    # PAGINA 1
    b.pdf.start_page()
    b.draw_banner(1)

    b.add_section_title("1. EL VALOR DE TU MEMORIA: UNA EPOCA UNICA DE ESPANA", (0.50, 0.20, 0.70))
    b.add_card(
        "NUESTRA GENERACION NO VIVIO LA POSGUERRA: VIVIO EL GRAN CAMBIO",
        [
            "Los alumnos nacidos hacia 1960 fueron la juventud de los anos 70 y 80: los anos del Seat 127, los casetes,",
            "  la tele en color, la Transicion democratica, los primeros viajes por carretera y los guateques con amigos.",
            "El problema: Esas vivencias se quedan en charlas de sobremesa y los hijos y nietos no conocen los detalles.",
            "El reto: Convertir tus notas de voz o textos dictados en un libro de memorias estructurado y una tertulia de radio."
        ],
        badge="MEMORIA",
        border_color=(0.85, 0.75, 0.95),
        bg_color=(0.98, 0.95, 1.00),
        title_color=(0.50, 0.20, 0.70)
    )

    b.add_section_title("2. QUE FUENTES SUBIR A TU CUADERNO FAMILIAR", (0.15, 0.35, 0.65))
    b.add_card(
        "MATERIA PRIMA EN TRES SENCILLOS PASOS",
        [
            "1. Dicta por voz en tu movil o PC 3 anecdotas reales (tu primer sueldo, las vacaciones de verano, como conociste a tu pareja).",
            "2. Sube ese archivo de texto como Fuente 1 a NotebookLM.",
            "3. Sube como Fuente 2 una lista de tus canciones favoritas de los 70 y 80 (Duo Dinamico, Camilo Sesto, Mecano).",
            "4. Opcional: Sube un recorte o cronologia de noticias de la epoca de 1975 a 1982."
        ],
        badge="FUENTES",
        border_color=(0.70, 0.82, 0.95),
        bg_color=(0.95, 0.97, 1.00),
        title_color=(0.15, 0.35, 0.65)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # PAGINA 2
    b.pdf.start_page()
    b.draw_banner(2)

    b.add_section_title("3. PROMPTS MAESTROS PARA REVIVIR LA HISTORIA", (0.50, 0.20, 0.70))
    b.add_prompt_card(
        "PROMPT 1: CRONICA NOVELADA DE NUESTRA JUVENTUD (PARA NIETOS)",
        (
            "«Con las anecdotas de mis fuentes, redacta un capitulo literario y emotivo titulado 'Nuestra Juventud en los 70 y 80'. "
            "Describe como era el dia a dia, el sonido de los cassettes, la ilusion del primer coche y las costumbres familiares. "
            "Manten mi propia voz y anade un toque de carino pensando en que lo lean mis nietos dentro de 20 anos.»"
        ),
        target_note="Chat central de NotebookLM"
    )

    b.add_prompt_card(
        "PROMPT 2: EL CUESTIONARIO BIOGRAFICO PARA SEGUIR ESCRIBIENDO",
        (
            "«Leeme con atencion y hazme 5 preguntas sugerentes sobre momentos que he mencionado de pasada "
            "(como mi primer trabajo o como era la vida sin moviles) para que yo pueda dictar nuevos audios y completar mi libro.»"
        ),
        target_note="Chat central de NotebookLM"
    )

    b.add_section_title("4. EL GRAN BROCHE DE ORO EN STUDIO: LA RADIO FAMILIAR", (0.10, 0.48, 0.35))
    b.add_card(
        "ESCUCHAR TU VIDA EN AUDIO OVERVIEW",
        [
            "Pulsa en Studio el boton 'Audio Overview (Resumen de Audio)':",
            "  Dos presentadores de radio mantendran una conversacion apasionante sobre tu vida y tus recuerdos de los 70 y 80.",
            "Descarga el MP3 resultante y compartelo en el grupo de WhatsApp de tus hijos. ¡Sera el regalo familiar del ano!"
        ],
        badge="LEGADO",
        border_color=(0.70, 0.88, 0.78),
        bg_color=(0.94, 0.98, 0.95),
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
        primary_color=(0.10, 0.55, 0.85)
    )

    # PAGINA 1
    b.pdf.start_page()
    b.draw_banner(1)

    b.add_section_title("1. EL RETO: DEFENDERSE DE LA COMPLEJIDAD Y EL LABERINTO LEGAL", (0.10, 0.45, 0.75))
    b.add_card(
        "ADIOS A LA LETRA PEQUENA INCOMPRENSIBLE",
        [
            "El problema: Facturas electricas llenas de peajes, terminos de potencia y servicios de mantenimiento sorpresa.",
            "  Polizas de seguro de 45 paginas donde nunca sabemos si una gotera o rotura de electrodomestico esta cubierta.",
            "La solucion: Subir el PDF real del contrato a NotebookLM y convertirlo en un asesor financiero privado.",
            "Ventaja crucial: NotebookLM te dira la pagina y linea exacta donde se explica cada cobro o exclusion."
        ],
        badge="AUDITORIA",
        border_color=(0.70, 0.85, 0.95),
        bg_color=(0.95, 0.97, 1.00),
        title_color=(0.10, 0.45, 0.75)
    )

    b.add_section_title("2. PREPARACION DEL DOCUMENTO EN NOTEBOOKLM", (0.15, 0.35, 0.65))
    b.add_card(
        "COMO SUBIR TU FACTURA O CONTRATO EN 3 MINUTOS",
        [
            "1. Descarga de la web de tu compania (Iberdrola, Endesa, aseguradora) la factura o poliza en formato PDF.",
            "2. Entra en NotebookLM, crea el cuaderno 'Auditor Facturas y Seguros' y sube el archivo con '+ Anadir fuentes'.",
            "3. En la zona central observaras de inmediato el resumen automatico con el nombre de la empresa y fecha."
        ],
        badge="SUBIDA",
        border_color=(0.70, 0.82, 0.95),
        bg_color=(0.95, 0.97, 1.00),
        title_color=(0.15, 0.35, 0.65)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # PAGINA 2
    b.pdf.start_page()
    b.draw_banner(2)

    b.add_section_title("3. PROMPTS MAESTROS PARA DESCIFRAR CADA CENTIMO", (0.10, 0.45, 0.75))
    b.add_prompt_card(
        "PROMPT 1: RADIOGRAFIA DE LA FACTURA DE LA LUZ Y DETECCION DE COBROS EXTRA",
        (
            "«Desglosa esta factura de la luz en 4 conceptos faciles de entender:\n"
            "1. ¿Cuanto pago por potencia contratada (termino fijo)?\n"
            "2. ¿Cuanto pago por la energia realmente consumida (kWh)?\n"
            "3. ¿Hay algun concepto de seguro, mantenimiento, urgencias o servicios extra que encarezca el recibo?\n"
            "4. ¿Que precio exacto por kWh estoy pagando y como se compara con una tarifa razonable?»"
        ),
        target_note="Chat central de NotebookLM"
    )

    b.add_prompt_card(
        "PROMPT 2: AUDITORIA DEL SEGURO DEL HOGAR (SIMULACRO DE SINIESTRO)",
        (
            "«Imagina que se me ha roto el frigorifico por una subida de tension y se ha estropeado la comida. "
            "Revisa mi poliza y dime con exactitud si esta cubierto, cual es el limite maximo de indemnizacion "
            "y en que articulo y pagina del contrato se especifica la condicion.»"
        ),
        target_note="Chat central de NotebookLM"
    )

    b.add_section_title("4. PRODUCTO FINAL EN PANEL STUDIO: INFORME DE AHORRO", (0.10, 0.48, 0.35))
    b.add_card(
        "INFORME FORMAL Y CARTA DE RECLAMACION",
        [
            "Boton 'Informe' en Studio: Genera un documento ejecutivo para reclamar a la compania o comparar con la competencia.",
            "Prompt adicional de redaccion: 'Escribe una carta formal solicitando la baja de los servicios extra que no contrate'.",
            "Poder en tus manos: Nunca mas pagaras por conceptos que no entiendes."
        ],
        badge="AHORRO",
        border_color=(0.70, 0.88, 0.78),
        bg_color=(0.94, 0.98, 0.95),
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
        primary_color=(0.95, 0.60, 0.10)
    )

    # PAGINA 1
    b.pdf.start_page()
    b.draw_banner(1)

    b.add_section_title("1. EL PODER DE LA VOZ: DE LA LECTURA PESADA AL PROGRAMA DE RADIO", (0.85, 0.50, 0.10))
    b.add_card(
        "COMO FUNCIONA EL MILAGRO AUDIO OVERVIEW DE NOTEBOOKLM",
        [
            "El reto: Leer documentos largos, leyes complejas o libros tecnicos en pantalla cansa la vista de los seniors.",
            "La magia: NotebookLM es capaz de transformar cualquier texto en una tertulia viva entre dos periodistas de radio.",
            "No es un robot leyendo con voz fria: bromean, se interrumpen con elegancia, usan metaforas y debaten posturas.",
            "Lo mejor: Tu puedes indicarles como enfocar el debate antes de que empiecen a grabar el programa."
        ],
        badge="RADIO",
        border_color=(0.95, 0.85, 0.65),
        bg_color=(0.99, 0.97, 0.94),
        title_color=(0.85, 0.50, 0.10)
    )

    b.add_section_title("2. PREPARACION DE FUENTES EN EL CUADERNO", (0.15, 0.35, 0.65))
    b.add_card(
        "ELIGE UN TEMA DE DEBATE APASIONANTE",
        [
            "1. Sube un articulo de opinion o reportaje sobre pensiones, inteligencia artificial, coches electricos o salud.",
            "2. Opcional: Anade dos fuentes con visiones opuestas (ejemplo: pros y contras de la energia nuclear o digitalizacion bancaria).",
            "3. Ve directamente a la columna derecha Studio y localiza el bloque superior 'Audio Overview'."
        ],
        badge="CONFIG",
        border_color=(0.70, 0.82, 0.95),
        bg_color=(0.95, 0.97, 1.00),
        title_color=(0.15, 0.35, 0.65)
    )

    b.draw_footer(1)
    b.pdf.end_page()

    # PAGINA 2
    b.pdf.start_page()
    b.draw_banner(2)

    b.add_section_title("3. LA CLAVE DEL EXITO: PERSONALIZAR EL DEBATE ANTES DE GRABAR", (0.85, 0.50, 0.10))
    b.add_prompt_card(
        "INSTRUCCION MAESTRA EN EL BOTON 'PERSONALIZAR' DE AUDIO OVERVIEW",
        (
            "«Haz que los dos presentadores mantengan una tertulia de radio dinamica en formato debate:\n"
            "• El primer presentador defiende las ventajas y el progreso que aporta la tecnologia a los mayores.\n"
            "• La segunda presentadora plantea con sensatez las dudas, brechas digitales y riesgos de exclusion.\n"
            "• Ambos deben usar un tono ameno, con buen humor, sin tecnicismos y cerrando con una conclusion util.»"
        ),
        target_note="Studio > Audio Overview > Personalizar"
    )

    b.add_section_title("4. COMO APROVECHAR AL MAXIMO LA ESCUCHA", (0.10, 0.48, 0.35))
    b.add_card(
        "PASEAR Y APRENDER: TU PODCAST PRIVADO EN EL MOVIL",
        [
            "1. Pulsa 'Generar': en unos 3 a 5 minutos tendras tu programa de radio de 8 a 12 minutos listo.",
            "2. Pulsa los tres puntitos en el reproductor de audio y selecciona 'Descargar' para guardar el MP3.",
            "3. Metetelo en el movil para escucharlo con auriculares mientras das tu paseo diario o vas en coche.",
            "4. Comprobacion de citas: Si algo que dijeron te llama la atencion, buscalo en el chat de NotebookLM para ver la fuente."
        ],
        badge="MOVIL",
        border_color=(0.70, 0.88, 0.78),
        bg_color=(0.94, 0.98, 0.95),
        title_color=(0.10, 0.48, 0.35)
    )

    b.draw_footer(2)
    b.pdf.end_page()
    b.pdf.write_to_file(b.filename)
    print(f"✅ Generado: {b.filename}")


def main():
    print("Iniciando compilacion de las 6 Fichas Didacticas de Retos de Vida Real...")
    compilar_reto_00()
    compilar_reto_01()
    compilar_reto_02()
    compilar_reto_03()
    compilar_reto_04()
    compilar_reto_05()
    print("✅ Todas las 6 Fichas Didacticas compiladas exitosamente en PDF.")

if __name__ == "__main__":
    main()
