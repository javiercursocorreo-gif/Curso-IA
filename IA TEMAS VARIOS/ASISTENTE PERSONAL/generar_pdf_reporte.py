#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_pdf_reporte.py
Genera un PDF limpio, profesional y estructurado con el panel de ideas y tareas pendientes
a partir de 'BUZON_IDEAS_VOZ.md'.
Utiliza únicamente Python estándar nativo (sin dependencias externas).
"""

import os
import sys
import datetime
import re

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
BUZON_MD = os.path.join(WORKSPACE_DIR, "BUZON_IDEAS_VOZ.md")
PDF_OUTPUT = os.path.join(WORKSPACE_DIR, "PANEL_TAREAS_PENDIENTES.pdf")
ROOT_DIR = os.path.abspath(os.path.join(WORKSPACE_DIR, "..", ".."))
MIRROR_PDF = os.path.join(ROOT_DIR, "CURSO-IA", "IA TEMAS VARIOS", "ASISTENTE PERSONAL", "PANEL_TAREAS_PENDIENTES.pdf")

ICLOUD_SHORTCUTS_DIR = os.path.expanduser("~/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents")
SHORTCUTS_PDF = os.path.join(ICLOUD_SHORTCUTS_DIR, "PANEL_TAREAS_PENDIENTES.pdf")

def escape_pdf_text(text):
    text = str(text)
    text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    replacements = {
        'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
        'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
        'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
        '«': '<<', '»': '>>', '•': '-', '—': '-', '–': '-',
        'º': 'o', 'ª': 'a', '¿': '\xbf', '¡': '\xa1',
        '🤖': '[ROB]', '🧠': '[IA]', '🩺': '[MED]', '🎹': '[MUS]', '🛠️': '[HOG]',
        '🏡': '', '🔧': '', '✅': '[OK]', '📌': '', '🆕': '[NUEVO]'
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

class SimplePDFWriter:
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

def parse_buzon_md():
    if not os.path.exists(BUZON_MD):
        return []

    with open(BUZON_MD, "r", encoding="utf-8", errors="ignore") as f:
        contenido = f.read()

    # Partir por secciones
    partes_completadas = contenido.split("## ✅ TAREAS COMPLETADAS Y ARCHIVADAS")
    activo = partes_completadas[0]

    secciones = []
    lineas = activo.splitlines()
    sec_actual = None

    for l in lineas:
        l_str = l.strip()
        if l_str.startswith("## ") and not "COMPLETADAS" in l_str:
            titulo = l_str.replace("## ", "").strip()
            # Limpiar emojis para títulos
            titulo_limpio = re.sub(r'^[^\w\d]+', '', titulo).strip()
            sec_actual = {
                "titulo": titulo_limpio,
                "tareas": []
            }
            secciones.append(sec_actual)
        elif l_str.startswith("- [ ]") and sec_actual:
            # Tarea activa
            m = re.match(r'^-\s*\[\s*\]\s*(\*\*\[#\d+\]\*\*|\(\d+\)|\[#\d+\])?\s*(.*)$', l_str)
            if m:
                num = m.group(1) or ""
                num = num.replace("**", "").replace("[", "").replace("]", "").replace("#", "").strip()
                texto_tarea = m.group(2).strip()
                # Limpiar negritas Markdown
                texto_tarea = re.sub(r'\*\*(.*?)\*\*', r'\1', texto_tarea)
                sec_actual["tareas"].append({
                    "num": f"#{int(num):02d}" if num.isdigit() else "#--",
                    "texto": texto_tarea
                })

    return secciones

def generar_pdf():
    secciones = parse_buzon_md()
    if not secciones:
        print("⚠️ No hay secciones para generar el PDF.")
        return

    writer = SimplePDFWriter()
    ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    # Contar total de tareas
    total_tareas = sum(len(s["tareas"]) for s in secciones)

    writer.start_page()
    page_num = 1

    # Margen superior
    y = writer.h - 45

    # Cabecera principal ejecutiva
    # Barra azul superior decorativa
    writer.set_fill_color(0.12, 0.23, 0.54) # Azul Marino
    writer.rect(36, writer.h - 20, writer.w - 72, 4, fill=True, stroke=False)

    writer.draw_text(36, y, "PANEL MAESTRO DE TAREAS E IDEAS PENDIENTES", "F2", 15, 0.12, 0.23, 0.54)
    y -= 16
    writer.draw_text(36, y, f"Asistente Personal • Actualizado: {ahora} • {total_tareas} tareas activas", "F1", 9, 0.45, 0.5, 0.58)

    # Línea divisoria cabecera
    y -= 12
    writer.set_stroke_color(0.82, 0.86, 0.92)
    writer.set_line_width(0.8)
    writer.line(36, y, writer.w - 36, y)
    y -= 20

    colores_tema = {
        "ROBOTICA": (0.15, 0.35, 0.65),      # Azul cobalto
        "INTELIGENCIA": (0.35, 0.20, 0.60),  # Morado índigo
        "SALUD": (0.05, 0.50, 0.40),         # Verde azulado esmeralda
        "MUSICA": (0.80, 0.45, 0.10),        # Ámbar / Cobre
        "HOGAR": (0.45, 0.25, 0.25)          # Teja / Pizarra
    }

    for sec in secciones:
        if not sec["tareas"]:
            continue

        # Color temático
        color_header = (0.2, 0.25, 0.35)
        for k, col in colores_tema.items():
            if k in sec["titulo"].upper():
                color_header = col
                break

        # Comprobar si cabe el bloque de la sección (al menos cabecera + 1 tarea)
        if y < 110:
            # Pie de página
            writer.draw_text(36, 25, f"Página {page_num} • Panel de Tareas del Asistente Personal", "F1", 8, 0.5, 0.55, 0.6)
            writer.end_page()
            page_num += 1
            writer.start_page()
            y = writer.h - 50

        # Fondo del encabezado de sección
        writer.set_fill_color(color_header[0], color_header[1], color_header[2])
        writer.rect(36, y - 4, writer.w - 72, 18, fill=True, stroke=False)
        writer.draw_text(44, y + 1, sec["titulo"].upper(), "F2", 9.5, 1, 1, 1)
        y -= 22

        # Tareas
        for t in sec["tareas"]:
            # Líneas del texto con wrap
            # Disponemos de ancho = writer.w - 72 - 45 (para el badge de número) = ~440 puntos => ~80 caracteres
            lineas_tarea = wrap_text(t["texto"], max_chars=82)
            altura_necesaria = len(lineas_tarea) * 12 + 6

            if y - altura_necesaria < 45:
                # Salto de página
                writer.draw_text(36, 25, f"Página {page_num} • Panel de Tareas del Asistente Personal", "F1", 8, 0.5, 0.55, 0.6)
                writer.end_page()
                page_num += 1
                writer.start_page()
                y = writer.h - 50

            # Badge del número [#01]
            writer.set_fill_color(0.92, 0.94, 0.97)
            writer.set_stroke_color(0.78, 0.83, 0.90)
            writer.set_line_width(0.5)
            writer.rect(40, y - 10, 32, 14, fill=True, stroke=True)
            writer.draw_text(44, y - 7, t["num"], "F2", 8.5, color_header[0], color_header[1], color_header[2])

            # Texto de la tarea
            ty = y - 6
            for idx_l, lt in enumerate(lineas_tarea):
                fnt = "F2" if idx_l == 0 and ":" in lt else "F1"
                writer.draw_text(80, ty, lt, fnt, 8.5, 0.15, 0.18, 0.22)
                ty -= 11.5

            y = ty - 4

        y -= 10 # Separación entre secciones

    # Pie de última página
    writer.draw_text(36, 25, f"Página {page_num} de {page_num} • Documento Vivo generado automáticamente", "F1", 8, 0.5, 0.55, 0.6)
    writer.draw_text(writer.w - 180, 25, "Buzón de Voz & Asistente Personal", "F2", 8, 0.12, 0.23, 0.54)
    writer.end_page()

    writer.write_to_file(PDF_OUTPUT)
    print(f"✅ PDF generado con éxito en: {PDF_OUTPUT}")

    if os.path.exists(os.path.dirname(MIRROR_PDF)):
        writer.write_to_file(MIRROR_PDF)
        print(f"✅ Espejo actualizado en: {MIRROR_PDF}")

    try:
        if os.path.exists(ICLOUD_SHORTCUTS_DIR):
            import shutil
            shutil.copy2(PDF_OUTPUT, SHORTCUTS_PDF)
            print(f"✅ Copia en Atajos de iCloud sincronizada: {SHORTCUTS_PDF}")
    except Exception as e:
        pass

if __name__ == "__main__":
    generar_pdf()
