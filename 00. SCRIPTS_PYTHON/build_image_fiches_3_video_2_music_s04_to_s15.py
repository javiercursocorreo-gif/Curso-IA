#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_image_fiches_3_video_2_music_s04_to_s15.py
Compilación Oficial de Fichas de Imagen con Distribución 3/2 en Sesiones 04 a 15:
- 3 Fichas con VÍDEO FLOW (Consumo controlado de 30 créditos/día = 3 clips).
- 2 Fichas con GOOGLE FLOW MUSIC (Banda sonora a medida + Visor Fotográfico Cinemático Ken Burns y exportación .html).
- Actualización de todos los mapas interactivos (MAPA_SESION_XX.html y MAPA_CLASE_SESION_XX.html).
- Sincronización completa de los 60 PDFs en los bloques oficiales 02, 03, 05, 06 y 08.
"""

import os
import re
import sys
import shutil

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SESSIONS_DIR = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
BLOCKS_BASE = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF")

BLOCK_DIRS = {
    'EST': os.path.join(BLOCKS_BASE, "02. [EST] BLOQUE_2_ESTILOS_DE_IMAGEN_IA", "Lote_01_al_20"),
    'PRAC': os.path.join(BLOCKS_BASE, "03. [PRAC] BLOQUE_3_TALLERES_DE_PROMPTS_PRACTICOS", "Lote_01_al_20"),
    'INT': os.path.join(BLOCKS_BASE, "05. [INT] BLOQUE_5_MUNDO_POR_DENTRO_Y_RECONSTRUCCION", "Lote_01_al_20"),
    'FUT': os.path.join(BLOCKS_BASE, "06. [FUT] BLOQUE_6_INFOGRAFIAS_DEL_FUTURO_SCI_FI", "Lote_01_al_20"),
    'ARTE': os.path.join(BLOCKS_BASE, "08. [ARTE] BLOQUE_8_CUADROS_MAS_FAMOSOS_DE_LA_HISTORIA", "Lote_01_al_20")
}

def escape_pdf_text(text):
    text = str(text)
    text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    replacements = {
        'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
        'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
        'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
        '«': '<<', '»': '>>', '•': '-', '—': '-', '–': '-',
        'º': 'o', 'ª': 'a', '¿': '\xbf', '¡': '\xa1',
        '➔': '->', '→': '->', '’': "'", '‘': "'", '“': '"', '”': '"', '…': '...'
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
    def __init__(self, page_width=612.0, page_height=792.0):
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

# ==============================================================================
# CATÁLOGO DE LAS 60 FICHAS DE IMAGEN CON REPARTO 3/2 (SESIONES 04 A 15)
# ==============================================================================
ALL_ITEMS = [
    # ---------------- SESION 04 ----------------
    {
        'session': 4, 'tag': 'EST-004', 'prefix': '2. EST-004',
        'title': 'Estilo Impresionista y Oleo: Campo de Amapolas (Monet)',
        'desc': 'Pinceladas sueltas, colores vibrantes y enfasis en la luz natural y el aire libre, inspirado en las grandes obras paisajisticas de Claude Monet y el postimpresionismo frances.',
        'prompt_gemini': '"Pintura al oleo de un campo de amapolas silvestres bajo un cielo nublado, estilo impresionista similar a Monet, pinceladas sueltas y gruesas, textura de lienzo visible, colores vivos y luz natural al atardecer. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling lateral lento y suave a traves del campo de amapolas. El viento mece suavemente las flores rojas y la hierba silvestre, mientras las nubes se desplazan lentamente en el cielo al atardecer. Estetica de pintura al oleo viva con luz constante."',
        'color': (0.3, 0.4, 0.85)
    },
    {
        'session': 4, 'tag': 'PRAC-004', 'prefix': '3. PRAC-004',
        'title': 'Viaje en el Tiempo: Volver a la Juventud en los Anos 60 / Epoca Dorada',
        'desc': 'Transportar tu fotografia o recuerdo a la estetica, vestuario y optimismo de los anos 60 o 70, frente a un escenario clasico de epoca y con iluminacion cinematografica calida.',
        'prompt_gemini': '"Fotografia realista de epoca en blanco y negro o color calido de los anos 60: retrato sonriente de una persona joven vestida con moda clasica de la decada, en una cafeteria vintage o avenida transitada con coches de la epoca al fondo. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Balada Pop Acústica Nostálgica • Años 60',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta imagen que acabo de subir:\n"
            "1. Analiza la imagen: el retrato juvenil, la moda clásica y la atmósfera dorada y optimista de los años 60.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de la década de 1960:\n"
            "   - ESTILO OBLIGATORIO: Balada pop acústica de los años 60, guitarra dulce de 12 cuerdas, piano cálido y melodía nostálgica y entrañable.\n"
            "   - PROHIBIDO: Sintetizadores electrónicos modernos o ritmos acelerados de pop comercial.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música de los años 60 integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.85, 0.45, 0.15)
    },
    {
        'session': 4, 'tag': 'INT-004', 'prefix': '5. INT-004',
        'title': 'Corte del Transbordador Espacial en Orbita con Bodega Abierta y Brazo Canadarm',
        'desc': 'La iconica nave reutilizable de la NASA por dentro: cabina de dos cubiertas para astronautas, bodega de carga y el brazo mecanico Canadarm desplegado sobre la curvatura de la Tierra.',
        'prompt_gemini': '"Infografia y corte transversal 3D de un Transbordador Espacial de la NASA orbitando la Tierra: bodega de carga abierta con un satelite de comunicaciones desplegado por el brazo Canadarm. Fondo de la curvatura azul de la Tierra y estrellas brillantes. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Plano orbital cinematico alejandose suavemente del transbordador espacial. El brazo Canadarm sostiene el satelite en gravedad cero mientras la Tierra gira majestuosamente y en silencio en el horizonte azul."',
        'color': (0.1, 0.55, 0.65)
    },
    {
        'session': 4, 'tag': 'FUT-004', 'prefix': '6. FUT-004',
        'title': 'Ano 2035: Terapia Genica Personalizada y Medicina Molecular de Precision',
        'desc': 'La era de la medicina molecular de precision: nanosensores inteligentes y terapias celulares que detectan anomalias a nivel sanguineo y de ADN antes de que aparezcan sintomas clinicos.',
        'prompt_gemini': '"Infografia biomedica 3D cientifica y esperanzadora sobre la medicina del ano 2035: celula humana iluminada donde hebras de ADN son reparadas por nanosensores microscopicos luminosos que liberan terapia genica de precision. Fondo azul medico de alta tecnologia. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Camara lenta microscopica navegando por el espacio celular. Las hebras de ADN brillan con pulsos suaves de luz dorada y los nanosensores se desplazan con movimiento suave y constante en un entorno biomedico de alta definicion."',
        'color': (0.15, 0.6, 0.4)
    },
    {
        'session': 4, 'tag': 'ARTE-004', 'prefix': '8. ARTE-004',
        'title': 'El Nacimiento de Venus de Sandro Botticelli (1485)',
        'desc': 'La obra cumbre del Renacimiento florentino en la Galeria Uffizi: la diosa del amor y la belleza emerge de las aguas sobre una concha gigante impulsada por el viento divino de los cefiros.',
        'prompt_gemini': '"Ilustracion clasica y recreacion pictorica luminosa del Nacimiento de Venus de Botticelli: Venus de pie sobre una gran concha marina dorada sobre el mar turquesa, el dios Cefiro soplando rosas flotantes y la ninfa Primavera ofreciendo un manto floreado. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Música Renacentista Florentina • Siglo XV',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la escena: el cuadro 'El Nacimiento de Venus' de Sandro Botticelli (1485), la concha marina dorada, el oleaje turquesa suave y las rosas sopladas por Céfiro.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del Renacimiento italiano:\n"
            "   - ESTILO OBLIGATORIO: Música de corte renacentista toscana, flauta dulce pastoril, laúd sereno y arpa delicada con aire primaveral luminoso.\n"
            "   - PROHIBIDO: Guitarras eléctricas, sintetizadores modernos o fanfarrias orquestales pesadas.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Pintura centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música renacentista integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.6, 0.3, 0.7)
    },

    # ---------------- SESION 05 ----------------
    {
        'session': 5, 'tag': 'EST-005', 'prefix': '2. EST-005',
        'title': 'Serie Carrusel: Monumentos de Madrid con Cielos de los 7 Grandes Maestros',
        'desc': 'Reinterpretar la arquitectura monumental de Madrid sustituyendo sus cielos por los estilos pictoricos de 7 genios universales (Van Gogh, Turner, Monet, Constable, Cezanne, Munch, Friedrich).',
        'prompt_gemini': '"Fotografia hiperrealista y pictorica de la Puerta de Alcala en Madrid al atardecer: el monumento de piedra clasica perfectamente iluminado, pero con un cielo dramatico inspirado en la Noche Estrellada de Van Gogh, con remolinos de oleo azul cobalto, amarillo dorado y pinceladas gruesas texturizadas. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling frontal lento y cinematico acercandose a la Puerta de Alcala. Los remolinos de nubes en el cielo de oleo giran con movimiento hipnotico y sutil, mientras las luces calidas de las farolas en la base parpadean suavemente sobre los adoquines de Madrid."',
        'color': (0.2, 0.45, 0.8)
    },
    {
        'session': 5, 'tag': 'PRAC-005', 'prefix': '3. PRAC-005',
        'title': 'Eliminacion de Objetos o Personas Molestos (Fotografia Practica)',
        'desc': 'Limpieza digital de fotografias turisticas o familiares mediante IA (Generative Inpainting). Aprender a eliminar turistas de fondo, cables de electricidad o papeleras para dejar un encuadre limpio y diafano.',
        'prompt_gemini': '"Fotografia turistica antes y despues: en el lado izquierdo una plaza historica con turistas cruzando y cables de luz; en el lado derecho la misma plaza perfectamente limpia, despejada y soleada, con arquitectura nitida y suelo empedrado impecable. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Paneo horizontal lento barriendo de izquierda a derecha la plaza historica. Las palomas revolotean suavemente sobre la fuente de piedra central y la brisa mece las sombras de los soportales en una manana serena y despejada."',
        'color': (0.85, 0.45, 0.15)
    },
    {
        'session': 5, 'tag': 'INT-005', 'prefix': '5. INT-005',
        'title': 'El Partenon de Atenas a Todo Color con la Colosal Estatua de Atenea',
        'desc': 'Reconstruccion arqueologica hiperrealista del interior de la Acropolis de Atenas en el siglo V a.C.: templos policromados albergando la colosal estatua de Atenea Partenos de 12 metros de oro y marfil.',
        'prompt_gemini': '"Reconstruccion arqueologica hiperrealista del interior del Partenon de Atenas en el ano 438 a.C.: columnas de marmol policromadas en rojo y azul egipcio, pebeteros de bronce con humo aromatico y la colosal estatua crisoelefantina de Atenea de 12 metros de altura en oro resplandeciente y marfil. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Música Griega Clásica Solemne • Siglo V a.C.',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta reconstrucción arqueológica que acabo de subir:\n"
            "1. Analiza la escena: el interior policromado del Partenón de Atenas, la colosal estatua criselefantina de Atenea Partenos en oro y marfil y los pebeteros de bronce humeantes.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de la Grecia clásica antigua:\n"
            "   - ESTILO OBLIGATORIO: Aire sagrado y solemne de la Acrópolis clásica, lira griega de cuerda pulsada, flauta aulos suave y coro modal majestuoso.\n"
            "   - PROHIBIDO: Guitarras modernas, baterías, sintetizadores o fanfarrias de tráiler.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Reconstrucción centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música griega solemne integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.1, 0.55, 0.65)
    },
    {
        'session': 5, 'tag': 'FUT-005', 'prefix': '6. FUT-005',
        'title': 'Ano 2038: Redes Electricas Inteligentes Cuanticas y Reactores Modulares SMR',
        'desc': 'La revolucion energetica limpia y descentralizada de la proxima decada: reactores modulares SMR compactos y seguros, conectados a micro-redes inteligentes gestionadas por computacion cuantica.',
        'prompt_gemini': '"Infografia cientifica 3D futurista sobre la energia del ano 2038: corte transversal de un reactor modular SMR compacto y seguro en un entorno suburbano limpio, conectado mediante cables subterraneos luminosos a una red electrica inteligente cuantica. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Camara orbital lenta alrededor del complejo energetico modular. Los pulsos luminosos de energia azulada viajan por las lineas subterraneas conectando cada edificio de la ciudad ecologica, con turbinas de vapor girando en silencio y cielo diafano."',
        'color': (0.15, 0.6, 0.4)
    },
    {
        'session': 5, 'tag': 'ARTE-005', 'prefix': '8. ARTE-005',
        'title': 'La Primavera de Sandro Botticelli (1482)',
        'desc': 'Obra cumbre de la mitologia renacentista en la Florencia de los Medici: el jardin idilico de naranjos donde nueve figuras mitologicas celebran el renacer de la vida y el humanismo.',
        'prompt_gemini': '"Ilustracion y recreacion artistica hiperrealista de La Primavera de Sandro Botticelli (1482): jardin renacentista de naranjos con frutos dorados, Venus en el centro vestida de blanco, las Tres Gracias danzando en velos traslucidos y la ninfa Flora esparciendo rosas silvestres. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Madrigal Renacentista Primaveral • c. 1482',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la imagen: 'La Primavera' de Sandro Botticelli, el jardín de naranjos dorados, la danza de las Tres Gracias y la ninfa Flora esparciendo rosas silvestres.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) renacentista florentina:\n"
            "   - ESTILO OBLIGATORIO: Madrigal renacentista alegre y lírico, flautas de madera dulces, laúd pulsado y viola de brazo celebrando la llegada de la primavera toscana.\n"
            "   - PROHIBIDO: Música pop contemporánea, sintetizadores o percusión de cine de acción.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Cuadro centrado en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Madrigal primaveral integrado con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.6, 0.3, 0.7)
    },

    # ---------------- SESION 06 ----------------
    {
        'session': 6, 'tag': 'EST-006', 'prefix': '2. EST-006',
        'title': 'Serie Carrusel Magistral: La Puerta de San Vicente bajo 9 Genios del Arte',
        'desc': 'Reinterpretar la historica Puerta de San Vicente de Madrid fusionando su arquitectura clasica con las paletas, luces y texturas de 9 genios de la pintura (Goya, Sorolla, Velazquez, Monet, Van Gogh, El Greco, Turner, Cezanne, Friedrich).',
        'prompt_gemini': '"Recreacion pictorica magistral de la Puerta de San Vicente de Madrid en 1787: composicion clasica basada en el oleo de Gines Andres de Aguirre, con carruajes de caballos y damas con mantilla cruzando el arco de piedra, pero reinterpretada con la luz vibrante del mar mediterraneo y pinceladas luminosas al estilo de Joaquin Sorolla. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling frontal suave y cinematico avanzando hacia la Puerta de San Vicente. La luz dorada del sol resplandece sobre la piedra caliza, los caballos tiran suavemente del carruaje de epoca y los vestidos de las damas se mecen con una brisa tenue en una manana madrilena llena de vida."',
        'color': (0.2, 0.45, 0.8)
    },
    {
        'session': 6, 'tag': 'PRAC-006', 'prefix': '3. PRAC-006',
        'title': 'Vestuario de Alta Costura o Gala para la Alfombra Roja (Fotografia Practica)',
        'desc': 'Transformacion estetica de retratos cotidianos en vestidos de noche o esmoquines de alta costura disenados para festivales internacionales de cine (Cannes, San Sebastian, Venecia).',
        'prompt_gemini': '"Fotografia editorial de alfombra roja de festival de cine: retrato elegante de una persona madura vestida con un impecable esmoquin negro a medida o vestido de gala de terciopelo azul noche con bordados discretos de hilo de plata, sonriendo con distincion ante los focos suaves. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Sinfonía Clásica de Gala y Noche de Estreno • Cine Clásico',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía editorial que acabo de subir:\n"
            "1. Analiza la imagen: el retrato de gala sobre la alfombra roja, el terciopelo noble, la elegancia madura y el ambiente festivo de gran festival de cine.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) sinfónica y glamurosa:\n"
            "   - ESTILO OBLIGATORIO: Obertura sinfónica clásica de noche de estreno cinematográfico, sección de cuerdas nobles, piano virtuoso y aire distinguido de terciopelo y gala.\n"
            "   - PROHIBIDO: Música tecno, sintetizadores estridentes o ritmos urbanos pesados.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música de gala integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.85, 0.45, 0.15)
    },
    {
        'session': 6, 'tag': 'INT-006', 'prefix': '5. INT-006',
        'title': 'Reconstruccion del Mausoleo de Halicarnaso con Cuadriga de Marmol',
        'desc': 'Una de las Siete Maravillas del Mundo Antiguo: la colosal tumba del rey Mausolo de Caria con sus 45 metros de altura, 36 columnas jonicas y coronado por una cuadriga colosal de marmol blanco.',
        'prompt_gemini': '"Reconstruccion arqueologica hiperrealista del Mausoleo de Halicarnaso en su maximo esplendor (ano 350 a.C.): colosal monumento de 45 metros de altura en marmol blanco brillante junto al mar Egeo, rodeado de estatuas de leones y coronado por una piramide con la majestuosa cuadriga de cuatro caballos guiada por el rey Mausolo. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Plano aereo en semi-orbita cinematografica rodeando la cima del monumento. La gran cuadriga de marmol blanco se alza majestuosa contra el azul profundo del mar Egeo, las olas rompen suaves en la costa lejana y la luz dorada del atardecer resalta cada bajorrelieve esculpido."',
        'color': (0.1, 0.55, 0.65)
    },
    {
        'session': 6, 'tag': 'FUT-006', 'prefix': '6. FUT-006',
        'title': 'Ano 2040: Drones Urbanos de Pasajeros (eVTOL) y Aeropuertos en Azoteas',
        'desc': 'La movilidad urbana aerea en la proxima decada: aeronaves electricas de despegue y aterrizaje vertical (eVTOL) sin emisiones ni ruido que conectan azoteas y vertipuertos urbanos a 200 km/h.',
        'prompt_gemini': '"Infografia y render fotografico futurista de una metropolis europea en el ano 2040: vertipuerto ajardinado sobre la azotea de un rascacielos sostenible de madera y cristal, donde aterriza suavemente un dron taxi de pasajeros eVTOL electrico y silencioso con diseno aerodinamico blanco y cabina panoramica. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Descenso suave en camara lenta del dron de pasajeros eVTOL posandose con precision en el circulo luminoso del vertipuerto. Sus rotores electricos desaceleran en silencio, las puertas de cristal de la azotea se abren suavemente y el horizonte de la ciudad al atardecer refleja luces ecologicas tenues."',
        'color': (0.15, 0.6, 0.4)
    },
    {
        'session': 6, 'tag': 'ARTE-006', 'prefix': '8. ARTE-006',
        'title': 'La Escuela de Atenas de Rafael Sanzio (1511)',
        'desc': 'Fresco cumbre del Renacimiento en las Estancias Vaticanas: la gran asamblea del saber humano donde Platon senala al cielo y Aristoteles extiende su palma hacia la tierra, rodeados por sabios clasicos.',
        'prompt_gemini': '"Ilustracion y recreacion hiperrealista al fresco de La Escuela de Atenas de Rafael Sanzio (1511): monumental basilica renacentista de techos abovedados y esculturas clasicas de Apolo y Minerva, con Platon vestido de rojo senalando al cielo y Aristoteles vestido de azul con su libro de etica, debatiendo rodeados por filosofos clasicos en tunicas fluidas. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Polifonía Renacentista Sacra y Órgano de Salón • 1511',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la imagen: el fresco 'La Escuela de Atenas' de Rafael Sanzio (1511), la basílica clásica abovedada y el debate eterno entre Platón y Aristóteles.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del Alto Renacimiento italiano:\n"
            "   - ESTILO OBLIGATORIO: Polifonía sacra y académica renacentista (estilo Josquin des Prez), órgano de piedra noble, coro de cámara sereno y atmósfera de gran sabiduría inmortal.\n"
            "   - PROHIBIDO: Sonidos electrónicos, sintetizadores modernos o percusión de cine.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Pintura centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Polifonía clásica integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.6, 0.3, 0.7)
    },

    # ---------------- SESION 07 ----------------
    {
        'session': 7, 'tag': 'EST-007', 'prefix': '2. EST-007',
        'title': 'IMPRESIONISTA Y POST-IMPRESIONISTA - Klimt: Dama en Pan de Oro',
        'desc': 'Retrato modernista de la Secesion de Viena inspirado en Gustav Klimt: elegante dama con peinado recogido, mirada enigmatica y suntuosa tunica decorada con teselas, espirales doradas y patrones de pan de oro auténtico.',
        'prompt_gemini': '"Retrato pictorico fotorrealista al estilo de Gustav Klimt (Secesion de Viena): elegante dama de perfil sereno con peinado recogido y mantilla sutil, envuelta en una grandiosa tunica cubierta de mosaicos dorados, espirales de pan de oro reluciente y texturas bizantinas. Fondo de laminas de oro envejecido con relieves brillantes bajo luz calida de atardecer. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Vals Vienés Lírico y Arpa Modernista • Gustav Klimt',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la imagen: el retrato modernista de la Secesión de Viena al estilo de Gustav Klimt, las teselas de pan de oro relucientes y la atmósfera aristocrática de principios de siglo.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de la Viena finisecular (c. 1900):\n"
            "   - ESTILO OBLIGATORIO: Vals vienés lírico, arpa dorada, celesta luminosa y sección de violines íntimos y envolventes.\n"
            "   - PROHIBIDO: Guitarras modernas, baterías pesadas o electrónica.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Pintura centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Vals vienés integrado con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.8, 0.6, 0.1)
    },
    {
        'session': 7, 'tag': 'PRAC-007', 'prefix': '3. PRAC-007',
        'title': 'Protagonista de Cine Negro y Misterio Clasico (Film Noir)',
        'desc': 'Recreacion fotografica de cine clasico de los anos 40 y 50: iluminacion expresionista con claroscuro marcado (sombras de persiana veneciana), sombrero fedora, gabardina y lluvia fina.',
        'prompt_gemini': '"Retrato fotografico en blanco y negro de pelicula de cine negro clasico (anos 40): detective veterano con sombrero fedora inclinado y gabardina clasica, apoyado en una esquina de adoquines mojados. Luz lateral dura proyectando sombras de persiana veneciana sobre su rostro reflexivo y el humo tenue de una alcantarilla. Atmosfera de suspense y lluvia fina. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Jazz Noir Melancólico y Saxo Nocturno • Años 40',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía de cine clásico que acabo de subir:\n"
            "1. Analiza la imagen: la atmósfera de película de cine negro de los años 40, adoquines mojados bajo la lluvia, sombrero fedora y sombras de persiana veneciana.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de Film Noir:\n"
            "   - ESTILO OBLIGATORIO: Jazz noir melancólico y cinematográfico de los años 40, saxofón tenor solitario y nostálgico, contrabajo pausado y platillos con escobilla suave.\n"
            "   - PROHIBIDO: Melodías tecno, sintetizadores pop o ritmos bailables alegres.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía en blanco y negro centrada con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Jazz noir integrado con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.3, 0.35, 0.4)
    },
    {
        'session': 7, 'tag': 'INT-007', 'prefix': '5. INT-007',
        'title': 'El Faro de Alejandria (120 m) con su Gran Espejo de Bronce',
        'desc': 'Reconstruccion arqueologica del interior del Faro de Alejandria: la rampa helicoidal de piedra, el horno de fuego colosal y el gigantesco espejo paraboloide de bronce pulido que proyectaba luz a 50 km.',
        'prompt_gemini': '"Corte transversal e interior 3D hiperrealista del Faro de Alejandria en el ano 280 a.C.: en la cima, una gran fogata de lena aromatica arde con fuerza frente a un colosal espejo concavo de bronce bruñido que proyecta un haz de luz cegador sobre el mar Mediterraneo nocturno. Barcos antiguos navegando a lo lejos guiados por el destello. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Camara en vuelo de drone orbitando alrededor del fuego en la cima del faro. El gran espejo de bronce refleja las llamaradas danzantes mientras el haz de luz corta la noche estrellada sobre el oleaje del Mediterraneo."',
        'color': (0.15, 0.45, 0.75)
    },
    {
        'session': 7, 'tag': 'FUT-007', 'prefix': '6. FUT-007',
        'title': 'Ano 2042: Regeneracion de Organos 3D con Biotinta de Celulas Madre',
        'desc': 'Biomedicina regenerativa del futuro: bioimpresoras 3D de precision milimetrica fabricando corazones, rinones y valvulas biologicas utilizando celulas madre cultivadas del propio paciente.',
        'prompt_gemini': '"Infografia medica 3D hiperrealista en un quirofano del ano 2042: un brazo robotico de bioimpresion 3D deposita finas capas de biotinta translucida con celulas madre vivas para formar un corazon humano completo dentro de una camara de cultivo esteril con fluidos nutricionales luminiscentes. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Zoom in optico muy lento hacia la boquilla microscopica de la bioimpresora. La biotinta pulsa con luz bioelectrica azulada y el tejido celular recien formado comienza a latir suavemente dentro de la camara nutricional."',
        'color': (0.1, 0.6, 0.45)
    },
    {
        'session': 7, 'tag': 'ARTE-007', 'prefix': '8. ARTE-007',
        'title': 'El Hombre de Vitruvio de Leonardo da Vinci (1490)',
        'desc': 'El canon iconico de proporcion humana y conexion cosmica del Renacimiento: dibujo a pluma y tinta sepia sobre papel verjurado inscrito simultaneamente en un circulo y un cuadrado.',
        'prompt_gemini': '"Estudio renacentista fotorrealista del Hombre de Vitruvio de Leonardo da Vinci sobre papel verjurado antiguo con bordes desgastados y manchas de tinta sepia: trazos minuciosos a pluma mostrando la doble postura de brazos y piernas inscrita en el circulo y el cuadrado perfectos. Anotaciones caligraficas especulares invertidas en italiano renacentista. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Paneo diagonal suave recorriendo los trazos a pluma del dibujo desde el circulo exterior hasta el rostro sereno de la figura. Las sombras de la luz de vela tiemblan calidamente sobre la textura rugosa del papel antiguo."',
        'color': (0.55, 0.35, 0.15)
    },

    # ---------------- SESION 08 ----------------
    {
        'session': 8, 'tag': 'EST-008', 'prefix': '2. EST-008',
        'title': 'SURREALISTA - Relojes Blandos en el Desierto Onirico',
        'desc': 'Atmosfera de sueno inspirada en Salvador Dali: relojes de bolsillo de oro derritiendose sobre ramas secas de olivo y acantilados petreos de Cadaques, bajo un cielo infinito y solitario.',
        'prompt_gemini': '"Pintura surrealista al oleo fotorrealista al estilo de Salvador Dali: relojes de bolsillo dorados derritiendose suavemente como cera caliente sobre la rama de un arbol seco y sobre rocas pulidas de una playa solitaria. Al fondo, acantilados escarpados y un mar en calma absoluta bajo un cielo crepuscular de tonos dorados y violetas. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling frontal lento y pausado sobre la llanura desertica. Las manecillas del reloj blando giran suavemente en camara lenta mientras las sombras de los acantilados se alargan con la brisa tibia del crepusculo."',
        'color': (0.8, 0.45, 0.1)
    },
    {
        'session': 8, 'tag': 'PRAC-008', 'prefix': '3. PRAC-008',
        'title': 'Mi Vocacion Sonada: Director de Orquesta Sinfonica en el Auditorio',
        'desc': 'Cumplir el sueno fotografico de subirte al podio de una gran filarmonica: batuta en mano frente a 80 musicos, partitura abierta sobre el atril dorado y la emocion de dirigir un concierto magistral.',
        'prompt_gemini': '"Fotografia editorial nitida y solemne: persona mayor jubilada en el podio de director de una gran orquesta sinfonica en un auditorio majestuoso de madera noble y terciopelo rojo. Viste frac elegante, sostiene la batuta en alto con gesto apasionado mientras violinistas y chelistas le miran concentrados. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Obertura Sinfónica Clásica y Cuerdas Nobles • Filarmónica',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía editorial que acabo de subir:\n"
            "1. Analiza la imagen: el director en el podio de la orquesta sinfónica, la batuta en alto, el auditorio de madera noble y la concentración de los músicos.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) sinfónica clásica:\n"
            "   - ESTILO OBLIGATORIO: Gran obertura orquestal clásica, violines virtuosos al unísono, timbales solemnes y metales nobles con la majestuosidad de una sala de conciertos filarmónica.\n"
            "   - PROHIBIDO: Música tecno, sintetizadores modernos o pop.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Obertura sinfónica integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.2, 0.35, 0.6)
    },
    {
        'session': 8, 'tag': 'INT-008', 'prefix': '5. INT-008',
        'title': 'El Panteon de Roma por Dentro: Oculo Solar y Cupula de Hormigon',
        'desc': 'La cupula de hormigon no armado mas grande jamas construida: 43 metros de diametro con casetones y el magico oculo cenital abierto de 9 metros por donde entra un haz de luz solar.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista del interior del Panteon de Agripa en Roma al mediodia del equinoccio: un haz de luz solar solido y luminoso entra por el oculo circular de la gran cupula de casetones de hormigon aligerado, iluminando el pavimento de marmoles de colores. Visitantes contemplando la inmensidad del espacio con pebeteros encendidos. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Camara inclinada hacia arriba subiendo en travelling vertical por el cilindro del haz de luz solar hasta salir por el oculo al cielo azul romano, con motas de polvo dorado flotando en el rayo de luz."',
        'color': (0.65, 0.4, 0.15)
    },
    {
        'session': 8, 'tag': 'FUT-008', 'prefix': '6. FUT-008',
        'title': 'Ano 2045: Carne Cultivada Celular en Gastronomia Sostenible',
        'desc': 'La revolucion culinaria y etica del futuro: cortes selectos de carne wagyu y salmon producidos a partir de celulas madre en biorreactores alimentados por energias renovables sin sacrificio animal.',
        'prompt_gemini': '"Infografia gastronomica y tecnologica 3D: en un restaurante de alta cocina del ano 2045, un chef experto emplata un jugoso filete de ternera cultivada celular sobre pizarra negra con guarnicion de microvegetales hidroponicos. Al fondo, a traves de una mampara de cristal esteril, se aprecian elegantes biorreactores de acero pulido y luz ambiental calida. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling circular cercano alrededor del plato recien cocinado. El vapor aromatico se eleva suavemente del filete dorado al punto, mostrando el brillo de los jugos y la textura fibrosa perfecta."',
        'color': (0.75, 0.3, 0.2)
    },
    {
        'session': 8, 'tag': 'ARTE-008', 'prefix': '8. ARTE-008',
        'title': 'La Virgen del Prado de Rafael Sanzio (1506)',
        'desc': 'La composicion triangular perfecta de armonia renacentista: la Virgen Maria sentada en un prado florido de la campina toscana sosteniendo con ternura a Jesus nino y San Juanito.',
        'prompt_gemini': '"Recreacion pictorica clasica al oleo de La Virgen del Prado de Rafael Sanzio: composicion piramidal serena de la Virgen con manto azul ultramar y tunica roja carmin, velando los juegos de Jesus nino y San Juan Bautista nino entre amapolas y lirios silvestres. Paisaje toscano de suaves colinas y lago en calma bajo una luz diáfana y cristalina. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Música Sacra Renacentista Toscana • Rafael (1506)',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la imagen: 'La Virgen del Prado' de Rafael Sanzio (1506), la pradera toscana florida, el manto azul ultramar y la mirada serena y materna sobre el lago en calma.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) sacra renacentista italiana:\n"
            "   - ESTILO OBLIGATORIO: Polifonía sacra y dulce del Renacimiento toscano, viola da gamba serena, laúd punteado y arpa medieval de sonido cristalino.\n"
            "   - PROHIBIDO: Guitarras eléctricas, sintetizadores modernos o percusión de cine.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Pintura centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música sacra integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.15, 0.4, 0.7)
    },

    # ---------------- SESION 09 ----------------
    {
        'session': 9, 'tag': 'EST-009', 'prefix': '2. EST-009',
        'title': 'SURREALISTA - Cuadros en Ruinas Flotando en el Desierto',
        'desc': 'Misterio onirico y tiempo suspendido: marcos barrocos dorados flotando en el aire sobre una llanura desertica de arena fina, en cuyo interior se asoman mares y constelaciones.',
        'prompt_gemini': '"Pintura surrealista de estilo pictorico refinado: enormes marcos dorados barrocos flotan verticalmente en el aire sobre un desierto de arena blanca con dunas suaves. Cada marco funciona como una ventana magica a otra dimension (uno muestra una tormenta marina, otro una via lactea centelleante y otro un bosque verde). Sombras geometricas proyectadas en la arena. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Música Onírica y Éterea Surrealista • Atmósfera de Ensueño',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la escena: marcos dorados barrocos suspendidos en el desierto infinito, ventanas a otras dimensiones y tiempo onírico detenido.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de atmósfera mágica y surrealista:\n"
            "   - ESTILO OBLIGATORIO: Nocturno impresionista etéreo, piano acústico con reverberación de cristal, cuerdas misteriosas en pizzicato y arpa flotante.\n"
            "   - PROHIBIDO: Ritmos tecno, baterías pesadas o sintetizadores pop comerciales.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Pintura centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música onírica integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.85, 0.5, 0.15)
    },
    {
        'session': 9, 'tag': 'PRAC-009', 'prefix': '3. PRAC-009',
        'title': 'Reconstruccion Digital de Objetos y Fotos Rotas Familiares',
        'desc': 'Restauracion con IA generativa (Inpainting): recuperar una taza antigua de porcelana quebrada, un jarron de Talavera o una foto de boda rota, recomponiendo las partes que faltan.',
        'prompt_gemini': '"Fotografia antes y despues de restauracion patrimonial: en la mitad izquierda, un plato de ceramica de Talavera del siglo XIX quebrado en multiples pedazos con grietas visibles; en la mitad derecha, la misma pieza perfectamente reconstruida, con sus esmaltes azules y amarillos relucientes y superficie lisa impecable sobre fondo neutro de museo. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling frontal continuo mientras una linea de luz brillante barre de izquierda a derecha la ceramica rota, uniendo las piezas rotas en una transicion magica hasta dejarla impecable y brillante."',
        'color': (0.1, 0.5, 0.65)
    },
    {
        'session': 9, 'tag': 'INT-009', 'prefix': '5. INT-009',
        'title': 'Los Banos de Caracalla en Roma: Caldarium, Piscinas e Hipocausto',
        'desc': 'La monumentalidad termal de la Roma imperial: el gigantesco Caldarium circular con su cupula de 35 metros, piscinas de agua caliente bajo bovedas y los hornos subterraneos de hipocausto.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista de las Termas de Caracalla en el ano 216 d.C.: en el piso superior, la grandiosa piscina del caldarium con vapor de agua ascendiendo entre columnas corintias de granito rojo y mosaicos de atletas; en el subsuelo, laberinto de hornos de ladrillo donde el fuego del hipocausto calienta el suelo radiante. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling descendente desde el vapor relajante de las piscinas superiores hasta el brillo rojizo de los hornos subterraneos del hipocausto, revelando la colosal ingenieria termica romana."',
        'color': (0.7, 0.25, 0.1)
    },
    {
        'session': 9, 'tag': 'FUT-009', 'prefix': '6. FUT-009',
        'title': 'Ano 2050: La Base Lunar Artemis-Shackleton Permanente',
        'desc': 'El primer asentamiento humano permanente en el Polo Sur de la Luna: cupulas inflables cubiertas de regolito lunar impreso en 3D para frenar la radiacion y la Tierra azul en el horizonte.',
        'prompt_gemini': '"Infografia aeroespacial 3D fotorrealista de la base lunar permanente en el crater Shackleton en el ano 2050: modulos habitacionales conectados por tuneles presurizados, excavadoras roboticas depositando regolito lunar protector, astronautas con trajes ligeros recogiendo hielo en la sombra del crater y la Tierra azul resplandeciendo en el horizonte negro estrellado. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Camara orbital de drone sobrevolando las cupulas lunares. Los rovers avanzan levantando polvo gris en gravedad baja mientras la Tierra gira majestuosamente en el cielo negro infinito."',
        'color': (0.2, 0.35, 0.6)
    },
    {
        'session': 9, 'tag': 'ARTE-009', 'prefix': '8. ARTE-009',
        'title': 'Venus de Urbino de Tiziano Vecellio (1538)',
        'desc': 'La cumbre del color y la sensualidad veneciana: la dama recostada sobre sabanas de lino blanco y terciopelo carmesi, con un perrito faldero durmiendo a sus pies bajo la luz calida de Venecia.',
        'prompt_gemini': '"Recreacion al oleo hiperrealista de la Venus de Urbino de Tiziano: dama renacentista de cabellos dorados recostada con elegancia serena sobre un lecho con sabanas de saten blanco y colcha de terciopelo carmesi. A sus pies duerme un perrito spaniel. Al fondo, a traves de una estancia con columnas de marmol, doncellas buscan en un arcon nupcial bajo la luz calida veneciana. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Música Renacentista Veneciana de Salón • Tiziano (1538)',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la imagen: 'La Venus de Urbino' de Tiziano Vecellio (1538), el terciopelo carmesí, las sábanas de satén blanco y la dorada luz de salón de la Venecia renacentista.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) veneciana del siglo XVI:\n"
            "   - ESTILO OBLIGATORIO: Música cortesana veneciana renacentista, laúd dulce, espineta de salón y viola da gamba pausada, elegante y llena de intimidad.\n"
            "   - PROHIBIDO: Música contemporánea, guitarras eléctricas o ritmos tecno.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Pintura centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música veneciana integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.6, 0.2, 0.25)
    },

    # ---------------- SESION 10 ----------------
    {
        'session': 10, 'tag': 'EST-010', 'prefix': '2. EST-010',
        'title': 'COMIC / MANGA Y HALFTONE RETRO - Tren Nevado Manga',
        'desc': 'Estilo de novela grafica japonesa clasica (halftone y tramas de puntos): un tren expreso de vapor cruzando a toda velocidad un puente de hierro sobre un desfiladero nevado en Hokkaido.',
        'prompt_gemini': '"Ilustracion estilo manga clasico y comic retro de los anos 70 con tramas de puntos halftone: locomotora de vapor de gran potencia cruzando un puente metalico en las montanas nevadas de Japon durante una ventisca. Fuertes contrastes de tinta china negra sobre papel blanco, lineas cineticas de velocidad y bocanadas de humo texturizadas con puntos. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling lateral a la velocidad del tren. Las ruedas de hierro giran velozmente echando chispas, el humo blanco envuelve el puente y los copos de nieve pasan zumbando frente a la camara."',
        'color': (0.2, 0.25, 0.3)
    },
    {
        'session': 10, 'tag': 'PRAC-010', 'prefix': '3. PRAC-010',
        'title': 'Restauracion Digital de Monumentos Historicos con IA',
        'desc': 'Rehabilitacion virtual del patrimonio espanol: limpiar grafitis, reponer sillares de piedra caidos y restaurar molduras barrocas en una ermita romanica o portada renacentista.',
        'prompt_gemini': '"Fotografia de restauracion arquitectonica con IA: la portada renacentista de una colegiata espanola dividida en dos mitades; en la izquierda muestra sillares con manchas de humedad, grietas y piezas erosionadas; en la derecha luce perfectamente consolidada, con piedra caliza limpia, relieves escultoricos restaurados y sin alteraciones invasivas. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Guitarra Clásica Española y Vihuela Castellana • Siglo de Oro',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía de patrimonio histórico que acabo de subir:\n"
            "1. Analiza la imagen: la portada renacentista de piedra de una colegiata histórica española restaurada bajo la limpia luz del sol castellano.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) española clásica de época:\n"
            "   - ESTILO OBLIGATORIO: Guitarra clásica española de concierto o vihuela renacentista, notas nobles, pausadas y solemnes evocando la piedra centenaria y la historia castellana.\n"
            "   - PROHIBIDO: Guitarras eléctricas, sintetizadores tecno o fanfarrias estridentes.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Guitarra española integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.6, 0.45, 0.25)
    },
    {
        'session': 10, 'tag': 'INT-010', 'prefix': '5. INT-010',
        'title': 'La Mitica Atlantida con sus Anillos Concentricos de Agua y Palacios',
        'desc': 'La ciudad ideal descrita por Platon: tres anillos colosales de mar y tierra conectados por canales navegables, puentes monumentales cubiertos de oricalco y el gran templo de Poseidon.',
        'prompt_gemini': '"Vista aerea y corte transversal 3D fotorrealista de la capital de la Atlantida segun el relato de Platon: tres murallas circulares concentricas revestidas de bronce, estano y oricalco rojo brillante, separadas por canales de agua turquesa donde navegan trirremes. En el centro elevado, el colosal templo de Poseidon con fuentes de agua fria y caliente. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Vuelo de camara descendente desde las nubes doradas sobrevolando en espiral los anillos de agua y palacios de oricalco hasta posarse en las escalinatas del gran templo de Poseidon."',
        'color': (0.1, 0.45, 0.65)
    },
    {
        'session': 10, 'tag': 'FUT-010', 'prefix': '6. FUT-010',
        'title': 'Ano 2055: Uteros Artificiales Bio-Sinteticos (Ectogenesis)',
        'desc': 'Medicina neonatal avanzada para prematuridad extrema: camaras bio-sinteticas que replican con exactitud el fluido amniotico, la oxigenacion por cordon umbilical y los latidos maternos.',
        'prompt_gemini': '"Infografia cientifica y medica hiperrealista en un centro neonatal de alta tecnologia del ano 2055: modulos transparentes ovales de ectogenesis donde bebes prematuros flotan serenamente en liquido amniotico bio-sintetico regulado a 37°C. Tubos umbilicales biocompatibles suministran oxigeno y nutrientes mientras monitores holograficos proyectan el desarrollo pulmonar. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Zoom in optico muy suave hacia la capsula de incubacion. Los latidos ritmicos generan ondas suaves en el fluido amniotico mientras una luz calida acaricia las manitas del bebe en reposo."',
        'color': (0.2, 0.55, 0.5)
    },
    {
        'session': 10, 'tag': 'ARTE-010', 'prefix': '8. ARTE-010',
        'title': 'El Matrimonio Arnolfini de Jan van Eyck (1434)',
        'desc': 'La obra cumbre del Renacimiento flamenco y el detalle microscopico: la pareja nupcial en su alcoba flamenca, los zuecos de madera y el celebre espejo convexo al fondo donde se refleja el pintor.',
        'prompt_gemini': '"Recreacion al oleo fotorrealista de El Matrimonio Arnolfini de Jan van Eyck: Giovanni Arnolfini y su esposa tomados de la mano en una alcoba de Brujas con luz lateral de ventana. Destacan el rico ropaje de terciopelo verde y capa de piel de marta, la lampara de laton dorado bruñido y el espejo circular convexo en la pared del fondo reflejando la estancia entera. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Polifonía Flamenca Medieval de Brujas • Jan van Eyck (1434)',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la imagen: 'El Matrimonio Arnolfini' de Jan van Eyck (1434), la alcoba de Brujas, el terciopelo verde, la lámpara de latón y el espejo convexo del fondo.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del Renacimiento flamenco (siglo XV):\n"
            "   - ESTILO OBLIGATORIO: Polifonía flamenca medieval de cámara (estilo Guillaume Dufay), arpa gótica pura, salterio dulce y coro suave e íntimo de Brujas.\n"
            "   - PROHIBIDO: Guitarras eléctricas, sintetizadores modernos o percusión de cine.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Pintura flamenca centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Polifonía de Brujas integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.25, 0.45, 0.25)
    },

    # ---------------- SESION 11 ----------------
    {
        'session': 11, 'tag': 'EST-011', 'prefix': '2. EST-011',
        'title': 'COMIC / MANGA Y HALFTONE RETRO - Serie Retratos Grabado Pop Art',
        'desc': 'Homenaje al Pop Art de Roy Lichtenstein y el grabado vintage: retratos expresivos de personas mayores con tramas de puntos Benday gigantes, bordes negros gruesos y colores primarios saturados.',
        'prompt_gemini': '"Retrato estilo Pop Art retro inspirado en Roy Lichtenstein: rostro de perfil de un abuelo sonriente con gafas de pasta, delineado con trazos de tinta gruesos y coloreado mediante tramas de puntos Benday de color cyan y magenta. Fondo amarillo canario con bocadillo de comic de texto clasico y textura de papel de periodico antiguo. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Jazz Pop Acústico y Swing Retro de los 60 • Pop Art',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta ilustración Pop Art que acabo de subir:\n"
            "1. Analiza la imagen: el retrato expresivo en estilo Pop Art al estilo Roy Lichtenstein, los puntos Benday gigantes y la estética de cómic vintage de los 60.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) pop acústica retro de los años 60:\n"
            "   - ESTILO OBLIGATORIO: Swing y jazz pop acústico divertido de los años 60, contrabajo elástico, piano desenfadado y guitarra limpia con aire de cómic neoyorquino.\n"
            "   - PROHIBIDO: Sonidos electrónicos pesados, distorsión metálica o ritmos oscuros.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Ilustración Pop Art centrada con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Jazz pop integrado con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.85, 0.2, 0.25)
    },
    {
        'session': 11, 'tag': 'PRAC-011', 'prefix': '3. PRAC-011',
        'title': 'Reinterpretacion Fantastica de Lugares Conocidos de tu Ciudad',
        'desc': 'Creatividad visual desbordante con Gemini: transformar la plaza mayor de tu pueblo o la Gran Via de Madrid en una ciudad flotante entre nubes o un valle magico con cascadas y rios navegables.',
        'prompt_gemini': '"Fotografia hiperrealista transformando la Gran Via de Madrid en un valle magico futurista: los edificios clasicos de piedra blanca estan cubiertos por jardines verticales exuberantes y cascadas de agua cristalina que caen entre balcones; por la calzada no hay coches sino un rio navegable con barcas solares de madera y cielo azul radiante. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Vuelo de drone descendiendo por el canon de la Gran Via renacida. El agua de las cascadas salpica suavemente y las barcas navegan entre reflejos esmeralda bajo la brisa fresca matinal."',
        'color': (0.1, 0.6, 0.4)
    },
    {
        'session': 11, 'tag': 'INT-011', 'prefix': '5. INT-011',
        'title': 'Machu Picchu por Dentro: Acueductos en Terraza y Canales de Piedra',
        'desc': 'La genialidad hidraulica inca: terrazas agricolas escalonadas con drenajes subterraneos de cascajo para resistir lluvias, y una red de 16 fuentes litúrgicas de piedra tallada.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista de la ciudadela inca de Machu Picchu mostrando su sistema hidraulico subterraneo: capas de grava y arena bajo las terrazas agricolas para filtrar la lluvia sin deslizamientos, canales de piedra granitica pulida conduciendo el agua a las 16 fuentes de la ciudadela y el Templo del Sol al amanecer entre la niebla andina. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Camara siguiendo el curso del agua cristalina por el canal de piedra pulida, saltando de fuente en fuente hasta abrir el plano a la inmensidad de las montanas verdes de los Andes."',
        'color': (0.2, 0.5, 0.25)
    },
    {
        'session': 11, 'tag': 'FUT-011', 'prefix': '6. FUT-011',
        'title': 'Ano 2058: Ciber-Protesis Bionicas Neuro-Conectadas con Tacto',
        'desc': 'El fin de la discapacidad motora: manos y piernas bionicas de fibra de carbono y titanio conectadas directamente a los nervios del paciente, capaces de transmitir sensaciones tactiles reales.',
        'prompt_gemini': '"Infografia biomedica 3D: primer plano de una mano bionica ultrafina de titanio satinado y fibra de carbono acariciando un tejido de seda roja. Haces de luz de fibra optica en la muneca indican la transmision de impulsos sensoriales directamente a los nervios biologicos del brazo. Pantalla de diagnostico mostrando la respuesta sinaptica instantanea. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling circular en torno a los dedos bionicos mientras palpan la seda. Las luces de los sensores tactiles parpadean en tonos dorados mostrando el flujo neuronal continuo y fluido."',
        'color': (0.35, 0.4, 0.55)
    },
    {
        'session': 11, 'tag': 'ARTE-011', 'prefix': '8. ARTE-011',
        'title': 'Las Meninas de Diego Velazquez (1656)',
        'desc': 'La joya indiscutible del Museo del Prado y el misterio del aire pintado: el taller del pintor en el Alcazar de Madrid con la infanta Margarita rodeada de sus damas y Velazquez ante su lienzo.',
        'prompt_gemini': '"Recreacion al oleo fotorrealista de Las Meninas de Diego Velazquez: la infanta Margarita con vestido de guardainfante blanco dorado recibe agua en un búcaro rojo de su dama Menina. A la izquierda, Velazquez con la cruz de Santiago en el pecho sostiene su paleta y pincel. La luz dorada entra por la ventana derecha iluminando el polvo en suspension y el espejo del fondo con los monarcas. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Música Barroca Cortesana del Alcázar de Madrid • Velázquez (1656)',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la imagen: 'Las Meninas' de Diego Velázquez (1656), la infanta Margarita con su guardainfante dorado, el aire en suspensión y la atmósfera palaciega del Alcázar de Madrid.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del Barroco español del Siglo de Oro:\n"
            "   - ESTILO OBLIGATORIO: Música de cámara de la corte de Felipe IV, guitarra barroca española punteada, violines nobles y atmósfera solemne y etérea.\n"
            "   - PROHIBIDO: Música tecno, sintetizadores modernos o percusión de cine.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Obra maestra centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música barroca integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.5, 0.35, 0.2)
    },

    # ---------------- SESION 12 ----------------
    {
        'session': 12, 'tag': 'EST-012', 'prefix': '2. EST-012',
        'title': 'PIXEL ART - Cafeteria Retro 16-Bit en Noche Lluviosa',
        'desc': 'Nostalgia de los videojuegos clasicos de los 90: cafeteria acogedora vista desde la calle a traves de una ventana empanada por la lluvia, con luces de neon, taza humeante y un gato durmiendo.',
        'prompt_gemini': '"Ilustracion en pixel art impecable estilo 16-bit (Super Nintendo): interior de una cafeteria acogedora vista desde la calle empedrada en una noche lluviosa. Luces de neon calidas en tonos naranja y violeta, vapor pixelado saliendo de una taza de cafe sobre una mesa de madera y un gato atigrado durmiendo en el alfeizar de la ventana con gotas de lluvia cayendo. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Chiptune Lo-Fi Relajante y Acústico • 16-Bit Nostalgia',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta ilustración pixel art que acabo de subir:\n"
            "1. Analiza la imagen: la cafetería retro 16-bit, la noche lluviosa, el vapor del café caliente y el gato durmiendo junto a la ventana de neón.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) de estética lo-fi y chiptune acústica:\n"
            "   - ESTILO OBLIGATORIO: Melodía lo-fi acogedora y nostálgica con toques de chiptune suave de 16 bits, piano cálido, sonido sutil de lluvia de fondo y ritmo tranquilo y relajante.\n"
            "   - PROHIBIDO: Ritmos estridentes, guitarras agresivas o música bailable acelerada.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Ilustración pixel art centrada con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Melodía lo-fi integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.35, 0.2, 0.5)
    },
    {
        'session': 12, 'tag': 'PRAC-012', 'prefix': '3. PRAC-012',
        'title': 'De Boceto Infantil a Fotografia Real 8K (Sketch to Real)',
        'desc': 'La magia de convertir el garabato de un nieto en una escena de cine: tomar un dibujo infantil a lapiz de colores y pedirle a Gemini que lo transforme en una fotografia arquitectonica de ensueno.',
        'prompt_gemini': '"Comparativa visual antes y despues: en el lado izquierdo, un tierno dibujo infantil hecho con ceras de colores de una casita de campo con chimenea humeante, un gran arbol y un sol brillante; en el lado derecho, la misma escena convertida en una impresionante fotografia hiperrealista 8K de una cabana de piedra real en un prado alpino con luz de amanecer. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Transicion cinematografica fluida donde los trazos de cera de colores se van disolviendo para revelar la piedra real de la cabana, el movimiento de la hierba fresca y el humo calido saliendo de la chimenea."',
        'color': (0.8, 0.45, 0.15)
    },
    {
        'session': 12, 'tag': 'INT-012', 'prefix': '5. INT-012',
        'title': 'Santa Sofia de Constantinopla: Cupula Flotante sobre Pechinas',
        'desc': 'La joya bizantina de la arquitectura sagrada: una cupula colosal de 31 metros que parece suspendida en el aire sobre cuatro pechinas triangulares y 40 ventanas en la base.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista del interior de la Basilica de Santa Sofia en el siglo VI: la inmensa cupula dorada parece levitar gracias a la corona de 40 ventanas de arco en su base que inundan de luz dorada las pechinas de marmol verde de Tesalia y porfido rojo. Mosaicos bizantinos resplandeciendo bajo candelabros circulares de bronce suspendidos de cadenas. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Camara ascendiendo lentamente en plano cenital hacia el vertice de la cupula. La luz que entra por las 40 ventanas crea una corona dorada radiante mientras los cantos sagrados parecen resonar en el aire."',
        'color': (0.75, 0.55, 0.15)
    },
    {
        'session': 12, 'tag': 'FUT-012', 'prefix': '6. FUT-012',
        'title': 'Ano 2060: Hoteles Orbitales con Gravedad y Cupula a la Tierra',
        'desc': 'El turismo espacial para todas las edades: una gran rueda giratoria en orbita baja que genera gravedad artificial, con salones panoramicos para contemplar amaneceres orbitales.',
        'prompt_gemini': '"Infografia 3D fotorrealista del salon panoramico de un hotel orbital en el ano 2060: amplios ventanales curvos de suelo a techo a traves de los cuales se contempla la Tierra azul con la peninsula iberica iluminada por el sol naciente. En el interior confortable, personas mayores sentadas comodamente en sillones de diseno con gravedad artificial, servidos por camareros roboticos amables. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling lateral muy lento por el ventanal panoramico. La curva azul de la Tierra y la atmosfera brillante se desplazan serenamente bajo las estrellas en el silencio majestuoso del espacio."',
        'color': (0.1, 0.35, 0.65)
    },
    {
        'session': 12, 'tag': 'ARTE-012', 'prefix': '8. ARTE-012',
        'title': 'La Joven de la Perla de Johannes Vermeer (1665)',
        'desc': 'La Mona Lisa del Norte y el dominio de la luz holandesa: el retrato intimo de la joven con turbante azul y amarillo volviendose hacia el espectador con el destello perfecto de un pendiente de perla.',
        'prompt_gemini': '"Recreacion al oleo hiperrealista de La Joven de la Perla de Johannes Vermeer: joven de mirada enigmatica y labios humedos entreabiertos volviendose sobre su hombro hacia el espectador sobre un fondo oscuro profundo. Destacan el turbante de seda azul ultramar con caida dorada y el extraordinario pendiente de perla en forma de lagrima que refleja la luz pura de la ventana. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Barroco Holandés Íntimo y Clavecín • Vermeer (1665)',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la imagen: 'La Joven de la Perla' de Johannes Vermeer (1665), la mirada enigmática sobre fondo oscuro, el turbante azul ultramar y el destello nacarado del pendiente de perla.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del Barroco holandés íntimo:\n"
            "   - ESTILO OBLIGATORIO: Clavecín delicado y pausado, violonchelo barroco profundo y melodía contemplativa y nostálgica de Delft del siglo XVII.\n"
            "   - PROHIBIDO: Guitarras modernas, sintetizadores pop o ritmos electrónicos.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Cuadro centrado en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música de Vermeer integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.2, 0.45, 0.6)
    },

    # ---------------- SESION 13 ----------------
    {
        'session': 13, 'tag': 'EST-013', 'prefix': '2. EST-013',
        'title': 'HDR (HIGH DYNAMIC RANGE) - Calles Empedradas de Toledo al Atardecer',
        'desc': 'Fotografia de alto rango dinamico: callejon historico de Toledo empedrado de canto rodado, fachadas mudejares y el cielo de poniente encendido en tonos cobrizos sobre la catedral.',
        'prompt_gemini': '"Fotografia HDR fotorrealista de una calle estrecha y empinada del casco historico de Toledo al atardecer: adoquines pulidos y mojados reflejando la luz calida de los faroles de forja recien encendidos. Fachadas de ladrillo mudejar y rejas castellanas con macetas floridas. Maximo rango dinamico entre las sombras nitidas y el cielo de poniente naranja cobrizo sobre la torre de la catedral. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Guitarra Clásica Española y Campanas de Toledo • Atardecer Castellano',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía histórica que acabo de subir:\n"
            "1. Analiza la imagen: el callejón empedrado de Toledo al atardecer, los faroles de forja encendidos sobre ladrillo mudéjar y la silueta de la catedral bajo el cielo cobrizo.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) toledana y española:\n"
            "   - ESTILO OBLIGATORIO: Guitarra clásica española emotiva y virtuosa, eco suave de campanas catedralicias lejanas y aire melancólico y noble del atardecer toledano.\n"
            "   - PROHIBIDO: Música tecno, sintetizadores estridentes o ritmos pop modernos.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía centrada en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Guitarra toledana integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.8, 0.45, 0.2)
    },
    {
        'session': 13, 'tag': 'PRAC-013', 'prefix': '3. PRAC-013',
        'title': 'De Captura de Mapa Satelital a Vista Fotorrealista a Pie de Calle',
        'desc': 'De la vista satelital plana a la realidad inmersiva: tomar una captura aerea cenital de Google Maps y pedirle a Gemini que reconstruya la escena fotorrealista a nivel de calle.',
        'prompt_gemini': '"Comparativa visual 3D: en la parte superior, una captura aerea satelital plana de una plaza de pueblo espanol con su fuente central y arboleda; en la parte inferior, la reconstruccion hiperrealista a nivel de calle con iluminacion de manana soleada, bancos de piedra con vecinos charlando, palomas bebiendo en la fuente y soportales de madera con sombras suaves. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Plano secuencia en picado que desciende desde la vista aerea cenital hasta situarse a nivel de suelo entre los vecinos de la plaza, con una transicion visual fluida y natural."',
        'color': (0.2, 0.5, 0.4)
    },
    {
        'session': 13, 'tag': 'INT-013', 'prefix': '5. INT-013',
        'title': 'La Ciudad Prohibida de Pekin: El Gran Salon de la Armonia Suprema',
        'desc': 'El corazon imperial de la dinastia Ming: el Salon Taihe con sus columnas de nanmu dorado, el Trono del Dragon esculpido en oro macizo y suelo de ladrillos sonoros.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista del Gran Salon de la Armonia Suprema en la Ciudad Prohibida de Pekin en el siglo XV: inmensas columnas de madera dorada sosteniendo techos artesonados con dragones entrelazados. En el centro elevado sobre una plataforma de marmol blanco, el deslumbrante Trono del Dragon de oro con pebeteros de bronce con forma de grulla humeando incienso. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling frontal solemne recorriendo la alfombra roja central hacia el Trono del Dragon. El humo aromatico se eleva en volutas doradas iluminadas por los rayos de sol que entran por las celosias."',
        'color': (0.85, 0.3, 0.15)
    },
    {
        'session': 13, 'tag': 'FUT-013', 'prefix': '6. FUT-013',
        'title': 'Ano 2063: Red Hyperloop de Levitacion Magnetica a 1200 km/h',
        'desc': 'Transporte ultrarrapido sostenible: capsulas aerodinamicas que levitan mediante superconductores dentro de tubos de acero al vacio sellados, uniendo Madrid y Barcelona en 35 minutos.',
        'prompt_gemini': '"Infografia de transporte futurista 3D: corte transversal de un tubo de transporte Hyperloop sellado al vacio en el ano 2063. Una capsula aerodinamica de levitacion magnetica pasiva vuela a 1200 km/h guiada por bobinas superconductoras. A traves del lateral transparente de la capsula se ve a pasajeros relajados leyendo y tomando un cafe mientras monitores muestran el trayecto Madrid-Paris. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Camara persiguiendo a gran velocidad la capsula magnetica por el interior del tubo iluminado con anillos LED azules, con un zumbido electromagnetico suave y sensacion de suavidad absoluta."',
        'color': (0.1, 0.4, 0.7)
    },
    {
        'session': 13, 'tag': 'ARTE-013', 'prefix': '8. ARTE-013',
        'title': 'La Ronda de Noche de Rembrandt van Rijn (1642)',
        'desc': 'El claroscuro magistral y el dinamismo barroco holandes: la compania de milicianos saliendo de un portal sombrio bajo un foco de luz teatral que ilumina a una misteriosa nina dorada.',
        'prompt_gemini': '"Recreacion pictorica al oleo de La Ronda de Noche de Rembrandt: el capitan Frans Banninck Cocq de riguroso negro con banda roja y su teniente de jubon amarillo oro dan la orden de marcha a la guardia civica. En medio de la penumbra teatral, una nina vestida de oro resplandece como un foco de luz magica entre picas, mosquetes y tambores en movimiento. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Marcha Barroca Holandesa de Guardia Cívica • Rembrandt (1642)',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la escena: 'La Ronda de Noche' de Rembrandt (1642), la milicia cívica en marcha, el claroscuro teatral de Ámsterdam, picas y mosquetes en movimiento.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del Barroco holandés marcial:\n"
            "   - ESTILO OBLIGATORIO: Marcha solemne de guardia cívica del siglo XVII, tambor de desfile lento y constante, trompetas barrocas nobles y cuerdas enérgicas de claroscuro.\n"
            "   - PROHIBIDO: Guitarras eléctricas, sintetizadores tecno o pop contemporáneo.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Pintura barroca centrada con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Marcha de Rembrandt integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.55, 0.35, 0.15)
    },

    # ---------------- SESION 14 ----------------
    {
        'session': 14, 'tag': 'EST-014', 'prefix': '2. EST-014',
        'title': 'HDR (HIGH DYNAMIC RANGE) - Bodegon del Mar y Redes Marineras',
        'desc': 'Bodegon marinero mediterraneo con nitidez cristalina: cesta de mimbre con bogavantes rojos, salmonetes de roca y sardinas brillantes sobre una mesa carcomida por el salitre y redes.',
        'prompt_gemini': '"Fotografia HDR fotorrealista de un bodegon marinero tradicional en un puerto pesquero gallego: mesa de madera desgastada con salitre donde reposa una cesta con pescados de roca frescos de escamas irisadas, un bogavante de caparazon rojo vivo, redes de canamo mojadas y un cuchillo de mango de madera. Luz limpia y diáfana con gotas de agua cristalinas brillando. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling circular cercano alrededor de la mesa marinera. El agua de las escamas gotea suavemente sobre la madera del barco y la brisa del puerto mece una red con boyas de cristal verde."',
        'color': (0.15, 0.5, 0.6)
    },
    {
        'session': 14, 'tag': 'PRAC-014', 'prefix': '3. PRAC-014',
        'title': 'De Fotografia Retrato a Diseno de Tatuaje Minimalista de Trazo Fino',
        'desc': 'Diseno grafico familiar con IA: convertir el retrato fotografico de un nieto o de una mascota en un elegante diseno de tatuaje lineal a un solo trazo continuo (Single Line Art).',
        'prompt_gemini': '"Comparativa grafica elegante: a la izquierda, la fotografia de primer plano de un perro labrador con mirada carinosa; a la derecha, la transformacion artistica en ilustracion minimalista de una sola linea continua (Single Line Art) trazada con tinta negra fina sobre piel limpia, capturando con sutileza y precision la silueta y emocion del animal. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Piano Minimalista Íntimo y Violonchelo Sutil • Single Line Art',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta ilustración minimalista que acabo de subir:\n"
            "1. Analiza la imagen: el diseño artístico a un solo trazo continuo (Single Line Art), la mirada fiel del perro y la elegancia del trazo limpio.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) contemporánea y minimalista:\n"
            "   - ESTILO OBLIGATORIO: Piano acústico minimalista íntimo (estilo Ludovico Einaudi), violonchelo emotivo en notas sostenidas y melodía tierna y poética.\n"
            "   - PROHIBIDO: Ritmos tecno, percusión acelerada o sintetizadores estridentes.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Ilustración minimalista centrada con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Piano íntimo integrado con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.3, 0.3, 0.35)
    },
    {
        'session': 14, 'tag': 'INT-014', 'prefix': '5. INT-014',
        'title': 'Tenochtitlan por Dentro: Calzadas, Chinampas y Templo Mayor',
        'desc': 'La colosal metropoli azteca flotando en el lago de Texcoco: calzadas de piedra con puentes levadizos, huertos flotantes (chinampas) rebosantes de maiz y flores, y el sagrado Templo Mayor.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista de la ciudad lacustre de Tenochtitlan en el ano 1500: la gran calzada de Iztapalapa cortando las aguas del lago Texcoco con canoas navegando entre huertos flotantes (chinampas) de flores y maiz. Al fondo, el recinto sagrado con el Templo Mayor policromado en rojo y azul, pebeteros de copal humeando y los volcanes nevados al horizonte. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Vuelo rasante en canoa deslizandose por los canales entre las chinampas floridas hasta enfocar la imponente mole del Templo Mayor alzandose hacia el cielo azul mesoamericano."',
        'color': (0.7, 0.3, 0.15)
    },
    {
        'session': 14, 'tag': 'FUT-014', 'prefix': '6. FUT-014',
        'title': 'Ano 2065: Desalinizadoras Solares de Grafeno y Oasis en el Sahara',
        'desc': 'El milagro del agua dulce inagotable: membranas de grafeno nanoporoso que desalan agua de mar con energia solar termica, canalizando rios que reverdecen valles deserticos.',
        'prompt_gemini': '"Infografia medioambiental 3D en el desierto del Sahara en el ano 2065: una gigantesca planta desalinizadora de arquitectura bio-morfica alimentada por torres solares de concentracion. Membranas de grafeno translucidas filtran agua de mar que sale como rios caudalosos de agua potable, transformando las dunas amarillas en campos de cultivo verdes y palmerales densos. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling aereo sobrevolando el canal de agua cristalina que nace en la desalinizadora solar y avanza transformando la arena seca en vergel verde lleno de cultivos y vida vegetal."',
        'color': (0.1, 0.6, 0.45)
    },
    {
        'session': 14, 'tag': 'ARTE-014', 'prefix': '8. ARTE-014',
        'title': 'La Leccion de Anatomia del Dr. Nicolaes Tulp de Rembrandt (1632)',
        'desc': 'El amanecer de la ciencia medica moderna y la luz barroca: el celebre cirujano diseca con pinzas los tendones del brazo izquierdo de un cadaver mientras medicos contemplan fascinados.',
        'prompt_gemini': '"Recreacion al oleo hiperrealista de La Leccion de Anatomia del Dr. Nicolaes Tulp de Rembrandt: en un anfiteatro anatomico en penumbra, el doctor Tulp con sombrero negro levanta con unas pinzas metalicas los flexores del brazo del cuerpo disecado. Siete cirujanos con cuellos de gorguera blanca se inclinan hacia adelante con miradas cientificas fascinadas bajo una potente luz cenital. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Música Barroca Solemne y Cuerda Médica Reflexiva • Rembrandt (1632)',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la imagen: 'La Lección de Anatomía del Dr. Tulp' de Rembrandt (1632), el anfiteatro en penumbra, las gorgueras blancas y la mirada científica y asombrada ante el cuerpo humano.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del Barroco científico holandés:\n"
            "   - ESTILO OBLIGATORIO: Cuerdas frotadas graves y solemnes (viola de gamba y violonchelo), aire reflexivo y majestuoso del Siglo de Oro holandés y un compás pausado de descubrimiento médico.\n"
            "   - PROHIBIDO: Guitarras modernas, baterías de rock o sintetizadores tecno.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Cuadro centrado en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Cuerda barroca integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.5, 0.3, 0.15)
    },

    # ---------------- SESION 15 ----------------
    {
        'session': 15, 'tag': 'EST-015', 'prefix': '2. EST-015',
        'title': 'BLANCO Y NEGRO (MONOCROMATICO) - Anciano Violinista en Teatro',
        'desc': 'La emocion del blanco y negro puro y el retrato psicologico: un anciano musico de manos arrugadas ensayando en solitario con su violin en el foso de un teatro vacio bajo un foco cenital.',
        'prompt_gemini': '"Retrato fotografico en blanco y negro monocromatico puro con rica escala de grises: un anciano violinista de cabello canoso y manos curtidas toca su instrumento con los ojos cerrados en medio del foso vacio de un teatro clasico de opera. Unico foco de luz cenital de plata esculpiendo las arrugas nobles de su frente, la madera barnizada del violin y el polvo danzando en el aire. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Violín Solista Clásico Íntimo y Melancólico • Foso de Teatro',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta fotografía en blanco y negro que acabo de subir:\n"
            "1. Analiza la imagen: el anciano violinista tocando con los ojos cerrados en el foso solitario del teatro, la madera noble del instrumento y el haz de luz de plata cenital.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) para violín solista clásico:\n"
            "   - ESTILO OBLIGATORIO: Violín acústico solista clásico y virtuoso, melodía íntima, desgarradora y profundamente emotiva, con la acústica natural y reverberación de un gran teatro vacío.\n"
            "   - PROHIBIDO: Ritmos electrónicos modernos, baterías o sintetizadores pop.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Fotografía monocromática centrada con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Violín solista integrado con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.25, 0.25, 0.3)
    },
    {
        'session': 15, 'tag': 'PRAC-015', 'prefix': '3. PRAC-015',
        'title': 'Extraccion y Aislamiento 3D de un Objeto Familiar con Fondo Puro',
        'desc': 'Fotografia de catalogo profesional en casa: recortar con precision milimetrica un objeto querido (un reloj antiguo de bolsillo) y colocarlo flotando sobre fondo blanco con sombras realistas.',
        'prompt_gemini': '"Fotografia de producto editorial y aislamiento 3D: un reloj de bolsillo de oro antiguo con cadena de eslabones perfectamente recortado y flotando en un angulo de 45 grados sobre fondo blanco puro de estudio. Reflejos metalicos nitidos en la tapa grabada, cristal pulido y sombra de contacto suave proyectada en la base. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Giro orbital de 360 grados del reloj de bolsillo suspendido en el aire. Los reflejos dorados y los grabados de la tapa deslumbran con suavidad bajo la luz de estudio impecable."',
        'color': (0.7, 0.5, 0.1)
    },
    {
        'session': 15, 'tag': 'INT-015', 'prefix': '5. INT-015',
        'title': 'La Ciudadela de Petra: El Tesoro (Al-Khazneh) Tallado en la Roca',
        'desc': 'La maravilla nabatea esculpida en la arenisca roja del desfiladero del Siq: la fachada monumental helenistica de 40 metros de altura y sus camaras interiores secretas de caravanas de incienso.',
        'prompt_gemini': '"Corte transversal 3D e interior arqueologico del Tesoro de Petra (Al-Khazneh) en Jordania al amanecer: la monumental fachada clasica tallada directamente en la roca arenisca rosa emerge al final del estrecho desfiladero del Siq. En el interior de la gran camara cuadrada, comerciantes nabateos con tunicas revisan arcones de incienso bajo la luz calida de pebeteros. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Avanzar a paso de dromedario por la estrecha garganta rocosa del Siq en penumbra hasta que se abre de golpe la hendidura revelando la majestuosa fachada rosada del Tesoro banada por el sol matinal."',
        'color': (0.75, 0.35, 0.2)
    },
    {
        'session': 15, 'tag': 'FUT-015', 'prefix': '6. FUT-015',
        'title': 'Ano 2070: Primera Ciudad en Marte bajo Cupulas de Diamante',
        'desc': 'El gran salto de la civilizacion interplanetaria: la metropoli de Ares Vallis en el planeta rojo, albergando a 50.000 habitantes bajo cupulas geodesicas con lagos y vistas a Fobos y Deimos.',
        'prompt_gemini': '"Infografia aeroespacial 3D fotorrealista de la primera gran ciudad humana en Marte en el ano 2070: inmensas cupulas geodesicas de carbono transparente en el canon de Ares Vallis que protegen una urbe verde con arboles terrestres, lagos artificiales y monorrailes flotantes. Fuera de las cupulas, el paisaje marciano rojizo con rovers solares y las dos lunas Fobos y Deimos en el cielo de color salmon. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'video',
        'prompt_flow': '"Travelling aereo descendente desde la orbita marciana atravesando la cupula geodesica transparente para descender sobre los jardines arbolados y avenidas de la ciudad marciana."',
        'color': (0.8, 0.3, 0.15)
    },
    {
        'session': 15, 'tag': 'ARTE-015', 'prefix': '8. ARTE-015',
        'title': 'La Encajera de Johannes Vermeer (1670)',
        'desc': 'El homenaje a la labor paciente y artesana: la joven holandesa inclinada sobre su almohadilla tejiendo encaje de bolillos con finos hilos de seda blanca y roja que caen como gotas de luz.',
        'prompt_gemini': '"Recreacion al oleo hiperrealista de La Encajera de Johannes Vermeer: joven artesana de cabello recogido con trenzas inclinada con concentracion absoluta sobre su labor de encaje de bolillos. Viste corpiño amarillo mostaza y cuello blanco. Hilos de seda roja y blanca fluyen de su almohadilla de coser sobre un tapiz floral con luz de ventana matinal destacando cada textura. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'mode': 'music',
        'music_style': 'Cuerda Barroca Íntima y Clavecín Sutil • Vermeer (1670)',
        'prompt_music': (
            "Actúa como editor y compositor multimedia. A partir de esta recreación pictórica que acabo de subir:\n"
            "1. Analiza la imagen: 'La Encajera' de Johannes Vermeer (1670), la paciente concentración de la joven tejiendo bolillos, los hilos de seda roja y la luz suave matinal.\n"
            "2. Compón una pieza musical breve (10 a 15 segundos) del Barroco íntimo holandés:\n"
            "   - ESTILO OBLIGATORIO: Cuerda barroca pulsada sutil, clavecín delicado y atmósfera serena de silencio y concentración artesanal en Delft.\n"
            "   - PROHIBIDO: Guitarras modernas, baterías o sintetizadores pop.\n"
            "3. Ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un Visor Fotográfico Cinemático:\n"
            "   - Cuadro centrado en alta resolución con suave movimiento cinemático (efecto Ken Burns).\n"
            "   - Música de época integrada con botón táctil grande de 'Reproducir / Pausar Música'.\n"
            "   - Botón 'Descargar Visor (.html)' para guardarlo en el Mac y disfrutarlo sin conexión."
        ),
        'color': (0.6, 0.45, 0.2)
    }
]

def find_target_filename(session_folder, tag_prefix):
    if not os.path.exists(session_folder):
        return None
    for f in os.listdir(session_folder):
        if f.startswith(tag_prefix) and f.endswith('.pdf'):
            return f
    return None

def build_worksheet(output_path, item):
    pdf = RobustNativePDFWriter(page_width=612.0, page_height=792.0)
    pdf.start_page()

    tag_code = item['tag']
    session_num = item['session']
    mode = item['mode']
    r_c, g_c, b_c = item['color']

    # Barra superior decorativa
    pdf.set_fill_color(r_c, g_c, b_c)
    pdf.rect(30, 762, 552, 6, fill=True, stroke=False)

    if mode == 'video':
        pdf.draw_text(36, 750, f'SESION {session_num:02d} • FICHA DE GENERACION VISUAL + AMPLIACION A VIDEO [{tag_code}]', font='F2', size=8.5, r=r_c * 0.7 + 0.1, g=g_c * 0.7 + 0.1, b=b_c * 0.7 + 0.1)
    else:
        pdf.draw_text(36, 750, f'SESION {session_num:02d} • FICHA DE GENERACION VISUAL + BANDA SONORA FLOW [{tag_code}]', font='F2', size=8.5, r=0.55, g=0.2, b=0.8)

    pdf.draw_text(36, 735, item['title'], font='F2', size=11.5, r=0.1, g=0.15, b=0.25)

    # Linea divisoria
    pdf.set_stroke_color(0.85, 0.88, 0.92)
    pdf.set_line_width(0.8)
    pdf.line(30, 725, 582, 725)

    # Seccion 1: Concepto Didactico
    pdf.set_fill_color(0.97, 0.98, 0.99)
    pdf.set_stroke_color(0.85, 0.88, 0.92)
    pdf.set_line_width(0.8)
    pdf.rect(30, 625, 552, 92, fill=True, stroke=True)

    pdf.draw_text(42, 703, '1. OBJETIVO DIDACTICO Y CONCEPTO CLAVE', font='F2', size=8.8, r=0.2, g=0.25, b=0.35)
    lines_desc = wrap_text(item['desc'], 114)
    y_desc = 689
    for l in lines_desc:
        pdf.draw_text(42, y_desc, l, font='F1', size=7.5, r=0.25, g=0.3, b=0.35)
        y_desc -= 11

    if mode == 'video':
        pdf.draw_text(42, 633, 'METODO DIDACTICO: 1. Pegar prompt en Gemini -> 2. Descargar imagen JPG -> 3. Animar video en Google Flow.', font='F2', size=7.6, r=0.1, g=0.45, b=0.65)
    else:
        pdf.draw_text(42, 633, 'METODO DIDACTICO: 1. Pegar prompt en Gemini -> 2. Descargar imagen JPG -> 3. Visor con Musica en Google Flow.', font='F2', size=7.6, r=0.5, g=0.2, b=0.7)

    # Seccion 2: Prompt Maestro para Gemini
    pdf.set_fill_color(0.96, 0.98, 1.0)
    pdf.set_stroke_color(r_c * 0.8, g_c * 0.8, b_c * 0.8)
    pdf.set_line_width(1.0)
    pdf.rect(30, 445, 552, 172, fill=True, stroke=True)

    pdf.draw_text(42, 603, '2. PROMPT MAESTRO PARA CREAR LA IMAGEN EN GEMINI (gemini.google.com)', font='F2', size=8.8, r=0.1, g=0.3, b=0.55)
    pdf.draw_text(42, 591, '(Copia todo el texto del recuadro inferior y pegalo directamente en el chat de Gemini)', font='F3', size=7.2, r=0.4, g=0.45, b=0.5)

    # Recuadro interior Gemini
    pdf.set_fill_color(0.90, 0.94, 0.99)
    pdf.set_stroke_color(r_c * 0.9, g_c * 0.9, b_c * 0.9)
    pdf.set_line_width(0.8)
    pdf.rect(40, 455, 532, 130, fill=True, stroke=True)

    lines_pg = wrap_text(item['prompt_gemini'], 108)
    y_pg = 572
    for l in lines_pg:
        pdf.draw_text(48, y_pg, l, font='F1', size=7.3, r=0.08, g=0.15, b=0.3)
        y_pg -= 11

    # Seccion 3: Modo Video o Modo Musica
    if mode == 'video':
        pdf.set_fill_color(0.99, 0.97, 0.93)
        pdf.set_stroke_color(0.85, 0.45, 0.1)
        pdf.set_line_width(1.2)
        pdf.rect(30, 235, 552, 202, fill=True, stroke=True)

        pdf.draw_text(42, 422, '3. AMPLIACION: ¡DALE VIDA EN VIDEO CON GOOGLE FLOW! (Gasta 10 de tus 50 puntos diarios)', font='F2', size=8.8, r=0.75, g=0.3, b=0.02)

        steps_txt = [
            "1. Descarga la imagen: Haz clic en la imagen generada en Gemini y pulsa en 'Descargar' (la flecha).",
            "2. Entra en Google Flow y arrastra: Abre https://labs.google/flow y arrastra directamente la imagen a la pantalla.",
            "3. Pega el prompt de abajo: En el recuadro de texto de Flow, pega el siguiente prompt de movimiento y pulsa 'Generar Video'."
        ]
        y_st = 408
        for st in steps_txt:
            lines_st = wrap_text(st, 114)
            for idx, l in enumerate(lines_st):
                is_bold = (idx == 0 and ('1.' in l or '2.' in l or '3.' in l))
                pdf.draw_text(42, y_st, l, font='F2' if is_bold else 'F1', size=7.2, r=0.25, g=0.2, b=0.15)
                y_st -= 10

        pdf.set_fill_color(1.0, 0.95, 0.88)
        pdf.set_stroke_color(0.85, 0.45, 0.1)
        pdf.set_line_width(0.8)
        pdf.rect(40, 248, 532, 98, fill=True, stroke=True)

        pdf.draw_text(48, 332, 'PROMPT EXACTO DE MOVIMIENTO PARA PEGAR EN GOOGLE FLOW (labs.google/flow):', font='F2', size=7.5, r=0.6, g=0.2, b=0.0)
        lines_pf = wrap_text(item['prompt_flow'], 108)
        y_pf = 318
        for l in lines_pf:
            pdf.draw_text(48, y_pf, l, font='F1', size=7.2, r=0.2, g=0.1, b=0.0)
            y_pf -= 11

        pdf.draw_text(48, 255, 'Resultado: En 10 segundos tendras tu escena convertida en un video MP4 listo para compartir en WhatsApp.', font='F3', size=6.8, r=0.45, g=0.3, b=0.1)

    else:
        # Modo Música Flow + Visor Cinemático
        pdf.set_fill_color(0.97, 0.95, 1.0) # Violeta tenue
        pdf.set_stroke_color(0.55, 0.25, 0.8) # Violeta medio
        pdf.set_line_width(1.2)
        pdf.rect(30, 235, 552, 202, fill=True, stroke=True)

        pdf.draw_text(42, 422, '3. AMPLIACION: ¡PONLE MUSICA Y CREA TU VISOR CINEMATICO EN GOOGLE FLOW!', font='F2', size=8.8, r=0.5, g=0.15, b=0.75)

        steps_txt = [
            "1. Descarga la imagen: Haz clic en la imagen generada en Gemini y pulsa en 'Descargar' (la flecha).",
            "2. Entra en Google Flow y arrastra: Abre https://labs.google/flow y arrastra directamente la imagen a la pantalla.",
            f"3. Pega el prompt de abajo: Copia el prompt para componer la banda sonora ({item['music_style']}) y generar el visor interactivo."
        ]
        y_st = 408
        for st in steps_txt:
            lines_st = wrap_text(st, 114)
            for idx, l in enumerate(lines_st):
                is_bold = (idx == 0 and ('1.' in l or '2.' in l or '3.' in l))
                pdf.draw_text(42, y_st, l, font='F2' if is_bold else 'F1', size=7.2, r=0.2, g=0.15, b=0.3)
                y_st -= 10

        pdf.set_fill_color(0.92, 0.88, 0.98)
        pdf.set_stroke_color(0.55, 0.25, 0.8)
        pdf.set_line_width(0.8)
        pdf.rect(40, 248, 532, 98, fill=True, stroke=True)

        pdf.draw_text(48, 332, f"PROMPT DE BANDA SONORA Y VISOR CINEMATICO (https://labs.google/flow) [{item['music_style']}]:", font='F2', size=7.3, r=0.45, g=0.1, b=0.65)
        lines_pm = wrap_text(item['prompt_music'], 108)
        y_pm = 320
        for l in lines_pm[:7]: # Máximo 7 líneas para que no desborde
            pdf.draw_text(48, y_pm, l, font='F1', size=7.0, r=0.15, g=0.1, b=0.25)
            y_pm -= 9.8

        pdf.draw_text(48, 253, "Compartir seguro: En el visor pulsa 'Publish' en Gemini Canvas, copia el enlace publico y pegalo en WhatsApp.", font='F2', size=6.9, r=0.35, g=0.1, b=0.55)

    # Pie de pagina institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 222, 582, 222)
    if mode == 'video':
        pdf.draw_text(36, 208, f'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION {session_num:02d} • {tag_code}', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
        pdf.draw_text(36, 196, 'Metodologia Dual: Gemini (Imagen Fija) + Google Flow (Animacion de Video • 10 Creditos)', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)
    else:
        pdf.draw_text(36, 208, f'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION {session_num:02d} • {tag_code}', font='F2', size=7.2, r=0.45, g=0.2, b=0.65)
        pdf.draw_text(36, 196, 'Metodologia Dual: Gemini (Imagen Fija) + Google Flow Music (Banda Sonora & Visor Cinemático)', font='F3', size=6.8, r=0.5, g=0.3, b=0.6)

    pdf.end_page()
    pdf.write_to_file(output_path)

def sync_all_fiches_and_maps():
    print("==================================================================")
    print("=== [1] COMPILACIÓN DE 60 FICHAS DE IMAGEN (3 VÍDEO / 2 MÚSICA) ===")
    print("==================================================================")

    generated_count = 0
    video_count = 0
    music_count = 0

    for item in ALL_ITEMS:
        s = item['session']
        s_folder = os.path.join(SESSIONS_DIR, f"{s:02d}_Sesion")
        target_fn = find_target_filename(s_folder, item['prefix'])

        if not target_fn:
            clean_title = re.sub(r'[\/:*?"<>|]', '', item['title'])
            target_fn = f"{item['prefix']}_{clean_title}.pdf"

        output_path = os.path.join(s_folder, target_fn)
        build_worksheet(output_path, item)
        generated_count += 1
        if item['mode'] == 'video':
            video_count += 1
        else:
            music_count += 1

        # Sincronizar al bloque correspondiente
        tag_key = item['tag'].split('-')[0]
        block_dir = BLOCK_DIRS.get(tag_key)
        if block_dir and os.path.exists(block_dir):
            shutil.copy2(output_path, os.path.join(block_dir, target_fn))

    print(f"✅ Total Fichas Generadas: {generated_count} ({video_count} VÍDEO FLOW + {music_count} FLOW MUSIC)")
    print("✅ Todas las fichas han sido sincronizadas en los Bloques 02, 03, 05, 06 y 08.")

    print("\n==================================================================")
    print("=== [2] ACTUALIZACIÓN DE MAPAS INTERACTIVOS (SESIONES 04 A 15) ===")
    print("==================================================================")

    # Crear mapa de consulta rápida por sesión y tag
    tag_mode_map = {}
    for item in ALL_ITEMS:
        tag_mode_map[(item['session'], item['tag'])] = item['mode']

    for s in range(4, 16):
        s_folder = os.path.join(SESSIONS_DIR, f"{s:02d}_Sesion")
        if not os.path.exists(s_folder):
            continue

        for map_name in [f"MAPA_CLASE_SESION_{s:02d}.html", f"MAPA_SESION_{s:02d}.html"]:
            map_path = os.path.join(s_folder, map_name)
            if not os.path.exists(map_path):
                continue

            with open(map_path, "r", encoding="utf-8") as f:
                html = f.read()

            def update_card(match):
                card_html = match.group(0)
                href = match.group(1)
                inner = match.group(2)

                matched_tag = None
                for t in ['EST', 'ARTE', 'PRAC', 'INT', 'FUT']:
                    code = f"{t}-{s:03d}"
                    if code in href or f"[{t}]" in inner or f" {t}-" in href:
                        matched_tag = code
                        break

                if not matched_tag:
                    return card_html

                mode = tag_mode_map.get((s, matched_tag), 'video')

                if mode == 'video':
                    new_tag = '<span class="file-tag tag-pdf" style="background:#ea4335; color:#fff;">+ VÍDEO FLOW</span>'
                    inner_new = re.sub(r'<span class="file-tag tag-pdf"[^>]*>[^<]*</span>', new_tag, inner)
                    # Descripción
                    inner_new = re.sub(r'•\s*(Ampliaci[oó]n[^<]*|Banda Sonora[^<]*)', '• Ampliación a Vídeo con Google Flow (10 créditos) 🎬', inner_new)
                    if "Google Flow" not in inner_new and "•" in inner_new:
                        inner_new = re.sub(r'(<span class="file-desc">[^<]+)</span>', r'\1 • Ampliación a Vídeo con Google Flow (10 créditos) 🎬</span>', inner_new)
                else:
                    new_tag = '<span class="file-tag tag-pdf" style="background:#9333ea; color:#fff;">+ MÚSICA FLOW</span>'
                    inner_new = re.sub(r'<span class="file-tag tag-pdf"[^>]*>[^<]*</span>', new_tag, inner)
                    # Descripción
                    inner_new = re.sub(r'•\s*(Ampliaci[oó]n[^<]*|Banda Sonora[^<]*)', '• Banda Sonora & Visor Cinemático en Google Flow 🎵', inner_new)
                    if "Google Flow" not in inner_new and "•" in inner_new:
                        inner_new = re.sub(r'(<span class="file-desc">[^<]+)</span>', r'\1 • Banda Sonora & Visor Cinemático en Google Flow 🎵</span>', inner_new)

                return f'<a href="{href}" target="_blank" class="file-card">{inner_new}</a>'

            new_html = re.sub(r'<a\s+href="([^"]+)"[^>]*class="file-card"[^>]*>(.*?)</a>', update_card, html, flags=re.DOTALL)

            if new_html != html:
                with open(map_path, "w", encoding="utf-8") as f:
                    f.write(new_html)
                v_cnt = len(re.findall(r'\+ V[IÍ]DEO FLOW', new_html))
                m_cnt = len(re.findall(r'\+ M[UÚ]SICA FLOW', new_html))
                print(f"✅ [S{s:02d} {map_name}] Sincronizado: {v_cnt} Vídeo Flow / {m_cnt} Música Flow")

    print("\n✨ Proceso de rebalanceo 3/2 completado al 100% en todas las sesiones.")

if __name__ == '__main__':
    sync_all_fiches_and_maps()
