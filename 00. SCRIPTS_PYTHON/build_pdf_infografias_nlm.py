#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_infografias_nlm.py
Genera las Fichas Didácticas Oficiales en PDF (Letter) para las Infografías [INFO]:
- INFO-004: La IA es la Máquina Más Grande de la Historia (Sesión 04)
- INFO-005: El Plan Maestro de Integración Vertical de IA (Sesión 05)

Usa NativePDFWriter con embebido directo de JPEG (/Filter /DCTDecode)
para que la infografía se visualice nítida y a pantalla completa dentro del PDF sin librerías externas.
"""

import os
import sys
import shutil
import struct

def get_jpeg_size(filepath):
    with open(filepath, 'rb') as f:
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
    page_w = 612.0
    page_h = 792.0

    # Dimensiones de la imagen dentro de la página
    target_img_w = 564.0
    target_img_h = (img_h / img_w) * target_img_w # ~314.5 pt
    img_x = (page_w - target_img_w) / 2.0 # 24 pt
    img_y = 385.0 # Posicion vertical

    stream_cmds = []
    
    # 1. Marco exterior
    stream_cmds.append("0.985 0.992 1.000 rg\n")
    stream_cmds.append("0.150 0.450 0.850 RG\n")
    stream_cmds.append("1.50 w\n")
    stream_cmds.append(f"20.00 20.00 {page_w - 40:.2f} {page_h - 40:.2f} re B\n")

    # 2. Cabecera
    stream_cmds.append("0.050 0.180 0.420 rg\n")
    stream_cmds.append(f"24.00 716.00 {page_w - 48:.2f} 52.00 re f\n")
    
    # Texto cabecera
    esc_hdr = escape_pdf_text(title_header)
    esc_main = escape_pdf_text(title_main)
    stream_cmds.append(f"BT /F2 8.5 Tf 0.400 0.800 1.000 rg 36.00 750.00 Td ({esc_hdr}) Tj ET\n")
    stream_cmds.append(f"BT /F2 12.0 Tf 1.000 1.000 1.000 rg 36.00 730.00 Td ({esc_main}) Tj ET\n")

    # 3. Marco y Renderizado de la Imagen JPG
    stream_cmds.append("0.020 0.050 0.120 rg\n")
    stream_cmds.append("0.200 0.500 0.850 RG\n")
    stream_cmds.append("1.00 w\n")
    stream_cmds.append(f"{img_x - 3:.2f} {img_y - 3:.2f} {target_img_w + 6:.2f} {target_img_h + 6:.2f} re B\n")
    
    # Dibujar la imagen con operador Do
    stream_cmds.append("q\n")
    stream_cmds.append(f"{target_img_w:.2f} 0 0 {target_img_h:.2f} {img_x:.2f} {img_y:.2f} cm\n")
    stream_cmds.append("/Im1 Do\n")
    stream_cmds.append("Q\n")

    # 4. Cuadro explicativo inferior: Los 4 pilares de la infografia
    box_y = 190.0
    box_h = 185.0
    stream_cmds.append("0.950 0.980 1.000 rg\n")
    stream_cmds.append("0.180 0.550 0.850 RG\n")
    stream_cmds.append("1.00 w\n")
    stream_cmds.append(f"28.00 {box_y:.2f} {page_w - 56:.2f} {box_h:.2f} re B\n")

    stream_cmds.append(f"BT /F2 9.2 Tf 0.050 0.250 0.550 rg 40.00 {box_y + box_h - 18:.2f} Td (RESUMEN DIDACTICO VISUAL DE LA INFOGRAFIA) Tj ET\n")
    
    desc_lines = wrap_text(desc_text, 114)
    y_cur = box_y + box_h - 30
    for dl in desc_lines:
        stream_cmds.append(f"BT /F1 7.8 Tf 0.150 0.200 0.250 rg 40.00 {y_cur:.2f} Td ({escape_pdf_text(dl)}) Tj ET\n")
        y_cur -= 10.5

    y_cur -= 4
    for pt_title, pt_desc in key_points:
        stream_cmds.append(f"BT /F2 8.0 Tf 0.080 0.350 0.700 rg 40.00 {y_cur:.2f} Td ({escape_pdf_text(pt_title)}) Tj ET\n")
        y_cur -= 10.0
        pt_lines = wrap_text(pt_desc, 114)
        for ptl in pt_lines:
            stream_cmds.append(f"BT /F1 7.4 Tf 0.200 0.250 0.300 rg 40.00 {y_cur:.2f} Td ({escape_pdf_text(ptl)}) Tj ET\n")
            y_cur -= 9.5
        y_cur -= 3.0

    # 5. Preguntas de Reflexion para Gemini en el Aula
    q_box_y = 42.0
    q_box_h = 138.0
    stream_cmds.append("0.990 0.980 0.950 rg\n")
    stream_cmds.append("0.800 0.500 0.100 RG\n")
    stream_cmds.append("1.00 w\n")
    stream_cmds.append(f"28.00 {q_box_y:.2f} {page_w - 56:.2f} {q_box_h:.2f} re B\n")

    stream_cmds.append(f"BT /F2 8.8 Tf 0.700 0.350 0.050 rg 40.00 {q_box_y + q_box_h - 16:.2f} Td (PREGUNTAS DE DIALOGO CON GEMINI EN EL AULA:) Tj ET\n")
    
    y_q = q_box_y + q_box_h - 30
    for q_idx, (q_t, q_d) in enumerate(questions, 1):
        stream_cmds.append(f"BT /F2 7.6 Tf 0.100 0.200 0.300 rg 40.00 {y_q:.2f} Td ({escape_pdf_text(f'Pregunta {q_idx} • {q_t}')}) Tj ET\n")
        y_q -= 9.5
        q_lines = wrap_text(q_d, 114)
        for ql in q_lines:
            stream_cmds.append(f"BT /F1 7.2 Tf 0.250 0.300 0.350 rg 40.00 {y_q:.2f} Td ({escape_pdf_text(ql)}) Tj ET\n")
            y_q -= 9.0
        y_q -= 3.5

    # Pie de pagina
    stream_cmds.append("0.800 0.850 0.900 RG\n")
    stream_cmds.append(f"28.00 32.00 {page_w - 56:.2f} 32.00 m {page_w - 28:.2f} 32.00 l S\n")
    stream_cmds.append(f"BT /F2 7.0 Tf 0.300 0.400 0.500 rg 36.00 24.00 Td ({escape_pdf_text('CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • INFOGRAFIA OFICIAL [INFO]')}) Tj ET\n")
    
    content_stream = "".join(stream_cmds).encode('latin1', errors='replace')

    # Estructura de Objetos PDF
    # Obj 1: Catalog
    # Obj 2: Pages
    # Obj 3: Font F1 (Helvetica)
    # Obj 4: Font F2 (Helvetica-Bold)
    # Obj 5: Font F3 (Helvetica-Oblique)
    # Obj 6: Image XObject (/Im1)
    # Obj 7: Page
    # Obj 8: Contents stream
    
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

    page_obj = f"""<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 {page_w} {page_h}]
