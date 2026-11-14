#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_niv_005.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter):
9. NIV-005_Los_5_Niveles_de_la_Evolucin_del_Dinero.pdf
para la Sesión 05 del Curso de IA.

Contenido:
- Título: Los 5 Niveles de la Evolución del Dinero: Del Trueque a Bizum (+65)
- Metodología: Generación y ejecución directa en Gemini + BKP Oficial.
- Prompt Maestro exacto para generar la app de tranquilidad financiera y pagos seguros.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/05_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "9. NIV-005_Los_5_Niveles_de_la_Evolucin_del_Dinero.pdf")

ALT_PATHS = [
    "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/09. [NIV] BLOQUE_9_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20/NIV-005_Los 5 Niveles de la Evolución del Dinero.pdf",
    "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/[NIV] BLOQUE_10_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20/NIV-005_Los_5_Niveles_de_la_Evolucin_del_Dinero.pdf"
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
            f.write(b'%PDF-1.4\n')
            offsets = []
            cur_offset = f.tell()

            for i, obj in enumerate(all_objs):
                offsets.append(cur_offset)
                obj_num = i + 1
                f.write(f'{obj_num} 0 obj\n'.encode('ascii'))
                f.write(obj)
                f.write(b'\nendobj\n')
                cur_offset = f.tell()

            xref_offset = cur_offset
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

def build_niv_005_pdf(output_path=PDF_PATH):
    pdf = NativePDFWriter(612.0, 792.0)
    pdf.start_page()

    # Marco exterior esmeralda y oro
    pdf.set_fill_color(0.99, 0.995, 0.99)
    pdf.set_stroke_color(0.05, 0.55, 0.35)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal
    pdf.set_fill_color(0.04, 0.22, 0.14)
    pdf.rect(24, 716, 564, 52, fill=True, stroke=False)

    pdf.draw_text(36, 750, 'SESION 05 • MICRO-APLICACION DE VIDA REAL (+65) [NIV-005]', font='F2', size=8.5, r=0.4, g=0.9, b=0.6)
    pdf.draw_text(36, 730, 'Los 5 Niveles de la Evolucion del Dinero: Del Trueque a Bizum (+65)', font='F2', size=13.0, r=1, g=1, b=1)

    # Seccion 1: Metodologia Directa en 2 Pasos
    pdf.set_fill_color(0.94, 0.985, 0.95)
    pdf.set_stroke_color(0.1, 0.65, 0.4)
    pdf.set_line_width(1.0)
    pdf.rect(30, 580, 552, 126, fill=True, stroke=True)

    pdf.draw_text(42, 692, 'METODOLOGIA DIRECTA: GENERACION Y VISUALIZACION EN PANTALLA SIN CODIGO', font='F2', size=9.2, r=0.05, g=0.4, b=0.2)

    p1_title = 'PASO 1 • Copiar el Prompt Maestro en Gemini (gemini.google.com):'
    p1_desc = 'Abre Gemini en tu navegador y pega el recuadro inferior. El prompt esta calibrado para que Gemini abra y ejecute directamente la aplicacion interactiva en pantalla (Canvas / Vista previa) sin obligarte a revisar codigo.'
    p1_lines = wrap_text(p1_desc, 114)
    pdf.draw_text(42, 676, p1_title, font='F2', size=8.0, r=0.05, g=0.5, b=0.3)
    pdf.draw_text(42, 665, p1_lines[0], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    if len(p1_lines) > 1:
        pdf.draw_text(42, 655, p1_lines[1], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p2_title = 'PASO 2 • Experimentar y Dialogar con Gemini en el Aula:'
    p2_desc = 'Selecciona tu medio de pago habitual, comprueba el termometro de seguridad frente a perdidas y robos, y plantea a Gemini las 3 preguntas de tranquilidad digital de abajo.'
    pdf.draw_text(42, 638, p2_title, font='F2', size=8.0, r=0.05, g=0.5, b=0.3)
    pdf.draw_text(42, 627, p2_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p3_title = 'GARANTIA OFICIAL • Copia de Respaldo Oficial Garantizada (BKP en el Mapa):'
    p3_desc = 'Si deseas abrir la aplicacion terminada y depurada con voz y diseno senior, pulsa en el Cuadro de Mando del curso:'
    p3_btn = '«🛡️ Abrir Simulador Evolucion del Dinero (+65) (HTML)» para interactuar de inmediato con total tranquilidad.'
    pdf.draw_text(42, 610, p3_title, font='F2', size=8.0, r=0.7, g=0.3, b=0.05)
    pdf.draw_text(42, 599, p3_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    pdf.draw_text(42, 588, p3_btn, font='F2', size=7.8, r=0.05, g=0.5, b=0.3)

    # Seccion 2: Prompt Maestro para Gemini
    pdf.set_fill_color(0.96, 0.99, 0.97)
    pdf.set_stroke_color(0.15, 0.6, 0.35)
    pdf.set_line_width(1.0)
    pdf.rect(30, 360, 552, 210, fill=True, stroke=True)

    pdf.draw_text(42, 555, 'PROMPT MAESTRO PARA CREAR EL SIMULADOR DE EVOLUCION DEL DINERO (+65):', font='F2', size=9.0, r=0.05, g=0.4, b=0.25)
    pdf.draw_text(42, 542, '(Selecciona y copia todo el bloque de texto para pegarlo en gemini.google.com)', font='F3', size=7.4, r=0.4, g=0.45, b=0.5)

    # Recuadro interior del prompt
    pdf.set_fill_color(0.91, 0.97, 0.93)
    pdf.set_stroke_color(0.18, 0.65, 0.4)
    pdf.set_line_width(0.8)
    pdf.rect(40, 370, 532, 160, fill=True, stroke=True)

    prompt_lines = [
        "\"Actua como un educador financiero y pedagogo digital para personas mayores (+65).",
        "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador sobre la evolucion del dinero:",
        "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
        "1. Nivel 1: Trueque y mercancias basicas (intercambio directo de sal, trigo o ganado en sociedades antiguas).",
        "2. Nivel 2: Monedas de oro y plata (aparicion del dinero contable de curso legal y patron metalico).",
        "3. Nivel 3: Billetes de papel y libreta de ahorros tradicional (el dinero impreso y bancario de toda la vida).",
        "4. Nivel 4: Tarjetas con chip contactless y cajeros automaticos (seguridad bancaria frente a robos en la calle).",
        "5. Nivel 5: Pagos inmediatos por movil (Bizum, compras online y doble factor biometrico con IA).",
        "Controles interactivos: Selector del medio de pago, termometro de riesgo ante perdidas y guia practica de Bizum.",
        "Ergonomia Senior (+60): Botones grandes, alto contraste, modo lectura y lenguaje claro que transmita tranquilidad.\""
    ]
    y_pr = 516
    for pl in prompt_lines:
        is_bold = pl.startswith('"Actua') or pl.startswith('Requisitos') or pl.startswith('1.') or pl.startswith('2.') or pl.startswith('3.') or pl.startswith('4.') or pl.startswith('5.') or pl.startswith('Ergonomia')
        pdf.draw_text(48, y_pr, pl, font='F2' if is_bold else 'F1', size=7.2, r=0.05, g=0.25, b=0.15)
        y_pr -= 12.0

    # Seccion 3: Dialogo y Preguntas de Reflexion con Gemini en el Aula
    pdf.set_fill_color(0.99, 0.98, 0.96)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 225, 552, 122, fill=True, stroke=True)

    pdf.draw_text(42, 332, 'PREGUNTAS DE DIALOGO CON GEMINI EN EL AULA (TRANQUILIDAD Y SEGURIDAD):', font='F2', size=8.8, r=0.7, g=0.35, b=0.05)

    q1 = "Pregunta 1 • La Seguridad Real de Bizum vs. Billetes en la Calle: \"Gemini, muchos mayores tememos que nos roben si usamos el movil para pagar. ¿Por que en realidad pagar con Bizum o tarjeta es mucho mas seguro que llevar 200 euros en billetes en la cartera o el bolso?\""
    q1_lines = wrap_text(q1, 114)
    pdf.draw_text(42, 316, q1_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 305, q1_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q2 = "Pregunta 2 • Que Hacer si te Equivocas de Numero al Enviar un Bizum: \"Gemini, ¿como funciona la doble verificacion de Bizum (que muestra el nombre del destinatario antes de confirmar) y que pasos debes dar en tu banco si por error mandas dinero al numero equivocado?\""
    q2_lines = wrap_text(q2, 114)
    pdf.draw_text(42, 288, q2_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 277, q2_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q3 = "Pregunta 3 • La Libreta de Ahorros vs. la Pantalla del Telefono: \"Gemini, ¿por que los bancos estan retirando las libretas fisicas de papel y como puede un adulto mayor configurar la aplicacion bancaria para ver los apuntes con letra grande y sin complicaciones?\""
    q3_lines = wrap_text(q3, 114)
    pdf.draw_text(42, 260, q3_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 249, q3_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 212, 582, 212)
    pdf.draw_text(36, 198, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 05 • MICRO-APLICACIONES [NIV]', font='F2', size=7.2, r=0.25, g=0.4, b=0.3)
    pdf.draw_text(36, 186, 'Metodologia de Visualizacion Directa (Canvas / Gemini) • Respaldo: SIMULADOR_EVOLUCION_DINERO_SENIORS.html', font='F3', size=6.8, r=0.4, g=0.5, b=0.45)

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
    build_niv_005_pdf()
