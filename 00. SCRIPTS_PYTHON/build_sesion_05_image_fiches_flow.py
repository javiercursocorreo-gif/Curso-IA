#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_sesion_05_image_fiches_flow.py
Genera las 5 Fichas Didácticas de Imagen de la Sesión 05 actualizadas con
la Ampliación Oficial a Vídeo en Google Flow (50 Créditos Diarios):
- 2. EST-005: Serie Carrusel Monumentos de Madrid con Cielos de los 7 Grandes Maestros
- 3. PRAC-005: Eliminación de Objetos o Personas Molestos (Fotografía Práctica)
- 5. INT-005: El Partenón de Atenas a Todo Color con la Estatua de Atenea
- 6. FUT-005: Año 2038: Redes Eléctricas Cuánticas y Reactores Modulares SMR
- 8. ARTE-005: La Primavera de Sandro Botticelli (1482)
"""

import os
import sys

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
S05_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/05_Sesion")

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
    pdf.draw_text(36, 750, f'SESION 05 • FICHA DIDACTICA DE CREACION CON GEMINI [{tag_code}]', font='F2', size=8.5, r=r_c * 0.8 + 0.2, g=g_c * 0.8 + 0.2, b=b_c * 0.8 + 0.2)
    pdf.draw_text(36, 730, title, font='F2', size=12.0, r=1, g=1, b=1)

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
    pdf.draw_text(36, 208, f'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 05 • {tag_code}', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 196, 'Metodologia Dual: Gemini (Imagen Fija) + Google Flow (Animacion de Video • 10 Creditos)', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha con ampliación Flow generada: {output_path}")

def update_all_s05_image_fiches():
    print("=== [INICIANDO ACTUALIZACION SESION 05 CON GOOGLE FLOW EN 5 FICHAS] ===")

    # 1. EST-005
    p_est = None
    for f in os.listdir(S05_DIR):
        if f.startswith("2. EST-005") and f.endswith(".pdf"):
            p_est = os.path.join(S05_DIR, f)
            break
    if not p_est:
        p_est = os.path.join(S05_DIR, "2. EST-005_IMPRESIONISTA Y POST-IMPRESIONISTA - Serie Carrusel_ Monumentos de Madrid con Cielos de los 7 Grandes Maestros.pdf")

    build_worksheet_with_flow(
        output_path=p_est,
        tag_code="EST-005",
        num_str="2. EST-005",
        title="Serie Carrusel: Monumentos de Madrid con Cielos de los 7 Grandes Maestros",
        desc_concept="Reinterpretar la arquitectura monumental de Madrid (Puerta de Alcala, Cibeles, Palacio Real) sustituyendo sus cielos por los estilos pictoricos y pinceladas de 7 genios universales (Van Gogh, Turner, Monet, Constable, Cezanne, Munch, Friedrich).",
        prompt_gemini="\"Fotografia hiperrealista y pictorica de la Puerta de Alcala en Madrid al atardecer: el monumento de piedra clasica perfectamente iluminado, pero con un cielo dramatico inspirado en la 'Noche Estrellada' de Van Gogh, con remolinos de oleo azul cobalto, amarillo dorado y pinceladas gruesas texturizadas. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Travelling frontal lento y cinematico acercandose a la Puerta de Alcala. Los remolinos de nubes en el cielo de oleo giran con movimiento hipnotico y sutil, mientras las luces calidas de las farolas en la base parpadean suavemente sobre los adoquines de Madrid.\"",
        theme_color_rgb=(0.2, 0.45, 0.8)
    )

    # 2. PRAC-005
    p_prac = None
    for f in os.listdir(S05_DIR):
        if f.startswith("3. PRAC-005") and f.endswith(".pdf"):
            p_prac = os.path.join(S05_DIR, f)
            break
    if not p_prac:
        p_prac = os.path.join(S05_DIR, "3. PRAC-005_Eliminación de objetos o personas molestos.pdf")

    build_worksheet_with_flow(
        output_path=p_prac,
        tag_code="PRAC-005",
        num_str="3. PRAC-005",
        title="Eliminacion de Objetos o Personas Molestos (Fotografia Practica)",
        desc_concept="Limpieza digital de fotografias turisticas o familiares mediante IA (Generative Inpainting). Aprender a eliminar turistas de fondo, cables de electricidad o papeleras para dejar un encuadre limpio, profesional y diáfano.",
        prompt_gemini="\"Fotografia turistica antes y despues: en el lado izquierdo una plaza historica con turistas cruzando y cables de luz; en el lado derecho la misma plaza perfectamente limpia, despejada y soleada, con arquitectura nitida y suelo empedrado impecable. Composicion editorial diafana. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Paneo horizontal lento barriendo de izquierda a derecha la plaza historica. Las palomas revolotean suavemente sobre la fuente de piedra central y la brisa mece las sombras de los soportales en una manana serena y despejada.\"",
        theme_color_rgb=(0.85, 0.45, 0.15)
    )

    # 3. INT-005
    p_int = None
    for f in os.listdir(S05_DIR):
        if f.startswith("5. INT-005") and f.endswith(".pdf"):
            p_int = os.path.join(S05_DIR, f)
            break
    if not p_int:
        p_int = os.path.join(S05_DIR, "5. INT-005_El Partenón de Atenas a todo color con la colosal estatua de Atenea.pdf")

    build_worksheet_with_flow(
        output_path=p_int,
        tag_code="INT-005",
        num_str="5. INT-005",
        title="El Partenon de Atenas a Todo Color con la Colosal Estatua de Atenea",
        desc_concept="Reconstruccion arqueologica hiperrealista del interior de la Acropolis de Atenas en el siglo V a.C.: templos policromados con ricos pigmentos rojos, dorados y azules, albergando la colosal estatua de Atenea Partenos de 12 metros de oro y marfil esculpida por Fidias.",
        prompt_gemini="\"Reconstruccion arqueologica hiperrealista del interior del Partenon de Atenas en el ano 438 a.C.: columnas de marmol policromadas en rojo y azul egipcio, pebeteros de bronce con humo aromatico y la colosal estatua crisoelefantina de Atenea de 12 metros de altura en oro resplandeciente y marfil, sosteniendo a Nike en su mano derecha. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Plano secuencia ascendente muy lento desde el suelo de marmol pulido hacia el rostro sereno de la colosal estatua de Atenea. El humo de los pebeteros flota en espirales doradas y la luz del sol entra por la gran puerta, haciendo brillar los relieves de oro de su escudo.\"",
        theme_color_rgb=(0.1, 0.55, 0.65)
    )

    # 4. FUT-005
    p_fut = None
    for f in os.listdir(S05_DIR):
        if f.startswith("6. FUT-005") and f.endswith(".pdf"):
            p_fut = os.path.join(S05_DIR, f)
            break
    if not p_fut:
        p_fut = os.path.join(S05_DIR, "6. FUT-005_Año 2038_ Redes eléctricas inteligentes cuánticas y reactores modulares de fusión SMR.pdf")

    build_worksheet_with_flow(
        output_path=p_fut,
        tag_code="FUT-005",
        num_str="6. FUT-005",
        title="Ano 2038: Redes Electricas Inteligentes Cuanticas y Reactores Modulares SMR",
        desc_concept="La revolucion energetica limpia y descentralizada de la proxima decada: reactores modulares SMR compactos y seguros, conectados a micro-redes inteligentes gestionadas por computacion cuantica que distribuyen energia a hogares y hospitales sin riesgo de apagones.",
        prompt_gemini="\"Infografia cientifica 3D futurista sobre la energia del ano 2038: corte transversal de un reactor modular SMR compacto y seguro en un entorno suburbano limpio, conectado mediante cables subterraneos luminosos a una red electrica inteligente cuantica que abastece un barrio verde con paneles solares y vehiculos electricos. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Camara orbital lenta alrededor del complejo energetico modular. Los pulsos luminosos de energia azulada viajan por las lineas subterraneas conectando cada edificio de la ciudad ecologica, con turbinas de vapor girando en silencio y cielo diafano.\"",
        theme_color_rgb=(0.15, 0.6, 0.4)
    )

    # 5. ARTE-005
    p_arte = None
    for f in os.listdir(S05_DIR):
        if f.startswith("8. ARTE-005") and f.endswith(".pdf"):
            p_arte = os.path.join(S05_DIR, f)
            break
    if not p_arte:
        p_arte = os.path.join(S05_DIR, "8. ARTE-005_La Primavera de Sandro Botticelli (1482).pdf")

    build_worksheet_with_flow(
        output_path=p_arte,
        tag_code="ARTE-005",
        num_str="8. ARTE-005",
        title="La Primavera de Sandro Botticelli (1482)",
        desc_concept="Obra cumbre de la mitologia renacentista en la Florencia de los Medici: el jardin idilico de naranjos y laureles donde nueve figuras mitologicas (las Tres Gracias, Mercurio disipando nubes, Venus, Flora esparciendo rosas y Cefiro) celebran el renacer de la vida y el humanismo.",
        prompt_gemini="\"Ilustracion y recreacion artistica hiperrealista de 'La Primavera' de Sandro Botticelli (1482): jardin renacentista de naranjos con frutos dorados y fondo umbrio, Venus en el centro vestida de blanco, las Tres Gracias danzando en velos traslucidos a la izquierda y la ninfa Flora esparciendo rosas sobre la hierba verde llena de flores silvestres. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Giro de camara lento en semicirculo frente a las Tres Gracias danzando. Sus velos transparentes de seda ondean con suavidad extrema, las flores del suelo se mecen con una brisa tenue y petalos de rosa caen flotando en camara lenta alrededor de Venus.\"",
        theme_color_rgb=(0.6, 0.3, 0.7)
    )

    print("\n✨ Las 5 fichas de imagen de Sesión 05 han sido generadas con la ampliación oficial a Google Flow.")

if __name__ == '__main__':
    update_all_s05_image_fiches()
