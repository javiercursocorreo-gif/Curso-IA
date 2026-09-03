# -*- coding: utf-8 -*-
"""
Generador de Paneles CSV para Google Classroom (CURSO-IA)
Genera exactamente 5 paneles CSV:
- 0.PANEL_MONOGRAFICOS.csv: Las 4 Clases Monográficas (Intro IA, Gemini PC+Móvil, NotebookLM, Cuentos/Cómics)
- 1.PANEL_SESIONES_01_AL_15.csv: Ternas 01 a 15 (con filtro de cuentos en Sesión 01 para antes del Monográfico 3/4)
- 2.PANEL_SESIONES_16_AL_30.csv: Ternas 16 a 30
- 3.PANEL_SESIONES_31_AL_45.csv: Ternas 31 a 45
- 4.PANEL_SESIONES_46_AL_60.csv: Ternas 46 a 60
"""

import os
import csv
import re
import unicodedata
import urllib.parse

BASE_URL = "https://javiercursocorreo-gif.github.io/Curso-IA/"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSIONS_DIR = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
OUTPUT_DIR = os.path.join(ROOT_DIR, "PANELES_CSV")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def clean_title(filename):
    name, ext = os.path.splitext(filename)
    clean = re.sub(r'^\d+\.\s*', '', name)
    clean = clean.replace('_', ' ').replace('-', ' - ')
    clean = re.sub(r'\s+', ' ', clean).strip()
    return f"{clean} ({ext[1:].upper()})"

def get_description_for_file(filename):
    f_upper = filename.upper()
    if "TXT-" in f_upper:
        return "Paso 1: Prompts de Comunicación y Texto (El poder de la palabra en la IA)."
    elif "EST-" in f_upper:
        return "Paso 2: Estilos Visuales de Imagen (Aprender a pedir estilos artísticos y fotográficos)."
    elif "PRAC-" in f_upper:
        return "Paso 3: Taller Práctico con Gemini (Transformación y creatividad aplicada)."
    elif "FRAC-" in f_upper or "FRACTAL" in f_upper:
        if filename.lower().endswith('.mp4'):
            return "Paso 4: Vídeo Fractal del Día en Alta Resolución (Visualización y asombro en aula)."
        return "Paso 4: Ficha del Fractal del Día (Geometría visual explicada para mayores)."
    elif "INT-" in f_upper:
        return "Paso 5: El Mundo por Dentro y Reconstrucción Histórica (Corte transversal y arquitectura)."
    elif "FUT-" in f_upper:
        return "Paso 6: Línea de Tiempo del Futuro y Sci-Fi (Tecnología amable y robótica del mañana)."
    elif "NAT-" in f_upper or "AVES-" in f_upper:
        return "Paso 7: Biodiversidad y Naturaleza Fascinante (Fauna, flora e infografías científicas)."
    elif "ARTE-" in f_upper:
        return "Paso 8: Obras Maestras de la Historia del Arte (Los grandes genios de la pintura universal)."
    elif "NIV-" in f_upper:
        return "Paso 9: Escalafones y Niveles (Cultura 101: clasificaciones del mundo con Meta-Prompting)."
    elif "TRUC-" in f_upper:
        return "Paso 10: Trucos y Soluciones Cotidianas (Hogar, cocina y vida práctica con IA)."
    elif "CUENT-" in f_upper:
        return "Paso 11: Cuentos Ilustrados para Nietos (Historias personalizadas con valores)."
    elif "MOVIL" in f_upper:
        return "Paso 12: El Salvavidas del Móvil (Cámara y voz con la app de Gemini ante la pantalla)."
    elif "MEM" in f_upper:
        return "Paso 13: Cápsula de la Memoria (Fotos de pueblo o barrio con microrrelato para nietos)."
    else:
        return "Material didáctico de apoyo para la sesión de clase."

