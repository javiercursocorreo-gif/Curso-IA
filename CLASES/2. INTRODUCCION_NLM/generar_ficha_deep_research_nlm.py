#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_ficha_deep_research_nlm.py
Genera la ficha pedagógica oficial:
FICHA_TALLER_DEEP_RESEARCH_AUDITORIA_NOTEBOOKLM.pdf (2 páginas A4).
100% Python nativo estándar (sin dependencias externas).
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(OUTPUT_DIR, "FICHA_TALLER_DEEP_RESEARCH_AUDITORIA_NOTEBOOKLM.pdf")


def escape_pdf_text(text):
    text = str(text)
    replacements = {
        'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
        'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
        'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
        '«': '<<', '»': '>>', '•': '-', '—': '-', '–': '-',
        'º': 'o', 'ª': 'a', '¿': '\xbf', '¡': '\xa1',
        '“': '"', '”': '"', '’': "'", '‘': "'", '→': '->'
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    clean_chars = [ch if ord(ch) < 256 else ' ' for ch in text]
    text = ''.join(clean_chars)
    return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')


def wrap_text(text, max_chars=80):
    lines = []
    for p in str(text).split('\n'):
        p = p.strip()
        if not p:
            lines.append('')
            continue
        words = p.split(' ')
        cur, cur_len = [], 0
        for w in words:
            if not w:
                continue
            if cur_len + len(w) + (1 if cur else 0) <= max_chars:
                cur.append(w)
                cur_len += len(w) + (1 if cur[:-1] else 0)
            else:
                if cur:
                    lines.append(' '.join(cur))
                cur = [w]
                cur_len = len(w)
        if cur:
            lines.append(' '.join(cur))
    return lines or ['']


class RobustPDFWriter:
    def __init__(self, w=595, h=842):
        self.w = w
        self.h = h
        self.pages = []
        self.current_stream = []

    def new_page(self):
        if self.current_stream:
            self.pages.append("".join(self.current_stream))
            self.current_stream = []

    def set_fill_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} rg\n")

    def set_stroke_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} RG\n")

    def set_line_width(self, w):
        self.current_stream.append(f"{w:.2f} w\n")

    def rect(self, x, y, w, h, fill=True, stroke=True):
        op = "B\n" if (fill and stroke) else ("f\n" if fill else "S\n")
        self.current_stream.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}")

    def line(self, x1, y1, x2, y2):
        self.current_stream.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S\n")

    def draw_text(self, x, y, text, font="F1", size=9.5, r=0.1, g=0.1, b=0.1):
        escaped = escape_pdf_text(text)
        self.current_stream.append(
            f"BT /{font} {size:.1f} Tf {x:.2f} {y:.2f} Td {r:.3f} {g:.3f} {b:.3f} rg ({escaped}) Tj ET\n"
        )

    def save(self, filename):
        if self.current_stream:
            self.pages.append("".join(self.current_stream))
            self.current_stream = []

        objs = []
        # 1: Catalog, 2: Pages, 3: F1 Helvetica, 4: F2 Helvetica-Bold, 5: F3 Courier
        objs.append("1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")

        page_ids = []
        next_id = 6
        content_objs = []
        page_objs = []
        for stream_data in self.pages:
            content_id = next_id
            page_id = next_id + 1
            next_id += 2
            page_ids.append(f"{page_id} 0 R")
            stream_bytes = stream_data.encode("latin-1", errors="replace")
            content_objs.append(
                f"{content_id} 0 obj\n<< /Length {len(stream_bytes)} >>\nstream\n{stream_data}endstream\nendobj\n"
            )
            page_objs.append(
                f"{page_id} 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.w} {self.h}] "
                f"/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> /Contents {content_id} 0 R >>\nendobj\n"
            )

        objs.append(f"2 0 obj\n<< /Type /Pages /Kids [{' '.join(page_ids)}] /Count {len(page_ids)} >>\nendobj\n")
        objs.append("3 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>\nendobj\n")
        objs.append("4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>\nendobj\n")
        objs.append("5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>\nendobj\n")

        for c_obj, p_obj in zip(content_objs, page_objs):
            objs.append(c_obj)
            objs.append(p_obj)

        pdf = ["%PDF-1.4\n"]
        offsets = [0]
        for o in objs:
            offsets.append(sum(len(x.encode("latin-1", errors="replace")) for x in pdf))
            pdf.append(o)

        xref_pos = sum(len(x.encode("latin-1", errors="replace")) for x in pdf)
        pdf.append(f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n")
        for off in offsets[1:]:
            pdf.append(f"{off:010d} 00000 n \n")
        pdf.append(f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n")

        with open(filename, "wb") as f:
            f.write("".join(pdf).encode("latin-1", errors="replace"))


def draw_header(pdf, page_num, total_pages=2):
    # Barra superior azul marino sobria
    pdf.set_fill_color(0.08, 0.16, 0.34)
    pdf.set_stroke_color(0.08, 0.16, 0.34)
    pdf.rect(0, 772, 595, 70, fill=True, stroke=False)
    pdf.draw_text(40, 816, "CURSO DE INTELIGENCIA ARTIFICIAL (+65)  |  MONOGRÁFICO: NOTEBOOKLM AVANZADO", "F2", 8.5, 0.65, 0.80, 0.98)
    pdf.draw_text(40, 795, "Taller Práctico: Búsqueda Web, Deep Research y Prompt Auditor", "F2", 14.0, 1.0, 1.0, 1.0)
    pdf.draw_text(40, 780, "Cómo investigar en profundidad sin perder fuentes y obtener informes técnicos fiables", "F1", 9.0, 0.85, 0.90, 0.98)

    # Pie de página
    pdf.set_stroke_color(0.82, 0.85, 0.90)
    pdf.set_line_width(0.8)
    pdf.line(40, 38, 555, 38)
    pdf.draw_text(40, 24, "Material Didáctico Oficial - Aula de Tecnología Senior", "F1", 8.0, 0.45, 0.48, 0.55)
    pdf.draw_text(495, 24, f"Página {page_num} de {total_pages}", "F2", 8.0, 0.30, 0.35, 0.45)


def draw_section_box(pdf, y_top, title, subtitle):
    pdf.set_fill_color(0.92, 0.95, 0.99)
    pdf.set_stroke_color(0.22, 0.46, 0.80)
    pdf.set_line_width(1.2)
    pdf.rect(40, y_top - 38, 515, 38, fill=True, stroke=True)
    pdf.draw_text(50, y_top - 17, title, "F2", 12.5, 0.08, 0.22, 0.48)
    pdf.draw_text(50, y_top - 31, subtitle, "F1", 8.8, 0.25, 0.32, 0.42)
    return y_top - 50


def build_pdf():
    pdf = RobustPDFWriter()

    # ================= PÁGINA 1 =================
    draw_header(pdf, 1, 2)
    y = 755

    # Caja de Objetivo
    pdf.set_fill_color(0.96, 0.98, 0.95)
    pdf.set_stroke_color(0.22, 0.62, 0.35)
    pdf.set_line_width(1.0)
    pdf.rect(40, y - 58, 515, 58, fill=True, stroke=True)
    pdf.draw_text(50, y - 16, "IDEA CLAVE DEL EJERCICIO: NO EMPEZAR DESDE CERO", "F2", 10.0, 0.12, 0.42, 0.22)
    intro_lines = wrap_text(
        "Cuando investigamos un tema nuevo con NotebookLM, primero reunimos fuentes (búsqueda rápida + Deep Research) "
        "y después exprimimos ese cuaderno con un Prompt Auditor bien estructurado. Solo si falta detalle técnico "
        "añadimos una segunda búsqueda en inglés dentro del MISMO cuaderno, sin tirar el trabajo previo.",
        86
    )
    iy = y - 30
    for ln in intro_lines:
        pdf.draw_text(50, iy, ln, "F1", 9.0, 0.15, 0.20, 0.18)
        iy -= 12
    y -= 72

    # SECCIÓN 1
    y = draw_section_box(
        pdf, y,
        "1. PASO 1: BÚSQUEDA WEB + DEEP RESEARCH EN NOTEBOOKLM",
        "Cómo cargar las primeras fuentes reales antes de preguntar en el chat central"
    )
    step1_items = [
        ("1A. Búsqueda Web Inicial (10 fuentes):",
         "En el panel izquierdo (Fuentes -> Descubrir fuentes), escribe el tema principal. Por ejemplo: "
         "\"Arquitectura, Instalación y Gobernanza en Google Antigravity\". NotebookLM seleccionará unas 10 webs."),
        ("1B. Ampliación con Deep Research:",
         "Pulsa después la opción Deep Research para que NotebookLM investigue en profundidad y genere un informe "
         "completo añadido como fuente dentro del mismo cuaderno."),
        ("1C. Regla de Oro:",
         "No borres ni empieces un cuaderno nuevo antes de auditar lo que ya has recopilado con un buen prompt.")
    ]
    for label, body in step1_items:
        pdf.draw_text(44, y, label, "F2", 9.5, 0.10, 0.25, 0.50)
        y -= 13
        for ln in wrap_text(body, 84):
            pdf.draw_text(54, y, ln, "F1", 9.2, 0.15, 0.18, 0.22)
            y -= 12.5
        y -= 4

    # SECCIÓN 2: PROMPT AUDITOR
    y = draw_section_box(
        pdf, y - 4,
        "2. PASO 2: PROMPT MAESTRO AUDITOR (COPIAR Y PEGAR EN EL CHAT CENTRAL)",
        "Obliga a la IA a dar comandos, rutas y ejemplos reales con citas [1], [2]... evitando resúmenes vagos"
    )

    prompt_text = [
        "Actúa como un arquitecto de sistemas senior especializado en Google Antigravity IDE.",
        "Analiza EXCLUSIVAMENTE las fuentes y el informe de Deep Research de este cuaderno y",
        "extrae un informe técnico exhaustivo y accionable para mejorar una guía maestra.",
        "",
        "Organiza la respuesta exactamente en estos 6 bloques, incluyendo siempre comandos",
        "literales, rutas de archivos, nombres exactos de ajustes JSON y citas [1], [2]...:",
        "1. INSTALACIÓN, CUENTAS Y ENTORNOS: descarga, IDE vs CLI vs Desktop, cuotas, errores.",
        "2. ARQUITECTURA DE WORKSPACE Y CONTEXTO: carpetas, monorepo, límites y AGENTS.md.",
        "3. SKILLS, WORKFLOWS, SUBAGENTES Y HOOKS: .agents/skills/, subagentes y MCP.",
        "4. GOBERNANZA, SEGURIDAD Y SANDBOX: permisos, sandbox vs bypass, borradores y Git.",
        "5. ANTI-PATRONES Y PROBLEMAS REALES: bucles, consumo de cuota, caché y soluciones.",
        "6. NOVEDADES O FUNCIONES POCO CONOCIDAS: trucos prácticos que mejoren la fiabilidad.",
        "",
        "Regla estricta: No resumas con generalidades. Si un dato técnico concreto no aparece",
        "en las fuentes, indícalo explícitamente como 'No detallado en las fuentes'."
    ]

    box_h = len(prompt_text) * 12.5 + 22
    pdf.set_fill_color(0.95, 0.96, 0.98)
    pdf.set_stroke_color(0.35, 0.42, 0.55)
    pdf.set_line_width(0.9)
    pdf.rect(40, y - box_h, 515, box_h, fill=True, stroke=True)
    py = y - 16
    for pln in prompt_text:
        if pln:
            pdf.draw_text(50, py, pln, "F3", 8.2, 0.12, 0.15, 0.22)
        py -= 12.5

    # ================= PÁGINA 2 =================
    pdf.new_page()
    draw_header(pdf, 2, 2)
    y = 755

    # SECCIÓN 3
    y = draw_section_box(
        pdf, y,
        "3. PASO 3: CUÁNDO Y CÓMO HACER UNA 2ª BÚSQUEDA EN INGLÉS",
        "Si el Prompt Auditor responde muchas veces 'No detallado en las fuentes', ampliamos el MISMO cuaderno"
    )
    why_en = (
        "La documentación técnica oficial y las guías avanzadas suelen publicarse primero en inglés. "
        "Sin borrar el cuaderno actual, pulsa de nuevo 'Descubrir fuentes -> Deep Research' y pega esta frase:"
    )
    for ln in wrap_text(why_en, 86):
        pdf.draw_text(44, y, ln, "F1", 9.5, 0.15, 0.18, 0.22)
        y -= 13
    y -= 6

    # Caja frase en inglés
    pdf.set_fill_color(0.98, 0.96, 0.90)
    pdf.set_stroke_color(0.82, 0.55, 0.12)
    pdf.set_line_width(1.1)
    pdf.rect(40, y - 42, 515, 42, fill=True, stroke=True)
    pdf.draw_text(50, y - 16, "FRASE DE BÚSQUEDA EN INGLÉS (DEEP RESEARCH):", "F2", 8.5, 0.62, 0.36, 0.05)
    pdf.draw_text(50, y - 31, "Google Antigravity IDE official documentation AGENTS.md skills MCP servers sandbox rules workflows", "F3", 8.1, 0.15, 0.15, 0.15)
    y -= 58

    note_en = (
        "Una vez incorporadas estas nuevas fuentes al mismo cuaderno, vuelve a ejecutar el Prompt Auditor del Paso 2. "
        "Ahora NotebookLM combinará las webs en español con la documentación técnica oficial en inglés."
    )
    for ln in wrap_text(note_en, 86):
        pdf.draw_text(44, y, ln, "F1", 9.5, 0.15, 0.18, 0.22)
        y -= 13
    y -= 14

    # SECCIÓN 4: EJERCICIO Y DIÁLOGO EN CLASE
    y = draw_section_box(
        pdf, y,
        "4. PASO 4: PRÁCTICA Y 3 PREGUNTAS DE REFLEXIÓN EN EL AULA",
        "Actividad guiada para comprobar la calidad de las respuestas de la IA con fuentes reales"
    )

    questions = [
        ("1. ¿Por qué pedimos 'No detallado en las fuentes' al final del prompt?",
         "Para evitar que la IA rellene huecos inventando respuestas (alucinaciones). Así sabemos con certeza "
         "qué información falta y si necesitamos añadir nuevas fuentes."),
        ("2. ¿Qué ventaja tiene exigir citas [1], [2] y nombres exactos de comandos o ajustes?",
         "Permite verificar con un solo clic de qué web salió cada dato y distinguir un artículo comercial "
         "superficial de una guía técnica fiable."),
        ("3. ¿Por qué añadimos la búsqueda en inglés al mismo cuaderno en lugar de empezar de cero?",
         "Porque sumamos el conocimiento previo con la documentación original del fabricante, creando una base "
         "bilingüe completa sobre la que hacer preguntas en español.")
    ]

    for q_title, q_body in questions:
        pdf.set_fill_color(0.95, 0.97, 1.0)
        pdf.set_stroke_color(0.75, 0.82, 0.92)
        pdf.set_line_width(0.8)
        wrapped = wrap_text(q_body, 82)
        q_h = 24 + len(wrapped) * 12.5
        pdf.rect(40, y - q_h, 515, q_h, fill=True, stroke=True)
        pdf.draw_text(50, y - 15, q_title, "F2", 9.8, 0.08, 0.22, 0.48)
        qy = y - 29
        for ln in wrapped:
            pdf.draw_text(54, qy, ln, "F1", 9.2, 0.15, 0.18, 0.22)
            qy -= 12.5
        y -= (q_h + 12)

    # Caja final de resumen práctico
    y -= 6
    pdf.set_fill_color(0.92, 0.98, 0.94)
    pdf.set_stroke_color(0.20, 0.58, 0.34)
    pdf.set_line_width(1.0)
    pdf.rect(40, y - 48, 515, 48, fill=True, stroke=True)
    pdf.draw_text(50, y - 16, "RESUMEN EN 3 CLICS PARA TU PROPIO PROYECTO:", "F2", 9.5, 0.10, 0.40, 0.20)
    pdf.draw_text(50, y - 31, "1) Descubrir fuentes -> Deep Research   2) Pegar Prompt Auditor   3) Ampliar en inglés si falta detalle", "F1", 9.2, 0.12, 0.22, 0.15)

    pdf.save(PDF_PATH)
    print(f"PDF generado correctamente: {PDF_PATH} (2 páginas)")


if __name__ == "__main__":
    build_pdf()
