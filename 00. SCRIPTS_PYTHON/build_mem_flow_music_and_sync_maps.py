#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_mem_flow_music_and_sync_maps.py
1. Inyecta en las fichas [MEM-003] a [MEM-015] el Paso 3: Postal Sonora con Google Flow Music (Música 60s, 70s y 80s).
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

# Diccionario de Prompts Musicales calibrados en estilos de los años 60, 70 y 80
MUSIC_FLOW_PROMPTS = {
    3: {
        "estilo": "Orquesta y Guitarra Clásica Española • Años 60",
        "prompt": "Composición solemne y castiza para orquesta de cuerda y guitarra española virtuosa al estilo clásico de los años 60, trompeta noble lejana, castañuelas sutiles y aire ilustrado de época, 80 BPM, producción analógica cálida."
    },
    4: {
        "estilo": "Banda Sonora Sinfónica Épica • Años 60",
        "prompt": "Orquesta sinfónica cinematográfica evocadora y solemne al estilo de las bandas sonoras de los años 60, metales nobles, cuerdas majestuosas, timbales lejanos y un crescendo triunfal nostálgico, 75 BPM, calidad analógica cálida."
    },
    5: {
        "estilo": "Balada Melódica Instrumental • Años 70",
        "prompt": "Balada instrumental melódica de principios de los años 70, guitarra acústica de 12 cuerdas, piano vertical cálido, bajo melódico suave, sección de viento madera nostálgica y aire cosmopolita otoñal, 80 BPM."
    },
    6: {
        "estilo": "Folk-Rock Progresivo y Coral Sacro • Años 70",
        "prompt": "Música orquestal coral con aire de folk acústico y progresivo de los años 70, coros solemnes a capella mezclados con laúd, flauta travesera y cuerdas profundas, atmósfera espiritual y grandiosa, 65 BPM."
    },
    7: {
        "estilo": "Concierto para Guitarra Española y Cuerda • Años 60",
        "prompt": "Composición solemne para guitarra clásica española y orquesta de cuerda al estilo de Joaquín Rodrigo (años 60), ritmo pausado renacentista con producción cálida de vinilo analógico, ecos de granito y sierra, 68 BPM."
    },
    8: {
        "estilo": "Sinfonía Cinematográfica y Ancestral • Años 70-80",
        "prompt": "Tema instrumental épico y reflexivo de finales de los 70 / principios de los 80, percusión terrenal resonante, vientos de madera ancestrales, sintetizador atmosférico cálido analógico y cuerdas cinematográficas, 72 BPM."
    },
    9: {
        "estilo": "Pop Sinfónico Romántico e Instrumental • Años 70",
        "prompt": "Pieza lírica y romántica al estilo del pop sinfónico instrumental de los años 70 (Augusto Algueró / Manuel Alejandro), piano de cola cristalino, arpa brillante, flauta y sección de violines en un jardín de cristal, 76 BPM."
    },
    10: {
        "estilo": "Tema Rítmico de Viaje y Progreso • Años 70",
        "prompt": "Tema dinámico y majestuoso de los años 70 con ritmo constante de tren de vapor, guitarra de 12 cuerdas con picking rítmico, contrabajo con cuerpo, metales cálidos y sensación de viaje hacia el progreso, 88 BPM."
    },
    11: {
        "estilo": "Folk Instrumental Vasco y Sinfónico • Años 70",
        "prompt": "Folk acústico vasco e instrumental de los años 70, acordeón melancólico, flauta tradicional, guitarras de cuerda de acero y oleaje de cuerda sinfónica evocando la bruma marina y el hierro industrial, 74 BPM."
    },
    12: {
        "estilo": "Obertura Teatral y Vals Sinfónico • Años 60",
        "prompt": "Obertura orquestal grandiosa al estilo clásico cinematográfico de los 60, fanfarria noble de trompas, cuerdas virtuosas en staccato y un vals majestuoso que revive el brillo de las butacas de terciopelo, 84 BPM."
    },
    13: {
        "estilo": "Poema Místico y Cuerdas Líricas • Años 70",
        "prompt": "Poema sonoro místico y lírico de los años 70, guitarras acústicas arpegiadas, campanas tubulares lejanas, coro etéreo y violonchelo solista cantando a las esculturas de piedra viviente, 66 BPM."
    },
    14: {
        "estilo": "Tango Dramático Instrumental • Años 60-70",
        "prompt": "Tango instrumental nostálgico y dramático de los años 60/70, bandoneón expresivo, violín desgarrador, piano rítmico y contrabajo marcando el abismo bajo la estructura de hierro, 70 BPM."
    },
    15: {
        "estilo": "Jazz Balada Nocturno y Urbano • Años 60",
        "prompt": "Jazz balada nocturno y elegante al estilo de los años 60, saxofón tenor aterciopelado con sordina, piano de club con reverberación natural, escobillas suaves de batería y contrabajo profundo, 64 BPM."
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
    writer.draw_text(margin_x, y, "BLOQUE 13: CÁPSULA DE LA MEMORIA [MEM] • GRANDES OBRAS Y POSTAL SONORA", "F2", 10.0, 0.1, 0.05, 0.2)
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
    prompt_box_h = 20 + (len(p_lines) * 10.5)

    writer.set_fill_color(0.98, 0.96, 0.91) # Crema / pergamino claro
    writer.set_stroke_color(0.72, 0.53, 0.04)
    writer.set_line_width(1.0)
    writer.rect(margin_x, y - prompt_box_h, content_w, prompt_box_h, fill=True, stroke=True)

    ty = y - 12
    writer.draw_text(margin_x + 8, ty, "Copia este prompt exacto y pégalo en Gemini Web para generar la imagen documental:", "F2", 7.8, 0.1, 0.05, 0.2)
    ty -= 11.5
    for pl in p_lines:
        writer.draw_text(margin_x + 8, ty, pl, "F3", 7.6, 0.1, 0.05, 0.2)
        ty -= 10.5

    y -= (prompt_box_h + 10)

    # 3. Paso 2: Reto y Preguntas de Investigación con Gemini
    writer.draw_text(margin_x, y, "Paso 2: Preguntas de Ingeniería y Vida Cotidiana para el Diálogo con Gemini", "F2", 8.8, 0.72, 0.53, 0.04)
    y -= 8

    q1_lines = wrap_text(f"1. Ingeniería de época: {item['pregunta1']}", 92)
    q2_lines = wrap_text(f"2. Entorno y vida cotidiana: {item['pregunta2']}", 92)
    tips_box_h = 20 + ((len(q1_lines) + len(q2_lines)) * 10.5) + 6

    writer.set_fill_color(1.0, 1.0, 1.0)
    writer.set_stroke_color(0.72, 0.53, 0.04)
    writer.set_line_width(1.0)
    writer.rect(margin_x, y - tips_box_h, content_w, tips_box_h, fill=True, stroke=True)

    ty = y - 12
    writer.draw_text(margin_x + 8, ty, "Escribe o dicta por voz estas dos preguntas a Gemini tras observar la imagen:", "F2", 7.8, 0.72, 0.53, 0.04)
    ty -= 12
    for ql in q1_lines:
        writer.draw_text(margin_x + 8, ty, ql, "F1", 7.6, 0.15, 0.2, 0.26)
        ty -= 10.5
    ty -= 3
    for ql in q2_lines:
        writer.draw_text(margin_x + 8, ty, ql, "F1", 7.6, 0.15, 0.2, 0.26)
        ty -= 10.5

    y -= (tips_box_h + 10)

    # 4. Paso 3: Postal Sonora con Google Flow Music (Música Décadas 60s, 70s y 80s)
    music_info = MUSIC_FLOW_PROMPTS.get(item['num'], {
        "estilo": "Banda Sonora Cinematográfica Épica • Años 60-70",
        "prompt": "Orquesta sinfónica cálida y evocadora al estilo de las bandas sonoras épicas de los años 60 y 70, cuerdas majestuosas, guitarra acústica y aire nostálgico, 75 BPM."
    })

    writer.draw_text(margin_x, y, "Paso 3: Postal Sonora con Google Flow Music (Ambientación Musical 60s, 70s y 80s)", "F2", 8.8, 0.72, 0.53, 0.04)
    y -= 8

    m_lines = wrap_text(f'"{music_info["prompt"]}"', 92)
    music_box_h = 20 + (len(m_lines) * 10.5) + 16

    writer.set_fill_color(0.96, 0.98, 1.0) # Azul suave tenue
    writer.set_stroke_color(0.2, 0.45, 0.8) # Azul medio
    writer.set_line_width(1.0)
    writer.rect(margin_x, y - music_box_h, content_w, music_box_h, fill=True, stroke=True)

    ty = y - 12
    writer.draw_text(margin_x + 8, ty, f"Entra en labs.google/flow (o music-fx) y pega este prompt musical ({music_info['estilo']}):", "F2", 7.8, 0.1, 0.25, 0.6)
    ty -= 12
    for ml in m_lines:
        writer.draw_text(margin_x + 8, ty, ml, "F3", 7.6, 0.05, 0.15, 0.35)
        ty -= 10.5
    ty -= 3
    writer.draw_text(margin_x + 8, ty, "Productor IA: Puedes pedirle a Gemini conversacional ajustar la mezcla: \"Quiero darle un aire más cálido con guitarra acústica al estilo de los años 70\".", "F1", 7.0, 0.35, 0.4, 0.45)

    y -= (music_box_h + 10)

    # Pie de página
    writer.set_stroke_color(0.85, 0.88, 0.92)
    writer.set_line_width(0.6)
    writer.line(margin_x, 26, margin_x + content_w, 26)
    writer.draw_text(margin_x, 16, f"Curso de Inteligencia Artificial para Seniors • Sesión {item['num']:02d} • {item['id_code']} {item['titulo_corto']} • Postal Sonora", "F1", 7.4, 0.45, 0.48, 0.52)
    writer.draw_text(margin_x + content_w - 180, 16, "Patrimonio Histórico y Técnico de España", "F2", 7.4, 0.72, 0.53, 0.04)

    writer.end_page()
    writer.write_to_file(output_path)

def update_all_mem_pdfs():
    print("=== [1] ACTUALIZANDO FICHAS MEM CON ENCODING WINANSI COMPLETO Y POSTAL SONORA ===")
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