# ==============================================================================
# PANEL 0: CLASES MONOGRÁFICAS
def generate_panel_0():
    csv_path = os.path.join(OUTPUT_DIR, "0.PANEL_MONOGRAFICOS.csv")
    print(f"📄 Generando {os.path.basename(csv_path)}...")
    
    monograficos = [
        ("Taller 1. Introducción a la Inteligencia Artificial",
         os.path.join(ROOT_DIR, "CLASES", "0. INTRODUCCION A LA IA"),
         "Sesión inaugural de motivación: qué es la IA, desmontando mitos, galería visual de impacto y primeros pasos sin agobios."),
        ("Taller 2. Gemini en PC y Móvil (Instalación y Uso)",
         os.path.join(ROOT_DIR, "CLASES", "1. INTRODUCCION_GEMINI"),
         "Nuestra IA de cabecera: manejo en ordenador, instalación de la app oficial en el móvil, dictado por voz y fotos con la cámara."),
        ("Taller 3. NotebookLM: Tu Cuaderno Inteligente",
         os.path.join(ROOT_DIR, "CLASES", "2. INTRODUCCION_NLM"),
         "Tu biblioteca personal inteligente: cómo subir documentos familiares o recuerdos para resumir, hacer preguntas y generar guiones."),
        ("Taller 4. Creación de Cuentos Ilustrados para Nietos",
         os.path.join(ROOT_DIR, "CLASES", "CLASE DE CREACIÓN DE COMICS"),
         "Metodología en 3 pasos para crear historias inolvidables: el héroe, el guion por escenas y las ilustraciones para los nietos.")
    ]
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID_CURSO', 'TEMA_CLASSROOM', 'TITULO_MATERIAL', 'DESCRIPCION_MATERIAL', 'URL_GITHUB'])
        
        for tema_nombre, carpeta_path, desc_default in monograficos:
            if not os.path.exists(carpeta_path):
                continue
                
            # Para los alumnos en Google Classroom se publican PDFs, vídeos explicativos y audios m4a/mp3
            archivos = sorted([x for x in os.listdir(carpeta_path) 
                               if not x.startswith('.') and not x.startswith('~$') 
                               and x.endswith(('.pdf', '.mp4', '.m4a', '.mp3'))
                               and "PROMPT" not in x.upper()], key=natural_sort_key)
            
            for a in archivos:
                rel_path = os.path.relpath(os.path.join(carpeta_path, a), ROOT_DIR)
                rel_path_nfc = unicodedata.normalize('NFC', rel_path)
                url = BASE_URL + urllib.parse.quote(rel_path_nfc)
                title = f"Material: {clean_title(a)}"
                writer.writerow(['', tema_nombre, title, desc_default, url])

# ==============================================================================
# PANELES 1 A 4: TERNAS DE SESIONES (15 SESIONES POR PANEL)
# ==============================================================================
def generate_panels_sessions():
    paneles_config = [
        (1, 1, 15, "1.PANEL_SESIONES_01_AL_15.csv"),
        (2, 16, 30, "2.PANEL_SESIONES_16_AL_30.csv"),
        (3, 31, 45, "3.PANEL_SESIONES_31_AL_45.csv"),
        (4, 46, 60, "4.PANEL_SESIONES_46_AL_60.csv")
    ]
    
    if not os.path.exists(SESSIONS_DIR):
        print(f"⚠️ Advertencia: No existe la carpeta de sesiones en {SESSIONS_DIR}")
        return

    # Mapear las carpetas de sesiones disponibles
    all_session_folders = sorted([d for d in os.listdir(SESSIONS_DIR) if os.path.isdir(os.path.join(SESSIONS_DIR, d)) and not d.startswith('.')], key=natural_sort_key)
    
    # Diccionario para acceder por número de sesión (1 a 60)
    sessions_by_num = {}
    for f in all_session_folders:
        m = re.match(r'^(\d+)_', f)
        if m:
            num = int(m.group(1))
            sessions_by_num[num] = f

    for panel_num, start_ses, end_ses, csv_name in paneles_config:
        csv_path = os.path.join(OUTPUT_DIR, csv_name)
        print(f"📄 Generando {csv_name} (Sesiones {start_ses:02d} a {end_ses:02d})...")
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID_CURSO', 'TEMA_CLASSROOM', 'TITULO_MATERIAL', 'DESCRIPCION_MATERIAL', 'URL_GITHUB'])
            
            for s_idx in range(start_ses, end_ses + 1):
                folder_name = sessions_by_num.get(s_idx)
                if not folder_name:
                    continue
                    
                tema_nombre = f"Sesión {s_idx:02d}"
                if s_idx == 60:
                    tema_nombre = "Sesión 60 (Cierre y Celebración)"
                    
                session_path = os.path.join(SESSIONS_DIR, folder_name)
                files = sorted([x for x in os.listdir(session_path) if not x.startswith('.') and not x.startswith('~$') and x.endswith(('.pdf', '.mp4'))], key=natural_sort_key)
                
                for file_item in files:
                    # En la Sesión 1: aplazar los cuentos para impartirlos tras la clase monográfica de NLM/Cuentos
                    if s_idx == 1 and "CUENT" in file_item.upper():
                        continue
                        
                    rel_path = os.path.relpath(os.path.join(session_path, file_item), ROOT_DIR)
                    rel_path_nfc = unicodedata.normalize('NFC', rel_path)
                    url = BASE_URL + urllib.parse.quote(rel_path_nfc)
                    
                    titulo = clean_title(file_item)
                    descripcion = get_description_for_file(file_item)
                    
                    writer.writerow(['', tema_nombre, titulo, descripcion, url])

def main():
    print("🚀 Generando los 5 Paneles CSV para Google Classroom...")
    generate_panel_0()
    generate_panels_sessions()
    print("\n✅ ¡Los 5 Paneles CSV han sido creados con éxito en la carpeta PANELES_CSV/!")

if __name__ == "__main__":
    main()
