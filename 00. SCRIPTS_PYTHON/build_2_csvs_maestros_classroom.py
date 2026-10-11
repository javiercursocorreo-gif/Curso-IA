#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_2_csvs_maestros_classroom.py
Genera los DOS únicos archivos CSV unificados para Google Classroom:
1. CURSO_IA_UNIFICADO.csv (en CURSO-IA/PANELES_CSV/)
   - Tema 1: MONOGRAFICOS (con los 6 mapas interactivos de los monográficos)
   - Temas siguientes: SESIÓN 1 a SESIÓN 60 (cada una con su Mapa Interactivo en 3 columnas)
2. CURSO_ROBOTICA_UNIFICADO.csv (en CURSO-ROBOTICA-V2/PANELES_CSV/ y copia en CURSO-IA/PANELES_CSV/)
   - Unifica todos los paneles/bloques de CURSO-ROBOTICA-V2/PANELES_CSV en un único CSV donde cada bloque es un TEMA
     (INTRODUCCIÓN, ROB1. UN MOTOR, ROB2. SENSORES-Y-DECISIONES, etc.) y cada clase dentro del tema lleva a su mapa interactivo.
"""

import os
import csv
import re
import glob

IA_ROOT = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
IA_CSV_DIR = os.path.join(IA_ROOT, "PANELES_CSV")

ROB_ROOT = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-V2"
ROB_CSV_DIR = os.path.join(ROB_ROOT, "PANELES_CSV")

HEADER = ['ID_CURSO', 'TEMA_CLASSROOM', 'TITULO_MATERIAL', 'DESCRIPCION_MATERIAL', 'URL_GITHUB']


def generate_ia_unified_csv():
    os.makedirs(IA_CSV_DIR, exist_ok=True)
    out_path = os.path.join(IA_CSV_DIR, "CURSO_IA_UNIFICADO.csv")

    rows = []

    # 1. TEMA: MONOGRAFICOS (los 6 mapas interactivos de los Monográficos)
    monograficos_rows = [
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 1. Gemini en PC y Móvil (Instalación y Uso)',
            'Cuadro de mando interactivo del Monográfico 1 con la Guía visual oficial completa y acceso directo al portal de Google Gemini.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/1.%20INTRODUCCION_GEMINI/MAPA_CLASE_1_GEMINI.html'
        ],
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 2. NotebookLM: Tu Cuaderno Inteligente',
            'Cuadro de mando interactivo del Monográfico 2: Guía oficial (PDF), portal de NotebookLM, fichas de práctica guiada, fuentes de prueba (Apolo 11) y resultados generados por IA.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/2.%20INTRODUCCION_NLM/MAPA_CLASE_2_NLM.html'
        ],
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 3. Cómo Crear un Cuento Ilustrado con NotebookLM',
            'Cuadro de mando interactivo del Monográfico 3 con la metodología en 4 fases guiadas: Introducción al Proyecto, Creación del Cuento, Generador de Guion e Ilustrador Visual.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/3.%20COMO_HACER_UN_CUENTO_CON_NLM/MAPA_CLASE_3_CUENTO.html'
        ],
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 4. Mi Biografía (Escribe tus Memorias con IA)',
            'Cuadro de mando interactivo del Monográfico 4 con el manual metodológico de instrucciones (PDF) y la aplicación web interactiva para redactar vivencias y anécdotas con IA.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/4.%20Mi_Biografia/MAPA_CLASE_4_BIOGRAFIA.html'
        ],
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 5. Educanietos IA: Ayuda a tus Nietos con IA (Ciencias, Mates e Historia)',
            'Cuadro de mando interactivo del Monográfico 5 con el protocolo pedagógico (PDF), simulador interactivo de tutoría escolar y bancos de ejercicios prácticos de Historia y Matemáticas.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/5.%20EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/MAPA_CLASE_5_EDUCANIETOS.html'
        ],
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 6. Mapa de Gestión del Proyecto con IA (Arquitectura y Flujo de Trabajo)',
            'Cuadro de mando interactivo del Monográfico 6 con la ficha técnica de arquitectura del sistema, el simulador de flujo de producción y el póster infográfico de creación de materiales.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/7.%20MAPA_GESTION_PROYECTO_CON_IA/MAPA_CLASE_7_GESTION.html'
        ],
    ]
    rows.extend(monograficos_rows)

    # 2. TEMAS: SESIÓN 1 a SESIÓN 60
    for s_num in range(1, 61):
        folder_name = f"{s_num:02d}_Sesion" if s_num < 60 else "60_Sesion_Cierre"
        tema = f"SESIÓN {s_num}"
        titulo = f"Mapa Interactivo: Sesión {s_num:02d} (HTML)"
        desc = f"Cuadro de mando interactivo en 3 columnas de la Sesión {s_num:02d} con todos los recursos y retos guiados paso a paso."
        url = (
            f"https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/"
            f"EXPORTACION_FICHAS_CLASSROOM_PDF/100.%20%5BSESSIONS%5D%20TERNAS_LISTAS_PARA_CLASSROOM/"
            f"{folder_name}/MAPA_SESION_{s_num:02d}.html"
        )
        rows.append(['', tema, titulo, desc, url])

    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerows(rows)

    print(f"✅ CSV UNIFICADO DE IA generado ({len(rows)} filas): {out_path}")
    return out_path


def infer_block_theme_from_filename(fname, original_tema):
    """
    Convierte el nombre del archivo CSV de bloque de Robótica (o el tema original)
    en el nombre del TEMA unificado de Classroom:
      0 / INTRO -> INTRODUCCIÓN
      1 / ROB1  -> ROB1. UN MOTOR
      2 / ROB2  -> ROB2. SENSORES-Y-DECISIONES
      etc.
    """
    base = os.path.splitext(os.path.basename(fname))[0]
    u = base.upper()

    # Mapeo explícito para los bloques estándar si aparecen por número o nombre
    if u.startswith("0.") or "INTRO" in u or "INAUGURAL" in u or "COMUN" in u:
        return "INTRODUCCIÓN"

    # Si el nombre del CSV ya contiene ROB1, ROB2, BLOQUE_1, etc., limpiarlo con elegancia
    m_rob = re.search(r'(ROB\s*\d+|BLOQUE\s*\d+|PANEL[_\s]*\d+)', u)
    # Comprobar nombres específicos pedidos por el usuario
    if "ROB1" in u or "UN_MOTOR" in u or "UN MOTOR" in u or re.match(r'^1[\._]', u):
        return "ROB1. UN MOTOR"
    if "ROB2" in u or "SENSORES" in u or re.match(r'^2[\._]', u):
        return "ROB2. SENSORES-Y-DECISIONES"

    # Para el resto de bloques de robótica (ROB3, ROB4, ...), extraer el nombre limpio del archivo CSV
    # Ej: "3.PANEL_ROB3_CINEMATICA.csv" o "ROB3. ... .csv"
    clean = re.sub(r'^\d+[\._-]*', '', base)
    clean = re.sub(r'^(PANEL|BLOQUE|CURSO|ROBOTICA)[_\s-]*', '', clean, flags=re.IGNORECASE)
    clean = clean.replace('_', ' ').strip()

    # Si empieza por ROB3, ROB4, etc. poner punto tras ROBx si no lo lleva
    m_num = re.match(r'^(\d+)[\._\s-]*(.*)$', base)
    if m_num:
        b_idx = int(m_num.group(1))
        rest = m_num.group(2)
        rest = re.sub(r'^(PANEL|BLOQUE|ROB\d*)[_\s\.-]*', '', rest, flags=re.IGNORECASE)
        rest = rest.replace('_', ' ').strip()
        if b_idx == 0:
            return "INTRODUCCIÓN"
        elif b_idx == 1:
            return "ROB1. UN MOTOR"
        elif b_idx == 2:
            return "ROB2. SENSORES-Y-DECISIONES"
        elif rest:
            return f"ROB{b_idx}. {rest.upper()}"
        else:
            return f"ROB{b_idx}"

    if clean:
        return clean.upper()
    return original_tema


def clean_lesson_title(original_tema, original_titulo):
    """
    Como cada clase de Robótica tenía antes su propio Tema dentro del CSV del bloque
    (por ejemplo: TEMA_CLASSROOM='1.1. Lavadora', TITULO_MATERIAL='Mapa Interactivo: Lavadora (HTML)'),
    usamos el nombre de la clase/lección para que dentro del nuevo TEMA (que ahora es el Bloque)
    cada elemento se identifique claramente con el nombre de su clase.
    """
    t_tema = (original_tema or "").strip()
    t_tit = (original_titulo or "").strip()

    if t_tema and t_tema.upper() not in ("INTRODUCCIÓN", "INTRODUCCION", "GENERAL"):
        # Si el título ya contiene el nombre de la lección o es "Mapa Interactivo...", dejamos claro el nombre de la clase
        if "presentación inaugural" in t_tema.lower() or "presentacion inaugural" in t_tit.lower():
            return "Presentación inaugural"
        if "manual de classroom" in t_tema.lower() or "manual de classroom" in t_tit.lower():
            return "Manual de Classroom"
        if "puerta supermercado" in t_tema.lower() or "puerta" in t_tema.lower() and "supermercado" in t_tema.lower():
            return "Puerta supermercado"
        return t_tema
    return t_tit


def generate_robotica_unified_csv():
    try:
        csv_files = sorted(glob.glob(os.path.join(ROB_CSV_DIR, "*.csv")))
    except PermissionError:
        csv_files = []

    # Excluir el propio archivo unificado o índices gigantes si existen
    source_csvs = [
        f for f in csv_files
        if "UNIFICADO" not in os.path.basename(f).upper()
        and "INDICE" not in os.path.basename(f).upper()
        and not os.path.basename(f).startswith("._")
    ]

    if not source_csvs:
        print(f"ℹ️ Ejecuta este script desde tu terminal externa para leer y escribir en {ROB_CSV_DIR}.")
        return None

    print(f"📂 Encontrados {len(source_csvs)} archivos CSV de bloques en CURSO-ROBOTICA-V2/PANELES_CSV:")
    for sc in source_csvs:
        print(f"   • {os.path.basename(sc)}")

    unified_rows = []
    seen_urls = set()

    for csv_path in source_csvs:
        with open(csv_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                orig_tema = (row.get('TEMA_CLASSROOM') or '').strip()
                orig_titulo = (row.get('TITULO_MATERIAL') or '').strip()
                orig_desc = (row.get('DESCRIPCION_MATERIAL') or '').strip()
                orig_url = (row.get('URL_GITHUB') or '').strip()

                if not orig_url:
                    continue
                if orig_url in seen_urls:
                    continue
                seen_urls.add(orig_url)

                # Determinar el TEMA de Classroom (INTRODUCCIÓN, ROB1. UN MOTOR, ROB2. SENSORES-Y-DECISIONES, ROB3..., etc.)
                new_tema = infer_block_theme_from_filename(csv_path, orig_tema)

                # Si dentro de un CSV el propio orig_tema indica Introducción (Presentación inaugural o Manual de Classroom)
                low_check = f"{orig_tema} {orig_titulo}".lower()
                if "inaugural" in low_check or "manual de classroom" in low_check or "introducci" in low_check:
                    new_tema = "INTRODUCCIÓN"

                # Determinar el título limpio de la clase dentro del tema
                new_titulo = clean_lesson_title(orig_tema, orig_titulo)

                unified_rows.append(['', new_tema, new_titulo, orig_desc, orig_url])

    out_rob_path = os.path.join(ROB_CSV_DIR, "CURSO_ROBOTICA_UNIFICADO.csv")
    with open(out_rob_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerows(unified_rows)

    # Guardar también copia en CURSO-IA/PANELES_CSV para tener los 2 CSV juntos en el mismo sitio
    out_copy_in_ia = os.path.join(IA_CSV_DIR, "CURSO_ROBOTICA_UNIFICADO.csv")
    with open(out_copy_in_ia, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerows(unified_rows)

    print(f"✅ CSV UNIFICADO DE ROBÓTICA generado ({len(unified_rows)} filas):")
    print(f"   • {out_rob_path}")
    print(f"   • {out_copy_in_ia}")
    return out_rob_path


if __name__ == "__main__":
    print("🚀 Generando los 2 únicos CSV Maestros Unificados (CURSO DE IA y CURSO DE ROBÓTICA)...")
    generate_ia_unified_csv()
    generate_robotica_unified_csv()
    print("\n🎉 ¡Proceso completado!")
