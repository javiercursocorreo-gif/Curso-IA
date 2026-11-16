#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_sesion_06_image_fiches_flow.py
Genera las 5 Fichas Didácticas de Imagen de la Sesión 06 actualizadas con
la Ampliación Oficial a Vídeo en Google Flow (50 Créditos Diarios):
- 2. EST-006: Serie Carrusel Magistral: La Puerta de San Vicente bajo 9 Genios del Arte
- 3. PRAC-006: Vestuario de Alta Costura o Gala para la Alfombra Roja (Fotografía Práctica)
- 5. INT-006: Reconstrucción del Mausoleo de Halicarnaso con Cuadriga de Mármol
- 6. FUT-006: Año 2040: Drones Urbanos de Pasajeros (eVTOL) y Aeropuertos en Azoteas
- 8. ARTE-006: La Escuela de Atenas de Rafael Sanzio (1511)
"""

import os
import sys

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
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
    pdf.draw_text(36, 750, f'SESION 06 • FICHA DIDACTICA DE CREACION CON GEMINI [{tag_code}]', font='F2', size=8.5, r=r_c * 0.8 + 0.2, g=g_c * 0.8 + 0.2, b=b_c * 0.8 + 0.2)
    pdf.draw_text(36, 730, title, font='F2', size=11.8, r=1, g=1, b=1)

    # Sección 1: Concepto y Objetivo en el Aula
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

    # Sección 2: Prompt Maestro para Gemini
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

    # Sección 3: Ampliación Oficial con Google Flow (10 Puntos)
    pdf.set_fill_color(0.99, 0.97, 0.93)
    pdf.set_stroke_color(0.85, 0.45, 0.1)
    pdf.set_line_width(1.2)
    pdf.rect(30, 235, 552, 200, fill=True, stroke=True)

    pdf.draw_text(42, 420, '3. AMPLIACION: ¡DALE VIDA EN VIDEO CON GOOGLE FLOW! (Gasta 10 de tus 50 puntos diarios)', font='F2', size=8.8, r=0.75, g=0.3, b=0.02)
    
    steps_txt = [
        "1. Guarda la imagen: Haz clic sobre la imagen que acaba de generar Gemini y pulsa el icono de 'Descargar' (la flecha).",
        "2. Entra en Google Flow: Abre https://labs.google/flow con tu cuenta de Google y pulsa en 'Subir Imagen' (Upload).",
        "3. Pega el prompt de abajo: En el recuadro de texto de Flow, pega el siguiente prompt de movimiento y pulsa 'Generar Video'."
    ]
    y_st = 405
    for st in steps_txt:
        pdf.draw_text(42, y_st, st, font='F2' if '1.' in st or '2.' in st or '3.' in st else 'F1', size=7.2, r=0.25, g=0.2, b=0.15)
        y_st -= 11

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
    pdf.draw_text(36, 208, f'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 06 • {tag_code}', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 196, 'Metodologia Dual: Gemini (Imagen Fija) + Google Flow (Animacion de Video • 10 Creditos)', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha con ampliación Flow generada: {output_path}")

def update_all_s06_image_fiches():
    print("=== [INICIANDO ACTUALIZACION SESION 06 CON GOOGLE FLOW EN 5 FICHAS] ===")

    # 1. EST-006
    p_est = None
    for f in os.listdir(S06_DIR):
        if f.startswith("2. EST-006") and f.endswith(".pdf"):
            p_est = os.path.join(S06_DIR, f)
            break
    if not p_est:
        p_est = os.path.join(S06_DIR, "2. EST-006_IMPRESIONISTA Y POST-IMPRESIONISTA - Serie Carrusel Magistral_ El Cuadro de Aguirre de la Puerta de San Vicente bajo 9 Genios del Arte.pdf")

    build_worksheet_with_flow(
        output_path=p_est,
        tag_code="EST-006",
        num_str="2. EST-006",
        title="Serie Carrusel Magistral: La Puerta de San Vicente bajo 9 Genios del Arte",
        desc_concept="Reinterpretar la historica Puerta de San Vicente de Madrid (oleo de Gines Andres de Aguirre, 1787, Museo del Prado) fusionando su arquitectura clasica con las paletas, luces y texturas de 9 genios de la pintura (Goya, Sorolla, Velazquez, Monet, Van Gogh, El Greco, Turner, Cezanne, Friedrich).",
        prompt_gemini="\"Recreacion pictorica magistral de la Puerta de San Vicente de Madrid en 1787: composicion clasica basada en el oleo de Gines Andres de Aguirre, con carruajes de caballos y damas con mantilla cruzando el arco de piedra, pero reinterpretada con la luz vibrante del mar mediterraneo y pinceladas luminosas y sueltas al estilo de Joaquin Sorolla. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Travelling frontal suave y cinematico avanzando hacia la Puerta de San Vicente. La luz dorada del sol resplandece sobre la piedra caliza, los caballos tiran suavemente del carruaje de epoca y los vestidos de las damas se mecen con una brisa tenue en una manana madrilena llena de vida.\"",
        theme_color_rgb=(0.2, 0.45, 0.8)
    )

    # 2. PRAC-006
    p_prac = None
    for f in os.listdir(S06_DIR):
        if f.startswith("3. PRAC-006") and f.endswith(".pdf"):
            p_prac = os.path.join(S06_DIR, f)
            break
    if not p_prac:
        p_prac = os.path.join(S06_DIR, "3. PRAC-006_Vestuario de Alta Costura o Gala para la Alfombra Roja.pdf")

    build_worksheet_with_flow(
        output_path=p_prac,
        tag_code="PRAC-006",
        num_str="3. PRAC-006",
        title="Vestuario de Alta Costura o Gala para la Alfombra Roja (Fotografia Practica)",
        desc_concept="Transformacion estetica de retratos cotidianos en vestidos de noche o esmoquines de alta costura disenados para festivales internacionales de cine (Cannes, San Sebastian, Venecia). Dominio de tejidos ricos (seda salvaje, terciopelo, pedreria fina), iluminacion de flashes y alfombra roja.",
        prompt_gemini="\"Fotografia editorial de alfombra roja de festival de cine: retrato elegante de una persona madura vestida con un impecable esmoquin negro a medida o vestido de gala de terciopelo azul noche con bordados discretos de hilo de plata, sonriendo con distincion ante la barrera de fotografos y focos suaves. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Camara lenta con ligero acercamiento al rostro mientras los flashes de los fotografos parpadean en el fondo desenfocado. La persona sonrie con serenidad, hace un saludo sutil con la mano y los reflejos de luz brillan sobre el terciopelo y la alfombra roja.\"",
        theme_color_rgb=(0.85, 0.45, 0.15)
    )

    # 3. INT-006
    p_int = None
    for f in os.listdir(S06_DIR):
        if f.startswith("5. INT-006") and f.endswith(".pdf"):
            p_int = os.path.join(S06_DIR, f)
            break
    if not p_int:
        p_int = os.path.join(S06_DIR, "5. INT-006_Reconstrucción del Mausoleo de Halicarnaso culminado con cuadriga de mármol.pdf")

    build_worksheet_with_flow(
        output_path=p_int,
        tag_code="INT-006",
        num_str="5. INT-006",
        title="Reconstruccion del Mausoleo de Halicarnaso con Cuadriga de Marmol",
        desc_concept="Una de las Siete Maravillas del Mundo Antiguo (siglo IV a.C., actual Turquia): la colosal tumba del rey Mausolo de Caria con sus 45 metros de altura, 36 columnas jonicas, friso de amazonas esculpido por Escopas y coronado por una cuadriga colosal de marmol blanco conducida por Mausolo y Artemisia.",
        prompt_gemini="\"Reconstruccion arqueologica hiperrealista del Mausoleo de Halicarnaso en su maximo esplendor (ano 350 a.C.): colosal monumento de 45 metros de altura en marmol blanco brillante junto al mar Egeo, rodeado de estatuas de leones y coronado por una piramide con la majestuosa cuadriga de cuatro caballos guiada por el rey Mausolo. Cielo mediterraneo diafano. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Plano aereo en semi-orbita cinematografica rodeando la cima del monumento. La gran cuadriga de marmol blanco se alza majestuosa contra el azul profundo del mar Egeo, las olas rompen suaves en la costa lejana y la luz dorada del atardecer resalta cada bajorrelieve esculpido.\"",
        theme_color_rgb=(0.1, 0.55, 0.65)
    )

    # 4. FUT-006
    p_fut = None
    for f in os.listdir(S06_DIR):
        if f.startswith("6. FUT-006") and f.endswith(".pdf"):
            p_fut = os.path.join(S06_DIR, f)
            break
    if not p_fut:
        p_fut = os.path.join(S06_DIR, "6. FUT-006_Año 2040_ Drones urbanos de transporte de pasajeros (eVTOL) y aeropuertos en azoteas.pdf")

    build_worksheet_with_flow(
        output_path=p_fut,
        tag_code="FUT-006",
        num_str="6. FUT-006",
        title="Ano 2040: Drones Urbanos de Pasajeros (eVTOL) y Aeropuertos en Azoteas",
        desc_concept="La movilidad urbana aerea en la proxima decada: aeronaves electricas de despegue y aterrizaje vertical (eVTOL) sin emisiones ni ruido que conectan azoteas y vertipuertos urbanos a 200 km/h, transformando el trafico de las grandes capitales y liberando el suelo para parques peatonales.",
        prompt_gemini="\"Infografia y render fotografico futurista de una metropolis europea en el ano 2040: vertipuerto ajardinado sobre la azotea de un rascacielos sostenible de madera y cristal, donde aterriza suavemente un dron taxi de pasajeros eVTOL electrico y silencioso con diseno aerodinamico blanco y cabina panoramica. Al fondo, corredores aereos ordenados y calles peatonales verdes. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Descenso suave en camara lenta del dron de pasajeros eVTOL posandose con precision en el circulo luminoso del vertipuerto. Sus rotores electricos desaceleran en silencio, las puertas de cristal de la azotea se abren suavemente y el horizonte de la ciudad al atardecer refleja luces ecologicas tenues.\"",
        theme_color_rgb=(0.15, 0.6, 0.4)
    )

    # 5. ARTE-006
    p_arte = None
    for f in os.listdir(S06_DIR):
        if f.startswith("8. ARTE-006") and f.endswith(".pdf"):
            p_arte = os.path.join(S06_DIR, f)
            break
    if not p_arte:
        p_arte = os.path.join(S06_DIR, "8. ARTE-006_La Escuela de Atenas de Rafael Sanzio (1511).pdf")

    build_worksheet_with_flow(
        output_path=p_arte,
        tag_code="ARTE-006",
        num_str="8. ARTE-006",
        title="La Escuela de Atenas de Rafael Sanzio (1511)",
        desc_concept="Fresco cumbre del Renacimiento en las Estancias Vaticanas: la gran asamblea del saber humano donde Platon (con los rasgos de Leonardo da Vinci) senala al cielo de las ideas y Aristoteles extiende su palma hacia la tierra de la experiencia tangible, rodeados por Socrates, Pitagoras, Euclides y Diogenes bajo una colosal basilica de arcos de medio punto.",
        prompt_gemini="\"Ilustracion y recreacion hiperrealista al fresco de 'La Escuela de Atenas' de Rafael Sanzio (1511): monumental basilica renacentista de techos abovedados y esculturas clasicas de Apolo y Minerva, con Platon vestido de rojo senalando al cielo y Aristoteles vestido de azul con su libro de etica, debatiendo rodeados por filosofos y matematicos clasicos en tunicas fluidas. Iluminacion celestial majestuosa. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Travelling frontal lento avanzando majestuosamente por la nave central hacia Platon y Aristoteles. Los rayos de luz solar caen en haces dorados desde el gran arco romano, las tunicas de los filosofos se mueven suavemente al debatir y el polvo cosmico dorado flota en el aire de la academia eterna.\"",
        theme_color_rgb=(0.6, 0.3, 0.7)
    )

    print("\n✨ Las 5 fichas de imagen de Sesión 06 han sido generadas con la ampliación oficial a Google Flow.")

if __name__ == '__main__':
    update_all_s06_image_fiches()
