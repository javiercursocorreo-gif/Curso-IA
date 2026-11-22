#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_info_005_aula_invertida.py
Sustituye en la Sesión 05 la antigua ficha repetida de Google Flow por la nueva
Infografía oficial de Google IA: "El futuro de la educación según Google IA: El aula invertida".

Acciones:
1. Copia la imagen subida por el usuario a Sesión 05 y Bloque 15.
2. Genera el PDF Widescreen 16:9 de 2 páginas (Pág 1: Infografía HD, Pág 2: Guía didáctica y preguntas).
3. Genera el visor HTML HD interactivo: VISOR_INFOGRAFIA_AULA_INVERTIDA_GOOGLE_IA.html.
4. Elimina la ficha obsoleta repetida de Google Flow en S05 y Bloque 15.
5. Actualiza MAPA_SESION_05.html y MAPA_CLASE_SESION_05.html con la nueva tarjeta y renumeración correlativa (#01, #02...).
"""

import os
import sys
import shutil
import struct
import re

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
S05_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/05_Sesion")
B15_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/15. [INFO] BLOQUE_15_INFOGRAFIAS_Y_NOVEDADES_IA/Lote_01_al_20")

USER_IMG = "/Users/externo/.gemini/antigravity/brain/20b634df-ef73-4425-bdf6-207788a8b014/.user_uploaded/media_1795344806996_b64c6f6c.jpg"

DEST_JPG_NAME = "1. INFO-005_El_Futuro_de_la_Educacion_segun_Google_IA_El_Aula_Invertida.jpg"
DEST_PDF_NAME = "1. INFO-005_El_Futuro_de_la_Educacion_segun_Google_IA_El_Aula_Invertida.pdf"
B15_JPG_NAME = "INFO-005_El_Futuro_de_la_Educacion_segun_Google_IA_El_Aula_Invertida.jpg"
B15_PDF_NAME = "INFO-005_El_Futuro_de_la_Educacion_segun_Google_IA_El_Aula_Invertida.pdf"

VISOR_HTML_NAME = "VISOR_INFOGRAFIA_AULA_INVERTIDA_GOOGLE_IA.html"

def get_jpeg_size(image_path):
    with open(image_path, 'rb') as f:
        data = f.read()
    i = 0
    while i < len(data) - 8:
        if data[i:i+2] in (b'\xff\xc0', b'\xff\xc2'):
            h, w = struct.unpack('>HH', data[i+5:i+9])
            return w, h
        i += 1
    return 1024, 571

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

def create_infografia_pdf(output_pdf_path, jpg_image_path, title_header, title_main, desc_text, key_points, questions):
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
    
    with open(jpg_image_path, 'rb') as f:
        jpg_bytes = f.read()
    
    img_w, img_h = get_jpeg_size(jpg_image_path)
    page_w = 1024.0
    page_h = 571.0

    # PÁGINA 1: INFOGRAFÍA HORIZONTAL (16:9) FULL-SCREEN
    stream_p1_cmds = f"q\n{page_w:.2f} 0 0 {page_h:.2f} 0.00 0.00 cm\n/Im1 Do\nQ\n"
    content_stream_p1 = stream_p1_cmds.encode('ascii')

    # PÁGINA 2: GUÍA DIDÁCTICA Y PREGUNTAS EN FORMATO WIDESCREEN
    stream_p2_cmds = []
    
    # 1. Fondo suave y marco
    stream_p2_cmds.append("0.985 0.992 1.000 rg\n")
    stream_p2_cmds.append("0.150 0.450 0.850 RG\n")
    stream_p2_cmds.append("1.50 w\n")
    stream_p2_cmds.append(f"16.00 16.00 {page_w - 32:.2f} {page_h - 32:.2f} re B\n")

    # 2. Cabecera Widescreen
    stream_p2_cmds.append("0.050 0.180 0.420 rg\n")
    stream_p2_cmds.append(f"20.00 505.00 {page_w - 40:.2f} 46.00 re f\n")
    
    esc_hdr = escape_pdf_text(title_header)
    esc_main = escape_pdf_text(title_main)
    stream_p2_cmds.append(f"BT /F2 9.0 Tf 0.400 0.800 1.000 rg 36.00 534.00 Td ({esc_hdr}) Tj ET\n")
    stream_p2_cmds.append(f"BT /F2 13.5 Tf 1.000 1.000 1.000 rg 36.00 514.00 Td ({esc_main}) Tj ET\n")

    # 3. Dos Columnas Didácticas
    col_w = 478.0
    col_h = 445.0
    col_y = 50.0

    # COLUMNA 1 (IZQUIERDA): RESUMEN Y PILARES
    c1_x = 24.0
    stream_p2_cmds.append("0.950 0.980 1.000 rg\n")
    stream_p2_cmds.append("0.180 0.550 0.850 RG\n")
    stream_p2_cmds.append("1.00 w\n")
    stream_p2_cmds.append(f"{c1_x:.2f} {col_y:.2f} {col_w:.2f} {col_h:.2f} re B\n")

    stream_p2_cmds.append(f"BT /F2 9.5 Tf 0.050 0.250 0.550 rg {c1_x + 14:.2f} {col_y + col_h - 20:.2f} Td (RESUMEN DIDACTICO Y ARQUITECTURA VISUAL) Tj ET\n")
    
    y_c1 = col_y + col_h - 36
    desc_lines = wrap_text(desc_text, 70)
    for dl in desc_lines:
        stream_p2_cmds.append(f"BT /F1 8.2 Tf 0.150 0.200 0.250 rg {c1_x + 14:.2f} {y_c1:.2f} Td ({escape_pdf_text(dl)}) Tj ET\n")
        y_c1 -= 11.5

    y_c1 -= 6
    for pt_title, pt_desc in key_points:
        stream_p2_cmds.append(f"BT /F2 8.5 Tf 0.080 0.350 0.700 rg {c1_x + 14:.2f} {y_c1:.2f} Td ({escape_pdf_text(pt_title)}) Tj ET\n")
        y_c1 -= 11.0
        pt_lines = wrap_text(pt_desc, 70)
        for ptl in pt_lines:
            stream_p2_cmds.append(f"BT /F1 7.8 Tf 0.200 0.250 0.300 rg {c1_x + 14:.2f} {y_c1:.2f} Td ({escape_pdf_text(ptl)}) Tj ET\n")
            y_c1 -= 10.5
        y_c1 -= 5.0

    # COLUMNA 2 (DERECHA): PREGUNTAS DE DIÁLOGO CON GEMINI
    c2_x = 522.0
    stream_p2_cmds.append("0.995 0.985 0.950 rg\n")
    stream_p2_cmds.append("0.850 0.520 0.100 RG\n")
    stream_p2_cmds.append("1.00 w\n")
    stream_p2_cmds.append(f"{c2_x:.2f} {col_y:.2f} {col_w:.2f} {col_h:.2f} re B\n")

    stream_p2_cmds.append(f"BT /F2 9.5 Tf 0.750 0.380 0.050 rg {c2_x + 14:.2f} {col_y + col_h - 20:.2f} Td (PREGUNTAS DE DIALOGO CON GEMINI EN EL AULA:) Tj ET\n")
    
    y_c2 = col_y + col_h - 36
    for q_idx, (q_t, q_d) in enumerate(questions, 1):
        stream_p2_cmds.append(f"BT /F2 8.5 Tf 0.100 0.200 0.300 rg {c2_x + 14:.2f} {y_c2:.2f} Td ({escape_pdf_text(f'Pregunta {q_idx} - {q_t}')}) Tj ET\n")
        y_c2 -= 11.0
        q_lines = wrap_text(q_d, 70)
        for ql in q_lines:
            stream_p2_cmds.append(f"BT /F1 7.8 Tf 0.250 0.300 0.350 rg {c2_x + 14:.2f} {y_c2:.2f} Td ({escape_pdf_text(ql)}) Tj ET\n")
            y_c2 -= 10.5
        y_c2 -= 6.0

    # 4. Pie de página Widescreen
    stream_p2_cmds.append("0.800 0.850 0.900 RG\n")
    stream_p2_cmds.append(f"24.00 34.00 {page_w - 48:.2f} 34.00 m {page_w - 24:.2f} 34.00 l S\n")
    stream_p2_cmds.append(f"BT /F2 7.5 Tf 0.300 0.400 0.500 rg 36.00 24.00 Td ({escape_pdf_text('CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) - GUIA DIDACTICA OFICIAL [INFO-005]')}) Tj ET\n")

    content_stream_p2 = "".join(stream_p2_cmds).encode('latin1', errors='replace')

    image_xobject = f"""<<
/Type /XObject
/Subtype /Image
/Width {img_w}
/Height {img_h}
/ColorSpace /DeviceRGB
/BitsPerComponent 8
/Filter /DCTDecode
/Length {len(jpg_bytes)}
>>
stream
""".encode('ascii') + jpg_bytes + b"\nendstream"

    page1_obj = f"""<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 {page_w} {page_h}]
