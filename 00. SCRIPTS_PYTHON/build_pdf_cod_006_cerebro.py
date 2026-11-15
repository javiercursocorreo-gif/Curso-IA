#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_006_cerebro.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-006_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 06 del Curso de IA.

Nuevo estándar de visualización directa:
- Cero código intermedio para el alumno senior.
- Generación y ejecución directa en pantalla (Canvas / Vista previa).
- Copia de respaldo (BKP) oficial garantizada con SIMULADOR_CEREBRO_3D.html.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/06_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-006_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
ALT_PATH_6 = os.path.join(OUTPUT_DIR, "6. COD-006_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/06_COD-006_Taller_Simulador_Cerebro_3D.pdf"

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

def build_cod_006_pdf(output_path=PDF_PATH):
    pdf = NativePDFWriter(612.0, 792.0)
    pdf.start_page()

    # Marco exterior elegante azul violeta
    pdf.set_fill_color(0.985, 0.985, 1.0)
    pdf.set_stroke_color(0.48, 0.22, 0.85)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal
    pdf.set_fill_color(0.18, 0.08, 0.38)
    pdf.rect(24, 716, 564, 52, fill=True, stroke=False)

    pdf.draw_text(36, 750, 'SESION 06 • FICHA DIDACTICA DE CREACION CON GEMINI [COD-006]', font='F2', size=8.5, r=0.75, g=0.55, b=1.0)
    pdf.draw_text(36, 730, 'Simulador 3D del Cerebro Humano y Red Sinaptica con Gemini', font='F2', size=13.0, r=1, g=1, b=1)

    # Seccion 1: Metodologia Directa en 2 Pasos
    pdf.set_fill_color(0.95, 0.93, 1.0)
    pdf.set_stroke_color(0.5, 0.25, 0.9)
    pdf.set_line_width(1.0)
    pdf.rect(30, 580, 552, 125, fill=True, stroke=True)

    pdf.draw_text(42, 692, 'METODOLOGIA DIRECTA: GENERACION Y VISUALIZACION EN PANTALLA SIN CODIGO', font='F2', size=9.2, r=0.25, g=0.1, b=0.55)

    p1_title = 'PASO 1 • Copiar el Prompt en Gemini (gemini.google.com):'
    p1_desc = 'Pega el texto del recuadro inferior en Gemini. El prompt esta calibrado para que Gemini abra y ejecute directamente el simulador interactivo en pantalla (Canvas / Vista previa) en pleno funcionamiento, sin pedirte pasos de codigo.'
    p1_lines = wrap_text(p1_desc, 114)
    pdf.draw_text(42, 676, p1_title, font='F2', size=8.0, r=0.35, g=0.15, b=0.7)
    pdf.draw_text(42, 665, p1_lines[0], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    if len(p1_lines) > 1:
        pdf.draw_text(42, 655, p1_lines[1], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p2_title = 'PASO 2 • Experimentar y Dialogar con Gemini en el Aula:'
    p2_desc = 'Rota los lobulos cerebrales, activa los destellos de transmision sinaptica y plantea a Gemini las preguntas sobre memoria y plasticidad cerebral que tienes abajo para profundizar en el aula.'
    pdf.draw_text(42, 638, p2_title, font='F2', size=8.0, r=0.35, g=0.15, b=0.7)
    pdf.draw_text(42, 627, p2_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p3_title = 'GARANTIA OFICIAL • Copia de Respaldo Garantizada (BKP Oficial en el Mapa):'
    p3_desc = 'Si por saturacion o corte de red la IA no visualiza el modelo interactivo, pulsa en el Cuadro de Mando del curso:'
    p3_btn = '«🧠 Ver Simulador Cerebro 3D (BKP)» para abrir al instante la maqueta neurologica garantizada.'
    pdf.draw_text(42, 610, p3_title, font='F2', size=8.0, r=0.8, g=0.3, b=0.1)
    pdf.draw_text(42, 599, p3_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    pdf.draw_text(42, 588, p3_btn, font='F2', size=7.8, r=0.4, g=0.15, b=0.75)

    # Seccion 2: Prompt Maestro para Gemini
    pdf.set_fill_color(0.97, 0.95, 1.0)
    pdf.set_stroke_color(0.48, 0.22, 0.85)
    pdf.set_line_width(1.0)
    pdf.rect(30, 360, 552, 210, fill=True, stroke=True)

    pdf.draw_text(42, 555, 'PROMPT MAESTRO PARA CREAR EL SIMULADOR 3D DEL CEREBRO HUMANO:', font='F2', size=9.0, r=0.25, g=0.1, b=0.55)
    pdf.draw_text(42, 542, '(Selecciona y copia todo el bloque de texto para pegarlo en gemini.google.com)', font='F3', size=7.4, r=0.4, g=0.45, b=0.5)

    # Recuadro interior del prompt
    pdf.set_fill_color(0.93, 0.90, 0.99)
    pdf.set_stroke_color(0.55, 0.3, 0.9)
    pdf.set_line_width(0.8)
    pdf.rect(40, 370, 532, 160, fill=True, stroke=True)

    prompt_lines = [
        "\"Actua como un programador senior y especialista en neuroanatomia y divulgacion cientifica.",
        "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador 3D sobre el Cerebro Humano:",
        "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
        "1. Escena 3D interactiva en Three.js con un modelo hiperrealista del cerebro humano y sus 4 lobulos diferenciados.",
        "2. Red sinaptica animada: particulas luminosas que simulan impulsos electricos recorriendo los circuitos neuronales.",
        "3. Controles tactiles y raton: rotacion 360 grados, zoom suave y selector de lobulos (Frontal, Parietal, Temporal, Occipital).",
        "4. Panel informativo flotante a la derecha (HUD) con la funcion cognitiva de cada area (memoria, lenguaje, vision, motricidad).",
        "5. Boton de actividad: alternar entre modo 'Reposo', 'Aprendizaje activo' y 'Descanso profundo'.",
        "Estetica cientifica impecable sobre fondo oscuro OLED, iluminacion cinematofradica y tipografia clara adaptada a seniors.\""
    ]
    y_pr = 516
    for pl in prompt_lines:
        is_bold = pl.startswith('"Actua') or pl.startswith('Requisitos') or pl.startswith('1.') or pl.startswith('2.') or pl.startswith('3.') or pl.startswith('4.') or pl.startswith('5.') or pl.startswith('Estetica')
        pdf.draw_text(48, y_pr, pl, font='F2' if is_bold else 'F1', size=7.2, r=0.15, g=0.08, b=0.3)
        y_pr -= 13.0

    # Seccion 3: Dialogo y Preguntas de Reflexion con Gemini en el Aula
    pdf.set_fill_color(0.99, 0.98, 0.96)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 225, 552, 122, fill=True, stroke=True)

    pdf.draw_text(42, 332, 'PREGUNTAS DE DIALOGO CON GEMINI EN EL AULA (NEUROCIENCIA Y SABIDURIA SENIOR):', font='F2', size=8.8, r=0.7, g=0.35, b=0.05)

    q1 = "Pregunta 1 • La Plasticidad Cerebral en Adultos Mayores (+65): \"Gemini, ¿por que la neurociencia moderna ha demostrado que el cerebro sigue creando nuevas conexiones y neuronas a cualquier edad cuando aprendemos tecnologia o un nuevo idioma?\""
    q1_lines = wrap_text(q1, 114)
    pdf.draw_text(42, 316, q1_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 305, q1_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q2 = "Pregunta 2 • El Hipocampo y los Recuerdos a Largo Plazo: \"Gemini, ¿que ocurre en el hipocampo y los lobulos temporales para que podamos recordar con tanta nitidez momentos de nuestra infancia y que habitos diarios protegen esa reserva cognitiva?\""
    q2_lines = wrap_text(q2, 114)
    pdf.draw_text(42, 288, q2_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 277, q2_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q3 = "Pregunta 3 • La 'Gimnasia Cerebral' de Manejar la IA: \"Gemini, ¿como estimula a nuestro cerebro formular prompts estructurados, pensar preguntas logicas y explorar simuladores visuales en comparacion con el consumo pasivo de television?\""
    q3_lines = wrap_text(q3, 114)
    pdf.draw_text(42, 260, q3_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 249, q3_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 212, 582, 212)
    pdf.draw_text(36, 198, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 06 • CIENCIA INTERACTIVA 3D [COD]', font='F2', size=7.2, r=0.3, g=0.2, b=0.5)
    pdf.draw_text(36, 186, 'Metodologia de Visualizacion Directa (Canvas / Gemini) • Respaldo: SIMULADOR_CEREBRO_3D.html', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ PDF generado exitosamente: {output_path}")

    # Sincronizar copia alternativa 6. COD-006...
    try:
        shutil.copy2(output_path, ALT_PATH_6)
        print(f"📦 Copia sincronizada en: {ALT_PATH_6}")
    except Exception as e:
        print(f"Error copia alt: {e}")

    try:
        os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
        shutil.copy2(output_path, LOCAL_BACKUP)
        print(f"📦 Respaldo sincronizado en: {LOCAL_BACKUP}")
    except Exception as e:
        print(f"Error copia backup: {e}")

if __name__ == '__main__':
    build_cod_006_pdf()
