#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_sesion_04_google_flow.py
Actualización integral de la Sesión 04:
1. Nueva Ficha Oficial INFO-004: Taller Rápido de Google Flow (Estudio de Cine y Vídeo con IA).
2. Ampliación oficial en las 5 fichas de creación visual de la Sesión 04:
   - 2. EST-004 (Campo de Amapolas - Monet)
   - 3. PRAC-004 (Viaje en el Tiempo - Años 60)
   - 5. INT-004 (Corte del Transbordador Espacial)
   - 6. FUT-004 (Año 2035: Terapia Génica Personalizada)
   - 8. ARTE-004 (El Nacimiento de Venus - Botticelli)
3. Reubicación en cadena de infografías:
   - INFO-004 previa -> INFO-005 en Sesión 05
   - INFO-005 previa -> INFO-006 en Sesión 06
"""

import os
import sys
import shutil

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
S04_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion")
S05_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/05_Sesion")
S06_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/06_Sesion")

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

# -------------------------------------------------------------
# 1. GENERADOR DE LA FICHA MAESTRA INFO-004: GOOGLE FLOW
# -------------------------------------------------------------
def build_info_004_pdf(output_path):
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
    pdf.draw_text(36, 750, 'SESION 04 • FICHA DIDACTICA DE INNOVACION [INFO-004]', font='F2', size=8.5, r=0.4, g=0.75, b=1.0)
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
    pdf.draw_text(36, 230, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 04 • CINE Y VIDEO CON IA [INFO-004]', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 218, 'Herramienta Oficial: Google Flow (https://labs.google/flow) • Saldo Diario: 50 Creditos Gratuitos Renovables', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha INFO-004 generada: {output_path}")

# -------------------------------------------------------------
# 2. GENERADOR DE LAS 5 FICHAS CONCRETA CON LA AMPLIACIÓN FLOW
# -------------------------------------------------------------
def build_worksheet_with_flow(output_path, tag_code, num_str, title, desc_concept, prompt_gemini, prompt_flow, theme_color_rgb):
    pdf = NativePDFWriter()
    pdf.start_page()

    r_c, g_c, b_c = theme_color_rgb

    # Fondo y borde exterior
    pdf.set_fill_color(0.98, 0.99, 1.0)
    pdf.set_stroke_color(r_c, g_c, b_c)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal
    pdf.set_fill_color(r_c * 0.4, g_c * 0.4, b_c * 0.4)
    pdf.rect(24, 716, 564, 52, fill=True, stroke=False)
    pdf.draw_text(36, 750, f'SESION 04 • FICHA DIDACTICA DE CREACION CON GEMINI [{tag_code}]', font='F2', size=8.5, r=r_c * 0.8 + 0.2, g=g_c * 0.8 + 0.2, b=b_c * 0.8 + 0.2)
    pdf.draw_text(36, 730, title, font='F2', size=12.2, r=1, g=1, b=1)

    # Seccion 1: Concepto y Objetivo en el Aula
    pdf.set_fill_color(0.94, 0.97, 1.0)
    pdf.set_stroke_color(r_c * 0.7, g_c * 0.7, b_c * 0.7)
    pdf.set_line_width(1.0)
    pdf.rect(30, 615, 552, 90, fill=True, stroke=True)

    pdf.draw_text(42, 690, '1. CONCEPTO Y OBJETIVO EN EL AULA', font='F2', size=9.0, r=0.1, g=0.25, b=0.45)
    lines_desc = wrap_text(desc_concept, 114)
    y_d = 675
    for l in lines_desc:
        pdf.draw_text(42, y_d, l, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
        y_d -= 11

    pdf.draw_text(42, 630, 'METODO DIDACTICO: 1. Pegar prompt en Gemini -> 2. Descargar imagen JPG -> 3. Animar en Google Flow.', font='F2', size=7.6, r=0.1, g=0.45, b=0.65)

    # Seccion 2: Prompt Maestro para Gemini
    pdf.set_fill_color(0.96, 0.98, 1.0)
    pdf.set_stroke_color(r_c * 0.8, g_c * 0.8, b_c * 0.8)
    pdf.set_line_width(1.0)
    pdf.rect(30, 445, 552, 160, fill=True, stroke=True)

    pdf.draw_text(42, 590, '2. PROMPT MAESTRO PARA CREAR LA IMAGEN EN GEMINI (gemini.google.com)', font='F2', size=8.8, r=0.1, g=0.3, b=0.55)
    pdf.draw_text(42, 578, '(Copia todo el texto del recuadro inferior y pegalo directamente en el chat de Gemini)', font='F3', size=7.2, r=0.4, g=0.45, b=0.5)

    # Recuadro interior Gemini
    pdf.set_fill_color(0.90, 0.94, 0.99)
    pdf.set_stroke_color(r_c * 0.9, g_c * 0.9, b_c * 0.9)
    pdf.set_line_width(0.8)
    pdf.rect(40, 455, 532, 115, fill=True, stroke=True)

    lines_pg = wrap_text(prompt_gemini, 108)
    y_pg = 552
    for l in lines_pg:
        pdf.draw_text(48, y_pg, l, font='F1', size=7.3, r=0.08, g=0.15, b=0.3)
        y_pg -= 11

    # Seccion 3: Ampliacion Oficial con Google Flow (10 Puntos)
    pdf.set_fill_color(0.99, 0.97, 0.93)
    pdf.set_stroke_color(0.85, 0.45, 0.1)
    pdf.set_line_width(1.2)
    pdf.rect(30, 235, 552, 200, fill=True, stroke=True)

    pdf.draw_text(42, 420, '3. AMPLIACION: ¡DALE VIDA EN VIDEO CON GOOGLE FLOW! (Gasta 10 de tus 50 puntos diarios)', font='F2', size=8.8, r=0.75, g=0.3, b=0.02)
    
    # Pasos recordatorio
    steps_txt = [
        "1. Descarga la imagen: Haz clic en la imagen generada en Gemini y pulsa en 'Descargar' (la flecha).",
        "2. Entra en Google Flow y arrastra: Abre https://labs.google/flow. En lugar de pulsar en 'Subir imagen', como ya la tienes en la flechita de descargas del navegador, arrastrala directamente a la pantalla de Flow.",
        "3. Pega el prompt de abajo: En el recuadro de texto de Flow, pega el siguiente prompt de movimiento y pulsa 'Generar Video'."
    ]
    y_st = 406
    for st in steps_txt:
        lines_st = wrap_text(st, 114)
        for idx, l in enumerate(lines_st):
            is_bold = (idx == 0 and ('1.' in l or '2.' in l or '3.' in l))
            pdf.draw_text(42, y_st, l, font='F2' if is_bold else 'F1', size=7.2, r=0.25, g=0.2, b=0.15)
            y_st -= 10

    # Recuadro interior Prompt Flow
    pdf.set_fill_color(1.0, 0.95, 0.88)
    pdf.set_stroke_color(0.85, 0.45, 0.1)
    pdf.set_line_width(0.8)
    pdf.rect(40, 245, 532, 95, fill=True, stroke=True)

    pdf.draw_text(48, 325, 'PROMPT EXACTO DE MOVIMIENTO PARA PEGAR EN GOOGLE FLOW (labs.google/flow):', font='F2', size=7.5, r=0.6, g=0.2, b=0.0)
    lines_pf = wrap_text(prompt_flow, 108)
    y_pf = 310
    for l in lines_pf:
        pdf.draw_text(48, y_pf, l, font='F1', size=7.2, r=0.2, g=0.1, b=0.0)
        y_pf -= 11

    pdf.draw_text(48, 252, 'Resultado: En 10 segundos tendras tu escena convertida en un video MP4 listo para compartir en WhatsApp.', font='F3', size=6.8, r=0.45, g=0.3, b=0.1)

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 222, 582, 222)
    pdf.draw_text(36, 208, f'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 04 • {tag_code}', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 196, 'Metodologia Dual: Gemini (Imagen Fija) + Google Flow (Animacion de Video • 10 Creditos)', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha con ampliación Flow generada: {output_path}")

def main():
    print("=== [INICIO ACTUALIZACION SESION 04 CON GOOGLE FLOW] ===")

    # 1. Reubicación de infografías en cadena:
    # INFO-005 en S05 -> INFO-006 en S06
    old_info5_pdf = os.path.join(S05_DIR, "1. INFO-005_El_Plan_Maestro_de_Integracion_Vertical_de_IA.pdf")
    old_info5_jpg = os.path.join(S05_DIR, "1. INFO-005_El_Plan_Maestro_de_Integracion_Vertical_de_IA.jpg")
    new_info6_pdf = os.path.join(S06_DIR, "1. INFO-006_El_Plan_Maestro_de_Integracion_Vertical_de_IA.pdf")
    new_info6_jpg = os.path.join(S06_DIR, "1. INFO-006_El_Plan_Maestro_de_Integracion_Vertical_de_IA.jpg")
    if os.path.exists(old_info5_pdf):
        shutil.copy2(old_info5_pdf, new_info6_pdf)
    if os.path.exists(old_info5_jpg):
        shutil.copy2(old_info5_jpg, new_info6_jpg)
    print("📦 Infografía 'Plan Maestro' movida a Sesión 06 como INFO-006")

    # INFO-004 en S04 -> INFO-005 en S05
    old_info4_pdf = os.path.join(S04_DIR, "1. INFO-004_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.pdf")
    old_info4_jpg = os.path.join(S04_DIR, "1. INFO-004_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.jpg")
    new_info5_pdf = os.path.join(S05_DIR, "1. INFO-005_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.pdf")
    new_info5_jpg = os.path.join(S05_DIR, "1. INFO-005_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.jpg")
    if os.path.exists(old_info4_pdf):
        shutil.copy2(old_info4_pdf, new_info5_pdf)
        os.remove(old_info4_pdf)
    if os.path.exists(old_info4_jpg):
        shutil.copy2(old_info4_jpg, new_info5_jpg)
        os.remove(old_info4_jpg)
    print("📦 Infografía 'La Máquina Más Grande' movida a Sesión 05 como INFO-005")

    # 2. Generar INFO-004: Taller Google Flow en Sesión 04
    info4_dest = os.path.join(S04_DIR, "1. INFO-004_Taller_Google_Flow_Video_con_IA.pdf")
    build_info_004_pdf(info4_dest)

    # 3. Generar las 5 fichas de imagen con ampliación Google Flow
    # 3.1. EST-004
    p_est = os.path.join(S04_DIR, "2. EST-004_IMPRESIONISTA Y POST-IMPRESIONISTA - Campo de Amapolas.pdf")
    build_worksheet_with_flow(
        output_path=p_est,
        tag_code="EST-004",
        num_str="2. EST-004",
        title="Estilo Impresionista y Oleo: Campo de Amapolas (Monet)",
        desc_concept="Pinceladas sueltas, colores vibrantes y enfasis en la luz natural y el aire libre, inspirado en las grandes obras paisajisticas de Claude Monet y el postimpresionismo frances.",
        prompt_gemini="\"Pintura al oleo de un campo de amapolas silvestres bajo un cielo nublado, estilo impresionista similar a Monet, pinceladas sueltas y gruesas, textura de lienzo visible, colores vivos y luz natural al atardecer. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Travelling lateral lento y suave a traves del campo de amapolas. El viento mece suavemente las flores rojas y la hierba silvestre, mientras las nubes se desplazan lentamente en el cielo al atardecer. Estetica de pintura al oleo viva con luz constante.\"",
        theme_color_rgb=(0.3, 0.4, 0.85)
    )

    # 3.2. PRAC-004
    # Detectar nombre exacto de archivo preexistente en S04_DIR
    p_prac = None
    for f in os.listdir(S04_DIR):
        if f.startswith("3. PRAC-004") and f.endswith(".pdf"):
            p_prac = os.path.join(S04_DIR, f)
            break
    if not p_prac:
        p_prac = os.path.join(S04_DIR, "3. PRAC-004_Viaje en el Tiempo_ Volver a la Juventud en los Años 60.pdf")

    build_worksheet_with_flow(
        output_path=p_prac,
        tag_code="PRAC-004",
        num_str="3. PRAC-004",
        title="Viaje en el Tiempo: Volver a la Juventud en los Anos 60 / Epoca Dorada",
        desc_concept="Transportar tu fotografia o recuerdo a la estetica, vestuario y optimismo de los anos 60 o 70, frente a un escenario clasico de epoca y con iluminacion cinematografica calida.",
        prompt_gemini="\"Fotografia realista de epoca en blanco y negro o color calido de los anos 60: retrato sonriente de una persona joven vestida con moda clasica de la decada, en una cafeteria vintage o avenida transitada con coches de la epoca al fondo. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Camara lenta con ligero acercamiento al rostro. La persona parpadea con naturalidad, sonrie calidamente y una brisa ligera mueve su cabello. De fondo, los coches de epoca circulan suavemente y las luces de la calle parpadean tenues.\"",
        theme_color_rgb=(0.85, 0.45, 0.15)
    )

    # 3.3. INT-004
    p_int = None
    for f in os.listdir(S04_DIR):
        if f.startswith("5. INT-004") and f.endswith(".pdf"):
            p_int = os.path.join(S04_DIR, f)
            break
    if not p_int:
        p_int = os.path.join(S04_DIR, "5. INT-004_Corte del Transbordador Espacial en Orbita.pdf")

    build_worksheet_with_flow(
        output_path=p_int,
        tag_code="INT-004",
        num_str="5. INT-004",
        title="Corte del Transbordador Espacial en Orbita con Bodega Abierta y Brazo Canadarm",
        desc_concept="La iconica nave reutilizable de la NASA por dentro: cabina de dos cubiertas para astronautas, bodega de carga y el brazo mecanico Canadarm desplegado sobre la curvatura de la Tierra.",
        prompt_gemini="\"Infografia y corte transversal 3D de un Transbordador Espacial de la NASA orbitando la Tierra: bodega de carga abierta con un satelite de comunicaciones desplegado por el brazo Canadarm. Fondo de la curvatura azul de la Tierra y estrellas brillantes. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Plano orbital cinematico alejandose suavemente del transbordador espacial. El brazo Canadarm sostiene el satelite en gravedad cero mientras la Tierra gira majestuosamente y en silencio en el horizonte azul.\"",
        theme_color_rgb=(0.1, 0.55, 0.65)
    )

    # 3.4. FUT-004
    p_fut = None
    for f in os.listdir(S04_DIR):
        if f.startswith("6. FUT-004") and f.endswith(".pdf"):
            p_fut = os.path.join(S04_DIR, f)
            break
    if not p_fut:
        p_fut = os.path.join(S04_DIR, "6. FUT-004_Ano 2035_ Terapia Genica Personalizada.pdf")

    build_worksheet_with_flow(
        output_path=p_fut,
        tag_code="FUT-004",
        num_str="6. FUT-004",
        title="Ano 2035: Terapia Genica Personalizada y Medicina Molecular de Precision",
        desc_concept="La era de la medicina molecular de precision: nanosensores inteligentes y terapias celulares que detectan anomalias a nivel sanguineo y de ADN antes de que aparezcan sintomas clinicos.",
        prompt_gemini="\"Infografia biomedica 3D cientifica y esperanzadora sobre la medicina del ano 2035: celula humana iluminada donde hebras de ADN son reparadas por nanosensores microscopicos luminosos que liberan terapia genica de precision. Fondo azul medico de alta tecnologia. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Camara lenta microscopica navegando por el espacio celular. Las hebras de ADN brillan con pulsos suaves de luz dorada y los nanosensores se desplazan con movimiento suave y constante en un entorno biomedico de alta definicion.\"",
        theme_color_rgb=(0.15, 0.6, 0.4)
    )

    # 3.5. ARTE-004
    p_arte = None
    for f in os.listdir(S04_DIR):
        if f.startswith("8. ARTE-004") and f.endswith(".pdf"):
            p_arte = os.path.join(S04_DIR, f)
            break
    if not p_arte:
        p_arte = os.path.join(S04_DIR, "8. ARTE-004_El Nacimiento de Venus de Sandro Botticelli.pdf")

    build_worksheet_with_flow(
        output_path=p_arte,
        tag_code="ARTE-004",
        num_str="8. ARTE-004",
        title="El Nacimiento de Venus de Sandro Botticelli (1485)",
        desc_concept="La obra cumbre del Renacimiento florentino en la Galeria Uffizi: la diosa del amor y la belleza emerge de las aguas sobre una concha gigante impulsada por el viento divino de los cefiros.",
        prompt_gemini="\"Ilustracion clasica y recreacion pictorica luminosa del Nacimiento de Venus de Botticelli: Venus de pie sobre una gran concha marina dorada sobre el mar turquesa, el dios Cefiro soplando rosas flotantes y la ninfa Primavera ofreciendo un manto floreado. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Giro de camara lento en semi-arco alrededor de la escena. Las olas del mar ondean suavemente con espuma blanca, las rosas flotan y giran mecidas por el viento divino y el manto purpura ondea con elegancia renacentista.\"",
        theme_color_rgb=(0.6, 0.3, 0.7)
    )

    print("\n✨ Todas las fichas de Sesión 04 han sido generadas con la ampliación oficial de Google Flow.")

if __name__ == '__main__':
    main()
