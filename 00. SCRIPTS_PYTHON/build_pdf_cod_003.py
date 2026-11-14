#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_003.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-003_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 03 del Curso de IA.

Contenido simplificado y desatendido:
- Generación y ejecución directa de código en el chat de Gemini.
- Cero visores externos ni talleres manuales.
- Copia de respaldo (BKP) oficial garantizada con SIMULADOR_POMPEYA_3D.html.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/03_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-003_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/03_COD-003_Taller_Simulador_Pompeya_HD.pdf"

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

def build_cod_003_pdf(output_path=PDF_PATH):
    pdf = NativePDFWriter(page_width=612.0, page_height=792.0)
    pdf.start_page()

    # Cabecera Oficial
    pdf.set_fill_color(0.97, 0.98, 1.0)
    pdf.set_stroke_color(0.85, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 746, 552, 28, fill=True, stroke=True)
    pdf.draw_text(42, 755, 'CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGIA PARA ADULTOS MAYORES (60+)', font='F2', size=8.5, r=0.7, g=0.35, b=0.05)
    pdf.draw_text(410, 755, 'SESION 03 • GUIA DE AULA', font='F2', size=8.0, r=0.2, g=0.3, b=0.4)

    # Subtitulo y Titulo
    pdf.draw_text(30, 730, 'BLOQUE IV: CIENCIA Y RECONSTRUCCION CON GEMINI • ARQUEOLOGIA DIGITAL [COD]', font='F2', size=8.8, r=0.75, g=0.38, b=0.05)
    pdf.draw_text(30, 712, '[COD-003] Reconstruccion Arqueologica de Pompeya con Gemini (Ano 79 d.C.)', font='F2', size=13.0, r=0.06, g=0.09, b=0.16)

    # Linea divisoria
    pdf.set_stroke_color(0.85, 0.5, 0.1)
    pdf.set_line_width(1.5)
    pdf.line(30, 703, 582, 703)

    # Seccion 1: Mision Didactica
    pdf.draw_text(30, 689, 'MISION DIDACTICA: ARQUEOLOGIA VISUAL DIRECTA EN PANTALLA (CERO CODIGO)', font='F2', size=9.2, r=0.1, g=0.2, b=0.45)
    intro_p1 = "En esta sesion pediras a Gemini que abra y muestre directamente en pantalla una reconstruccion arqueologica interactiva de Pompeya en el ano 79 d.C., comparandola con sus ruinas actuales desenterradas tras el Vesubio. Sin pantallas de codigo fuente ni instalaciones: Gemini despliega la experiencia visual interactiva directamente en tu pantalla de chat lista para explorar."
    intro_lines = wrap_text(intro_p1, 120)
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

    paso1 = "Paso 1 • Copiar el Prompt en Gemini (gemini.google.com): Pega el texto del recuadro inferior en Gemini. El prompt esta calibrado para que Gemini abra y ejecute directamente el visor interactivo en pantalla (Canvas / Vista previa) en pleno funcionamiento, sin pedirte pasos de codigo."
    p1_lines = wrap_text(paso1, 114)
    pdf.draw_text(42, 608, p1_lines[0], font='F2', size=8.0, r=0.1, g=0.2, b=0.3)
    pdf.draw_text(42, 596, p1_lines[1], font='F1', size=7.7, r=0.2, g=0.25, b=0.3)

    paso2 = "Paso 2 • Experimentar y Dialogar con Gemini en el Aula: Mueve el deslizador antes/despues entre las ruinas y la reconstruccion de la Domus romana. A continuacion, escribe en el chat de Gemini las preguntas de reflexion historica propuestas abajo para dialogar con la IA."
    p2_lines = wrap_text(paso2, 114)
    pdf.draw_text(42, 574, p2_lines[0], font='F2', size=8.0, r=0.05, g=0.5, b=0.2)
    pdf.draw_text(42, 562, p2_lines[1], font='F1', size=7.7, r=0.2, g=0.25, b=0.3)

    paso3 = "Garantia Oficial • Copia de Respaldo Garantizada (BKP en el Mapa): Si por saturacion o corte de red la IA no visualiza el modelo interactivo, pulsa en el Cuadro de Mando del curso «🏛️ Ver Tesoro Arqueologico 3D (BKP)» para abrir al instante la version arqueologica oficial garantizada."
    p3_lines = wrap_text(paso3, 114)
    pdf.draw_text(42, 540, p3_lines[0], font='F2', size=8.0, r=0.8, g=0.4, b=0.05)
    pdf.draw_text(42, 528, p3_lines[1], font='F1', size=7.7, r=0.2, g=0.25, b=0.3)
    if len(p3_lines) > 2:
        pdf.draw_text(42, 516, p3_lines[2], font='F1', size=7.7, r=0.2, g=0.25, b=0.3)

    pdf.draw_text(42, 496, 'Resultado esperado: Comparacion visual interactiva directa en pantalla sin tocar una sola linea de programacion.', font='F3', size=7.5, r=0.35, g=0.4, b=0.45)

    # Seccion 3: Prompt Maestro para Copiar y Pegar en Gemini
    pdf.set_fill_color(0.97, 0.98, 0.99)
    pdf.set_stroke_color(0.7, 0.4, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 362, 552, 110, fill=True, stroke=True)

    pdf.draw_text(42, 458, 'PROMPT MAESTRO PARA COPIAR Y PEGAR EN GEMINI (VISUALIZACION DIRECTA):', font='F2', size=8.8, r=0.7, g=0.35, b=0.05)

    prompt_lines = [
        "\"Actua como un arqueologo digital y experto en el Imperio Romano.",
        "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un visor comparativo de Pompeya:",
        "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
        "1. Muestra una vista comparativa con deslizador central (antes / despues) entre las ruinas excavadas y la Domus romana restaurada.",
        "2. Incluye explicaciones didacticas de los elementos arquitectonicos: el impluvium, el peristilo porticado y los frescos policromados.",
        "3. Interfaz senior (+60): Diseno amplio, textos en espanol y presentacion directa en pantalla lista para explorar en el chat.\""
        "3. Deja el codigo listo para ejecutar en pantalla con un solo clic.\""
    ]
    y_pr = 442
    for pl in prompt_lines:
        pdf.draw_text(48, y_pr, pl, font='F2' if pl.startswith('"Genera') or pl.startswith('Requisitos') else 'F1', size=7.6, r=0.1, g=0.2, b=0.35)
        y_pr -= 13

    # Seccion 4: Dialogo y Preguntas de Reflexion con Gemini en el Aula
    pdf.set_fill_color(0.96, 0.99, 0.97)
    pdf.set_stroke_color(0.1, 0.65, 0.4)
    pdf.set_line_width(1.0)
    pdf.rect(30, 240, 552, 112, fill=True, stroke=True)

    pdf.draw_text(42, 338, 'PREGUNTAS DE REFLEXION Y DIALOGO CON GEMINI EN EL AULA:', font='F2', size=8.8, r=0.05, g=0.5, b=0.3)

    q1 = "Pregunta 1 • La Vida en la Domus: \"Gemini, observando la reconstruccion de la casa pompeyana, explicame como era un dia normal de una familia romana acomodada, el papel de los esclavos y que comian en el triclinio.\""
    q1_lines = wrap_text(q1, 114)
    pdf.draw_text(42, 320, q1_lines[0], font='F2', size=7.6, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 308, q1_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    q2 = "Pregunta 2 • El Impluvium y el Agua: \"Gemini, ¿por que el techo del atrio tenia una apertura central (compluvium) y como canalizaban el agua de lluvia hacia la cisterna subterranea para el consumo del hogar?\""
    q2_lines = wrap_text(q2, 114)
    pdf.draw_text(42, 290, q2_lines[0], font='F2', size=7.6, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 278, q2_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    q3 = "Pregunta 3 • La Erupcion del Vesubio: \"Gemini, ¿por que la ceniza volcanica y el material piroclastico sellaron los frescos con colores tan vivos durante 1.700 anos en vez de destruirlos por completo?\""
    q3_lines = wrap_text(q3, 114)
    pdf.draw_text(42, 260, q3_lines[0], font='F2', size=7.6, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 248, q3_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    # Seccion 5: Procedencia Cientifica Oficial & Triple Salvaguarda
    pdf.set_fill_color(0.98, 0.98, 0.99)
    pdf.set_stroke_color(0.5, 0.5, 0.6)
    pdf.set_line_width(0.8)
    pdf.rect(30, 115, 552, 115, fill=True, stroke=True)

    pdf.draw_text(42, 216, 'PROCEDENCIA CIENTIFICA OFICIAL Y METODOLOGIA DIDACTICA GARANTIZADA:', font='F2', size=8.5, r=0.2, g=0.25, b=0.35)
    fuente1 = "- Fuentes Arqueologicas Acreditadas: Ortofotografias de alta definicion y levantamientos fotogrametricos oficiales del Parco Archeologico di Pompei (Ministero della Cultura de Italia) y proyectos de digitalizacion patrimonial de la UNESCO."
    f1_lines = wrap_text(fuente1, 114)
    pdf.draw_text(42, 200, f1_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f1_lines) > 1:
        pdf.draw_text(42, 189, f1_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente2 = "- Triple Salvaguarda Pedagogica: El alumno experimenta primero la creacion guiada con Gemini y, simultaneamente, dispone del boton oficial de respaldo (BKP) para que el 100% de la clase complete la experiencia con exito absoluto."
    f2_lines = wrap_text(fuente2, 114)
    pdf.draw_text(42, 172, f2_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f2_lines) > 1:
        pdf.draw_text(42, 161, f2_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente3 = "- Adaptacion Senior (+60): Sin instalaciones, sin comandos de terminal y sin descargas de software ajeno. Todo funciona a traves de la interfaz limpia del navegador en gemini.google.com y el Cuadro de Mando del aula."
    f3_lines = wrap_text(fuente3, 114)
    pdf.draw_text(42, 144, f3_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f3_lines) > 1:
        pdf.draw_text(42, 133, f3_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    # Banner inferior BKP
    pdf.set_fill_color(0.06, 0.09, 0.16)
    pdf.set_stroke_color(0.9, 0.6, 0.1)
    pdf.set_line_width(1.2)
    pdf.rect(30, 45, 552, 60, fill=True, stroke=True)

    pdf.draw_text(42, 88, 'COPIA DE RESPALDO OFICIAL (BKP): SIMULADOR_POMPEYA_3D.HTML', font='F2', size=9.0, r=0.98, g=0.75, b=0.2)
    pdf.draw_text(42, 73, 'Si por alguna razon tecnica el codigo no se visualiza en tu pantalla de Gemini, pulsa en el Cuadro de Mando del curso:', font='F1', size=7.8, r=0.8, g=0.85, b=0.9)
    pdf.draw_text(42, 58, '«🏛️ Ver Tesoro Arqueologico 3D (BKP)» para abrir al instante la reconstruccion arqueologica HD garantizada.', font='F2', size=8.0, r=0.98, g=0.75, b=0.2)

    pdf.end_page()

    pdf.write_to_file(output_path)
    try:
        os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
        shutil.copy2(output_path, LOCAL_BACKUP)
    except Exception:
        pass

    print(f"✅ PDF COD-003 generado con éxito en: {output_path}")
    return output_path

if __name__ == '__main__':
    try:
        build_cod_003_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-003: {e}")
        sys.exit(1)