/Resources <<
  /XObject << /Im1 6 0 R >>
>>
/Contents 8 0 R
>>""".encode('ascii')

    contents_p1_obj = f"""<<
/Length {len(content_stream_p1)}
>>
stream
""".encode('ascii') + content_stream_p1 + b"\nendstream"

    page2_obj = f"""<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 {page_w} {page_h}]
/Resources <<
  /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >>
>>
/Contents 10 0 R
>>""".encode('ascii')

    contents_p2_obj = f"""<<
/Length {len(content_stream_p2)}
>>
stream
""".encode('ascii') + content_stream_p2 + b"\nendstream"

    all_objs = [
        b'<< /Type /Catalog /Pages 2 0 R >>',
        b'<< /Type /Pages /Kids [7 0 R 9 0 R] /Count 2 >>',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>',
        image_xobject,
        page1_obj,
        contents_p1_obj,
        page2_obj,
        contents_p2_obj
    ]

    with open(output_pdf_path, 'wb') as f:
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
    
    print(f"✅ PDF Widescreen 16:9 generado: {output_pdf_path}")

def generate_visor_html(output_html_path, title, badge, img_src, pdf_href):
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, maximum-scale=1.0">
    <title>{title} - Visor HD</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            background-color: #030712;
            color: #f3f4f6;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        header {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 60px;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
            z-index: 50;
        }}
        .header-title {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .badge {{
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: #fff;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.5px;
        }}
        h1 {{
            font-size: 16px;
            font-weight: 600;
            color: #fff;
        }}
        .controls {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .btn {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #f3f4f6;
            padding: 7px 14px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
            transition: all 0.2s ease;
        }}
        .btn:hover {{
            background: rgba(255, 255, 255, 0.18);
            border-color: rgba(255, 255, 255, 0.3);
        }}
        .btn-primary {{
            background: linear-gradient(135deg, #0284c7, #0369a1);
            border-color: #38bdf8;
            color: #fff;
        }}
        .btn-primary:hover {{
            background: linear-gradient(135deg, #0369a1, #075985);
        }}
        #viewport {{
            flex: 1;
            margin-top: 60px;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: grab;
            touch-action: none;
        }}
        #viewport:active {{
            cursor: grabbing;
        }}
        #infografia-img {{
            max-width: 95vw;
            max-height: calc(95vh - 70px);
            object-fit: contain;
            border-radius: 10px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.1);
            transform-origin: center center;
            transition: transform 0.05s ease-out;
            user-select: none;
            -webkit-user-drag: none;
        }}
        .hint {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #94a3b8;
            font-size: 12px;
            padding: 6px 16px;
            border-radius: 20px;
            pointer-events: none;
            z-index: 40;
            transition: opacity 0.5s ease;
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-title">
            <span class="badge">{badge}</span>
            <h1>{title}</h1>
        </div>
        <div class="controls">
            <button class="btn" id="btn-zoom-in" title="Acercar">🔍 +</button>
            <button class="btn" id="btn-zoom-out" title="Alejar">🔍 -</button>
            <button class="btn" id="btn-reset" title="Restablecer tamaño">↺ Ajustar</button>
            <a href="{pdf_href}" target="_blank" class="btn btn-primary" title="Abrir Ficha Guía en PDF">📄 Ficha y Preguntas (PDF) ↗</a>
        </div>
    </header>

    <div id="viewport">
        <img id="infografia-img" src="{img_src}" alt="{title}">
    </div>

    <div class="hint" id="hint">💡 Usa la rueda del ratón o pellizca en la tablet para hacer zoom • Arrastra para explorar</div>

    <script>
        const img = document.getElementById('infografia-img');
        const viewport = document.getElementById('viewport');
        const hint = document.getElementById('hint');

        let scale = 1;
        let panX = 0;
        let panY = 0;
        let isDragging = false;
        let startX, startY;

        function updateTransform() {{
            img.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{scale}})`;
        }}

        function zoom(delta, clientX, clientY) {{
            const prevScale = scale;
            scale = Math.min(Math.max(0.6, scale + delta), 4.5);
            updateTransform();
        }}

        document.getElementById('btn-zoom-in').addEventListener('click', () => zoom(0.3));
        document.getElementById('btn-zoom-out').addEventListener('click', () => zoom(-0.3));
        document.getElementById('btn-reset').addEventListener('click', () => {{
            scale = 1;
            panX = 0;
            panY = 0;
            updateTransform();
        }});

        viewport.addEventListener('wheel', (e) => {{
            e.preventDefault();
            const delta = e.deltaY < 0 ? 0.15 : -0.15;
            zoom(delta);
        }}, {{ passive: false }});

        viewport.addEventListener('mousedown', (e) => {{
            isDragging = true;
            startX = e.clientX - panX;
            startY = e.clientY - panY;
        }});

        window.addEventListener('mousemove', (e) => {{
            if (!isDragging) return;
            panX = e.clientX - startX;
            panY = e.clientY - startY;
            updateTransform();
        }});

        window.addEventListener('mouseup', () => isDragging = false);

        // SOPORTE TÁCTIL PARA IPAD Y MÓVIL
        let touchStartDist = 0;
        let touchStartScale = 1;

        viewport.addEventListener('touchstart', (e) => {{
            if (e.touches.length === 1) {{
                isDragging = true;
                startX = e.touches[0].clientX - panX;
                startY = e.touches[0].clientY - panY;
            }} else if (e.touches.length === 2) {{
                isDragging = false;
                touchStartDist = Math.hypot(
                    e.touches[0].clientX - e.touches[1].clientX,
                    e.touches[0].clientY - e.touches[1].clientY
                );
                touchStartScale = scale;
            }}
        }}, {{ passive: true }});

        viewport.addEventListener('touchmove', (e) => {{
            if (isDragging && e.touches.length === 1) {{
                panX = e.touches[0].clientX - startX;
                panY = e.touches[0].clientY - startY;
                updateTransform();
            }} else if (e.touches.length === 2) {{
                const dist = Math.hypot(
                    e.touches[0].clientX - e.touches[1].clientX,
                    e.touches[0].clientY - e.touches[1].clientY
                );
                scale = Math.min(Math.max(0.6, touchStartScale * (dist / touchStartDist)), 4.5);
                updateTransform();
            }}
        }}, {{ passive: true }});

        viewport.addEventListener('touchend', () => isDragging = false);

        setTimeout(() => {{
            if (hint) hint.style.opacity = '0';
        }}, 5000);
    </script>
</body>
</html>
"""
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Visor HTML HD generado: {output_html_path}")

