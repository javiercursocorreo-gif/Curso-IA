#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_sesion_07_image_fiches_flow.py
Genera las 5 Fichas Didácticas de Imagen de la Sesión 07 actualizadas con
la Ampliación Oficial a Vídeo en Google Flow (50 Créditos Diarios):
- 2. EST-007: IMPRESIONISTA Y POST-IMPRESIONISTA - Gustav Klimt: Dama en Pan de Oro
- 3. PRAC-007: Protagonista de Cine Negro y Misterio Clásico (Film Noir)
- 5. INT-007: El Faro de Alejandría (120 m de altura) con su espejo reflectante
- 6. FUT-007: Año 2042: Regeneración de órganos 3D con biotinta de células madre
- 8. ARTE-007: El Hombre de Vitruvio de Leonardo da Vinci (1490)
"""

import os
import sys
import shutil

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
S07_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/07_Sesion")

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
        self.stream = []
        self.fonts = {"F1": "Helvetica", "F2": "Helvetica-Bold", "F3": "Helvetica-Oblique"}

    def start_page(self):
        self.stream = []

    def set_fill_color(self, r, g, b):
        self.stream.append(f"{r:.3f} {g:.3f} {b:.3f} rg")

    def set_stroke_color(self, r, g, b):
        self.stream.append(f"{r:.3f} {g:.3f} {b:.3f} RG")

    def set_line_width(self, w):
        self.stream.append(f"{w:.2f} w")

    def rect(self, x, y, width, height, fill=False, stroke=True):
        op = "b" if fill and stroke else ("f" if fill else "s")
        self.stream.append(f"{x:.2f} {y:.2f} {width:.2f} {height:.2f} re {op}")

    def line(self, x1, y1, x2, y2):
        self.stream.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l s")

    def draw_text(self, x, y, text, font="F1", size=10.0, r=0.0, g=0.0, b=0.0):
        safe = escape_pdf_text(text)
        self.set_fill_color(r, g, b)
        self.stream.append(f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({safe}) Tj ET")

    def end_page(self):
        pass

    def write_to_file(self, filepath):
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        content_stream = "\n".join(self.stream).encode('latin-1', 'replace')
        
        objs = []
        objs.append(b"<< /Type /Catalog /Pages 2 0 R >>")
        objs.append(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
        
        page_dict = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.w:.2f} {self.h:.2f}] "
            f"/Contents 4 0 R /Resources << /Font << "
            f"/F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >> "
            f"/F2 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >> "
            f"/F3 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >> "
            f">> >> >>"
        ).encode('latin-1')
        objs.append(page_dict)
        
        stream_dict = f"<< /Length {len(content_stream)} >>\nstream\n".encode('latin-1')
        stream_dict += content_stream + b"\nendstream"
        objs.append(stream_dict)

        with open(filepath, "wb") as f:
            f.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
            xref_offsets = []
            for i, obj in enumerate(objs, start=1):
                xref_offsets.append(f.tell())
                f.write(f"{i} 0 obj\n".encode('ascii'))
                f.write(obj)
                f.write(b"\nendobj\n")
            
            xref_start = f.tell()
            f.write(f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode('ascii'))
            for off in xref_offsets:
                f.write(f"{off:010d} 00000 n \n".encode('ascii'))
            
            f.write(f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\n".encode('ascii'))
            f.write(f"startxref\n{xref_start}\n%%EOF\n".encode('ascii'))

def build_worksheet_with_flow(
    output_path,
    tag_code,
    num_str,
    title,
    desc_concept,
    prompt_gemini,
    prompt_flow,
    theme_color_rgb=(0.15, 0.45, 0.75)
):
    pdf = NativePDFWriter(page_width=612.0, page_height=792.0)
    pdf.start_page()

    # Marco exterior elegante
    pdf.set_fill_color(0.985, 0.99, 1.0)
    pdf.set_stroke_color(theme_color_rgb[0], theme_color_rgb[1], theme_color_rgb[2])
    pdf.set_line_width(1.5)
    pdf.rect(20, 20, 572, 752, fill=True, stroke=True)

    # Cabecera principal institucional
    pdf.set_fill_color(theme_color_rgb[0] * 0.3, theme_color_rgb[1] * 0.3, theme_color_rgb[2] * 0.3)
    pdf.rect(24, 714, 564, 54, fill=True, stroke=False)

    pdf.draw_text(36, 750, f'SESION 07 • FICHA DE GENERACION VISUAL + AMPLIACION A VIDEO [{tag_code}]', font='F2', size=8.5, r=0.85, g=0.92, b=1.0)
    pdf.draw_text(36, 730, f'{num_str}: {title}', font='F2', size=11.5, r=1, g=1, b=1)

    # Sección 1: Concepto y Objetivo Visual
    pdf.set_fill_color(0.95, 0.97, 1.0)
    pdf.set_stroke_color(theme_color_rgb[0], theme_color_rgb[1], theme_color_rgb[2])
    pdf.set_line_width(1.0)
    pdf.rect(30, 615, 552, 90, fill=True, stroke=True)

    pdf.draw_text(42, 690, '1. CONCEPTO Y OBJETIVO VISUAL:', font='F2', size=9.0, r=0.08, g=0.25, b=0.55)
    lines_desc = wrap_text(desc_concept, 114)
    y_dc = 674
    for l in lines_desc:
        pdf.draw_text(42, y_dc, l, font='F1', size=7.8, r=0.15, g=0.2, b=0.25)
        y_dc -= 11.5

    # Sección 2: Prompt Maestro para Gemini (Imagen Fija)
    pdf.set_fill_color(0.98, 0.99, 1.0)
    pdf.set_stroke_color(0.2, 0.55, 0.85)
    pdf.set_line_width(1.0)
    pdf.rect(30, 445, 552, 160, fill=True, stroke=True)

    pdf.draw_text(42, 590, '2. PROMPT MAESTRO PARA GEMINI (IMAGEN FIJA DE ALTA DEFINICION):', font='F2', size=9.0, r=0.05, g=0.3, b=0.6)
    pdf.draw_text(42, 577, '(Copia este texto y pegalo en gemini.google.com para generar la imagen base de partida)', font='F3', size=7.2, r=0.4, g=0.45, b=0.5)

    # Recuadro interior Prompt Gemini
    pdf.set_fill_color(0.92, 0.96, 1.0)
    pdf.set_stroke_color(0.25, 0.6, 0.9)
    pdf.set_line_width(0.8)
    pdf.rect(40, 455, 532, 115, fill=True, stroke=True)

    lines_pg = wrap_text(prompt_gemini, 108)
    y_pg = 552
    for l in lines_pg:
        pdf.draw_text(48, y_pg, l, font='F1', size=7.3, r=0.08, g=0.15, b=0.3)
        y_pg -= 11

    # Sección 3: Ampliación Oficial con Google Flow (10 Créditos)
    pdf.set_fill_color(0.99, 0.97, 0.93)
    pdf.set_stroke_color(0.85, 0.45, 0.1)
    pdf.set_line_width(1.2)
    pdf.rect(30, 235, 552, 200, fill=True, stroke=True)

    pdf.draw_text(42, 420, '3. AMPLIACION: ¡DALE VIDA EN VIDEO CON GOOGLE FLOW! (Gasta 10 de tus 50 puntos diarios)', font='F2', size=8.8, r=0.75, g=0.3, b=0.02)
    
    steps_txt = [
        "1. Guarda la imagen: Haz clic sobre la imagen que acaba de generar Gemini y pulsa el icono de 'Descargar' (la flecha).",
        "2. Entra en Google Flow: Abre https://labs.google/flow con tu cuenta de Google y pulsa en 'Subir Imagen' (Upload).",
        "3. Pega el prompt de abajo: En el recuadro de texto de Flow, pega el siguiente prompt de movimiento y pulsa 'Generar Video'."
    ]
    y_st = 405
    for st in steps_txt:
        pdf.draw_text(42, y_st, st, font='F2' if '1.' in st or '2.' in st or '3.' in st else 'F1', size=7.2, r=0.25, g=0.2, b=0.15)
        y_st -= 11

    # Recuadro interior Prompt Flow
    pdf.set_fill_color(1.0, 0.95, 0.88)
    pdf.set_stroke_color(0.85, 0.45, 0.1)
    pdf.set_line_width(0.8)
    pdf.rect(40, 245, 532, 95, fill=True, stroke=True)

    pdf.draw_text(48, 325, 'PROMPT EXACTO DE MOVIMIENTO PARA PEGAR EN GOOGLE FLOW (labs.google/flow):', font='F2', size=7.5, r=0.6, g=0.2, b=0.0)
    lines_pf = wrap_text(prompt_flow, 108)
    y_pf = 310
    for l in lines_pf:
        pdf.draw_text(48, y_pf, l, font='F1', size=7.2, r=0.2, g=0.1, b=0.0)
        y_pf -= 11

    pdf.draw_text(48, 252, 'Resultado: En 10 segundos tendras tu escena convertida en un video MP4 listo para compartir en WhatsApp.', font='F3', size=6.8, r=0.45, g=0.3, b=0.1)

    # Pie institucional
    pdf.set_stroke_color(0.8, 0.85, 0.9)
    pdf.line(30, 222, 582, 222)
    pdf.draw_text(36, 208, f'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESION 07 • {tag_code}', font='F2', size=7.2, r=0.15, g=0.35, b=0.55)
    pdf.draw_text(36, 196, 'Metodologia Dual: Gemini (Imagen Fija) + Google Flow (Animacion de Video • 10 Creditos)', font='F3', size=6.8, r=0.45, g=0.45, b=0.55)

    pdf.end_page()
    pdf.write_to_file(output_path)
    print(f"✅ Ficha con ampliación Flow generada: {output_path}")

def safe_sync(src, dst):
    if os.path.exists(os.path.dirname(dst)):
        try:
            if not os.path.samefile(src, dst):
                shutil.copyfile(src, dst)
        except Exception:
            pass

def update_all_s07_image_fiches():
    print("=== [INICIANDO ACTUALIZACION SESION 07 CON GOOGLE FLOW EN 5 FICHAS] ===")

    # 1. EST-007: Klimt
    p_est = os.path.join(S07_DIR, "2. EST-007_IMPRESIONISTA Y POST-IMPRESIONISTA - Klimt_ Dama en Pan de Oro.pdf")
    build_worksheet_with_flow(
        output_path=p_est,
        tag_code="EST-007",
        num_str="2. EST-007",
        title="IMPRESIONISTA Y POST-IMPRESIONISTA - Gustav Klimt: Dama en Pan de Oro",
        desc_concept="Retrato modernista de la Secesion de Viena inspirado en la epoca dorada de Gustav Klimt (El Beso, Adele Bloch-Bauer): una dama elegante con peinado recogido, mirada enigmatica y una suntuosa tunica decorada con teselas, espirales doradas y patrones geometricos bizantinos de pan de oro auténtico sobre oleo.",
        prompt_gemini="\"Retrato pictorico fotorrealista al estilo de Gustav Klimt (Secesion de Viena): elegante dama de perfil sereno con peinado recogido y mantilla sutil, envuelta en una grandiosa tunica cubierta de mosaicos dorados, espirales de pan de oro reluciente y texturas bizantinas. Fondo de laminas de oro envejecido con relieves brillantes bajo luz calida de atardecer. Oleo sobre lienzo con textura tangible. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Travelling circular sutil y cinematografico alrededor de la dama. La luz dorada hace centellear las teselas y laminas de pan de oro de su tunica, creando reflejos tornasolados y un halo tenue de particulas de oro flotando en el aire calido de la estancia.\"",
        theme_color_rgb=(0.85, 0.55, 0.1)
    )
    # Sincronizar copia en master lote
    m_est = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/02. [EST] BLOQUE_2_ESTILOS_DE_IMAGEN_IA/Lote_01_al_20/EST-007_IMPRESIONISTA Y POST-IMPRESIONISTA - Klimt_ Dama en Pan de Oro.pdf")
    safe_sync(p_est, m_est)

    # 2. PRAC-007: Cine Negro (Film Noir)
    p_prac = os.path.join(S07_DIR, "3. PRAC-007_Protagonista de Cine Negro y Misterio Clásico (Film Noir).pdf")
    build_worksheet_with_flow(
        output_path=p_prac,
        tag_code="PRAC-007",
        num_str="3. PRAC-007",
        title="Protagonista de Cine Negro y Misterio Clasico (Film Noir)",
        desc_concept="Fotografia cinematografica de los anos 40 estilo Cine Negro (El Halcon Maltes, El Tercer Hombre): atmosfera nocturna de misterio, iluminacion en alto contraste (claroscuro de luz veneciana), detective solitario con gabardina y sombrero fedora caminando por calles adoquinadas mojadas que reflejan la luz de las farolas.",
        prompt_gemini="\"Fotografia cinematografica en blanco y negro puro estilo Cine Negro (Film Noir, anos 40): detective con sombrero fedora inclinado y gabardina clasica caminando bajo una llovizna suave por una calle solitaria de adoquines mojados. Iluminacion lateral de alto contraste (claroscuro) que proyecta sombras venecianas dramaticas. Humo saliendo de una alcantarilla y reflejos de farolas de gas en los charcos. Grano fino de pelicula Kodak Tri-X 400. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Camara lenta y suave en travelling frontal retrocediendo ante los pasos del detective. Las gotas de lluvia caen sobre los charcos creando ondas concentricas iluminadas, el humo de la alcantarilla se eleva en volutas densas y las sombras alargadas se proyectan dramaticas sobre la pared de ladrillo.\"",
        theme_color_rgb=(0.25, 0.35, 0.45)
    )
    m_prac = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/03. [PRAC] BLOQUE_3_TALLERES_DE_PROMPTS_PRACTICOS/Lote_01_al_20/PRAC-007_Protagonista de Cine Negro y Misterio Clásico (Film Noir).pdf")
    safe_sync(p_prac, m_prac)

    # 3. INT-007: Faro de Alejandría
    p_int = os.path.join(S07_DIR, "5. INT-007_El Faro de Alejandría (120 m de altura) con su espejo reflectante.pdf")
    build_worksheet_with_flow(
        output_path=p_int,
        tag_code="INT-007",
        num_str="5. INT-007",
        title="El Faro de Alejandria (120 m de altura) con su Espejo Reflectante",
        desc_concept="Reconstruccion historica y corte transversal de la Septima Maravilla del Mundo Antiguo (siglo III a.C., Egipto): colosal torre de piedra blanca de 120 metros en la isla de Faros con sus tres niveles (base cuadrada, torre octogonal y linterna cilindrica con la gran hoguera y el legendario espejo parabolico de bronce bruñido).",
        prompt_gemini="\"Reconstruccion arqueologica fotorrealista y corte arquitectonico del Faro de Alejandria en el ano 280 a.C.: colosal faro de 120 metros de piedra blanca caliza al borde de los acantilados de la isla de Faros, con su base cuadrada, nivel octogonal y la cima cilíndrica con la gran hoguera humeante y su espejo de bronce bruñido proyectando un haz de luz sobre las galeras del Mediterraneo al atardecer. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Plano aereo majestuoso en descenso suave orbitando alrededor de la cumbre del Faro de Alejandria. Las llamas de la gran hoguera ondean al viento expulsando chispas y humo hacia el crepusculo, el haz del espejo parabolico barre las aguas del mar y las olas rompen con fuerza contra los arrecifes de la base.\"",
        theme_color_rgb=(0.1, 0.5, 0.65)
    )
    m_int = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/05. [INT] BLOQUE_5_MUNDO_POR_DENTRO_Y_RECONSTRUCCION/Lote_01_al_20/INT-007_El Faro de Alejandría (120 m de altura) con su espejo reflectante.pdf")
    safe_sync(p_int, m_int)

    # 4. FUT-007: Regeneración de órganos 3D
    p_fut = os.path.join(S07_DIR, "6. FUT-007_Año 2042_ Regeneración de órganos 3D con biotinta de células madr.pdf")
    build_worksheet_with_flow(
        output_path=p_fut,
        tag_code="FUT-007",
        num_str="6. FUT-007",
        title="Ano 2042: Regeneracion de Organos 3D con Biotinta de Celulas Madre",
        desc_concept="Avance biomedico del futuro: bioimpresoras 3D de precision micrometrica en salas blancas hospitalarias capaces de depositar capas de hidrogel y biotinta viva con celulas madre pluripotentes, tejiendo redes capilares y matrices funcionales de organos humanos sin riesgo de rechazo inmunologico.",
        prompt_gemini="\"Fotografia cientifica y render de alta resolucion de medicina regenerativa en el ano 2042: cabezal robotico de bioimpresora 3D quirurgica depositando filamentos luminosos de biotinta de celulas madre vivas para crear un corazon humano translúcido y vascularizado. Las redes capilares resplandecen bajo luz ultravioleta suave en una campana de cultivo esterilizada con instrumental robotico avanzado. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Macro acercamiento cinematografico hacia la aguja de la bioimpresora 3D. El brazo robotico traza las fibras musculares con suavidad milimetrica, la luz violeta solidifica el hidrogel celular con destellos pulsantes y se aprecia una sutil palpitacion en la red vascular recien creada.\"",
        theme_color_rgb=(0.3, 0.25, 0.7)
    )
    m_fut = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/06. [FUT] BLOQUE_6_INFOGRAFIAS_DEL_FUTURO_SCI_FI/Lote_01_al_20/FUT-007_Año 2042_ Regeneración de órganos 3D con biotinta de células madr.pdf")
    safe_sync(p_fut, m_fut)

    # 5. ARTE-007: Hombre de Vitruvio
    p_arte = os.path.join(S07_DIR, "8. ARTE-007_El Hombre de Vitruvio de Leonardo da Vinci (1490).pdf")
    build_worksheet_with_flow(
        output_path=p_arte,
        tag_code="ARTE-007",
        num_str="8. ARTE-007",
        title="El Hombre de Vitruvio de Leonardo da Vinci (1490)",
        desc_concept="Obra cumbre del Renacimiento italiano: el estudio de las proporciones ideales del cuerpo humano trazado por Leonardo da Vinci segun los tratados del arquitecto romano Vitruvio. La figura masculina se inscribe simultaneamente en un circulo y un cuadrado, uniendo anatomia, geometria sagrada y humanismo.",
        prompt_gemini="\"Reproduccion fotorrealista de museo del 'Hombre de Vitruvio' de Leonardo da Vinci (1490): dibujo a pluma y tinta sepia sobre pergamino original amarillento con textura fibrosa y manchas historicas. La figura masculina muestra las dos posiciones de brazos y piernas perfectamente superpuestas dentro del circulo y el cuadrado geometricos, rodeada de anotaciones en escritura especular de Da Vinci. REGLA DE ORO DE IDIOMA: 100% en espanol.\"",
        prompt_flow="\"Travelling frontal lento y cinematografico sobre el pergamino renacentista. La caligrafia italiana de Da Vinci y las lineas geometricas del circulo y del cuadrado cobran un brillo dorado tenue bajo la luz parpadeante de una vela, mientras la figura anatomica realiza una transicion fluida y elegante entre ambas posturas.\"",
        theme_color_rgb=(0.55, 0.35, 0.15)
    )
    m_arte = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/08. [ARTE] BLOQUE_8_CUADROS_MAS_FAMOSOS_DE_LA_HISTORIA/Lote_01_al_20/ARTE-007_El Hombre de Vitruvio de Leonardo da Vinci (1490).pdf")
    safe_sync(p_arte, m_arte)

    print("\n✨ Las 5 fichas de imagen de Sesión 07 han sido generadas y sincronizadas con la ampliación oficial a Google Flow.")

if __name__ == '__main__':
    update_all_s07_image_fiches()
