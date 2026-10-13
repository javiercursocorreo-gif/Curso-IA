#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_005.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
5. COD-005_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 05 del Curso de IA (Simulador 3D: Sistema Solar Interactivo • Planetario Orbital con Mapas NASA).
Incluye respaldo vectorial nativo si reportlab no está disponible en el entorno actual.
"""

import os
import sys
import zlib
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(
    ROOT_DIR,
    "CLASES",
    "EXPORTACION_FICHAS_CLASSROOM_PDF",
    "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM",
    "05_Sesion"
)
PDF_PATH = os.path.join(OUTPUT_DIR, "5. COD-005_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = os.path.join(
    ROOT_DIR,
    "SIMULADORES_INTERACTIVOS",
    "02_INDICES_Y_CATALOGOS",
    "05_COD-005_Taller_Simulador_Sistema_Solar_3D.pdf"
)


def _pdf_escape(text):
    b = text.encode("cp1252", errors="replace")
    out = bytearray()
    for ch in b:
        if ch in (40, 41, 92):
            out.append(92)
        out.append(ch)
    return out.decode("latin1")


def build_pure_python_cod_005(dest_path):
    """Genera la ficha oficial COD-005 de 1 página en PDF vectorial nativo."""
    W, H = 612.0, 792.0  # Letter
    ops = []

    def rect(x, y, w, h, fill_rgb=None, stroke_rgb=None, lw=0.8):
        ops.append(f"{lw:.2f} w")
        if fill_rgb:
            ops.append(f"{fill_rgb[0]:.3f} {fill_rgb[1]:.3f} {fill_rgb[2]:.3f} rg")
        if stroke_rgb:
            ops.append(f"{stroke_rgb[0]:.3f} {stroke_rgb[1]:.3f} {stroke_rgb[2]:.3f} RG")
        mode = "B" if (fill_rgb and stroke_rgb) else ("f" if fill_rgb else "S")
        ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {mode}")

    def text_xy(x, y, txt, font="F1", size=8.5, rgb=(0.06, 0.09, 0.16)):
        ops.append("BT")
        ops.append(f"/{font} {size:.2f} Tf")
        ops.append(f"{rgb[0]:.3f} {rgb[1]:.3f} {rgb[2]:.3f} rg")
        ops.append(f"{x:.2f} {y:.2f} Td")
        ops.append(f"({_pdf_escape(txt)}) Tj")
        ops.append("ET")

    def draw_wrapped(x, y_start, text_str, max_chars=96, font="F1", size=8.0, leading=10.5, rgb=(0.12, 0.16, 0.23)):
        words = text_str.split(" ")
        lines, cur = [], ""
        for w in words:
            if len(cur) + len(w) + 1 <= max_chars:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        y = y_start
        for line in lines:
            text_xy(x, y, line, font, size, rgb)
            y -= leading
        return y

    # Cabecera
    text_xy(105, 762, "CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", "F2", 8.2, (0.01, 0.52, 0.78))
    text_xy(118, 748, "BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", "F2", 9.6, (0.06, 0.09, 0.16))
    rect(36, 740, W - 72, 1.2, fill_rgb=(0.01, 0.52, 0.78))

    text_xy(36, 722, "[COD-005] Taller: Crea tu propio simulador 3D del Sistema Solar", "F2", 12.0, (0.06, 0.09, 0.16))

    text_xy(36, 705, "Misión Didáctica • Exploración Espacial y Mecánica Orbital con Inteligencia Artificial:", "F2", 8.8, (0.01, 0.41, 0.63))
    mision = (
        "En este taller ordenarás a Gemini programar en Three.js un planetario 3D interactivo del Sistema Solar con mapas satelitales reales "
        "de la NASA. Sin saber programar: pedirás el código a Gemini con el prompt maestro, lo probarás pulsando «Ejecutar Creación» y "
        "explorarás los 8 planetas, la Luna, las 4 lunas de Júpiter, asteroides, anillos de Saturno, el Vórtice Galáctico y la Voyager 1."
    )
    draw_wrapped(36, 693, mision, 102, "F1", 7.9, 10.0)

    text_xy(36, 650, "Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):", "F2", 8.8, (0.01, 0.41, 0.63))
    rect(36, 542, W - 72, 102, fill_rgb=(0.94, 0.98, 1.0), stroke_rgb=(0.01, 0.52, 0.78), lw=1.0)
    tasks = [
        ("Tarea 1 • Pídele el código a Gemini (Pestaña 1):", "Abre Gemini (gemini.google.com). Copia el Prompt Maestro inferior, pégalo en el chat y pulsa Enviar."),
        ("Tarea 2 • Copia el código generado por la IA:", "En la respuesta de Gemini, haz clic en el botón «Copiar código» situado en la esquina superior derecha."),
        ("Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):", "En el mapa de la Sesión 05, pulsa «Abrir Taller Interactivo de Pruebas»."),
        ("Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:", "Pega el código en el cuadro izquierdo y pulsa «Ejecutar Creación» para explorar tu Sistema Solar 3D."),
        ("Tarea 5 • Explora la Demo NASA («Sistema Solar 3D»):", "Pulsa «Sistema Solar 3D» y haz clic en «Júpiter + 4 Lunas» o «Tirabuzón Galáctico» para verlo en acción."),
    ]
    ty = 631
    for t_bold, t_rest in tasks:
        text_xy(44, ty, t_bold, "F2", 7.8, (0.06, 0.09, 0.16))
        text_xy(44, ty - 9, t_rest, "F1", 7.6, (0.15, 0.20, 0.28))
        ty -= 19.5

    text_xy(36, 524, "Prompt Maestro para Copiar y Pegar en Gemini:", "F2", 8.8, (0.01, 0.41, 0.63))
    rect(36, 336, W - 72, 182, fill_rgb=(0.97, 0.98, 0.99), stroke_rgb=(0.39, 0.45, 0.55), lw=1.0)
    text_xy(44, 505, "Copia exactamente este texto en Gemini:", "F2", 7.8, (0.06, 0.09, 0.16))
    prompt_lines = [
        "\"Genera el código completo en un único archivo (HTML, CSS y JavaScript con Three.js) para crear un simulador",
        "interactivo 3D del Sistema Solar con texturas fotográficas satelitales reales de la NASA / Solar System Scope.",
        "Requisitos del código:",
        "1. Entrega todo en un único bloque de código para pulsar «Copiar código» y pegarlo en mi taller interactivo.",
        "2. Carga Three.js y OrbitControls desde CDN oficial (cdnjs / jsdelivr) en la cabecera.",
        "3. Carga las texturas equirectangulares 2K reales de la NASA desde el repositorio CDN:",
        "   https://cdn.jsdelivr.net/gh/zhangwenqiang0214/solar-system-3d@main/assets/",
        "   (2k_sun.jpg, 2k_mercury.jpg, 2k_venus_atmosphere.jpg, 2k_earth_daymap.jpg, 2k_earth_clouds.jpg,",
        "   2k_moon.jpg, 2k_mars.jpg, 2k_jupiter.jpg, 2k_saturn.jpg, 2k_saturn_ring_alpha.png, 2k_uranus.jpg,",
        "   2k_neptune.jpg y 8k_stars_milky_way.jpg).",
        "4. Modela el Sol central, los 8 planetas en órbitas keplerianas, la Luna en la Tierra, las 4 lunas galileanas",
        "   orbitando Júpiter (Ío, Europa, Ganímedes y Calisto), el Cinturón Principal de Asteroides y los anillos de Saturno.",
        "5. Añade botones para enfocar cualquier planeta, Cinturón de Asteroides, Vórtice Galáctico, comparar tamaños",
        "   y un control deslizante (slider) de Velocidad Orbital.",
        "6. Escribe exclusivamente el bloque de código sin explicaciones previas ni posteriores.\""
    ]
    py = 493
    for pl in prompt_lines:
        text_xy(44, py, pl, "F3", 7.5, (0.06, 0.09, 0.16))
        py -= 10.2

    text_xy(36, 318, "El Reto Extra (Para Alumnos Curiosos):", "F2", 8.8, (0.01, 0.41, 0.63))
    reto = (
        "¡Pídele a Gemini que amplíe tu planetario! En la misma conversación dile: «Añade al simulador el Cometa Halley "
        "cruzando el Sistema Solar en una órbita elíptica alargada con su núcleo brillante y una cola luminosa azulada»."
    )
    draw_wrapped(36, 305, reto, 102, "F1", 7.9, 10.2)

    text_xy(36, 276, "¿De dónde proceden las texturas hiperrealistas de la NASA y cómo se ha montado el Sistema Solar 3D?", "F2", 8.8, (0.01, 0.41, 0.63))
    rect(36, 152, W - 72, 118, fill_rgb=(0.93, 0.99, 0.96), stroke_rgb=(0.02, 0.59, 0.41), lw=1.0)
    tech_lines = [
        "• Origen de los mapas fotográficos satelitales (NASA / Solar System Scope 2K-8K): Cada esfera planetaria viste el mosaico",
        "  fotográfico real captado por las misiones espaciales de la NASA y la ESA: telescopio solar SDO (Sol), sonda MESSENGER",
        "  (Mercurio), radar Magellan / Akatsuki (Venus), satélite MODIS Blue Marble + nubes reales (Tierra), Lunar Reconnaissance",
        "  Orbiter LRO (Luna), misiones Viking y MGS (Marte), sonda Cassini, Galileo y Juno (Júpiter con sus 4 lunas galileanas Ío,",
        "  Europa, Ganímedes y Calisto, y Saturno con sus anillos), Voyager 2 (Urano y Neptuno) y panorama 360° de la Vía Láctea.",
        "• Montaje interactivo en Three.js (WebGL): Incluye órbitas keplerianas (1x = 1 año/60 s), las 4 lunas de Júpiter con etiquetas",
        "  en vivo, el Vórtice Helicoidal Galáctico (tirabuzón a 828.000 km/h) y la sonda Voyager 1 en la barrera de la Heliopausa."
    ]
    ty2 = 256
    for tl in tech_lines:
        text_xy(44, ty2, tl, "F1", 7.5, (0.06, 0.09, 0.16))
        ty2 -= 12.2

    stream_bytes = "\n".join(ops).encode("latin1")
    compressed = zlib.compress(stream_bytes)

    objs = []
    objs.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    objs.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
    objs.append(f"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W:.2f} {H:.2f}] /Resources << /Font << /F1 4 0 R /F2 5 0 R /F3 6 0 R >> >> /Contents 7 0 R >>\nendobj\n".encode("latin1"))
    objs.append(b"4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>\nendobj\n")
    objs.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>\nendobj\n")
    objs.append(b"6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>\nendobj\n")
    objs.append(f"7 0 obj\n<< /Length {len(compressed)} /Filter /FlateDecode >>\nstream\n".encode("latin1") + compressed + b"\nendstream\nendobj\n")

    pdf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for o in objs:
        offsets.append(len(pdf))
        pdf.extend(o)
    xref_pos = len(pdf)
    pdf.extend(f"xref\n0 {len(objs)+1}\n0000000000 65535 f \n".encode("latin1"))
    for off in offsets[1:]:
        pdf.extend(f"{off:010d} 00000 n \n".encode("latin1"))
    pdf.extend(f"trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode("latin1"))

    with open(dest_path, "wb") as f:
        f.write(pdf)


def build_cod_005_taller_3d_pdf(output_path=PDF_PATH):
    os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
    dest_path = output_path
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as _:
            pass
    except Exception:
        dest_path = LOCAL_BACKUP

    build_pure_python_cod_005(dest_path)
    if dest_path != LOCAL_BACKUP:
        try:
            shutil.copy2(dest_path, LOCAL_BACKUP)
        except Exception:
            pass
    print(f"✅ PDF COD-005 generado con éxito en: {dest_path}")


if __name__ == "__main__":
    build_cod_005_taller_3d_pdf()