def update_maps_sesion_05():
    map_files = [
        os.path.join(S05_DIR, "MAPA_SESION_05.html"),
        os.path.join(S05_DIR, "MAPA_CLASE_SESION_05.html")
    ]
    
    new_info_card_html = f'''                    <div class="file-card file-card-special" style="background: rgba(66, 133, 244, 0.08); border-color: rgba(66, 133, 244, 0.35);">
                        <a href="1.%20INFO-005_El_Futuro_de_la_Educacion_segun_Google_IA_El_Aula_Invertida.pdf" target="_blank" class="file-card-special-top" title="Abrir Ficha Didáctica / Infografía (PDF)">
                            <div class="file-left">
                                <span class="file-num">#01 [INFO]</span>
                                <span class="file-tag tag-pdf" style="background:#2563eb; color:#fff;">INFOGRAFÍA</span>
                                <div class="file-details">
                                    <span class="file-title">El Futuro de la Educación según Google IA: El Aula Invertida</span>
                                    <span class="file-desc">Infografía NLM & Novedades IA • Tutores Personalizados y Aprendizaje Guiado con Gemini</span>
                                </div>
                            </div>
                            <span class="file-arrow">↗</span>
                        </a>
                        <a href="{VISOR_HTML_NAME}" target="_blank" class="btn-launch-interactive" style="background:linear-gradient(135deg, #1d4ed8, #2563eb); border-color:#60a5fa;" title="Ver Infografía a Pantalla Completa (HD)">
                            🖼️ Ver Infografía a Pantalla Completa (HD) ↗
                        </a>
                        <a href="1.%20INFO-005_El_Futuro_de_la_Educacion_segun_Google_IA_El_Aula_Invertida.pdf" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background:linear-gradient(135deg, #334155, #1e293b); border-color:#64748b;" title="Abrir Ficha Didáctica y Prompts (PDF)">
                            📄 Abrir Ficha Didáctica e Infografía (PDF) ↗
                        </a>
                    </div>'''

    for map_path in map_files:
        if not os.path.exists(map_path):
            continue
        with open(map_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Reemplazar la tarjeta antigua de Google Flow #01 [INFO]
        pattern_old_info = r'<div class="file-card file-card-special"[^>]*>.*?INFO-005_Taller_Google_Flow.*?</div>\s*</div>'
        m = re.search(pattern_old_info, content, re.DOTALL)
        if m:
            content = content[:m.start()] + new_info_card_html + content[m.end():]
            print(f"  🎯 Reemplazada tarjeta #01 [INFO] en {os.path.basename(map_path)}")
        else:
            # Buscar por etiqueta #01 [INFO]
            pattern_alt = r'<div class="file-card file-card-special"[^>]*>\s*<a href="[^"]*INFO-005[^"]*"[^>]*>.*?</div>\s*</div>'
            m2 = re.search(pattern_alt, content, re.DOTALL)
            if m2:
                content = content[:m2.start()] + new_info_card_html + content[m2.end():]
                print(f"  🎯 Reemplazada tarjeta alternativa #01 [INFO] en {os.path.basename(map_path)}")
            else:
                print(f"  ⚠️ No se encontró la tarjeta antigua en {os.path.basename(map_path)}")

        # Arreglar la tarjeta cómic si tenía #XX [COMIC]
        content = content.replace("#XX [COMIC]", "#02 [COMIC]")

        # Renumerar estrictamente todas las tarjetas correlativamente
        card_counter = 1
        def renumerate(match):
            nonlocal card_counter
            tag = match.group(2) or ""
            res = f'<span class="file-num">#{card_counter:02d}{tag}</span>'
            card_counter += 1
            return res

        content = re.sub(r'<span class="file-num">#(?:\d+|XX)([A-Z]?)(\s*\[[^\]]+\])?</span>', renumerate, content)

        with open(map_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  🔢 {os.path.basename(map_path)} renumerado y guardado.")

def main():
    print("==================================================================")
    print("=== [DESPLIEGUE OFICIAL: INFOGRAFÍA AULA INVERTIDA (SESIÓN 05)] ===")
    print("==================================================================")

    dest_jpg_s05 = os.path.join(S05_DIR, DEST_JPG_NAME)
    dest_pdf_s05 = os.path.join(S05_DIR, DEST_PDF_NAME)
    dest_jpg_b15 = os.path.join(B15_DIR, B15_JPG_NAME)
    dest_pdf_b15 = os.path.join(B15_DIR, B15_PDF_NAME)
    visor_html_s05 = os.path.join(S05_DIR, VISOR_HTML_NAME)

    # 1. Copiar imagen del usuario
    if os.path.exists(USER_IMG):
        shutil.copy2(USER_IMG, dest_jpg_s05)
        shutil.copy2(USER_IMG, dest_jpg_b15)
        print(f"✅ Imagen copiada a Sesión 05: {dest_jpg_s05}")
        print(f"✅ Imagen copiada a Bloque 15: {dest_jpg_b15}")
    else:
        print(f"❌ Error: No existe la imagen de usuario: {USER_IMG}")
        return

    # 2. Generar el PDF Widescreen 16:9
    desc = (
        "El lider de inteligencia artificial de Google propone transformar el modelo educativo 'invirtiendo el aula': "
        "dedicar el tiempo presencial en la escuela a la creatividad, proyectos practicos, robotica y habilidades interpersonales, "
        "y trasladar el estudio memoristico al hogar con tutores de IA personalizados al ritmo de cada alumno utilizando Google Gemini gratuito."
    )
    key_points = [
        ("La Vision de la Educacion Invertida (Flipped Classroom):",
         "1. Redefinir el rol del aula: La escuela presencial debe centrarse en talleres practicos, creatividad, emprendimiento y colaboracion.\n"
         "2. IA personalizada en casa: El aprendizaje memoristico se traslada fuera de clase, adaptado al ritmo individual sin frustracion."),
        ("El Metodo en 3 Pasos con Google Gemini en Casa:",
         "Paso 1: Seleccionar aprendizaje guiado en la aplicacion de Gemini.\n"
         "Paso 2: Subir una foto de los apuntes o tema que deseas estudiar (biologia, historia, formulas).\n"
         "Paso 3: Tutoria interactiva socratica: la IA no da la respuesta hecha, sino que guia paso a paso mediante preguntas.")
    ]
    questions = [
        ("El Rol del Abuelo Tutor con Aprendizaje Guiado:",
         "Gemini, ¿como puedo usar el modo de Aprendizaje Guiado de Gemini para ayudar a mis nietos a preparar sus examenes de biologia o historia haciendoles preguntas en lugar de darles las respuestas hechas?"),
        ("Creatividad Presencial vs Memorizacion en Casa:",
         "Gemini, ¿que ventajas tiene trasladar la memorizacion al hogar con tutores de IA y dedicar las horas de clase a debatir, programar robots y hacer experimentos en equipo?"),
        ("Paciencia Infinita y Reduccion de la Ansiedad Escolar:",
         "Gemini, ¿por que un tutor de IA personalizado que adapta el ritmo y la paciencia a cada estudiante puede reducir el fracaso escolar y el miedo a equivocarse?")
    ]

    create_infografia_pdf(
        dest_pdf_s05,
        dest_jpg_s05,
        "SESION 05 • INFOGRAFIA Y NOVEDADES IA [INFO-005]",
        "El Futuro de la Educacion segun Google IA: El Aula Invertida",
        desc,
        key_points,
        questions
    )
    shutil.copy2(dest_pdf_s05, dest_pdf_b15)
    print(f"📦 Copiado PDF a Bloque 15: {dest_pdf_b15}")

    # 3. Generar Visor HTML HD
    generate_visor_html(
        visor_html_s05,
        "El Futuro de la Educación según Google IA: El Aula Invertida",
        "SESIÓN 05 • INFOGRAFÍA DE ALTA DEFINICIÓN",
        DEST_JPG_NAME,
        DEST_PDF_NAME
    )

    # 4. Eliminar archivos antiguos de Google Flow en S05 y Bloque 15
    old_flow_s05 = os.path.join(S05_DIR, "1. INFO-005_Taller_Google_Flow_Video_con_IA.pdf")
    old_flow_b15 = os.path.join(B15_DIR, "INFO-005_Taller_Google_Flow_Video_con_IA.pdf")
    for f_del in [old_flow_s05, old_flow_b15]:
        if os.path.exists(f_del):
            try:
                os.remove(f_del)
                print(f"🗑️ Eliminado archivo obsoleto de Google Flow: {os.path.basename(f_del)}")
            except Exception as e:
                print(f"Aviso al eliminar: {e}")

    # 5. Actualizar Mapas
    update_maps_sesion_05()

    print("\n🎉 ¡INFOGRAFÍA INFO-005 DESPLEGADA CON ÉXITO ABSOLUTO EN SESIÓN 05 Y BLOQUE 15!")

if __name__ == "__main__":
    main()