/Resources <<
  /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >>
  /XObject << /Im1 6 0 R >>
>>
/Contents 8 0 R
>>""".encode('ascii')

    contents_obj = f"""<<
/Length {len(content_stream)}
>>
stream
""".encode('ascii') + content_stream + b"\nendstream"

    all_objs = [
        b'<< /Type /Catalog /Pages 2 0 R >>',
        b'<< /Type /Pages /Kids [7 0 R] /Count 1 >>',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>',
        image_xobject,
        page_obj,
        contents_obj
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
    
    print(f"✅ PDF de infografía generado exitosamente: {output_pdf_path}")

def generate_all_infografias():
    root_s4 = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion"
    root_s5 = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/05_Sesion"
    root_s6 = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/06_Sesion"
    master_dir = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/15. [INFO] BLOQUE_15_INFOGRAFIAS_Y_NOVEDADES_IA/Lote_01_al_20"

    # Purgar residuos obsoletos de INFO-005 Plan Maestro
    old_info5_jpg = os.path.join(master_dir, "INFO-005_El_Plan_Maestro_de_Integracion_Vertical_de_IA.jpg")
    old_info5_pdf = os.path.join(master_dir, "INFO-005_El_Plan_Maestro_de_Integracion_Vertical_de_IA.pdf")
    if os.path.exists(old_info5_jpg):
        os.remove(old_info5_jpg)
    if os.path.exists(old_info5_pdf):
        os.remove(old_info5_pdf)

    # Renombrar en Bloque 15 si existía INFO-006 La Ruptura de Internet -> INFO-007 para no colisionar
    ruptura_old = os.path.join(master_dir, "INFO-006_La_Ruptura_de_Internet_Agentes_de_IA_vs_Modelo_Publicitario.jpg")
    ruptura_new = os.path.join(master_dir, "INFO-007_La_Ruptura_de_Internet_Agentes_de_IA_vs_Modelo_Publicitario.jpg")
    if os.path.exists(ruptura_old) and not os.path.exists(ruptura_new):
        os.rename(ruptura_old, ruptura_new)
        print("📦 Renombrado INFO-006 Ruptura de Internet a INFO-007")

    # Copiar Ficha Google Flow a Bloque 15 si está en Sesión 05
    flow_s5 = os.path.join(root_s5, "1. INFO-005_Taller_Google_Flow_Video_con_IA.pdf")
    flow_master = os.path.join(master_dir, "INFO-005_Taller_Google_Flow_Video_con_IA.pdf")
    if os.path.exists(flow_s5):
        shutil.copy2(flow_s5, flow_master)

    # INFOGRAFÍA 4 (Sesión 04)
    jpg4 = os.path.join(master_dir, "INFO-004_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.jpg")
    dest_jpg4 = os.path.join(root_s4, "1. INFO-004_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.jpg")
    dest_pdf4 = os.path.join(root_s4, "1. INFO-004_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.pdf")
    master_pdf4 = os.path.join(master_dir, "INFO-004_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.pdf")

    if os.path.exists(jpg4):
        shutil.copy2(jpg4, dest_jpg4)
        create_infografia_pdf(
            dest_pdf4,
            jpg4,
            "SESION 04 • INFOGRAFIA Y NOVEDADES IA [INFO-004]",
            "La IA es la Maquina Mas Grande de la Historia",
            "La Inteligencia Artificial no flota en una nube abstracta; es una gigantesca cadena industrial de 7 niveles fisicos interconectados en todo el planeta con inversiones previstas de mas de un billon de dolares anuales.",
            [
                ("Los 7 Pisos de la Gran Maquina:", "Piso 1 Modelo -> Piso 2 Chip -> Piso 3 Fabrica (TSMC) -> Piso 4 Litografia (ASML) -> Piso 5 Memoria (HBM) -> Piso 6 Centro de Datos -> Piso 7 Mundo Fisico (cobre, agua y turbinas)."),
                ("Los 4 Frenos Fisicos de la Expansion:", "1. Energia Electrica (consumira tanto como Japon en 2030) | 2. Escasez de Memoria HBM | 3. Mineria del Cobre (abrir una mina toma de 17 a 29 anos) | 4. Falta de electricistas y mano de obra cualificada.")
            ],
            [
                ("El Impacto Economico:", "Gemini, ¿por que se compara la infraestructura de IA (2,5% PIB) con el ferrocarril del siglo XIX (6% PIB) en lugar de una simple burbuja punto com?"),
                ("El Agua y la Electricidad en el Hogar:", "Gemini, ¿como pueden convivir los centros de datos masivos con las necesidades de suministro de agua y luz de las ciudades?"),
                ("Soberania Tecnologica:", "Gemini, ¿por que depender de una sola fabrica en Taiwan (TSMC) y una sola maquina en Holanda (ASML) convierte a la IA en un asunto geopolitico critico?")
            ]
        )
        shutil.copy2(dest_pdf4, master_pdf4)

    # INFOGRAFÍA 6 (Sesión 06) - El Plan Maestro de Integración Vertical de IA
    # Usar la nueva imagen limpia de NotebookLM
    user_img = "/Users/externo/.gemini/antigravity/brain/17d6cb63-82ca-4daa-9a67-ead6d748d2d0/.user_uploaded/media_1794779289258_a5b88413.jpg"
    dest_jpg6 = os.path.join(root_s6, "1. INFO-006_El_Plan_Maestro_de_Integracion_Vertical_de_IA.jpg")
    dest_pdf6 = os.path.join(root_s6, "1. INFO-006_El_Plan_Maestro_de_Integracion_Vertical_de_IA.pdf")
    master_jpg6 = os.path.join(master_dir, "INFO-006_El_Plan_Maestro_de_Integracion_Vertical_de_IA.jpg")
    master_pdf6 = os.path.join(master_dir, "INFO-006_El_Plan_Maestro_de_Integracion_Vertical_de_IA.pdf")

    if os.path.exists(user_img):
        shutil.copy2(user_img, dest_jpg6)
        shutil.copy2(user_img, master_jpg6)
        print("✅ Imagen actualizada copiada a Sesión 06 y Bloque 15")

    create_infografia_pdf(
        dest_pdf6,
        dest_jpg6,
        "SESION 06 • INFOGRAFIA Y NOVEDADES IA [INFO-006]",
        "El Plan Maestro de Integracion Vertical en IA",
        "Estrategia de integracion vertical inspirada en el modelo de la Standard Oil (1870): unificar en una sola arquitectura industrial desde el transporte espacial orbital y centros de datos hasta la fabricacion de silicio, modelos de IA y aplicaciones directas.",
        [
            ("Los 5 Niveles de la Piramide de Integracion:", "Nivel 1: Transporte Espacial (Starship, 200 $/kg) | Nivel 2: Conectividad Orbital (>80% masa orbital global, 10,6M usuarios) | Nivel 3: Centros de Datos (Cluster Colossus 10 GW en 2027) | Nivel 4: Fabricacion de Silicio (Proyecto Terafab de 300.000 a 500.000 M$) | Nivel 5: Software y Modelos (Herramientas para reducir coste de inferencia)."),
            ("Riesgos y Presiones del Ecosistema:", "1. Convergencia Fisica: Robots humanoides y automocion conectados al cerebro digital | 2. Alta Intensidad de Capital: CapEx trimestral de hasta 40.000 millones $ | 3. Presion Regulatoria: Riesgo de medidas antimonopolio por concentracion industrial.")
        ],
        [
            ("El Modelo Rockefeller (1870) vs Era Digital:", "Gemini, ¿en que se parece controlar la energia, los cohetes, los satelites y los chips al monopolio del 90% del refinado que consiguio Rockefeller con la Standard Oil?"),
            ("Centros de Datos y Enfriamiento Orbital:", "Gemini, ¿por que enviar servidores al espacio y conectarlos via laser en orbita podria resolver los problemas de consumo de agua y energia en tierra?"),
            ("Convergencia entre IA y Robotica Fisica:", "Gemini, ¿que ventaja competitiva tiene una empresa si su mismo modelo de IA gobierna un coche autonomo, un robot de fabrica y un satelite?")
        ]
    )
    shutil.copy2(dest_pdf6, master_pdf6)

if __name__ == '__main__':
    generate_all_infografias()
