#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_006.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
6. COD-006_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 06 del Curso de IA (Simulador 3D: Cerebro Humano, Lóbulos Corticales y Red Sináptica).
Generador vectorial nativo en Python puro (100% independiente de reportlab).
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
    "06_Sesion"
)
PDF_PATH = os.path.join(OUTPUT_DIR, "6. COD-006_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = os.path.join(
    ROOT_DIR,
    "SIMULADORES_INTERACTIVOS",
    "02_INDICES_Y_CATALOGOS",
    "06_COD-006_Taller_Simulador_Cerebro_Humano_3D.pdf"
)


def _pdf_escape(text):
    b = text.encode("cp1252", errors="replace")
    out = bytearray()
    for ch in b:
        if ch in (40, 41, 92):
            out.append(92)
        out.append(ch)
    return out.decode("latin1")


def build_pure_python_cod_006(dest_path):
    """Genera la ficha oficial COD-006 de 1 página en PDF vectorial nativo."""
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
    text_xy(105, 760, "CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", "F2", 8.2, (0.01, 0.52, 0.78))
    text_xy(118, 746, "BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", "F2", 9.6, (0.06, 0.09, 0.16))
    rect(36, 738, W - 72, 1.2, fill_rgb=(0.01, 0.52, 0.78))

    text_xy(36, 720, "[COD-006] Taller: Crea tu propio simulador del cerebro humano", "F2", 12.0, (0.06, 0.09, 0.16))

    text_xy(36, 702, "Misión Didáctica • Neurociencia y Redes Neuronales 3D con Inteligencia Artificial:", "F2", 8.8, (0.01, 0.41, 0.63))
    mision = (
        "En este taller ordenarás a Gemini programar en Three.js un cerebro humano 3D interactivo con lóbulos cerebrales diferenciados "
        "y pulsos de sinapsis bioeléctricos. Sin saber programar: pedirás el código a Gemini con el prompt maestro, lo probarás en el "
        "taller pulsando «Ejecutar Creación» y explorarás el lóbulo frontal (pensamiento), parietal (tacto), temporal (memoria), occipital "
        "(visión), cerebelo y los haces neuronales que comunican ambos hemisferios."
    )
    draw_wrapped(36, 689, mision, 102, "F1", 8.0, 10.5)

    text_xy(36, 650, "Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):", "F2", 8.8, (0.01, 0.41, 0.63))
    rect(36, 542, W - 72, 102, fill_rgb=(0.94, 0.98, 1.0), stroke_rgb=(0.01, 0.52, 0.78), lw=1.0)
    tasks = [
        ("Tarea 1 • Pídele el código a Gemini (Pestaña 1):", "Abre Gemini (gemini.google.com). Copia el Prompt Maestro inferior, pégalo en el chat y pulsa Enviar."),
        ("Tarea 2 • Copia el código generado por la IA:", "En la respuesta de Gemini, haz clic en el botón «Copiar código» situado en la esquina superior derecha."),
        ("Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):", "En el mapa de la Sesión 06, pulsa «Abrir Taller Interactivo de Pruebas»."),
        ("Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:", "Pega el código en el cuadro izquierdo y pulsa «Ejecutar Creación» para explorar el cerebro y sus sinapsis."),
        ("Tarea 5 • Explora la Demo («Cerebro 3D»):", "Pulsa «Cerebro 3D» y haz clic en «Lóbulo Frontal», «Sinapsis» o «Hemisferio Izq/Der» para examinar el interior."),
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
        "interactivo 3D del Cerebro Humano con corteza translúcida, lóbulos diferenciados y red de sinapsis bioeléctricas.",
        "Requisitos del código:",
        "1. Entrega todo en un único bloque de código para pulsar «Copiar código» y pegarlo en mi taller interactivo.",
        "2. Carga Three.js y OrbitControls desde CDN oficial (cdnjs) en la cabecera.",
        "3. Modela el encéfalo en 3D con circunvoluciones anatómicas PBR y asigna colores diferenciados a cada lóbulo:",
        "   Frontal (azul), Parietal (amarillo), Temporal (verde), Occipital (rojo-rosa), Cerebelo (violeta) y Tronco (gris).",
        "4. Genera una red neuronal interna con curvas sinápticas (THREE.QuadraticBezierCurve3) y partículas luminosas en",
        "   movimiento continuo simulando la transmisión de impulsos bioeléctricos (potenciales de acción) a través del encéfalo.",
        "5. Añade botones para enfocar la cámara en cada lóbulo, alternar la visibilidad de la corteza/sinapsis, deslizar la",
        "   velocidad del impulso bioeléctrico y separar ambos hemisferios cerebrales.",
        "6. Escribe exclusivamente el bloque de código sin explicaciones previas ni posteriores.\""
    ]
    py = 493
    for pl in prompt_lines:
        text_xy(44, py, pl, "F3", 7.5, (0.06, 0.09, 0.16))
        py -= 10.2

    text_xy(36, 318, "El Reto Extra (Para Alumnos Curiosos):", "F2", 8.8, (0.01, 0.41, 0.63))
    reto = (
        "¡Pídele a Gemini que amplíe tu laboratorio neurocientífico! En la misma conversación dile: «Añade al simulador "
        "un selector de Ondas Cerebrales (Beta en vigilia a 25 Hz, Alfa en relajación a 10 Hz y Theta en sueño a 5 Hz) "
        "que cambie el color y la cadencia de disparo de los pulsos sinápticos»."
    )
    draw_wrapped(36, 305, reto, 102, "F1", 7.9, 10.2)

    text_xy(36, 276, "¿Cómo se ha modelado la neuroanatomía hiperrealista y la red sináptica en 3D?", "F2", 8.8, (0.01, 0.41, 0.63))
    rect(36, 152, W - 72, 118, fill_rgb=(0.93, 0.99, 0.96), stroke_rgb=(0.02, 0.59, 0.41), lw=1.0)
    tech_lines = [
        "• Modelado cortical orgánico (Gyri y Sulci): Las circunvoluciones del cerebro se sintetizan mediante perturbaciones",
        "  armónicas tridimensionales (fórmulas trigonométricas sinusoidales acopladas) aplicadas a mallas esferoidales de alta",
        "  densidad poligonal (SphereGeometry 48×48), logrando los pliegues y surcos anatómicos exactos de la corteza cerebral.",
        "• Red axonal y destellos sinápticos: Una red tridimensional de más de 300 haces axonales interconecta los núcleos del tálamo,",
        "  el cuerpo calloso y los cuatro polos corticales. Sobre ellos, 450 partículas bioluminiscentes (THREE.Points con shader aditivo)",
        "  viajan a lo largo de curvas Bezier cuadráticas recreando el tráfico bioeléctrico de 40 Hz en tiempo real."
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
    objs.append(b"6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>\nendobj\n")
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

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "wb") as f:
        f.write(pdf)


def main():
    dest = PDF_PATH
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        build_pure_python_cod_006(dest)
    except Exception:
        dest = LOCAL_BACKUP

    build_pure_python_cod_006(LOCAL_BACKUP)
    print(f"✅ PDF COD-006 generado con éxito en: {LOCAL_BACKUP}")


if __name__ == "__main__":
    main()

