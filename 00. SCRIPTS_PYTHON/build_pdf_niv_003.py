#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_niv_003.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter):
9. NIV-003_Los_5_Niveles_del_Poder_Geopoltico_y_la.pdf
para la Sesión 03 del Curso de IA.

Contenido:
- Título: Del Telediario a tu Cesta de la Compra (Geopolítica del Hogar)
- Metodología: Generación y ejecución directa en Gemini + BKP Oficial.
- Prompt Maestro exacto para generar la app de 3 columnas (Noticias, Cesta, Tique en 3 pasos).
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/03_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "9. NIV-003_Los_5_Niveles_del_Poder_Geopoltico_y_la.pdf")

ALT_PATHS = [
    "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/09. [NIV] BLOQUE_9_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20/NIV-003_Los 5 Niveles del Poder Geopolítico y Hegemonía Mundial.pdf",
    "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/[NIV] BLOQUE_10_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20/NIV-003_Los_5_Niveles_del_Poder_Geopoltico_y_la.pdf"
]

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
            p_dict = f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.w} {self.h}] /Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> /Contents {content_idx} 0 R >>'.encode('ascii')
            all_objs.append(p_dict)
            stream_bytes = page_stream.encode('latin-1', errors='replace')
            c_dict = f'<< /Length {len(stream_bytes)} >>\nstream\n'.encode('ascii') + stream_bytes + b'\nendstream'
            all_objs.append(c_dict)

        offsets = []
        curr_offset = 15
        pdf_parts = [b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n']

        for i, obj_data in enumerate(all_objs, start=1):
            offsets.append(curr_offset)
            header = f'{i} 0 obj\n'.encode('ascii')
            footer = b'\nendobj\n'
            chunk = header + obj_data + footer
            pdf_parts.append(chunk)
            curr_offset += len(chunk)

        xref_offset = curr_offset
        xref_parts = [f'xref\n0 {len(all_objs) + 1}\n0000000000 65535 f \n'.encode('ascii')]
        for off in offsets:
            xref_parts.append(f'{off:010d} 00000 n \n'.encode('ascii'))
        xref_bytes = b''.join(xref_parts)

        trailer = f'trailer\n<< /Size {len(all_objs) + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n'.encode('ascii')
        pdf_parts.append(xref_bytes)
        pdf_parts.append(trailer)

        with open(filename, 'wb') as f:
            f.write(b''.join(pdf_parts))

def build_niv_003_pdf(output_path=PDF_PATH):
    pdf = NativePDFWriter(page_width=612.0, page_height=792.0)
    pdf.start_page()

    # Cabecera Oficial
    pdf.set_fill_color(0.96, 0.99, 0.97)
    pdf.set_stroke_color(0.05, 0.6, 0.35)
    pdf.set_line_width(1.0)
    pdf.rect(30, 746, 552, 28, fill=True, stroke=True)
    pdf.draw_text(42, 755, 'CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGIA PARA ADULTOS MAYORES (60+)', font='F2', size=8.5, r=0.04, g=0.45, b=0.25)
    pdf.draw_text(410, 755, 'SESION 03 • GUIA DE AULA', font='F2', size=8.0, r=0.2, g=0.3, b=0.4)

    # Subtitulo y Titulo
    pdf.draw_text(30, 730, 'BLOQUE IX: ESCALAFONES DE VIDA REAL Y ECONOMIA DOMESTICA [NIV-003]', font='F2', size=8.8, r=0.05, g=0.55, b=0.3)
    pdf.draw_text(30, 712, '[NIV-003] Del Telediario a tu Cesta de la Compra (Geopolitica del Hogar)', font='F2', size=13.0, r=0.06, g=0.09, b=0.16)

    # Linea divisoria
    pdf.set_stroke_color(0.05, 0.6, 0.35)
    pdf.set_line_width(1.5)
    pdf.line(30, 703, 582, 703)

    # Seccion 1: Mision Didactica
    pdf.draw_text(30, 689, 'MISION DIDACTICA: COMPRENDER COMO LAS NOTICIAS MUNDIALES AFECTAN TU TIQUE DEL SUPER', font='F2', size=9.0, r=0.1, g=0.25, b=0.45)
    intro_p1 = "En esta sesion pediras a Gemini que cree y ejecute directamente en tu pantalla una aplicacion interactiva que conecta los grandes titulares del telediario (subidas del petroleo, sequias en Espana o crisis de transporte maritimo) con los precios reales de los alimentos que compras cada semana. Comprenderas por que el aceite de oliva, la leche o el pan suben o bajan, y como proteger el presupuesto familiar consumiendo productos de temporada y cercania."
    intro_lines = wrap_text(intro_p1, 118)
    pdf.draw_text(30, 675, intro_lines[0], font='F1', size=7.8, r=0.18, g=0.24, b=0.3)
    if len(intro_lines) > 1:
        pdf.draw_text(30, 663, intro_lines[1], font='F1', size=7.8, r=0.18, g=0.24, b=0.3)
    if len(intro_lines) > 2:
        pdf.draw_text(30, 651, intro_lines[2], font='F1', size=7.8, r=0.18, g=0.24, b=0.3)

    # Seccion 2: Metodologia Directa en 2 Pasos
    pdf.set_fill_color(0.98, 0.99, 1.0)
    pdf.set_stroke_color(0.18, 0.55, 0.9)
    pdf.set_line_width(1.0)
    pdf.rect(30, 482, 552, 160, fill=True, stroke=True)

    pdf.draw_text(42, 626, 'METODOLOGIA DIRECTA: GENERACION Y VISUALIZACION EN PANTALLA SIN CODIGO', font='F2', size=9.0, r=0.1, g=0.35, b=0.75)

    paso1 = "Paso 1 • Copia el Prompt Maestro en Gemini: Entra en gemini.google.com con tu cuenta de Google. Pega el texto del recuadro inferior. El prompt esta calibrado para que Gemini abra y ejecute directamente la aplicacion en pantalla (Canvas / Vista previa) sin obligarte a revisar codigo."
    p1_lines = wrap_text(paso1, 114)
    pdf.draw_text(42, 608, p1_lines[0], font='F2', size=8.0, r=0.1, g=0.2, b=0.3)
    pdf.draw_text(42, 596, p1_lines[1], font='F1', size=7.7, r=0.2, g=0.25, b=0.3)

    paso2 = "Paso 2 • Experimenta y Dialoga con Gemini en el Aula: Activa las noticias de impacto (sequia, petroleo o barcos) para ver el efecto en la cesta de 8 alimentos, y plantea a Gemini las 3 preguntas de debate economico que tienes abajo para profundizar."
    p2_lines = wrap_text(paso2, 114)
    pdf.draw_text(42, 574, p2_lines[0], font='F2', size=8.0, r=0.05, g=0.5, b=0.2)
    pdf.draw_text(42, 562, p2_lines[1], font='F1', size=7.7, r=0.2, g=0.25, b=0.3)
    if len(p2_lines) > 2:
        pdf.draw_text(42, 550, p2_lines[2], font='F1', size=7.7, r=0.2, g=0.25, b=0.3)

    paso3 = "Garantia Oficial • Copia de Respaldo Garantizada (BKP en el Mapa): Si tu navegador no muestra el interactivo, ve al Cuadro de Mando del curso y pulsa «🛡️ Abrir Radar Geopolitica y Cesta de la Compra (HTML)». Se abrira al instante la aplicacion oficial depurada con voz y texto grande."
    p3_lines = wrap_text(paso3, 114)
    pdf.draw_text(42, 532, p3_lines[0], font='F2', size=8.0, r=0.8, g=0.4, b=0.05)
    pdf.draw_text(42, 520, p3_lines[1], font='F1', size=7.7, r=0.2, g=0.25, b=0.3)
    if len(p3_lines) > 2:
        pdf.draw_text(42, 508, p3_lines[2], font='F1', size=7.7, r=0.2, g=0.25, b=0.3)

    pdf.draw_text(42, 492, 'Resultado: Simulador visual directo con voz en espanol y letra grande para entender la economia domestica.', font='F3', size=7.5, r=0.35, g=0.4, b=0.45)

    # Seccion 3: Prompt Maestro para Copiar y Pegar en Gemini
    pdf.set_fill_color(0.97, 0.99, 0.98)
    pdf.set_stroke_color(0.05, 0.55, 0.3)
    pdf.set_line_width(1.0)
    pdf.rect(30, 342, 552, 130, fill=True, stroke=True)

    pdf.draw_text(42, 458, 'PROMPT MAESTRO PARA COPIAR Y PEGAR EN GEMINI (VISUALIZACION DIRECTA):', font='F2', size=8.8, r=0.04, g=0.45, b=0.25)

    prompt_lines = [
        "\"Actua como un economista divulgador y pedagogo para adultos mayores (+65).",
        "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador visual sobre la Geopolitica del Hogar:",
        "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
        "1. Columna 1 (Noticias): 4 interruptores con eventos mundiales: Sequia en el campo, Subida del petroleo, Problemas en barcos e Inflacion general.",
        "2. Columna 2 (Cesta del Supermercado): 8 alimentos basicos: Aceite de oliva, Leche, Huevos, Pan, Pollo, Tomates, Arroz y Manzanas.",
        "3. Columna 3 (Tique y Explicacion): Tique de caja con precio base, precio actual y explicacion clara de como la noticia afecta a ese producto.",
        "4. Accesibilidad Senior: Selector de letra grande (18.5px), lectura por voz sintetizada en espanol (es-ES) y boton de reinicio.\""
    ]
    y_pr = 442
    for pl in prompt_lines:
        is_bold = pl.startswith('"Actua') or pl.startswith('Estructura') or pl.startswith('1.') or pl.startswith('2.') or pl.startswith('3.') or pl.startswith('4.')
        pdf.draw_text(48, y_pr, pl, font='F2' if is_bold else 'F1', size=7.2, r=0.08, g=0.2, b=0.3)
        y_pr -= 10.5

    # Seccion 4: Preguntas para Dialogar con Gemini en el Aula
    pdf.set_fill_color(0.99, 0.98, 0.96)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 222, 552, 112, fill=True, stroke=True)

    pdf.draw_text(42, 320, 'PREGUNTAS DE DIALOGO CON GEMINI EN EL AULA (DEBATE ECONOMICO):', font='F2', size=8.8, r=0.7, g=0.35, b=0.05)

    q1 = "Pregunta 1 • La Sequia y el Aceite: \"Gemini, en el simulador veo que la sequia sube la botella de aceite 1,95 € pero los tomates solo suben 0,35 €. ¿Por que el olivo sufre de forma tan diferente a los invernaderos de huerta?\""
    q1_lines = wrap_text(q1, 114)
    pdf.draw_text(42, 304, q1_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 293, q1_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q2 = "Pregunta 2 • El Barco y los Huevos: \"Gemini, al activar 'Problemas en barcos', los huevos suben 0,30 € y el pollo 0,50 €. Si las granjas estan en Espana, ¿por que el transporte maritimo encarece tanto la comida avicola?\""
    q2_lines = wrap_text(q2, 114)
    pdf.draw_text(42, 276, q2_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 265, q2_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q3 = "Pregunta 3 • Estrategia de Ahorro: \"Gemini, ¿cuales son los 3 habitos de compra mas eficaces que una persona mayor jubilada en Espana puede aplicar para no perder poder adquisitivo cuando suben la luz y los combustibles?\""
    q3_lines = wrap_text(q3, 114)
    pdf.draw_text(42, 248, q3_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 237, q3_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    # Seccion 5: Triple Salvaguarda & Garantia Pedagogica
    pdf.set_fill_color(0.98, 0.98, 0.99)
    pdf.set_stroke_color(0.5, 0.5, 0.6)
    pdf.set_line_width(0.8)
    pdf.rect(30, 105, 552, 108, fill=True, stroke=True)

    pdf.draw_text(42, 199, 'LA TRIPLE SALVAGUARDA PEDAGOGICA Y ACCESIBILIDAD SENIOR:', font='F2', size=8.5, r=0.2, g=0.25, b=0.35)
    fuente1 = "- Explicacion en 3 Pasos Visuales: La aplicacion divide el impacto de cada alimento en: 1. Que pasa lejos (origen mundial), 2. Como nos afecta aqui (transporte y costes nacionales) y 3. Que vemos en la tienda (precio final en estanteria)."
    f1_lines = wrap_text(fuente1, 114)
    pdf.draw_text(42, 185, f1_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f1_lines) > 1:
        pdf.draw_text(42, 174, f1_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente2 = "- Diseno Ergonomico sin Barreras: Letra ampliable a 18.5px, botones de alto contraste, lectura por voz sintetizada en espanol nativo y adaptacion automatica a portatiles, pantallas de aula y tabletas iPad."
    f2_lines = wrap_text(fuente2, 114)
    pdf.draw_text(42, 159, f2_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f2_lines) > 1:
        pdf.draw_text(42, 148, f2_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente3 = "- Garantia de Respaldo Tecnico: El alumno experimenta el prompt en Gemini sabiendo que dispone del simulador oficial garantizado en el Cuadro de Mando del curso para asegurar el 100% de exito pedagógico en la clase."
    f3_lines = wrap_text(fuente3, 114)
    pdf.draw_text(42, 133, f3_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f3_lines) > 1:
        pdf.draw_text(42, 122, f3_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    # Banner inferior BKP
    pdf.set_fill_color(0.06, 0.09, 0.16)
    pdf.set_stroke_color(0.2, 0.8, 0.5)
    pdf.set_line_width(1.2)
    pdf.rect(30, 42, 552, 54, fill=True, stroke=True)

    pdf.draw_text(42, 80, 'APLICACION OFICIAL GARANTIZADA (BKP): SIMULADOR_RADAR_GEOPOLITICA_SENIORS.HTML', font='F2', size=8.8, r=0.2, g=0.85, b=0.5)
    pdf.draw_text(42, 65, 'Si deseas abrir la aplicacion terminada y depurada, en el Cuadro de Mando de la Sesion 03 haz clic en:', font='F1', size=7.6, r=0.8, g=0.85, b=0.9)
    pdf.draw_text(42, 52, '«🛡️ Abrir Radar Geopolitica y Cesta de la Compra (+65) (HTML)» para interactuar al instante con datos reales.', font='F2', size=7.8, r=0.2, g=0.85, b=0.5)

    pdf.end_page()

    pdf.write_to_file(output_path)
    for alt in ALT_PATHS:
        try:
            os.makedirs(os.path.dirname(alt), exist_ok=True)
            shutil.copy2(output_path, alt)
        except Exception:
            pass

    print(f"✅ PDF NIV-003 generado con éxito en: {output_path}")
    return output_path

if __name__ == '__main__':
    try:
        build_niv_003_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF NIV-003: {e}")
        sys.exit(1)
