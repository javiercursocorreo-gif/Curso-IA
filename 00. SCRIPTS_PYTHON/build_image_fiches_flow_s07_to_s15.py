#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_image_fiches_flow_s07_to_s15.py
Genera las 45 Fichas Didácticas de Imagen (5 fichas por sesión x 9 sesiones: S07 a S15)
actualizadas con la Ampliación Oficial a Vídeo en Google Flow (12 Créditos):
- 2. [EST]
- 3. [PRAC]
- 5. [INT]
- 6. [FUT]
- 8. [ARTE]
"""

import os
import sys
import shutil

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SESSIONS_BASE = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

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

def build_image_worksheet(output_path, session_num, tag_code, num_str, title, desc_concept, prompt_gemini, prompt_flow, theme_color_rgb):
    pdf = NativePDFWriter(page_width=612.0, page_height=792.0)
    pdf.start_page()

    # Marco exterior elegante
    pdf.set_fill_color(0.985, 0.99, 1.0)
    pdf.set_stroke_color(theme_color_rgb[0], theme_color_rgb[1], theme_color_rgb[2])
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal institucional
    pdf.set_fill_color(theme_color_rgb[0] * 0.35, theme_color_rgb[1] * 0.35, theme_color_rgb[2] * 0.35)
    pdf.rect(24, 714, 564, 54, fill=True, stroke=False)

    pdf.draw_text(36, 750, f'SESION {session_num:02d} • FICHA DE GENERACION VISUAL + AMPLIACION A VIDEO [{tag_code}]', font='F2', size=8.5, r=0.85, g=0.92, b=1.0)
    pdf.draw_text(36, 730, f'{num_str}: {title}', font='F2', size=11.2, r=1, g=1, b=1)

    # Sección 1: Concepto y Objetivo Visual
    pdf.set_fill_color(0.95, 0.97, 1.0)
    pdf.set_stroke_color(theme_color_rgb[0], theme_color_rgb[1], theme_color_rgb[2])
    pdf.set_line_width(1.0)
    pdf.rect(30, 615, 552, 90, fill=True, stroke=True)

    pdf.draw_text(42, 690, '1. CONCEPTO Y OBJETIVO VISUAL:', font='F2', size=9.0, r=0.08, g=0.25, b=0.55)
    lines_desc = wrap_text(desc_concept, 114)
    y_dc = 674
    for l in lines_desc:
        pdf.draw_text(42, y_dc, l, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
        y_dc -= 11.2

    # Sección 2: Prompt Maestro para Gemini (Imagen Fija)
    pdf.set_fill_color(0.98, 0.99, 1.0)
    pdf.set_stroke_color(0.2, 0.55, 0.85)
    pdf.set_line_width(1.0)
    pdf.rect(30, 445, 552, 160, fill=True, stroke=True)

    pdf.draw_text(42, 590, '2. PROMPT MAESTRO PARA GEMINI (IMAGEN FIJA DE ALTA DEFINICION):', font='F2', size=9.0, r=0.05, g=0.3, b=0.6)
    pdf.draw_text(42, 577, '(Copia este texto y pegalo en gemini.google.com para generar la imagen base de partida)', font='F3', size=7.2, r=0.4, g=0.45, b=0.5)

    # Recuadro interior Prompt Gemini
    pdf.set_fill_color(0.92, 0.96, 1.0)
    pdf.set_stroke_color(0.25, 0.6, 0.9)
    pdf.set_line_width(0.8)
    pdf.rect(40, 455, 532, 115, fill=True, stroke=True)

    lines_pg = wrap_text(prompt_gemini, 108)
    y_pg = 552
    for l in lines_pg:
        pdf.draw_text(48, y_pg, l, font='F1', size=7.2, r=0.08, g=0.15, b=0.3)
        y_pg -= 10.8

    # Sección 3: Ampliación Oficial con Google Flow (12 Créditos)
    pdf.set_fill_color(0.99, 0.97, 0.93)
    pdf.set_stroke_color(0.85, 0.45, 0.1)
    pdf.set_line_width(1.2)
    pdf.rect(30, 235, 552, 200, fill=True, stroke=True)

    pdf.draw_text(42, 420, '3. AMPLIACION: ¡DALE VIDA EN VIDEO CON GOOGLE FLOW! (Gasta 12 de tus 50 puntos diarios)', font='F2', size=8.8, r=0.75, g=0.3, b=0.02)
    
    steps_txt = [
        "1. Descarga la imagen: Haz clic en la imagen generada en Gemini y pulsa en 'Descargar' (la flecha).",
        "2. Entra en Google Flow y arrastra: Abre https://labs.google/flow. En lugar de pulsar en 'Subir imagen', arrastrala directamente desde la flechita de descargas del navegador a la pantalla de Flow.",
        "3. Pega el prompt de abajo: En el recuadro de texto de Flow, pega el siguiente prompt de movimiento cinematografico y pulsa 'Generar Video'."
    ]
    y_st = 406
    for st in steps_txt:
        lines_st = wrap_text(st, 114)
        for idx, l in enumerate(lines_st):
            is_bold = (idx == 0 and ('1.' in l or '2.' in l or '3.' in l))
            pdf.draw_text(42, y_st, l, font='F2' if is_bold else 'F1', size=7.2, r=0.25, g=0.2, b=0.15)
            y_st -= 9.8

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
        y_pf -= 10.8

    pdf.draw_text(48, 252, 'Resultado: En 10 segundos tendras tu escena convertida en un video MP4 de 5s con camara cinematografica profesional.', font='F3', size=6.8, r=0.45, g=0.3, b=0.1)

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 222, 582, 222)
    pdf.draw_text(36, 208, f'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION {session_num:02d} • {tag_code}', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 196, 'Metodologia Dual: Gemini (Imagen Fija) + Google Flow (Animacion de Video • 12 Creditos)', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ [{tag_code}] Ficha con ampliación Flow generada: {output_path}")

IMAGE_WORKSHEETS_DATA = [
    # ==========================================
    # SESIÓN 07
    # ==========================================
    {
        'session': 7,
        'tag': 'EST-007',
        'prefix': '2. EST-007',
        'title': 'IMPRESIONISTA Y POST-IMPRESIONISTA - Klimt: Dama en Pan de Oro',
        'desc': 'Retrato modernista de la Secesion de Viena inspirado en Gustav Klimt: elegante dama con peinado recogido, mirada enigmatica y suntuosa tunica decorada con teselas, espirales doradas y patrones geometricos bizantinos de pan de oro auténtico sobre oleo.',
        'prompt_gemini': '"Retrato pictorico fotorrealista al estilo de Gustav Klimt (Secesion de Viena): elegante dama de perfil sereno con peinado recogido y mantilla sutil, envuelta en una grandiosa tunica cubierta de mosaicos dorados, espirales de pan de oro reluciente y texturas bizantinas. Fondo de laminas de oro envejecido con relieves brillantes bajo luz calida de atardecer. Oleo sobre lienzo con textura tangible. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling circular sutil y cinematografico alrededor de la dama. La luz dorada hace centellear las teselas y laminas de pan de oro de su tunica, creando reflejos tornasolados y un halo tenue de particulas de oro flotando en el aire calido de la estancia."',
        'color': (0.8, 0.6, 0.1)
    },
    {
        'session': 7,
        'tag': 'PRAC-007',
        'prefix': '3. PRAC-007',
        'title': 'Protagonista de Cine Negro y Misterio Clasico (Film Noir)',
        'desc': 'Recreacion fotografica de cine clasico de los anos 40 y 50: iluminacion expresionista con claroscuro marcado (sombras de persiana veneciana), sombrero fedora, gabardina con cuello alzado y un ambiente de intriga bajo farolas en noche lluviosa.',
        'prompt_gemini': '"Retrato fotografico en blanco y negro de pelicula de cine negro clasico (anos 40): detective veterano con sombrero fedora inclinado y gabardina clasica, apoyado en una esquina de adoquines mojados. Luz lateral dura proyectando sombras de persiana veneciana sobre su rostro reflexivo y el humo tenue de una alcantarilla. Atmosfera de suspense y lluvia fina. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling frontal lento acercandose a la mirada misteriosa del detective bajo el ala del sombrero. El vapor sube suavemente de los adoquines mojados y las gotas de lluvia rompen con destellos en el charco a sus pies."',
        'color': (0.3, 0.35, 0.4)
    },
    {
        'session': 7,
        'tag': 'INT-007',
        'prefix': '5. INT-007',
        'title': 'El Faro de Alejandria (120 m) con su Gran Espejo de Bronce',
        'desc': 'Reconstruccion arqueologica del interior del legendario Faro de Alejandria: la gran rampa helicoidal de piedra por donde subian carretas con lena, el horno de fuego colosal en la cumbre y el gigantesco espejo paraboloide de bronce pulido que proyectaba luz a 50 km mar adentro.',
        'prompt_gemini': '"Corte transversal e interior 3D hiperrealista del Faro de Alejandria en el ano 280 a.C.: en la cima, una gran fogata de lena aromatica arde con fuerza frente a un colosal espejo concavo de bronce bruñido que proyecta un haz de luz cegador sobre el mar Mediterraneo nocturno. Barcos antiguos navegando a lo lejos guiados por el destello. Humo denso y arquitectura de sillares de granito blanco. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Camara en vuelo de drone orbitando alrededor del fuego en la cima del faro. El gran espejo de bronce refleja las llamaradas danzantes mientras el haz de luz corta la noche estrellada sobre el oleaje del Mediterraneo."',
        'color': (0.15, 0.45, 0.75)
    },
    {
        'session': 7,
        'tag': 'FUT-007',
        'prefix': '6. FUT-007',
        'title': 'Ano 2042: Regeneracion de Organos 3D con Biotinta de Celulas Madre',
        'desc': 'Biomedicina regenerativa del futuro: bioimpresoras 3D de precision milimetrica fabricando corazones, rinones y valvulas biologicas utilizando celulas madre cultivadas del propio paciente, eliminando para siempre las listas de espera de trasplantes y el rechazo.',
        'prompt_gemini': '"Infografia medica 3D hiperrealista en un quirofano del ano 2042: un brazo robotico de bioimpresion 3D deposita finas capas de biotinta translucida con celulas madre vivas para formar un corazon humano completo dentro de una camara de cultivo esteril con fluidos nutricionales luminiscentes. Pantallas holograficas mostrando la vascularizacion coronaria y el latido autonomo. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Zoom in optico muy lento hacia la boquilla microscopica de la bioimpresora. La biotinta pulsa con luz bioelectrica azulada y el tejido celular recien formado comienza a latir suavemente dentro de la camara nutricional."',
        'color': (0.1, 0.6, 0.45)
    },
    {
        'session': 7,
        'tag': 'ARTE-007',
        'prefix': '8. ARTE-007',
        'title': 'El Hombre de Vitruvio de Leonardo da Vinci (1490)',
        'desc': 'El canon iconico de proporcion humana y conexion cosmica del Renacimiento: dibujo a pluma y tinta parda sobre papel verjurado, donde la figura humana desnuda se inscribe simultaneamente en un circulo (lo espiritual y divino) y un cuadrado (lo terrenal y geometrico).',
        'prompt_gemini': '"Estudio renacentista fotorrealista del Hombre de Vitruvio de Leonardo da Vinci sobre papel verjurado antiguo con bordes desgastados y manchas de tinta sepia: trazos minuciosos a pluma mostrando la doble postura de brazos y piernas inscrita en el circulo y el cuadrado perfectos. Anotaciones caligraficas especulares invertidas en italiano renacentista. Luz calida de vela sobre la mesa de trabajo. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Paneo diagonal suave recorriendo los trazos a pluma del dibujo desde el circulo exterior hasta el rostro sereno de la figura. Las sombras de la luz de vela tiemblan calidamente sobre la textura rugosa del papel antiguo."',
        'color': (0.55, 0.35, 0.15)
    },

    # ==========================================
    # SESIÓN 08
    # ==========================================
    {
        'session': 8,
        'tag': 'EST-008',
        'prefix': '2. EST-008',
        'title': 'SURREALISTA - Relojes Blandos en el Desierto Onirico',
        'desc': 'Atmosfera de sueno inspirada en Salvador Dali: relojes de bolsillo de oro derritiendose sobre ramas secas de olivo y acantilados petreos de Cadaques, bajo un cielo infinito y solitario que desafia las leyes del tiempo y la gravedad.',
        'prompt_gemini': '"Pintura surrealista al oleo fotorrealista al estilo de Salvador Dali: relojes de bolsillo dorados derritiendose suavemente como cera caliente sobre la rama de un arbol seco y sobre rocas pulidas de una playa solitaria. Al fondo, acantilados escarpados y un mar en calma absoluta bajo un cielo crepuscular de tonos dorados y violetas. Horizonte infinito y sombras alargadas. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling frontal lento y pausado sobre la llanura desertica. Las manecillas del reloj blando giran suavemente en camara lenta mientras las sombras de los acantilados se alargan con la brisa tibia del crepusculo."',
        'color': (0.8, 0.45, 0.1)
    },
    {
        'session': 8,
        'tag': 'PRAC-008',
        'prefix': '3. PRAC-008',
        'title': 'Mi Vocacion Sonada: Director de Orquesta Sinfonica en el Auditorio',
        'desc': 'Cumplir el sueno fotografico de subirte al podio del Teatro Real o la Filarmonica: batuta en mano frente a 80 musicos, partitura abierta sobre el atril dorado y la emocion de dirigir un concierto magistral bajo los focos escénicos.',
        'prompt_gemini': '"Fotografia editorial nitida y solemne: persona mayor jubilada en el podio de director de una gran orquesta sinfonica en un auditorio majestuoso de madera noble y terciopelo rojo. Viste frac elegante, sostiene la batuta en alto con gesto apasionado mientras violinistas y chelistas le miran concentrados. Focos calidos cenitales e iluminacion cinematografica. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Plano secuencia ascendente desde las cuerdas de los violines hasta el gesto emocionado del director al bajar la batuta en el primer compas. La orquesta cobra vida al unisono con la iluminacion calida del auditorio."',
        'color': (0.2, 0.35, 0.6)
    },
    {
        'session': 8,
        'tag': 'INT-008',
        'prefix': '5. INT-008',
        'title': 'El Panteon de Roma por Dentro: Oculo Solar y Cupula de Hormigon',
        'desc': 'La cupula de hormigon no armado mas grande jamas construida: 43 metros de diametro con casetones decrecientes y el magico oculo cenital abierto de 9 metros por donde entra un solido haz de luz solar que viaja por los marmoles imperiales como un reloj de sol divino.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista del interior del Panteon de Agripa en Roma al mediodia del equinoccio: un haz de luz solar solido y luminoso entra por el oculo circular de la gran cupula de casetones de hormigon aligerado, iluminando el pavimento de marmoles de colores (giallo antico y porfido). Visitantes contemplando la inmensidad del espacio con pebeteros encendidos. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Camara inclinada hacia arriba subiendo en travelling vertical por el cilindro del haz de luz solar hasta salir por el oculo al cielo azul romano, con motas de polvo dorado flotando en el rayo de luz."',
        'color': (0.65, 0.4, 0.15)
    },
    {
        'session': 8,
        'tag': 'FUT-008',
        'prefix': '6. FUT-008',
        'title': 'Ano 2045: Carne Cultivada Celular en Gastronomia Sostenible',
        'desc': 'La revolucion culinaria y etica del futuro: cortes selectos de carne wagyu y salmon producidos a partir de celulas madre en biorreactores alimentados por energias renovables, con idéntica textura, sabor y nutrientes pero con cero emisiones y sin sufrimiento animal.',
        'prompt_gemini': '"Infografia gastronomica y tecnologica 3D: en un restaurante de alta cocina del ano 2045, un chef experto emplata un jugoso filete de ternera cultivada celular sobre pizarra negra con guarnicion de microvegetales hidroponicos. Al fondo, a traves de una mampara de cristal esteril, se aprecian elegantes biorreactores de acero pulido y luz ambiental calida. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling circular cercano alrededor del plato recien cocinado. El vapor aromatico se eleva suavemente del filete dorado al punto, mostrando el brillo de los jugos y la textura fibrosa perfecta."',
        'color': (0.75, 0.3, 0.2)
    },
    {
        'session': 8,
        'tag': 'ARTE-008',
        'prefix': '8. ARTE-008',
        'title': 'La Virgen del Prado de Rafael Sanzio (1506)',
        'desc': 'La composicion triangular perfecta de armonia renacentista: la Virgen Maria sentada en un prado florido de la campina toscana sosteniendo con ternura a Jesus nino mientras San Juanito le ofrece la cruz de cana, con lago sereno y colinas azules al fondo.',
        'prompt_gemini': '"Recreacion pictorica clasica al oleo de La Virgen del Prado de Rafael Sanzio: composicion piramidal serena de la Virgen con manto azul ultramar y tunica roja carmin, velando los juegos de Jesus nino y San Juan Bautista nino entre amapolas y lirios silvestres. Paisaje toscano de suaves colinas y lago en calma bajo una luz diáfana y cristalina. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling horizontal muy suave acercandose a las miradas llenas de ternura entre la Virgen y los ninos. La brisa primaveral mueve levemente las flores del prado y el reflejo del sol en el lago toscano."',
        'color': (0.15, 0.4, 0.7)
    },

    # ==========================================
    # SESIÓN 09
    # ==========================================
    {
        'session': 9,
        'tag': 'EST-009',
        'prefix': '2. EST-009',
        'title': 'SURREALISTA - Cuadros en Ruinas Flotando en el Desierto',
        'desc': 'Misterio onirico y tiempo suspendido: marcos barrocos dorados flotando en el aire sobre una llanura desertica de arena fina, en cuyo interior se asoman mares embravecidos, constelaciones brillantes y arquitecturas imposibles.',
        'prompt_gemini': '"Pintura surrealista de estilo pictorico refinado: enormes marcos dorados barrocos flotan verticalmente en el aire sobre un desierto de arena blanca con dunas suaves. Cada marco funciona como una ventana magica a otra dimension (uno muestra una tormenta marina, otro una via lactea centelleante y otro un bosque verde). Sombras geometricas proyectadas en la arena. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Vuelo rasante de camara pasando a traves de uno de los marcos dorados flotantes, cambiando de la calma del desierto al oleaje nocturno de la dimension interior con un suave destello magico."',
        'color': (0.85, 0.5, 0.15)
    },
    {
        'session': 9,
        'tag': 'PRAC-009',
        'prefix': '3. PRAC-009',
        'title': 'Reconstruccion Digital de Objetos y Fotos Rotas Familiares',
        'desc': 'Restauracion con IA generativa (Inpainting): recuperar una taza antigua de porcelana quebrada, un jarron de Talavera hecho anicos o una foto de boda rota por la mitad, recomponiendo las partes que faltan con total fidelidad historica y nitidez.',
        'prompt_gemini': '"Fotografia antes y despues de restauracion patrimonial: en la mitad izquierda, un plato de ceramica de Talavera del siglo XIX quebrado en multiples pedazos con grietas visibles; en la mitad derecha, la misma pieza perfectamente reconstruida, con sus esmaltes azules y amarillos relucientes y superficie lisa impecable sobre fondo neutro de museo. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling frontal continuo mientras una linea de luz brillante barre de izquierda a derecha la ceramica rota, uniendo las piezas rotas en una transicion magica hasta dejarla impecable y brillante."',
        'color': (0.1, 0.5, 0.65)
    },
    {
        'session': 9,
        'tag': 'INT-009',
        'prefix': '5. INT-009',
        'title': 'Los Banos de Caracalla en Roma: Caldarium, Piscinas e Hipocausto',
        'desc': 'La monumentalidad termal de la Roma imperial: el gigantesco Caldarium circular con su cupula de 35 metros, piscinas de agua caliente bajo bovedas decoradas con estucos dorados, y en el subsuelo los hornos de hipocausto con esclavos alimentando el fuego.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista de las Termas de Caracalla en el ano 216 d.C.: en el piso superior, la grandiosa piscina del caldarium con vapor de agua ascendiendo entre columnas corintias de granito rojo y mosaicos de atletas; en el subsuelo, laberinto de hornos de ladrillo donde el fuego del hipocausto calienta el suelo radiante. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling descendente desde el vapor relajante de las piscinas superiores hasta el brillo rojizo de los hornos subterraneos del hipocausto, revelando la colosal ingenieria termica romana."',
        'color': (0.7, 0.25, 0.1)
    },
    {
        'session': 9,
        'tag': 'FUT-009',
        'prefix': '6. FUT-009',
        'title': 'Ano 2050: La Base Lunar Artemis-Shackleton Permanente',
        'desc': 'El primer asentamiento humano permanente en el Polo Sur de la Luna: cupulas inflables cubiertas de regolito lunar impreso en 3D para frenar la radiacion, paneles solares verticales sobre picos de luz eterna e invernaderos hidroponicos con lechugas lunares.',
        'prompt_gemini': '"Infografia aeroespacial 3D fotorrealista de la base lunar permanente en el crater Shackleton en el ano 2050: modulos habitacionales conectados por tuneles presurizados, excavadoras roboticas depositando regolito lunar protector, astronautas con trajes ligeros recogiendo hielo en la sombra del crater y la Tierra azul resplandeciendo en el horizonte negro estrellado. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Camara orbital de drone sobrevolando las cupulas lunares. Los rovers avanzan levantando polvo gris en gravedad baja mientras la Tierra gira majestuosamente en el cielo negro infinito."',
        'color': (0.2, 0.35, 0.6)
    },
    {
        'session': 9,
        'tag': 'ARTE-009',
        'prefix': '8. ARTE-009',
        'title': 'Venus de Urbino de Tiziano Vecellio (1538)',
        'desc': 'La cumbre del color y la sensualidad veneciana: la diosa del amor retratada como una dama renacentista recostada sobre sabanas de lino blanco y terciopelo rojo, con un perrito faldero durmiendo a sus pies (simbolo de fidelidad conyugal) y sirvientas al fondo.',
        'prompt_gemini': '"Recreacion al oleo hiperrealista de la Venus de Urbino de Tiziano: dama renacentista de cabellos dorados recostada con elegancia serena sobre un lecho con sabanas de saten blanco y colcha de terciopelo carmesi. A sus pies duerme un perrito spaniel. Al fondo, a traves de una estancia con columnas de marmol, doncellas buscan en un arcon nupcial bajo la luz calida veneciana. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling horizontal muy lento de derecha a izquierda recorriendo el lecho. La luz calida de Venecia acaricia los pliegues de terciopelo rojo mientras el perrito abre los ojos con parsimonia."',
        'color': (0.6, 0.2, 0.25)
    },

    # ==========================================
    # SESIÓN 10
    # ==========================================
    {
        'session': 10,
        'tag': 'EST-010',
        'prefix': '2. EST-010',
        'title': 'COMIC / MANGA Y HALFTONE RETRO - Tren Nevado Manga',
        'desc': 'Estilo de novela grafica japonesa clasica (halftone y tramas de puntos): un tren expreso de vapor cruzando a toda velocidad un puente de hierro sobre un desfiladero nevado en Hokkaido, con copos cayendo y humo denso en blanco y negro puro.',
        'prompt_gemini': '"Ilustracion estilo manga clasico y comic retro de los anos 70 con tramas de puntos halftone: locomotora de vapor de gran potencia cruzando un puente metalico en las montanas nevadas de Japon durante una ventisca. Fuertes contrastes de tinta china negra sobre papel blanco, lineas cineticas de velocidad y bocanadas de humo texturizadas con puntos. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling lateral a la velocidad del tren. Las ruedas de hierro giran velozmente echando chispas, el humo blanco envuelve el puente y los copos de nieve pasan zumbando frente a la camara."',
        'color': (0.2, 0.25, 0.3)
    },
    {
        'session': 10,
        'tag': 'PRAC-010',
        'prefix': '3. PRAC-010',
        'title': 'Restauracion Digital de Monumentos Historicos con IA',
        'desc': 'Rehabilitacion virtual del patrimonio espanol: limpiar grafitis, reponer sillares de piedra caidos y restaurar molduras barrocas en una ermita romanica o portada renacentista mediante IA generativa, preservando la pátina del tiempo.',
        'prompt_gemini': '"Fotografia de restauracion arquitectonica con IA: la portada renacentista de una colegiata espanola dividida en dos mitades; en la izquierda muestra sillares con manchas de humedad, grietas y piezas erosionadas; en la derecha luce perfectamente consolidada, con piedra caliza limpia, relieves escultoricos restaurados y sin alteraciones invasivas. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Paneo vertical ascendente desde los escalones de piedra limpios hasta las arquivoltas restauradas de la portada, destacando los detalles esculpidos bajo la luz calida del sol castellano."',
        'color': (0.6, 0.45, 0.25)
    },
    {
        'session': 10,
        'tag': 'INT-010',
        'prefix': '5. INT-010',
        'title': 'La Mitica Atlantida con sus Anillos Concentricos de Agua y Palacios',
        'desc': 'La ciudad ideal descrita por Platon: tres anillos colosales de mar y tierra conectados por canales navegables, puentes monumentales cubiertos de oricalco reluciente y en la colina central el gran templo de Poseidon con estatuas de oro.',
        'prompt_gemini': '"Vista aerea y corte transversal 3D fotorrealista de la capital de la Atlantida segun el relato de Platon: tres murallas circulares concentricas revestidas de bronce, estano y oricalco rojo brillante, separadas por canales de agua turquesa donde navegan trirremes. En el centro elevado, el colosal templo de Poseidon con fuentes de agua fria y caliente. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Vuelo de camara descendente desde las nubes doradas sobrevolando en espiral los anillos de agua y palacios de oricalco hasta posarse en las escalinatas del gran templo de Poseidon."',
        'color': (0.1, 0.45, 0.65)
    },
    {
        'session': 10,
        'tag': 'FUT-010',
        'prefix': '6. FUT-010',
        'title': 'Ano 2055: Uteros Artificiales Bio-Sinteticos (Ectogenesis)',
        'desc': 'Medicina neonatal avanzada para prematuridad extrema: camaras bio-sinteticas que replican con exactitud el fluido amniotico, la oxigenacion por cordon umbilical artificial y los latidos maternos, garantizando el desarrollo seguro de bebes de 22 semanas sin secuelas.',
        'prompt_gemini': '"Infografia cientifica y medica hiperrealista en un centro neonatal de alta tecnologia del ano 2055: modulos transparentes ovales de ectogenesis donde bebes prematuros flotan serenamente en liquido amniotico bio-sintetico regulado a 37°C. Tubos umbilicales biocompatibles suministran oxigeno y nutrientes mientras monitores holograficos proyectan el desarrollo pulmonar. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Zoom in optico muy suave hacia la capsula de incubacion. Los latidos ritmicos generan ondas suaves en el fluido amniotico mientras una luz calida acaricia las manitas del bebe en reposo."',
        'color': (0.2, 0.55, 0.5)
    },
    {
        'session': 10,
        'tag': 'ARTE-010',
        'prefix': '8. ARTE-010',
        'title': 'El Matrimonio Arnolfini de Jan van Eyck (1434)',
        'desc': 'La obra cumbre del Renacimiento flamenco y el detalle microscopico: la pareja nupcial en su alcoba flamenca, los zuecos de madera en el suelo, la lampara de laton con una sola vela encendida y el celebre espejo convexo al fondo donde se refleja el propio pintor.',
        'prompt_gemini': '"Recreacion al oleo fotorrealista de El Matrimonio Arnolfini de Jan van Eyck: Giovanni Arnolfini y su esposa tomados de la mano en una alcoba de Brujas con luz lateral de ventana. Destacan el rico ropaje de terciopelo verde y capa de piel de marta, la lampara de laton dorado bruñido y el espejo circular convexo en la pared del fondo reflejando la estancia entera. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling frontal continuo avanzando entre la pareja hasta sumergir la mirada en el espejo convexo del fondo, donde se aprecia con nitidez milimetrica el reflejo del pintor saludando en la puerta."',
        'color': (0.25, 0.45, 0.25)
    },

    # ==========================================
    # SESIÓN 11
    # ==========================================
    {
        'session': 11,
        'tag': 'EST-011',
        'prefix': '2. EST-011',
        'title': 'COMIC / MANGA Y HALFTONE RETRO - Serie Retratos Grabado Pop Art',
        'desc': 'Homenaje al Pop Art de Roy Lichtenstein y el grabado vintage: retratos expresivos de personas mayores con tramas de puntos Benday gigantes, bordes negros gruesos y colores primarios puros saturados (amarillo, azul cyan y rojo fuego).',
        'prompt_gemini': '"Retrato estilo Pop Art retro inspirado en Roy Lichtenstein: rostro de perfil de un abuelo sonriente con gafas de pasta, delineado con trazos de tinta gruesos y coloreado mediante tramas de puntos Benday de color cyan y magenta. Fondo amarillo canario con bocadillo de comic de texto clasico y textura de papel de periodico antiguo. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling rapido con zoom in hacia las gafas del personaje. Los puntos Benday de la trama cobran volumen tridimensional como esferas de colores brillantes que laten al ritmo del Pop Art."',
        'color': (0.85, 0.2, 0.25)
    },
    {
        'session': 11,
        'tag': 'PRAC-011',
        'prefix': '3. PRAC-011',
        'title': 'Reinterpretacion Fantastica de Lugares Conocidos de tu Ciudad',
        'desc': 'Creatividad visual desbordante con Gemini: transformar la plaza mayor de tu pueblo o la Gran Via de Madrid en una ciudad flotante entre nubes, un bosque magico con farolas de enredadera o una estacion espacial futurista.',
        'prompt_gemini': '"Fotografia hiperrealista transformando la Gran Via de Madrid en un valle magico futurista: los edificios clasicos de piedra blanca estan cubiertos por jardines verticales exuberantes y cascadas de agua cristalina que caen entre balcones; por la calzada no hay coches sino un rio navegable con barcas solares de madera y cielo azul radiante. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Vuelo de drone descendiendo por el canon de la Gran Via renacida. El agua de las cascadas salpica suavemente y las barcas navegan entre reflejos esmeralda bajo la brisa fresca matinal."',
        'color': (0.1, 0.6, 0.4)
    },
    {
        'session': 11,
        'tag': 'INT-011',
        'prefix': '5. INT-011',
        'title': 'Machu Picchu por Dentro: Acueductos en Terraza y Canales de Piedra',
        'desc': 'La genialidad hidraulica inca: terrazas agricolas escalonadas con drenajes subterraneos de cascajo para resistir lluvias torrenciales, y una red de 16 fuentes litúrgicas de piedra tallada donde el agua de manantial fluia sin interrupcion hasta el Templo del Sol.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista de la ciudadela inca de Machu Picchu mostrando su sistema hidraulico subterraneo: capas de grava y arena bajo las terrazas agricolas para filtrar la lluvia sin deslizamientos, canales de piedra granitica pulida conduciendo el agua a las 16 fuentes de la ciudadela y el Templo del Sol al amanecer entre la niebla andina. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Camara siguiendo el curso del agua cristalina por el canal de piedra pulida, saltando de fuente en fuente hasta abrir el plano a la inmensidad de las montanas verdes de los Andes."',
        'color': (0.2, 0.5, 0.25)
    },
    {
        'session': 11,
        'tag': 'FUT-011',
        'prefix': '6. FUT-011',
        'title': 'Ano 2058: Ciber-Protesis Bionicas Neuro-Conectadas con Tacto',
        'desc': 'El fin de la discapacidad motora: manos y piernas bionicas de fibra de carbono y titanio conectadas directamente a las terminaciones nerviosas del paciente, capaces de transmitir sensaciones tactiles reales (temperatura, textura de seda y presion milimetrica).',
        'prompt_gemini': '"Infografia biomedica 3D: primer plano de una mano bionica ultrafina de titanio satinado y fibra de carbono acariciando un tejido de seda roja. Haces de luz de fibra optica en la muneca indican la transmision de impulsos sensoriales directamente a los nervios biologicos del brazo. Pantalla de diagnostico mostrando la respuesta sinaptica instantanea. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling circular en torno a los dedos bionicos mientras palpan la seda. Las luces de los sensores tactiles parpadean en tonos dorados mostrando el flujo neuronal continuo y fluido."',
        'color': (0.35, 0.4, 0.55)
    },
    {
        'session': 11,
        'tag': 'ARTE-011',
        'prefix': '8. ARTE-011',
        'title': 'Las Meninas de Diego Velazquez (1656)',
        'desc': 'La joya indiscutible del Museo del Prado y el misterio del aire pintado: el taller del pintor en el Alcazar de Madrid con la infanta Margarita rodeada de sus damas, el perro mastin reposando, Velazquez ante su enorme lienzo y los reyes reflejados en el espejo del fondo.',
        'prompt_gemini': '"Recreacion al oleo fotorrealista de Las Meninas de Diego Velazquez: la infanta Margarita con vestido de guardainfante blanco dorado recibe agua en un búcaro rojo de su dama Menina. A la izquierda, Velazquez con la cruz de Santiago en el pecho sostiene su paleta y pincel. La luz dorada entra por la ventana derecha iluminando el polvo en suspension y el espejo del fondo con los monarcas. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling frontal lento adentrandose en la estancia del Alcazar. La luz se cuela entre los personajes revelando la atmosfera eterea de Velazquez hasta enfocar la puerta abierta donde saluda Jose Nieto."',
        'color': (0.5, 0.35, 0.2)
    },

    # ==========================================
    # SESIÓN 12
    # ==========================================
    {
        'session': 12,
        'tag': 'EST-012',
        'prefix': '2. EST-012',
        'title': 'PIXEL ART - Cafeteria Retro 16-Bit en Noche Lluviosa',
        'desc': 'Nostalgia de los videojuegos clasicos de los 90: cafeteria acogedora vista desde la calle a traves de una ventana empanada por la lluvia, con luces de neon parpadeando, una taza de cafe humeante y un gato durmiendo sobre el mostrador de madera pixelada.',
        'prompt_gemini': '"Ilustracion en pixel art impecable estilo 16-bit (Super Nintendo): interior de una cafeteria acogedora vista desde la calle empedrada en una noche lluviosa. Luces de neon calidas en tonos naranja y violeta, vapor pixelado saliendo de una taza de cafe sobre una mesa de madera y un gato atigrado durmiendo en el alfeizar de la ventana con gotas de lluvia cayendo. Paleta de colores cuidada. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Animacion pixel art con movimiento fluido de lluvia constante. Las luces de neon titilan suavemente, el humo del cafe sube en espirales de pixeles y las gotas resbalan por el cristal de la ventana."',
        'color': (0.35, 0.2, 0.5)
    },
    {
        'session': 12,
        'tag': 'PRAC-012',
        'prefix': '3. PRAC-012',
        'title': 'De Boceto Infantil a Fotografia Real 8K (Sketch to Real)',
        'desc': 'La magia de convertir el garabato de un nieto en una escena de cine: tomar un dibujo infantil a lapiz de colores (una casa con chimenea torcida y un sol sonriente) y pedirle a Gemini que lo transforme en una fotografia arquitectonica de ensueno.',
        'prompt_gemini': '"Comparativa visual antes y despues: en el lado izquierdo, un tierno dibujo infantil hecho con ceras de colores de una casita de campo con chimenea humeante, un gran arbol y un sol brillante; en el lado derecho, la misma escena convertida en una impresionante fotografia hiperrealista 8K de una cabana de piedra real en un prado alpino con luz de amanecer y naturaleza exuberante. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Transicion cinematografica fluida donde los trazos de cera de colores se van disolviendo para revelar la piedra real de la cabana, el movimiento de la hierba fresca y el humo calido saliendo de la chimenea."',
        'color': (0.8, 0.45, 0.15)
    },
    {
        'session': 12,
        'tag': 'INT-012',
        'prefix': '5. INT-012',
        'title': 'Santa Sofia de Constantinopla: Cupula Flotante sobre Pechinas',
        'desc': 'La joya bizantina de la arquitectura sagrada: una cupula colosal de 31 metros que parece suspendida en el aire sobre cuatro pechinas triangulares y 40 ventanas en la base, por donde entra un halo de luz celestial que hace brillar millones de teselas doradas.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista del interior de la Basilica de Santa Sofia en el siglo VI: la inmensa cupula dorada parece levitar gracias a la corona de 40 ventanas de arco en su base que inundan de luz dorada las pechinas de marmol verde de Tesalia y porfido rojo. Mosaicos bizantinos resplandeciendo bajo candelabros circulares de bronce suspendidos de cadenas. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Camara ascendiendo lentamente en plano cenital hacia el vertice de la cupula. La luz que entra por las 40 ventanas crea una corona dorada radiante mientras los cantos sagrados parecen resonar en el aire."',
        'color': (0.75, 0.55, 0.15)
    },
    {
        'session': 12,
        'tag': 'FUT-012',
        'prefix': '6. FUT-012',
        'title': 'Ano 2060: Hoteles Orbitales con Gravedad y Cupula a la Tierra',
        'desc': 'El turismo espacial para todas las edades: una gran rueda giratoria en orbita baja que genera gravedad artificial similar a la Tierra, con salones de descanso panoramicos donde los viajeros disfrutan de un cafe mientras contemplan amaneceres orbitales cada 90 minutos.',
        'prompt_gemini': '"Infografia 3D fotorrealista del salon panoramico de un hotel orbital en el ano 2060: amplios ventanales curvos de suelo a techo a traves de los cuales se contempla la Tierra azul con la peninsula iberica iluminada por el sol naciente. En el interior confortable, personas mayores sentadas comodamente en sillones de diseno con gravedad artificial, servidos por camareros roboticos amables. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling lateral muy lento por el ventanal panoramico. La curva azul de la Tierra y la atmosfera brillante se desplazan serenamente bajo las estrellas en el silencio majestuoso del espacio."',
        'color': (0.1, 0.35, 0.65)
    },
    {
        'session': 12,
        'tag': 'ARTE-012',
        'prefix': '8. ARTE-012',
        'title': 'La Joven de la Perla de Johannes Vermeer (1665)',
        'desc': 'La Mona Lisa del Norte y el dominio de la luz holandesa: el retrato intimo de la joven con turbante oriental azul y amarillo volviendose hacia el espectador con labios entreabiertos, iluminada por el destello perfecto de un pendiente de perla con brillo de lagrima.',
        'prompt_gemini': '"Recreacion al oleo hiperrealista de La Joven de la Perla de Johannes Vermeer: joven de mirada enigmatica y labios humedos entreabiertos volviendose sobre su hombro hacia el espectador sobre un fondo oscuro profundo. Destacan el turbante de seda azul ultramar con caida dorada y el extraordinario pendiente de perla en forma de lagrima que refleja la luz pura de la ventana. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Zoom in optico muy lento hacia el brillo nacarado de la perla en la oreja. La perla destella con suavidad mientras la mirada serena de la joven parece cobrar vida con un parpadeo tenue."',
        'color': (0.2, 0.45, 0.6)
    },

    # ==========================================
    # SESIÓN 13
    # ==========================================
    {
        'session': 13,
        'tag': 'EST-013',
        'prefix': '2. EST-013',
        'title': 'HDR (HIGH DYNAMIC RANGE) - Calles Empedradas de Toledo al Atardecer',
        'desc': 'Fotografia de alto rango dinamico con maxima riqueza tonal: callejon historico de Toledo empedrado de canto rodado, fachadas de ladrillo mudejar y yeserias, sombras profundas sin empastar y el cielo de poniente encendido en tonos cobrizos y dorados.',
        'prompt_gemini': '"Fotografia HDR fotorrealista de una calle estrecha y empinada del casco historico de Toledo al atardecer: adoquines pulidos y mojados reflejando la luz calida de los faroles de forja recien encendidos. Fachadas de ladrillo mudejar y rejas castellanas con macetas floridas. Maximo rango dinamico entre las sombras nitidas y el cielo de poniente naranja cobrizo sobre la torre de la catedral. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling hacia adelante a ras del suelo por el callejon empedrado. Los reflejos dorados bailan sobre los charcos de agua limpia mientras las campanas de la catedral suenan a lo lejos al atardecer."',
        'color': (0.8, 0.45, 0.2)
    },
    {
        'session': 13,
        'tag': 'PRAC-013',
        'prefix': '3. PRAC-013',
        'title': 'De Captura de Mapa Satelital a Vista Fotorrealista a Pie de Calle',
        'desc': 'De la vista satelital plana a la realidad inmersiva: tomar una captura aerea cenital de Google Maps (de una casa de campo, un pueblo o un monumento) y pedirle a Gemini que reconstruya la escena fotorrealista vista desde los ojos de un peaton en la acera.',
        'prompt_gemini': '"Comparativa visual 3D: en la parte superior, una captura aerea satelital plana de una plaza de pueblo espanol con su fuente central y arboleda; en la parte inferior, la reconstruccion hiperrealista a nivel de calle con iluminacion de manana soleada, bancos de piedra con vecinos charlando, palomas bebiendo en la fuente y soportales de madera con sombras suaves. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Plano secuencia en picado que desciende desde la vista aerea cenital hasta situarse a nivel de suelo entre los vecinos de la plaza, con una transicion visual fluida y natural."',
        'color': (0.2, 0.5, 0.4)
    },
    {
        'session': 13,
        'tag': 'INT-013',
        'prefix': '5. INT-013',
        'title': 'La Ciudad Prohibida de Pekin: El Gran Salon de la Armonia Suprema',
        'desc': 'El corazon imperial de la dinastia Ming: el Salon Taihe con sus colosales columnas de madera de nanmu dorado, el Trono del Dragon esculpido en oro macizo sobre nueve escalinatas y el suelo de ladrillos de oro que suenan como campanas de bronce.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista del Gran Salon de la Armonia Suprema en la Ciudad Prohibida de Pekin en el siglo XV: inmensas columnas de madera dorada sosteniendo techos artesonados con dragones entrelazados. En el centro elevado sobre una plataforma de marmol blanco, el deslumbrante Trono del Dragon de oro con pebeteros de bronce con forma de grulla humeando incienso. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling frontal solemne recorriendo la alfombra roja central hacia el Trono del Dragon. El humo aromatico se eleva en volutas doradas iluminadas por los rayos de sol que entran por las celosias."',
        'color': (0.85, 0.3, 0.15)
    },
    {
        'session': 13,
        'tag': 'FUT-013',
        'prefix': '6. FUT-013',
        'title': 'Ano 2063: Red Hyperloop de Levitacion Magnetica a 1200 km/h',
        'desc': 'Transporte ultrarrapido sostenible entre ciudades: capsulas aerodinamicas que levitan mediante superconductores dentro de tubos de acero al vacio sellados, uniendo Madrid y Barcelona en apenas 35 minutos sin ruidos, turbulencias ni consumo de combustibles fosiles.',
        'prompt_gemini': '"Infografia de transporte futurista 3D: corte transversal de un tubo de transporte Hyperloop sellado al vacio en el ano 2063. Una capsula aerodinamica de levitacion magnetica pasiva vuela a 1200 km/h guiada por bobinas superconductoras. A traves del lateral transparente de la capsula se ve a pasajeros relajados leyendo y tomando un cafe mientras monitores muestran el trayecto Madrid-Paris. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Camara persiguiendo a gran velocidad la capsula magnetica por el interior del tubo iluminado con anillos LED azules, con un zumbido electromagnetico suave y sensacion de suavidad absoluta."',
        'color': (0.1, 0.4, 0.7)
    },
    {
        'session': 13,
        'tag': 'ARTE-013',
        'prefix': '8. ARTE-013',
        'title': 'La Ronda de Noche de Rembrandt van Rijn (1642)',
        'desc': 'El claroscuro magistral y el dinamismo barroco holandes: la compania de milicianos del capitan Frans Banninck Cocq saliendo de un portal sombrio bajo un foco de luz teatral que ilumina con brillo magico a una misteriosa nina con un pollo colgado del cinto.',
        'prompt_gemini': '"Recreacion pictorica al oleo de La Ronda de Noche de Rembrandt: el capitan Frans Banninck Cocq de riguroso negro con banda roja y su teniente de jubon amarillo oro dan la orden de marcha a la guardia civica. En medio de la penumbra teatral, una nina vestida de oro resplandece como un foco de luz magica entre picas, mosquetes y tambores en movimiento. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling lateral con movimiento de camara siguiendo el paso adelante del capitan y su teniente. La luz barroca de Rembrandt hace brillar los cascos de acero y el tamborilero marca el paso."',
        'color': (0.55, 0.35, 0.15)
    },

    # ==========================================
    # SESIÓN 14
    # ==========================================
    {
        'session': 14,
        'tag': 'EST-014',
        'prefix': '2. EST-014',
        'title': 'HDR (HIGH DYNAMIC RANGE) - Bodegon del Mar y Redes Marineras',
        'desc': 'Bodegon marinero mediterraneo con nitidez cristalina: cesta de mimbre con bogavantes rojos, salmonetes de roca y sardinas brillantes sobre una mesa de madera de barco carcomida por el salitre, redes de cáñamo y boyas de cristal bajo luz limpia de puerto.',
        'prompt_gemini': '"Fotografia HDR fotorrealista de un bodegon marinero tradicional en un puerto pesquero gallego: mesa de madera desgastada con salitre donde reposa una cesta con pescados de roca frescos de escamas irisadas, un bogavante de caparazon rojo vivo, redes de canamo mojadas y un cuchillo de mango de madera. Luz limpia y diáfana con gotas de agua cristalinas brillando. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling circular cercano alrededor de la mesa marinera. El agua de las escamas gotea suavemente sobre la madera del barco y la brisa del puerto mece una red con boyas de cristal verde."',
        'color': (0.15, 0.5, 0.6)
    },
    {
        'session': 14,
        'tag': 'PRAC-014',
        'prefix': '3. PRAC-014',
        'title': 'De Fotografia Retrato a Diseno de Tatuaje Minimalista de Trazo Fino',
        'desc': 'Diseno grafico familiar con IA: convertir el retrato fotografico de un nieto o de una mascota en un elegante diseno de tatuaje lineal a un solo trazo continuo (Single Line Art) minimalista y poetico, ideal para grabar en joyeria o tatuarse con discrecion.',
        'prompt_gemini': '"Comparativa grafica elegante: a la izquierda, la fotografia de primer plano de un perro labrador con mirada carinosa; a la derecha, la transformacion artistica en ilustracion minimalista de una sola linea continua (Single Line Art) trazada con tinta negra fina sobre piel limpia, capturando con sutileza y precision la silueta y emocion del animal. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Animacion donde una pluma de tinta dibuja en tiempo real el trazo lineal continuo sobre el lienzo blanco, completando con fluidez la silueta emotiva del perro hasta el ultimo detalle."',
        'color': (0.3, 0.3, 0.35)
    },
    {
        'session': 14,
        'tag': 'INT-014',
        'prefix': '5. INT-014',
        'title': 'Tenochtitlan por Dentro: Calzadas, Chinampas y Templo Mayor',
        'desc': 'La colosal metropoli azteca flotando en el lago de Texcoco: calzadas de piedra con puentes levadizos, huertos flotantes (chinampas) rebosantes de maiz y flores, y el sagrado Templo Mayor bicéfalo dedicado a Tlaloc y Huitzilopochtli.',
        'prompt_gemini': '"Corte transversal 3D fotorrealista de la ciudad lacustre de Tenochtitlan en el ano 1500: la gran calzada de Iztapalapa cortando las aguas del lago Texcoco con canoas navegando entre huertos flotantes (chinampas) de flores y maiz. Al fondo, el recinto sagrado con el Templo Mayor policromado en rojo y azul, pebeteros de copal humeando y los volcanes nevados al horizonte. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Vuelo rasante en canoa deslizandose por los canales entre las chinampas floridas hasta enfocar la imponente mole del Templo Mayor alzandose hacia el cielo azul mesoamericano."',
        'color': (0.7, 0.3, 0.15)
    },
    {
        'session': 14,
        'tag': 'FUT-014',
        'prefix': '6. FUT-014',
        'title': 'Ano 2065: Desalinizadoras Solares de Grafeno y Oasis en el Sahara',
        'desc': 'El milagro del agua dulce inagotable: membranas de grafeno nanoporoso que desalan agua de mar con energia solar termica al 99% de eficiencia, canalizando rios artificiales que reverdecen valles deserticos convirtiendolos en granjas agricolas.',
        'prompt_gemini': '"Infografia medioambiental 3D en el desierto del Sahara en el ano 2065: una gigantesca planta desalinizadora de arquitectura bio-morfica alimentada por torres solares de concentracion. Membranas de grafeno translucidas filtran agua de mar que sale como rios caudalosos de agua potable, transformando las dunas amarillas en campos de cultivo verdes y palmerales densos. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling aereo sobrevolando el canal de agua cristalina que nace en la desalinizadora solar y avanza transformando la arena seca en vergel verde lleno de cultivos y vida vegetal."',
        'color': (0.1, 0.6, 0.45)
    },
    {
        'session': 14,
        'tag': 'ARTE-014',
        'prefix': '8. ARTE-014',
        'title': 'La Leccion de Anatomia del Dr. Nicolaes Tulp de Rembrandt (1632)',
        'desc': 'El amanecer de la ciencia medica moderna y la luz barroca: el celebre cirujano diseca con pinzas los tendones del brazo izquierdo de un cadaver mientras siete medicos de gorgueras blancas contemplan hipnotizados la maquinaria biologica humana.',
        'prompt_gemini': '"Recreacion al oleo hiperrealista de La Leccion de Anatomia del Dr. Nicolaes Tulp de Rembrandt: en un anfiteatro anatomico en penumbra, el doctor Tulp con sombrero negro levanta con unas pinzas metalicas los flexores del brazo del cuerpo disecado. Siete cirujanos con cuellos de gorguera blanca se inclinan hacia adelante con miradas cientificas fascinadas bajo una potente luz cenital. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Zoom in lento y respetuoso hacia el gesto quirurgico de las pinzas sosteniendo el tendon y las miradas atentas de los doctores, con la luz dorada de Rembrandt esculpiendo cada rostro."',
        'color': (0.5, 0.3, 0.15)
    },

    # ==========================================
    # SESIÓN 15
    # ==========================================
    {
        'session': 15,
        'tag': 'EST-015',
        'prefix': '2. EST-015',
        'title': 'BLANCO Y NEGRO (MONOCROMATICO) - Anciano Violinista en Teatro',
        'desc': 'La emocion del blanco y negro puro y el retrato psicologico: un anciano musico de manos arrugadas y mirada llena de memoria ensayando en solitario con su violin en el foso de un teatro antiguo vacio, bajo un unico foco cenital de luz de plata.',
        'prompt_gemini': '"Retrato fotografico en blanco y negro monocromatico puro con rica escala de grises: un anciano violinista de cabello canoso y manos curtidas toca su instrumento con los ojos cerrados en medio del foso vacio de un teatro clasico de opera. Unico foco de luz cenital de plata esculpiendo las arrugas nobles de su frente, la madera barnizada del violin y el polvo danzando en el aire. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling circular muy lento alrededor del violinista mientras sus dedos se deslizan con maestria por las cuerdas. Las motas de polvo brillan en el rayo de luz cenital como notas flotantes."',
        'color': (0.25, 0.25, 0.3)
    },
    {
        'session': 15,
        'tag': 'PRAC-015',
        'prefix': '3. PRAC-015',
        'title': 'Extraccion y Aislamiento 3D de un Objeto Familiar con Fondo Puro',
        'desc': 'Fotografia de catalogo profesional en casa: recortar con precision milimetrica un objeto querido (un reloj antiguo de bolsillo, unas gafas o una medalla militar) y colocarlo flotando sobre fondo blanco puro con sombras realistas para vender o catalogar.',
        'prompt_gemini': '"Fotografia de producto editorial y aislamiento 3D: un reloj de bolsillo de oro antiguo con cadena de eslabones perfectamente recortado y flotando en un angulo de 45 grados sobre fondo blanco puro de estudio. Reflejos metalicos nitidos en la tapa grabada, cristal pulido y sombra de contacto suave proyectada en la base. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Giro orbital de 360 grados del reloj de bolsillo suspendido en el aire. Los reflejos dorados y los grabados de la tapa deslumbran con suavidad bajo la luz de estudio impecable."',
        'color': (0.7, 0.5, 0.1)
    },
    {
        'session': 15,
        'tag': 'INT-015',
        'prefix': '5. INT-015',
        'title': 'La Ciudadela de Petra: El Tesoro (Al-Khazneh) Tallado en la Roca',
        'desc': 'La maravilla nabatea esculpida en la arenisca roja del desfiladero del Siq: la fachada monumental helenistica de 40 metros de altura y sus camaras interiores secretas donde las caravanas de incienso y mirra comerciaban hace dos mil anos.',
        'prompt_gemini': '"Corte transversal 3D e interior arqueologico del Tesoro de Petra (Al-Khazneh) en Jordania al amanecer: la monumental fachada clasica tallada directamente en la roca arenisca rosa emerge al final del estrecho desfiladero del Siq. En el interior de la gran camara cuadrada, comerciantes nabateos con tunicas revisan arcones de incienso bajo la luz calida de pebeteros. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Avanzar a paso de dromedario por la estrecha garganta rocosa del Siq en penumbra hasta que se abre de golpe la hendidura revelando la majestuosa fachada rosada del Tesoro banada por el sol matinal."',
        'color': (0.75, 0.35, 0.2)
    },
    {
        'session': 15,
        'tag': 'FUT-015',
        'prefix': '6. FUT-015',
        'title': 'Ano 2070: Primera Ciudad en Marte bajo Cupulas de Diamante',
        'desc': 'El gran salto de la civilizacion interplanetaria: la metropoli de Ares Vallis Capitol en el planeta rojo, albergando a 50.000 habitantes bajo gigantescas cupulas geodesicas de carbono sintetico con lagos artificiales, vegetacion terrestre y vistas a las lunas Fobos y Deimos.',
        'prompt_gemini': '"Infografia aeroespacial 3D fotorrealista de la primera gran ciudad humana en Marte en el ano 2070: inmensas cupulas geodesicas de carbono transparente en el canon de Ares Vallis que protegen una urbe verde con arboles terrestres, lagos artificiales y monorrailes flotantes. Fuera de las cupulas, el paisaje marciano rojizo con rovers solares y las dos lunas Fobos y Deimos en el cielo de color salmon. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling aereo descendente desde la orbita marciana atravesando la cupula geodesica transparente para descender sobre los jardines arbolados y avenidas de la ciudad marciana."',
        'color': (0.8, 0.3, 0.15)
    },
    {
        'session': 15,
        'tag': 'ARTE-015',
        'prefix': '8. ARTE-015',
        'title': 'La Encajera de Johannes Vermeer (1670)',
        'desc': 'El homenaje a la concentracion y la labor paciente y artesana: la joven holandesa inclinada sobre su almohadilla tejiendo encaje de bolillos con aguja y finos hilos de seda blanca y roja que caen como gotas de luz desde un libro forrado de terciopelo.',
        'prompt_gemini': '"Recreacion al oleo hiperrealista de La Encajera de Johannes Vermeer: joven artesana de cabello recogido con trenzas inclinada con concentracion absoluta sobre su labor de encaje de bolillos. Viste corpiño amarillo mostaza y cuello blanco. Hilos de seda roja y blanca fluyen de su almohadilla de coser sobre un tapiz floral con luz de ventana matinal destacando cada textura. REGLA DE ORO DE IDIOMA: 100% en espanol."',
        'prompt_flow': '"Travelling microscopico acercandose a los dedos agiles de la encajera moviendo los bolillos de madera, con los hilos de seda brillando delicadamente bajo la luz holandesa."',
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

def update_all_image_fiches():
    print("=================================================================")
    print("=== [ACTUALIZANDO 45 FICHAS DE IMAGEN (S07 A S15) CON GOOGLE FLOW] ===")
    print("=================================================================")
    
    total = len(IMAGE_WORKSHEETS_DATA)
    count = 0
    for item in IMAGE_WORKSHEETS_DATA:
        s_num = item['session']
        s_folder = os.path.join(SESSIONS_BASE, f"{s_num:02d}_Sesion")
        target_file = find_target_filename(s_folder, item['prefix'])
        
        if not target_file:
            print(f"⚠️ No se encontró archivo existente para {item['prefix']} en {s_folder}")
            target_file = f"{item['prefix']}_{item['title'].replace(':', '_')}.pdf"
            
        full_path = os.path.join(s_folder, target_file)
        build_image_worksheet(
            output_path=full_path,
            session_num=s_num,
            tag_code=item['tag'],
            num_str=item['prefix'],
            title=item['title'],
            desc_concept=item['desc'],
            prompt_gemini=item['prompt_gemini'],
            prompt_flow=item['prompt_flow'],
            theme_color_rgb=item['color']
        )
        count += 1

    print("=================================================================")
    print(f"🎉 ¡COMPLETADO CON ÉXITO: {count}/{total} FICHAS DE IMAGEN ACTUALIZADAS CON FLOW!")
    print("=================================================================")

if __name__ == '__main__':
    update_all_image_fiches()
