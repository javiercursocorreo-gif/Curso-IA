# -*- coding: utf-8 -*-
"""
Generador del Cuaderno / Panel de Índice para Google Classroom: IA_INDICE
Agrupa TODOS los ejercicios por ETIQUETA (Tema en Classroom) en lugar de por Sesión.
En cada etiqueta, muestra los ejercicios ordenados por sesión indicando:
- Nombre del ejercicio
- Sesión a la que pertenece
- Enlace directo al archivo (PDF / Vídeo) en GitHub Pages

Permite generar el índice filtrado por las sesiones que el usuario haya publicado,
o generar el índice maestro completo de las 60 sesiones.
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
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sesiones_publicadas.json")

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
    f_upper = filename.upper()
    if re.search(r'(^|\D)TXT[-_\s\d]', f_upper):
        return "TXT", "01. [TXT] Prompts de Comunicación y Texto", "Paso 1: Prompts de Comunicación y Texto (El poder de la palabra en la IA)."
    if re.search(r'(^|\D)EST[-_\s\d]', f_upper):
        return "EST", "02. [EST] Estilos Visuales de Imagen", "Paso 2: Estilos Visuales de Imagen (Aprender a pedir estilos artísticos y fotográficos)."
    if re.search(r'(^|\D)PRAC[-_\s\d]', f_upper):
        return "PRAC", "03. [PRAC] Talleres Prácticos con Gemini", "Paso 3: Taller Práctico con Gemini (Transformación y creatividad aplicada)."
    if re.search(r'(^|\D)FRAC[-_\s\d]', f_upper) or "FRACTAL" in f_upper:
        return "FRAC", "04. [FRAC] Fractales en IA (Vídeos y Fichas)", "Paso 4: Geometría Fractal en IA (Visualización y asombro en aula)."
    if re.search(r'(^|\D)INT[-_\s\d]', f_upper):
        return "INT", "05. [INT] El Mundo por Dentro y Reconstrucción", "Paso 5: El Mundo por Dentro y Reconstrucción Histórica (Corte transversal y arquitectura)."
    if re.search(r'(^|\D)FUT[-_\s\d]', f_upper):
        return "FUT", "06. [FUT] Línea de Tiempo del Futuro (2030+)", "Paso 6: Línea de Tiempo del Futuro y Sci-Fi (Tecnología amable y robótica del mañana)."
    if re.search(r'(^|\D)NAT[-_\s\d]', f_upper) or re.search(r'(^|\D)AVES[-_\s\d]', f_upper):
        return "NAT", "07. [NAT] Naturaleza Fascinante y Biodiversidad", "Paso 7: Biodiversidad y Naturaleza Fascinante (Fauna, flora e infografías científicas)."
    if re.search(r'(^|\D)ARTE[-_\s\d]', f_upper):
        return "ARTE", "08. [ARTE] Obras Maestras del Arte Universal", "Paso 8: Obras Maestras de la Historia del Arte (Los grandes genios de la pintura)."
    if re.search(r'(^|\D)NIV[-_\s\d]', f_upper):
        return "NIV", "09. [NIV] Escalafones y Niveles (Cultura 101)", "Paso 9: Escalafones y Niveles (Cultura 101: clasificaciones del mundo)."
    if re.search(r'(^|\D)TRUC[-_\s\d]', f_upper):
        return "TRUC", "10. [TRUC] Trucos y Soluciones Cotidianas", "Paso 10: Trucos y Soluciones Cotidianas (Hogar, cocina y vida práctica con IA)."
    if re.search(r'(^|\D)CUENT[-_\s\d]', f_upper):
        return "CUENT", "11. [CUENT] Cuentos Ilustrados para Nietos", "Paso 11: Cuentos Ilustrados para Nietos (Historias personalizadas con valores)."
    if re.search(r'(^|\D)MOVIL[-_\s\d]', f_upper):
        return "MOVIL", "12. [MOVIL] El Salvavidas del Móvil (Cámara y Voz)", "Paso 12: El Salvavidas del Móvil (Cámara y voz con la app de Gemini ante la pantalla)."
    if re.search(r'(^|\D)MEM[-_\s\d]', f_upper):
        return "MEM", "13. [MEM] Cápsula de la Memoria", "Paso 13: Cápsula de la Memoria (Fotos de pueblo o barrio con microrrelato para nietos)."
    if re.search(r'(^|\D)MEC[-_\s\d]', f_upper):
        return "MEC", "14. [MEC] Cómo Funcionan las Cosas (Vídeo 3D)", "Paso 14: Cómo Funcionan las Cosas (Mecánica e Ingeniería en Vídeo 3D de 10 seg con Gemini)."
    return "OTROS", "15. [OTROS] Material Adicional", "Material didáctico adicional."

def load_published_sessions():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return sorted(list(set(data.get("published", [1]))))
        except Exception:
            pass
    return [1]

def save_published_sessions(sessions_list):
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump({"published": sorted(list(set(sessions_list)))}, f, indent=2)

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
            # En Sesión 1 si no hay cuentos en la sesión se respeta
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

        for code, tag_name, tag_desc in TAG_DEFINITIONS:
            tag_items = items_by_tag.get(code, [])
            # Filtrar por sesiones permitidas si se especifican
            if allowed_sessions is not None:
                tag_items = [it for it in tag_items if it['session_num'] in allowed_sessions]

            # Ordenar por sesión y nombre
            tag_items.sort(key=lambda x: (x['session_num'], natural_sort_key(x['filename'])))

            for it in tag_items:
                # Título que destaca la sesión donde se encuentra y el nombre del ejercicio
                mat_title = f"[{it['session_name']}] {it['clean_title']} ({it['extension']})"
                mat_desc = f"Disponible en {it['session_name']}. {it['tag_desc']} Acceso directo al recurso interactivo."
                writer.writerow(['', tag_name, mat_title, mat_desc, it['url']])
                total_written += 1

    print(f"✅ Generado '{output_filename}' con {total_written} recursos agrupados por etiqueta.")
    return csv_path, total_written

def main():
    parser = argparse.ArgumentParser(description="Generador de IA_INDICE agrupado por etiquetas")
    parser.add_argument("--hasta", type=int, help="Incluir hasta la sesión N (ej: --hasta 5)")
    parser.add_argument("--sesiones", type=str, help="Lista de sesiones separadas por coma (ej: --sesiones 1,2,3)")
    parser.add_argument("--todas", action="store_true", help="Generar con las 60 sesiones completas")
    parser.add_argument("--add", type=int, help="Añadir una nueva sesión publicada (ej: --add 2)")

    args = parser.parse_args()

    items_by_tag = collect_all_session_items()

    published = load_published_sessions()

    if args.add:
        if args.add not in published:
            published.append(args.add)
            published.sort()
            save_published_sessions(published)
            print(f"📌 Añadida Sesión {args.add:02d} a la lista de publicadas.")
    elif args.hasta:
        published = list(range(1, args.hasta + 1))
        save_published_sessions(published)
        print(f"📌 Establecidas sesiones publicadas de la 01 a la {args.hasta:02d}.")
    elif args.sesiones:
        published = sorted([int(s.strip()) for s in args.sesiones.split(',') if s.strip().isdigit()])
        save_published_sessions(published)
        print(f"📌 Establecidas sesiones publicadas: {published}.")
    elif args.todas:
        published = list(range(1, 61))
        save_published_sessions(published)
        print("📌 Establecidas las 60 sesiones completas como publicadas.")

    # 1. Generar el CSV principal IA_INDICE.csv con las sesiones actualmente publicadas
    print(f"\n📂 Generando IA_INDICE.csv para las sesiones publicadas: {published}...")
    write_indice_csv("IA_INDICE.csv", items_by_tag, allowed_sessions=published)

    # 2. Generar también el Maestro Completo con las 60 sesiones por si se quiere consultar o importar al completo
    print("\n📂 Generando IA_INDICE_COMPLETO_60_SESIONES.csv (con todos los ~850 ejercicios del curso)...")
    write_indice_csv("IA_INDICE_COMPLETO_60_SESIONES.csv", items_by_tag, allowed_sessions=None)

if __name__ == "__main__":
    main()
