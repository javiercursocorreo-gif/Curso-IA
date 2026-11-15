#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_niv_007.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter):
9. NIV-007_Los_5_Niveles_de_Automatizacin_e_IA_en_e.pdf
para la Sesión 07 del Curso de IA.

Contenido:
- Título: Los 5 Niveles de Automatización e IA en el Hogar Senior (+65)
- Metodología: Generación y ejecución directa en Gemini + BKP Oficial.
- Prompt Maestro exacto para generar la micro-app de diagnóstico y niveles de confort.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/07_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "9. NIV-007_Los_5_Niveles_de_Automatizacin_e_IA_en_e.pdf")

ALT_PATHS = [
    "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/09. [NIV] BLOQUE_9_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20/NIV-007_Los_5_Niveles_de_Automatizacion_e_IA_en_el_Hogar.pdf",
    "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/[NIV] BLOQUE_10_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20/NIV-007_Los_5_Niveles_de_Automatizacion_e_IA_en_el_Hogar.pdf"
]

def escape_pdf_text(text):
    text = str(text)
    text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    replacements = {
        'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
        'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
        'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
        '«': '<<', '»': '>>', '•': '-', '—': '-', '–': '-',
        'º': 'o', 'ª': 'a', '¿': '\xbf', '¡': '\xa1',
        '➔': '->', '→': '->', '’': "'", '‘': "'", '“': '"', '”': '"'
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

class NativePDFWriter:
    def __init__(self, page_width=612.0, page_height=792.0):
        self.w = page_width
        self.h = page_height
        self.pages = []
        self.current_stream = []

    def start_page(self):
        self.current_stream = []

    def end_page(self):
        self.pages.append(''.join(self.current_stream))
        self.current_stream = []

    def set_fill_color(self, r, g, b):
        self.current_stream.append(f'{r:.3f} {g:.3f} {b:.3f} rg\n')

    def set_stroke_color(self, r, g, b):
        self.current_stream.append(f'{r:.3f} {g:.3f} {b:.3f} RG\n')

    def set_line_width(self, width):
        self.current_stream.append(f'{width:.2f} w\n')

    def rect(self, x, y, width, height, fill=True, stroke=True):
        op = 'B' if (fill and stroke) else ('f' if fill else 'S')
        self.current_stream.append(f'{x:.2f} {y:.2f} {width:.2f} {height:.2f} re {op}\n')

    def line(self, x1, y1, x2, y2):
        self.current_stream.append(f'{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S\n')

    def draw_text(self, x, y, text, font='F1', size=10, r=0, g=0, b=0):
        self.set_fill_color(r, g, b)
        escaped = escape_pdf_text(text)
        self.current_stream.append(f'BT /{font} {size} Tf {x:.2f} {y:.2f} Td ({escaped}) Tj ET\n')

    def write_to_file(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        page_obj_indices = []
        content_obj_indices = []
        cur_obj_idx = 6

        for _ in self.pages:
            page_obj_indices.append(cur_obj_idx)
            cur_obj_idx += 1
            content_obj_indices.append(cur_obj_idx)
            cur_obj_idx += 1

        kids_str = ' '.join([f'{idx} 0 R' for idx in page_obj_indices])
        pages_dict = f'<< /Type /Pages /Kids [{kids_str}] /Count {len(self.pages)} >>'.encode('ascii')

        all_objs = [
            b'<< /Type /Catalog /Pages 2 0 R >>',
            pages_dict,
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>',
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>',
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>',
        ]

        for i, page_stream in enumerate(self.pages):
            content_idx = content_obj_indices[i]
            p_obj = (
                f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.w} {self.h}] '
                f'/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> '
                f'/Contents {content_idx} 0 R >>'
            ).encode('ascii')
            all_objs.append(p_obj)

            s_bytes = page_stream.encode('latin1', errors='replace')
            c_obj = f'<< /Length {len(s_bytes)} >>\nstream\n'.encode('ascii') + s_bytes + b'\nendstream'
            all_objs.append(c_obj)

        with open(filename, 'wb') as f:
            f.write(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
            offsets = []
            for i, obj in enumerate(all_objs, start=1):
                offsets.append(f.tell())
                f.write(f'{i} 0 obj\n'.encode('ascii'))
                f.write(obj)
                f.write(b'\nendobj\n')

            xref_offset = f.tell()
            f.write(b'xref\n')
            f.write(f'0 {len(all_objs) + 1}\n'.encode('ascii'))
            f.write(b'0000000000 65535 f \n')
            for off in offsets:
                f.write(f'{off:010d} 00000 n \n'.encode('ascii'))

            f.write(b'trailer\n')
            f.write(f'<< /Size {len(all_objs) + 1} /Root 1 0 R >>\n'.encode('ascii'))
            f.write(b'startxref\n')
            f.write(f'{xref_offset}\n'.encode('ascii'))
            f.write(b'%%EOF\n')

def build_niv_007_pdf(output_path=PDF_PATH):
    pdf = NativePDFWriter(page_width=612.0, page_height=792.0)
    pdf.start_page()

    # Fondo general
    pdf.set_fill_color(0.98, 0.99, 0.99)
    pdf.set_stroke_color(0.05, 0.55, 0.65)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal
    pdf.set_fill_color(0.04, 0.22, 0.28)
    pdf.rect(24, 716, 564, 52, fill=True, stroke=False)

    pdf.draw_text(36, 750, 'SESION 07 • FICHA DIDACTICA DE CREACION CON GEMINI [NIV-007]', font='F2', size=8.5, r=0.4, g=0.85, b=0.9)
    pdf.draw_text(36, 730, 'Los 5 Niveles de Automatizacion e IA en el Hogar Senior (+65)', font='F2', size=13.0, r=1, g=1, b=1)

    # Seccion 1: Metodologia Directa en 2 Pasos
    pdf.set_fill_color(0.93, 0.98, 0.98)
    pdf.set_stroke_color(0.1, 0.55, 0.65)
    pdf.set_line_width(1.0)
    pdf.rect(30, 580, 552, 125, fill=True, stroke=True)

    pdf.draw_text(42, 692, 'METODOLOGIA DIRECTA: GENERACION Y VISUALIZACION EN PANTALLA SIN CODIGO', font='F2', size=9.2, r=0.05, g=0.35, b=0.45)

    p1_title = 'PASO 1 • Copiar el Prompt en Gemini (gemini.google.com):'
    p1_desc = 'Pega el texto del recuadro inferior en Gemini. El prompt esta calibrado para que Gemini abra y ejecute directamente el simulador interactivo en pantalla (Canvas / Vista previa) en pleno funcionamiento, sin pedirte pasos de codigo.'
    p1_lines = wrap_text(p1_desc, 114)
    pdf.draw_text(42, 676, p1_title, font='F2', size=8.0, r=0.05, g=0.45, b=0.55)
    pdf.draw_text(42, 665, p1_lines[0], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    if len(p1_lines) > 1:
        pdf.draw_text(42, 655, p1_lines[1], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p2_title = 'PASO 2 • Experimentar y Dialogar con Gemini en el Aula:'
    p2_desc = 'Marca los dispositivos de tu casa, descubre tu nivel de confort y tiempo ganado, y reflexiona con las 3 preguntas inferiores sobre la tranquilidad y seguridad que aporta la tecnologia amigable.'
    pdf.draw_text(42, 638, p2_title, font='F2', size=8.0, r=0.05, g=0.45, b=0.55)
    pdf.draw_text(42, 627, p2_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p3_title = 'GARANTIA OFICIAL • Copia de Respaldo Garantizada (BKP Oficial en el Mapa):'
    p3_desc = 'Si por saturacion o corte de red la IA no visualiza el modelo interactivo, pulsa en el Cuadro de Mando del curso:'
    p3_btn = '«Abrir Simulador Automatizacion Hogar (+65) (HTML)» para acceder a la aplicacion oficial garantizada.'
    pdf.draw_text(42, 610, p3_title, font='F2', size=8.0, r=0.8, g=0.3, b=0.1)
    pdf.draw_text(42, 599, p3_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    pdf.draw_text(42, 588, p3_btn, font='F2', size=7.8, r=0.05, g=0.45, b=0.55)

    # Seccion 2: Prompt Maestro para Gemini
    pdf.set_fill_color(0.95, 0.99, 0.99)
    pdf.set_stroke_color(0.12, 0.58, 0.68)
    pdf.set_line_width(1.0)
    pdf.rect(30, 360, 552, 210, fill=True, stroke=True)

    pdf.draw_text(42, 555, 'PROMPT MAESTRO PARA CREAR EL SIMULADOR DE AUTOMATIZACION DEL HOGAR (+65):', font='F2', size=9.0, r=0.05, g=0.35, b=0.45)
    pdf.draw_text(42, 542, '(Selecciona y copia todo el bloque de texto para pegarlo en gemini.google.com)', font='F3', size=7.4, r=0.4, g=0.45, b=0.5)

    # Recuadro interior del prompt
    pdf.set_fill_color(0.90, 0.97, 0.97)
    pdf.set_stroke_color(0.15, 0.62, 0.72)
    pdf.set_line_width(0.8)
    pdf.rect(40, 370, 532, 160, fill=True, stroke=True)

    prompt_lines = [
        "\"Actua como un experto en domotica amigable y divulgador tecnologico para personas mayores (+65).",
        "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador sobre el hogar senior:",
        "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
        "1. Escala de 5 niveles: 1) Mecanizacion basica, 2) Hogar programable, 3) Salud y conexion, 4) Voz, 5) IA Gemini.",
        "2. Test interactivo del hogar: casillas de seleccion para lavadora, microondas con reloj, Smart TV, Alexa y Gemini.",
        "3. Calculador de horas de vida ahorradas: indicador visual de tiempo libre semanal ganado gracias a la tecnologia.",
        "4. Termometro de confianza tecnologica: selector de actitud (timida, prudente, normal, buena o entusiasta).",
        "5. Consejos practicos para dar el siguiente paso sin miedo: dictado por voz, recordatorios hablados y consultas faciles.",
        "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
    ]
    y_pr = 516
    for pl in prompt_lines:
        is_bold = pl.startswith('"Actua') or pl.startswith('Requisitos') or pl.startswith('1.') or pl.startswith('2.') or pl.startswith('3.') or pl.startswith('4.') or pl.startswith('5.') or pl.startswith('Ergonomia')
        pdf.draw_text(48, y_pr, pl, font='F2' if is_bold else 'F1', size=7.2, r=0.05, g=0.25, b=0.3)
        y_pr -= 13.0

    # Seccion 3: Dialogo y Preguntas de Reflexion con Gemini en el Aula
    pdf.set_fill_color(0.99, 0.98, 0.96)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 225, 552, 122, fill=True, stroke=True)

    pdf.draw_text(42, 332, 'PREGUNTAS DE DIALOGO CON GEMINI EN EL AULA (DOMOTICA Y TRANQUILIDAD SENIOR):', font='F2', size=8.8, r=0.7, g=0.35, b=0.05)

    q1 = "Pregunta 1 • La Tranquilidad y el Control en Casa: \"Gemini, ¿por que automatizar tareas cotidianas (como encender luces por sensor o pedir la radio con la voz) no significa perder el control ni acomodarse, sino ganar seguridad y bienestar?\""
    q1_lines = wrap_text(q1, 114)
    pdf.draw_text(42, 316, q1_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 305, q1_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q2 = "Pregunta 2 • El Poder del Dictado por Voz: \"Gemini, ¿como puede una persona mayor que tiene dificultad para teclear en la pantalla tactil usar el microfono del teclado y la IA para dictar mensajes largos o notas sin cansancio visual?\""
    q2_lines = wrap_text(q2, 114)
    pdf.draw_text(42, 288, q2_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 277, q2_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q3 = "Pregunta 3 • La IA como Secretaria Personal: \"Gemini, ¿de que formas cotidianas puedes ayudarme en el dia a dia: resumiendo un prospecto de medicamento, recordando fechas importantes o redactando una reclamacion formal?\""
    q3_lines = wrap_text(q3, 114)
    pdf.draw_text(42, 260, q3_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 249, q3_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 212, 582, 212)
    pdf.draw_text(36, 198, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 07 • MICRO-APLICACIONES [NIV]', font='F2', size=7.2, r=0.08, g=0.35, b=0.45)
    pdf.draw_text(36, 186, 'Metodologia de Visualizacion Directa (Canvas / Gemini) • Respaldo: SIMULADOR_AUTOMATIZACION_TRABAJO_IA_SENIORS.html', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ PDF generado exitosamente: {output_path}")

    for alt in ALT_PATHS:
        try:
            os.makedirs(os.path.dirname(alt), exist_ok=True)
            shutil.copy2(output_path, alt)
            print(f"📦 Copia sincronizada en: {alt}")
        except Exception:
            pass

if __name__ == '__main__':
    build_niv_007_pdf()
