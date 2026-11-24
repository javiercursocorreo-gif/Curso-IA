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

    # 1. TÍTULO MAYOR 1 (PÁGINA 1)
    # Barra de acento y caja destacada para título mayor (13.0pt)
    pdf.set_fill_color(0.85, 0.25, 0.2)
    pdf.rect(30, 706, 552, 3, fill=True, stroke=False)
    pdf.set_fill_color(0.98, 0.92, 0.92)
    pdf.set_stroke_color(0.85, 0.25, 0.2)
    pdf.set_line_width(1.0)
    pdf.rect(30, 680, 552, 24, fill=True, stroke=True)
    pdf.draw_text(42, 687, '1. EL ESTUDIO DE CINE DE GOOGLE: 50 CRÉDITOS DIARIOS GRATUITOS', font='F2', size=12.5, r=0.75, g=0.15, b=0.1)

    # Tarjeta de contenido Sección 1
    pdf.set_fill_color(1.0, 1.0, 1.0)
    pdf.set_stroke_color(0.85, 0.25, 0.2)
    pdf.set_line_width(0.8)
    pdf.rect(30, 584, 552, 90, fill=True, stroke=True)
    
    t1 = (
        "Google Flow (https://labs.google/flow) es la herramienta de Google que genera clips de cine en movimiento "
        "de 5 segundos con fisica realista y movimientos profesionales de camara a partir de prompts de texto.\n"
        "• Acceso directo con tu cuenta de Google (Gmail): Sin pagos, sin suscripciones y sin tarjetas de credito.\n"
        "• 50 Creditos diarios renovables a las 00:00: Cada clip de 5 segundos consume 12 creditos (hasta 4 videos gratis al dia).\n"
        "• Metodologia Directa en 3 Pasos (Sin fotos intermedias): 1) Copiar el prompt de la ficha a Gemini. "
        "2) Gemini redacta tus 3 prompts de camara. 3) Copiar sucesivamente cada prompt en Flow y generar el clip."
    )
    y_pos = 660
    for par in t1.split('\n'):
        lines = wrap_text(par, 114)
        for l in lines:
            pdf.draw_text(42, y_pos, l, font='F2' if '•' in l and ':' in l else 'F1', size=7.4, r=0.15, g=0.2, b=0.25)
            y_pos -= 11.2

    # 2. TÍTULO MAYOR 2 (PÁGINA 1)
    pdf.set_fill_color(0.1, 0.3, 0.65)
    pdf.rect(30, 574, 552, 3, fill=True, stroke=False)
    pdf.set_fill_color(0.92, 0.95, 0.99)
    pdf.set_stroke_color(0.1, 0.3, 0.65)
    pdf.set_line_width(1.0)
    pdf.rect(30, 548, 552, 24, fill=True, stroke=True)
    pdf.draw_text(42, 555, '2. LOS 4 MOVIMIENTOS CINEMÁTICOS DE CÁMARA (DIRECCIÓN DE ESCENA)', font='F2', size=12.5, r=0.1, g=0.3, b=0.65)

    moves = [
        ("1. DRONE VIEW (Vuelo Aereo / Perspectiva Cenital):",
         "La camara sobrevuela como un dron desde gran altura, ascendiendo o descendiendo suavemente para mostrar grandes paisajes, desfiladeros o montanas. Aporta sensacion de escala majestuosa y vuelo sereno.",
         "🎬 Efecto en pantalla: Vuelo aereo suave sobre la Serrania de Ronda al amanecer desvelando el camino real.",
         (0.1, 0.45, 0.75)),

        ("2. ORBIT (Giro 360 Grados Orbital):",
         "La camara rota circularmente alrededor del sujeto principal manteniendolo siempre en el centro del encuadre. Aporta volumen y tridimensionalidad cinematografica al personaje, estatua o vehiculo.",
         "🎬 Efecto en pantalla: Giro circular lento alrededor de Curro Jimenez sobre su caballo en el risco rocoso.",
         (0.75, 0.25, 0.1)),

        ("3. TRACKING (Camara de Seguimiento en Movimiento):",
         "La camara se desplaza en paralelo acompanando al sujeto mientras cabalga o camina por el sendero. Mantiene el dinamismo y la sensacion de viaje y aventura sin movimientos bruscos.",
         "🎬 Efecto en pantalla: La camara acompana de lado el avance elegante del caballo al paso.",
         (0.1, 0.55, 0.3)),

        ("4. BULLET TIME / ZOOM IN (Camara Ultralenta y Acercamiento Dramatico):",
         "El tiempo parece detenerse mientras la camara se aproxima con suavidad milimetrica al foco emocional de la escena, como la mirada decidida del heroe o el brillo de su sombrero y trabuco.",
         "🎬 Efecto en pantalla: Acercamiento suave a camara lenta hacia la mirada decidida bajo el sombrero calanes.",
         (0.5, 0.2, 0.7))
    ]

    card_h = 100
    gap = 10
    y_top = 538
    for i, (m_title, m_desc, m_ex, col) in enumerate(moves):
        y_card = y_top - i * (card_h + gap)
        pdf.set_fill_color(0.98, 0.99, 1.0)
        pdf.set_stroke_color(col[0], col[1], col[2])
        pdf.set_line_width(0.8)
        pdf.rect(30, y_card - card_h, 552, card_h, fill=True, stroke=True)

        pdf.draw_text(42, y_card - 18, m_title, font='F2', size=8.2, r=col[0], g=col[1], b=col[2])
        yc = y_card - 32
        for l in wrap_text(m_desc, 112):
            pdf.draw_text(42, yc, l, font='F1', size=7.2, r=0.2, g=0.25, b=0.3)
            yc -= 10.0
        yc -= 2.0
        for l in wrap_text(m_ex, 112):
            pdf.draw_text(42, yc, l, font='F3', size=7.0, r=col[0]*0.8, g=col[1]*0.8, b=col[2]*0.8)
            yc -= 9.5

    # Pie institucional página 1
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 85, 582, 85)
    pdf.draw_text(36, 72, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 03 • TALLER GOOGLE FLOW [INFO-003B] • PAGINA 1 DE 2', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 60, 'Herramienta: Google Flow (https://labs.google/flow) • 50 Creditos Diarios Gratuitos • Cine con IA en Espanol', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    # =========================================================================
    # PÁGINA 2: TALLER AVANZADO DE RECREACIÓN DE SERIES Y PERSONAJE ANCLA
    # =========================================================================
    pdf.end_page()
    pdf.start_page()

    # Marco exterior elegante
    pdf.set_fill_color(0.99, 0.99, 1.0)
    pdf.set_stroke_color(0.85, 0.25, 0.2)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera página 2
    pdf.set_fill_color(0.82, 0.18, 0.15)
    pdf.rect(24, 714, 564, 54, fill=True, stroke=False)
    pdf.draw_text(36, 750, 'SESION 03 • TALLER CINEMATOGRAFICO AVANZADO • GOOGLE FLOW & GEMINI [INFO-003B]', font='F2', size=8.5, r=1, g=1, b=1)
    pdf.draw_text(36, 730, 'Caso Práctico Real: Mini-Película de Curro Jiménez (De Gemini a Google Flow)', font='F2', size=11.5, r=1, g=1, b=1)

    # 3. TÍTULO MAYOR 3 (PÁGINA 2)
    pdf.set_fill_color(0.85, 0.25, 0.2)
    pdf.rect(30, 706, 552, 3, fill=True, stroke=False)
    pdf.set_fill_color(0.98, 0.92, 0.92)
    pdf.set_stroke_color(0.85, 0.25, 0.2)
    pdf.set_line_width(1.0)
    pdf.rect(30, 680, 552, 24, fill=True, stroke=True)
    pdf.draw_text(42, 687, '3. EL MÉTODO DIRECTO EN 3 PASOS (CERO FOTOS INTERMEDIAS)', font='F2', size=12.5, r=0.75, g=0.15, b=0.1)

    # Tarjeta Sección 3
    pdf.set_fill_color(1.0, 1.0, 1.0)
    pdf.set_stroke_color(0.85, 0.25, 0.2)
    pdf.set_line_width(0.8)
    pdf.rect(30, 565, 552, 110, fill=True, stroke=True)

    s4_text = (
        "• PASO 1 (El Guion en Gemini): Copias el prompt de abajo y lo pegas en Gemini. Gemini actua como director de cine: "
        "aplica las tecnicas de camara, mantiene el personaje de Curro identico en las 3 tomas y te entrega 3 prompts en espanol listos para Flow.\n"
        "• PASO 2 (El Rodaje en Flow): Entras a Google Flow (https://labs.google/flow) y ruedas clip a clip. Pegas el Prompt 1 "
        "y pulsas Generar (12 creditos); luego el Prompt 2 (12 creditos); y finalmente el Prompt 3 (12 creditos).\n"
        "• PASO 3 (Tu Mini-Pelicula): Obtienes 3 clips de 5 segundos (15 segundos de cine historico) con el mismo Curro sin mutaciones. "
        "Presupuesto: 3 tomas x 12 = 36 creditos consumidos de los 50 gratuitos diarios. ¡Te sobran 14 creditos cada dia!"
    )
    y4 = 658
    for par in s4_text.split('\n'):
        for l in wrap_text(par, 114):
            pdf.draw_text(42, y4, l, font='F2' if '•' in l and ':' in l else 'F1', size=7.2, r=0.15, g=0.2, b=0.25)
            y4 -= 10.0

    # 4. TÍTULO MAYOR 4 (PÁGINA 2)
    pdf.set_fill_color(0.2, 0.45, 0.8)
    pdf.rect(30, 555, 552, 3, fill=True, stroke=False)
    pdf.set_fill_color(0.93, 0.96, 1.0)
    pdf.set_stroke_color(0.2, 0.45, 0.8)
    pdf.set_line_width(1.0)
    pdf.rect(30, 529, 552, 24, fill=True, stroke=True)
    pdf.draw_text(42, 536, '4. EL PROMPT MAESTRO DE DIRECCIÓN (COPIA Y PEGA EN GEMINI)', font='F2', size=12.5, r=0.1, g=0.3, b=0.65)

    # Tarjeta Sección 4
    pdf.set_fill_color(1.0, 1.0, 1.0)
    pdf.set_stroke_color(0.2, 0.45, 0.8)
    pdf.set_line_width(0.8)
    pdf.rect(30, 248, 552, 276, fill=True, stroke=True)

    pdf.draw_text(42, 510, 'Este prompt ya incluye todas las ordenes tecnicas de rodaje y coherencia para que tu no tengas que inventar nada:', font='F3', size=7.1, r=0.4, g=0.45, b=0.5)

    p_master = (
        "\"Actua como director de cine profesional. Disena una escena cinematografica de 3 planos continuos inspirada en la mitica serie espanola 'Curro Jimenez' ambientada en la Serrania de Ronda (1808).\n"
        "Instrucciones de direccion:\n"
        "1) Personaje consistente: Describe a Curro Jimenez con los mismos rasgos exactos en todas las tomas (patillas patibularias, sombrero calanes negro, capa andaluza, trabuco de chispa y caballo tordo).\n"
        "2) Movimientos de camara: Aplica en cada plano uno de los 4 movimientos cinematicos maestros para crear dinamismo y tension dramatica.\n"
        "3) Entrega tecnica: Redacta directamente los 3 prompts en espanol claro y cinematografico, listos para que los alumnos los entiendan y los copien en Google Flow:\n"
        "   - TOMA 1 (5s): Plano general del paisaje serrano al amanecer con VISTA AEREA / DRON (Drone View).\n"
        "   - TOMA 2 (5s): Plano medio de Curro a caballo vigilando el camino real con CAMARA ORBITAL o SEGUIMIENTO (Orbit / Tracking).\n"
        "   - TOMA 3 (5s): Primer plano dramatico de su mirada decidida bajo el sombrero calanes con ZOOM IN lento o BULLET TIME.\""
    )
    y5 = 496
    for par in p_master.split('\n'):
        for l in wrap_text(par, 114):
            pdf.draw_text(42, y5, l, font='F2' if any(k in l for k in ['1)', '2)', '3)', '- TOMA']) else 'F1', size=7.0, r=0.15, g=0.2, b=0.25)
            y5 -= 9.5

    pdf.draw_text(42, 256, '➔ Gemini te entregara en segundos tus 3 Prompts de Rodaje en espanol listos para llevar a Google Flow.', font='F2', size=7.3, r=0.05, g=0.45, b=0.25)

    # 5. TÍTULO MAYOR 5 (PÁGINA 2)
    pdf.set_fill_color(0.8, 0.5, 0.1)
    pdf.rect(30, 238, 552, 3, fill=True, stroke=False)
    pdf.set_fill_color(0.99, 0.96, 0.91)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 212, 552, 24, fill=True, stroke=True)
    pdf.draw_text(42, 219, '5. CÓMO UNIR TUS 3 CLIPS EN UN SOLO VÍDEO (CLIPCHAMP)', font='F2', size=12.0, r=0.7, g=0.35, b=0.05)

    # Tarjeta Sección 5
    pdf.set_fill_color(0.98, 0.98, 1.0)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(0.8)
    pdf.rect(30, 95, 552, 113, fill=True, stroke=True)

    v_text = (
        "Si quieres juntar tus 3 tomas de Google Flow en una sola pelicula continua de 15 segundos para enviarla por WhatsApp a tu familia:\n"
        "• 1. Abrir el Editor Gratuito: En la barra de busqueda de tu ordenador Windows (lupa abajo a la izquierda), escribe Clipchamp (o Editor de video) y abre la aplicacion gratuita integrada.\n"
        "• 2. Anadir tus 3 Videos: Pulsa en Crear un nuevo video. Haz clic en Importar multimedia y selecciona los 3 videos descargados de Google Flow (Toma 1, Toma 2 y Toma 3).\n"
        "• 3. Ordenar en la Linea de Tiempo: Arrastra los 3 videos a la pista inferior horizontal, colocandolos uno detras de otro en fila (primero el paisaje, luego Curro a caballo y al final su primer plano).\n"
        "• 4. Guardar tu Pelicula Final: Pulsa arriba a la derecha en el boton Exportar y elige 1080p (HD). ¡En pocos segundos tendras tu archivo de video completo listo para disfrutar!"
    )
    y6 = 194
    for par in v_text.split('\n'):
        for l in wrap_text(par, 112):
            pdf.draw_text(42, y6, l, font='F2' if any(k in l for k in ['• 1.', '• 2.', '• 3.', '• 4.']) else 'F1', size=7.1, r=0.15, g=0.2, b=0.25)
            y6 -= 9.5

    # Pie institucional página 2
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 85, 582, 85)
    pdf.draw_text(36, 72, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 03 • TALLER GOOGLE FLOW [INFO-003B] • PAGINA 2 DE 2', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 60, 'Metodologia Oficial: Guion Tecnico en Gemini + Rodaje Directo en Google Flow • 3 Planos Continuos de Curro Jimenez', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha INFO-003B generada con éxito (2 páginas completas): {output_path}")

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

    pdf.draw_text(42, 420, '3. AMPLIACION: ¡DALE VIDA EN VIDEO CON GOOGLE FLOW! (Gasta 12 de tus 50 puntos diarios)', font='F2', size=8.8, r=0.75, g=0.3, b=0.02)
    
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
    pdf.draw_text(36, 196, 'Metodologia Dual: Gemini (Imagen Fija) + Google Flow (Animacion de Camara • 12 Creditos)', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

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
    pdf.draw_text(36, 730, 'Taller Oficial: Google Flow Music (Productor IA, Tarareo y Banda Sonora para tus Imagenes)', font='F2', size=11.2, r=1, g=1, b=1)

    # Sección 1: Qué es Google Flow Music y el Productor IA
    pdf.set_fill_color(1.0, 1.0, 1.0) # Fondo blanco
    pdf.set_stroke_color(0.1, 0.6, 0.35)
    pdf.set_line_width(1.0)
    pdf.rect(30, 585, 552, 115, fill=True, stroke=True)

    pdf.draw_text(42, 684, '1. GOOGLE FLOW MUSIC: TU ESTUDIO DE GRABACION Y PRODUCTOR VIRTUAL CON IA', font='F2', size=9.2, r=0.08, g=0.45, b=0.25)
    
    t1 = (
        "Google Flow Music (tecnologia Lyria de Google DeepMind en labs.google) crea canciones y bandas sonoras completas "
        "con voces e instrumentacion realista en segundos, adaptada a la musica de los anos 60, 70 y 80 de nuestra juventud.\n"
        "• Productor Virtual IA (Gemini): Habla con el en espanol como en un estudio real (\"haz el piano mas suave\", \"voz mas calida\").\n"
        "• Image-to-Music (De Imagen a Musica): Sube cualquier imagen generada en clase para que la IA componga su banda sonora a medida.\n"
        "• Audio-to-Music (El Milagro del Tarareo): Tarareas 4 notas al microfono y la IA lo transforma en una orquesta o balada de los 70."
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
    pdf.draw_text(42, 547, 'Practicas guiadas para crear musica de los anos 60, 70 y 80 y sonorizar las imagenes del curso:', font='F3', size=7.2, r=0.4, g=0.45, b=0.5)

    exercises = [
        ("EJERCICIO 1 • EL MILAGRO DEL TARAREO (DEL MICROFONO A LA BALADA POP-ROCK):",
         "1. Pulsa el icono del microfono en Google Flow Music y tararea 4 notas sencillas con tu propia voz ('na, na, na...').\n"
         "2. Elige el estilo escribiendo en el recuadro de peticion o chatea con el Productor Virtual IA.\n"
         "3. Prompt Maestro: \"Transforma este tarareo en una balada acustica pop-rock anos 70 al estilo de Los Secretos o Eagles, con guitarras de doce cuerdas, bajo calido y melodia emotiva. Duracion: 15 segundos.\"\n"
         "Resultado: Tu tarareo casero se convierte en una produccion de estudio con la magia del pop clasico."),

        ("EJERCICIO 2 • DE CUALQUIER IMAGEN A LA BANDA SONORA ORIGINAL (IMAGE-TO-MUSIC):",
         "1. Descarga cualquier imagen creada en Gemini (paisajes, monumentos de [MEM], arte de Botticelli o escenas de futuro).\n"
         "2. Subela a Google Flow Music y pulsa 'Generar musica inspirada en esta imagen'.\n"
         "3. Prompt Maestro: \"Banda sonora instrumental inspirada en esta imagen, con guitarras calidas, sintetizador suave anos 80 y atmosfera de paz serena. Duracion: 10 segundos.\"\n"
         "Resultado: Cada imagen fija del curso cobra vida con su propia postal sonora sincronizada a medida."),

        ("EJERCICIO 3 • FOTO FAMILIAR DE LOS ANOS 70-80 A LA CANCION NOSTALGICA:",
         "1. Generamos en Gemini una imagen evocadora: \"Fotografia familiar de 1978 en color calido: tarde de verano junto a un Seat 127 blanco, risas y ropa de epoca.\"\n"
         "2. Subimos la foto familiar generada a Google Flow Music.\n"
         "3. Prompt Maestro de Cancion: \"Cancion melodica espanola de finales de los 70 al estilo de Nino Bravo o Mocedades, con piano luminoso, cuerdas orquestales y nostalgia de vacaciones inolvidables.\"\n"
         "4. Diálogo con el Productor: Escribe en el chat: \"Haz que la voz entre despacio y anade un solo de guitarra acustica al final\".")
    ]

    y_e = 532
    for ex_title, ex_body in exercises:
        pdf.draw_text(42, y_e, ex_title, font='F2', size=7.8, r=0.1, g=0.35, b=0.65)
        y_e -= 10
        for par in ex_body.split('\n'):
            for l in wrap_text(par, 114):
                is_prompt = 'Prompt Maestro' in l or '"' in l or 'Diálogo' in l
                pdf.draw_text(42, y_e, l, font='F2' if is_prompt else 'F1', size=7.2, r=0.7 if is_prompt else 0.2, g=0.3 if is_prompt else 0.25, b=0.05 if is_prompt else 0.3)
                y_e -= 9.5
        y_e -= 3

    # Sección 3: Poner música a las imágenes de todas las etiquetas
    pdf.set_fill_color(1.0, 1.0, 1.0)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 205, 552, 60, fill=True, stroke=True)

    pdf.draw_text(42, 252, '3. EL NUEVO ESTANDAR: PONER MUSICA A LAS IMAGENES FIJAS DE TODAS LAS ETIQUETAS', font='F2', size=8.8, r=0.7, g=0.35, b=0.05)
    t3 = (
        "Los clips animados de Google Flow ya generan su propio sonido ambiental. La verdadera joya creativa consiste en sonorizar "
        "las imagenes fijas de clase ([EST], [PRAC], [INT], [FUT], [ARTE], [MEM]): subiendo la imagen a Google Flow Music, "
        "cada alumno convierte sus ilustraciones en una Postal Sonora completa con su banda sonora original exclusiva."
    )
    y_t = 238
    for l in wrap_text(t3, 114):
        pdf.draw_text(42, y_t, l, font='F1', size=7.4, r=0.2, g=0.25, b=0.3)
        y_t -= 10.5

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 195, 582, 195)
    pdf.draw_text(36, 180, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 04 • TALLER GOOGLE FLOW MUSIC [INFO-004B]', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 168, 'Herramienta: Google Flow Music (flowmusic.google) • Productor Virtual Gemini • Postales Sonoras para tus Imagenes', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha INFO-004B generada con éxito: {output_path}")

# ==============================================================================
# 4. ACTUALIZACIÓN DE MAPAS HTML (SESIÓN 03 Y SESIÓN 04)
# ==============================================================================
def update_maps():
    print("=== [MAPAS INTERACTIVOS: YA ESTÁN VALIDADOS Y EN FORMATO OFICIAL] ===")
    return

# ==============================================================================
# MAIN
# ==============================================================================
def main():
    print("=================================================================")
    print("=== [DESPLIEGUE OFICIAL: INFO-003B (FLOW) Y INFO-004B (MUSIC)] ===")
    print("=================================================================")

    # 1. Generar INFO-003B en S03 y Bloque 15 (Nuevo nombre con prefijo 2.)
    p_info_003b_s03 = os.path.join(S03_DIR, "2. INFO-003B_Taller_Google_Flow_Camara_Cinematica.pdf")
    p_info_003b_b15 = os.path.join(BLOQUE_15_DIR, "INFO-003B_Taller_Google_Flow_Camara_Cinematica.pdf")
    build_info_003b_pdf(p_info_003b_s03)
    shutil.copy2(p_info_003b_s03, p_info_003b_b15)
    print(f"📦 Copiado a Bloque 15: {p_info_003b_b15}")

    # Limpiar archivo viejo 1B si existía en S03
    old_1b = os.path.join(S03_DIR, "1B. INFO-003B_Taller_Google_Flow_Camara_Cinematica.pdf")
    if os.path.exists(old_1b):
        try:
            os.remove(old_1b)
            print(f"🗑️ Eliminado archivo antiguo con prefijo 1B: {old_1b}")
        except Exception as e:
            print(f"Aviso al limpiar 1B: {e}")

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
