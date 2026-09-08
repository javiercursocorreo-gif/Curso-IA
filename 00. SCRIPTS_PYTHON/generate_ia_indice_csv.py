# -*- coding: utf-8 -*-
"""
Generador del Cuaderno / Panel de Índice para Google Classroom: IA_INDICE
Agrupa TODOS los ejercicios por ETIQUETA (Tema en Classroom) en lugar de por Sesión.
En cada etiqueta, muestra los ejercicios ordenados por sesión indicando:
- Nombre del ejercicio
- Sesión a la que pertenece
- Enlace directo al archivo (PDF / Vídeo) en GitHub Pages

Incluye la fila 00 del Glosario de Etiquetas al principio y genera:
- IA_INDICE.csv
- IA_INDICE_COMPLETO_60_SESIONES.csv
"""

import os
import csv
import re
import json
import argparse
import unicodedata
import urllib.parse

BASE_URL = "https://javiercursocorreo-gif.github.io/Curso-IA/"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSIONS_DIR = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
OUTPUT_DIR = os.path.join(ROOT_DIR, "PANELES_CSV")
GLOSARIO_PDF_REL = "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/00. [GUIA] GLOSARIO_DE_ETIQUETAS/00. GLOSARIO_ETIQUETAS_DEL_CURSO.pdf"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# 14 Etiquetas Oficiales del Curso
TAG_DEFINITIONS = [
    ("TXT",   "01. [TXT] Prompts de Comunicación y Texto",       "Paso 1: Prompts de Comunicación y Texto (El poder de la palabra en la IA)."),
    ("EST",   "02. [EST] Estilos Visuales de Imagen",             "Paso 2: Estilos Visuales de Imagen (Aprender a pedir estilos artísticos y fotográficos)."),
    ("PRAC",  "03. [PRAC] Talleres Prácticos con Gemini",         "Paso 3: Taller Práctico con Gemini (Transformación y creatividad aplicada)."),
    ("FRAC",  "04. [FRAC] Fractales en IA (Vídeos y Fichas)",     "Paso 4: Geometría Fractal en IA (Visualización y asombro en aula)."),
    ("INT",   "05. [INT] El Mundo por Dentro y Reconstrucción",   "Paso 5: El Mundo por Dentro y Reconstrucción Histórica (Corte transversal y arquitectura)."),
    ("FUT",   "06. [FUT] Línea de Tiempo del Futuro (2030+)",     "Paso 6: Línea de Tiempo del Futuro y Sci-Fi (Tecnología amable y robótica del mañana)."),
    ("NAT",   "07. [NAT] Naturaleza Fascinante y Biodiversidad",  "Paso 7: Biodiversidad y Naturaleza Fascinante (Fauna, flora e infografías científicas)."),
    ("ARTE",  "08. [ARTE] Obras Maestras del Arte Universal",     "Paso 8: Obras Maestras de la Historia del Arte (Los grandes genios de la pintura)."),
    ("NIV",   "09. [NIV] Escalafones y Niveles (Cultura 101)",    "Paso 9: Escalafones y Niveles (Cultura 101: clasificaciones del mundo)."),
    ("TRUC",  "10. [TRUC] Trucos y Soluciones Cotidianas",        "Paso 10: Trucos y Soluciones Cotidianas (Hogar, cocina y vida práctica con IA)."),
    ("CUENT", "11. [CUENT] Cuentos Ilustrados para Nietos",       "Paso 11: Cuentos Ilustrados para Nietos (Historias personalizadas con valores)."),
    ("MOVIL", "12. [MOVIL] El Salvavidas del Móvil (Cámara y Voz)","Paso 12: El Salvavidas del Móvil (Cámara y voz con la app de Gemini ante la pantalla)."),
    ("MEM",   "13. [MEM] Cápsula de la Memoria",                  "Paso 13: Cápsula de la Memoria (Fotos de pueblo o barrio con microrrelato para nietos)."),
    ("MEC",   "14. [MEC] Cómo Funcionan las Cosas (Vídeo 3D)",    "Paso 14: Cómo Funcionan las Cosas (Mecánica e Ingeniería en Vídeo 3D de 10 seg con Gemini)."),
]

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def clean_title(filename):
    name, ext = os.path.splitext(filename)
    clean = re.sub(r'^\d+\.\s*', '', name)
    clean = clean.replace('_', ' ').replace('-', ' - ')
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean, ext[1:].upper()

