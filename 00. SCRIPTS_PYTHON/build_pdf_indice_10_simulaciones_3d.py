#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_indice_10_simulaciones_3d.py
Genera el PDF (y versión HTML interactiva) del Catálogo Maestro de las 10 Grandes Simulaciones Interactivas 3D Intercaladas
(Anatomía Humana / Historia / Espacio - Sistema Solar 3D NASA / Mecánica / Paleontología / Acústica).
Incluye generador vectorial nativo en Python puro como respaldo automático si reportlab no está activo en el entorno.
"""

import os
import sys
import zlib

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "02_INDICES_Y_CATALOGOS")
PDF_PATH = os.path.join(OUT_DIR, "INDICE_10_SIMULACIONES_INTERACTIVAS_3D.pdf")
HTML_PATH = os.path.join(OUT_DIR, "INDICE_10_SIMULACIONES_INTERACTIVAS_3D.html")

SIMULACIONES_DATA = [
    ("01", "[COD-001]", "Salud & Respiración", "Árbol Traqueobronquial & Pulmones",
     "Estructura traqueal fractal, ventilación alveolar biofísica rítmica y audio respiratorio.",
     "Ver Simulador Pulmones 3D", "../01_SIMULADORES/01_SIMULADOR_PULMONES_3D.html", "Activo en S01"),
    ("02", "[COD-002]", "Salud & Cardiología", "Corazón Humano con Fonendoscopio",
     "Fotogrametría PBR 4K miocardio, ecuación Wiggers (sístole/diástole), slider BPM y fonendoscopio acústico.",
     "Ver Simulador Corazón 3D", "../01_SIMULADORES/02_SIMULADOR_CORAZON_3D.html", "Activo en S02"),
    ("03", "[COD-003]", "Historia & Arqueología", "Tesoro de Pompeya (Foro CyArk)",
     "Arqueología digital HD, comparador de viaje en el tiempo (ruinas vs. reconstrucción imperial), iluminación cinematográfica.",
     "Ver Tesoro Arqueológico 3D", "../01_SIMULADORES/03_SIMULADOR_POMPEYA_3D.html", "Activo en S03"),
    ("04", "[COD-004]", "Salud & Óptica", "Globo Ocular Humano & Cristalino",
     "Córnea de cristal reflectante, iris 4K, pupila interactiva con reflejo fotomotor (miosis/midriasis por slider) y corte sagital.",
     "Ver Simulador Ojo Humano 3D", "../01_SIMULADORES/04_SIMULADOR_OJO_HUMANO_3D_V2.html", "Activo en S04"),
    ("05", "[COD-005]", "Espacio & Exploración", "Sistema Solar 3D Orbital & Cinturón (NASA)",
     "Fotogrametría NASA 2K-8K, viaje 3D a 8 planetas + Sol, Luna, 4 lunas de Júpiter, Cinturón de Asteroides y Voyager 1.",
     "Ver Sistema Solar 3D", "../01_SIMULADORES/05_SIMULADOR_SISTEMA_SOLAR_3D.html", "Activo en S05"),
    ("06", "[COD-006]", "Salud & Neurociencia", "Cerebro Humano & Red Sináptica",
     "Resonancia magnética médica cortical, vías neuronales, pulsos lumínicos bioeléctricos y selector de lóbulos cerebrales.",
     "Ver Simulador Cerebro 3D", "../01_SIMULADORES/06_SIMULADOR_CEREBRO_3D.html", "Activo en S06"),
    ("07", "[COD-007]", "Espacio & Selenografía", "Atlas 3D de la Luna NASA LRO",
     "Fotogrametría NASA LRO 4K, mares basálticos (Tranquillitatis, Procellarum), cráteres (Tycho), sitios Apolo 11-17 y fases.",
     "Ver Atlas Lunar 3D", "../01_SIMULADORES/07_SIMULADOR_LUNA_3D.html", "Plan S07"),
    ("08", "[COD-008]", "Ingeniería Mecánica & Motores", "Motor Térmico de Combustión (Corte Técnico Real HD)",
     "Fotografía técnica de corte seccional de ingeniería real, termografía infrarroja, análisis de esfuerzos en biela y ciclo Otto 4T.",
     "Ver Laboratorio Motor HD", "../01_SIMULADORES/08_SIMULADOR_MOTOR_TURBOFAN_3D.html", "Activo en S08"),
    ("09", "[COD-009]", "Biología Celular & Microscopía", "Célula Eucariota en Micrografía Electrónica (TEM 50.000x)",
     "Micrografía electrónica de transmisión auténtica a 50.000x, ultraestructura celular, tinción citoquímica y fluorescencia molecular.",
     "Ver Laboratorio Célula TEM", "../01_SIMULADORES/09_SIMULADOR_CELULA_EUCARIOTA_3D.html", "Activo en S09"),
    ("10", "[COD-010]", "Salud & Odontología", "Molar Humano en Sección Anatómica",
     "Esmalte lúcido, dentina, pulpa vascularizada y terminaciones nerviosas; despiece tridimensional por capas clínicas.",
     "Ver Molar Anatómico 3D", "#", "Plan S10"),
    ("11", "[COD-011]", "Acústica & Arte Musical", "Violín Stradivarius & Resonancia",
     "Madera de arce noble barnizada PBR 4K, simulación de cuerdas en vibración física armónica y ondas de presión acústica.",
     "Ver Acústica Stradivarius 3D", "#", "Plan S11"),
    ("12", "[COD-012]", "NASA • Cosmos & Óptica", "Nebulosa Helix: El Ojo de Dios (Spitzer)",
     "Fotografía infrarroja espacial Spitzer de NGC 7293: estrella central moribunda y disco de polvo cósmico con forma de iris.",
     "Ver Nebulosa Helix 3D", "#", "Plan S12"),
    ("13", "[COD-013]", "Salud & Genética", "Doble Hélice del ADN & Código Genético",
     "Estructura molecular 3D Watson-Crick, pares de bases nitrogenadas (A-T, C-G) y animación de transcripción biológica.",
     "Ver ADN Molecular 3D", "#", "Plan S13"),
    ("14", "[COD-014]", "NASA • Espacio Profundo", "Auroras Ultravioletas de Júpiter (Hubble)",
     "Espectacular fotografía UV del polo norte de Júpiter, anillo de plasma fluorescente y colisión de viento solar con la magnetosfera.",
     "Ver Auroras de Júpiter 3D", "#", "Plan S14"),
    ("15", "[COD-015]", "Historia & Arquitectura", "El Partenón & Proporción Áurea 3D",
     "Reconstrucción arqueológica de la Acrópolis de Atenas, columnas dóricas y trazado interactivo de la espiral de Fibonacci / Phi.",
     "Ver Partenón Dorado 3D", "#", "Plan S15"),
    ("16", "[COD-016]", "NASA • Selenografía Real", "Tránsito Cara Oculta Lunar (DSCOVR)",
     "Fotografía histórica de la cámara EPIC: la cara oculta de la Luna totalmente iluminada cruzando por delante de la Tierra.",
     "Ver Tránsito Lunar 3D", "#", "Plan S16"),
    ("17", "[COD-017]", "Ingeniería & Energía", "Turbina Eólica Marina en Sección",
     "Góndola, rotor, multiplicadora y generador síncrono; orientación aerodinámica de palas eólica offshore frente al viento marino.",
     "Ver Turbina Eólica 3D", "#", "Plan S17"),
    ("18", "[COD-018]", "NASA • Hito Histórico", "Earthrise: Salida de la Tierra (Apollo 11)",
     "La emblemática imagen de la Tierra azul elevándose sobre el horizonte árido del Mar de la Tranquilidad lunar tomada en 1969.",
     "Ver Earthrise 3D", "#", "Plan S18"),
    ("19", "[COD-019]", "Salud & Fisiología", "Sistema Renal & Nefrona Humana",
     "Riñón en corte coronal con cápsula, pirámides y corteza; microestructura 3D del glomérulo y filtrado microscópico de sangre.",
     "Ver Sistema Renal 3D", "#", "Plan S19"),
    ("20", "[COD-020]", "NASA • Hazaña Humana", "Paseo Espacial en el Vacío (Gemini 4)",
     "Fotografía histórica del astronauta Ed White flotando libre durante 21 minutos sobre la Tierra con cordón umbilical dorado.",
     "Ver Paseo Espacial 3D", "#", "Plan S20"),
    ("21", "[COD-021]", "Geología & Vulcanismo", "Cámara Magmática de un Volcán 3D",
     "Corte transversal de un estratovolcán activo: chimenea central, cámara magmática incandescente, magma viscoso y erupción.",
     "Ver Volcán Activo 3D", "#", "Plan S21"),
    ("22", "[COD-022]", "NASA • Cosmos Profundo", "Telescopio Espacial James Webb (JWST)",
     "Espejo primario hexagonal de oro de 24K, parasol de 5 capas de Kapton, instrumentos infrarrojos NIRCam y órbita en L2.",
     "Ver James Webb 3D", "#", "Plan S22"),
    ("23", "[COD-023]", "Geofísica & Tierra", "Viaje al Núcleo de la Tierra (Geodinamo)",
     "Corte sagital 3D: corteza, manto en convección, núcleo externo líquido (geodinamo/magnetosfera) y núcleo interno sólido 5.500 °C.",
     "Ver Núcleo de la Tierra 3D", "#", "Plan S23"),
]


def _pdf_escape(text):
    b = text.encode("cp1252", errors="replace")
    out = bytearray()
    for ch in b:
        if ch in (40, 41, 92):
            out.append(92)
        out.append(ch)
    return out.decode("latin1")


def _generate_page_stream(items, page_num, total_pages, title_part, subtitle_text, intro1, intro2, W, H):
    """Genera las instrucciones de dibujo vectoriales de una página en PDF nativo."""
    ops = []

    def rect(x, y, w, h, fill_rgb=None, stroke_rgb=None, lw=0.6):
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

    # Cabecera
    text_xy(105, 558, f"CATÁLOGO MAESTRO: SIMULACIONES INTERACTIVAS 3D INTERCALADAS ({title_part})", "F2", 13.5, (0.06, 0.09, 0.16))
    text_xy(125, 542, subtitle_text, "F3", 8.8, (0.28, 0.33, 0.41))
    rect(32, 534, W - 64, 1.5, fill_rgb=(0.01, 0.52, 0.78))

    text_xy(32, 520, intro1, "F1", 8.0, (0.12, 0.16, 0.23))
    text_xy(32, 510, intro2, "F1", 8.0, (0.12, 0.16, 0.23))

    # Tabla
    col_x = [32, 84, 198, 338, 601, 739, 809]
    col_w = [col_x[i+1] - col_x[i] for i in range(len(col_x)-1)]
    headers = ["Sesión", "Universo / Temática", "Modelo Aprobado (PBR / NASA)", "Experiencia Visual e Interactiva", "Botón 2 • Simulador Terminado", "Estado"]

    y_top = 498
    row_h_header = 20
    rect(32, y_top - row_h_header, W - 64, row_h_header, fill_rgb=(0.06, 0.09, 0.16), stroke_rgb=(0.80, 0.84, 0.88))
    for i, h_txt in enumerate(headers):
        text_xy(col_x[i] + 5, y_top - 13.5, h_txt, "F2", 8.0, (1, 1, 1))

    y_curr = y_top - row_h_header
    row_h = 35.0 if len(items) > 11 else 38.0
    for idx, (ses, cod, univ, mod, exp, btn, _, est) in enumerate(items):
        y_curr -= row_h
        bg = (0.97, 0.98, 0.99) if idx % 2 == 0 else (1.0, 1.0, 1.0)
        if ses in ("05", "07", "12", "14", "16", "18", "20", "22"):
            bg = (0.94, 0.98, 1.0)
        for c_i in range(6):
            rect(col_x[c_i], y_curr, col_w[c_i], row_h, fill_rgb=bg, stroke_rgb=(0.80, 0.84, 0.88), lw=0.5)

        text_xy(col_x[0] + 18, y_curr + (20 if row_h < 36 else 22), ses, "F2", 8.8, (0.06, 0.09, 0.16))
        text_xy(col_x[0] + 6, y_curr + (8 if row_h < 36 else 10), cod, "F1", 7.4, (0.39, 0.45, 0.55))

        text_xy(col_x[1] + 5, y_curr + (13 if row_h < 36 else 15), univ, "F2", 7.6, (0.01, 0.52, 0.78))

        if len(mod) > 28:
            parts = mod.split(" ")
            mid = len(parts) // 2
            text_xy(col_x[2] + 5, y_curr + (19 if row_h < 36 else 21), " ".join(parts[:mid]), "F2", 7.8, (0.06, 0.09, 0.16))
            text_xy(col_x[2] + 5, y_curr + (8 if row_h < 36 else 10), " ".join(parts[mid:]), "F2", 7.8, (0.06, 0.09, 0.16))
        else:
            text_xy(col_x[2] + 5, y_curr + (13 if row_h < 36 else 15), mod, "F2", 7.8, (0.06, 0.09, 0.16))

        words = exp.split(" ")
        lines, cur = [], ""
        for w in words:
            if len(cur) + len(w) + 1 <= 58:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        start_y = y_curr + (22 if row_h < 36 else 25) if len(lines) >= 3 else (y_curr + (17 if row_h < 36 else 20) if len(lines) == 2 else y_curr + (13 if row_h < 36 else 15))
        for l_i, line_str in enumerate(lines[:3]):
            text_xy(col_x[3] + 5, start_y - l_i * (8.2 if row_h < 36 else 9.0), line_str, "F1", 7.3, (0.20, 0.25, 0.33))

        text_xy(col_x[4] + 5, y_curr + (13 if row_h < 36 else 15), btn, "F2", 7.4, (0.02, 0.47, 0.34))

        est_color = (0.02, 0.47, 0.34) if "Activo" in est else (0.28, 0.33, 0.41)
        est_font = "F2" if "Activo" in est else "F3"
        text_xy(col_x[5] + 6, y_curr + (13 if row_h < 36 else 15), est, est_font, 7.4, est_color)

    foot_txt = f"Página {page_num} de {total_pages} • Estándar Técnico WebGL / Three.js sin descargas ni plugins externos, garantizando fluidez total en el aula senior (60+)."
    text_xy(32, 34, foot_txt, "F1", 8.0, (0.12, 0.16, 0.23))

    return "\n".join(ops).encode("latin1")


def build_pure_python_pdf():
    """Genera el PDF vectorial horizontal A4 de 2 páginas sin dependencias externas."""
    os.makedirs(OUT_DIR, exist_ok=True)
    W, H = 841.89, 595.27  # A4 Landscape

    intro1_p1 = "Metodología de Intercalación Temática (Fase 1: S01 a S11): Para evitar la fatiga cognitiva y mantener la fascinación visual permanente en el alumnado senior (60+),"
    intro2_p1 = "el bloque de creación [COD] alterna sesiones de Anatomía y Salud Humana con Grandes Hitos de la Ciencia (Pompeya, Sistema Solar 3D NASA, Atlas Lunar LRO y Fósiles)."

    intro1_p2 = "Expansión Cósmica e Innovación (Fase 2: S12 a S23): Intercala Grandes Fotografías de la NASA (Helix, Júpiter, DSCOVR, Apollo, Gemini, James Webb) con modelos"
    intro2_p2 = "biomédicos (ADN, Nefrona), arquitectura clásica (Partenón), energía eólica marina, vulcanismo activo y el viaje al Núcleo de la Tierra (Geodinamo)."

    stream1 = _generate_page_stream(
        SIMULACIONES_DATA[:11], 1, 2, "Parte 1: Sesiones 01 a 11",
        "Plan Didáctico Intercalado: Alternancia de Anatomía Biomédica, Historia, Sistema Solar NASA y Selenografía",
        intro1_p1, intro2_p1, W, H
    )
    stream2 = _generate_page_stream(
        SIMULACIONES_DATA[11:], 2, 2, "Parte 2: Sesiones 12 a 23",
        "Expansión Cósmica y Geofísica: Hitos de la NASA (Spitzer, Hubble, DSCOVR, Apollo, Gemini, Webb) e Interior Terrestre",
        intro1_p2, intro2_p2, W, H
    )

    comp1 = zlib.compress(stream1)
    comp2 = zlib.compress(stream2)

    objs = []
    objs.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    objs.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R 8 0 R] /Count 2 >>\nendobj\n")
    objs.append(f"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W:.2f} {H:.2f}] /Resources << /Font << /F1 4 0 R /F2 5 0 R /F3 6 0 R >> >> /Contents 7 0 R >>\nendobj\n".encode("latin1"))
    objs.append(b"4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>\nendobj\n")
    objs.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>\nendobj\n")
    objs.append(b"6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>\nendobj\n")
    objs.append(f"7 0 obj\n<< /Length {len(comp1)} /Filter /FlateDecode >>\nstream\n".encode("latin1") + comp1 + b"\nendstream\nendobj\n")
    objs.append(f"8 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W:.2f} {H:.2f}] /Resources << /Font << /F1 4 0 R /F2 5 0 R /F3 6 0 R >> >> /Contents 9 0 R >>\nendobj\n".encode("latin1"))
    objs.append(f"9 0 obj\n<< /Length {len(comp2)} /Filter /FlateDecode >>\nstream\n".encode("latin1") + comp2 + b"\nendstream\nendobj\n")

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

    with open(PDF_PATH, "wb") as f:
        f.write(pdf)
    print(f"✅ PDF del Catálogo Maestro (2 Páginas Vectoriales Nativas) generado en: {PDF_PATH} ({len(pdf)} bytes)")


def build_html_catalog():
    """Genera también una versión HTML interactiva del Catálogo Maestro de las 21 Simulaciones e Hitos NASA."""
    os.makedirs(OUT_DIR, exist_ok=True)
    rows_html = ""
    for ses, cod, univ, mod, exp, btn, href, est in SIMULACIONES_DATA:
        is_active = "Activo" in est
        badge_cls = "status-active" if is_active else "status-plan"
        btn_el = f'<a href="{href}" target="_blank" class="sim-link">🚀 {btn} ↗</a>' if href != "#" else f'<span class="sim-pending">⏳ {btn}</span>'
        is_space = ses in ("05", "07", "12", "14", "16", "18", "20")
        rows_html += f"""
        <tr class="{'row-highlight' if is_space else ''}">
            <td class="col-ses"><strong>{ses}</strong><span>{cod}</span></td>
            <td class="col-univ">{univ}</td>
            <td class="col-mod">{mod}</td>
            <td class="col-exp">{exp}</td>
            <td class="col-btn">{btn_el}</td>
            <td class="col-est"><span class="status-pill {badge_cls}">{'✅ ' + est if is_active else '📅 ' + est}</span></td>
        </tr>"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo Maestro: Simulaciones Interactivas 3D</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #070b14; color: #f8fafc; margin: 0; padding: 28px; }}
        .container {{ max-width: 1320px; margin: 0 auto; background: #0f172a; border: 1px solid #1e293b; border-radius: 18px; padding: 26px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); }}
        h1 {{ font-size: 1.6rem; margin: 0 0 6px; color: #ffffff; text-align: center; }}
        p.sub {{ text-align: center; color: #94a3b8; font-size: 0.92rem; margin: 0 0 18px; line-height: 1.45; }}
        table {{ width: 100%; border-collapse: collapse; font-size: 0.88rem; }}
        th {{ background: #1e293b; color: #38bdf8; text-transform: uppercase; font-size: 0.76rem; letter-spacing: 0.05em; padding: 12px 10px; text-align: left; border-bottom: 2px solid #334155; }}
        td {{ padding: 11px 10px; border-bottom: 1px solid #1e293b; vertical-align: middle; }}
        tr:hover {{ background: rgba(30, 41, 59, 0.5); }}
        tr.row-highlight {{ background: rgba(56, 189, 248, 0.08); }}
        .col-ses {{ text-align: center; width: 75px; }}
        .col-ses strong {{ display: block; font-size: 1rem; color: #fff; }}
        .col-ses span {{ font-size: 0.72rem; color: #64748b; font-family: monospace; }}
        .col-univ {{ color: #38bdf8; font-weight: 700; width: 160px; }}
        .col-mod {{ font-weight: 800; color: #f8fafc; width: 230px; }}
        .col-exp {{ color: #cbd5e1; line-height: 1.38; font-size: 0.85rem; }}
        .sim-link {{ display: inline-block; background: rgba(16, 185, 129, 0.16); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); padding: 5px 10px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 0.78rem; white-space: nowrap; }}
        .sim-link:hover {{ background: rgba(16, 185, 129, 0.28); }}
        .sim-pending {{ color: #64748b; font-size: 0.78rem; font-weight: 600; white-space: nowrap; }}
        .status-pill {{ display: inline-block; padding: 4px 9px; border-radius: 999px; font-size: 0.75rem; font-weight: 800; white-space: nowrap; }}
        .status-active {{ background: rgba(52, 211, 153, 0.15); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.35); }}
        .status-plan {{ background: rgba(148, 163, 184, 0.12); color: #94a3b8; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🌌 CATÁLOGO MAESTRO: SIMULACIONES INTERACTIVAS 3D INTERCALADAS</h1>
        <p class="sub">Plan Didáctico Intercalado: Alternancia de Anatomía Biomédica, Hitos Fotográficos NASA (Spitzer, Hubble, DSCOVR, Apollo, Gemini), Historia, Ingeniería y Geología</p>
        <table>
            <thead>
                <tr>
                    <th>Sesión</th>
                    <th>Universo / Temática</th>
                    <th>Modelo Aprobado (PBR / NASA)</th>
                    <th>Experiencia Visual e Interactiva</th>
                    <th>Simulador 3D</th>
                    <th>Estado</th>
                </tr>
            </thead>
            <tbody>{rows_html}
            </tbody>
        </table>
    </div>
</body>
</html>"""
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Catálogo HTML interactivo generado en: {HTML_PATH}")


def build_pdf():
    build_html_catalog()
    try:
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    except ImportError:
        build_pure_python_pdf()
        return

    os.makedirs(OUT_DIR, exist_ok=True)
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=landscape(A4),
        leftMargin=32, rightMargin=32,
        topMargin=28, bottomMargin=26
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("TitleStyle", parent=styles["Heading1"], fontSize=17, leading=21, textColor=colors.HexColor("#0f172a"), alignment=1, fontName="Helvetica-Bold")
    sub_style = ParagraphStyle("SubStyle", parent=styles["Normal"], fontSize=9.5, leading=13, textColor=colors.HexColor("#475569"), alignment=1, fontName="Helvetica-Oblique")
    intro_style = ParagraphStyle("IntroStyle", parent=styles["Normal"], fontSize=8.5, leading=11.5, textColor=colors.HexColor("#1e293b"), fontName="Helvetica")
    table_header_style = ParagraphStyle("THStyle", parent=styles["Normal"], fontSize=8.5, leading=11, textColor=colors.white, fontName="Helvetica-Bold", alignment=1)
    tc_sesion = ParagraphStyle("TCSesion", parent=styles["Normal"], fontSize=8.2, leading=10.5, textColor=colors.HexColor("#0f172a"), fontName="Helvetica-Bold", alignment=1)
    tc_theme = ParagraphStyle("TCTheme", parent=styles["Normal"], fontSize=8, leading=10.5, textColor=colors.HexColor("#0284c7"), fontName="Helvetica-Bold")
    tc_model = ParagraphStyle("TCModel", parent=styles["Normal"], fontSize=8.2, leading=11, textColor=colors.HexColor("#0f172a"), fontName="Helvetica-Bold")
    tc_exp = ParagraphStyle("TCExp", parent=styles["Normal"], fontSize=7.8, leading=10.5, textColor=colors.HexColor("#334155"), fontName="Helvetica")
    tc_btn = ParagraphStyle("TCBtn", parent=styles["Normal"], fontSize=7.8, leading=10.5, textColor=colors.HexColor("#047857"), fontName="Helvetica-Bold")
    tc_status = ParagraphStyle("TCStatus", parent=styles["Normal"], fontSize=7.5, leading=10, textColor=colors.HexColor("#475569"), fontName="Helvetica-Oblique", alignment=1)

    elements = []
    elements.append(Paragraph("🌌 CATÁLOGO MAESTRO: 21 GRANDES SIMULACIONES INTERACTIVAS 3D INTERCALADAS", title_style))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph("Plan Didáctico Intercalado: Alternancia de Anatomía Biomédica, Hitos NASA (Spitzer, Hubble, DSCOVR, Apollo, Gemini), Historia e Ingeniería", sub_style))
    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284c7"), spaceAfter=6))

    intro_p = (
        "<b>Metodología de Intercalación Temática:</b> Para evitar la fatiga cognitiva y mantener la fascinación visual permanente en el alumnado senior (60+), "
        "el bloque de creación de simuladores con IA <b>[COD]</b> alterna sesiones de <i>Anatomía y Salud Humana</i> (fotorrealismo biomédico con pulso, respiración o genética) "
        "con sesiones de <i>Grandes Hitos de la Humanidad y el Cosmos</i> (arqueología milenaria, las 5 fotos más asombrosas de la NASA, energía eólica y vulcanología). "
        "Cada experiencia incluye arquitectura de <b>Doble Botón</b>: Taller Interactivo de Pruebas de Código generado con Gemini y acceso directo al Simulador Terminado."
    )
    elements.append(Paragraph(intro_p, intro_style))
    elements.append(Spacer(1, 6))

    headers = [
        Paragraph("Sesión", table_header_style),
        Paragraph("Universo / Temática", table_header_style),
        Paragraph("Modelo Aprobado (PBR 4K / NASA)", table_header_style),
        Paragraph("Experiencia Visual e Interactiva", table_header_style),
        Paragraph("Botón 2 • Simulador Terminado", table_header_style),
        Paragraph("Estado en Aula", table_header_style)
    ]

    rows = []
    for ses, cod, univ, mod, exp, btn, _, est in SIMULACIONES_DATA:
        status_txt = f"✅ <b>{est}</b>" if "Activo" in est else f"📅 {est}"
        rows.append([
            Paragraph(f"<b>{ses}</b><br/><font color='#64748B'>{cod}</font>", tc_sesion),
            Paragraph(univ, tc_theme),
            Paragraph(mod, tc_model),
            Paragraph(exp, tc_exp),
            Paragraph(f"{btn} ↗", tc_btn),
            Paragraph(status_txt, tc_status)
        ])

    table_data = [headers] + rows
    col_widths = [54, 98, 142, 275, 138, 70]
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#f8fafc"), colors.HexColor("#ffffff")]),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))

    elements.append(t)
    elements.append(Spacer(1, 6))
    footer_text = (
        "<b>Estándar Técnico Compartido:</b> Todos los simuladores operan en el navegador sin descargas pesadas ni plugins externos, "
        "compatibles con WebGL / Babylon.js / Three.js, y garantizan una experiencia pedagógica fluida en equipos estándar."
    )
    elements.append(Paragraph(footer_text, intro_style))
    doc.build(elements)
    print(f"✅ PDF del Catálogo Maestro de 10 Simulaciones generado con éxito en: {PDF_PATH} ({os.path.getsize(PDF_PATH)} bytes)")


if __name__ == "__main__":
    build_pdf()
