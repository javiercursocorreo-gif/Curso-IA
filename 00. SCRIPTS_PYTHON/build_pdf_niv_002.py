#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_niv_002.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter):
9. NIV-002_Radar_de_Deteccin_de_Fraudes_y_Estafas_p.pdf
para la Sesión 02 del Curso de IA.

Nuevo estándar de visualización directa:
- Cero código intermedio para el alumno senior.
- Generación y ejecución directa en pantalla (Canvas / Vista previa).
- Copia de respaldo (BKP) oficial garantizada con SIMULADOR_RADAR_ESTAFAS_SENIORS.html.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/02_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "9. NIV-002_Radar_de_Deteccin_de_Fraudes_y_Estafas_p.pdf")

ALT_PATHS = [
    "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/09. [NIV] BLOQUE_9_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20/NIV-002_Radar de Detección de Fraudes y Estafas para Mayores.pdf",
    "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/[NIV] BLOQUE_10_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20/NIV-002_Radar_de_Deteccin_de_Fraudes_y_Estafas_p.pdf"
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

def build_niv_002_pdf(output_path=PDF_PATH):
    pdf = NativePDFWriter(612.0, 792.0)
    pdf.start_page()

    # Marco exterior ámbar de alerta y seguridad
    pdf.set_fill_color(0.995, 0.99, 0.97)
    pdf.set_stroke_color(0.85, 0.5, 0.05)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal
    pdf.set_fill_color(0.25, 0.12, 0.02)
    pdf.rect(24, 716, 564, 52, fill=True, stroke=False)

    pdf.draw_text(36, 750, 'SESION 02 • MICRO-APLICACION DE VIDA REAL (+65) [NIV-002]', font='F2', size=8.5, r=1.0, g=0.75, b=0.4)
    pdf.draw_text(36, 730, 'Radar de Deteccion de Fraudes y Estafas para Mayores (+65)', font='F2', size=13.0, r=1, g=1, b=1)

    # Seccion 1: Metodologia Directa en 2 Pasos
    pdf.set_fill_color(1.0, 0.97, 0.92)
    pdf.set_stroke_color(0.9, 0.55, 0.15)
    pdf.set_line_width(1.0)
    pdf.rect(30, 580, 552, 126, fill=True, stroke=True)

    pdf.draw_text(42, 692, 'METODOLOGIA DIRECTA: GENERACION Y VISUALIZACION EN PANTALLA SIN CODIGO', font='F2', size=9.2, r=0.6, g=0.3, b=0.05)

    p1_title = 'PASO 1 • Copiar el Prompt Maestro en Gemini (gemini.google.com):'
    p1_desc = 'Pega el texto del recuadro inferior en Gemini. El prompt esta calibrado para que Gemini abra y ejecute directamente el radar interactivo en pantalla (Canvas / Vista previa) sin obligarte a revisar codigo.'
    p1_lines = wrap_text(p1_desc, 114)
    pdf.draw_text(42, 676, p1_title, font='F2', size=8.0, r=0.75, g=0.35, b=0.05)
    pdf.draw_text(42, 665, p1_lines[0], font='F1', size=7.8, r=0.25, g=0.2, b=0.15)
    if len(p1_lines) > 1:
        pdf.draw_text(42, 655, p1_lines[1], font='F1', size=7.8, r=0.25, g=0.2, b=0.15)

    p2_title = 'PASO 2 • Experimentar y Dialogar con Gemini en el Aula:'
    p2_desc = 'Prueba las 6 situaciones cotidianas de riesgo (SMS falsos, llamadas del banco o timo del hijo) para ver el semaforo de peligro, y plantea a Gemini las 3 preguntas de ciberseguridad ciudadana.'
    pdf.draw_text(42, 638, p2_title, font='F2', size=8.0, r=0.75, g=0.35, b=0.05)
    pdf.draw_text(42, 627, p2_desc, font='F1', size=7.8, r=0.25, g=0.2, b=0.15)

    p3_title = 'GARANTIA OFICIAL • Copia de Respaldo Oficial Garantizada (BKP en el Mapa):'
    p3_desc = 'Si por saturacion o corte de red la IA no visualiza el modelo interactivo, pulsa en el Cuadro de Mando del curso:'
    p3_btn = '«🛡️ Abrir Radar Anti-Estafas (+65) (HTML)» para interactuar de inmediato con el escudo de seguridad garantizado.'
    pdf.draw_text(42, 610, p3_title, font='F2', size=8.0, r=0.8, g=0.2, b=0.05)
    pdf.draw_text(42, 599, p3_desc, font='F1', size=7.8, r=0.25, g=0.2, b=0.15)
    pdf.draw_text(42, 588, p3_btn, font='F2', size=7.8, r=0.75, g=0.3, b=0.05)

    # Seccion 2: Prompt Maestro para Gemini
    pdf.set_fill_color(0.99, 0.97, 0.93)
    pdf.set_stroke_color(0.85, 0.5, 0.15)
    pdf.set_line_width(1.0)
    pdf.rect(30, 360, 552, 210, fill=True, stroke=True)

    pdf.draw_text(42, 555, 'PROMPT MAESTRO PARA CREAR EL RADAR DE DETECCION DE ESTAFAS SENIOR (+65):', font='F2', size=9.0, r=0.6, g=0.3, b=0.05)
    pdf.draw_text(42, 542, '(Selecciona y copia todo el bloque de texto para pegarlo en gemini.google.com)', font='F3', size=7.4, r=0.5, g=0.4, b=0.3)

    # Recuadro interior del prompt
    pdf.set_fill_color(0.98, 0.94, 0.88)
    pdf.set_stroke_color(0.85, 0.55, 0.2)
    pdf.set_line_width(0.8)
    pdf.rect(40, 370, 532, 160, fill=True, stroke=True)

    prompt_lines = [
        "\"Actua como un inspector de policia especializado en ciberseguridad y proteccion de mayores (+65).",
        "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) una aplicacion titulada 'Radar Antifraude':",
        "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
        "1. Cuestionario de 6 situaciones con botones Si/No: Llamada urgente pidiendo claves, SMS de paquete con enlace,",
        "   mensaje de WhatsApp de numero desconocido diciendo ser un familiar, revisor no avisado del gas.",
        "2. Semaforo dinamico de peligro: Verde (Seguro, 0 puntos), Ambar (Sospechoso, 1-2 puntos), Rojo (Estafa Inminente, 3+ puntos).",
        "3. Panel de socorro rapido: Botones directos para llamar al 091 (Policia), 062 (Guardia Civil) y pautas de bloqueo bancario.",
        "4. Ergonomia Senior: Letra grande (18px), alto contraste, explicaciones sin tecnicismos y boton de reinicio.\""
    ]
    y_pr = 516
    for pl in prompt_lines:
        is_bold = pl.startswith('"Actua') or pl.startswith('Muestra') or pl.startswith('1.') or pl.startswith('2.') or pl.startswith('3.') or pl.startswith('4.')
        pdf.draw_text(48, y_pr, pl, font='F2' if is_bold else 'F1', size=7.3, r=0.35, g=0.15, b=0.05)
        y_pr -= 12.0

    # Seccion 3: Dialogo y Preguntas de Reflexion con Gemini en el Aula
    pdf.set_fill_color(0.99, 0.98, 0.96)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 225, 552, 122, fill=True, stroke=True)

    pdf.draw_text(42, 332, 'PREGUNTAS DE DIALOGO CON GEMINI EN EL AULA (CIBERSEGURIDAD SENIOR):', font='F2', size=8.8, r=0.7, g=0.35, b=0.05)

    q1 = "Pregunta 1 • La Regla de Oro Bancaria: \"Gemini, ¿por que un banco real nunca jamas pide por telefono ni por SMS la clave secreta o un codigo de confirmacion recibido por mensaje?\""
    q1_lines = wrap_text(q1, 114)
    pdf.draw_text(42, 316, q1_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 305, q1_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q2 = "Pregunta 2 • El Timo del Hijo en Apuros: \"Gemini, si recibo un mensaje de un numero desconocido diciendo 'Papa, se me ha roto el movil, hablame por aqui y hazme un Bizum urgente', ¿que 2 pasos debo dar antes de responder?\""
    q2_lines = wrap_text(q2, 114)
    pdf.draw_text(42, 288, q2_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 277, q2_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    q3 = "Pregunta 3 • Falsos Revisores en Casa: \"Gemini, ¿que documento oficial deben mostrar los tecnicos legitimos del gas o la luz y por que esta prohibido pagarles dinero en metalico en el domicilio?\""
    q3_lines = wrap_text(q3, 114)
    pdf.draw_text(42, 260, q3_lines[0], font='F2', size=7.5, r=0.1, g=0.2, b=0.25)
    pdf.draw_text(42, 249, q3_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    # Seccion 4: Triple Salvaguarda & Garantia Pedagogica
    pdf.set_fill_color(0.98, 0.98, 0.99)
    pdf.set_stroke_color(0.5, 0.5, 0.6)
    pdf.set_line_width(0.8)
    pdf.rect(30, 108, 552, 105, fill=True, stroke=True)

    pdf.draw_text(42, 198, 'LA TRIPLE SALVAGUARDA PEDAGOGICA Y ACCESIBILIDAD SENIOR (+65):', font='F2', size=8.5, r=0.2, g=0.25, b=0.35)
    fuente1 = "- Fuentes de Seguridad Oficiales: Protocolos de prevencion del Instituto Nacional de Ciberseguridad (INCIBE 017), Policia Nacional y Guardia Civil para la proteccion del colectivo de mayores."
    f1_lines = wrap_text(fuente1, 114)
    pdf.draw_text(42, 184, f1_lines[0], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)
    if len(f1_lines) > 1:
        pdf.draw_text(42, 173, f1_lines[1], font='F1', size=7.5, r=0.2, g=0.25, b=0.3)

    fuente2 = "- Diseno Ergonomico sin Barreras: Letra grande, botones de alto contraste, lectura adaptada y compatibilidad total con pantallas de aula, iPad y ordenadores portatiles."
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
    pdf.set_fill_color(0.25, 0.1, 0.02)
    pdf.set_stroke_color(0.9, 0.5, 0.1)
    pdf.set_line_width(1.2)
    pdf.rect(30, 42, 552, 54, fill=True, stroke=True)

    pdf.draw_text(42, 80, 'APLICACION OFICIAL GARANTIZADA (BKP): SIMULADOR_RADAR_ESTAFAS_SENIORS.HTML', font='F2', size=8.8, r=1.0, g=0.7, b=0.3)
    pdf.draw_text(42, 65, 'Si deseas abrir la aplicacion terminada y depurada, en el Cuadro de Mando de la Sesion 02 haz clic en:', font='F1', size=7.6, r=0.85, g=0.85, b=0.9)
    pdf.draw_text(42, 52, '«🛡️ Abrir Radar Anti-Estafas (+65) (HTML)» para interactuar al instante con el escudo de ciberseguridad.', font='F2', size=7.8, r=1.0, g=0.7, b=0.3)

    pdf.end_page()

    pdf.write_to_file(output_path)
    for alt in ALT_PATHS:
        try:
            os.makedirs(os.path.dirname(alt), exist_ok=True)
            shutil.copy2(output_path, alt)
        except Exception:
            pass

    print(f"✅ PDF NIV-002 generado con éxito en: {output_path}")
    return output_path

if __name__ == '__main__':
    try:
        build_niv_002_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF NIV-002: {e}")
        sys.exit(1)
