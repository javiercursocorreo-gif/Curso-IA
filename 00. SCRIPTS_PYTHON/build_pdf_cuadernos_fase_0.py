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

# ETIQUETAS: (Sigla, Nombre a escribir en Gemini, Qué guardaremos en este Cuaderno)
ETIQUETAS = [
    ("[TXT]", "TEXTO", "Cartas formales, reclamaciones, comparativas de compra, menús de salud y consultas."),
    ("[EST]", "ESTILO", "Fotografía realista, acuarela, grabado, cine negro, texturas 3D y técnicas visuales."),
    ("[PRAC]", "PRÁCTICA", "Ejercicios guiados paso a paso y desafíos interactivos en clase con Gemini."),
    ("[ARTE]", "ARTE", "Obras maestras de la pinacoteca universal, genios de la pintura y análisis estético."),
    ("[FRAC]", "FRACTALES", "Formas de la naturaleza, matemáticas visuales y vídeos en alta definición."),
    ("[FUNC]", "FUNCIONES", "Fórmulas matemáticas en 3D, superficies complejas y geometría computacional."),
    ("[INT]", "INTERIOR", "Cortes transversales, arquitectura interior, monumentos y maquinaria por dentro."),
    ("[FUT]", "FUTURO", "El mundo del mañana, hábitats espaciales, robótica avanzada y vida futura."),
    ("[NAT]", "NATURALEZA", "Biomecánica animal, aves del mundo, botánica y maravillas del reino natural."),
    ("[NIV]", "NIVELES", "Pirámides de conocimiento, escalas jerárquicas y clasificaciones universales (101)."),
    ("[TRUC]", "TRUCOS", "Remedios prácticos, bricolaje rápido, limpieza ecológica y soluciones caseras."),
    ("[MOVIL]", "MÓVIL", "Símbolos de pantalla, configuración rápida, alertas del hogar y cámara útil."),
    ("[MEM]", "MEMORIA", "Lugares de infancia, objetos de época, oficios antiguos y memoria compartida."),
    ("[MEC]", "MECÁNICA", "Funcionamiento de ingenios mecánicos, motores clásicos y tecnología histórica."),
    ("[CUENT]", "CUENTOS", "Historias ilustradas y cómics secuenciales con IA (tras la lección de NotebookLM).")
]

