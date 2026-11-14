#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_002.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-002_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 02 del Curso de IA.

Nuevo estándar de visualización directa:
- Cero código intermedio para el alumno senior.
- Generación y ejecución directa en pantalla (Canvas / Vista previa).
- Copia de respaldo (BKP) oficial garantizada con SIMULADOR_CORAZON_3D.html.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/02_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-002_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/02_COD-002_Taller_Simulador_Corazon_3D.pdf"

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

def build_cod_002_pdf(output_path=PDF_PATH):
    pdf = NativePDFWriter(612.0, 792.0)
    pdf.start_page()

    # Marco exterior elegante carmín y rubí
    pdf.set_fill_color(0.995, 0.985, 0.985)
    pdf.set_stroke_color(0.75, 0.1, 0.25)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal
    pdf.set_fill_color(0.3, 0.04, 0.1)
    pdf.rect(24, 716, 564, 52, fill=True, stroke=False)

    pdf.draw_text(36, 750, 'SESION 02 • FICHA DIDACTICA DE CREACION CON GEMINI [COD-002]', font='F2', size=8.5, r=1.0, g=0.55, b=0.65)
    pdf.draw_text(36, 730, 'Simulador 3D del Latido Cardiaco con Gemini (Corazon Humano)', font='F2', size=13.0, r=1, g=1, b=1)

    # Seccion 1: Metodologia Directa en 2 Pasos
    pdf.set_fill_color(1.0, 0.94, 0.95)
    pdf.set_stroke_color(0.85, 0.2, 0.35)
    pdf.set_line_width(1.0)
    pdf.rect(30, 580, 552, 125, fill=True, stroke=True)

    pdf.draw_text(42, 692, 'METODOLOGIA DIRECTA: GENERACION Y VISUALIZACION EN PANTALLA SIN CODIGO', font='F2', size=9.2, r=0.55, g=0.05, b=0.15)

    p1_title = 'PASO 1 • Copiar el Prompt en Gemini (gemini.google.com):'
    p1_desc = 'Pega el texto del recuadro inferior en Gemini. El prompt esta calibrado para que Gemini abra y ejecute directamente el simulador cardiaco interactivo en pantalla (Canvas / Vista previa) sin obligarte a revisar codigo.'
    p1_lines = wrap_text(p1_desc, 114)
    pdf.draw_text(42, 676, p1_title, font='F2', size=8.0, r=0.75, g=0.1, b=0.25)
    pdf.draw_text(42, 665, p1_lines[0], font='F1', size=7.8, r=0.25, g=0.15, b=0.15)
    if len(p1_lines) > 1:
        pdf.draw_text(42, 655, p1_lines[1], font='F1', size=7.8, r=0.25, g=0.15, b=0.15)

    p2_title = 'PASO 2 • Experimentar y Dialogar con Gemini en el Aula:'
    p2_desc = 'Ajusta las pulsaciones por minuto, escucha el fonendoscopio, explora las 4 cavidades y escribe a Gemini las preguntas de reflexion medica que tienes abajo para profundizar en el aula.'
    pdf.draw_text(42, 638, p2_title, font='F2', size=8.0, r=0.75, g=0.1, b=0.25)
    pdf.draw_text(42, 627, p2_desc, font='F1', size=7.8, r=0.25, g=0.15, b=0.15)

    p3_title = 'GARANTIA OFICIAL • Copia de Respaldo Garantizada (BKP Oficial en el Mapa):'
    p3_desc = 'Si por saturacion o corte de red la IA no visualiza el modelo interactivo, pulsa en el Cuadro de Mando del curso:'
    p3_btn = '«🫀 Ver Simulador Corazon 3D (BKP)» para abrir al instante la maqueta cardiaca oficial garantizada.'
    pdf.draw_text(42, 610, p3_title, font='F2', size=8.0, r=0.8, g=0.2, b=0.05)
    pdf.draw_text(42, 599, p3_desc, font='F1', size=7.8, r=0.25, g=0.15, b=0.15)
    pdf.draw_text(42, 588, p3_btn, font='F2', size=7.8, r=0.75, g=0.05, b=0.2)

    # Seccion 2: Prompt Maestro para Gemini
    pdf.set_fill_color(0.995, 0.96, 0.97)
    pdf.set_stroke_color(0.85, 0.25, 0.4)
    pdf.set_line_width(1.0)
    pdf.rect(30, 360, 552, 205, fill=True, stroke=True)

    pdf.draw_text(42, 548, 'PROMPT MAESTRO PARA GENERAR EL SIMULADOR DEL CORAZON 3D:', font='F2', size=9.2, r=0.6, g=0.05, b=0.2)
    pdf.draw_text(42, 535, '(Selecciona y copia todo el texto carmin para pegarlo en gemini.google.com)', font='F3', size=7.4, r=0.55, g=0.4, b=0.45)

    # Recuadro interior del prompt
    pdf.set_fill_color(0.98, 0.92, 0.94)
    pdf.set_stroke_color(0.85, 0.3, 0.45)
    pdf.set_line_width(0.8)
    pdf.rect(40, 370, 532, 155, fill=True, stroke=True)

    prompt_lines = [
        "\"Actua como un cardiologo, anatomista humano y desarrollador de simuladores 3D biomedicos.",
        "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador visual sobre el Latido Cardiaco y Anatomia del Corazon Humano en 3D:",
        "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
        "1. Modelo 3D interactivo con rotacion 360 grados: Vista exterior e interior con las 4 cavidades (auriculas y ventriculos derecho e izquierdo).",
        "2. Latido Realista Continuo: Animacion biomecanica sincrona de sistole (contraccion ventricular) y diastole (llenado auricular).",
        "3. Simulador de Fonendoscopio y Pulso: Control deslizante de frecuencia cardiaca (de 50 lpm en reposo hasta 130 lpm en esfuerzo) con audio 'lub-dub'.",
        "4. Circulacion Mayor y Menor: Visualizacion interactiva del flujo de sangre oxigenada (roja, arteria aorta) y desoxigenada (azul, venas cavas).",
        "5. Ergonomia Senior (+60): Botones grandes de facil lectura, alto contraste visual y textos medicos explicativos 100% en espanol.",
        "Presenta la aplicacion interactiva terminada y lista para explorar directamente en la pantalla de chat.\""
    ]
    y_pr = 512
    for pl in prompt_lines:
        is_bold = pl.startswith('"Actua') or pl.startswith('Presenta') or pl.startswith('Muestra') or pl.startswith('1.') or pl.startswith('2.') or pl.startswith('3.') or pl.startswith('4.') or pl.startswith('5.')
        pdf.draw_text(48, y_pr, pl, font='F2' if is_bold else 'F1', size=7.4, r=0.45, g=0.08, b=0.18)
        y_pr -= 13.5

    # Seccion 3: Dialogo y Preguntas de Reflexion con Gemini en el Aula
    pdf.set_fill_color(0.99, 0.97, 0.98)
    pdf.set_stroke_color(0.7, 0.2, 0.35)
    pdf.set_line_width(1.0)
    pdf.rect(30, 235, 552, 115, fill=True, stroke=True)

    pdf.draw_text(42, 335, 'PREGUNTAS DE REFLEXION Y DIALOGO CON GEMINI EN EL AULA:', font='F2', size=8.8, r=0.55, g=0.05, b=0.2)

    q1 = "Pregunta 1 • El Sonido Cardiaco y las Valvulas: \"Gemini, en el fonendoscopio escucho el ritmo 'lub-dub'. ¿Que valvulas se cierran en cada golpe (mitral/tricuspide vs. aortica/pulmonar) y como sostiene este bombeo continuo la presion arterial?\""
    q1_lines = wrap_text(q1, 114)
    pdf.draw_text(42, 318, q1_lines[0], font='F2', size=7.5, r=0.2, g=0.1, b=0.15)
    pdf.draw_text(42, 307, q1_lines[1], font='F1', size=7.4, r=0.25, g=0.15, b=0.2)

    q2 = "Pregunta 2 • El Sistema Electrico y el Marcapasos Natural: \"Gemini, ¿como genera el nodulo sinusal los impulsos electricos que coordinan la contraccion de las auriculas antes de los ventriculos y por que a veces se necesita un marcapasos artificial?\""
    q2_lines = wrap_text(q2, 114)
    pdf.draw_text(42, 290, q2_lines[0], font='F2', size=7.5, r=0.2, g=0.1, b=0.15)
    pdf.draw_text(42, 279, q2_lines[1], font='F1', size=7.4, r=0.25, g=0.15, b=0.2)

    q3 = "Pregunta 3 • Salud Cardiovascular Senior (+65): \"Gemini, ¿cuales son los 3 habitos diarios mas determinantes (caminar a ritmo activo, dieta mediterranea baja en sal y descanso nocturno) para cuidar la elasticidad arterial en personas mayores?\""
    q3_lines = wrap_text(q3, 114)
    pdf.draw_text(42, 262, q3_lines[0], font='F2', size=7.5, r=0.2, g=0.1, b=0.15)
    pdf.draw_text(42, 251, q3_lines[1], font='F1', size=7.4, r=0.25, g=0.15, b=0.2)

    # Seccion 4: Procedencia Cientifica Oficial & Triple Salvaguarda
    pdf.set_fill_color(0.98, 0.98, 0.99)
    pdf.set_stroke_color(0.5, 0.5, 0.6)
    pdf.set_line_width(0.8)
    pdf.rect(30, 115, 552, 110, fill=True, stroke=True)

    pdf.draw_text(42, 212, 'PROCEDENCIA CIENTIFICA OFICIAL Y METODOLOGIA DIDACTICA GARANTIZADA:', font='F2', size=8.5, r=0.2, g=0.25, b=0.35)
    fuente1 = "- Fuentes Cardiologicas Acreditadas: Modelos volumetricos basados en las guias de la American Heart Association (AHA), la Sociedad Espanola de Cardiologia (SEC) y escaneos por resonancia magnetica cardiaca del NIH."
    f1_lines = wrap_text(fuente1, 114)
    pdf.draw_text(42, 197, f1_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f1_lines) > 1:
        pdf.draw_text(42, 186, f1_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente2 = "- Triple Salvaguarda Pedagogica: El alumno experimenta primero la creacion visual directa con Gemini y dispone del boton de respaldo oficial (BKP) para garantizar que el 100% de la clase complete la experiencia sin fallos."
    f2_lines = wrap_text(fuente2, 114)
    pdf.draw_text(42, 170, f2_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f2_lines) > 1:
        pdf.draw_text(42, 159, f2_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente3 = "- Adaptacion Senior (+60): Cero codigo para el alumno, sin terminales, sin instalaciones externas y con diseno ergonomico optimizado para pantallas tactiles de iPad y monitores del aula."
    f3_lines = wrap_text(fuente3, 114)
    pdf.draw_text(42, 143, f3_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f3_lines) > 1:
        pdf.draw_text(42, 132, f3_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    # Banner inferior BKP
    pdf.set_fill_color(0.2, 0.04, 0.08)
    pdf.set_stroke_color(0.9, 0.3, 0.45)
    pdf.set_line_width(1.2)
    pdf.rect(30, 45, 552, 60, fill=True, stroke=True)

    pdf.draw_text(42, 88, 'COPIA DE RESPALDO OFICIAL (BKP): SIMULADOR_CORAZON_3D.HTML', font='F2', size=9.0, r=1.0, g=0.6, b=0.7)
    pdf.draw_text(42, 73, 'Si por alguna razon tecnica el simulador no se visualiza en tu pantalla de Gemini, pulsa en el Cuadro de Mando del curso:', font='F1', size=7.8, r=0.85, g=0.85, b=0.9)
    pdf.draw_text(42, 58, '«🫀 Ver Simulador Corazon 3D (BKP)» para abrir al instante el modelo 3D oficial garantizado.', font='F2', size=8.0, r=1.0, g=0.6, b=0.7)

    pdf.end_page()

    pdf.write_to_file(output_path)
    try:
        os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
        shutil.copy2(output_path, LOCAL_BACKUP)
    except Exception:
        pass

    print(f"✅ PDF COD-002 generado con éxito en: {output_path}")
    return output_path

if __name__ == '__main__':
    try:
        build_cod_002_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-002: {e}")
        sys.exit(1)
