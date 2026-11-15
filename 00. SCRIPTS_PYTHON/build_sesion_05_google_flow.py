#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_sesion_05_google_flow.py
Genera la Ficha Didáctica Oficial INFO-005:
1. INFO-005_Taller_Google_Flow_Video_con_IA.pdf
en la Sesión 05 del Curso de IA.
"""

import os
import sys

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
S05_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/05_Sesion")
PDF_PATH = os.path.join(S05_DIR, "1. INFO-005_Taller_Google_Flow_Video_con_IA.pdf")

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

def build_info_005_pdf(output_path=PDF_PATH):
    pdf = NativePDFWriter()
    pdf.start_page()

    # Fondo y borde exterior
    pdf.set_fill_color(0.98, 0.99, 1.0)
    pdf.set_stroke_color(0.15, 0.45, 0.85)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera
    pdf.set_fill_color(0.08, 0.18, 0.35)
    pdf.rect(24, 716, 564, 52, fill=True, stroke=False)
    pdf.draw_text(36, 750, 'SESION 05 • FICHA DIDACTICA DE INNOVACION [INFO-005]', font='F2', size=8.5, r=0.4, g=0.75, b=1.0)
    pdf.draw_text(36, 730, 'Google Flow: El Estudio de Cine y Video con IA (Veo & Gemini)', font='F2', size=13.0, r=1, g=1, b=1)

    # Seccion 1: Que es y los 50 puntos diarios
    pdf.set_fill_color(0.93, 0.96, 1.0)
    pdf.set_stroke_color(0.2, 0.5, 0.85)
    pdf.set_line_width(1.0)
    pdf.rect(30, 595, 552, 110, fill=True, stroke=True)

    pdf.draw_text(42, 690, '1. ¿QUE ES GOOGLE FLOW Y POR QUE ES IDEAL PARA NOSOTROS?', font='F2', size=9.2, r=0.08, g=0.25, b=0.55)
    t1 = "Google Flow es el nuevo espacio creativo de Google para generar y animar video cinematografico mediante sus modelos mas avanzados (Google Veo y Gemini Omni). Permite dar movimiento suave y realista a cualquier fotografia o escena a partir de instrucciones en espanol."
    for idx, l in enumerate(wrap_text(t1, 112)):
        pdf.draw_text(42, 675 - (idx * 11), l, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    pdf.draw_text(42, 642, 'LA GRAN VENTAJA SENIOR: 50 PUNTOS DIARIOS GRATUITOS (CERO TARJETAS)', font='F2', size=8.2, r=0.8, g=0.3, b=0.05)
    t2 = "• Entras directamente con tu cuenta habitual de Google (la misma de Gmail). Sin suscripciones ni registrar tarjetas.\n• Todos los dias a las 00:00 se renuevan 50 creditos gratuitos en tu marcador. Cada video de 5 segundos cuesta 10 creditos.\n• Tienes margen para crear hasta 5 clips de video diarios sin pagar nada. Si un dia no te gusta el resultado, manana tienes 50 puntos nuevos."
    y_pos = 629
    for par in t2.split('\n'):
        pdf.draw_text(42, y_pos, par, font='F1', size=7.5, r=0.15, g=0.2, b=0.25)
        y_pos -= 11

    # Seccion 2: Como acceder y los 3 pasos
    pdf.set_fill_color(0.96, 0.98, 1.0)
    pdf.set_stroke_color(0.15, 0.45, 0.8)
    pdf.set_line_width(1.0)
    pdf.rect(30, 440, 552, 145, fill=True, stroke=True)

    pdf.draw_text(42, 568, '2. DIRECCION WEB OFICIAL Y LOS 3 PASOS PARA ANIMAR TUS IMAGENES', font='F2', size=9.2, r=0.08, g=0.25, b=0.55)
    
    # Recuadro URL destacada
    pdf.set_fill_color(0.12, 0.25, 0.45)
    pdf.rect(42, 538, 528, 22, fill=True, stroke=False)
    pdf.draw_text(52, 545, 'PLATAFORMA OFICIAL: https://labs.google/flow  (o busca "Google Flow" en tu navegador)', font='F2', size=8.2, r=1, g=1, b=1)

    steps = [
        ("PASO 1 • Iniciar Sesion:", "Abre https://labs.google/flow y pulsa en 'Sign In' (Iniciar sesion) con tu cuenta de Google normal. Comprueba arriba a la derecha que tu saldo marca 50 creditos."),
        ("PASO 2 • Subir tu Imagen:", "Descarga en tu ordenador o tablet la imagen que has generado en Gemini (en las fichas [EST], [PRAC], [INT], [FUT] o [ARTE]). En Google Flow, arrastra el archivo o pulsa 'Subir Imagen'."),
        ("PASO 3 • Copiar el Prompt y Crear:", "Pega el prompt de movimiento que te dejamos preparado en la ficha y pulsa 'Generar Video'. En unos 10 segundos tendras tu clip en movimiento listo para descargar en MP4 y enviarlo a tu familia por WhatsApp.")
    ]
    y_s = 520
    for st_title, st_desc in steps:
        pdf.draw_text(42, y_s, st_title, font='F2', size=7.8, r=0.1, g=0.35, b=0.65)
        y_s -= 10
        lines = wrap_text(st_desc, 114)
        for l in lines:
            pdf.draw_text(42, y_s, l, font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
            y_s -= 10
        y_s -= 3

    # Seccion 3: La formula del prompt de video
    pdf.set_fill_color(0.99, 0.98, 0.95)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 260, 552, 170, fill=True, stroke=True)

    pdf.draw_text(42, 415, '3. LA FORMULA DE ORO PARA EL PROMPT DE VIDEO EN GOOGLE FLOW', font='F2', size=9.0, r=0.7, g=0.35, b=0.05)
    
    rule_intro = "Google Flow no lee historias largas ni dialogos: interpreta movimiento fisico de camara y ambiente. La formula magica para conseguir resultados perfectos al primer intento es combinar siempre estos 4 ingredientes:"
    for idx, l in enumerate(wrap_text(rule_intro, 114)):
        pdf.draw_text(42, 400 - (idx * 11), l, font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    # Recuadro interior de la formula
    pdf.set_fill_color(1.0, 0.96, 0.90)
    pdf.set_stroke_color(0.85, 0.55, 0.15)
    pdf.set_line_width(0.8)
    pdf.rect(40, 295, 532, 85, fill=True, stroke=True)

    formula_items = [
        "1. Sujeto Principal: 'Retrato de la dama', 'El barco de vapor', 'El faro de piedra sobre el acantilado'.",
        "2. Movimiento Sutil: 'Parpadeo suave y respiracion natural', 'Olas rompiendo con espuma', 'Humo subiendo en espiral'.",
        "3. Movimiento de Camara: 'Camara lenta acercandose suavemente (zoom in)', 'Travelling lateral lento', 'Giro orbital 45 grados'.",
        "4. Ambiente e Iluminacion: 'Luz dorada de atardecer constante', 'Reflejos brillantes', 'Estetica cinematografica impecable'."
    ]
    y_f = 365
    for fi in formula_items:
        pdf.draw_text(48, y_f, fi, font='F2' if '1.' in fi or '2.' in fi or '3.' in fi or '4.' in fi else 'F1', size=7.2, r=0.2, g=0.15, b=0.05)
        y_f -= 16

    pdf.draw_text(42, 278, "CONSEJO SENIOR: Evita pedir carreras o giros bruscos. La IA destaca y emociona con movimientos suaves y serenos.", font='F2', size=7.2, r=0.65, g=0.25, b=0.05)

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 245, 582, 245)
    pdf.draw_text(36, 230, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 05 • CINE Y VIDEO CON IA [INFO-005]', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 218, 'Herramienta Oficial: Google Flow (https://labs.google/flow) • Saldo Diario: 50 Creditos Gratuitos Renovables', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha INFO-005 generada: {output_path}")

if __name__ == '__main__':
    build_info_005_pdf()
