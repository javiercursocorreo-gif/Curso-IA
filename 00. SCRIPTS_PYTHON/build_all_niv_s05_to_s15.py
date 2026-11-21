#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_all_niv_s05_to_s15.py
Genera las Fichas Didácticas Oficiales de 1 Página (Letter) para la Etiqueta [NIV]
desde la Sesión 05 hasta la Sesión 15 (ambas inclusive), aplicando estrictamente
el FORMATO OFICIAL NUEVO de la Sesión 04 (build_pdf_niv_004.py):

Estructura de 1 Página Completa:
1. Marco exterior elegante verde esmeralda y oro (20, 20, 572, 752)
2. Cabecera principal institucional (24, 716, 564, 52)
3. Sección 1: Metodología Directa en 2 Pasos (30, 580, 552, 126)
4. Sección 2: Prompt Maestro para Gemini con caja interior (30, 360, 552, 210)
5. Sección 3: Diálogo y Preguntas de Reflexión con Gemini en el Aula (30, 225, 552, 122)
6. Sección 4: La Triple Salvaguarda Pedagógica y Accesibilidad Senior (+65) (30, 108, 552, 105)
7. Banner Inferior BKP: Aplicación Oficial Garantizada en el Mapa (30, 42, 552, 54)
"""

import os
import sys
import shutil

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SESSIONS_BASE = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

def escape_pdf_text(text):
    text = str(text)
    for em in ['🛡️', '🛡', '🚀', '✨', '⭐', '💡', '📌', '🎉', '📄', '⚙️', '🔧', '🧭', '🌲', '⚡', '🎬', '🎥', '🍿', '🎵', '🎹', '🎼', '🏛️', '🏛', '«', '»']:
        text = text.replace(em, '')
    text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    replacements = {
        'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
        'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
        'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
        '•': '-', '—': '-', '–': '-', 'º': 'o', 'ª': 'a',
        '¿': '\xbf', '¡': '\xa1', '➔': '->', '→': '->',
        '’': "'", '‘': "'", '“': '"', '”': '"'
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

def render_niv_worksheet(data):
    session_num = data['session_num']
    tag_code = data['tag_code']
    title = data['title']
    output_filename = data['filename']
    output_path = os.path.join(SESSIONS_BASE, f"{session_num:02d}_Sesion", output_filename)
    
    pdf = NativePDFWriter(612.0, 792.0)
    pdf.start_page()

    # 1. Marco exterior esmeralda y ámbar
    pdf.set_fill_color(0.99, 0.995, 0.99)
    pdf.set_stroke_color(0.05, 0.55, 0.35)
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # 2. Cabecera principal
    pdf.set_fill_color(0.04, 0.22, 0.14)
    pdf.rect(24, 716, 564, 52, fill=True, stroke=False)
    pdf.draw_text(36, 750, f'SESION {session_num:02d} • MICRO-APLICACION DE VIDA REAL (+65) [{tag_code}]', font='F2', size=8.5, r=0.4, g=0.9, b=0.6)
    pdf.draw_text(36, 730, title, font='F2', size=12.2, r=1, g=1, b=1)

    # 3. Sección 1: Metodología Directa en 2 Pasos
    pdf.set_fill_color(0.94, 0.985, 0.95)
    pdf.set_stroke_color(0.1, 0.65, 0.4)
    pdf.set_line_width(1.0)
    pdf.rect(30, 580, 552, 126, fill=True, stroke=True)

    pdf.draw_text(42, 692, 'METODOLOGIA DIRECTA: GENERACION Y VISUALIZACION EN PANTALLA SIN CODIGO', font='F2', size=9.2, r=0.05, g=0.4, b=0.2)

    p1_title = 'PASO 1 • Copiar el Prompt Maestro en Gemini (gemini.google.com):'
    p1_desc = 'Abre Gemini en tu navegador y pega el recuadro inferior. El prompt esta calibrado para que Gemini abra y ejecute directamente la aplicacion interactiva en pantalla (Canvas / Vista previa) sin obligarte a revisar codigo.'
    p1_lines = wrap_text(p1_desc, 114)
    pdf.draw_text(42, 676, p1_title, font='F2', size=8.0, r=0.05, g=0.5, b=0.3)
    pdf.draw_text(42, 665, p1_lines[0], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    if len(p1_lines) > 1:
        pdf.draw_text(42, 655, p1_lines[1], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p2_title = 'PASO 2 • Experimentar y Dialogar con Gemini en el Aula:'
    p2_desc = data['step2_desc']
    p2_lines = wrap_text(p2_desc, 114)
    pdf.draw_text(42, 638, p2_title, font='F2', size=8.0, r=0.05, g=0.5, b=0.3)
    pdf.draw_text(42, 627, p2_lines[0], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    if len(p2_lines) > 1:
        pdf.draw_text(42, 617, p2_lines[1], font='F1', size=7.8, r=0.15, g=0.2, b=0.25)

    p3_title = 'GARANTIA OFICIAL • Copia de Respaldo Oficial Garantizada (BKP en el Mapa):'
    p3_desc = 'Si deseas abrir la aplicacion terminada y depurada con voz y diseno senior, pulsa en el Cuadro de Mando del curso:'
    p3_btn = f'<<Abrir {data["sim_title"]} (HTML)» para interactuar de inmediato con tus datos reales.'
    pdf.draw_text(42, 603, p3_title, font='F2', size=8.0, r=0.7, g=0.3, b=0.05)
    pdf.draw_text(42, 593, p3_desc, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
    pdf.draw_text(42, 583, p3_btn, font='F2', size=7.8, r=0.05, g=0.5, b=0.3)

    # 4. Sección 2: Prompt Maestro para Gemini
    pdf.set_fill_color(0.96, 0.99, 0.97)
    pdf.set_stroke_color(0.15, 0.6, 0.35)
    pdf.set_line_width(1.0)
    pdf.rect(30, 360, 552, 210, fill=True, stroke=True)

    pdf.draw_text(42, 555, f'PROMPT MAESTRO PARA CREAR {data["app_name_upper"]} (+65):', font='F2', size=9.0, r=0.05, g=0.4, b=0.25)
    pdf.draw_text(42, 542, '(Selecciona y copia todo el bloque de texto para pegarlo en gemini.google.com)', font='F3', size=7.4, r=0.4, g=0.45, b=0.5)

    # Recuadro interior del prompt
    pdf.set_fill_color(0.91, 0.97, 0.93)
    pdf.set_stroke_color(0.18, 0.65, 0.4)
    pdf.set_line_width(0.8)
    pdf.rect(40, 370, 532, 160, fill=True, stroke=True)

    y_pr = 516
    for pl in data['prompt_lines']:
        lines_wrapped = wrap_text(pl, 110)
        for idx_l, lw in enumerate(lines_wrapped):
            is_bold = (idx_l == 0 and any(lw.startswith(k) for k in ['"Actua', 'Requisitos', '1.', '2.', '3.', '4.', '5.', '6.', '7.', 'Ergonomia', 'Controles']))
            pdf.draw_text(48, y_pr, lw, font='F2' if is_bold else 'F1', size=7.1, r=0.05, g=0.25, b=0.15)
            y_pr -= 10.5

    # 5. Sección 3: Diálogo y Preguntas de Reflexión con Gemini en el Aula
    pdf.set_fill_color(0.99, 0.98, 0.96)
    pdf.set_stroke_color(0.8, 0.5, 0.1)
    pdf.set_line_width(1.0)
    pdf.rect(30, 225, 552, 122, fill=True, stroke=True)

    pdf.draw_text(42, 332, f'PREGUNTAS DE DIALOGO CON GEMINI EN EL AULA ({data["debate_topic_upper"]}):', font='F2', size=8.8, r=0.7, g=0.35, b=0.05)

    y_q = 316
    for q_text in data['questions']:
        q_lines = wrap_text(q_text, 114)
        for idx_q, ql in enumerate(q_lines):
            pdf.draw_text(42, y_q, ql, font='F2' if idx_q == 0 else 'F1', size=7.3, r=0.1 if idx_q == 0 else 0.2, g=0.2 if idx_q == 0 else 0.25, b=0.25 if idx_q == 0 else 0.3)
            y_q -= 9.8
        y_q -= 3.0

    # 6. Sección 4: Triple Salvaguarda Pedagógica y Accesibilidad Senior (+65)
    pdf.set_fill_color(0.98, 0.98, 0.99)
    pdf.set_stroke_color(0.5, 0.5, 0.6)
    pdf.set_line_width(0.8)
    pdf.rect(30, 108, 552, 105, fill=True, stroke=True)

    pdf.draw_text(42, 198, 'LA TRIPLE SALVAGUARDA PEDAGOGICA Y ACCESIBILIDAD SENIOR (+65):', font='F2', size=8.5, r=0.2, g=0.25, b=0.35)
    
    f1_lines = wrap_text(data['fuente1'], 114)
    pdf.draw_text(42, 184, f1_lines[0], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)
    if len(f1_lines) > 1:
        pdf.draw_text(42, 174, f1_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    f2_text = "- Diseno Ergonomico sin Barreras: Letra ampliable a 18.5px con un solo clic, botones de alto contraste, lectura por voz sintetizada en espanol nativo (es-ES) y compatibilidad total con pantallas de aula, iPad y portatiles."
    f2_lines = wrap_text(f2_text, 114)
    pdf.draw_text(42, 160, f2_lines[0], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)
    if len(f2_lines) > 1:
        pdf.draw_text(42, 150, f2_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    f3_text = "- Garantia de Respaldo Tecnico: El alumno experimenta el prompt en Gemini sabiendo que dispone del simulador oficial garantizado en el Cuadro de Mando del curso para asegurar el 100% de exito pedagogico en la clase."
    f3_lines = wrap_text(f3_text, 114)
    pdf.draw_text(42, 136, f3_lines[0], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)
    if len(f3_lines) > 1:
        pdf.draw_text(42, 126, f3_lines[1], font='F1', size=7.4, r=0.2, g=0.25, b=0.3)

    # 7. Banner inferior BKP
    pdf.set_fill_color(0.04, 0.18, 0.1)
    pdf.set_stroke_color(0.2, 0.8, 0.5)
    pdf.set_line_width(1.2)
    pdf.rect(30, 42, 552, 54, fill=True, stroke=True)

    pdf.draw_text(42, 80, f'APLICACION OFICIAL GARANTIZADA (BKP): {data["sim_file"].upper()}', font='F2', size=8.8, r=0.2, g=0.85, b=0.5)
    pdf.draw_text(42, 65, f'Si deseas abrir la aplicacion terminada y depurada, en el Cuadro de Mando de la Sesion {session_num:02d} haz clic en:', font='F1', size=7.6, r=0.8, g=0.85, b=0.9)
    pdf.draw_text(42, 52, f'<<Abrir {data["sim_title"]} (HTML)» para interactuar al instante con datos reales.', font='F2', size=7.8, r=0.2, g=0.85, b=0.5)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ [{tag_code}] Ficha NIV generada con éxito (1 página completa): {output_path}")

        # Sincronización exhaustiva en Bloque 9, Bloque 10 y Carpeta de Sesión
    canonical_names = {
        5: ["NIV-005_Los 5 Niveles de la Evolución del Dinero.pdf", "NIV-005_Los_5_Niveles_de_la_Evolucin_del_Dinero.pdf"],
        6: ["NIV-006_Calculadora de Poder Adquisitivo y Cesta de la Compra.pdf", "NIV-006_Calculadora_de_Poder_Adquisitivo_y_Cesta.pdf", "NIV-006_Los 6 Niveles del Poder Adquisitivo y Coste de Vida Global.pdf"],
        7: ["NIV-007_Los 5 Niveles de Automatización del Trabajo Humano.pdf", "NIV-007_Los_5_Niveles_de_Automatizacion_e_IA_en_el_Hogar.pdf", "NIV-007_Los_5_Niveles_de_Automatizacin_e_IA_en_e.pdf"],
        8: ["NIV-008_Los 6 Niveles de Persuasión e Influencia de Masas.pdf", "NIV-008_Radar_Antimanipulacin_Los_6_Niveles_de_P.pdf"],
        9: ["NIV-009_Los 5 Niveles de Seguridad Ciudadana y Prevención Urbana.pdf", "NIV-009_Semforo_de_Seguridad_Ciudadana_y_Prevenc.pdf"],
        10: ["NIV-010_Los 6 Niveles de Alfabetización Financiera Personal.pdf", "NIV-010_Los_6_Niveles_de_Alfabetizacin_y_Blindaj.pdf"],
        11: ["NIV-011_Los 7 Niveles de Inteligencia Cognitiva y Conciencia.pdf", "NIV-011_Los_7_Niveles_de_Inteligencia_Cognitiva.pdf"],
        12: ["NIV-012_Los 6 Niveles de Conciencia y Alerta Neurológica.pdf", "NIV-012_Los_6_Niveles_de_Conciencia_Ritmos_Circa.pdf"],
        13: ["NIV-013_Los 5 Niveles de la Memoria y Retención Biológica.pdf", "NIV-013_Los_5_Niveles_de_Memoria_Prctica_y_Reten.pdf"],
        14: ["NIV-014_Los 6 Niveles de Toma de Decisiones y Sesgos Cognitivos.pdf", "NIV-014_Los_6_Niveles_de_Toma_de_Decisiones_y_Fi.pdf"],
        15: ["NIV-015_Los 5 Niveles de Resiliencia y Salud Mental.pdf", "NIV-015_Los_5_Niveles_de_Resiliencia_Emocional_y.pdf"]
    }

    # Copiar a Bloque 9 y Bloque 10
    b9_dir = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/09. [NIV] BLOQUE_9_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20")
    b10_dir = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/[NIV] BLOQUE_10_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20")
    sess_dir = os.path.join(SESSIONS_BASE, f"{session_num:02d}_Sesion")

    for cname in canonical_names.get(session_num, []):
        for target_dir in [b9_dir, b10_dir]:
            try:
                os.makedirs(target_dir, exist_ok=True)
                shutil.copy2(output_path, os.path.join(target_dir, cname))
            except Exception as e:
                print(f"Error copiando a {target_dir}: {e}")
        
        # También en la carpeta de sesión con prefijo 9. y sin prefijo
        try:
            shutil.copy2(output_path, os.path.join(sess_dir, cname))
            if not cname.startswith("9. "):
                shutil.copy2(output_path, os.path.join(sess_dir, f"9. {cname}"))
        except Exception as e:
            pass

# ==============================================================================
# CATÁLOGO DE DATOS DIDÁCTICOS PARA NIV-005 A NIV-015
# ==============================================================================
NIV_DATA = [
    {
        'session_num': 5,
        'tag_code': 'NIV-005',
        'filename': '9. NIV-005_Los_5_Niveles_de_la_Evolucin_del_Dinero.pdf',
        'title': 'Los 5 Niveles de la Evolucion del Dinero: Del Trueque a Bizum (+65)',
        'app_name_upper': 'EL SIMULADOR DE EVOLUCION DEL DINERO',
        'debate_topic_upper': 'TRANQUILIDAD Y SEGURIDAD FINANCIERA',
        'step2_desc': 'Selecciona tu medio de pago habitual, comprueba el termometro de seguridad frente a perdidas y robos, y plantea a Gemini las 3 preguntas de tranquilidad digital de abajo.',
        'sim_file': 'SIMULADOR_EVOLUCION_DINERO_SENIORS.html',
        'sim_title': 'Simulador Evolución del Dinero (+65)',
        'prompt_lines': [
            "\"Actua como un educador financiero y pedagogo digital para personas mayores (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador sobre la evolucion del dinero:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. Nivel 1: Trueque y mercancias basicas (intercambio directo de sal, trigo o ganado en sociedades antiguas).",
            "2. Nivel 2: Monedas de oro y plata (aparicion del dinero contable de curso legal y patron metalico).",
            "3. Nivel 3: Billetes de papel y libreta de ahorros tradicional (el dinero impreso y bancario de toda la vida).",
            "4. Nivel 4: Tarjetas con chip contactless y cajeros automaticos (seguridad bancaria frente a robos en la calle).",
            "5. Nivel 5: Pagos inmediatos por movil (Bizum, compras online y doble factor biometrico con IA).",
            "Controles interactivos: Selector del medio de pago, termometro de riesgo ante perdidas y guia practica de Bizum.",
            "Ergonomia Senior (+60): Botones grandes, alto contraste, modo lectura y lenguaje claro que transmita tranquilidad.\""
        ],
        'questions': [
            "Pregunta 1 • La Seguridad Real de Bizum vs. Billetes: \"Gemini, muchos mayores tememos que nos roben si usamos el movil para pagar. ¿Por que en realidad pagar con Bizum o tarjeta es mucho mas seguro que llevar 200 euros en billetes en la cartera o el bolso?\"",
            "Pregunta 2 • Que Hacer si te Equivocas de Numero al Enviar un Bizum: \"Gemini, ¿como funciona la doble verificacion de Bizum (que muestra el nombre del destinatario antes de confirmar) y que pasos debes dar en tu banco si por error mandas dinero al numero equivocado?\"",
            "Pregunta 3 • La Libreta de Ahorros vs. la Pantalla del Telefono: \"Gemini, ¿por que los bancos estan retirando las libretas fisicas de papel y como puede un adulto mayor configurar la aplicacion bancaria para ver los apuntes con letra grande y sin complicaciones?\""
        ],
        'fuente1': "- Enfoque en Inclusion Financiera: Basado en las recomendaciones del Banco de Espana y la campana 'Soy Mayor, No Idiota' para garantizar una banca accesible, transparente y sin comisiones abusivas para los mayores."
    },
    {
        'session_num': 6,
        'tag_code': 'NIV-006',
        'filename': '9. NIV-006_Calculadora_de_Poder_Adquisitivo_y_Cesta.pdf',
        'title': 'Calculadora de Poder Adquisitivo y Cesta de la Compra (+65)',
        'app_name_upper': 'LA CALCULADORA DE PODER ADQUISITIVO Y CESTA',
        'debate_topic_upper': 'ECONOMIA FAMILIAR Y PODER ADQUISITIVO',
        'step2_desc': 'Mueve los controles de ano (desde 2002 hasta hoy), compara el precio de la cesta basica (aceite, pan, leche, luz) y plantea a Gemini las 3 preguntas de economia familiar de abajo.',
        'sim_file': 'SIMULADOR_PODER_ADQUISITIVO_COSTE_VIDA_SENIORS.html',
        'sim_title': 'Calculadora Poder Adquisitivo (+65)',
        'prompt_lines': [
            "\"Actua como un economista divulgador y pedagogo para personas mayores (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador sobre el poder adquisitivo:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. Selector temporal: compara el coste de la vida entre el ano 2002 (llegada del euro) y el ano actual.",
            "2. Cesta basica senior: barra de pan, litro de aceite de oliva, docena de huevos, recibo de la luz y kilo de ternera.",
            "3. Equivalencia de billetes: muestra que podias comprar con un billete de 50 euros en 2002 vs lo que compras hoy.",
            "4. Termometro de inflacion acumulada: porcentaje real de subida de precios y efecto en las pensiones.",
            "5. Consejos practicos de ahorro inteligente en la cesta de la compra para proteger la economia familiar.",
            "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
        ],
        'questions': [
            "Pregunta 1 • La Ilusion Monetaria y la Inflacion Real: \"Gemini, ¿por que aunque nuestra pension suba cada ano, cuando vamos al supermercado sentimos que nuestro carrito lleva menos productos que hace diez anos?\"",
            "Pregunta 2 • La Comparativa con las Pesetas: \"Gemini, los mayores seguimos convirtiendo mentalmente los precios a pesetas: ¿que productos cotidianos se han encarecido mas desde el cambio de moneda y por que?\"",
            "Pregunta 3 • Estrategias Practicas de Ahorro con IA: \"Gemini, ¿como puedo usar la IA en mi movil para comparar folletos de supermercados locales y planificar menus semanales saludables al mejor precio?\""
        ],
        'fuente1': "- Enfoque en Economia Domestica Senior: Basado en los indices oficiales del Instituto Nacional de Estadistica (INE) y estudios de la OCU sobre patrones de gasto en hogares de personas jubiladas."
    },
    {
        'session_num': 7,
        'tag_code': 'NIV-007',
        'filename': '9. NIV-007_Los_5_Niveles_de_Automatizacin_e_IA_en_e.pdf',
        'title': 'Los 5 Niveles de Automatizacion e IA en el Hogar (+65)',
        'app_name_upper': 'EL SIMULADOR DE AUTOMATIZACION DEL HOGAR',
        'debate_topic_upper': 'DOMOTICA AMIGABLE Y TRANQUILIDAD SENIOR',
        'step2_desc': 'Marca los electrodomesticos que tienes en casa, descubre tu nivel de automatizacion y plantea a Gemini las 3 preguntas sobre como simplificar tareas cotidianas sin estres.',
        'sim_file': 'SIMULADOR_AUTOMATIZACION_TRABAJO_IA_SENIORS.html',
        'sim_title': 'Simulador Automatización Hogar (+65)',
        'prompt_lines': [
            "\"Actua como un experto en domotica amigable y divulgador tecnologico para personas mayores (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador sobre el hogar senior:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. Escala de 5 niveles: 1) Mecanizacion basica, 2) Hogar programable, 3) Salud y conexion, 4) Voz, 5) IA Gemini.",
            "2. Test interactivo del hogar: casillas de seleccion para lavadora, microondas con reloj, Smart TV, Alexa y Gemini.",
            "3. Calculador de horas de vida ahorradas: indicador visual de tiempo libre semanal ganado gracias a la tecnologia.",
            "4. Termometro de confianza tecnologica: selector de actitud (timida, prudente, normal, buena o entusiasta).",
            "5. Consejos practicos para dar el siguiente paso sin miedo: dictado por voz, recordatorios hablados y consultas faciles.",
            "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
        ],
        'questions': [
            "Pregunta 1 • La Tranquilidad y el Control en Casa: \"Gemini, ¿por que automatizar tareas cotidianas (como encender luces por sensor o pedir la radio con la voz) no significa perder el control ni acomodarse, sino ganar seguridad y bienestar?\"",
            "Pregunta 2 • El Poder del Dictado por Voz: \"Gemini, ¿como puede una persona mayor que tiene dificultad para teclear en la pantalla tactil usar el microfono del teclado y la IA para dictar mensajes largos o notas sin cansancio visual?\"",
            "Pregunta 3 • La IA como Secretaria Personal: \"Gemini, ¿de que formas cotidianas puedes ayudarme en el dia a dia: resumiendo un prospecto de medicamento, recordando fechas importantes o redactando una reclamacion formal?\""
        ],
        'fuente1': "- Enfoque en Vida Independiente: Basado en estudios sobre entornos inteligentes para la tercera edad (Ambient Assisted Living - AAL) orientados a prolongar la estancia autonoma y segura en el propio hogar."
    },
    {
        'session_num': 8,
        'tag_code': 'NIV-008',
        'filename': '9. NIV-008_Radar_Antimanipulacin_Los_6_Niveles_de_P.pdf',
        'title': 'Radar Antimanipulacion: Los 6 Niveles de Venta Agresiva (+65)',
        'app_name_upper': 'EL RADAR ANTIMANIPULACION Y VENTAS AGRESIVAS',
        'debate_topic_upper': 'PROTECCION DEL CONSUMIDOR Y DERECHOS',
        'step2_desc': 'Selecciona las situaciones comerciales tipicas (llamadas de luz a la siesta, visitas a puerta fria), mide el nivel de presion y plantea a Gemini las 3 preguntas de proteccion asertiva.',
        'sim_file': 'SIMULADOR_RADAR_PERSUASION_PUBLICIDAD_SENIORS.html',
        'sim_title': 'Radar Antimanipulación y Ventas (+65)',
        'prompt_lines': [
            "\"Actua como un experto en derechos del consumidor y asertividad para personas mayores (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un radar antimanipulacion:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. 6 Niveles de Presion comercial: Informacion neutra, simpatia fingida, falsa urgencia, miedo, confusion y coaccion.",
            "2. Situaciones cotidianas: llamadas comerciales a horas intempestivas, revisiones falsas del gas y ofertas unicas.",
            "3. Guion de respuestas asertivas: frases rotundas y amables para colgar el telefono o despedir visitas no deseadas.",
            "4. Guia practica de la Lista Robinson: explicacion sencilla de como registrarse gratis para bloquear llamadas comerciales.",
            "5. Semáforo de alerta: indicador visual de peligro contractual y recordatorio de los 14 dias de derecho de desistimiento.",
            "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
        ],
        'questions': [
            "Pregunta 1 • La Presion Psicologica del Comercial: \"Gemini, ¿por que los comerciales telefonicos insisten tanto en que 'la oferta solo dura hasta hoy' y que tactica psicologica usan para hacernos sentir culpables o desconfiados?\"",
            "Pregunta 2 • El Derecho a Decir 'No' sin Dar Explicaciones: \"Gemini, a los mayores nos educaron para ser amables y educados con quien llama a nuestra puerta o telefono: ¿como podemos rechazar una venta sin sentir que estamos siendo groseros?\"",
            "Pregunta 3 • Que Hacer si Hemos Firmado sin Querer: \"Gemini, si un comercial nos ha convencido para cambiar de compania de luz o gas por telefono, ¿cuales son los pasos exactos y el plazo legal de 14 dias para anularlo todo sin coste?\""
        ],
        'fuente1': "- Enfoque en Consumo Seguro: Basado en las directrices de la Agencia Espanola de Proteccion de Datos (AEPD), el Ministerio de Consumo y la normativa europea sobre practicas comerciales desleales."
    },
    {
        'session_num': 9,
        'tag_code': 'NIV-009',
        'filename': '9. NIV-009_Semforo_de_Seguridad_Ciudadana_y_Prevenc.pdf',
        'title': 'Semaforo de Seguridad Ciudadana y Prevencion (+65)',
        'app_name_upper': 'EL SEMAFORO DE SEGURIDAD CIUDADANA Y PREVENCION',
        'debate_topic_upper': 'PREVENCION Y TRANQUILIDAD CIUDADANA',
        'step2_desc': 'Evalua tus habitos cotidianos al sacar dinero en el cajero, abrir el portal o caminar por la calle, y plantea a Gemini las 3 preguntas clave sobre seguridad y auxilio rapido.',
        'sim_file': 'SIMULADOR_SEGURIDAD_PREVENCION_SENIORS.html',
        'sim_title': 'Semáforo Seguridad Ciudadana (+65)',
        'prompt_lines': [
            "\"Actua como un delegado de participacion ciudadana de la Policia Nacional y formador senior (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un semaforo de seguridad:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. 3 Entornos clave: 1) Cajero y dinero en efectivo, 2) Portal, escaleras y ascensor, 3) Calle y transporte publico.",
            "2. Checklist de prevencion: tapar el teclado al teclear el PIN, no abrir a desconocidos, bolso cruzado y desconfiar de distracciones.",
            "3. Semaforo interactivo: puntuacion verde (habitos blindados), ambar (precaucion necesaria) y rojo (descuidos peligrosos).",
            "4. Directorio de emergencia directo: botones visuales con los telefonos 091 (Policia), 062 (Guardia Civil) y 112 (Emergencias).",
            "5. Consejos practicos frente al timo del abrazo solidario, la mancha en la chaqueta o el billete caido al suelo.",
            "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
        ],
        'questions': [
            "Pregunta 1 • La Rutina al Sacar Dinero del Banco: \"Gemini, ¿cuales son las 3 reglas de oro que debe seguir un jubilado al sacar dinero del cajero para no ser senalado por carteristas que vigilan en los alrededores?\"",
            "Pregunta 2 • La Seguridad en el Portal de Casa: \"Gemini, ¿por que el descansillo y el portal son los lugares mas vulnerables y que debemos hacer si un desconocido intenta entrar a la vez que nosotros diciendo que va al 3º B?\"",
            "Pregunta 3 • Como Pedir Ayuda en la Calle sin Panico: \"Gemini, si una persona mayor se desorienta, se marea o sospecha que alguien la sigue en la calle, ¿cual es el protocolo mas rapido y seguro para buscar refugio inmediato?\""
        ],
        'fuente1': "- Enfoque en Seguridad Participativa: Basado en el 'Plan Mayor Seguridad' de la Secretaria de Estado de Seguridad (Policia Nacional y Guardia Civil) para la proteccion y asistencia al colectivo senior."
    },
    {
        'session_num': 10,
        'tag_code': 'NIV-010',
        'filename': '9. NIV-010_Los_6_Niveles_de_Alfabetizacin_y_Blindaj.pdf',
        'title': 'Los 6 Niveles de Blindaje Patrimonial Familiar (+65)',
        'app_name_upper': 'EL SIMULADOR DE BLINDAJE PATRIMONIAL FAMILIAR',
        'debate_topic_upper': 'ORDEN JURIDICO Y TRANQUILIDAD FAMILIAR',
        'step2_desc': 'Revisa el estado de tus escrituras, cuentas bancarias y testamento, comprueba tu porcentaje de tranquilidad juridica y plantea a Gemini las 3 preguntas sobre como evitar problemas a tus herederos.',
        'sim_file': 'SIMULADOR_SALUD_FINANCIERA_SENIORS.html',
        'sim_title': 'Blindaje Patrimonial y Cuentas (+65)',
        'prompt_lines': [
            "\"Actua como un notario y asesor juridico familiar de confianza para personas mayores (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador de blindaje patrimonial:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. 6 Pilares de Tranquilidad: Testamento al dia, cotitularidad bancaria vs autorizados, poder preventivo, escrituras y donaciones.",
            "2. Checklist de documentos: organizacion de carpetas de suministros, seguro de decesos y registro de voluntades anticipadas.",
            "3. Diferencia practica crucial: por que un 'autorizado' en cuenta no puede disponer de fondos tras el fallecimiento y un cotitular si.",
            "4. Diagnostico interactivo de proteccion: medidor de tranquilidad familiar (0% a 100%) segun los tramites realizados.",
            "5. Guia paso a paso para acudir al notario: costes asequibles, explicaciones sencillas y resolucion de dudas frecuentes.",
            "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
        ],
        'questions': [
            "Pregunta 1 • El Mito del Bloqueo Bancario por Herencia: \"Gemini, ¿por que al fallecer uno de los conyuges el banco suele bloquear parte de las cuentas y como se puede organizar la titularidad en vida para que el viudo/a no se quede sin liquidez?\"",
            "Pregunta 2 • El Gran Beneficio del Poder Notarial Preventivo: \"Gemini, ¿que es un poder preventivo y por que los notarios lo recomiendan a partir de los 65 anos para evitar costosos juicios de incapacitacion si surge un problema de salud?\"",
            "Pregunta 3 • Testamento Tradicional vs. Donacion en Vida: \"Gemini, ¿cuales son los pros y contras fiscales en Espana entre dejar una vivienda en testamento o donarla en vida a los hijos, teniendo en cuenta la plusvalia municipal?\""
        ],
        'fuente1': "- Enfoque en Seguridad Juridica Preventiva: Basado en las publicaciones oficiales del Consejo General del Notariado y las guias de proteccion de patrimonios familiares para personas de edad avanzada."
    },
    {
        'session_num': 11,
        'tag_code': 'NIV-011',
        'filename': '9. NIV-011_Los_7_Niveles_de_Inteligencia_Cognitiva.pdf',
        'title': 'Los 7 Niveles de Inteligencia Cognitiva y Sabiduria (+65)',
        'app_name_upper': 'EL DIAGNOSTICO DE RESERVA COGNITIVA Y SABIDURIA',
        'debate_topic_upper': 'ESTIMULACION MENTAL Y RESERVA COGNITIVA',
        'step2_desc': 'Explora las 7 dimensiones de tu mente madura, prueba los ejercicios breves de asociacion y reflejos, y plantea a Gemini las 3 preguntas sobre como mantener un cerebro lucido y activo.',
        'sim_file': 'SIMULADOR_INTELIGENCIA_COGNITIVA_SENIORS.html',
        'sim_title': 'Diagnóstico Reserva Cognitiva (+65)',
        'prompt_lines': [
            "\"Actua como un neuropsicologo experto en envejecimiento activo y plasticidad cerebral senior (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador de reserva cognitiva:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. 7 Dimensiones cognitivas: Vocabulario, razonamiento verbal, juicio etico, memoria de trabajo, creatividad, templanza y sintesis.",
            "2. Inteligencia fluida vs cristalizada: demostracion de como la experiencia vital supera a la rapidez matematica de los jovenes.",
            "3. Ejercicios breves de gimnasia cerebral: asociacion rapida de ideas, calculo mental cotidiano y reconocimiento de patrones.",
            "4. Medidor de Reserva Cognitiva Activa: evaluacion de habitos protectores (lectura, vida social, paseos y alimentacion mediterranea).",
            "5. Plan semanal de estimulacion mental sin frustracion ni estres, adaptado a la vida diaria de una persona jubilada.",
            "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
        ],
        'questions': [
            "Pregunta 1 • La Plasticidad Cerebral a Cualquier Edad: \"Gemini, durante decadas se creyo que los mayores perdiamos neuronas sin remedio. ¿Que nos ensena la neurociencia moderna sobre la neurogenesis y la creacion de nuevas conexiones neuronales a los 70 y 80 anos?\"",
            "Pregunta 2 • El Papel Clave de las Relaciones Sociales: \"Gemini, ¿por que charlar con amigos, jugar a las cartas o pasear en grupo protege mas al cerebro contra el deterioro cognitivo que hacer pasatiempos en solitario?\"",
            "Pregunta 3 • Actividades Novedosas vs. Rutina: \"Gemini, ¿por que aprender una habilidad completamente nueva (como usar la IA, tocar el piano o aprender un idioma) genera un escudo cognitivo mucho mas potente que repetir tareas ya dominadas?\""
        ],
        'fuente1': "- Enfoque en Neurogerontologia: Basado en las investigaciones del Proyecto Harvard sobre Envejecimiento y los estudios de la Sociedad Espanola de Neurologia (SEN) sobre reserva cognitiva y longevidad activa."
    },
    {
        'session_num': 12,
        'tag_code': 'NIV-012',
        'filename': '9. NIV-012_Los_6_Niveles_de_Conciencia_Ritmos_Circa.pdf',
        'title': 'Los 6 Niveles de Conciencia, Ritmos Circadianos y Sueno (+65)',
        'app_name_upper': 'EL SIMULADOR DE RITMOS CIRCADIANOS Y SUEÑO',
        'debate_topic_upper': 'HIGIENE DEL SUEÑO Y ENERGIA COTIDIANA',
        'step2_desc': 'Ajusta tu reloj de 24 horas (luz solar, comidas, siesta y hora de dormir), mide la calidad de tu descanso y plantea a Gemini las 3 preguntas para dormir mejor sin pastillas.',
        'sim_file': 'SIMULADOR_CONCIENCIA_ALERTA_NEUROLOGICA_SENIORS.html',
        'sim_title': 'Simulador Ritmos y Alerta Serena (+65)',
        'prompt_lines': [
            "\"Actua como un medico especialista en medicina del sueno y ritmos biologicos para personas mayores (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador circadiano:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. Reloj interactivo de 24 horas: paseo matinal bajo la luz del sol, horarios de comidas, siesta reparadora y desconexion nocturna.",
            "2. Los 6 Niveles de Conciencia: desde el sueno profundo delta y REM hasta la alerta serena y la vigilia activa matutina.",
            "3. La Siesta Perfecta: guia interactiva de la siesta de 20 minutos (por que alargarla mas de media hora perjudica el sueno nocturno).",
            "4. Termometro de higiene del sueno: temperatura de la habitacion, cenas ligeras, control de liquidos antes de acostarse y luz calida.",
            "5. Ejercicio guiado de respiracion 4-7-8 con guia visual relajante para conciliar el sueno cuando la mente se desvela de madrugada.",
            "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
        ],
        'questions': [
            "Pregunta 1 • Por Que Despertamos mas Temprano al Envejecer: \"Gemini, ¿por que a partir de los 65 anos el cuerpo adelanta la produccion de melatonina y por que despertarse temprano es un cambio biologico natural y no un sintoma de insomnio?\"",
            "Pregunta 2 • La Trampa de los Somniferos y Pastillas para Dormir: \"Gemini, ¿que riesgos de caidas y perdida de memoria conllevan los ansioliticos y pastillas para dormir en personas mayores, y que pautas naturales son mas eficaces a largo plazo?\"",
            "Pregunta 3 • La Luz del Sol como Medicamento Natural: \"Gemini, ¿por que recibir luz solar directa en los ojos durante el paseo matinal sincroniza el reloj biologico y nos ayuda a dormir profundamente doce horas despues?\""
        ],
        'fuente1': "- Enfoque en Cronobiologia: Basado en las recomendaciones de la Sociedad Espanola del Sueno (SES) y los estudios del Instituto de Investigacion del Sueno sobre el descanso en el adulto mayor."
    },
    {
        'session_num': 13,
        'tag_code': 'NIV-013',
        'filename': '9. NIV-013_Los_5_Niveles_de_Memoria_Prctica_y_Reten.pdf',
        'title': 'Los 5 Niveles de Memoria Practica y Retencion Cotidiana (+65)',
        'app_name_upper': 'EL SIMULADOR DE MEMORIA PRACTICA Y COTIDIANA',
        'debate_topic_upper': 'MEMORIA COTIDIANA Y PAZ MENTAL',
        'step2_desc': 'Explora las tecnicas mnemotecnicas sencillas para recordar llaves, gafas, medicamentos y citas, comprueba tu tranquilidad y plantea a Gemini las 3 preguntas sobre memoria y serenidad.',
        'sim_file': 'SIMULADOR_MEMORIA_RETENCION_BIOLOGICA_SENIORS.html',
        'sim_title': 'Simulador Memoria Cotidiana (+65)',
        'prompt_lines': [
            "\"Actua como un terapeuta ocupacional y pedagogo de memoria cotidiana para personas mayores (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un entrenador de memoria practica:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. 5 Niveles de Memoria: Sensorial, inmediata (objetos), procedural (cocinar/conducir), episodica (recuerdos) y prospectiva (citas).",
            "2. 'El Rincon de las Cosas Fijas': metodo interactivo para no perder jamas llaves, gafas, cartera y movil en casa.",
            "3. Tecnicas sencillas de asociacion: trucos visuales para recordar nombres de personas nuevas y caras sin pasar verguenza.",
            "4. Semáforo de Tranquilidad Mental: distincion clara y tranquilizadora entre despistes normales de la edad y senales clinicas reales.",
            "5. Guia para usar la voz de Gemini y el movil como secretaria para recordar la toma de pastillas y citas medicas.",
            "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
        ],
        'questions': [
            "Pregunta 1 • Despistes Benignos vs. Senales Reales: \"Gemini, si entro a una habitacion y olvido a que iba, o si tardo un minuto en recordar el nombre de un actor famoso, ¿por que esto es un fallo benigno de recuperacion y no un sintoma de Alzheimer?\"",
            "Pregunta 2 • El Poder del Orden y la Rutina en Casa: \"Gemini, ¿como ayuda 'la ley del sitio fijo' (tener una bandeja unica para llaves y cartera junto a la puerta) a liberar la mente de ansiedad y evitar extravios cotidianos?\"",
            "Pregunta 3 • La Memoria Emocional y los Recuerdos de Infancia: \"Gemini, ¿por que las personas mayores recordamos con tanta nitidez canciones, olores y anecdotas de nuestra juventud de hace 50 anos mientras olvidamos que comimos ayer?\""
        ],
        'fuente1': "- Enfoque en Terapia Ocupacional y Neuropsicologia: Basado en los programas de estimulacion de la memoria cotidiana de la Fundacion Alzheimer Espana y estudios del Centro Alzheimer Fundacion Reina Sofia."
    },
    {
        'session_num': 14,
        'tag_code': 'NIV-014',
        'filename': '9. NIV-014_Los_6_Niveles_de_Toma_de_Decisiones_y_Fi.pdf',
        'title': 'Los 6 Niveles de Toma de Decisiones y Filtro de Sesgos (+65)',
        'app_name_upper': 'LA BALANZA DE DECISIONES SERENAS Y SESGOS',
        'debate_topic_upper': 'TOMA DE DECISIONES Y CRITERIO MADURO',
        'step2_desc': 'Coloca en la balanza digital pros, contras y emociones ante una decision importante (vivienda, ayuda a hijos, inversiones), filtra el miedo y plantea a Gemini las 3 preguntas clave.',
        'sim_file': 'SIMULADOR_TOMA_DECISIONES_SESGOS_SENIORS.html',
        'sim_title': 'Filtro de Sesgos y Decisiones (+65)',
        'prompt_lines': [
            "\"Actua como un consejero de familia y mediador etico para personas mayores (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) una balanza de toma de decisiones serena:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. Balanza interactiva: ponderacion visual de factores economicos, de salud, familiares y de paz interior ante grandes cambios.",
            "2. 6 Niveles de Toma de Decisiones: desde el impulso temeroso y la presion familiar hasta el juicio sereno y la perspectiva madura.",
            "3. Filtro de los 4 Sesgos habituales: aversion al cambio de casa, culpa por decir no, exceso de confianza y efecto ancla en el pasado.",
            "4. Simulador de dilemas reales: ayudar con avales a un hijo, adaptar la banera a plato de ducha o vender el coche familiar.",
            "5. Informe final de decision templada con consejos para mantener una conversacion familiar constructiva y sin fricciones.",
            "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
        ],
        'questions': [
            "Pregunta 1 • El Dilema de Ayudar a los Hijos con Dinero: \"Gemini, muchos jubilados nos sentimos presionados para avalar o entregar nuestros ahorros a los hijos en apuros. ¿Como podemos ayudarlos con carino sin poner en riesgo nuestra subsistencia?\"",
            "Pregunta 2 • El Duelo por Vender la Casa Familiar: \"Gemini, ¿por que cambiar un piso grande lleno de recuerdos por una vivienda accesible con ascensor y plato de ducha genera tanta resistencia emocional y como se puede vivir con ilusion?\"",
            "Pregunta 3 • Decidir Cuando Dejar de Conducir: \"Gemini, ¿como debe afrontar una persona mayor y su familia el momento de colgar las llaves del coche con serenidad y dignidad, buscando alternativas de transporte seguras?\""
        ],
        'fuente1': "- Enfoque en Psicologia de la Decision y Mediacion Familiar: Basado en las teorias de racionalidad limitada de Daniel Kahneman y modelos de mediacion intergeneracional para la resolucion pacifica de conflictos."
    },
    {
        'session_num': 15,
        'tag_code': 'NIV-015',
        'filename': '9. NIV-015_Los_5_Niveles_de_Resiliencia_Emocional_y.pdf',
        'title': 'Los 5 Niveles de Resiliencia Emocional y Paz Interior (+65)',
        'app_name_upper': 'EL TERMOMETRO DE RESILIENCIA Y PAZ INTERIOR',
        'debate_topic_upper': 'BIENESTAR EMOCIONAL Y RESILIENCIA SENIOR',
        'step2_desc': 'Mueve el termometro del animo, completa el diario de agradecimiento en 3 clics, descubre tus fuentes de fortaleza y plantea a Gemini las 3 preguntas de sabiduria y serenidad.',
        'sim_file': 'SIMULADOR_RESILIENCIA_SALUD_MENTAL_SENIORS.html',
        'sim_title': 'Simulador Resiliencia y Paz Interior (+65)',
        'prompt_lines': [
            "\"Actua como un psicologo humanista experto en bienestar emocional y etapa de la madurez (+65).",
            "Disena y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un termometro de resiliencia:",
            "Muestra directamente el simulador en funcionamiento sin obligarme a revisar el codigo fuente. Requisitos:",
            "1. 5 Niveles de Fortaleza: Desanimo o soledad, aceptacion serena, conexion social, sentido de utilidad vital y plenitud interior.",
            "2. Diario de Agradecimiento rapido: casillas para anotar 3 cosas buenas del dia (un paseo agradable, una llamada, una comida rica).",
            "3. Caja de Herramientas para dias grises: pautas de accion inmediata cuando el desanimo, la nostalgia o la soledad aprietan.",
            "4. Directorio de conexion humana: telefonos gratuitos de acompanamiento de la Cruz Roja, centros de dia y clubes de mayores.",
            "5. Filosofia estoica amigable: reflexiones breves sobre aceptar lo que no podemos cambiar y disfrutar plenamente del presente.",
            "Ergonomia Senior (+60): Tipografia grande (18.5px), botones de alto contraste, boton de reinicio y voz en espanol.\""
        ],
        'questions': [
            "Pregunta 1 • La Soledad No Deseada vs. la Soledad Serena: \"Gemini, ¿cual es la diferencia entre sentirse solo y disfrutar de la propia soledad en paz, y que pasos practicos puede dar una persona jubilada para tejer nuevas amistades en su barrio?\"",
            "Pregunta 2 • Aceptar las Limitaciones Fisicas sin Amargura: \"Gemini, cuando el cuerpo empieza a doler o a caminar mas despacio, ¿como podemos adaptar nuestro ritmo de vida con dignidad y buen humor sin sentir que la vida ha perdido valor?\"",
            "Pregunta 3 • El Gran Proposito de los Anos Dorados: \"Gemini, en culturas orientales y tradicionales se considera que la vejez es la cumbre de la sabiduria y el refugio espiritual de la familia: ¿cual es el gran proposito vital de una persona tras jubilarse?\""
        ],
        'fuente1': "- Enfoque en Psicogerontologia Positiva: Basado en el modelo de resiliencia de Viktor Frankl sobre el sentido de la vida y estudios de la Organizacion Mundial de la Salud (OMS) sobre bienestar psicologico en la decada del envejecimiento saludable."
    }
]

def update_all_niv_fiches():
    print("=================================================================")
    print("=== [INICIANDO ACTUALIZACION DEFINITIVA DE NIV SESIONES 05 A 15] ===")
    print("=================================================================")
    for item in NIV_DATA:
        render_niv_worksheet(item)
    print("=================================================================")
    print("🎉 ¡TODAS LAS 11 FICHAS NIV (S05 A S15) HAN SIDO GENERADAS AL 100%!")
    print("=================================================================")

if __name__ == '__main__':
    update_all_niv_fiches()