def get_tag_info(filename):
    fu = filename.upper()
    if re.search(r'(^|\D)TXT[-_\s\d]', fu) or filename.startswith('1.') or filename.startswith('1 '):
        return "TXT", "01. [TXT] Prompts de Comunicación y Texto", "Paso 1: Prompts de Comunicación y Texto (El poder de la palabra en la IA)."
    if re.search(r'(^|\D)EST[-_\s\d]', fu) or filename.startswith('2.') or filename.startswith('2 '):
        return "EST", "02. [EST] Estilos Visuales de Imagen", "Paso 2: Estilos Visuales de Imagen (Aprender a pedir estilos artísticos y fotográficos)."
    if re.search(r'(^|\D)PRAC[-_\s\d]', fu) or filename.startswith('3.') or filename.startswith('3 '):
        return "PRAC", "03. [PRAC] Talleres Prácticos con Gemini", "Paso 3: Taller Práctico con Gemini (Transformación y creatividad aplicada)."
    if re.search(r'(^|\D)FRAC[-_\s\d]', fu) or 'FRACTAL' in fu or filename.startswith('4.') or filename.startswith('4 '):
        return "FRAC", "04. [FRAC] Fractales en IA (Vídeos y Fichas)", "Paso 4: Geometría Fractal en IA (Visualización y asombro en aula)."
    if re.search(r'(^|\D)INT[-_\s\d]', fu) or filename.startswith('5.') or filename.startswith('5 '):
        return "INT", "05. [INT] El Mundo por Dentro y Reconstrucción", "Paso 5: El Mundo por Dentro y Reconstrucción Histórica (Corte transversal y arquitectura)."
    if re.search(r'(^|\D)FUT[-_\s\d]', fu) or filename.startswith('6.') or filename.startswith('6 '):
        return "FUT", "06. [FUT] Línea de Tiempo del Futuro (2030+)", "Paso 6: Línea de Tiempo del Futuro y Sci-Fi (Tecnología amable y robótica del mañana)."
    if re.search(r'(^|\D)NAT[-_\s\d]', fu) or 'AVES' in fu or filename.startswith('7.') or filename.startswith('7 '):
        return "NAT", "07. [NAT] Naturaleza Fascinante y Biodiversidad", "Paso 7: Biodiversidad y Naturaleza Fascinante (Fauna, flora e infografías científicas)."
    if re.search(r'(^|\D)ARTE[-_\s\d]', fu) or filename.startswith('8.') or filename.startswith('8 '):
        return "ARTE", "08. [ARTE] Obras Maestras del Arte Universal", "Paso 8: Obras Maestras de la Historia del Arte (Los grandes genios de la pintura)."
    if re.search(r'(^|\D)NIV[-_\s\d]', fu) or filename.startswith('9.') or filename.startswith('9 '):
        return "NIV", "09. [NIV] Escalafones y Niveles (Cultura 101)", "Paso 9: Escalafones y Niveles (Cultura 101: clasificaciones del mundo)."
    if re.search(r'(^|\D)TRUC[-_\s\d]', fu) or filename.startswith('10.') or filename.startswith('10 '):
        return "TRUC", "10. [TRUC] Trucos y Soluciones Cotidianas", "Paso 10: Trucos y Soluciones Cotidianas (Hogar, cocina y vida práctica con IA)."
    if re.search(r'(^|\D)CUENT[-_\s\d]', fu) or filename.startswith('11.') or filename.startswith('11 '):
        return "CUENT", "11. [CUENT] Cuentos Ilustrados para Nietos", "Paso 11: Cuentos Ilustrados para Nietos (Historias personalizadas con valores)."
    if re.search(r'(^|\D)MOVIL[-_\s\d]', fu) or filename.startswith('12.') or filename.startswith('12 '):
        return "MOVIL", "12. [MOVIL] El Salvavidas del Móvil (Cámara y Voz)", "Paso 12: El Salvavidas del Móvil (Cámara y voz con la app de Gemini ante la pantalla)."
    if re.search(r'(^|\D)MEM[-_\s\d]', fu) or filename.startswith('13.') or filename.startswith('13 '):
        return "MEM", "13. [MEM] Cápsula de la Memoria", "Paso 13: Cápsula de la Memoria (Fotos de pueblo o barrio con microrrelato para nietos)."
    if re.search(r'(^|\D)MEC[-_\s\d]', fu) or filename.startswith('14.') or filename.startswith('14 '):
        return "MEC", "14. [MEC] Cómo Funcionan las Cosas (Vídeo 3D)", "Paso 14: Cómo Funcionan las Cosas (Mecánica e Ingeniería en Vídeo 3D de 10 seg con Gemini)."
    return "OTROS", "15. [OTROS] Material Adicional", "Material didáctico adicional."

