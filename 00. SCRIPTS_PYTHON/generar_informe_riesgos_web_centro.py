#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_informe_riesgos_web_centro.py
Genera un informe ejecutivo formal en PDF sobre los riesgos, inconvenientes
técnicos, legales y operativos de desplegar la Web del Centro de Mayores.
"""

import os

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/GRUPO DE TRABAJO. WEB DEL CENTRO DE MAYORES"
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "INFORME_VIABILIDAD_Y_RIESGOS_WEB_CENTRO_MAYORES.pdf")

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
    def __init__(self, page_width=595.28, page_height=841.89): # A4
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

            stream_bytes = page_stream.encode('latin1')
            c_obj = (
                f'<< /Length {len(stream_bytes)} >>\nstream\n'.encode('ascii') +
                stream_bytes +
                b'\nendstream'
            )
            all_objs.append(c_obj)

        with open(filename, 'wb') as f:
            f.write(b'%PDF-1.4\n')
            offsets = [0]
            for obj in all_objs:
                offsets.append(f.tell())
                obj_num = len(offsets) - 1
                f.write(f'{obj_num} 0 obj\n'.encode('ascii'))
                f.write(obj)
                f.write(b'\nendobj\n')

            xref_pos = f.tell()
            f.write(f'xref\n0 {len(offsets)}\n0000000000 65535 f \n'.encode('ascii'))
            for off in offsets[1:]:
                f.write(f'{off:010d} 00000 n \n'.encode('ascii'))

            trailer = (
                f'trailer\n<< /Size {len(offsets)} /Root 1 0 R >>\n'
                f'startxref\n{xref_pos}\n%%EOF\n'
            ).encode('ascii')
            f.write(trailer)

def build_pdf():
    pdf = NativePDFWriter(page_width=595.28, page_height=841.89) # A4

    # ================= PAGE 1 =================
    pdf.start_page()
    # Header Banner
    pdf.set_fill_color(0.85, 0.25, 0.2) # Crimson warning
    pdf.rect(0, 755, 595.28, 86.89, fill=True, stroke=False)
    pdf.draw_text(36, 805, "INFORME CRITICO DE VIABILIDAD TECNICA Y RIESGOS", font='F2', size=15, r=1, g=1, b=1)
    pdf.draw_text(36, 785, "PROYECTO: WEB DEL CENTRO DE MAYORES MUNICIPAL", font='F2', size=11, r=1, g=1, b=0.8)
    pdf.draw_text(36, 768, "Analisis de Gobernanza, Seguridad, Responsabilidad Civil y Servidumbre Operativa", font='F3', size=9, r=1, g=1, b=1)

    # Subheader / Meta
    pdf.set_fill_color(0.96, 0.96, 0.97)
    pdf.rect(36, 705, 523.28, 38, fill=True, stroke=False)
    pdf.set_stroke_color(0.8, 0.8, 0.85)
    pdf.set_line_width(0.8)
    pdf.rect(36, 705, 523.28, 38, fill=False, stroke=True)
    pdf.draw_text(46, 726, "DESTINATARIO: Coordinacion del Centro / Profesor / Voluntariado", font='F2', size=9, r=0.2, g=0.2, b=0.2)
    pdf.draw_text(46, 712, "DICTAMEN ESTRATEGICO: ALTO RIESGO OPERATIVO E INSTITUCIONAL (NO ASUMIR PRODUCCION)", font='F2', size=9, r=0.75, g=0.1, b=0.1)

    # Bloque 1: Diagnostico
    y = 675
    pdf.set_fill_color(0.2, 0.25, 0.35)
    pdf.rect(36, y, 523.28, 20, fill=True, stroke=False)
    pdf.draw_text(44, y + 6, "1. DIAGNOSTICO DE PARTIDA: LA 'TRAMPA DEL COMPROMISO VITALICIO'", font='F2', size=10, r=1, g=1, b=1)

    y -= 14
    diag_text = (
        "La intencion original de dotar al Centro de Mayores de una web publica accesible es loable y didacticamente "
        "enriquecedora para el aula. Sin embargo, dar el salto de un 'ejercicio didactico de clase' a un 'servicio oficial "
        "en produccion' para un centro dependiente del Ayuntamiento cruza una linea de altisimo riesgo. Convertir al profesor "
        "o a los voluntarios en los webmasters de facto de una entidad publica genera una servidumbre no retribuida, "
        "riesgos regulatorios y la certeza de quedar atrapados en un soporte tecnico 24/7 sin respaldo legal ni institucional."
    )
    for line in wrap_text(diag_text, 108):
        pdf.draw_text(36, y, line, font='F1', size=8.5, r=0.15, g=0.15, b=0.15)
        y -= 11.5

    # Bloque 2: Riesgos Institucionales y Legales
    y -= 10
    pdf.set_fill_color(0.2, 0.25, 0.35)
    pdf.rect(36, y, 523.28, 20, fill=True, stroke=False)
    pdf.draw_text(44, y + 6, "2. BARRERAS LEGALES, MUNICIPALES Y DE CIBERSEGURIDAD (CPD DEL AYUNTAMIENTO)", font='F2', size=10, r=1, g=1, b=1)

    y -= 14
    points_b2 = [
        ("A. Bloqueo de Instalacion en Ordenadores Municipales:",
         "Los equipos de centros dependientes del Ayuntamiento estan gestionados centralmente por el Servicio de Informatica (TI/CPD municipal). Tienen perfiles de usuario capados sin privilegios de administrador. Instalar software de desarrollo como Antigravity, VS Code, Git o entornos de ejecucion de IA esta terminantemente prohibido por politicas corporativas de seguridad."),
        ("B. Alojamiento en GitHub Pages vs. Esquema Nacional de Seguridad (ENS):",
         "Toda presencia web institucional de un Ayuntamiento debe someterse al ENS (Real Decreto 311/2022) y a la LOPDGDD/RGPD. Alojar la web del centro en servidores de GitHub (Microsoft, EE.UU.) fuera de los centros de datos autorizados del Ayuntamiento provocara que, en cuanto el area de Informatica municipal lo detecte, ordenen el cierre cautelar inmediato por riesgo de ciberseguridad y suplantacion de dominio."),
        ("C. Obligacion Legal de Accesibilidad (Real Decreto 1112/2018):",
         "Las webs del sector publico estan obligadas por ley a cumplir la norma europea EN 301 549 (WCAG 2.1 AA) y a disponer de una Declaracion Oficial de Accesibilidad firmada por el organo municipal competente. Cualquier queja o denuncia legal por falta de contraste, formularios inaccesibles o enlaces rotos recaera juridicamente sobre el Ayuntamiento."),
        ("D. Titularidad y Responsabilidad sobre Datos Personales:",
         "Al publicar nombres de profesores, listas de alumnos de talleres, fotos de excursiones o telefonos de contacto, se entra de lleno en la LOPD. Si la web no esta bajo el paraguas del Delegado de Proteccion de Datos (DPD) del Ayuntamiento, cualquier brecha o foto no autorizada genera responsabilidad civil directa.")
    ]
    for title, desc in points_b2:
        pdf.draw_text(40, y, title, font='F2', size=8.5, r=0.8, g=0.15, b=0.15)
        y -= 11
        for line in wrap_text(desc, 106):
            pdf.draw_text(48, y, line, font='F1', size=8, r=0.2, g=0.2, b=0.2)
            y -= 10.5
        y -= 3

    pdf.draw_text(260, 20, "Pagina 1 de 2", font='F1', size=8, r=0.5, g=0.5, b=0.5)
    pdf.end_page()

    # ================= PAGE 2 =================
    pdf.start_page()
    # Header Banner Page 2
    pdf.set_fill_color(0.2, 0.25, 0.35)
    pdf.rect(0, 785, 595.28, 56.89, fill=True, stroke=False)
    pdf.draw_text(36, 815, "INFORME DE VIABILIDAD Y RIESGOS - WEB CENTRO DE MAYORES", font='F2', size=13, r=1, g=1, b=1)
    pdf.draw_text(36, 797, "Inconvenientes Operativos, Dependencia Tecnica y Propuesta Alternativa", font='F3', size=9, r=0.9, g=0.9, b=0.9)

    # Bloque 3: Inconvenientes de Licencias y Cuentas
    y = 750
    pdf.set_fill_color(0.85, 0.25, 0.2)
    pdf.rect(36, y, 523.28, 20, fill=True, stroke=False)
    pdf.draw_text(44, y + 6, "3. PROBLEMAS DE CUENTAS, LICENCIAS Y GOBERNANZA DE ANTIGRAVITY", font='F2', size=10, r=1, g=1, b=1)

    y -= 14
    points_b3 = [
        ("A. Licenciamiento a Nombre de la Coordinadora o de un Tercero:",
         "Antigravity y las APIs de IA requieren cuentas de desarrollador y metodos de pago/facturacion. Un empleado publico (como la coordinadora) no puede registrar servicios a su nombre para el centro sin un contrato menor de suministro tramitado por Intervencion. Abrirlo a nombre particular del profesor o de un voluntario transfiere ilegalmente el coste y la custodia a un ciudadano particular."),
        ("B. Dependencia Absoluta para Secciones Nuevas (Falta de CMS Tradicional):",
         "Antigravity no es un WordPress con botones para crear paginas. Es un entorno de programacion asistida por agentes. Modificar la cabecera, reestructurar la navegacion o anadir un modulo nuevo exige modificar codigo fuente o dar instrucciones tecnicas precisas. Nadie en el centro de mayores tiene ese perfil; la dependencia de tu persona seria total y perpetua.")
    ]
    for title, desc in points_b3:
        pdf.draw_text(40, y, title, font='F2', size=8.5, r=0.7, g=0.1, b=0.1)
        y -= 11
        for line in wrap_text(desc, 106):
            pdf.draw_text(48, y, line, font='F1', size=8, r=0.2, g=0.2, b=0.2)
            y -= 10.5
        y -= 3

    # Bloque 4: La Esclavitud del Mantenimiento Diario
    y -= 8
    pdf.set_fill_color(0.85, 0.25, 0.2)
    pdf.rect(36, y, 523.28, 20, fill=True, stroke=False)
    pdf.draw_text(44, y + 6, "4. LA ESCLAVITUD DEL MANTENIMIENTO: CADUCIDAD Y FRAGILIDAD DEL VOLUNTARIADO", font='F2', size=10, r=1, g=1, b=1)

    y -= 14
    maint_text = [
        ("A. Ciclo de Vida Voraz de los Contenidos:",
         "Una web de centro de mayores no es estatica: las excursiones se llenan y hay que cerrarlas; cuando pasan, hay que quitarlas; los menus de cafeteria cambian a diario o semanalmente; los talleres sufren bajas de profesores; surgen avisos urgentes (ej. cancelacion por ola de calor). Si no se actualiza casi a diario, la web queda desfasada en dos semanas, danando la imagen publica del centro."),
        ("B. Vulnerabilidad del Grupo de Voluntarios Senior:",
         "El voluntariado no tiene obligaciones contractuales: los miembros enferman, viajan para ver a sus nietos o pierden el entusiasmo. En cuanto dos voluntarios clave fallan, el flujo de edicion se rompe. El miedo natural a 'romper la web' hara que cualquier error o descuadre de foto termine con llamadas insistentes al profesor pidiendo auxilio.")
    ]
    for title, desc in maint_text:
        pdf.draw_text(40, y, title, font='F2', size=8.5, r=0.7, g=0.1, b=0.1)
        y -= 11
        for line in wrap_text(desc, 106):
            pdf.draw_text(48, y, line, font='F1', size=8, r=0.2, g=0.2, b=0.2)
            y -= 10.5
        y -= 3

    # Bloque 5: Recomendacion Estrategica y Salida Elegante
    y -= 8
    pdf.set_fill_color(0.15, 0.55, 0.35) # Green box
    pdf.rect(36, y, 523.28, 20, fill=True, stroke=False)
    pdf.draw_text(44, y + 6, "5. DICTAMEN FINAL Y PROPUESTA ELEGANTE PARA LA COORDINADORA", font='F2', size=10, r=1, g=1, b=1)

    y -= 14
    concl_points = [
        ("• NO presentar la web como un 'servicio oficial' ni comprometerse a mantenerla en produccion.",
         "Es un error estrategico asumir el rol de proveedor informatico del Ayuntamiento sin contrato, soporte ni infraestructura."),
        ("• Presentarlo como un 'Proyecto Didactico de Aula' (Prototipo de Investigacion Senior con IA):",
         "Mostrarle a la coordinadora la maqueta como una demostracion brillante de lo que los alumnos son capaces de redactar, maquetar y reflexionar usando Gemini y la IA como herramienta formativa en el curso."),
        ("• Si el Centro o el Ayuntamiento desean una web publica oficial:",
         "La via correcta es que el Ayuntamiento asigne un apartado oficial dentro del portal municipal institucional (ej. ayuntamiento.es/mayores) gestionado por sus canales de comunicacion corporativos, donde los alumnos pueden colaborar voluntariamente aportando textos o sugerencias, pero JAMAS responsabilizandose de los servidores ni del codigo.")
    ]
    for title, desc in concl_points:
        pdf.draw_text(40, y, title, font='F2', size=8.5, r=0.1, g=0.4, b=0.2)
        y -= 11
        for line in wrap_text(desc, 106):
            pdf.draw_text(48, y, line, font='F1', size=8, r=0.15, g=0.15, b=0.15)
            y -= 10.5
        y -= 2

    pdf.draw_text(260, 20, "Pagina 2 de 2", font='F1', size=8, r=0.5, g=0.5, b=0.5)
    pdf.end_page()

    pdf.write_to_file(OUTPUT_PDF)
    print(f"✅ PDF generado exitosamente en: {OUTPUT_PDF}")

if __name__ == '__main__':
    build_pdf()
