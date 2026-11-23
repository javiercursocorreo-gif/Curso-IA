#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_mem_flow_music_and_sync_maps.py
1. Inyecta en las fichas [MEM-003] a [MEM-015] el Paso 3: Visor Fotográfico Cinemático y Postal Sonora en Gemini (Canvas / Vista Previa)
   con la ambientación musical histórica y auténtica de cada época y monumento.
2. Genera los PDFs nativos con codificación WinAnsiEncoding estándar, asegurando que todos los acentos (á, é, í, ó, ú, ñ, ¿, ¡, etc.)
   se muestren impecablemente en cualquier visor de PDF (Preview, Acrobat, Chrome, iPad).
3. Corrige cualquier falta ortográfica en encabezados, instrucciones y preguntas.
4. Renumera limpiamente y sin excepciones todos los mapas de Sesión 03 a 15 (MAPA_SESION_XX.html y MAPA_CLASE_SESION_XX.html).
"""

import os
import re
import sys
import shutil

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SESSIONS_DIR = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
MEM_DIR_LOTE1 = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "13. [MEM] BLOQUE_13_CAPSULA_DE_LA_MEMORIA", "Lote_01_al_20")

# Importar la lista de items base
sys.path.append(os.path.join(BASE_DIR, "00. SCRIPTS_PYTHON"))
from actualizar_memoria_construcciones_historicas import MEM_NUEVOS_ITEMS, sanitize_filename

# Diccionario de Prompts de Visor Fotográfico Cinemático calibrados por época histórica
MUSIC_FLOW_PROMPTS = {
    3: {
        "estilo": "Música Palaciega Neoclásica • Siglo XVIII",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta recreación histórica que acabo de subir:\n"
            "1. Analiza la escena: la construcción neoclásica de la Puerta de Alcalá hacia 1776 (diseño de Francesco Sabatini para el rey Carlos III), los andamios de madera de pino, los canteros labrando granito de Colmenar y las carretas de bueyes en el camino rural del Retiro.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de época neoclásica española (siglo XVIII):\n"
            "   - ESTILO OBLIGATORIO: Aire solemne e ilustrado de la corte de Carlos III (estilo marcha militar dieciochesca con caja / tambor de granaderos, flauta o música palaciega de cámara dieciochesca).\n"
            "   - PROHIBIDO: Sonidos electrónicos modernos, violín pop íntimo, guitarras eléctricas o fanfarrias de Hollywood.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con un suave y lento movimiento cinemático (efecto Ken Burns).\n"
            "   - Música de la corte del siglo XVIII integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    4: {
        "estilo": "Música de Salón y Violín Íntimo • c. 1905",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía histórica que acabo de subir:\n"
            "1. Analiza la imagen: capta el ambiente madrileño de principios del siglo XX (c. 1905-1910) durante la construcción del Palacio de Comunicaciones en la Plaza de Cibeles (arquitectos Palacios y Otamendi), los primeros tranvías y la elegancia de la época.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de época:\n"
            "   - ESTILO OBLIGATORIO: Violín íntimo y piano clásico de salón de principios de siglo, pausado, nostálgico y muy emotivo.\n"
            "   - PROHIBIDO: Fanfarrias estruendosas, sintetizadores modernos o percusión pesada.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con un suave y lento movimiento cinemático (efecto Ken Burns).\n"
            "   - Música de salón de época integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    5: {
        "estilo": "Chotis Castizo de Organillo y Zarzuela • 1912",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía histórica que acabo de subir:\n"
            "1. Analiza la imagen: la gran demolición urbana y apertura de la Gran Vía de Madrid hacia 1912, apisonadoras de vapor, carretas de escombros y los primeros edificios modernos en construcción.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de época madrileña:\n"
            "   - ESTILO OBLIGATORIO: Chotis castizo de organillo tradicional o melodía alegre de zarzuela madrileña con piano de época y aire bullicioso callejero.\n"
            "   - PROHIBIDO: Música contemporánea, sintetizadores o ritmos electrónicos.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música castiza integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    6: {
        "estilo": "Canto Gregoriano Polifónico y Órgano Gótico • Siglo XV",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta recreación histórica que acabo de subir:\n"
            "1. Analiza la escena: la construcción medieval de la Catedral de Burgos en el siglo XV, el alzamiento de las agujas góticas caladas de Juan de Colonia y las grúas de rueda de pisar sobre el río Arlanzón.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) sacra y gótica:\n"
            "   - ESTILO OBLIGATORIO: Canto gregoriano polifónico medieval solemne, órgano gótico profundo y resonancia de piedra catedralicia.\n"
            "   - PROHIBIDO: Guitarras modernas, baterías, fanfarrias orquestales o electrónica.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Imagen centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Canto gregoriano integrado con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    7: {
        "estilo": "Polifonía Renacentista Española • Tomás Luis de Victoria (1575)",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta recreación histórica que acabo de subir:\n"
            "1. Analiza la escena: la construcción renacentista del Monasterio de El Escorial hacia 1575 (Juan de Herrera y Felipe II), los ingenios mecánicos de elevación de granito y la ladera de Guadarrama.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del Renacimiento español:\n"
            "   - ESTILO OBLIGATORIO: Polifonía sacra y cortesana renacentista (estilo Tomás Luis de Victoria), vihuela clásica y coro de cámara sereno y majestuoso.\n"
            "   - PROHIBIDO: Instrumentos modernos, orquestas estridentes o percusión de cine.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Imagen centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música renacentista integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    8: {
        "estilo": "Música Marcial y Solemne del Imperio Romano • Siglo I-II d.C.",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta recreación histórica que acabo de subir:\n"
            "1. Analiza la escena: la ingeniería romana levantando las arquerías dobles del Acueducto de Segovia (siglo I-II d.C.) sin argamasa mediante grúas trispastos y tenazas de hierro.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del Imperio Romano clásico:\n"
            "   - ESTILO OBLIGATORIO: Aire solemne y marcial romano, viento de bronce antiguo (cornu / buccina), tambores lentos de legión y atmósfera de gran obra imperial.\n"
            "   - PROHIBIDO: Melodías pop, violines modernos o sintetizadores.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Imagen centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música romana integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    9: {
        "estilo": "Vals Romántico Decimonónico y Arpa • 1887",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía histórica que acabo de subir:\n"
            "1. Analiza la imagen: el montaje de la estructura ligera de hierro fundido curvado y láminas de cristal en el Parque del Retiro de Madrid (1887, Ricardo Velázquez Bosco) sobre el estanque.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del romanticismo decimonónico:\n"
            "   - ESTILO OBLIGATORIO: Vals romántico de salón decimonónico (estilo época alfonsina de 1880), arpa cristalina, flauta dulce y sección de violines líricos y elegantes.\n"
            "   - PROHIBIDO: Ritmos pesados, percusión moderna o electrónica.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Vals decimonónico integrado con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    10: {
        "estilo": "Marcha Sinfónica del Vapor y Ferrocarril • c. 1890",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía histórica que acabo de subir:\n"
            "1. Analiza la imagen: el montaje de la gran marquesina de hierro de 152 metros en la Estación de Atocha hacia 1890 (Alberto de Palacio), remachadores y locomotoras de vapor primitivas.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de la Revolución Industrial ferroviaria:\n"
            "   - ESTILO OBLIGATORIO: Marcha sinfónica del ferrocarril a vapor de finales del siglo XIX, ritmo constante y majestuoso de tren, cuerdas enérgicas y sensación de viaje hacia el progreso.\n"
            "   - PROHIBIDO: Sintetizadores electrónicos o baterías modernas.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Marcha de vapor integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    11: {
        "estilo": "Folk Marinero e Industrial Vasco • 1892",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía histórica que acabo de subir:\n"
            "1. Analiza la imagen: la construcción del Puente Colgante de Vizcaya en 1892 (Alberto de Palacio y Arnodin), las torres de 61 metros sobre la ría del Nervión y el tendido de cables de acero.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) marinera e industrial vasca de época:\n"
            "   - ESTILO OBLIGATORIO: Folk acústico vasco de finales del siglo XIX, acordeón tradicional melancólico, flauta de viento marina y oleaje de cuerda sinfónica de la ría industrial.\n"
            "   - PROHIBIDO: Música electrónica, pop o fanfarrias estridentes.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música de la ría integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    12: {
        "estilo": "Obertura de Ópera Romántica Clásica • c. 1845",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta recreación histórica que acabo de subir:\n"
            "1. Analiza la imagen: la construcción del Teatro Real de Madrid frente al Palacio Real en la década de 1840, muros de granito y cerchas de madera para la caja escénica en la Plaza de Oriente.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de ópera clásica decimonónica:\n"
            "   - ESTILO OBLIGATORIO: Obertura de ópera romántica clásica (estilo Bel Canto de mediados del siglo XIX), metales nobles, cuerdas virtuosas y un vals solemne de butaca de terciopelo.\n"
            "   - PROHIBIDO: Pop moderno, sintetizadores o ritmos electrónicos.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Imagen centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Obertura operística integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    13: {
        "estilo": "Poema Místico y Campanas Etéreas • c. 1915",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía histórica que acabo de subir:\n"
            "1. Analiza la imagen: la construcción de la Fachada del Nacimiento de la Sagrada Familia hacia 1915 con Antoni Gaudí en persona dirigiendo la obra entre los campos del Ensanche barcelonés.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del modernismo místico catalán:\n"
            "   - ESTILO OBLIGATORIO: Poema sonoro místico y lírico de principios del siglo XX, cuerdas contemplativas, campanas tubulares etéreas y violonchelo solista cantando a las esculturas de piedra viva.\n"
            "   - PROHIBIDO: Fanfarrias comerciales, música electrónica o percusión de cine de acción.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Poema místico integrado con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    14: {
        "estilo": "Melodía Decimonónica Madrileña para Celosía de Hierro • 1874",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía histórica que acabo de subir:\n"
            "1. Analiza la imagen: la construcción de la celosía metálica del primer Viaducto de Segovia en Madrid (1874, Eugenio Barrón), salvando la profunda hondonada sobre las casas bajas tradicionales.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) madrileña decimonónica:\n"
            "   - ESTILO OBLIGATORIO: Melodía madrileña decimonónica sobria y nostálgica, cuerda dramática de época, guitarra clásica española y aire solemne de gran puente de hierro forjado.\n"
            "   - PROHIBIDO: Sintetizadores modernos, efectos digitales o fanfarrias estridentes.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música decimonónica integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    },
    15: {
        "estilo": "Swing y Big Band Elegante de Posguerra • Años 50",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía histórica que acabo de subir:\n"
            "1. Analiza la imagen: la construcción en hormigón armado del Edificio España y la Torre de Madrid en los años 50 (hermanos Otamendi), grúas torre y el nacimiento del skyline moderno de Madrid.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de los años 50:\n"
            "   - ESTILO OBLIGATORIO: Orquesta de posguerra española, swing clásico y big band elegante de los años 50, saxofón tenor aterciopelado con sordina, piano de club acústico y contrabajo suave.\n"
            "   - PROHIBIDO: Música contemporánea, electrónica o sintetizadores modernos.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Swing de los años 50 integrado con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        )
    }
}

def escape_pdf_text(text):
    text = str(text)
    text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    replacements = {
        'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
        'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
        'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
        'ï': '\xef', 'Ï': '\xcf',
        '«': '<<', '»': '>>', '•': '-', '—': '-', '–': '-', '…': '...',
        'º': '\xba', 'ª': '\xaa', '¿': '\xbf', '¡': '\xa1',
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

class RobustNativePDFWriter:
    def __init__(self, page_width=612.0, page_height=792.0): # Letter estándar
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

    def draw_text(self, x, y, text, font="F1", size=10, r=0, g=0, b=0):
        self.set_fill_color(r, g, b)
        escaped = escape_pdf_text(text)
        self.current_stream.append(f"BT /{font} {size:.1f} Tf {x:.2f} {y:.2f} Td ({escaped}) Tj ET\n")

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

        kids_str = " ".join([f"{idx} 0 R" for idx in page_obj_indices])
        pages_dict = f"<< /Type /Pages /Kids [{kids_str}] /Count {len(self.pages)} >>".encode("ascii")

        # Configuración estándar con /Encoding /WinAnsiEncoding para renderizar perfectamente todos los acentos en español
        all_objs = [
            b"<< /Type /Catalog /Pages 2 0 R >>",
            pages_dict,
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>",
        ]

        for i, page_stream in enumerate(self.pages):
            content_idx = content_obj_indices[i]
            p_obj = (
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.w} {self.h}] "
                f"/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> "
                f"/Contents {content_idx} 0 R >>"
            ).encode("ascii")
            all_objs.append(p_obj)

            s_bytes = page_stream.encode("latin1", errors="replace")
            c_obj = f"<< /Length {len(s_bytes)} >>\nstream\n".encode("ascii") + s_bytes + b"\nendstream"
            all_objs.append(c_obj)

        with open(filename, "wb") as f:
            f.write(b"%PDF-1.4\n")
            offsets = []
            cur_offset = f.tell()

            for i, obj in enumerate(all_objs):
                offsets.append(cur_offset)
                obj_num = i + 1
                f.write(f"{obj_num} 0 obj\n".encode("ascii"))
                f.write(obj)
                f.write(b"\nendobj\n")
                cur_offset = f.tell()

            xref_offset = cur_offset
            f.write(b"xref\n")
            f.write(f"0 {len(all_objs) + 1}\n".encode("ascii"))
            f.write(b"0000000000 65535 f \n")
            for off in offsets:
                f.write(f"{off:010d} 00000 n \n".encode("ascii"))

            f.write(b"trailer\n")
            f.write(f"<< /Size {len(all_objs) + 1} /Root 1 0 R >>\n".encode("ascii"))
            f.write(b"startxref\n")
            f.write(f"{xref_offset}\n".encode("ascii"))
            f.write(b"%%EOF\n")

def create_mem_flow_music_pdf(output_path, item):
    writer = RobustNativePDFWriter(page_width=612.0, page_height=792.0) # Letter
    margin_x = 40.0
    content_w = writer.w - (margin_x * 2) # 532.0 pt

    writer.start_page()

    # Barra superior dorada / ámbar
    writer.set_fill_color(0.72, 0.53, 0.04) # Oro viejo / ámbar #B8860B
    writer.rect(margin_x, writer.h - 24, content_w, 3.5, fill=True, stroke=False)

    y = writer.h - 42
    writer.draw_text(margin_x, y, "CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", "F2", 8.2, 0.72, 0.53, 0.04)
    y -= 13
    writer.draw_text(margin_x, y, "BLOQUE 13: CÁPSULA DE LA MEMORIA [MEM] • GRANDES OBRAS Y VISOR CINEMÁTICO", "F2", 10.0, 0.1, 0.05, 0.2)
    y -= 8

    writer.set_stroke_color(0.72, 0.53, 0.04)
    writer.set_line_width(1.2)
    writer.line(margin_x, y, margin_x + content_w, y)
    y -= 15

    # Título del Ítem
    writer.draw_text(margin_x, y, f"{item['id_code']} {item['titulo_completo']}", "F2", 11.2, 0.1, 0.05, 0.2)
    y -= 13
    writer.draw_text(margin_x, y, f"Patrimonio Histórico: {item['lugar_epoca']}", "F3", 8.5, 0.45, 0.45, 0.45)
    y -= 14

    # 1. Contexto Histórico
    writer.draw_text(margin_x, y, "Objetivo Didáctico y Contexto Histórico:", "F2", 8.8, 0.72, 0.53, 0.04)
    y -= 11
    for line in wrap_text(item['concepto'], 96):
        writer.draw_text(margin_x, y, line, "F1", 8.2, 0.18, 0.22, 0.28)
        y -= 10.5

    y -= 4

    # 2. Paso 1: Generar la Recreación Histórica con IA (Gemini)
    writer.draw_text(margin_x, y, "Paso 1: Recrear la Escena de Construcción con IA en Gemini (gemini.google.com)", "F2", 8.8, 0.72, 0.53, 0.04)
    y -= 8

    p_lines = wrap_text(f'"{item["prompt"]}"', 92)
    prompt_box_h = 18 + (len(p_lines) * 10.0)

    writer.set_fill_color(0.98, 0.96, 0.91) # Crema / pergamino claro
    writer.set_stroke_color(0.72, 0.53, 0.04)
    writer.set_line_width(1.0)
    writer.rect(margin_x, y - prompt_box_h, content_w, prompt_box_h, fill=True, stroke=True)

    ty = y - 11
    writer.draw_text(margin_x + 8, ty, "Copia este prompt exacto y pégalo en Gemini Web para generar la imagen documental:", "F2", 7.8, 0.1, 0.05, 0.2)
    ty -= 11.0
    for pl in p_lines:
        writer.draw_text(margin_x + 8, ty, pl, "F3", 7.4, 0.1, 0.05, 0.2)
        ty -= 10.0

    y -= (prompt_box_h + 9)

    # 3. Paso 2: Reto y Preguntas de Investigación con Gemini
    writer.draw_text(margin_x, y, "Paso 2: Preguntas de Ingeniería y Vida Cotidiana para el Diálogo con Gemini", "F2", 8.8, 0.72, 0.53, 0.04)
    y -= 8

    q1_lines = wrap_text(f"1. Ingeniería de época: {item['pregunta1']}", 92)
    q2_lines = wrap_text(f"2. Entorno y vida cotidiana: {item['pregunta2']}", 92)
    tips_box_h = 18 + ((len(q1_lines) + len(q2_lines)) * 10.0) + 4

    writer.set_fill_color(1.0, 1.0, 1.0)
    writer.set_stroke_color(0.72, 0.53, 0.04)
    writer.set_line_width(1.0)
    writer.rect(margin_x, y - tips_box_h, content_w, tips_box_h, fill=True, stroke=True)

    ty = y - 11
    writer.draw_text(margin_x + 8, ty, "Escribe o dicta por voz estas dos preguntas a Gemini tras observar la imagen:", "F2", 7.8, 0.72, 0.53, 0.04)
    ty -= 11.5
    for ql in q1_lines:
        writer.draw_text(margin_x + 8, ty, ql, "F1", 7.4, 0.15, 0.2, 0.26)
        ty -= 10.0
    ty -= 2.5
    for ql in q2_lines:
        writer.draw_text(margin_x + 8, ty, ql, "F1", 7.4, 0.15, 0.2, 0.26)
        ty -= 10.0

    y -= (tips_box_h + 9)

    # 4. Paso 3: Visor Fotográfico Cinemático y Postal Sonora en Gemini (Canvas / Vista Previa)
    music_info = MUSIC_FLOW_PROMPTS.get(item['num'], {
        "estilo": "Música Histórica de Época",
        "prompt_canvas": (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía histórica que acabo de subir:\n"
            "1. Analiza la época y el entorno arquitectónico de la escena.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) adaptada al 100% a la época histórica.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa / Canvas) un Visor Fotográfico Cinemático con efecto Ken Burns y música integrada."
        )
    })

    writer.draw_text(margin_x, y, "Paso 3: Visor Fotográfico Cinemático y Postal Sonora en Gemini (Canvas / Vista Previa)", "F2", 8.8, 0.72, 0.53, 0.04)
    y -= 8

    m_prompt = music_info["prompt_canvas"]
    m_lines = wrap_text(m_prompt, 92)
    music_box_h = 20 + (len(m_lines) * 9.6) + 14

    writer.set_fill_color(0.96, 0.98, 1.0) # Azul suave tenue
    writer.set_stroke_color(0.2, 0.45, 0.8) # Azul medio
    writer.set_line_width(1.0)
    writer.rect(margin_x, y - music_box_h, content_w, music_box_h, fill=True, stroke=True)

    ty = y - 11
    writer.draw_text(margin_x + 8, ty, f"Descarga la imagen del Paso 1, súbela a Gemini y copia este prompt ({music_info['estilo']}):", "F2", 7.8, 0.1, 0.25, 0.6)
    ty -= 11.0
    for ml in m_lines:
        writer.draw_text(margin_x + 8, ty, ml, "F3", 7.2, 0.05, 0.15, 0.35)
        ty -= 9.6
    ty -= 2.5
    writer.draw_text(margin_x + 8, ty, "Consejo: En el visor puedes pulsar 'Publish' arriba a la derecha en Gemini para compartir el enlace del visor por WhatsApp.", "F1", 7.0, 0.35, 0.4, 0.45)

    y -= (music_box_h + 8)

    # Pie de página
    writer.set_stroke_color(0.85, 0.88, 0.92)
    writer.set_line_width(0.6)
    writer.line(margin_x, 26, margin_x + content_w, 26)
    writer.draw_text(margin_x, 16, f"Curso de Inteligencia Artificial para Seniors • Sesión {item['num']:02d} • {item['id_code']} {item['titulo_corto']} • Visor Cinemático", "F1", 7.4, 0.45, 0.48, 0.52)
    writer.draw_text(margin_x + content_w - 180, 16, "Patrimonio Histórico y Técnico de España", "F2", 7.4, 0.72, 0.53, 0.04)

    writer.end_page()
    writer.write_to_file(output_path)

def update_all_mem_pdfs():
    print("=== [1] ACTUALIZANDO FICHAS MEM CON VISOR CINEMÁTICO HISTÓRICO Y WINANSI COMPLETO ===")
    for item in MEM_NUEVOS_ITEMS:
        num = item['num']
        session_folder = f"{num:02d}_Sesion"
        session_path = os.path.join(SESSIONS_DIR, session_folder)

        safe_title = sanitize_filename(item['titulo_completo'])
        pdf_name = f"14. {item['id_code']}_{safe_title}.pdf"

        # 1. Guardar en carpeta de sesión
        if os.path.exists(session_path):
            session_pdf = os.path.join(session_path, pdf_name)
            create_mem_flow_music_pdf(session_pdf, item)
            print(f"  [S{num:02d}] Generado (WinAnsi OK): {pdf_name}")

        # 2. Guardar en bloque Lote_01_al_20
        lote_pdf_name = f"{item['id_code'][1:-1]}_{safe_title}.pdf"
        lote_pdf = os.path.join(MEM_DIR_LOTE1, lote_pdf_name)
        create_mem_flow_music_pdf(lote_pdf, item)

def renumber_and_clean_map(map_path, session_num):
    with open(map_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Patrón para identificar los números de archivo en las tarjetas
    pattern = r'<span class="file-num">#([^\s<]+)(\s*\[[^\]]+\])?</span>'
    
    matches = list(re.finditer(pattern, html))
    if not matches:
        return

    # Renumerar secuencialmente 1..N
    new_html = html
    for idx in range(len(matches) - 1, -1, -1):
        m = matches[idx]
        tag = m.group(2) or ""
        target_num = idx + 1
        new_card_str = f'<span class="file-num">#{target_num:02d}{tag}</span>'
        new_html = new_html[:m.start()] + new_card_str + new_html[m.end():]

    # Actualizar títulos de contador si existen
    total_cards = len(matches)
    new_html = re.sub(
        r'Itinerario Formativo Completo • \d+ Recursos Guiados',
        f'Itinerario Formativo Completo • {total_cards} Recursos Guiados',
        new_html
    )

    with open(map_path, "w", encoding="utf-8") as f:
        f.write(new_html)

    xx_count = len(re.findall(r'#XX', new_html))
    print(f"  [{os.path.basename(map_path)}] {total_cards} tarjetas renumeradas. Restantes #XX: {xx_count}")

def update_all_maps():
    print("\n=== [2] RENUMERANDO MAPAS INTERACTIVOS (SESIONES 03 A 15) ===")
    for num in range(3, 16):
        session_folder = f"{num:02d}_Sesion"
        session_path = os.path.join(SESSIONS_DIR, session_folder)
        if not os.path.exists(session_path):
            continue

        for mf_name in [f"MAPA_SESION_{num:02d}.html", f"MAPA_CLASE_SESION_{num:02d}.html"]:
            mf_path = os.path.join(session_path, mf_name)
            if os.path.exists(mf_path):
                renumber_and_clean_map(mf_path, num)

def main():
    update_all_mem_pdfs()
    update_all_maps()
    print("\n[OK] Actualización completada con éxito.")

if __name__ == "__main__":
    main()
