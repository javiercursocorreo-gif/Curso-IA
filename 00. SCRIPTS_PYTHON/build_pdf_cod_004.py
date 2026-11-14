#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_004.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 04 del Curso de IA.

Contenido simplificado y desatendido:
- Generación y ejecución directa de código en el chat de Gemini.
- Cero visores externos ni talleres manuales.
- Copia de respaldo (BKP) oficial garantizada con SIMULADOR_OJO_HUMANO_3D.html.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/04_COD-004_Taller_Simulador_Ojo_Humano_3D.pdf"

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

def build_cod_004_pdf(output_path=PDF_PATH):
    pdf = NativePDFWriter(612.0, 792.0)
    pdf.start_page()

    # Marco exterior elegante azul marino y cian
    pdf.set_fill_color(0.985, 0.995, 1.0)
    pdf.set_stroke_color(0.02, 0.5, 0.75)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal
    pdf.set_fill_color(0.03, 0.15, 0.3)
    pdf.rect(24, 716, 564, 52, fill=True, stroke=False)

    pdf.draw_text(36, 750, 'SESION 04 • FICHA DIDACTICA DE CODIGO CON GEMINI [COD-004]', font='F2', size=8.5, r=0.4, g=0.8, b=1.0)
    pdf.draw_text(36, 730, 'Simulador 3D del Ojo Humano con Gemini (Anatomia y Optica)', font='F2', size=13.0, r=1, g=1, b=1)

    # Seccion 1: Metodologia en 3 Pasos Directos en Gemini
    pdf.set_fill_color(0.92, 0.97, 1.0)
    pdf.set_stroke_color(0.05, 0.55, 0.85)
    pdf.set_line_width(1.0)
    pdf.rect(30, 575, 552, 130, fill=True, stroke=True)

    pdf.draw_text(42, 688, 'METODOLOGIA EN 3 PASOS: GENERACION Y EJECUCION DIRECTA EN GEMINI', font='F2', size=9.5, r=0.03, g=0.3, b=0.6)

    p1_title = 'PASO 1 • Copiar el Prompt Maestro en Gemini (gemini.google.com):'
    p1_desc = 'Accede a Gemini desde tu navegador habitual. Copia integro el recuadro azul inferior y pegalo en la barra de chat de Gemini sin modificar nada.'
    pdf.draw_text(42, 672, p1_title, font='F2', size=8.0, r=0.05, g=0.4, b=0.7)
    pdf.draw_text(42, 661, p1_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p2_title = 'PASO 2 • Indicar a Gemini la visualizacion directa en tu pantalla:'
    p2_desc = 'Cuando Gemini te responda con el bloque de codigo, no tienes que copiarlo ni abrir visores externos. Escribe de inmediato en el chat:'
    p2_cmd = '«Ejecuta este codigo y muestramelo en pantalla» (o «Run code»). Gemini renderizara el ojo 3D directamente dentro de la conversacion.'
    pdf.draw_text(42, 646, p2_title, font='F2', size=8.0, r=0.05, g=0.4, b=0.7)
    pdf.draw_text(42, 635, p2_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    pdf.draw_text(42, 624, p2_cmd, font='F2', size=7.8, r=0.02, g=0.45, b=0.3)

    p3_title = 'PASO 3 • Copia de Respaldo Garantizada (BKP Oficial en el Mapa):'
    p3_desc = 'Si por saturacion del servidor o corte de conexion no visualizas el modelo 3D, pulsa en el Cuadro de Mando de la Sesion 04 el boton:'
    p3_btn = '«👁️ Ver Simulador Ojo Humano 3D (BKP)» para abrir la maqueta oficial garantizada con Three.js de alta definicion.'
    pdf.draw_text(42, 609, p3_title, font='F2', size=8.0, r=0.7, g=0.25, b=0.05)
    pdf.draw_text(42, 598, p3_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    pdf.draw_text(42, 587, p3_btn, font='F2', size=7.8, r=0.02, g=0.45, b=0.75)

    # Seccion 2: Prompt Maestro para el Ojo Humano 3D
    pdf.set_fill_color(0.97, 0.99, 1.0)
    pdf.set_stroke_color(0.15, 0.5, 0.85)
    pdf.set_line_width(1.0)
    pdf.rect(30, 360, 552, 205, fill=True, stroke=True)

    pdf.draw_text(42, 548, 'PROMPT MAESTRO PARA GENERAR EL SIMULADOR DEL OJO HUMANO 3D:', font='F2', size=9.2, r=0.05, g=0.35, b=0.65)
    pdf.draw_text(42, 535, '(Selecciona y copia todo el texto azul para pegarlo en gemini.google.com)', font='F3', size=7.4, r=0.4, g=0.45, b=0.55)

    # Recuadro interior del prompt
    pdf.set_fill_color(0.92, 0.96, 1.0)
    pdf.set_stroke_color(0.2, 0.55, 0.85)
    pdf.set_line_width(0.8)
    pdf.rect(40, 370, 532, 155, fill=True, stroke=True)

    prompt_lines = [
        "\"Actua como un experto en oftalmologia, anatomia humana y programacion 3D con Three.js.",
        "Crea una aplicacion interactiva en un unico archivo HTML autocontenido que represente el Globo Ocular Humano en 3D:",
        "1. Modelo 3D con orbita 360 grados: Esclera blanca con vasos sanguineos, cornea transparente e iris realista con textura radial.",
        "2. Simulador de Reflejo Pupilar (Luz): Control deslizante de iluminacion que dilate la pupila en penumbra (midriasis, 7-8 mm)",
        "   y la contraiga ante un haz de linterna medica (miosis intensa, 2 mm), mostrando la medida milimetrica en pantalla.",
        "3. Corte Anatomico Sagital: Boton interactivo para seccionar el ojo y explorar el interior: Cristalino (lente biconvexa de enfoque),",
        "   humor vitreo transparente, retina posterior fotosensible y canal de salida del Nervio Optico hacia el cerebro.",
        "4. Enfoque y Presbicia: Selector para simular la vista cansada y la acomodacion del cristalino al enfocar objetos de cerca y lejos.",
        "5. Ergonomia Senior (+60): Botones grandes de facil lectura, fondo oscuro de alto contraste y textos medicos explicativos en espanol.",
        "Genera el codigo HTML completo con Three.js y OrbitControls via CDN, listo para ejecutar directamente en el navegador.\""
    ]
    y_pr = 512
    for pl in prompt_lines:
        is_bold = pl.startswith('"Actua') or pl.startswith('Genera') or pl.startswith('1.') or pl.startswith('2.') or pl.startswith('3.') or pl.startswith('4.') or pl.startswith('5.')
        pdf.draw_text(48, y_pr, pl, font='F2' if is_bold else 'F1', size=7.5, r=0.05, g=0.22, b=0.45)
        y_pr -= 13.5

    # Seccion 3: Dialogo y Preguntas de Reflexion con Gemini en el Aula
    pdf.set_fill_color(0.96, 0.99, 0.97)
    pdf.set_stroke_color(0.1, 0.65, 0.4)
    pdf.set_line_width(1.0)
    pdf.rect(30, 235, 552, 115, fill=True, stroke=True)

    pdf.draw_text(42, 335, 'PREGUNTAS DE REFLEXION Y DIALOGO CON GEMINI EN EL AULA:', font='F2', size=8.8, r=0.05, g=0.5, b=0.3)

    q1 = "Pregunta 1 • Reflejo Pupilar Fotomotor: \"Gemini, en el simulador veo como la pupila se contrae con la linterna. ¿Como coordinan los musculos esfinter y dilatador del iris este reflejo y por que los medicos iluminan el ojo tras un golpe en la cabeza?\""
    q1_lines = wrap_text(q1, 114)
    pdf.draw_text(42, 318, q1_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 307, q1_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q2 = "Pregunta 2 • El Cristalino y la Vista Cansada: \"Gemini, ¿por que el cristalino pierde flexibilidad a partir de los 45-50 anos impidiendo acomodar de cerca (presbicia) y por que una lente convergente (gafas de cerca) soluciona este problema optico?\""
    q2_lines = wrap_text(q2, 114)
    pdf.draw_text(42, 290, q2_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 279, q2_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q3 = "Pregunta 3 • Retina y Nervio Optico: \"Gemini, ¿cual es la diferencia funcional entre los bastones (vision periferica y con poca luz) y los conos (vision central y en color en la macula), y como viaja la senal electrica al lobulo occipital del cerebro?\""
    q3_lines = wrap_text(q3, 114)
    pdf.draw_text(42, 262, q3_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 251, q3_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    # Seccion 4: Procedencia Cientifica Oficial & Triple Salvaguarda
    pdf.set_fill_color(0.98, 0.98, 0.99)
    pdf.set_stroke_color(0.5, 0.5, 0.6)
    pdf.set_line_width(0.8)
    pdf.rect(30, 115, 552, 110, fill=True, stroke=True)

    pdf.draw_text(42, 212, 'PROCEDENCIA CIENTIFICA OFICIAL Y METODOLOGIA DIDACTICA GARANTIZADA:', font='F2', size=8.5, r=0.2, g=0.25, b=0.35)
    fuente1 = "- Fuentes Anatomicas Acreditadas: Modelos opticos basados en los parametros biometricos del Ojo de Gullstrand, el National Institutes of Health (NIH) y publicaciones de divulgacion de la Academia Americana de Oftalmologia (AAO)."
    f1_lines = wrap_text(fuente1, 114)
    pdf.draw_text(42, 197, f1_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f1_lines) > 1:
        pdf.draw_text(42, 186, f1_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente2 = "- Triple Salvaguarda Pedagogica: El alumno experimenta primero la programacion asistida con Gemini y dispone simultaneamente del boton de respaldo oficial (BKP) para asegurar que el 100% de los asistentes disfrute de la experiencia 3D completa."
    f2_lines = wrap_text(fuente2, 114)
    pdf.draw_text(42, 170, f2_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f2_lines) > 1:
        pdf.draw_text(42, 159, f2_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente3 = "- Adaptacion Senior (+60): Sin instalaciones complejas, sin comandos de consola y sin configuraciones. Todo se ejecuta de forma natural dentro del navegador en gemini.google.com y el Cuadro de Mando del aula."
    f3_lines = wrap_text(fuente3, 114)
    pdf.draw_text(42, 143, f3_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f3_lines) > 1:
        pdf.draw_text(42, 132, f3_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    # Banner inferior BKP
    pdf.set_fill_color(0.04, 0.1, 0.2)
    pdf.set_stroke_color(0.2, 0.75, 1.0)
    pdf.set_line_width(1.2)
    pdf.rect(30, 45, 552, 60, fill=True, stroke=True)

    pdf.draw_text(42, 88, 'COPIA DE RESPALDO OFICIAL (BKP): SIMULADOR_OJO_HUMANO_3D.HTML', font='F2', size=9.0, r=0.4, g=0.85, b=1.0)
    pdf.draw_text(42, 73, 'Si por alguna razon tecnica el codigo no se visualiza en tu pantalla de Gemini, pulsa en el Cuadro de Mando del curso:', font='F1', size=7.8, r=0.8, g=0.85, b=0.9)
    pdf.draw_text(42, 58, '«👁️ Ver Simulador Ojo Humano 3D (BKP)» para abrir al instante el modelo 3D anatomico garantizado con Three.js.', font='F2', size=8.0, r=0.4, g=0.85, b=1.0)

    pdf.end_page()

    pdf.write_to_file(output_path)
    try:
        os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
        shutil.copy2(output_path, LOCAL_BACKUP)
    except Exception:
        pass

    print(f"✅ PDF COD-004 generado con éxito en: {output_path}")
    return output_path

if __name__ == '__main__':
    try:
        build_cod_004_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-004: {e}")
        sys.exit(1)