def collect_all_session_items():
    all_session_folders = sorted(
        [d for d in os.listdir(SESSIONS_DIR) if os.path.isdir(os.path.join(SESSIONS_DIR, d)) and not d.startswith('.')],
        key=natural_sort_key
    )

    items_by_tag = {code: [] for code, _, _ in TAG_DEFINITIONS}
    items_by_tag["OTROS"] = []

    for s_folder in all_session_folders:
        m = re.match(r'^(\d+)_', s_folder)
        if not m:
            continue
        s_num = int(m.group(1))
        session_path = os.path.join(SESSIONS_DIR, s_folder)

        files = sorted(
            [x for x in os.listdir(session_path) if not x.startswith('.') and not x.startswith('~$') and x.endswith(('.pdf', '.mp4'))],
            key=natural_sort_key
        )

        for fname in files:
            tag_code, tag_name, tag_desc = get_tag_info(fname)
            clean_t, ext = clean_title(fname)

            rel_path = os.path.relpath(os.path.join(session_path, fname), ROOT_DIR)
            rel_path_nfc = unicodedata.normalize('NFC', rel_path)
            url = BASE_URL + urllib.parse.quote(rel_path_nfc)

            items_by_tag[tag_code].append({
                'session_num': s_num,
                'session_name': f"Sesión {s_num:02d}",
                'filename': fname,
                'clean_title': clean_t,
                'extension': ext,
                'tag_code': tag_code,
                'tag_name': tag_name,
                'tag_desc': tag_desc,
                'url': url
            })

    return items_by_tag

def write_indice_csv(output_filename, items_by_tag, allowed_sessions=None):
    csv_path = os.path.join(OUTPUT_DIR, output_filename)
    total_written = 0

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID_CURSO', 'TEMA_CLASSROOM', 'TITULO_MATERIAL', 'DESCRIPCION_MATERIAL', 'URL_GITHUB'])

        # Fila 00: Glosario de Etiquetas
        url_glosario = BASE_URL + urllib.parse.quote(unicodedata.normalize('NFC', GLOSARIO_PDF_REL))
        writer.writerow([
            '',
            '00. [GUÍA] Glosario de Etiquetas y Metodología',
            'Glosario de Etiquetas del Curso (Qué significa cada sigla: TXT, EST, PRAC...) (PDF)',
            'Guía oficial de referencia rápida. Explica el significado pedagógico, objetivo y ejemplos de las 15 etiquetas del curso.',
            url_glosario
        ])

        for code, tag_name, tag_desc in TAG_DEFINITIONS:
            tag_items = items_by_tag.get(code, [])
            if allowed_sessions is not None:
                tag_items = [it for it in tag_items if it['session_num'] in allowed_sessions]

            tag_items.sort(key=lambda x: (x['session_num'], natural_sort_key(x['filename'])))

            for it in tag_items:
                mat_title = f"[{it['session_name']}] {it['clean_title']} ({it['extension']})"
                mat_desc = f"Disponible en {it['session_name']}. {it['tag_desc']} Acceso directo al recurso interactivo."
                writer.writerow(['', tag_name, mat_title, mat_desc, it['url']])
                total_written += 1

    print(f"✅ Generado '{output_filename}' con 1 Glosario + {total_written} recursos agrupados por etiqueta.")
    return csv_path, total_written

def main():
    parser = argparse.ArgumentParser(description="Generador de IA_INDICE agrupado por etiquetas")
    parser.add_argument("--hasta", type=int, help="Incluir hasta la sesión N (ej: --hasta 60)")
    parser.add_argument("--sesiones", type=str, help="Lista de sesiones separadas por coma")
    parser.add_argument("--todas", action="store_true", default=True, help="Generar con las 60 sesiones completas")

    args = parser.parse_args()

    items_by_tag = collect_all_session_items()

    if args.hasta:
        published = list(range(1, args.hasta + 1))
    elif args.sesiones:
        published = sorted([int(s.strip()) for s in args.sesiones.split(',') if s.strip().isdigit()])
    else:
        published = list(range(1, 61))

    # 1. Generar IA_INDICE.csv con las 60 sesiones
    print(f"\n📂 Generando IA_INDICE.csv para todas las sesiones (1 a 60)...")
    write_indice_csv("IA_INDICE.csv", items_by_tag, allowed_sessions=published)

    # 2. Generar también IA_INDICE_COMPLETO_60_SESIONES.csv idéntico
    print(f"\n📂 Generando IA_INDICE_COMPLETO_60_SESIONES.csv...")
    write_indice_csv("IA_INDICE_COMPLETO_60_SESIONES.csv", items_by_tag, allowed_sessions=None)

if __name__ == "__main__":
    main()
