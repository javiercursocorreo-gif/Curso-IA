#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cuadernos_fase_0.py
Genera el PDF oficial de 1 SOLA PÁGINA:
0. FASE_0_GUIA_CUADERNOS_GEMINI.pdf
en CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion/
"""

import os
import subprocess

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "0. FASE_0_GUIA_CUADERNOS_GEMINI.pdf")
PS_PATH = "/tmp/cuadernos_fase_0_1pag.ps"

ETIQUETAS = [
    ("[COMICS]", "CÓMICS", "Novelas gráficas, narrativa secuencial e historietas con IA."),
    ("[TXT]", "TEXTO", "Cartas formales, consultas, comparativas de compra y recetas de salud."),
    ("[EST]", "ESTILO", "Fotografía fotorrealista, acuarela, grabado, cine negro y texturas 3D."),
    ("[PRAC]", "PRÁCTICA", "Retos paso a paso y desafíos interactivos en clase con Gemini."),
    ("[ARTE]", "ARTE", "Obras maestras de la pinacoteca universal y análisis artístico."),
    ("[FRAC]", "FRACTALES", "Geometría en la naturaleza, biomimética y vídeos en alta definición."),
    ("[INT]", "INTERIOR", "Cortes transversales: arquitectura, monumentos y maquinaria por dentro."),
    ("[FUT]", "FUTURO", "Ciencia ficción, hábitats espaciales y robótica avanzada del mañana."),
    ("[NAT]", "NATURALEZA", "Biomecánica animal, aves del mundo y maravillas del reino natural."),
    ("[NIV]", "NIVELES", "Escalafones del conocimiento y clasificaciones universales (101)."),
    ("[TRUC]", "TRUCOS", "Remedios prácticos del hogar, bricolaje rápido y limpieza ecológica."),
    ("[MOVIL]", "MÓVIL", "Símbolos de pantalla, salvavidas de configuración y cámara útil."),
    ("[MEM]", "MEMORIA", "Cápsula de recuerdos: lugares de infancia y objetos de época."),
    ("[MEC]", "MECÁNICA", "Engranajes, motores clásicos e inventos tecnológicos históricos.")
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
    lines.append("%%Pages: 1")
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

/FHead  { /Helvetica-Bold-ISO findfont 14 scalefont setfont } bind def
/FSub   { /Helvetica-Oblique-ISO findfont 9 scalefont setfont } bind def
/FSec   { /Helvetica-Bold-ISO findfont 9.5 scalefont setfont } bind def
/FTxt   { /Helvetica-ISO findfont 8.2 scalefont setfont } bind def
/FTxtB  { /Helvetica-Bold-ISO findfont 8.2 scalefont setfont } bind def
/FTable { /Helvetica-ISO findfont 8 scalefont setfont } bind def
/FTableB{ /Helvetica-Bold-ISO findfont 8.5 scalefont setfont } bind def
/FSmall { /Helvetica-ISO findfont 7.5 scalefont setfont } bind def

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

    lines.append("%%Page: 1 1")
    
    # 1. Cabecera (Y: 780..842)
    lines.append("0.08 0.12 0.22 setrgbcolor 0 782 595 60 rectfill")
    lines.append("0.22 0.74 0.97 setrgbcolor 0 779 595 3 rectfill")
    
    lines.append("1 1 1 setrgbcolor")
    lines.append("FHead 35 814 moveto (" + escape_ps("FASE 0 - GUÍA METODOLÓGICA: TU SISTEMA DE CUADERNOS EN GEMINI") + ") show")
    lines.append("0.75 0.85 0.95 setrgbcolor")
    lines.append("FSub 35 796 moveto (" + escape_ps("Organización de prácticas durante las 60 sesiones del Curso de Inteligencia Artificial") + ") show")
    
    # 2. Caja Metodológica superior (Y: 712..770, h=58)
    lines.append("0.96 0.97 0.99 setrgbcolor")
    lines.append("35 712 525 58 6 roundrect fill")
    lines.append("0.22 0.74 0.97 setrgbcolor")
    lines.append("35 712 525 58 6 roundrect stroke")
    
    lines.append("0.05 0.15 0.35 setrgbcolor")
    lines.append("FSec 48 754 moveto (" + escape_ps("¿Por qué usamos Cuadernos? Regla de oro para trabajar en clase") + ") show")
    lines.append("0.2 0.25 0.3 setrgbcolor")
    lines.append("FTxt 48 740 moveto (" + escape_ps("1. Si abrimos un chat nuevo para cada práctica, al cabo de semanas quedarán perdidas en el historial de chats.") + ") show")
    lines.append("FTxt 48 728 moveto (" + escape_ps("2. Con Cuadernos agrupamos por materia. La 1ª vez que ves una etiqueta, creas su cuaderno; en las siguientes ¡lo reutilizas!") + ") show")
    lines.append("FTxtB 48 716 moveto (" + escape_ps("3. Nombra tu cuaderno exactamente con la palabra de la columna verde para tener todo tu portafolio clasificado.") + ") show")

    # 3. Título de la tabla (Y: 695)
    lines.append("0.1 0.15 0.25 setrgbcolor")
    lines.append("FSec 35 696 moveto (" + escape_ps("TABLA OFICIAL DE REFERENCIA COMPLETA (14 ETIQUETAS DEL CURSO)") + ") show")
    lines.append("FSub 35 685 moveto (" + escape_ps("Escribe en Gemini exactamente la palabra de la 2ª columna para titular cada uno de tus cuadernos:") + ") show")

    # 4. Cabecera de la tabla (Y: 663..681)
    y_th = 663
    lines.append(f"0.15 0.22 0.35 setrgbcolor 35 {y_th} 525 18 rectfill")
    lines.append("1 1 1 setrgbcolor")
    lines.append(f"FTableB 45 {y_th+5} moveto (" + escape_ps("Etiqueta") + ") show")
    lines.append(f"FTableB 115 {y_th+5} moveto (" + escape_ps("Escribe en Gemini (Nombre)") + ") show")
    lines.append(f"FTableB 265 {y_th+5} moveto (" + escape_ps("Qué prácticas guardaremos en este Cuaderno") + ") show")

    # 5. Filas de la tabla (15 filas completas en la misma página)
    # y_th = 663, h_row = 18 pt. 15 filas = 270 pt -> Y va de 643 hasta 373
    y_row = 643
    for idx, (sigla, palabra, desc) in enumerate(ETIQUETAS):
        bg_col = "0.96 0.98 1.0" if idx % 2 == 0 else "1.0 1.0 1.0"
        lines.append(f"{bg_col} setrgbcolor 35 {y_row} 525 18 rectfill")
        lines.append(f"0.86 0.89 0.93 setrgbcolor 35 {y_row} 525 0.5 rectstroke")
        
        # Col 1: Sigla
        lines.append("0.1 0.45 0.8 setrgbcolor")
        lines.append(f"FTableB 45 {y_row+5} moveto (" + escape_ps(sigla) + ") show")
        
        # Col 2: Palabra a escribir (verde oscuro destacado)
        lines.append("0.05 0.48 0.25 setrgbcolor")
        lines.append(f"FTableB 115 {y_row+5} moveto (" + escape_ps(palabra) + ") show")
        
        # Col 3: Qué guardaremos
        lines.append("0.25 0.3 0.35 setrgbcolor")
        lines.append(f"FTable 280 {y_row+5} moveto (" + escape_ps(desc) + ") show")
        
        y_row -= 18

    # 6. Caja inferior de beneficio / resumen didáctico (Y: 275..355, h=80)
    box_y = 275
    lines.append("0.99 0.96 0.92 setrgbcolor")
    lines.append(f"35 {box_y} 525 80 6 roundrect fill")
    lines.append("0.95 0.65 0.2 setrgbcolor")
    lines.append(f"35 {box_y} 525 80 6 roundrect stroke")

    lines.append("0.55 0.3 0.05 setrgbcolor")
    lines.append(f"FSec 48 {box_y+62} moveto (" + escape_ps("[CONSEJO] El Gran Beneficio: Tu Portafolio Personal Ordenado") + ") show")
    lines.append("0.2 0.25 0.3 setrgbcolor")
    lines.append(f"FTxt 48 {box_y+47} moveto (" + escape_ps("- A lo largo de las 60 sesiones realizarás decenas de prácticas fascinantes con inteligencia artificial.") + ") show")
    lines.append(f"FTxt 48 {box_y+34} moveto (" + escape_ps("- Cuando quieras recuperar una receta o redacción formal, irás directo a tu cuaderno TEXTO.") + ") show")
    lines.append(f"FTxt 48 {box_y+21} moveto (" + escape_ps("- Si quieres admirar tus ilustraciones y cuadros generados, abrirás ESTILO y los tendrás todos juntos.") + ") show")
    lines.append(f"FTxtB 48 {box_y+8} moveto (" + escape_ps("- ¡Nunca más volverás a perder una práctica valiosa entre cientos de conversaciones dispersas!") + ") show")

    # 7. Pie de página
    lines.append("0.6 0.65 0.7 setrgbcolor")
    lines.append("FSmall 35 245 moveto (" + escape_ps("Curso de Inteligencia Artificial - Fase 0: Guía Metodológica de Cuadernos - Hoja Oficial de Referencia") + ") show")
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
        print(f"OK:{PDF_PATH}")
    else:
        print(f"ERR:{res.stderr.decode()}")

if __name__ == "__main__":
    build_pdf()
