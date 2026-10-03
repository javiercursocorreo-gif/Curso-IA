#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cuadernos_fase_0.py
Genera el PDF oficial:
0. FASE_0_GUIA_CUADERNOS_GEMINI.pdf
en CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion/
"""

import os
import subprocess

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "0. FASE_0_GUIA_CUADERNOS_GEMINI.pdf")
PS_PATH = "/tmp/cuadernos_fase_0.ps"

ETIQUETAS = [
    ("[TXT]", "Prompts y Comunicación de Texto", "Prompts y Comunicación de Texto", "Cartas formales, reclamaciones, comparativas de compra, menús de salud y consultas."),
    ("[EST]", "Estilos Artísticos de Imagen IA", "Estilos Artísticos e Imagen IA", "Fotografía realista, acuarela, grabado, cine negro, texturas 3D y técnicas visuales."),
    ("[PRAC]", "Taller Práctico y Retos Gemini", "Taller Práctico Gemini", "Ejercicios guiados paso a paso y desafíos interactivos en clase con Gemini."),
    ("[ARTE]", "Historia del Arte y Pintura Clásica", "Historia del Arte", "Obras maestras de la pinacoteca universal, genios de la pintura y análisis estético."),
    ("[FRAC]", "Geometría Fractal y Biomimética", "Fractales y Biomimética", "Formas de la naturaleza, matemáticas visuales y vídeos en alta definición."),
    ("[FUNC]", "Funciones y Modelado Visual 3D", "Funciones y Modelado 3D", "Fórmulas matemáticas en 3D, superficies complejas y geometría computacional."),
    ("[INT]", "El Mundo por Dentro (Cortes)", "El Mundo por Dentro", "Cortes transversales, arquitectura interior, monumentos y maquinaria por dentro."),
    ("[FUT]", "Ciencia Ficción y Visión de Futuro", "Ciencia Ficción y Futuro", "El mundo del mañana, hábitats espaciales, robótica avanzada y vida futura."),
    ("[NAT]", "Naturaleza Fascinante y Fauna", "Naturaleza y Biodiversidad", "Biomecánica animal, aves del mundo, botánica y maravillas del reino natural."),
    ("[NIV]", "Escalafones y Niveles del Mundo", "Escalafones y Niveles", "Pirámides de conocimiento, escalas jerárquicas y clasificaciones universales (101)."),
    ("[TRUC]", "Trucos Cotidianos y del Hogar", "Trucos y Consejos del Hogar", "Remedios prácticos, bricolaje rápido, limpieza ecológica y soluciones caseras."),
    ("[MOVIL]", "Salvavidas del Teléfono Móvil", "Salvavidas del Móvil", "Símbolos de pantalla, configuración rápida, alertas del hogar y cámara útil."),
    ("[MEM]", "Cápsula de Memoria y Recuerdos", "Cápsula de Memoria", "Lugares de infancia, objetos de época, oficios antiguos y memoria compartida."),
    ("[MEC]", "Mecánica, Engranajes e Inventos", "Mecánica e Inventos", "Funcionamiento de ingenios mecánicos, motores clásicos y tecnología histórica."),
    ("[CUENT]", "Cuentos y Cómics Ilustrados", "Cuentos y Cómics Ilustrados", "Historias ilustradas y cómics secuenciales con IA (tras la lección de NotebookLM).")
]

def escape_ps(text):
    # Convertir a octal de Latin1 para PostScript
    res = []
    # Reemplazar caracteres especiales si los hay
    text = text.replace("•", "-")
    for ch in text:
        if ch == '(':
            res.append(r'\(')
        elif ch == ')':
            res.append(r'\)')
        elif ch == '\\':
            res.append(r'\\')
        else:
            b = ch.encode('latin1', errors='replace')[0]
            if b < 32 or b >= 127:
                res.append(f'\\{b:03o}')
            else:
                res.append(chr(b))
    return ''.join(res)

def generate_ps():
    lines = []
    lines.append("%!PS-Adobe-3.0")
    lines.append("%%BoundingBox: 0 0 595 842")
    lines.append("%%Pages: 2")
    lines.append("%%DocumentData: Clean7Bit")
    
    # Configurar codificación Latin1 para tipografías
    setup_font = """
