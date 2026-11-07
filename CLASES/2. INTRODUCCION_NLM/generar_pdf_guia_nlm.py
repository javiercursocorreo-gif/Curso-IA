#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_pdf_guia_nlm.py
Genera 'GUIA_COMPLETA_ALUMNO_NOTEBOOKLM_Y_PRACTICAS.pdf' en formato profesional,
vistoso y con bloques de color, unificando teoría de pantalla y taller práctico sistemático.
100% Python nativo estándar (sin ReportLab, sin pip, sin dependencias externas).
"""

import os
import sys
import datetime

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_OUTPUT = os.path.join(OUTPUT_DIR, "GUIA_COMPLETA_ALUMNO_NOTEBOOKLM_Y_PRACTICAS.pdf")

def escape_pdf_text(text):
    text = str(text)
    text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    replacements = {
        'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
        'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
        'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
        '«': '<<', '»': '>>', '•': '-', '—': '-', '–': '-',
        'º': 'o', 'ª': 'a', '¿': '\xbf', '¡': '\xa1',
        '“': '"', '”': '"', '’': "'", '‘': "'"
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

class ColorfulPDFWriter:
    def __init__(self, page_width=595.28, page_height=841.89): # A4 standard
        self.w = page_width
        self.h = page_height
        self.pages = []
        self.current_stream = []

    def start_page(self):
        self.current_stream = []

    def end_page(self):
        self.pages.append("".join(self.current_stream))
        self.current_stream = []

    def set_fill_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} rg\n")

    def set_stroke_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} RG\n")

    def set_line_width(self, width):
        self.current_stream.append(f"{width:.2f} w\n")

    def rect(self, x, y, width, height, fill=True, stroke=True):
        op = "B" if (fill and stroke) else ("f" if fill else "S")
        self.current_stream.append(f"{x:.2f} {y:.2f} {width:.2f} {height:.2f} re {op}\n")

    def line(self, x1, y1, x2, y2):
        self.current_stream.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S\n")

    def draw_text(self, x, y, text, font="F1", size=10, r=0, g=0, b=0):
        self.set_fill_color(r, g, b)
        escaped = escape_pdf_text(text)
        self.current_stream.append(f"BT /{font} {size} Tf {x:.2f} {y:.2f} Td ({escaped}) Tj ET\n")

    def draw_header_footer(self, page_num, total_pages):
        # Header (página > 1)
        if page_num > 1:
            self.set_fill_color(0.08, 0.15, 0.35)
            self.rect(36, self.h - 22, self.w - 72, 2.5, fill=True, stroke=False)
            self.draw_text(36, self.h - 34, "MONOGRÁFICO 2: GUÍA VISUAL COMPLETA Y TALLER NOTEBOOKLM", "F2", 8, 0.15, 0.35, 0.65)
            self.draw_text(self.w - 180, self.h - 34, "Curso de IA para Adultos Mayores", "F1", 8, 0.45, 0.5, 0.58)
            self.set_stroke_color(0.85, 0.88, 0.92)
            self.set_line_width(0.5)
            self.line(36, self.h - 38, self.w - 36, self.h - 38)

        # Footer (todas las páginas)
        self.set_stroke_color(0.85, 0.88, 0.92)
        self.set_line_width(0.5)
        self.line(36, 32, self.w - 36, 32)
        self.draw_text(36, 20, "Guía Didáctica Oficial • Aprendizaje Activo con IA para Seniors, Hijos y Nietos", "F1", 7.5, 0.45, 0.5, 0.58)
        self.draw_text(self.w - 105, 20, f"Página {page_num} de {total_pages}", "F2", 8, 0.15, 0.35, 0.65)

    def write_to_file(self, filename):
        f1_idx, f2_idx, f3_idx = 3, 4, 5
        page_obj_indices = []
        content_obj_indices = []
        cur_obj_idx = 6

        for _ in self.pages:
            page_obj_indices.append(cur_obj_idx)
            cur_obj_idx += 1
            content_obj_indices.append(cur_obj_idx)
            cur_obj_idx += 1

        kids_str = " ".join([f"{idx} 0 R" for idx in page_obj_indices])
        pages_dict = f"<< /Type /Pages /Kids [{kids_str}] /Count {len(self.pages)} >>".encode('ascii')

        all_objs = [
            b"<< /Type /Catalog /Pages 2 0 R >>",
            pages_dict,
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>"
        ]

        for p_idx, c_idx in zip(page_obj_indices, content_obj_indices):
            p_obj = f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.w} {self.h}] /Contents {c_idx} 0 R /Resources << /Font << /F1 {f1_idx} 0 R /F2 {f2_idx} 0 R /F3 {f3_idx} 0 R >> >> >>".encode('ascii')
            p_stream = self.pages[(p_idx - 6) // 2]
            c_bytes = p_stream.encode('latin-1', errors='replace')
            c_obj = f"<< /Length {len(c_bytes)} >>\nstream\n".encode('ascii') + c_bytes + b"\nendstream"
            all_objs.append(p_obj)
            all_objs.append(c_obj)

        with open(filename, 'wb') as f:
            f.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
            xref_positions = [0]
            pos = f.tell()
            for idx, obj_bytes in enumerate(all_objs, start=1):
                xref_positions.append(pos)
                header = f"{idx} 0 obj\n".encode('ascii')
                footer = b"\nendobj\n"
                f.write(header + obj_bytes + footer)
                pos = f.tell()

            xref_start = pos
            f.write(f"xref\n0 {len(all_objs) + 1}\n".encode('ascii'))
            f.write(b"0000000000 65535 f \n")
            for p in xref_positions[1:]:
                f.write(f"{p:010d} 00000 n \n".encode('ascii'))

            trailer = f"trailer\n<< /Size {len(all_objs) + 1} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF\n".encode('ascii')
            f.write(trailer)

def construir_guia_pdf():
    # Generamos primero las páginas para calcular el total
    writer = ColorfulPDFWriter()

    # Estructura del contenido dividida en páginas lógicas para que quede impecable
    # PÁGINA 1: Portada, Qué es NotebookLM y El Mapa de las 3 Zonas
    writer.start_page()
    y = writer.h - 40

    # Banda azul superior
    writer.set_fill_color(0.12, 0.25, 0.55)
    writer.rect(36, y, writer.w - 72, 5, fill=True, stroke=False)
    y -= 18

    # Badge de cabecera
    writer.set_fill_color(0.90, 0.94, 0.99)
    writer.set_stroke_color(0.70, 0.82, 0.95)
    writer.rect(36, y - 10, 310, 15, fill=True, stroke=True)
    writer.draw_text(42, y - 7, "CURSO DE IA PARA PERSONAS MAYORES • MONOGRÁFICO 2", "F2", 7.5, 0.12, 0.35, 0.70)
    y -= 26

    # Título Principal
    writer.draw_text(36, y, "MANUAL VISUAL COMPLETO Y TALLER: NOTEBOOKLM", "F2", 15.5, 0.10, 0.18, 0.38)
    y -= 15
    writer.draw_text(36, y, "Tu Archivador Privado, Cuaderno Inteligente y Estudio Activo para Hijos y Nietos", "F3", 9.5, 0.35, 0.40, 0.48)
    y -= 14
    writer.set_stroke_color(0.85, 0.88, 0.92)
    writer.line(36, y, writer.w - 36, y)
    y -= 18

    # BLOQUE 1: De lo público a lo privado
    writer.set_fill_color(0.15, 0.35, 0.65) # Cabecera azul
    writer.rect(36, y - 4, writer.w - 72, 17, fill=True, stroke=False)
    writer.draw_text(44, y + 1, "1. EL GRAN CAMBIO: DE LO PÚBLICO (BUSCADORES) A TU ARCHIVADOR PRIVADO", "F2", 8.8, 1, 1, 1)
    y -= 20

    # Tabla comparativa
    filas_comp = [
        ("Concepto", "Gemini Público / ChatGPT Abierto", "Gemini Notebook (NotebookLM)"),
        ("Origen de datos", "Rastrea todo internet y webs no verificadas.", "SOLO lee tus documentos y papeles subidos."),
        ("Riesgo de invención", "Puede tener 'alucinaciones' o inventar datos.", "Cero alucinaciones: se ciñe a tus fuentes."),
        ("Regla de la Verdad", "Rellena lagunas con suposiciones.", "Si no figura, responde: 'No aparece en las fuentes'."),
        ("Privacidad", "Modelos públicos abiertos.", "Privado y cerrado: no entrena modelos con tus datos.")
    ]

    col_w = [105, 205, 213]
    for idx_f, (c1, c2, c3) in enumerate(filas_comp):
        bg = (0.94, 0.96, 0.99) if idx_f == 0 else ((0.98, 0.98, 0.99) if idx_f % 2 == 1 else (1, 1, 1))
        writer.set_fill_color(bg[0], bg[1], bg[2])
        writer.set_stroke_color(0.85, 0.88, 0.92)
        writer.rect(36, y - 9, writer.w - 72, 13, fill=True, stroke=True)

        fnt = "F2" if idx_f == 0 else "F1"
        col_txt = (0.12, 0.25, 0.55) if idx_f == 0 else (0.15, 0.18, 0.22)
        writer.draw_text(40, y - 6, c1, "F2" if idx_f > 0 else fnt, 7.8, col_txt[0], col_txt[1], col_txt[2])
        writer.draw_text(145, y - 6, c2, fnt, 7.8, 0.40, 0.45, 0.50 if idx_f > 0 else col_txt[2])
        writer.draw_text(350, y - 6, c3, "F2" if idx_f > 0 else fnt, 7.8, 0.10, 0.45, 0.30 if idx_f > 0 else col_txt[2])
        y -= 13

    y -= 10
    # Callout acceso
    writer.set_fill_color(0.92, 0.97, 0.94)
    writer.set_stroke_color(0.35, 0.70, 0.50)
    writer.rect(36, y - 18, writer.w - 72, 22, fill=True, stroke=True)
    writer.draw_text(44, y - 6, "ACCESO DIRECTO:", "F2", 8, 0.08, 0.45, 0.28)
    writer.draw_text(130, y - 6, "Entra en notebooklm.google.com con tu cuenta Gmail. Cero contraseñas nuevas.", "F1", 8, 0.15, 0.20, 0.25)
    writer.draw_text(44, y - 15, "CAPACIDAD ENORME: Hasta 50 fuentes por cuaderno y 500.000 palabras por fuente (PDF, Word, TXT, YouTube, Audio).", "F3", 7.5, 0.30, 0.35, 0.40)
    y -= 30

    # BLOQUE 2: Las 3 Zonas de la Pantalla Real
    writer.set_fill_color(0.30, 0.20, 0.55) # Cabecera morada
    writer.rect(36, y - 4, writer.w - 72, 17, fill=True, stroke=False)
    writer.draw_text(44, y + 1, "2. EL MAPA DE LA PANTALLA REAL: LAS TRES COLUMNAS PRINCIPALES", "F2", 8.8, 1, 1, 1)
    y -= 22

    # 3 Cajas horizontales representativas
    zonas = [
        ("ZONA 1 (IZQUIERDA): EL ARCHIVADOR", [
            "Boton '+ Añadir fuentes' (sube PDF, Word, TXT, MP3, YouTube, Docs).",
            "Casillas [v] para marcar o desmarcar cada documento.",
            "Regla de Aislamiento: la IA SOLO lee las fuentes con casilla marcada.",
            "Permite cruzar datos o analizar un solo papel sin contaminar."
        ], (0.15, 0.35, 0.65), (0.93, 0.96, 0.99)),
        ("ZONA 2 (CENTRAL): CONVERSACIÓN Y RESUMEN", [
            "Guia del Cuaderno: resumen estructurado automatico nada mas subir fuentes.",
            "Chips de preguntas sugeridas: un clic y arranca el analisis.",
            "Campo de Pregunta (Prompt): habla normal como a un bibliotecario.",
            "Citas Exactas [1]: haz clic y subraya en amarillo el documento original."
        ], (0.08, 0.48, 0.35), (0.92, 0.97, 0.94)),
        ("ZONA 3 (DERECHA): EL PANEL STUDIO (FÁBRICA)", [
            "Icono Chincheta (Pin): guarda respuestas utiles en el corcho permanente.",
            "9 Botones automaticos en 1 clic (FAQ, Guia estudio, Cronologia...).",
            "Presentaciones Diapositiva por Diapositiva con boton 'Revisar' en vivo.",
            "Audio Overview: podcast a dos voces debatiendo amistosamente tus papeles."
        ], (0.75, 0.42, 0.10), (0.99, 0.96, 0.91))
    ]

    for titulo_z, lineas_z, col_borde, col_fondo in zonas:
        h_box = len(lineas_z) * 11 + 20
        writer.set_fill_color(col_fondo[0], col_fondo[1], col_fondo[2])
        writer.set_stroke_color(col_borde[0], col_borde[1], col_borde[2])
        writer.rect(36, y - h_box + 8, writer.w - 72, h_box, fill=True, stroke=True)

        writer.draw_text(44, y - 2, titulo_z, "F2", 8.2, col_borde[0], col_borde[1], col_borde[2])
        ty = y - 14
        for lz in lineas_z:
            writer.draw_text(52, ty, "- " + lz, "F1", 7.5, 0.20, 0.22, 0.26)
            ty -= 10.5
        y = y - h_box - 4

    writer.end_page()

    # PÁGINA 2: Caso de Estudio (La Luna 1969), Fase 1 y Fase 2 del Taller
    writer.start_page()
    y = writer.h - 50

    writer.set_fill_color(0.08, 0.48, 0.35) # Verde esmeralda
    writer.rect(36, y - 4, writer.w - 72, 17, fill=True, stroke=False)
    writer.draw_text(44, y + 1, "3. CASO DE ESTUDIO DEL TALLER: LA LLEGADA A LA LUNA (20 DE JULIO DE 1969)", "F2", 8.8, 1, 1, 1)
    y -= 22

    # Fuentes del taller
    fuentes_info = [
        ("FUENTE 1 (Texto TXT)", "EJEMPLO_A_FUENTE_TEXTO_RECUERDO_LUNA_1969.txt", "Emocion humana: Noche calurosa en Madrid, tele Telefunken en B/N, voz de Hermida y lagrimas del abuelo (carro de mulas)."),
        ("FUENTE 2 (Documento PDF)", "EJEMPLO_A_FUENTE_HISTORIA_APOLO_11.pdf", "Rigor cientifico: 400.000 ingenieros, Saturno V, ordenador AGC con solo 4 KB de RAM y estacion de Fresnedillas (Madrid)."),
        ("FUENTE 3 (Video YouTube)", "https://www.youtube.com/watch?v=Wbh9VAuZcUM", "Conmemoracion oficial: Reportaje Euronews (50 años), declaraciones de historiadores y futuras misiones Artemis.")
    ]

    for tipo, nombre, desc in fuentes_info:
        writer.set_fill_color(0.97, 0.98, 0.99)
        writer.set_stroke_color(0.85, 0.88, 0.92)
        writer.rect(36, y - 24, writer.w - 72, 28, fill=True, stroke=True)

        writer.draw_text(44, y - 4, tipo, "F2", 8, 0.15, 0.35, 0.65)
        writer.draw_text(160, y - 4, nombre, "F3", 7.5, 0.40, 0.45, 0.50)
        lines_d = wrap_text(desc, max_chars=88)
        ty = y - 14
        for ld in lines_d:
            writer.draw_text(44, ty, ld, "F1", 7.5, 0.20, 0.25, 0.30)
            ty -= 9.5
        y -= 33

    y -= 6
    # FASE 1: Zona Central Paso a Paso
    writer.set_fill_color(0.15, 0.35, 0.65)
    writer.rect(36, y - 4, writer.w - 72, 17, fill=True, stroke=False)
    writer.draw_text(44, y + 1, "4. TALLER PRÁCTICO: FASE 1 (ZONA CENTRAL, RESÚMENES, CITAS Y CHINCHETA)", "F2", 8.8, 1, 1, 1)
    y -= 22

    pasos_fase1 = [
        ("1.1. Resumen Automatico Inicial", "Con las 3 fuentes marcadas [v], mira al centro: NotebookLM ha creado la 'Guia del cuaderno' sola sin teclear nada, identificando el tema comun y sugiriendo preguntas."),
        ("1.2. Practica de Aislamiento con Casillas", "Desmarca PDF y YouTube. Con solo TXT escribe: 'Resume en 3 lineas los recuerdos familiares y la emocion de la noche'. Desmarca TXT y activa solo PDF: 'Resume en 3 puntos tecnicos el Apolo 11'."),
        ("1.3. Busqueda Quirurgica y Citas [1]", "Marca las 3 fuentes [v]. Pregunta: '¿Que marca era la television familiar y cuanta RAM tenia la nave?'. Haz clic en la cita [1] o [2] al final: la pantalla salta al texto original y subraya Telefunken y 4 KB en amarillo fosforito."),
        ("1.4. Fijar como Nota Permanente (Pin)", "Pasa el raton sobre la respuesta comparativa y pulsa la Chincheta (Pin). La respuesta vuela al panel derecho (Studio) y se queda anclada para siempre, sin borrarse nunca.")
    ]

    for num_p, desc_p in pasos_fase1:
        lines_p = wrap_text(desc_p, max_chars=86)
        h_p = len(lines_p) * 10 + 16
        writer.set_fill_color(1, 1, 1)
        writer.set_stroke_color(0.85, 0.88, 0.92)
        writer.rect(36, y - h_p + 8, writer.w - 72, h_p, fill=True, stroke=True)

        writer.draw_text(44, y - 2, num_p, "F2", 8, 0.12, 0.25, 0.55)
        ty = y - 12
        for lp in lines_p:
            writer.draw_text(44, ty, lp, "F1", 7.5, 0.22, 0.25, 0.30)
            ty -= 9.5
        y = y - h_p - 3

    y -= 4
    # FASE 2: Studio y los 9 botones automáticos
    writer.set_fill_color(0.75, 0.42, 0.10)
    writer.rect(36, y - 4, writer.w - 72, 17, fill=True, stroke=False)
    writer.draw_text(44, y + 1, "5. TALLER PRÁCTICO: FASE 2 (PANEL STUDIO Y LOS 9 BOTONES AUTOMÁTICOS)", "F2", 8.8, 1, 1, 1)
    y -= 18

    writer.draw_text(40, y, "Paso clave: Desmarca TXT y PDF. Deja marcado ÚNICAMENTE el video de YouTube [v].", "F2", 8, 0.65, 0.35, 0.05)
    y -= 12

    botones_studio = [
        ("1. Preguntas Frecuentes (FAQ)", "Cuestionario con las dudas clave resueltas a partir del video."),
        ("2. Guia de Estudio", "Temario educativo con preguntas de repaso y conceptos clave."),
        ("3. Cronologia / Linea de Tiempo", "Rastrea y ordena todas las fechas mencionadas cronologicamente."),
        ("4. Documento Informativo (Briefing)", "Informe formal y ejecutivo listo para imprimir o enviar por email."),
        ("5. Puntos Clave / Ideas Destacadas", "Decalogo con las perlas de informacion mas importantes en viñetas."),
        ("6. Audio Overview (Podcast)", "Tertulia a dos voces amena y cercana explicando tus documentos.")
    ]

    for b_tit, b_desc in botones_studio:
        writer.draw_text(44, y, "[  ] " + b_tit + ":", "F2", 7.5, 0.15, 0.20, 0.25)
        writer.draw_text(210, y, b_desc, "F1", 7.5, 0.40, 0.45, 0.50)
        y -= 11.5

    writer.end_page()

    # PÁGINA 3: Presentación revisable, Resumen de Vídeo, Estudio para Hijos/Nietos y Checklist
    writer.start_page()
    y = writer.h - 50

    # FASE 3: Presentación con Estilo y Revisión en Vivo
    writer.set_fill_color(0.15, 0.35, 0.65)
    writer.rect(36, y - 4, writer.w - 72, 17, fill=True, stroke=False)
    writer.draw_text(44, y + 1, "6. PRESENTACIÓN CON ESTILO VISUAL Y REVISIÓN «SLIDE POR SLIDE» EN VIVO", "F2", 8.8, 1, 1, 1)
    y -= 20

    pasos_pres = [
        ("Paso 3.1: Seleccion de Fuentes", "Marca TXT [v] + PDF [v] (deja desmarcado el video)."),
        ("Paso 3.2: Boton Presentacion + Prompt de Estilo", "En Studio pulsa 'Presentacion'. En la casilla escribe: 'Crea una presentacion con estilo sobrio, elegante y cronica documental. Paleta limpia espacial (azul marino profundo y blanco de alto contraste), letra grande para personas mayores, equilibrando rigor NASA y emocion del salon en Madrid, evitando ilustraciones infantiles.'"),
        ("Paso 3.3: La Clave de la Revision en Vivo", "Abre la presentacion resultante. Con las flechas hojeas slide por slide. Pulsa el boton 'Revisar' (o Ajustar): puedes pedir ajustes sobre la marcha en clase. El control pedagogico siempre es tuyo.")
    ]

    for tit_pr, desc_pr in pasos_pres:
        lines_pr = wrap_text(desc_pr, max_chars=86)
        h_pr = len(lines_pr) * 10 + 15
        writer.set_fill_color(1, 1, 1)
        writer.set_stroke_color(0.85, 0.88, 0.92)
        writer.rect(36, y - h_pr + 8, writer.w - 72, h_pr, fill=True, stroke=True)

        writer.draw_text(44, y - 2, tit_pr, "F2", 8, 0.12, 0.25, 0.55)
        ty = y - 11
        for lpr in lines_pr:
            writer.draw_text(44, ty, lpr, "F1", 7.5, 0.20, 0.22, 0.26)
            ty -= 9.5
        y = y - h_pr - 3

    y -= 4
    # FASE 4: Gran Resumen de Vídeo (3 fuentes juntas)
    writer.set_fill_color(0.65, 0.20, 0.25) # Rojo cereza
    writer.rect(36, y - 4, writer.w - 72, 17, fill=True, stroke=False)
    writer.draw_text(44, y + 1, "7. EL GRAN RESUMEN DE VÍDEO (FUSIÓN DE LAS 3 FUENTES JUNTAS)", "F2", 8.8, 1, 1, 1)
    y -= 20

    writer.set_fill_color(0.99, 0.95, 0.95)
    writer.set_stroke_color(0.85, 0.70, 0.70)
    writer.rect(36, y - 22, writer.w - 72, 26, fill=True, stroke=True)
    writer.draw_text(44, y - 4, "PASO: Marca las 3 fuentes a la vez [v] (TXT + PDF + YouTube). Pulsa 'Resumen de video' en Studio.", "F2", 8, 0.60, 0.15, 0.20)
    writer.draw_text(44, y - 13, "NotebookLM funde la vivencia del salon madrileño, el Saturno V y la conmemoracion de Euronews en un video", "F1", 7.5, 0.25, 0.25, 0.25)
    writer.draw_text(44, y - 21, "resumen multimedia completo y moderno, listo para proyectar y comentar en clase sin escribir prompts.", "F1", 7.5, 0.25, 0.25, 0.25)
    y -= 32

    # FASE 5: Estudio activo para Hijos y Nietos
    writer.set_fill_color(0.35, 0.20, 0.60) # Morado didáctico
    writer.rect(36, y - 4, writer.w - 72, 17, fill=True, stroke=False)
    writer.draw_text(44, y + 1, "8. NOTEBOOKLM COMO HERRAMIENTA DE ESTUDIO ACTIVO PARA HIJOS Y NIETOS", "F2", 8.8, 1, 1, 1)
    y -= 20

    items_estudio = [
        ("Tarjetas de Repaso (Flashcards)", "Tarjetas interactivas con preguntas por delante que se dan la vuelta con la respuesta al hacer clic. Ideales para memorizar fechas, formulas o vocabulario de idiomas de forma amena."),
        ("Mapas Conceptuales y Esquemas", "Pide a la IA que estructure temas densos de 30 paginas en un mapa visual con causas, hechos y consecuencias conectadas."),
        ("Grabadora Movil de Bolsillo", "En el telefono movil puedes grabar hasta 1 hora continua (incluso con la pantalla apagada) para registrar consultas medicas, clases o dictar tus memorias familiares; al parar, se transcribe y archiva sola.")
    ]

    for tit_e, desc_e in items_estudio:
        lines_e = wrap_text(desc_e, max_chars=86)
        h_e = len(lines_e) * 9.5 + 15
        writer.set_fill_color(0.97, 0.95, 0.99)
        writer.set_stroke_color(0.80, 0.70, 0.90)
        writer.rect(36, y - h_e + 8, writer.w - 72, h_e, fill=True, stroke=True)

        writer.draw_text(44, y - 2, tit_e, "F2", 8, 0.35, 0.20, 0.60)
        ty = y - 11
        for le in lines_e:
            writer.draw_text(44, ty, le, "F1", 7.5, 0.20, 0.22, 0.26)
            ty -= 9.5
        y = y - h_e - 3

    y -= 4
    # CHECKLIST DE AUTOEVALUACIÓN DEL ALUMNO
    writer.set_fill_color(0.12, 0.23, 0.54)
    writer.rect(36, y - 4, writer.w - 72, 16, fill=True, stroke=False)
    writer.draw_text(44, y + 1, "9. CHECKLIST DE AUTOEVALUACIÓN Y COMPETENCIAS DEL ALUMNO", "F2", 8.5, 1, 1, 1)
    y -= 18

    checklist = [
        ("Paso 1", "Se entrar a notebooklm.google.com con mi cuenta Gmail y crear un nuevo cuaderno."),
        ("Paso 2", "Se subir archivos TXT, PDF y enlaces de YouTube mediante el boton '+ Añadir fuentes'."),
        ("Paso 3", "Se localizar el Resumen Central y utilizar los chips sugeridos para arrancar la conversacion."),
        ("Paso 4", "Se usar las casillas [v] para aislar una sola fuente y analizarla por separado sin mezclar."),
        ("Paso 5", "Se hacer preguntas en el chat y pulsar las citas [1] para verificar el subrayado en amarillo."),
        ("Paso 6", "Se fijar cualquier respuesta util como Nota permanente en Studio con la chincheta (Pin)."),
        ("Paso 7", "He probado los 9 botones de Studio con YouTube (FAQ, Guia, Cronologia, Resumen)."),
        ("Paso 8", "Se generar la Presentacion sobria (TXT+PDF) y utilizar el boton 'Revisar' en vivo."),
        ("Paso 9", "Se crear el Resumen de Video con las 3 fuentes y usar NLM para ayudar a estudiar a mi familia.")
    ]

    for paso_n, paso_txt in checklist:
        writer.draw_text(40, y, f"[  ] {paso_n}:", "F2", 7.2, 0.12, 0.25, 0.55)
        writer.draw_text(115, y, paso_txt, "F1", 7.2, 0.20, 0.25, 0.30)
        writer.draw_text(writer.w - 95, y, "[  ] SI  /  [  ] DUDAS", "F2", 7.0, 0.45, 0.50, 0.55)
        y -= 11

    writer.end_page()

    # Escribir encabezados y números de página reales (3 páginas en total)
    total_p = len(writer.pages)
    for p_num in range(1, total_p + 1):
        # Inyectar pie y encabezado en el stream de la página
        pass

    # Aplicar draw_header_footer en cada página
    for i in range(len(writer.pages)):
        # Añadimos al final del stream de cada página el pie
        writer.pages[i] += f"\nBT /F1 7.5 Tf 36 20 Td (Guia Didactica Oficial - Aprendizaje Activo con IA para Seniors, Hijos y Nietos) Tj ET\n"
        writer.pages[i] += f"BT /F2 8 Tf {writer.w - 110} 20 Td (Pagina {i+1} de {total_p}) Tj ET\n"
        writer.pages[i] += f"0.850 0.880 0.920 RG\n0.50 w\n36.00 32.00 m {writer.w - 36:.2f} 32.00 l S\n"
        if i > 0:
            writer.pages[i] += f"BT /F2 8 Tf 36 {writer.h - 32:.2f} Td (MONOGRAFICO 2: GUIA VISUAL COMPLETA Y TALLER NOTEBOOKLM) Tj ET\n"
            writer.pages[i] += f"BT /F1 8 Tf {writer.w - 180} {writer.h - 32:.2f} Td (Curso de IA para Adultos Mayores) Tj ET\n"
            writer.pages[i] += f"0.850 0.880 0.920 RG\n0.50 w\n36.00 {writer.h - 36:.2f} m {writer.w - 36:.2f} {writer.h - 36:.2f} l S\n"

    writer.write_to_file(PDF_OUTPUT)
    print(f"✅ PDF generado exitosamente: {PDF_OUTPUT} ({total_p} páginas)")

if __name__ == "__main__":
    construir_guia_pdf()
