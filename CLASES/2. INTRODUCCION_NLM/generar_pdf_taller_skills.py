#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_pdf_taller_skills.py
Genera 'TALLER_CREACION_GEMINI_SKILLS_CON_NOTEBOOKLM.pdf' con diseño claro,
tipografía legible para personas mayores, cajas de ejemplos prácticos y guía paso a paso.
100% Python nativo estándar.
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

    # =========================================================================
    # PÁGINA 1: CONCEPTO, COMPARATIVA Y EL PRIMER EJEMPLO PRÁCTICO
    # =========================================================================
    pdf.start_page()

    # Cabecera Banner
    pdf.set_fill_color(0.06, 0.09, 0.16)
    pdf.set_stroke_color(0.22, 0.74, 0.97)
    pdf.set_line_width(1.5)
    pdf.rect(36, 740, 523, 72, fill=True, stroke=True)

    pdf.draw_text(48, 792, "MONOGRAFICO 2 - CURSO DE INTELIGENCIA ARTIFICIAL", font="F2", size=9, r=0.22, g=0.74, b=0.97)
    pdf.draw_text(48, 772, "Taller: Como Crear tus Propias Gemini Skills con NotebookLM", font="F2", size=14, r=1.0, g=1.0, b=1.0)
    pdf.draw_text(48, 752, "El fin de los prompts largos: convierte tu cuaderno en una fabrica de asistentes tematicos", font="F1", size=8.5, r=0.8, g=0.85, b=0.9)

    y = 718

    # Bloque 1: Que es una Gemini Skill
    pdf.set_fill_color(0.08, 0.12, 0.20)
    pdf.set_stroke_color(0.18, 0.25, 0.35)
    pdf.set_line_width(1.0)
    pdf.rect(36, y - 85, 523, 85, fill=True, stroke=True)

    pdf.draw_text(48, y - 18, "1. QUE ES UNA «GEMINI SKILL» Y POR QUE CAMBIA LAS REGLAS DEL JUEGO", font="F2", size=10.5, r=0.22, g=0.74, b=0.97)
    intro_p = ("En Google Gemini, las «Skills» son asistentes especializados preconfigurados. "
               "En lugar de tener que teclear o pegar un prompt de 15 lineas cada vez que abres una conversacion, "
               "la Skill guarda internamente sus conocimientos, su personalidad y sus reglas de comportamiento. "
               "Basta con activarla con una sola palabra o comando para que Gemini sepa exactamente como responderte.")
    for l in wrap_text(intro_p, 88):
        y -= 14
        pdf.draw_text(48, y - 18, l, font="F1", size=8.5, r=0.9, g=0.9, b=0.95)

    y -= 105

    # Bloque 2: Comparativa Antes vs Ahora
    pdf.set_fill_color(0.12, 0.08, 0.08)
    pdf.set_stroke_color(0.6, 0.2, 0.2)
    pdf.rect(36, y - 75, 255, 75, fill=True, stroke=True)
    pdf.draw_text(44, y - 16, "ANTES (Metodo Tradicional Frustrante):", font="F2", size=8.5, r=0.95, g=0.6, b=0.6)
    antes_txt = ("- Escribir instrucciones largas cada dia.\n"
                 "- Si olvidas un detalle, Gemini te da tecnicismos.\n"
                 "- Ansiedad y pereza al volver a empezar de cero.")
    y_antes = y - 16
    for l in wrap_text(antes_txt, 46):
        y_antes -= 12
        pdf.draw_text(44, y_antes, l, font="F1", size=7.8, r=0.85, g=0.8, b=0.8)

    pdf.set_fill_color(0.06, 0.14, 0.10)
    pdf.set_stroke_color(0.2, 0.6, 0.35)
    pdf.rect(304, y - 75, 255, 75, fill=True, stroke=True)
    pdf.draw_text(312, y - 16, "AHORA (Con Gemini Skills + NotebookLM):", font="F2", size=8.5, r=0.5, g=0.9, b=0.65)
    ahora_txt = ("- Configuras la habilidad una sola vez.\n"
                 "- Se invoca con un nombre corto (ej. /banco).\n"
                 "- Tono paciente, claro y adaptado a mayores.")
    y_ahora = y - 16
    for l in wrap_text(ahora_txt, 46):
        y_ahora -= 12
        pdf.draw_text(312, y_ahora, l, font="F1", size=7.8, r=0.8, g=0.95, b=0.85)

    y -= 95

    # Bloque 3: El Secreto del Cuaderno
    pdf.set_fill_color(0.05, 0.12, 0.18)
    pdf.set_stroke_color(0.22, 0.74, 0.97)
    pdf.rect(36, y - 70, 523, 70, fill=True, stroke=True)
    pdf.draw_text(48, y - 16, "2. EL SECRETO: GEMINI NOTEBOOK COMO CREADOR AUTOMATICO DE SKILLS", font="F2", size=10, r=0.22, g=0.74, b=0.97)
    sec_txt = ("Disenar instrucciones perfectas a mano es dificil. Por eso usamos Gemini Notebook como fabrica: "
               "cargas en el cuaderno las especificaciones de Google, le pides en espanol corriente lo que necesitas "
               "(ejemplo: «Quiero un asistente que me explique analisis medicos sin asustarme») y el cuaderno "
               "redacta el prompt tecnico oficial listo para guardar en tu cuenta de Gemini.")
    y_sec = y - 16
    for l in wrap_text(sec_txt, 90):
        y_sec -= 13
        pdf.draw_text(48, y_sec, l, font="F1", size=8.3, r=0.85, g=0.92, b=0.98)

    y -= 90

    # Bloque 4: Ejemplo 1
    pdf.set_fill_color(0.08, 0.10, 0.16)
    pdf.set_stroke_color(0.75, 0.52, 0.98)
    pdf.rect(36, y - 125, 523, 125, fill=True, stroke=True)
    pdf.draw_text(48, y - 18, "EJEMPLO 1: «/banco-claro» - El Cazador de Comisiones Bancarias", font="F2", size=10, r=0.75, g=0.52, b=0.98)
    pdf.draw_text(48, y - 32, "Utilidad: Sube una foto de un recibo o carta del banco y te senala comisiones sorpresa en cristiano.", font="F3", size=8, r=0.7, g=0.75, b=0.85)

    prompt_1 = ("Prompt guardado en la Skill:\n"
                "«Eres Banco Claro, asesor financiero paciente para personas mayores de 65 anos.\n"
                "Reglas: 1. Habla sin tecnicismos bancarios y con total transparencia.\n"
                "2. Al recibir un recibo o carta, busca de inmediato: comisiones de mantenimiento, subidas no avisadas\n"
                "y fechas limite de cancelacion.\n"
                "3. Concluye siempre con un cuadro titulado QUE DEBO HACER con 3 pasos practicos y la frase exacta\n"
                "que el usuario debe decir en ventanilla para defender sus ahorros.»")
    y_p1 = y - 36
    for l in wrap_text(prompt_1, 88):
        y_p1 -= 11.5
        pdf.draw_text(48, y_p1, l, font="F1", size=7.8, r=0.92, g=0.92, b=0.95)

    # Pie Página 1
    pdf.draw_text(48, 30, "Monografico 2 • Curso de IA para Seniors • Ficha Didactica Gemini Skills", font="F1", size=8, r=0.5, g=0.55, b=0.65)
    pdf.draw_text(520, 30, "Pagina 1 / 2", font="F2", size=8, r=0.5, g=0.55, b=0.65)
    pdf.end_page()

    # =========================================================================
    # PÁGINA 2: EJEMPLOS 2 Y 3 + GUÍA DE ACTIVACIÓN EN 3 PASOS
    # =========================================================================
    pdf.start_page()

    # Cabecera Página 2
    pdf.set_fill_color(0.06, 0.09, 0.16)
    pdf.set_stroke_color(0.22, 0.74, 0.97)
    pdf.rect(36, 760, 523, 48, fill=True, stroke=True)
    pdf.draw_text(48, 788, "EJEMPLOS PRACTICOS PARA EL DIA A DIA Y PROTOCOLO EN 3 PASOS", font="F2", size=11, r=0.22, g=0.74, b=0.97)
    pdf.draw_text(48, 772, "Configuraciones listas para copiar en gemini.google.com > Administrador de Gems / Skills", font="F1", size=8.2, r=0.8, g=0.85, b=0.9)

    y2 = 740

    # Ejemplo 2: Medico Amigo
    pdf.set_fill_color(0.08, 0.10, 0.16)
    pdf.set_stroke_color(0.2, 0.8, 0.6)
    pdf.rect(36, y2 - 130, 523, 130, fill=True, stroke=True)
    pdf.draw_text(48, y2 - 18, "EJEMPLO 2: «/medico-amigo» - El Explicador de Analiticas y Prospectos", font="F2", size=10, r=0.2, g=0.8, b=0.6)
    pdf.draw_text(48, y2 - 32, "Utilidad: Traduce analiticas de sangre y prospectos a lenguaje cotidiano sin alarmar.", font="F3", size=8, r=0.7, g=0.75, b=0.85)

    prompt_2 = ("Prompt guardado en la Skill:\n"
                "«Eres Medico Amigo, divulgador de salud empatico y pedagogico para personas mayores.\n"
                "Reglas: 1. Jamas des diagnosticos definitivos ni alarmes; traduce los terminos medicos dificiles.\n"
                "2. Si te presentan una analitica, explica que mide cada parametro alterado usando analogias cotidianas\n"
                "(ejemplo: 'el colesterol es como el trafico en las tuberias') y aclara si es habitual por la edad.\n"
                "3. Concluye siempre con una tarjeta llamada PREGUNTAS PARA MI DOCTOR con 3 preguntas concretas\n"
                "y claras para llevar apuntadas a la proxima consulta medica.»")
    y_p2 = y2 - 36
    for l in wrap_text(prompt_2, 88):
        y_p2 -= 11.5
        pdf.draw_text(48, y_p2, l, font="F1", size=7.8, r=0.92, g=0.92, b=0.95)

    y2 -= 145

    # Ejemplo 3: Mi Biografo
    pdf.set_fill_color(0.08, 0.10, 0.16)
    pdf.set_stroke_color(0.98, 0.75, 0.2)
    pdf.rect(36, y2 - 130, 523, 130, fill=True, stroke=True)
    pdf.draw_text(48, y2 - 18, "EJEMPLO 3: «/mi-biografo» - El Cronista de Memorias y Relatos Familiares", font="F2", size=10, r=0.98, g=0.75, b=0.2)
    pdf.draw_text(48, y2 - 32, "Utilidad: Dictas un recuerdo desordenado por voz y te lo escribe como capitulo novelado.", font="F3", size=8, r=0.7, g=0.75, b=0.85)

    prompt_3 = ("Prompt guardado en la Skill:\n"
                "«Eres Mi Biografo, un escritor literario y cronista de la memoria oral familiar.\n"
                "Reglas: 1. Recibe cualquier relato o recuerdo dictado por voz por muy informal que sea.\n"
                "2. Transforma la anecdota en un capitulo de 3 parrafos con estilo literario calido y emotivo,\n"
                "ambientando la epoca (los olores de la cocina, las calles, la radio de la epoca).\n"
                "3. Conserva siempre los nombres propios, apodos y expresiones locales que use el narrador.\n"
                "4. Finaliza con una pregunta inspiradora para seguir recordando otros detalles complementarios.»")
    y_p3 = y2 - 36
    for l in wrap_text(prompt_3, 88):
        y_p3 -= 11.5
        pdf.draw_text(48, y_p3, l, font="F1", size=7.8, r=0.92, g=0.92, b=0.95)

    y2 -= 150

    # Guía en 3 Pasos
    pdf.set_fill_color(0.06, 0.10, 0.18)
    pdf.set_stroke_color(0.22, 0.74, 0.97)
    pdf.rect(36, y2 - 150, 523, 150, fill=True, stroke=True)
    pdf.draw_text(48, y2 - 18, "COMO GUARDAR TU SKILL EN GEMINI EN 3 CLICS SENCILLOS", font="F2", size=10.5, r=0.22, g=0.74, b=0.97)

    pasos = [
        ("PASO 1: Pide la Skill a Gemini Notebook",
         "Abre tu cuaderno de NotebookLM y dile en espanol: «Escribeme una Skill de Gemini para...». El cuaderno redactara el texto tecnico."),
        ("PASO 2: Entra en Gemini y crea el nuevo Gem",
         "Abre gemini.google.com en tu navegador o iPad. En el menu izquierdo haz clic en «Gems / Skills» y selecciona «+ Nuevo Gem»."),
        ("PASO 3: Pega las instrucciones y guarda",
         "Asignale un nombre corto (ej. Banco Claro) y pega las instrucciones copiadas. Pulsa «Guardar». ¡Tu asistente estara listo para siempre!")
    ]

    y_paso = y2 - 20
    for titulo, desc in pasos:
        y_paso -= 16
        pdf.draw_text(48, y_paso, titulo, font="F2", size=8.8, r=1.0, g=0.85, b=0.4)
        for dl in wrap_text(desc, 86):
            y_paso -= 11.5
            pdf.draw_text(48, y_paso, dl, font="F1", size=8, r=0.85, g=0.9, b=0.95)

    # Pie Página 2
    pdf.draw_text(48, 30, "Monografico 2 • Curso de IA para Seniors • Enlace video oficial: youtu.be/n2-YWzDpGZY", font="F1", size=8, r=0.5, g=0.55, b=0.65)
    pdf.draw_text(520, 30, "Pagina 2 / 2", font="F2", size=8, r=0.5, g=0.55, b=0.65)
    pdf.end_page()

    pdf.write_to_file(PDF_OUTPUT)
    print(f"PDF generado con exito: {PDF_OUTPUT}")

if __name__ == "__main__":
    compilar_pdf()
