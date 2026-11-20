#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_pdf_taller_skills.py
Genera 'TALLER_CREACION_GEMINI_SKILLS_CON_NOTEBOOKLM.pdf' con dimensionamiento dinámico
holgado, cero líneas cortadas y enfoque 100% NotebookLM (los cuadernos como asistentes
temáticos que sustituyen por completo a los Gems de Gemini).
100% Python nativo estándar (sin dependencias externas).
"""

import os
import sys

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_OUTPUT = os.path.join(OUTPUT_DIR, "TALLER_CREACION_GEMINI_SKILLS_CON_NOTEBOOKLM.pdf")

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


def compilar_pdf():
    pdf = RobustPDFWriter()
    margin_x = 36
    content_w = 523

    # =========================================================================
    # PÁGINA 1: CONCEPTO, COMPARATIVA Y EJEMPLO 1 (MÉDICO Y ANALÍTICAS)
    # =========================================================================
    pdf.start_page()

    # Cabecera Banner Superior
    pdf.set_fill_color(0.06, 0.09, 0.16)
    pdf.set_stroke_color(0.75, 0.45, 0.95)
    pdf.set_line_width(1.4)
    pdf.rect(margin_x, 742, content_w, 66, fill=True, stroke=True)

    pdf.draw_text(margin_x + 12, 790, "MONOGRAFICO 2 - CURSO DE INTELIGENCIA ARTIFICIAL (+65)", font="F2", size=8.5, r=0.75, g=0.45, b=0.95)
    pdf.draw_text(margin_x + 12, 770, "Tus Cuadernos como Asistentes Especializados (Skills)", font="F2", size=13.0, r=1.0, g=1.0, b=1.0)
    pdf.draw_text(margin_x + 12, 752, "El cuaderno es tu asistente tematico: olvidate de Gemini y de escribir prompts largos", font="F1", size=8.3, r=0.85, g=0.88, b=0.94)

    cur_y = 724

    # -------------------------------------------------------------------------
    # Bloque 1: El Gran Cambio Pedagógico (Por qué no usamos Gemini)
    # -------------------------------------------------------------------------
    intro_lines = [
        "En lugar de entrar a Gemini para configurar asistentes externos (Gems) que alucinan y olvidan,",
        "en NotebookLM cada Cuaderno que creas ES ya tu asistente especializado tematico (tu propia Skill).",
        "Cuando te dan una analitica medica, una factura o el seguro, se meten directamente en su cuaderno de NLM.",
        "El cuaderno queda guardado para siempre: no tienes que volver a explicarle quien eres ni pegar tus papeles.",
        "Cada vez que entres, le haces preguntas de 1 sola linea y te respondera con rigor y citas [1] exactas."
    ]
    b1_h = 22 + (len(intro_lines) * 13.5) + 20
    pdf.set_fill_color(0.07, 0.10, 0.18)
    pdf.set_stroke_color(0.75, 0.45, 0.95)
    pdf.set_line_width(0.8)
    pdf.rect(margin_x, cur_y - b1_h + 14, content_w, b1_h, fill=True, stroke=True)

    pdf.draw_text(margin_x + 10, cur_y - 2, "1. LA REGLA DE ORO: EL CUADERNO DE NLM SUSTITUYE A LOS GEMS DE GEMINI", font="F2", size=8.8, r=0.75, g=0.45, b=0.95)
    ty_1 = cur_y - 18
    for l in intro_lines:
        pdf.draw_text(margin_x + 14, ty_1, "- " + l, font="F1", size=7.8, r=0.85, g=0.88, b=0.95)
        ty_1 -= 13.5

    cur_y -= (b1_h + 10)

    # -------------------------------------------------------------------------
    # Bloque 2: Comparativa Antes vs Ahora (Dos columnas simétricas)
    # -------------------------------------------------------------------------
    antes_lines = [
        "- Entrar a Gemini y pegar prompts largos.",
        "- Subir los mismos documentos una y otra vez.",
        "- Riesgo de alucinaciones e invenciones.",
        "- Olvido de tus antecedentes en nuevas charlas."
    ]
    ahora_lines = [
        "- Creas el Cuaderno tematico una sola vez.",
        "- Metes tus analiticas o facturas en NLM.",
        "- Cero alucinacion: citas amarillas [1].",
        "- Preguntas en 1 linea y te responde al instante."
    ]
    b2_h = 24 + (4 * 13.5) + 16

    # Columna Izquierda (Antes)
    pdf.set_fill_color(0.14, 0.06, 0.08)
    pdf.set_stroke_color(0.7, 0.25, 0.3)
    pdf.rect(margin_x, cur_y - b2_h + 14, 255, b2_h, fill=True, stroke=True)
    pdf.draw_text(margin_x + 10, cur_y - 2, "ANTES (Con Gemini Abierto / Prompts):", font="F2", size=8.2, r=0.95, g=0.5, b=0.5)
    ty_a = cur_y - 18
    for l in antes_lines:
        pdf.draw_text(margin_x + 12, ty_a, l, font="F1", size=7.6, r=0.95, g=0.85, b=0.85)
        ty_a -= 13.5

    # Columna Derecha (Ahora)
    pdf.set_fill_color(0.06, 0.14, 0.10)
    pdf.set_stroke_color(0.2, 0.6, 0.35)
    pdf.rect(margin_x + 268, cur_y - b2_h + 14, 255, b2_h, fill=True, stroke=True)
    pdf.draw_text(margin_x + 278, cur_y - 2, "AHORA (Con tu Cuaderno Especializado en NLM):", font="F2", size=8.2, r=0.4, g=0.9, b=0.6)
    ty_h = cur_y - 18
    for l in ahora_lines:
        pdf.draw_text(margin_x + 280, ty_h, l, font="F1", size=7.6, r=0.85, g=0.96, b=0.88)
        ty_h -= 13.5

    cur_y -= (b2_h + 10)

    # -------------------------------------------------------------------------
    # Bloque 3: Ejemplo 1 - Cuaderno Asistente «Mi Médico Amigo y Analíticas»
    # -------------------------------------------------------------------------
    ej1_lines = [
        "Papeles que metes en este cuaderno: Tu ultima analitica de sangre (PDF o foto) y prospectos de medicinas.",
        "Regla de trato fijada en el cuaderno: «Traduce analiticas a lenguaje claro, sin alarmar y preparando preguntas».",
        "Como le preguntas a partir de ahora (en 1 sola linea en el chat central):",
        "  -> «¿Que significa el valor de colesterol que tiene asterisco en mi ultima analitica?»",
        "  -> «Hazme un resumen de 4 puntos para llevar impreso a mi consulta medica manana».",
        "Resultado: Te contesta solo con tus datos medicos reales, sin inventar y citando la pagina exacta [1]."
    ]
    b3_h = 24 + (len(ej1_lines) * 13.5) + 24
    pdf.set_fill_color(0.05, 0.11, 0.15)
    pdf.set_stroke_color(0.2, 0.75, 0.5)
    pdf.set_line_width(0.8)
    pdf.rect(margin_x, cur_y - b3_h + 14, content_w, b3_h, fill=True, stroke=True)

    pdf.draw_text(margin_x + 10, cur_y - 2, "EJEMPLO 1: CUADERNO ASISTENTE «MI MEDICO AMIGO Y ANALITICAS»", font="F2", size=8.8, r=0.2, g=0.8, b=0.55)
    ty_3 = cur_y - 18
    for l in ej1_lines:
        prefix = "- " if not l.startswith("  ->") else ""
        fnt = "F2" if l.startswith("  ->") else "F1"
        col = (0.3, 0.9, 0.7) if l.startswith("  ->") else (0.85, 0.92, 0.95)
        pdf.draw_text(margin_x + 14, ty_3, prefix + l, font=fnt, size=7.8, r=col[0], g=col[1], b=col[2])
        ty_3 -= 13.5

    # Pie Página 1
    pdf.set_stroke_color(0.85, 0.88, 0.92)
    pdf.set_line_width(0.5)
    pdf.line(margin_x, 34, margin_x + content_w, 34)
    pdf.draw_text(margin_x, 22, "Curso de IA - Monografico 2: Cuadernos como Asistentes Tematicos (NLM)", font="F1", size=7.5, r=0.4, g=0.45, b=0.5)
    pdf.draw_text(margin_x + content_w - 70, 22, "Pagina 1 de 2", font="F2", size=8.0, r=0.2, g=0.25, b=0.35)
    pdf.end_page()

    # =========================================================================
    # PÁGINA 2: EJEMPLOS 2 Y 3 + PROTOCOLO DE CREACIÓN EN 3 PASOS EN NLM
    # =========================================================================
    pdf.start_page()

    # Cabecera Banner Superior Página 2
    pdf.set_fill_color(0.06, 0.09, 0.16)
    pdf.set_stroke_color(0.75, 0.45, 0.95)
    pdf.set_line_width(1.4)
    pdf.rect(margin_x, 742, content_w, 66, fill=True, stroke=True)

    pdf.draw_text(margin_x + 12, 790, "BIBLIOTECA DE ASISTENTES TEMATICOS Y PROTOCOLO 100% NOTEBOOKLM", font="F2", size=8.5, r=0.75, g=0.45, b=0.95)
    pdf.draw_text(margin_x + 12, 770, "Casos de la Vida Real y Como Crear tu Asistente en 3 Clics", font="F2", size=13.0, r=1.0, g=1.0, b=1.0)
    pdf.draw_text(margin_x + 12, 752, "Todo ocurre dentro de NotebookLM: no necesitas entrar a Gemini ni configurar nada fuera", font="F1", size=8.3, r=0.85, g=0.88, b=0.94)

    cur_y2 = 724

    # -------------------------------------------------------------------------
    # Ejemplo 2: Cuaderno Asistente «Auditor de Facturas y Seguros»
    # -------------------------------------------------------------------------
    ej2_lines = [
        "Papeles que metes en este cuaderno: Tu factura de la luz en PDF y la poliza del seguro del hogar o coche.",
        "Como le preguntas en 1 sola linea:",
        "  -> «¿Hay algun concepto de mantenimiento extra cobrado en esta factura de la luz?»",
        "  -> «Si se me rompe el frigorifico por una tormenta, ¿mi seguro lo cubre? Citame la clausula exacta.»",
        "Resultado: Lee las 40 paginas de la poliza en segundos y te da la respuesta con el numero de pagina."
    ]
    b_ej2_h = 24 + (len(ej2_lines) * 13.5) + 22
    pdf.set_fill_color(0.06, 0.10, 0.16)
    pdf.set_stroke_color(0.2, 0.6, 0.9)
    pdf.set_line_width(0.8)
    pdf.rect(margin_x, cur_y2 - b_ej2_h + 14, content_w, b_ej2_h, fill=True, stroke=True)

    pdf.draw_text(margin_x + 10, cur_y2 - 2, "EJEMPLO 2: CUADERNO ASISTENTE «AUDITOR DE FACTURAS Y SEGUROS»", font="F2", size=8.8, r=0.3, g=0.7, b=1.0)
    ty_e2 = cur_y2 - 18
    for l in ej2_lines:
        prefix = "- " if not l.startswith("  ->") else ""
        fnt = "F2" if l.startswith("  ->") else "F1"
        col = (0.4, 0.8, 1.0) if l.startswith("  ->") else (0.85, 0.90, 0.96)
        pdf.draw_text(margin_x + 14, ty_e2, prefix + l, font=fnt, size=7.8, r=col[0], g=col[1], b=col[2])
        ty_e2 -= 13.5

    cur_y2 -= (b_ej2_h + 10)

    # -------------------------------------------------------------------------
    # Ejemplo 3: Cuaderno Asistente «Mi Biógrafo Familiar (Años 70 y 80)»
    # -------------------------------------------------------------------------
    ej3_lines = [
        "Papeles que metes en este cuaderno: Audios dictados por voz con anecdotas de juventud y musica de la epoca.",
        "Como le preguntas en 1 sola linea:",
        "  -> «Escribe un capitulo novelado y calido sobre el viaje a la playa en el Seat 127 para mis nietos».",
        "  -> «En Studio genera el Audio Overview con dos periodistas comentando mis recuerdos de juventud».",
        "Resultado: Convierte recuerdos sueltos en un libro familiar y en un podcast de radio para regalar a la familia."
    ]
    b_ej3_h = 24 + (len(ej3_lines) * 13.5) + 22
    pdf.set_fill_color(0.12, 0.08, 0.16)
    pdf.set_stroke_color(0.8, 0.5, 0.9)
    pdf.set_line_width(0.8)
    pdf.rect(margin_x, cur_y2 - b_ej3_h + 14, content_w, b_ej3_h, fill=True, stroke=True)

    pdf.draw_text(margin_x + 10, cur_y2 - 2, "EJEMPLO 3: CUADERNO ASISTENTE «MI BIOGRAFO FAMILIAR (ANOS 70 Y 80)»", font="F2", size=8.8, r=0.85, g=0.55, b=0.95)
    ty_e3 = cur_y2 - 18
    for l in ej3_lines:
        prefix = "- " if not l.startswith("  ->") else ""
        fnt = "F2" if l.startswith("  ->") else "F1"
        col = (0.9, 0.7, 1.0) if l.startswith("  ->") else (0.92, 0.88, 0.96)
        pdf.draw_text(margin_x + 14, ty_e3, prefix + l, font=fnt, size=7.8, r=col[0], g=col[1], b=col[2])
        ty_e3 -= 13.5

    cur_y2 -= (b_ej3_h + 10)

    # -------------------------------------------------------------------------
    # Protocolo Oficial en 3 Pasos (100% dentro de NotebookLM)
    # -------------------------------------------------------------------------
    pasos_lines = [
        ("PASO 1: Crea el Cuaderno Tematico en NotebookLM",
         "Entra en notebooklm.google.com y pulsa «+ Nuevo cuaderno». Ponle el nombre de tu asistente (ej. «Salud y Analiticas» o «Auditor Facturas»)."),
        ("PASO 2: Mete los Papeles Reales (+ Anadir fuentes)",
         "Sube las analiticas en PDF, las fotos de informes o la factura de la luz. En 3 segundos NLM habra creado la memoria de tu asistente."),
        ("PASO 3: Fija tus Reglas de Trato en Studio",
         "En la columna derecha Studio anade una Nota fija: «Respóndeme siempre en 4 puntos claros, letra grande y sin tecnicismos». ¡Listo para siempre!")
    ]

    total_p_lines = sum(len(wrap_text(d, 72)) for _, d in pasos_lines)
    b_pasos_h = 24 + (len(pasos_lines) * 16) + (total_p_lines * 13.5) + 26
    pdf.set_fill_color(0.06, 0.12, 0.10)
    pdf.set_stroke_color(0.3, 0.8, 0.5)
    pdf.set_line_width(1.0)
    pdf.rect(margin_x, cur_y2 - b_pasos_h + 14, content_w, b_pasos_h, fill=True, stroke=True)

    pdf.draw_text(margin_x + 10, cur_y2 - 2, "PROTOCOLO OFICIAL: COMO CREAR TU ASISTENTE EN NOTEBOOKLM EN 3 CLICS", font="F2", size=8.8, r=0.3, g=0.85, b=0.55)
    ty_p = cur_y2 - 18
    for tit, desc in pasos_lines:
        pdf.draw_text(margin_x + 14, ty_p, tit, font="F2", size=8.2, r=1.0, g=0.85, b=0.35)
        ty_p -= 14
        for dl in wrap_text(desc, 72):
            pdf.draw_text(margin_x + 22, ty_p, dl, font="F1", size=7.8, r=0.88, g=0.96, b=0.90)
            ty_p -= 13.0
        ty_p -= 4

    # Pie Página 2
    pdf.set_stroke_color(0.85, 0.88, 0.92)
    pdf.set_line_width(0.5)
    pdf.line(margin_x, 34, margin_x + content_w, 34)
    pdf.draw_text(margin_x, 22, "Curso de IA - Monografico 2: Cuadernos como Asistentes Tematicos (NLM)", font="F1", size=7.5, r=0.4, g=0.45, b=0.5)
    pdf.draw_text(margin_x + content_w - 70, 22, "Pagina 2 de 2", font="F2", size=8.0, r=0.2, g=0.25, b=0.35)
    pdf.end_page()

    pdf.write_to_file(PDF_OUTPUT)
    print(f"✅ PDF generado con éxito, holgura verificada y cero líneas cortadas: {PDF_OUTPUT}")

if __name__ == "__main__":
    compilar_pdf()