/reencodeISO {
  findfont
  dup length dict begin
    {1 index /FID ne {def} {pop pop} ifelse} forall
    /Encoding ISOLatin1Encoding def
    currentdict
  end
  definefont pop
} bind def

/Helvetica-ISO /Helvetica reencodeISO
/Helvetica-Bold-ISO /Helvetica-Bold reencodeISO
/Helvetica-Oblique-ISO /Helvetica-Oblique reencodeISO

/FHead { /Helvetica-Bold-ISO findfont 15 scalefont setfont } bind def
/FSub  { /Helvetica-Oblique-ISO findfont 10 scalefont setfont } bind def
/FSec  { /Helvetica-Bold-ISO findfont 11 scalefont setfont } bind def
/FTxt  { /Helvetica-ISO findfont 9 scalefont setfont } bind def
/FTxtB { /Helvetica-Bold-ISO findfont 9 scalefont setfont } bind def
/FSmall { /Helvetica-ISO findfont 8 scalefont setfont } bind def
/FSmallB { /Helvetica-Bold-ISO findfont 8 scalefont setfont } bind def

/roundrect {
  /r exch def
  /h exch def
  /w exch def
  /y exch def
  /x exch def
  x r add y moveto
  x w add y x w add y h add r arcto 4 {pop} repeat
  x w add y h add x y h add r arcto 4 {pop} repeat
  x y h add x y r arcto 4 {pop} repeat
  x y x w add y r arcto 4 {pop} repeat
  closepath
} bind def
"""
    lines.append(setup_font)

    # =========================================================================
    # PÁGINA 1: Introducción didáctica y primeros 8 cuadernos
    # =========================================================================
    lines.append("%%Page: 1 1")
    
    # Barra superior decorativa
    lines.append("0.08 0.12 0.22 setrgbcolor 0 760 595 82 rectfill")
    lines.append("0.22 0.74 0.97 setrgbcolor 0 757 595 3 rectfill")
    
    # Títulos cabecera
    lines.append("1 1 1 setrgbcolor")
    lines.append("FHead 40 790 moveto (" + escape_ps("FASE 0 • GUÍA METODOLÓGICA: TU SISTEMA DE CUADERNOS EN GEMINI") + ") show")
    lines.append("0.75 0.85 0.95 setrgbcolor")
    lines.append("FSub 40 770 moveto (" + escape_ps("Organización de prácticas durante las 60 sesiones del Curso de Inteligencia Artificial") + ") show")
    
    # Caja explicativa: El problema y la solución
    lines.append("0.96 0.97 0.99 setrgbcolor")
    lines.append("40 670 515 72 8 roundrect fill")
    lines.append("0.22 0.74 0.97 setrgbcolor")
    lines.append("40 670 515 72 8 roundrect stroke")
    
    lines.append("0.05 0.15 0.35 setrgbcolor")
    lines.append("FSec 55 722 moveto (" + escape_ps("¿Por qué usamos el Sistema de Cuadernos en lugar de abrir chats sueltos?") + ") show")
    lines.append("0.2 0.25 0.3 setrgbcolor")
    lines.append("FTxt 55 707 moveto (" + escape_ps("1. En Gemini, si abrimos un chat nuevo para cada práctica, quedarán desperdigados en el historial.") + ") show")
    lines.append("FTxt 55 694 moveto (" + escape_ps("2. Con la función CUADERNOS de Gemini, agrupamos todo el trabajo por MATERIAS y TEMÁTICAS.") + ") show")
    lines.append("FTxtB 55 680 moveto (" + escape_ps("Regla de Oro: La 1ª vez que veas una etiqueta creas su Cuaderno; en las siguientes ¡reutilizas ese cuaderno!") + ") show")

    # Los 3 pasos del alumno
    lines.append("0.94 0.98 0.95 setrgbcolor")
    lines.append("40 585 515 70 8 roundrect fill")
    lines.append("0.2 0.7 0.4 setrgbcolor")
    lines.append("40 585 515 70 8 roundrect stroke")
    
    lines.append("0.1 0.4 0.2 setrgbcolor")
    lines.append("FSec 55 635 moveto (" + escape_ps("Cómo funciona en clase: 3 Pasos muy sencillos") + ") show")
    lines.append("0.2 0.25 0.3 setrgbcolor")
    lines.append("FTxt 55 621 moveto (" + escape_ps("Paso A: Mira la etiqueta del ejercicio que vas a realizar (ejemplo: TXT, EST, ARTE, NIV...).") + ") show")
    lines.append("FTxt 55 608 moveto (" + escape_ps("Paso B: Entra en Gemini > Cuadernos. Si aún no existe, pulsa [+] y ponle el NOMBRE OFICIAL.") + ") show")
    lines.append("FTxt 55 595 moveto (" + escape_ps("Paso C: Si ya lo creaste en una clase anterior, ábrelo y haz allí tu práctica. ¡Todo ordenado!") + ") show")

    # Título de la tabla
    lines.append("0.1 0.15 0.25 setrgbcolor")
    lines.append("FSec 40 562 moveto (" + escape_ps("TABLA OFICIAL DE REFERENCIA: ETIQUETAS Y NOMBRES DE CUADERNOS") + ") show")
    lines.append("FSub 40 550 moveto (" + escape_ps("Consulta esta tabla siempre que vayas a nombrar un cuaderno nuevo en Google Gemini (4 Columnas):") + ") show")

    # Coordenadas X:
    # Margen izquierdo: 40 | Ancho total: 515
    # Col 1 (Sigla): 40..85 (45 pt)
    # Col 2 (Nombre completo etiqueta): 85..235 (150 pt)
    # Col 3 (Nombre en Gemini): 235..380 (145 pt)
    # Col 4 (Qué guardaremos): 380..555 (175 pt)
    
    def draw_table_header(y):
        lines.append(f"0.15 0.22 0.35 setrgbcolor 40 {y} 515 20 rectfill")
        lines.append("1 1 1 setrgbcolor")
        lines.append(f"FSmallB 45 {y+6} moveto (" + escape_ps("Sigla") + ") show")
        lines.append(f"FSmallB 90 {y+6} moveto (" + escape_ps("Nombre Completo Etiqueta") + ") show")
        lines.append(f"FSmallB 240 {y+6} moveto (" + escape_ps("Nombre de tu Cuaderno en Gemini") + ") show")
        lines.append(f"FSmallB 385 {y+6} moveto (" + escape_ps("Qué guardaremos en este Cuaderno") + ") show")

    draw_table_header(524)

    # Dibujar filas de la Página 1 (primeras 8 etiquetas)
    y_row = 502
    for idx, (sigla, nom_etiqueta, nom_cuaderno, desc) in enumerate(ETIQUETAS[:8]):
        bg_col = "0.96 0.98 1.0" if idx % 2 == 0 else "1.0 1.0 1.0"
        lines.append(f"{bg_col} setrgbcolor 40 {y_row} 515 22 rectfill")
        lines.append(f"0.85 0.88 0.92 setrgbcolor 40 {y_row} 515 0.5 rectstroke")
        
        # Sigla
        lines.append("0.1 0.45 0.8 setrgbcolor")
        lines.append(f"FSmallB 46 {y_row+7} moveto (" + escape_ps(sigla) + ") show")
        
        # Nombre completo etiqueta
        lines.append("0.15 0.2 0.25 setrgbcolor")
        lines.append(f"FSmallB 90 {y_row+7} moveto (" + escape_ps(nom_etiqueta) + ") show")
        
        # Nombre Cuaderno Gemini
        lines.append("0.05 0.35 0.2 setrgbcolor")
        lines.append(f"FSmallB 240 {y_row+7} moveto (" + escape_ps(nom_cuaderno) + ") show")
        
        # Descripción
        lines.append("0.35 0.4 0.45 setrgbcolor")
        words = desc.split()
        l1, l2 = [], []
        curr = l1
        for w in words:
            if curr is l1 and len(" ".join(l1 + [w])) <= 38:
                l1.append(w)
            else:
                curr = l2
                l2.append(w)
        lines.append(f"FSmall 385 {y_row+11} moveto (" + escape_ps(" ".join(l1)) + ") show")
        if l2:
            lines.append(f"FSmall 385 {y_row+2} moveto (" + escape_ps(" ".join(l2)) + ") show")
            
        y_row -= 23

    # Pie de página 1
    lines.append("0.6 0.65 0.7 setrgbcolor")
    lines.append("FSmall 40 40 moveto (" + escape_ps("Curso de Inteligencia Artificial - Fase 0: Guía Metodológica de Cuadernos - Página 1 de 2") + ") show")
    lines.append("showpage")

    # =========================================================================
    # PÁGINA 2: Resto de etiquetas (7 restantes) y consejos finales
    # =========================================================================
    lines.append("%%Page: 2 2")
    
    # Barra superior decorativa
    lines.append("0.08 0.12 0.22 setrgbcolor 0 760 595 82 rectfill")
    lines.append("0.22 0.74 0.97 setrgbcolor 0 757 595 3 rectfill")
    
    # Títulos cabecera pág 2
    lines.append("1 1 1 setrgbcolor")
    lines.append("FHead 40 790 moveto (" + escape_ps("FASE 0 • TABLA DE CUADERNOS DE GEMINI (CONTINUACIÓN)") + ") show")
    lines.append("0.75 0.85 0.95 setrgbcolor")
    lines.append("FSub 40 770 moveto (" + escape_ps("Etiquetas de Ciencias, Vida Práctica, Teléfono Móvil, Memoria y Cuentos") + ") show")

    draw_table_header(726)

    # Dibujar filas de la Página 2 (etiquetas 8 a 14)
    y_row = 704
    for idx, (sigla, nom_etiqueta, nom_cuaderno, desc) in enumerate(ETIQUETAS[8:]):
        bg_col = "0.96 0.98 1.0" if idx % 2 == 0 else "1.0 1.0 1.0"
        lines.append(f"{bg_col} setrgbcolor 40 {y_row} 515 22 rectfill")
        lines.append(f"0.85 0.88 0.92 setrgbcolor 40 {y_row} 515 0.5 rectstroke")
        
        # Sigla
        lines.append("0.1 0.45 0.8 setrgbcolor")
        lines.append(f"FSmallB 46 {y_row+7} moveto (" + escape_ps(sigla) + ") show")
        
        # Nombre completo etiqueta
        lines.append("0.15 0.2 0.25 setrgbcolor")
        lines.append(f"FSmallB 90 {y_row+7} moveto (" + escape_ps(nom_etiqueta) + ") show")
        
        # Nombre Cuaderno Gemini
        lines.append("0.05 0.35 0.2 setrgbcolor")
        lines.append(f"FSmallB 240 {y_row+7} moveto (" + escape_ps(nom_cuaderno) + ") show")
        
        # Descripción
        lines.append("0.35 0.4 0.45 setrgbcolor")
        words = desc.split()
        l1, l2 = [], []
        curr = l1
        for w in words:
            if curr is l1 and len(" ".join(l1 + [w])) <= 38:
                l1.append(w)
            else:
                curr = l2
                l2.append(w)
        lines.append(f"FSmall 385 {y_row+11} moveto (" + escape_ps(" ".join(l1)) + ") show")
        if l2:
            lines.append(f"FSmall 385 {y_row+2} moveto (" + escape_ps(" ".join(l2)) + ") show")
            
        y_row -= 23

    # Separación antes de la primera caja
    box1_top = y_row - 25
    lines.append("0.99 0.96 0.92 setrgbcolor")
    lines.append(f"40 {box1_top-88} 515 88 8 roundrect fill")
    lines.append("0.95 0.65 0.2 setrgbcolor")
    lines.append(f"40 {box1_top-88} 515 88 8 roundrect stroke")

    lines.append("0.55 0.3 0.05 setrgbcolor")
    lines.append(f"FSec 55 {box1_top-20} moveto (" + escape_ps("[CONSEJO] El Gran Beneficio: Tu Portafolio Personal Ordenado") + ") show")
    lines.append("0.2 0.25 0.3 setrgbcolor")
    lines.append(f"FTxt 55 {box1_top-36} moveto (" + escape_ps("- A lo largo del curso harás decenas de prácticas fascinantes con inteligencia artificial.") + ") show")
    lines.append(f"FTxt 55 {box1_top-50} moveto (" + escape_ps("- Gracias a este sistema, cuando busques una receta o carta formal, entrarás directo a tu cuaderno.") + ") show")
    lines.append(f"FTxt 55 {box1_top-64} moveto (" + escape_ps("- Si quieres ver tus cuadros e imágenes, abres 'Estilos Artísticos e Imagen IA' y los tendrás juntos.") + ") show")
    lines.append(f"FTxtB 55 {box1_top-78} moveto (" + escape_ps("- ¡Nunca más volverás a perder una conversación importante entre cientos de chats anónimos!") + ") show")

    # Resumen de inicio para la Sesión 1
    box2_top = box1_top - 105
    lines.append("0.95 0.97 1.0 setrgbcolor")
    lines.append(f"40 {box2_top-105} 515 105 8 roundrect fill")
    lines.append("0.3 0.5 0.9 setrgbcolor")
    lines.append(f"40 {box2_top-105} 515 105 8 roundrect stroke")

    lines.append("0.1 0.2 0.6 setrgbcolor")
    lines.append(f"FSec 55 {box2_top-20} moveto (" + escape_ps("[INICIO] Para empezar hoy en la SESIÓN 01:") + ") show")
    lines.append("0.2 0.25 0.3 setrgbcolor")
    lines.append(f"FTxt 55 {box2_top-36} moveto (" + escape_ps("En esta primera clase abrirás por primera vez los cuadernos de las etiquetas del día:") + ") show")
    lines.append(f"FTxtB 55 {box2_top-50} moveto (" + escape_ps("1. Prompts y Comunicación de Texto (para la práctica #01 TXT)") + ") show")
    lines.append(f"FTxtB 55 {box2_top-64} moveto (" + escape_ps("2. Estilos Artísticos e Imagen IA (para la práctica #02 EST)") + ") show")
    lines.append(f"FTxtB 55 {box2_top-78} moveto (" + escape_ps("3. Taller Práctico Gemini (para el retrato mágico #03 PRAC)") + ") show")
    lines.append(f"FTxtB 55 {box2_top-92} moveto (" + escape_ps("4. Historia del Arte (para la Gioconda #04 ARTE)") + ") show")

    # Pie de página 2
    lines.append("0.6 0.65 0.7 setrgbcolor")
    lines.append("FSmall 40 40 moveto (" + escape_ps("Curso de Inteligencia Artificial - Fase 0: Guía Metodológica de Cuadernos - Página 2 de 2") + ") show")
    lines.append("showpage")

    return "\n".join(lines)

def build_pdf():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ps_content = generate_ps()
    with open(PS_PATH, "w", encoding="latin1") as f:
        f.write(ps_content)
    
    cmd = ["/usr/bin/pstopdf", PS_PATH, "-o", PDF_PATH]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode == 0:
        print(f"✅ PDF generado con éxito ({os.path.getsize(PDF_PATH)} bytes): {PDF_PATH}")
    else:
        print(f"❌ Error al compilar PDF: {res.stderr.decode()}")

if __name__ == "__main__":
    build_pdf()