def escape_ps(text):
    res = []
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
/FSmallB { /Helvetica-Bold-ISO findfont 8.5 scalefont setfont } bind def

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
    # PÁGINA 1: Introducción didáctica y primeras 8 etiquetas
    # =========================================================================
    lines.append("%%Page: 1 1")
    
    # Barra superior decorativa
    lines.append("0.08 0.12 0.22 setrgbcolor 0 760 595 82 rectfill")
    lines.append("0.22 0.74 0.97 setrgbcolor 0 757 595 3 rectfill")
    
    # Títulos cabecera
    lines.append("1 1 1 setrgbcolor")
    lines.append("FHead 40 790 moveto (" + escape_ps("FASE 0 - GUÍA METODOLÓGICA: TU SISTEMA DE CUADERNOS EN GEMINI") + ") show")
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
    lines.append("FSec 40 562 moveto (" + escape_ps("TABLA OFICIAL DE REFERENCIA: ETIQUETAS Y PALABRA PARA EL CUADERNO") + ") show")
    lines.append("FSub 40 550 moveto (" + escape_ps("Escribe en Gemini exactamente la palabra de la 2ª columna para nombrar cada cuaderno:") + ") show")

    # Coordenadas X:
    # Margen izquierdo: 40 | Ancho total: 515
    # Col 1 (Sigla): 40..105 (65 pt)
    # Col 2 (Palabra a escribir como Nombre de Cuaderno): 105..250 (145 pt)
    # Col 3 (Qué guardaremos en este Cuaderno): 250..555 (305 pt)
    
    def draw_table_header(y):
        lines.append(f"0.15 0.22 0.35 setrgbcolor 40 {y} 515 20 rectfill")
        lines.append("1 1 1 setrgbcolor")
        lines.append(f"FSmallB 48 {y+6} moveto (" + escape_ps("Etiqueta") + ") show")
        lines.append(f"FSmallB 115 {y+6} moveto (" + escape_ps("Nombre a escribir en Gemini") + ") show")
        lines.append(f"FSmallB 260 {y+6} moveto (" + escape_ps("Qué prácticas guardaremos en este Cuaderno") + ") show")

    draw_table_header(524)

    # Dibujar filas de la Página 1 (primeras 8 etiquetas)
    y_row = 502
    for idx, (sigla, palabra, desc) in enumerate(ETIQUETAS[:8]):
        bg_col = "0.96 0.98 1.0" if idx % 2 == 0 else "1.0 1.0 1.0"
        lines.append(f"{bg_col} setrgbcolor 40 {y_row} 515 22 rectfill")
        lines.append(f"0.85 0.88 0.92 setrgbcolor 40 {y_row} 515 0.5 rectstroke")
        
        # Col 1: Sigla
        lines.append("0.1 0.45 0.8 setrgbcolor")
        lines.append(f"FSmallB 48 {y_row+7} moveto (" + escape_ps(sigla) + ") show")
        
        # Col 2: Palabra a escribir en Gemini (destacada en verde oscuro / bold)
        lines.append("0.05 0.45 0.25 setrgbcolor")
        lines.append(f"FSmallB 115 {y_row+7} moveto (" + escape_ps(palabra) + ") show")
        
        # Col 3: Descripción de qué guardaremos
        lines.append("0.25 0.3 0.35 setrgbcolor")
        words = desc.split()
        l1, l2 = [], []
        curr = l1
        for w in words:
            if curr is l1 and len(" ".join(l1 + [w])) <= 65:
                l1.append(w)
            else:
                curr = l2
                l2.append(w)
        lines.append(f"FSmall 260 {y_row+11} moveto (" + escape_ps(" ".join(l1)) + ") show")
        if l2:
            lines.append(f"FSmall 260 {y_row+2} moveto (" + escape_ps(" ".join(l2)) + ") show")
            
        y_row -= 23

    # Pie de página 1
    lines.append("0.6 0.65 0.7 setrgbcolor")
    lines.append("FSmall 40 40 moveto (" + escape_ps("Curso de Inteligencia Artificial - Fase 0: Guía Metodológica de Cuadernos - Página 1 de 2") + ") show")
    lines.append("showpage")

    # =========================================================================
    # PÁGINA 2: Resto de etiquetas (7 restantes) y consejo
    # =========================================================================
    lines.append("%%Page: 2 2")
    
    # Barra superior decorativa
    lines.append("0.08 0.12 0.22 setrgbcolor 0 760 595 82 rectfill")
    lines.append("0.22 0.74 0.97 setrgbcolor 0 757 595 3 rectfill")
    
    # Títulos cabecera pág 2
    lines.append("1 1 1 setrgbcolor")
    lines.append("FHead 40 790 moveto (" + escape_ps("FASE 0 - TABLA DE CUADERNOS DE GEMINI (CONTINUACIÓN)") + ") show")
    lines.append("0.75 0.85 0.95 setrgbcolor")
    lines.append("FSub 40 770 moveto (" + escape_ps("Etiquetas de Ciencias, Vida Práctica, Teléfono Móvil, Memoria y Cuentos") + ") show")

    draw_table_header(726)

    # Dibujar filas de la Página 2 (etiquetas 8 a 14)
    y_row = 704
    for idx, (sigla, palabra, desc) in enumerate(ETIQUETAS[8:]):
        bg_col = "0.96 0.98 1.0" if idx % 2 == 0 else "1.0 1.0 1.0"
        lines.append(f"{bg_col} setrgbcolor 40 {y_row} 515 22 rectfill")
        lines.append(f"0.85 0.88 0.92 setrgbcolor 40 {y_row} 515 0.5 rectstroke")
        
        # Col 1: Sigla
        lines.append("0.1 0.45 0.8 setrgbcolor")
        lines.append(f"FSmallB 48 {y_row+7} moveto (" + escape_ps(sigla) + ") show")
        
        # Col 2: Palabra a escribir en Gemini
        lines.append("0.05 0.45 0.25 setrgbcolor")
        lines.append(f"FSmallB 115 {y_row+7} moveto (" + escape_ps(palabra) + ") show")
        
        # Col 3: Descripción
        lines.append("0.25 0.3 0.35 setrgbcolor")
        words = desc.split()
        l1, l2 = [], []
        curr = l1
        for w in words:
            if curr is l1 and len(" ".join(l1 + [w])) <= 65:
                l1.append(w)
            else:
                curr = l2
                l2.append(w)
        lines.append(f"FSmall 260 {y_row+11} moveto (" + escape_ps(" ".join(l1)) + ") show")
        if l2:
            lines.append(f"FSmall 260 {y_row+2} moveto (" + escape_ps(" ".join(l2)) + ") show")
            
        y_row -= 23

    # Caja de Consejo de Oro: ¿Qué pasa cuando abres una sesión?
    # Se eliminó el párrafo final de [INICIO], dejando esta caja con amplio respiro
    box1_top = y_row - 35
    lines.append("0.99 0.96 0.92 setrgbcolor")
    lines.append(f"40 {box1_top-110} 515 110 8 roundrect fill")
    lines.append("0.95 0.65 0.2 setrgbcolor")
    lines.append(f"40 {box1_top-110} 515 110 8 roundrect stroke")

    lines.append("0.55 0.3 0.05 setrgbcolor")
    lines.append(f"FSec 55 {box1_top-22} moveto (" + escape_ps("[CONSEJO] El Gran Beneficio: Tu Portafolio Personal Ordenado") + ") show")
    lines.append("0.2 0.25 0.3 setrgbcolor")
    lines.append(f"FTxt 55 {box1_top-42} moveto (" + escape_ps("- A lo largo de las 60 sesiones realizarás decenas de ejercicios fascinantes.") + ") show")
    lines.append(f"FTxt 55 {box1_top-58} moveto (" + escape_ps("- Con este método, cuando busques una receta o redacción formal, irás directo a tu cuaderno TEXTO.") + ") show")
    lines.append(f"FTxt 55 {box1_top-74} moveto (" + escape_ps("- Si quieres revisar tus cuadros e ilustraciones, abrirás ESTILO y los tendrás todos reunidos.") + ") show")
    lines.append(f"FTxtB 55 {box1_top-92} moveto (" + escape_ps("- ¡Nunca más volverás a perder una práctica valiosa entre cientos de conversaciones dispersas!") + ") show")

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
