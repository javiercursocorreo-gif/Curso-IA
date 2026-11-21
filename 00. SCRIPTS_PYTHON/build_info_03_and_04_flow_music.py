#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_info_03_and_04_flow_music.py
1. Genera Ficha Oficial INFO-003B: Taller Google Flow y los 4 Movimientos Cinemáticos de Cámara (Sesión 03).
2. Actualiza las 5 fichas de imagen de la Sesión 03 con Google Flow (Orbit, Zoom in, Drone View x2, Bullet Time).
3. Genera Ficha Oficial INFO-004B: Taller Google Music AI (Banda Sonora, Tarareo y De Foto a Música) (Sesión 04).
4. Actualiza mapas interactivos de Sesión 03 y Sesión 04.
5. Sincroniza con el Bloque 15 de Infografías y Novedades IA.
"""

import os
import sys
import shutil

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
S03_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/03_Sesion")
S04_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion")
BLOQUE_15_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/15. [INFO] BLOQUE_15_INFOGRAFIAS_Y_NOVEDADES_IA/Lote_01_al_20")

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
                f.write(f'{i} 0 obj\n'.encode('ascii') + obj + b'\nendobj\n')

            startxref = f.tell()
            f.write(f'xref\n0 {len(all_objs) + 1}\n0000000000 65535 f \n'.encode('ascii'))
            for off in offsets:
                f.write(f'{off:010d} 00000 n \n'.encode('ascii'))

            trailer = f'trailer\n<< /Size {len(all_objs) + 1} /Root 1 0 R >>\nstartxref\n{startxref}\n%%EOF\n'.encode('ascii')
            f.write(trailer)

# ==============================================================================
# 1. FICHA INFO-003B: TALLER GOOGLE FLOW Y CÁMARA CINEMÁTICA (SESIÓN 03)
# ==============================================================================
def build_info_003b_pdf(output_path):
    pdf = NativePDFWriter(page_width=612.0, page_height=792.0)
    pdf.start_page()

    # Marco exterior elegante
    pdf.set_fill_color(0.99, 0.99, 1.0)
    pdf.set_stroke_color(0.85, 0.25, 0.2)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal
    pdf.set_fill_color(0.82, 0.18, 0.15)
    pdf.rect(24, 714, 564, 54, fill=True, stroke=False)
    pdf.draw_text(36, 750, 'SESION 03 • NOVEDADES Y TALLER TECNOLOGICO IA [INFO-003B]', font='F2', size=8.5, r=1, g=1, b=1)
    pdf.draw_text(36, 730, 'Taller Oficial: Google Flow y los 4 Movimientos Cinemáticos de Cámara', font='F2', size=11.5, r=1, g=1, b=1)

    # Sección 1: Qué es Flow y los 50 créditos
    pdf.set_fill_color(1.0, 1.0, 1.0) # Fondo blanco para impresión limpia
    pdf.set_stroke_color(0.85, 0.25, 0.2)
    pdf.set_line_width(1.0)
    pdf.rect(30, 600, 552, 105, fill=True, stroke=True)

    pdf.draw_text(42, 688, '1. EL ESTUDIO DE CINE DE GOOGLE: 50 CREDITOS DIARIOS GRATUITOS', font='F2', size=9.2, r=0.75, g=0.15, b=0.1)
    
    t1 = (
        "Google Flow (https://labs.google/flow) es la herramienta de Google que transforma cualquier imagen "
        "creada en Gemini en un clip de cine en movimiento de 5 segundos con fisica realista y camara profesional.\n"
        "• Acceso directo con tu cuenta de Google (Gmail): Sin pagos, sin suscripciones y sin tarjetas de credito.\n"
        "• 50 Creditos diarios renovables a las 00:00: Cada clip de 5 segundos consume 10 creditos (hasta 5 videos gratis diarios).\n"
        "• Flujo en 3 pasos: 1) Descargar en Gemini. 2) Arrastrar desde descargas a Flow. 3) Pegar el prompt y pulsar 'Generar Video'."
    )
    y_pos = 672
    for par in t1.split('\n'):
        lines = wrap_text(par, 114)
        for l in lines:
            pdf.draw_text(42, y_pos, l, font='F2' if '•' in l and ':' in l else 'F1', size=7.4, r=0.15, g=0.2, b=0.25)
            y_pos -= 11.2

    # Sección 2: Los 4 Movimientos de Cámara Cinemática Avanzada
    pdf.set_fill_color(1.0, 1.0, 1.0) # Fondo blanco
    pdf.set_stroke_color(0.2, 0.45, 0.8)
    pdf.set_line_width(1.0)
    pdf.rect(30, 265, 552, 325, fill=True, stroke=True)

    pdf.draw_text(42, 574, '2. LOS 4 MOVIMIENTOS CINEMATICOS DE CAMARA PROFESIONAL (ANALISIS DE DIRECCION)', font='F2', size=9.2, r=0.1, g=0.3, b=0.65)
    pdf.draw_text(42, 561, 'Aprende a dirigir la camara virtual con las tecnicas maestras de realizacion cinematografica:', font='F3', size=7.2, r=0.4, g=0.45, b=0.5)

    moves = [
        ("1. ORBIT (Giro 360 Grados Orbital):",
         "La camara rota circularmente alrededor del sujeto principal manteniendolo siempre en el centro del encuadre. "
         "Aporta volumen y tridimensionalidad majestuosa. Ideal para estatuas, bodegones, mesas de trabajo o edificios.",
         "Ejemplo de Prompt: \"Camara orbital lenta girando 360 grados alrededor del sujeto con iluminacion calida cinematica.\""),

        ("2. DRONE VIEW (Vuelo Aereo / Perspectiva Cenital):",
         "La camara sobrevuela como un dron desde gran altura, ascendiendo o descendiendo en linea recta para mostrar grandes paisajes, "
         "vistas aereas de ciudades o patios arquitectonicos. Proporciona escala colosal y sensacion de vuelo sereno.",
         "Ejemplo de Prompt: \"Plano aereo con dron ascendiendo suavemente para desvelar la escena principal a camara lenta.\""),

        ("3. BULLET TIME (Tiempo Congelado / Camara Ultralenta):",
         "El tiempo se detiene casi por completo mientras la camara se aproxima con suavidad milimetrica al foco de tension dramatica. "
         "Perfecto para chispas de luz, gotas suspendidas o el instante en que dos manos casi se tocan en obras renacentistas.",
         "Ejemplo de Prompt: \"Efecto camara ultralenta (bullet time) acercandose al punto exacto con luz constante y suave.\""),

        ("4. REVEAL (Camara de Revelacion Progresiva):",
         "La camara emerge desde el suelo, desde detras de una pared o asciende tras un obstaculo para descubrir el sujeto principal. "
         "Crea suspense, emocion visual y un impacto dramatico perfecto al desvelar rostros restaurados o tesoros ocultos.",
         "Ejemplo de Prompt: \"Camara lenta de revelacion ascendiendo desde el suelo para descubrir la mirada del personaje.\"")
    ]

    y_m = 544
    for m_title, m_desc, m_ex in moves:
        pdf.draw_text(42, y_m, m_title, font='F2', size=7.8, r=0.1, g=0.35, b=0.65)
        y_m -= 10
        for l in wrap_text(m_desc, 115):
            pdf.draw_text(42, y_m, l, font='F1', size=7.2, r=0.2, g=0.25, b=0.3)
            y_m -= 9.5
        for l in wrap_text(m_ex, 115):
            pdf.draw_text(42, y_m, l, font='F3', size=6.8, r=0.7, g=0.3, b=0.05)
            y_m -= 9.5
        y_m -= 5

    # Sección 3: Consejos prácticos de rodaje senior
    pdf.set_fill_color(1.0, 1.0, 1.0)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 95, 552, 160, fill=True, stroke=True)

    pdf.draw_text(42, 238, '3. CONSEJO SENIOR: LA REGLA DE ORO DEL RODAJE DIGITAL CON IA', font='F2', size=9.0, r=0.7, g=0.35, b=0.05)
    
    tips = (
        "• Menos es mas: Evita pedir carreras rapidas o acrobacias complejas. La IA destaca con movimientos suaves, lentos y serenos.\n"
        "• Luz constante: Incluye siempre en tu prompt palabras como 'luz calida constante' o 'reflejos suaves' para evitar parpadeos.\n"
        "• Integracion en tus 5 fichas: En esta sesion 03, hemos anadido al pie de tus 5 fichas de imagen ([EST], [PRAC], [INT], [FUT], [ARTE]) "
        "el prompt exacto de Flow para aplicar cada uno de estos movimientos sin que tengas que inventar nada."
    )
    y_t = 222
    for par in tips.split('\n'):
        for l in wrap_text(par, 114):
            pdf.draw_text(42, y_t, l, font='F1', size=7.4, r=0.2, g=0.25, b=0.3)
            y_t -= 10.5

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 85, 582, 85)
    pdf.draw_text(36, 72, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 03 • TALLER GOOGLE FLOW [INFO-003B]', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 60, 'Herramienta: Google Flow (https://labs.google/flow) • 50 Creditos Diarios Gratuitos • Cine con IA', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha INFO-003B generada con éxito: {output_path}")

# ==============================================================================
# 2. ACTUALIZACIÓN DE LAS 5 FICHAS DE IMAGEN EN SESIÓN 03
# ==============================================================================
def build_worksheet_with_flow(
    output_path,
    tag_code,
    num_str,
    title,
    desc_concept,
    prompt_gemini,
    prompt_flow,
    theme_color_rgb=(0.15, 0.45, 0.75)
):
    pdf = NativePDFWriter(page_width=612.0, page_height=792.0)
    pdf.start_page()

    # Marco exterior elegante
    pdf.set_fill_color(0.99, 0.99, 1.0)
    pdf.set_stroke_color(theme_color_rgb[0], theme_color_rgb[1], theme_color_rgb[2])
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal institucional
    pdf.set_fill_color(theme_color_rgb[0] * 0.3, theme_color_rgb[1] * 0.3, theme_color_rgb[2] * 0.3)
    pdf.rect(24, 714, 564, 54, fill=True, stroke=False)

    pdf.draw_text(36, 750, f'SESION 03 • FICHA DE GENERACION VISUAL + AMPLIACION A VIDEO [{tag_code}]', font='F2', size=8.5, r=0.85, g=0.92, b=1.0)
    pdf.draw_text(36, 730, f'{num_str}: {title}', font='F2', size=11.5, r=1, g=1, b=1)

    # Sección 1: Concepto y Objetivo Visual
    pdf.set_fill_color(1.0, 1.0, 1.0) # Fondo blanco para imprimir
    pdf.set_stroke_color(theme_color_rgb[0], theme_color_rgb[1], theme_color_rgb[2])
    pdf.set_line_width(1.0)
    pdf.rect(30, 615, 552, 90, fill=True, stroke=True)

    pdf.draw_text(42, 690, '1. CONCEPTO Y OBJETIVO VISUAL:', font='F2', size=9.0, r=0.08, g=0.25, b=0.55)
    lines_desc = wrap_text(desc_concept, 114)
    y_dc = 674
    for l in lines_desc:
        pdf.draw_text(42, y_dc, l, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
        y_dc -= 11.5

    # Sección 2: Prompt Maestro para Gemini (Imagen Fija)
    pdf.set_fill_color(1.0, 1.0, 1.0) # Fondo blanco
    pdf.set_stroke_color(0.2, 0.55, 0.85)
    pdf.set_line_width(1.0)
    pdf.rect(30, 445, 552, 160, fill=True, stroke=True)

    pdf.draw_text(42, 590, '2. PROMPT MAESTRO PARA GEMINI (IMAGEN FIJA DE ALTA DEFINICION):', font='F2', size=9.0, r=0.05, g=0.3, b=0.6)
    pdf.draw_text(42, 577, '(Copia este texto y pegalo en gemini.google.com para generar la imagen base de partida)', font='F3', size=7.2, r=0.4, g=0.45, b=0.5)

    # Recuadro interior Prompt Gemini
    pdf.set_fill_color(1.0, 1.0, 1.0)
    pdf.set_stroke_color(0.25, 0.6, 0.9)
    pdf.set_line_width(0.8)
    pdf.rect(40, 455, 532, 115, fill=True, stroke=True)

    lines_pg = wrap_text(prompt_gemini, 108)
    y_pg = 552
    for l in lines_pg:
        pdf.draw_text(48, y_pg, l, font='F1', size=7.3, r=0.08, g=0.15, b=0.3)
        y_pg -= 11

    # Sección 3: Ampliación Oficial con Google Flow (10 Créditos)
    pdf.set_fill_color(1.0, 1.0, 1.0) # Fondo blanco
    pdf.set_stroke_color(0.85, 0.45, 0.1)
    pdf.set_line_width(1.2)
    pdf.rect(30, 235, 552, 200, fill=True, stroke=True)

    pdf.draw_text(42, 420, '3. AMPLIACION: ¡DALE VIDA EN VIDEO CON GOOGLE FLOW! (Gasta 10 de tus 50 puntos diarios)', font='F2', size=8.8, r=0.75, g=0.3, b=0.02)
    
    steps_txt = [
        "1. Descarga la imagen: Haz clic en la imagen generada en Gemini y pulsa en 'Descargar' (la flecha).",
        "2. Entra en Google Flow y arrastra: Abre https://labs.google/flow. En lugar de pulsar en 'Subir imagen', como ya la tienes en la flechita de descargas del navegador, arrastrala directamente a la pantalla de Flow.",
        "3. Pega el prompt de abajo: En el recuadro de texto de Flow, pega el siguiente prompt de camara y pulsa 'Generar Video'."
    ]
    y_st = 406
    for st in steps_txt:
        lines_st = wrap_text(st, 114)
        for idx, l in enumerate(lines_st):
            is_bold = (idx == 0 and ('1.' in l or '2.' in l or '3.' in l))
            pdf.draw_text(42, y_st, l, font='F2' if is_bold else 'F1', size=7.2, r=0.25, g=0.2, b=0.15)
            y_st -= 10

    # Recuadro interior Prompt Flow
    pdf.set_fill_color(1.0, 1.0, 1.0)
    pdf.set_stroke_color(0.85, 0.45, 0.1)
    pdf.set_line_width(0.8)
    pdf.rect(40, 245, 532, 95, fill=True, stroke=True)

    pdf.draw_text(48, 325, 'PROMPT EXACTO DE MOVIMIENTO DE CAMARA PARA GOOGLE FLOW (labs.google/flow):', font='F2', size=7.5, r=0.6, g=0.2, b=0.0)
    lines_pf = wrap_text(prompt_flow, 108)
    y_pf = 310
    for l in lines_pf:
        pdf.draw_text(48, y_pf, l, font='F1', size=7.2, r=0.2, g=0.1, b=0.0)
        y_pf -= 11

    pdf.draw_text(48, 252, 'Resultado: En 10 segundos tendras tu escena convertida en un video MP4 listo para compartir en WhatsApp.', font='F3', size=6.8, r=0.45, g=0.3, b=0.1)

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 222, 582, 222)
    pdf.draw_text(36, 208, f'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 03 • {tag_code}', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 196, 'Metodologia Dual: Gemini (Imagen Fija) + Google Flow (Animacion de Camara • 10 Creditos)', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha con ampliación Flow generada: {output_path}")

def update_all_s03_image_fiches():
    print("=== [ACTUALIZANDO 5 FICHAS DE IMAGEN DE SESIÓN 03 CON GOOGLE FLOW] ===")

    # 1. EST-003: Cervantes y Shakespeare (Orbit 360)
    p_est = os.path.join(S03_DIR, "2. EST-003_REALISTA (FOTORREALISMO) - Cervantes y Shakespeare en el Siglo de.pdf")
    build_worksheet_with_flow(
        output_path=p_est,
        tag_code="EST-003",
        num_str="2. EST-003",
        title="Realista: Cervantes y Shakespeare en el Siglo de Oro",
        desc_concept="Encuentro historico e imaginario entre los dos maximos genios de las letras universales en una biblioteca del siglo XVI: manuscritos con pluma, libros encuadernados en cuero, luz calida de velas y conversacion serena.",
        prompt_gemini="\"Retrato fotorrealista 8K de Miguel de Cervantes y William Shakespeare conversando en una biblioteca del siglo XVI con pergaminos, iluminacion de plumas y velas, trajes de epoca nitidos sobre mesa de madera rustica. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Camara orbital lenta girando 360 grados alrededor de la mesa de madera (Orbit). La llama de las velas parpadea suavemente, el humo asciende en espiral y la luz calida ilumina los rostros serenos y concentrados de Cervantes y Shakespeare en ambiente constante.\"",
        theme_color_rgb=(0.3, 0.4, 0.85)
    )

    # 2. PRAC-003: Restauración y coloreado de fotos antiguas (Zoom in / Reveal)
    p_prac = os.path.join(S03_DIR, "3. PRAC-003_Restauración y coloreado de fotos antiguas.pdf")
    build_worksheet_with_flow(
        output_path=p_prac,
        tag_code="PRAC-003",
        num_str="3. PRAC-003",
        title="Restauracion y Coloreado de Fotos Antiguas",
        desc_concept="Recuperar fotografias familiares en blanco y negro o sepia deterioradas por el tiempo, devolviendoles nitidez, textura natural de piel, color vivo de epoca y emocion a traves de la restauracion digital con IA.",
        prompt_gemini="\"Fotografia realista y restaurada de una pareja joven en los anos 40 sonriendo con elegancia, vestuario de epoca impecable, piel natural con textura calida y suave luz de atardecer, alta definicion 8K. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Camara lenta con acercamiento suave (zoom in y reveal) hacia las miradas de la pareja. Parpadeo sutil y natural, ligera sonrisa que se ilumina con calidez y una suave brisa que mueve ligeramente el cabello en una atmosfera nostalgica y serena.\"",
        theme_color_rgb=(0.85, 0.45, 0.15)
    )

    # 3. INT-003: Hormiguero subterráneo por dentro (Drone View descendente)
    p_int = os.path.join(S03_DIR, "5. INT-003_El interior de un hormiguero subterráneo por dentro_ cámaras, rei.pdf")
    build_worksheet_with_flow(
        output_path=p_int,
        tag_code="INT-003",
        num_str="5. INT-003",
        title="El Interior de un Hormiguero Subterraneo por Dentro: Camaras, Reina y Tuneles",
        desc_concept="La asombrosa arquitectura social y biologica de las hormigas bajo tierra: camaras de cria, despensas de semillas, granjas de hongos y chimeneas de ventilacion vertical en corte longitudinal.",
        prompt_gemini="\"Infografia biologica en corte longitudinal 3D de un gran hormiguero subterraneo bajo el cesped de un bosque, mostrando en seccion transversal la compleja red de tuneles y camaras, revelando la camara real con la hormiga reina y las salas de cultivo de hongos iluminadas con detalle. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Vuelo de camara microscopica descendiendo suavemente (Drone View) por el tunel vertical principal hacia el interior de las camaras subterraneas. Las hormigas obreras se desplazan con actividad ordenada y la luz filtrada revela la textura terrosa y humeda de la colonia.\"",
        theme_color_rgb=(0.1, 0.55, 0.65)
    )

    # 4. FUT-003: Agricultura vertical urbana (Drone View ascendente)
    p_fut = os.path.join(S03_DIR, "6. FUT-003_Año 2033_ Agricultura vertical urbana e invernaderos hidropónicos.pdf")
    build_worksheet_with_flow(
        output_path=p_fut,
        tag_code="FUT-003",
        num_str="6. FUT-003",
        title="Ano 2033: Agricultura Vertical Urbana e Invernaderos Hidroponicos en Rascacielos",
        desc_concept="Como las ciudades del futuro producen vegetales frescos dentro de torres acristaladas de 30 plantas con iluminacion LED eficiente, cultivos sin tierra (hidroponia) y ahorro del 95% de agua dulce.",
        prompt_gemini="\"Infografia arquitectonica en corte 3D de un rascacielos invernadero vertical en el centro de una gran capital en el ano 2033, mostrando por dentro 20 plantas transparentes con bandejas hidroponicas de hortalizas bajo luz LED rosa y pequenos drones cosechadores. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Plano aereo con dron ascendiendo suavemente (Drone View) por la fachada de cristal del rascacielos agricola. A traves de las cristaleras se aprecian las hileras verdes de cultivo hidroponico iluminadas por luces LED, mientras el dron de recoleccion vuela en trayectoria suave.\"",
        theme_color_rgb=(0.15, 0.6, 0.4)
    )

    # 5. ARTE-003: La Creación de Adán (Bullet Time)
    p_arte = os.path.join(S03_DIR, "8. ARTE-003_La Creación de Adán de Miguel Ángel Buonarroti (1512).pdf")
    build_worksheet_with_flow(
        output_path=p_arte,
        tag_code="ARTE-003",
        num_str="8. ARTE-003",
        title="La Creacion de Adan de Miguel Angel Buonarroti (1512)",
        desc_concept="El fresco cumbre de la Boveda de la Capilla Sixtina donde el dedo de Dios infunde la chispa de la vida y el intelecto humano al dedo extendido de Adan en el momento de maxima tension cosmica.",
        prompt_gemini="\"Fotografia artistica de detalle ultra nitido inspirada en La Creacion de Adan de Miguel Angel en la Capilla Sixtina, centrada en el momento de maxima tension donde la mano del Creador se acerca a milimetros del dedo indice de Adan con luz divina radiante. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Efecto camara ultralenta (Bullet Time) acercandose al punto exacto donde los dos dedos casi se tocan. Rayos dorados de luz divina pulsan sutilmente en el vacio microscopico, con el manto celestial ondeando en una suspension temporal majestuosa.\"",
        theme_color_rgb=(0.6, 0.3, 0.7)
    )

# ==============================================================================
# 3. FICHA INFO-004B: TALLER GOOGLE MUSIC AI (SESIÓN 04)
# ==============================================================================
def build_info_004b_pdf(output_path):
    pdf = NativePDFWriter(page_width=612.0, page_height=792.0)
    pdf.start_page()

    # Marco exterior elegante
    pdf.set_fill_color(0.99, 1.0, 0.99)
    pdf.set_stroke_color(0.1, 0.6, 0.35)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal institucional
    pdf.set_fill_color(0.08, 0.45, 0.28)
    pdf.rect(24, 714, 564, 54, fill=True, stroke=False)
    pdf.draw_text(36, 750, 'SESION 04 • NOVEDADES Y TALLER TECNOLOGICO IA [INFO-004B]', font='F2', size=8.5, r=1, g=1, b=1)
    pdf.draw_text(36, 730, 'Taller Oficial: Google Music AI (Banda Sonora, Tarareo y De Foto a Música)', font='F2', size=11.5, r=1, g=1, b=1)

    # Sección 1: Qué es Google Music AI y por qué emociona a los seniors
    pdf.set_fill_color(1.0, 1.0, 1.0) # Fondo blanco
    pdf.set_stroke_color(0.1, 0.6, 0.35)
    pdf.set_line_width(1.0)
    pdf.rect(30, 585, 552, 115, fill=True, stroke=True)

    pdf.draw_text(42, 684, '1. LA REVOLUCION DE LA MUSICA CON IA: EMOCION Y BANDAS SONORAS EN SEGUNDOS', font='F2', size=9.2, r=0.08, g=0.45, b=0.25)
    
    t1 = (
        "Google Music AI (tecnologia Lyria integrada en el ecosistema de Google Flow) permite crear musica original y bandas sonoras "
        "de alta calidad en pocos segundos sin necesidad de saber solfeo ni tocar ningun instrumento tradicional.\n"
        "• Duracion al segundo exacto: Puedes pedirle que componga exactamente 5 segundos de musica para sincronizar con tu video de Flow.\n"
        "• Image-to-Music (De Imagen a Musica): Sube una fotografia y la IA analiza la luz, el color y la epoca para componer la banda sonora.\n"
        "• Audio-to-Music (El Milagro del Tarareo): Tarareas unos segundos con tu voz al microfono y la IA lo convierte en una orquesta o piano."
    )
    y_pos = 668
    for par in t1.split('\n'):
        for l in wrap_text(par, 114):
            pdf.draw_text(42, y_pos, l, font='F2' if '•' in l and ':' in l else 'F1', size=7.5, r=0.15, g=0.25, b=0.2)
            y_pos -= 11.5

    # Sección 2: Los 3 Ejercicios Prácticos Modelo
    pdf.set_fill_color(1.0, 1.0, 1.0) # Fondo blanco
    pdf.set_stroke_color(0.2, 0.45, 0.8)
    pdf.set_line_width(1.0)
    pdf.rect(30, 275, 552, 300, fill=True, stroke=True)

    pdf.draw_text(42, 560, '2. LOS 3 EJERCICIOS PRACTICOS DE AULA: APRENDE PASO A PASO', font='F2', size=9.2, r=0.1, g=0.3, b=0.65)
    pdf.draw_text(42, 547, 'Practicas guiadas disenadas para despertar la creatividad musical y los recuerdos familiares:', font='F3', size=7.2, r=0.4, g=0.45, b=0.5)

    exercises = [
        ("EJERCICIO 1 • EL MILAGRO DEL TARAREO (DEL MICROFONO A LA CANCION):",
         "1. Pulsa el icono del microfono en Google Music AI y tararea 4 notas sencillas con tu propia voz ('na, na, na...').\n"
         "2. Elige el estilo deseado escribiendo en el recuadro de texto.\n"
         "3. Prompt Maestro de Estilo: \"Transforma este tarareo en una balada acustica suave con piano de cola clasico, cuarteto de cuerdas calido y tempo lento y sereno. Duracion exacta: 15 segundos.\"\n"
         "Resultado: Tu tarareo casero se transforma en una pieza de estudio digna de una pelicula clasica."),

        ("EJERCICIO 2 • DE LA FOTO DE PAISAJE A LA SUITE ORQUESTAL (IMAGE-TO-MUSIC):",
         "1. Descarga una imagen de naturaleza creada en Gemini (un amanecer en el mar, un campo de lavanda o montana nevada).\n"
         "2. Subela al visor musical de Google Music y selecciona duracion de 10 segundos.\n"
         "3. Prompt Maestro de Estilo: \"Musica orquestal serena inspirada en este paisaje, con flauta travesera melancolica, cuerdas amplias y sensacion de paz profunda al atardecer.\"\n"
         "Resultado: La IA lee los colores calidos y genera una armonia que encaja a la perfeccion con la atmosfera visual."),

        ("EJERCICIO 3 • FOTO FAMILIAR DE LOS ANOS 70 A LA BALADA NOSTALGICA:",
         "1. Generamos primero en Gemini la foto modelo con el prompt: \"Fotografia familiar de 1978 en color analogico calido: abuelos, padres y ninos sonrientes junto a un Seat 127 blanco en la playa de Cullera, sol de verano y ropa de epoca.\"\n"
         "2. Subimos la foto familiar generada a Google Music AI.\n"
         "3. Prompt Maestro de Musica: \"Balada melodica espanola anos 70 al estilo de Nino Bravo o Mocedades, guitarra acustica doce cuerdas, bajo dulce y nostalgia luminosa de vacaciones familiares.\"\n"
         "Resultado: Una banda sonora conmovedora que revive la magia de aquellos veranos inolvidables.")
    ]

    y_e = 532
    for ex_title, ex_body in exercises:
        pdf.draw_text(42, y_e, ex_title, font='F2', size=7.8, r=0.1, g=0.35, b=0.65)
        y_e -= 10
        for par in ex_body.split('\n'):
            for l in wrap_text(par, 114):
                is_prompt = 'Prompt Maestro' in l or '"' in l
                pdf.draw_text(42, y_e, l, font='F2' if is_prompt else 'F1', size=7.2, r=0.7 if is_prompt else 0.2, g=0.3 if is_prompt else 0.25, b=0.05 if is_prompt else 0.3)
                y_e -= 9.5
        y_e -= 3

    # Sección 3: La unión de vídeo y música a partir de ahora
    pdf.set_fill_color(1.0, 1.0, 1.0)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 205, 552, 60, fill=True, stroke=True)

    pdf.draw_text(42, 252, '3. EL NUEVO ESTANDAR: A PARTIR DE AHORA, CADA VIDEO FLOW CON SU BANDA SONORA', font='F2', size=8.8, r=0.7, g=0.35, b=0.05)
    t3 = (
        "En las proximas sesiones, cada vez que creemos un clip en Google Flow con los movimientos de camara aprendidos, "
        "le anadiremos su pista de audio generada en Google Music. Asi obtendremos obras completas con imagen, movimiento y musica."
    )
    y_t = 238
    for l in wrap_text(t3, 114):
        pdf.draw_text(42, y_t, l, font='F1', size=7.4, r=0.2, g=0.25, b=0.3)
        y_t -= 10.5

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 195, 582, 195)
    pdf.draw_text(36, 180, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 04 • TALLER GOOGLE MUSIC AI [INFO-004B]', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 168, 'Herramienta: Google Music AI (Lyria / Flow Music) • De la Foto al Recuerdo Sonoro • Tarareo con Microfono', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha INFO-004B generada con éxito: {output_path}")

# ==============================================================================
# 4. ACTUALIZACIÓN DE MAPAS HTML (SESIÓN 03 Y SESIÓN 04)
# ==============================================================================
def update_maps():
    print("=== [ACTUALIZANDO MAPAS INTERACTIVOS DE SESION 03 Y 04] ===")

    # 1. MAPA SESIÓN 03
    s03_maps = [
        os.path.join(S03_DIR, "MAPA_CLASE_SESION_03.html"),
        os.path.join(S03_DIR, "MAPA_SESION_03.html")
    ]
    card_info_03b = '''                    <div class="file-card file-card-special" style="background: rgba(234, 67, 53, 0.08); border-color: rgba(234, 67, 53, 0.35);">
                        <a href="1B.%20INFO-003B_Taller_Google_Flow_Camara_Cinematica.pdf" target="_blank" class="file-card-special-top" title="Abrir Ficha Didáctica / Taller (PDF)">
                            <div class="file-left">
                                <span class="file-num">#01B [INFO]</span>
                                <span class="file-tag tag-pdf" style="background:#ea4335; color:#fff;">TALLER VÍDEO</span>
                                <div class="file-details">
                                    <span class="file-title">Taller Rápido: Google Flow y los 4 Movimientos Cinemáticos de Cámara</span>
                                    <span class="file-desc">Estudio de Cine con IA • Orbit, Drone View, Bullet Time y Reveal (50 Créditos/Día)</span>
                                </div>
                            </div>
                            <span class="file-arrow">↗</span>
                        </a>
                        <a href="https://labs.google/flow" target="_blank" class="btn-launch-interactive" style="background:linear-gradient(135deg, #ea4335, #c5221f); border-color:#f28b82;" title="Abrir Plataforma Oficial Google Flow">
                            🎬 Abrir Google Flow (Web Oficial) ↗
                        </a>
                        <a href="1B.%20INFO-003B_Taller_Google_Flow_Camara_Cinematica.pdf" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background:linear-gradient(135deg, #334155, #1e293b); border-color:#64748b;" title="Abrir Ficha Didáctica y Prompts (PDF)">
                            📄 Abrir Ficha Didáctica y Prompts de Cámara (PDF) ↗
                        </a>
                    </div>
'''
    for mpath in s03_maps:
        if os.path.exists(mpath):
            with open(mpath, 'r', encoding='utf-8') as f:
                content = f.read()
            if "INFO-003B" not in content:
                # Insertar tras el primer bloque de INFO-003
                target = '</a>\n                    </div>\n                    <a href="2.'
                replacement = '</a>\n                    </div>\n' + card_info_03b + '                    <a href="2.'
                if target in content:
                    content = content.replace(target, replacement, 1)
                else:
                    # Alternativa buscando por 1. INFO-003
                    idx = content.find('1.%20INFO-003_Novedades_Gemini_Gmail_y_Buscador_IA.pdf')
                    if idx != -1:
                        end_card = content.find('</div>', idx)
                        end_card = content.find('</div>', end_card + 6)
                        if end_card != -1:
                            end_card += 6
                            content = content[:end_card] + '\n' + card_info_03b + content[end_card:]
                # Actualizar contador de recursos de fase 1
                content = content.replace('<span class="branch-count">4 recursos</span>', '<span class="branch-count">5 recursos</span>')
                with open(mpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"🗺️ Mapa Sesión 03 actualizado: {os.path.basename(mpath)}")

    # 2. MAPA SESIÓN 04
    s04_maps = [
        os.path.join(S04_DIR, "MAPA_CLASE_SESION_04.html"),
        os.path.join(S04_DIR, "MAPA_SESION_04.html")
    ]
    card_info_04b = '''                    <div class="file-card file-card-special" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.35);">
                        <a href="1B.%20INFO-004B_Taller_Google_Music_AI_Banda_Sonora.pdf" target="_blank" class="file-card-special-top" title="Abrir Ficha Didáctica / Taller (PDF)">
                            <div class="file-left">
                                <span class="file-num">#01B [INFO]</span>
                                <span class="file-tag tag-pdf" style="background:#059669; color:#fff;">TALLER MÚSICA</span>
                                <div class="file-details">
                                    <span class="file-title">Taller Rápido: Google Music AI (Banda Sonora, Tarareo y De Foto a Música)</span>
                                    <span class="file-desc">Música y Emoción con IA • Tarareo al Micrófono, Paisaje y Recuerdos Familiares</span>
                                </div>
                            </div>
                            <span class="file-arrow">↗</span>
                        </a>
                        <a href="https://labs.google/flow" target="_blank" class="btn-launch-interactive" style="background:linear-gradient(135deg, #059669, #047857); border-color:#34d399;" title="Abrir Google Flow y Music AI">
                            🎵 Abrir Google Music AI (Flow) ↗
                        </a>
                        <a href="1B.%20INFO-004B_Taller_Google_Music_AI_Banda_Sonora.pdf" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background:linear-gradient(135deg, #334155, #1e293b); border-color:#64748b;" title="Abrir Ficha Didáctica y Ejercicios (PDF)">
                            📄 Abrir Ficha Didáctica y 3 Ejercicios Prácticos (PDF) ↗
                        </a>
                    </div>
'''
    for mpath in s04_maps:
        if os.path.exists(mpath):
            with open(mpath, 'r', encoding='utf-8') as f:
                content = f.read()
            if "INFO-004B" not in content:
                # Insertar tras el primer bloque de INFO-004
                target = '</a>\n                    </div>\n                    <a href="11.CUENT-004'
                replacement = '</a>\n                    </div>\n' + card_info_04b + '                    <a href="11.CUENT-004'
                if target in content:
                    content = content.replace(target, replacement, 1)
                else:
                    idx = content.find('1.%20INFO-004_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.pdf')
                    if idx != -1:
                        end_card = content.find('</div>', idx)
                        end_card = content.find('</div>', end_card + 6)
                        if end_card != -1:
                            end_card += 6
                            content = content[:end_card] + '\n' + card_info_04b + content[end_card:]
                # Actualizar contador de recursos de fase 1
                content = content.replace('<span class="branch-count">8 recursos</span>', '<span class="branch-count">9 recursos</span>')
                with open(mpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"🗺️ Mapa Sesión 04 actualizado: {os.path.basename(mpath)}")

# ==============================================================================
# MAIN
# ==============================================================================
def main():
    print("=================================================================")
    print("=== [DESPLIEGUE OFICIAL: INFO-003B (FLOW) Y INFO-004B (MUSIC)] ===")
    print("=================================================================")

    # 1. Generar INFO-003B en S03 y Bloque 15
    p_info_003b_s03 = os.path.join(S03_DIR, "1B. INFO-003B_Taller_Google_Flow_Camara_Cinematica.pdf")
    p_info_003b_b15 = os.path.join(BLOQUE_15_DIR, "INFO-003B_Taller_Google_Flow_Camara_Cinematica.pdf")
    build_info_003b_pdf(p_info_003b_s03)
    shutil.copy2(p_info_003b_s03, p_info_003b_b15)
    print(f"📦 Copiado a Bloque 15: {p_info_003b_b15}")

    # 2. Actualizar 5 fichas de imagen de Sesión 03 con Google Flow
    update_all_s03_image_fiches()

    # 3. Generar INFO-004B en S04 y Bloque 15
    p_info_004b_s04 = os.path.join(S04_DIR, "1B. INFO-004B_Taller_Google_Music_AI_Banda_Sonora.pdf")
    p_info_004b_b15 = os.path.join(BLOQUE_15_DIR, "INFO-004B_Taller_Google_Music_AI_Banda_Sonora.pdf")
    build_info_004b_pdf(p_info_004b_s04)
    shutil.copy2(p_info_004b_s04, p_info_004b_b15)
    print(f"📦 Copiado a Bloque 15: {p_info_004b_b15}")

    # 4. Actualizar mapas interactivos HTML
    update_maps()

    print("\n🎉 ¡DESPLIEGUE COMPLETADO CON ÉXITO ABSOLUTO!")

if __name__ == '__main__':
    main()
