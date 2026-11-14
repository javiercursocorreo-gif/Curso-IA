#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_niv_001.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter):
9. NIV-001_Los_5_Escalones_de_la_Tranquilidad_en_la.pdf
para la Sesión 01 del Curso de IA.

Nuevo estándar de visualización directa:
- Cero código intermedio para el alumno senior.
- Generación y ejecución directa en pantalla (Canvas / Vista previa).
- Copia de respaldo (BKP) oficial garantizada con SIMULADOR_TRANQUILIDAD_JUBILACION.html.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "9. NIV-001_Los_5_Escalones_de_la_Tranquilidad_en_la.pdf")

ALT_PATHS = [
    "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/09. [NIV] BLOQUE_9_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20/NIV-001_Los 5 Escalones de la Tranquilidad en la Jubilación.pdf",
    "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/[NIV] BLOQUE_10_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20/NIV-001_Los_5_Escalones_de_la_Tranquilidad_en_la.pdf"
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

def build_niv_001_pdf(output_path=PDF_PATH):
    pdf = NativePDFWriter(612.0, 792.0)
    pdf.start_page()

    # Marco exterior esmeralda y oro
    pdf.set_fill_color(0.99, 0.995, 0.99)
    pdf.set_stroke_color(0.05, 0.55, 0.35)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal
    pdf.set_fill_color(0.04, 0.22, 0.14)
    pdf.rect(24, 716, 564, 52, fill=True, stroke=False)

    pdf.draw_text(36, 750, 'SESION 01 • MICRO-APLICACION DE VIDA REAL (+65) [NIV-001]', font='F2', size=8.5, r=0.4, g=0.9, b=0.6)
    pdf.draw_text(36, 730, 'Los 5 Escalones de la Tranquilidad en la Jubilacion (+65)', font='F2', size=13.0, r=1, g=1, b=1)

    # Seccion 1: Metodologia Directa en 2 Pasos
    pdf.set_fill_color(0.94, 0.985, 0.95)
    pdf.set_stroke_color(0.1, 0.65, 0.4)
    pdf.set_line_width(1.0)
    pdf.rect(30, 580, 552, 126, fill=True, stroke=True)

    pdf.draw_text(42, 692, 'METODOLOGIA DIRECTA: GENERACION Y VISUALIZACION EN PANTALLA SIN CODIGO', font='F2', size=9.2, r=0.05, g=0.4, b=0.2)

    p1_title = 'PASO 1 • Copiar el Prompt Maestro en Gemini (gemini.google.com):'
    p1_desc = 'Pega el texto del recuadro inferior en Gemini. El prompt esta calibrado para que Gemini abra y ejecute directamente la calculadora interactiva en pantalla (Canvas / Vista previa) en pleno funcionamiento, sin pedirte pasos de codigo.'
    p1_lines = wrap_text(p1_desc, 114)
    pdf.draw_text(42, 676, p1_title, font='F2', size=8.0, r=0.05, g=0.5, b=0.3)
    pdf.draw_text(42, 665, p1_lines[0], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    if len(p1_lines) > 1:
        pdf.draw_text(42, 655, p1_lines[1], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p2_title = 'PASO 2 • Experimentar y Dialogar con Gemini en el Aula:'
    p2_desc = 'Mueve los controles de pension mensual, gastos fijos y ahorros guardados para comprobar tu nivel de solvencia vitalicia, y plantea a Gemini las 3 preguntas clave sobre tranquilidad patrimonial.'
    pdf.draw_text(42, 638, p2_title, font='F2', size=8.0, r=0.05, g=0.5, b=0.3)
    pdf.draw_text(42, 627, p2_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p3_title = 'GARANTIA OFICIAL • Copia de Respaldo Oficial Garantizada (BKP en el Mapa):'
    p3_desc = 'Si por saturacion o corte de red la IA no visualiza el modelo interactivo, pulsa en el Cuadro de Mando del curso:'
    p3_btn = '«🛡️ Abrir Calculadora Tranquilidad Jubilacion (+65) (HTML)» para interactuar de inmediato con tus datos reales.'
    pdf.draw_text(42, 610, p3_title, font='F2', size=8.0, r=0.7, g=0.3, b=0.05)
    pdf.draw_text(42, 599, p3_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    pdf.draw_text(42, 588, p3_btn, font='F2', size=7.8, r=0.05, g=0.5, b=0.3)

    # Seccion 2: Prompt Maestro para Gemini
    pdf.set_fill_color(0.96, 0.99, 0.97)
    pdf.set_stroke_color(0.15, 0.6, 0.35)
    pdf.set_line_width(1.0)
    pdf.rect(30, 360, 552, 210, fill=True, stroke=True)

    pdf.draw_text(42, 555, 'PROMPT MAESTRO PARA CREAR LA CALCULADORA DE TRANQUILIDAD EN LA JUBILACION:', font='F2', size=9.0, r=0.05, g=0.4, b=0.25)
    pdf.draw_text(42, 542, '(Selecciona y copia todo el bloque de texto para pegarlo en gemini.google.com)', font='F3', size=7.4, r=0.4, g=0.45, b=0.5)

    # Recuadro interior del prompt
    pdf.set_fill_color(0.91, 0.97, 0.93)
    pdf.set_stroke_color(0.18, 0.65, 0.4)
    pdf.set_line_width(0.8)
    pdf.rect(40, 370, 532, 160, fill=True, stroke=True)

    prompt_lines = [
        "\"Actua como un orientador financiero familiar y pedagogo para adultos mayores (+65).",
        "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) una calculadora visual interactiva:",
        "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
        "1. Controles deslizantes (Sliders): Pension mensual neta (0 a 3.500 €/mes), Gastos fijos del hogar (0 a 3.000 €/mes),",
        "   Ahorros bancarios de seguridad (0 a 200.000 €) y Vivienda en propiedad (Si/No).",
        "2. Diagnostico de los 5 Escalones: 1. Ajuste necesario, 2. Respiro mensual, 3. Colchon de seguridad, 4. Disfrutar de la jubilacion, 5. Paz total.",
        "3. Regla Vitalicia: Si la pension mensual cubre los gastos del hogar, los ahorros no se tocan jamas ('Solvencia Vitalicia Garantizada').",
        "4. Ergonomia Senior: Selector de letra grande, alto contraste, explicaciones sin anglicismos financieros y boton de reinicio.\""
    ]
    y_pr = 516
    for pl in prompt_lines:
        is_bold = pl.startswith('"Actua') or pl.startswith('Muestra') or pl.startswith('1.') or pl.startswith('2.') or pl.startswith('3.') or pl.startswith('4.')
        pdf.draw_text(48, y_pr, pl, font='F2' if is_bold else 'F1', size=7.3, r=0.05, g=0.25, b=0.15)
        y_pr -= 12.0

    # Seccion 3: Dialogo y Preguntas de Reflexion con Gemini en el Aula
    pdf.set_fill_color(0.99, 0.98, 0.96)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 225, 552, 122, fill=True, stroke=True)

    pdf.draw_text(42, 332, 'PREGUNTAS DE DIALOGO CON GEMINI EN EL AULA (EDUCACION PATRIMONIAL SENIOR):', font='F2', size=8.8, r=0.7, g=0.35, b=0.05)

    q1 = "Pregunta 1 • El Colchon de Emergencia: \"Gemini, en el simulador veo que si mi pension cubre mis gastos no necesito tocar mis ahorros. ¿Cuantos meses de gastos deberia tener en una cuenta a la vista para imprevistos domesticos?\""
    q1_lines = wrap_text(q1, 114)
    pdf.draw_text(42, 316, q1_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 305, q1_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q2 = "Pregunta 2 • El IPC y la Revalorizacion de Pensiones: \"Gemini, si el coste de la vida sube, ¿como protege el sistema publico espanol la capacidad de compra de las pensiones contributivas ano a ano?\""
    q2_lines = wrap_text(q2, 114)
    pdf.draw_text(42, 288, q2_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 277, q2_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q3 = "Pregunta 3 • La Vivienda en Propiedad: \"Gemini, ¿por que tener la vivienda pagada representa el mayor factor de proteccion economica y tranquilidad emocional para una persona jubilada en Espana?\""
    q3_lines = wrap_text(q3, 114)
    pdf.draw_text(42, 260, q3_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 249, q3_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    # Seccion 4: Triple Salvaguarda & Garantia Pedagogica
    pdf.set_fill_color(0.98, 0.98, 0.99)
    pdf.set_stroke_color(0.5, 0.5, 0.6)
    pdf.set_line_width(0.8)
    pdf.rect(30, 108, 552, 105, fill=True, stroke=True)

    pdf.draw_text(42, 198, 'LA TRIPLE SALVAGUARDA PEDAGOGICA Y ACCESIBILIDAD SENIOR (+65):', font='F2', size=8.5, r=0.2, g=0.25, b=0.35)
    fuente1 = "- Rigor Economico y Social: Basado en las pautas de educacion financiera del Banco de Espana y la Comision Nacional del Mercado de Valores (CNMV) para la planificacion del retiro activo."
    f1_lines = wrap_text(fuente1, 114)
    pdf.draw_text(42, 184, f1_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f1_lines) > 1:
        pdf.draw_text(42, 173, f1_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente2 = "- Diseno Ergonomico sin Barreras: Letra amplia, botones de alto contraste, lectura adaptada y compatibilidad total con pantallas de aula, iPad y ordenadores portatiles."
    f2_lines = wrap_text(fuente2, 114)
    pdf.draw_text(42, 158, f2_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f2_lines) > 1:
        pdf.draw_text(42, 147, f2_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente3 = "- Garantia de Respaldo Tecnico: El alumno experimenta el prompt en Gemini sabiendo que dispone del simulador oficial garantizado en el Cuadro de Mando del curso para asegurar el 100% de exito pedagogico."
    f3_lines = wrap_text(fuente3, 114)
    pdf.draw_text(42, 132, f3_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f3_lines) > 1:
        pdf.draw_text(42, 121, f3_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    # Banner inferior BKP
    pdf.set_fill_color(0.04, 0.18, 0.1)
    pdf.set_stroke_color(0.2, 0.8, 0.5)
    pdf.set_line_width(1.2)
    pdf.rect(30, 42, 552, 54, fill=True, stroke=True)

    pdf.draw_text(42, 80, 'APLICACION OFICIAL GARANTIZADA (BKP): SIMULADOR_TRANQUILIDAD_JUBILACION.HTML', font='F2', size=8.8, r=0.2, g=0.85, b=0.5)
    pdf.draw_text(42, 65, 'Si deseas abrir la aplicacion terminada y depurada, en el Cuadro de Mando de la Sesion 01 haz clic en:', font='F1', size=7.6, r=0.8, g=0.85, b=0.9)
    pdf.draw_text(42, 52, '«🛡️ Abrir Calculadora Tranquilidad Jubilacion (+65) (HTML)» para interactuar al instante con datos reales.', font='F2', size=7.8, r=0.2, g=0.85, b=0.5)

    pdf.end_page()

    pdf.write_to_file(output_path)
    for alt in ALT_PATHS:
        try:
            os.makedirs(os.path.dirname(alt), exist_ok=True)
            shutil.copy2(output_path, alt)
        except Exception:
            pass

    print(f"✅ PDF NIV-001 generado con éxito en: {output_path}")
    return output_path

if __name__ == '__main__':
    try:
        build_niv_001_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF NIV-001: {e}")
        sys.exit(1)
