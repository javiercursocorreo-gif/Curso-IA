#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_informe_riesgos_web_centro_v2.py
Genera un informe formal y exhaustivo de viabilidad y riesgos legales,
operativos e institucionales para la Coordinación del Centro de Mayores.
Incluye imagen de personas, LOPD, responsabilidad civil de contenidos,
alérgenos, licencias, TI municipal, ENS y accesibilidad (RD 1112/2018).
Maquetado en 3 páginas A4 con diseño ejecutivo de alto impacto.
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

def build_pdf_3pages():
    pdf = NativePDFWriter(page_width=595.28, page_height=841.89) # A4

    # ================= PAGE 1 =================
    pdf.start_page()

    # Header Banner Page 1 (Crimson Warning)
    pdf.set_fill_color(0.82, 0.2, 0.18)
    pdf.rect(0, 750, 595.28, 91.89, fill=True, stroke=False)
    pdf.draw_text(38, 804, "INFORME CRITICO DE VIABILIDAD LEGAL Y RIESGOS", font='F2', size=15, r=1, g=1, b=1)
    pdf.draw_text(38, 784, "PROYECTO: WEB DEL CENTRO MUNICIPAL DE MAYORES", font='F2', size=11, r=1, g=0.9, b=0.8)
    pdf.draw_text(38, 767, "Gobernanza, Responsabilidad Civil, RGPD, Licencias e Informatica Municipal", font='F3', size=8.5, r=1, g=1, b=1)

    # Subheader / Meta Destinatario
    pdf.set_fill_color(0.96, 0.96, 0.98)
    pdf.rect(38, 686, 519.28, 46, fill=True, stroke=False)
    pdf.set_stroke_color(0.8, 0.8, 0.85)
    pdf.set_line_width(0.8)
    pdf.rect(38, 686, 519.28, 46, fill=False, stroke=True)
    pdf.draw_text(48, 715, "DESTINATARIOS: Coordinacion del Centro, Direccion Municipal y Equipo Docente", font='F2', size=9, r=0.2, g=0.2, b=0.2)
    pdf.draw_text(48, 701, "DICTAMEN FORMAL: ALTO RIESGO DISCIPLINARIO Y JURIDICO (PROHIBIDO PASAR A PRODUCCION)", font='F2', size=8.5, r=0.8, g=0.1, b=0.1)

    y = 650
    # SECCIÓN 1: DIAGNÓSTICO
    pdf.set_fill_color(0.18, 0.24, 0.35)
    pdf.rect(38, y, 519.28, 20, fill=True, stroke=False)
    pdf.draw_text(46, y + 6, "1. EL ERROR DE FONDO: CONFUNDIR 'PROYECTO DE AULA' CON 'SERVICIO MUNICIPAL'", font='F2', size=10, r=1, g=1, b=1)

    y -= 16
    p1 = (
        "El desarrollo de una web didactica en clase de IA es un ejercicio sobresaliente de capacitacion tecnologica. "
        "Sin embargo, elevar esa maqueta a 'Web Oficial en Produccion' de un centro dependiente del Ayuntamiento introduce "
        "un laberinto de obligaciones legales y tecnicas que ni la Coordinacion del centro, ni el profesor, ni los alumnos "
        "voluntarios tienen capacidad de asumir sin incurrir en graves irregularidades administrativas y civiles."
    )
    for line in wrap_text(p1, 98):
        pdf.draw_text(40, y, line, font='F1', size=9, r=0.15, g=0.15, b=0.15)
        y -= 13

    # SECCIÓN 2: PROTECCIÓN DE DATOS, IMAGEN Y RESPONSABILIDAD CIVIL
    y -= 12
    pdf.set_fill_color(0.82, 0.2, 0.18)
    pdf.rect(38, y, 519.28, 20, fill=True, stroke=False)
    pdf.draw_text(46, y + 6, "2. CAMPO DE MINAS JURIDICO: IMAGEN DE SOCIOS, LOPD Y RESPONSABILIDAD CIVIL", font='F2', size=10, r=1, g=1, b=1)

    y -= 16
    points_s2 = [
        ("A. Derecho a la Propia Imagen y Sanciones de la AEPD (Ley 1/1982 y RGPD):",
         "Publicar fotos de excursiones, bailes de sevillanas o talleres donde aparecen socios identificables exige un consentimiento expreso, informado y firmado por escrito para difusion web publica. Sin ese archivo de consentimientos custodiado por el Delegado de Proteccion de Datos (DPD) del Ayuntamiento, cualquier queja de un socio o familiar acarrea denuncias inmediatas ante la Agencia Espanola de Proteccion de Datos (sanciones que pueden alcanzar miles de euros para la entidad responsable)."),
        ("B. Responsabilidad Civil sobre los Contenidos de Excursiones:",
         "Si en la web se publica una excursion con un precio, horario o cobertura de seguro erroneo, o si un viaje se suspende y los socios quedan desatendidos, ¿quien asume la responsabilidad civil por danos o reclamaciones economicas? La Coordinadora y quien administro la publicacion quedan legalmente expuestos al no existir una contratacion oficial ni un seguro publico que ampare un soporte casero."),
        ("C. Informacion Alimentaria Obligatoria y Alergenos (Reglamento UE 1169/2011):",
         "Publicar el Menu del Dia de la cafeteria en una web abierta no es un simple folleto: la ley europea obliga a identificar minuciosamente los 14 alergenos oficiales (gluten, frutos secos, lactosa, etc.). Un error de transcripcion por OCR o despiste de un voluntario que provoque una reaccion alergica grave en un usuario generaria responsabilidad civil y sanitaria directa contra el centro.")
    ]
    for title, desc in points_s2:
        pdf.draw_text(44, y, title, font='F2', size=8.8, r=0.75, g=0.12, b=0.12)
        y -= 12
        for line in wrap_text(desc, 96):
            pdf.draw_text(52, y, line, font='F1', size=8.5, r=0.2, g=0.2, b=0.2)
            y -= 11.5
        y -= 4

    pdf.draw_text(265, 20, "Pagina 1 de 3", font='F1', size=8.5, r=0.5, g=0.5, b=0.5)
    pdf.end_page()

    # ================= PAGE 2 =================
    pdf.start_page()

    # Header Banner Page 2
    pdf.set_fill_color(0.18, 0.24, 0.35)
    pdf.rect(0, 765, 595.28, 76.89, fill=True, stroke=False)
    pdf.draw_text(38, 805, "INFORME CRITICO DE VIABILIDAD LEGAL Y RIESGOS", font='F2', size=14, r=1, g=1, b=1)
    pdf.draw_text(38, 786, "Informatica Municipal, Esquema Nacional de Seguridad y Titularidad", font='F3', size=9.5, r=0.9, g=0.95, b=1)

    y = 725
    # SECCIÓN 3: EL MURO DE INFORMÁTICA MUNICIPAL
    pdf.set_fill_color(0.82, 0.2, 0.18)
    pdf.rect(38, y, 519.28, 20, fill=True, stroke=False)
    pdf.draw_text(46, y + 6, "3. EL MURO DE INFORMATICA MUNICIPAL (CPD/TI) Y EL ESQUEMA NACIONAL DE SEGURIDAD", font='F2', size=10, r=1, g=1, b=1)

    y -= 16
    points_s3 = [
        ("A. Imposibilidad de Instalar Software en los Ordenadores Municipales:",
         "Los equipos de las dependencias municipales estan gestionados por el Departamento de Informatica (CPD) del Ayuntamiento bajo perfiles blindados sin permisos de administrador. Instalar software de desarrollo como Antigravity, Node.js, Python o extensiones no homologadas esta tajantemente vetado por politicas de ciberseguridad. Cualquier solicitud de instalacion sera denegada por los tecnicos municipales."),
        ("B. Servidores en GitHub Pages vs. Esquema Nacional de Seguridad (ENS - RD 311/2022):",
         "La ley exige que los servicios web municipales se alojen en infraestructuras auditadas bajo el ENS dentro del territorio europeo. Alojar la web del centro en GitHub Pages (servidores extranjeros de Microsoft en EE.UU.) provocara que, en cuanto el area de Informatica del Ayuntamiento lo detecte, ordene el cierre cautelar fulminante por riesgo de ciberseguridad y uso ilicito de la marca municipal."),
        ("C. Obligacion Juridica de Accesibilidad Universal (Real Decreto 1112/2018):",
         "Toda web del sector publico esta obligada por ley a cumplir el estandar europeo EN 301 549 (WCAG 2.1 nivel AA) y a publicar una Declaracion Oficial de Accesibilidad auditada y firmada. El incumplimiento o cualquier queja formal por falta de contraste o barreras motoras abre expedientes sancionadores inmediatos contra el consistorio.")
    ]
    for title, desc in points_s3:
        pdf.draw_text(44, y, title, font='F2', size=8.8, r=0.75, g=0.12, b=0.12)
        y -= 12
        for line in wrap_text(desc, 96):
            pdf.draw_text(52, y, line, font='F1', size=8.5, r=0.2, g=0.2, b=0.2)
            y -= 11.5
        y -= 4

    # SECCIÓN 4: PROBLEMAS DE TITULARIDAD, LICENCIAS Y CUENTAS
    y -= 8
    pdf.set_fill_color(0.18, 0.24, 0.35)
    pdf.rect(38, y, 519.28, 20, fill=True, stroke=False)
    pdf.draw_text(46, y + 6, "4. PROBLEMAS DE PROPIEDAD, CUENTAS DE USUARIO Y CONTRATACION PUBLICA", font='F2', size=10, r=1, g=1, b=1)

    y -= 16
    points_s4 = [
        ("A. ¿A Nombre de Quien se Abren las Cuentas y Quien las Paga?:",
         "Un empleado publico (como la Coordinadora) no puede dar de alta cuentas de pago o suscripciones a servicios comerciales de IA en la nube a titulo institucional sin tramitar un contrato menor de suministro por Intervencion municipal. Si la cuenta se abre a nombre particular del profesor o de un voluntario, se comete una irregularidad administrativa de consecuencias legales."),
        ("B. La Trampa de la Custodia Privada de Servicios Publicos:",
         "Si el profesor o los voluntarios abandonan el centro, las contraseñas, los datos y el codigo quedan desamparados. Nadie en el Ayuntamiento sabe como modificar esa infraestructura; el centro quedaria rehén de una solucion privada sin soporte institucional.")
    ]
    for title, desc in points_s4:
        pdf.draw_text(44, y, title, font='F2', size=8.8, r=0.2, g=0.3, b=0.5)
        y -= 12
        for line in wrap_text(desc, 96):
            pdf.draw_text(52, y, line, font='F1', size=8.5, r=0.2, g=0.2, b=0.2)
            y -= 11.5
        y -= 4

    pdf.draw_text(265, 20, "Pagina 2 de 3", font='F1', size=8.5, r=0.5, g=0.5, b=0.5)
    pdf.end_page()

    # ================= PAGE 3 =================
    pdf.start_page()

    # Header Banner Page 3
    pdf.set_fill_color(0.18, 0.24, 0.35)
    pdf.rect(0, 765, 595.28, 76.89, fill=True, stroke=False)
    pdf.draw_text(38, 805, "INFORME CRITICO DE VIABILIDAD LEGAL Y RIESGOS", font='F2', size=14, r=1, g=1, b=1)
    pdf.draw_text(38, 786, "Esclavitud del Mantenimiento, Solucion Estrategica y Conclusiones", font='F3', size=9.5, r=0.9, g=0.95, b=1)

    y = 725
    # SECCIÓN 5: LA ESCLAVITUD DEL MANTENIMIENTO
    pdf.set_fill_color(0.82, 0.2, 0.18)
    pdf.rect(38, y, 519.28, 20, fill=True, stroke=False)
    pdf.draw_text(46, y + 6, "5. LA ESCLAVITUD OPERATIVA: CADUCIDAD DIARIA Y LLAMADAS A DESHORAS", font='F2', size=10, r=1, g=1, b=1)

    y -= 16
    points_s5 = [
        ("A. Ciclo de Vida Ininterrumpido de los Contenidos:",
         "Las excursiones se llenan y hay que cancelarlas; cuando pasan, hay que quitarlas para que nadie intente apuntarse a hechos pasados; los menus de catering cambian cada semana; los profesores de sevillanas enferman; se convocan avisos urgentes. Una web desactualizada durante dos semanas proyecta una imagen de abandono y negligencia institucional."),
        ("B. Fragilidad Absoluta del Voluntariado Sénior:",
         "Los alumnos voluntarios no tienen contrato ni obligacion laboral: enferman, viajan con sus familias o pierden el entusiasmo. En cuanto fallen dos personas, el sistema se colapsa. El miedo natural de los mayores a 'romper la web' hara que ante el menor fallo tecnico llamen a la Coordinadora o al profesor pidiendo auxilio urgente.")
    ]
    for title, desc in points_s5:
        pdf.draw_text(44, y, title, font='F2', size=8.8, r=0.75, g=0.12, b=0.12)
        y -= 12
        for line in wrap_text(desc, 96):
            pdf.draw_text(52, y, line, font='F1', size=8.5, r=0.2, g=0.2, b=0.2)
            y -= 11.5
        y -= 4

    # SECCIÓN 6: DICTAMEN FINAL Y PROPUESTA ELEGANTE
    y -= 8
    pdf.set_fill_color(0.12, 0.5, 0.3) # Forest Green
    pdf.rect(38, y, 519.28, 20, fill=True, stroke=False)
    pdf.draw_text(46, y + 6, "6. DICTAMEN DEFINITIVO Y SALIDA INSTITUCIONAL ELEGANTE", font='F2', size=10, r=1, g=1, b=1)

    y -= 16
    final_points = [
        ("1. Presentar el proyecto exclusivamente como «Taller de Investigacion Senior y Fin de Curso»:",
         "La Coordinadora debe contemplar la web como un ejercicio academico brillante de lo que los alumnos mayores son capaces de disenar con IA. De este modo se reconoce el merito pedagogico sin adquirir ningun compromiso de explotacion."),
        ("2. Blindar a la Coordinadora de cualquier intento de llevar esto al Ayuntamiento:",
         "Este informe debe entregarse a la Coordinadora para que comprenda que elevar este desarrollo a produccion la situaria en una posicion de maxima vulnerabilidad administrativa frente a Intervencion, el DPD y el CPD municipal."),
        ("3. La Via Legal Oficial (Si el Centro requiere presencia web en el futuro):",
         "Si el Ayuntamiento desea una web publica, la unica via legitima es que el Departamento de Informatica municipal habilite una pestana dentro del portal corporativo del consistorio (ayuntamiento.es/mayores). Los alumnos pueden colaborar aportando ideas, pero los servidores, la LOPD y el soporte deben quedar 100% en manos de los tecnicos municipales.")
    ]
    for title, desc in final_points:
        pdf.draw_text(44, y, title, font='F2', size=8.8, r=0.1, g=0.45, b=0.2)
        y -= 12
        for line in wrap_text(desc, 96):
            pdf.draw_text(52, y, line, font='F1', size=8.5, r=0.15, g=0.15, b=0.15)
            y -= 11.5
        y -= 4

    pdf.draw_text(265, 20, "Pagina 3 de 3", font='F1', size=8.5, r=0.5, g=0.5, b=0.5)
    pdf.end_page()

    pdf.write_to_file(OUTPUT_PDF)
    print(f"✅ Informe de Viabilidad de 3 páginas generado exitosamente en: {OUTPUT_PDF}")

if __name__ == '__main__':
    build_pdf_3pages()
