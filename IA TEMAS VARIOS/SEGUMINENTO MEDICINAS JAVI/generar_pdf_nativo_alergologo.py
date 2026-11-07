#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_pdf_nativo_alergologo.py
Generador de PDF 100% nativo en Python estándar (sin ReportLab, sin pip, sin dependencias externas).
Crea 'Informe_Alergologo_Medicinas_Picores.pdf' con cálculo dinámico estricto de alturas de fila,
retorno de carro automático (word-wrap) para que NUNCA se monten o machaquen los textos,
y márgenes perfectamente calibrados.
Incorpora la infiltración de corticoides en cresta ilíaca izquierda (Mayo 2024).
"""

import os
import sys

def escape_pdf_text(text):
    text = str(text)
    text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    replacements = {
        'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
        'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
        'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
        '«': '<<', '»': '>>', '•': '-', '—': '-', '–': '-',
        'º': 'o', 'ª': 'a', '¿': '\xbf', '¡': '\xa1'
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def wrap_cell(text, max_chars):
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
    def __init__(self, page_width=612, page_height=792):
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

    def draw_header_footer(self, page_num, total_pages):
        # Header (pages > 1)
        if page_num > 1:
            self.draw_text(36, self.h - 26, "HISTORIAL DE FARMACOVIGILANCIA CUTÁNEA: MEDICAMENTOS Y PICORES", "F2", 8, 0.12, 0.23, 0.54)
            self.draw_text(self.w - 230, self.h - 26, "Consulta Alergología • Paciente: Javi (67 a)", "F1", 8, 0.4, 0.45, 0.55)
            self.set_stroke_color(0.8, 0.83, 0.88)
            self.set_line_width(0.5)
            self.line(36, self.h - 30, self.w - 36, self.h - 30)

        # Footer
        self.set_stroke_color(0.88, 0.9, 0.94)
        self.set_line_width(0.5)
        self.line(36, 32, self.w - 36, 32)
        self.draw_text(36, 20, "Documento Clínico Estructurado para Alergología • Registro Histórico Vital de Tratamientos", "F1", 7.5, 0.4, 0.45, 0.55)
        self.draw_text(self.w - 95, 20, f"Página {page_num} de {total_pages}", "F2", 8, 0.12, 0.23, 0.54)

    def write_to_file(self, filename):
        f1_idx, f2_idx, f3_idx = 3, 4, 5
        page_obj_indices = []
        content_obj_indices = []
        cur_obj_idx = 6

        for p_stream in self.pages:
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
                f.write(f"{idx} 0 obj\n".encode('ascii'))
                f.write(obj_bytes)
                f.write(b"\nendobj\n")
                pos = f.tell()

            xref_pos = pos
            f.write(f"xref\n0 {len(all_objs) + 1}\n".encode('ascii'))
            f.write(b"0000000000 65535 f \n")
            for xpos in xref_positions[1:]:
                f.write(f"{xpos:010d} 00000 n \n".encode('ascii'))
            f.write(b"trailer\n")
            f.write(f"<< /Size {len(all_objs) + 1} /Root 1 0 R >>\n".encode('ascii'))
            f.write(b"startxref\n")
            f.write(f"{xref_pos}\n%%EOF\n".encode('ascii'))

def build_pdf_document(out_path):
    pdf = SimplePDFWriter(612, 792)
    total_pages = 3

    # Column layout for Master Table (Total width = 540 pt, X: 36 to 576)
    # Fecha: 52, Med: 86, Fam: 74, Motivo: 64, Características: 120, ¿Se quitó?: 84, Medidas: 60
    col_w = [52, 86, 74, 64, 120, 84, 60]
    col_x = [36]
    for w in col_w:
        col_x.append(col_x[-1] + w)
    max_chars_list = [11, 19, 17, 14, 26, 18, 13]

    headers = ["Fecha", "Medicamento", "Familia / Grupo", "Motivo", "Características del Picor", "¿Se Pasó / Quitó?", "Medidas"]

    all_meds = [
        # (Fecha, Med, Fam, Motivo, Caracteristicas, Se_paso, Medidas)
        ("1997", "CLAMOXIL\n(Amoxicilina 500)", "Betalactámico\n(Penicilina)", "Amigdalitis aguda", "Sarpullido eritematoso difuso en el pecho.", "Se quitó tras suspender. En 2017 tomó Amoxicilina 750 y volvieron algunos picores.", "Suspensión. Sospecha firme de alergia."),
        ("01/02/1999", "VELMONIT 500\n(Ciprofloxacino)", "Fluorquinolona", "Amigdalitis aguda", "Sarpullido pruriginoso en el pecho + nerviosismo agudo.", "Se quitó tras la retirada del fármaco a los 3 días.", "Suspendido a los 3 días de inicio."),
        ("07/05/1999", "BRONGENIT\n(Cotrimoxazol)", "Sulfamida\n(Sulfametoxazol)", "Prostatitis", "Picores cutáneos a la 3ª pastilla. Agitación a la 5ª y 6ª.", "Se resolvieron los picores tras suspender el fármaco.", "Suspendido a la 6ª pastilla por prurito."),
        ("11/05/1999", "VIBRACINA\n(Doxiciclina)", "Tetraciclina", "Prostatitis", "Tomado 7 días completos. El último día sarpullido en costado.", "El sarpullido remitió en los días posteriores a 7 días.", "Fin de pauta; posterior disbiosis tratada."),
        ("08/10/2001", "SURNOX\n(Ofloxacino)", "Fluorquinolona", "Prostatitis", "A la 2ª pastilla picores notables en espalda + agitación.", "Al 6º día se pasaron por completo los picores (18 comp).", "Apoyo de Orfidal; el prurito cedió al día 6."),
        ("01/12/2003\n01/04/2004", "BENERVA\n(Vitamina B1)", "Vitamina\n(Tiamina)", "Suplemento vitamínico", "2003: Prurito en 1ª pastilla; granos frente/pecho. 2004: Picadura roja dedo pie.", "Se quitó por completo a los 5 días aproximadamente.", "Retirada de la B1; remisión espontánea."),
        ("01/06/2004", "MICOSPORT\n(Bifonazol)", "Antifúngico imidazólico", "Micosis cutánea (hongos)", "Eficaz contra hongos. Al 7º día brotaron granos en frente y pecho.", "Erupción papulosa tardía que remitió tras suspender.", "Suspensión al 7º día tras curar micosis."),
        ("01/08/2004", "ALPRAZOLAM\n0,25 mg", "Benzodiazepina", "Ansiedad / insomnio", "Picores sin granos visibles, como pinchitos en brazos y cabeza.", "Duró 5 días y se pasó por completo solo.", "Autolimitado; remisión en 5 días."),
        ("26/12/2006", "KLACID UNIDIA\n(Claritromicina 500)", "Macrólido (14 átomos)", "Infección respiratoria", "Picores crecientes e intensos en piernas, palpitaciones.", "Desapareció tras la interrupción inmediata del fármaco.", "Suspendido a la 3ª pastilla de urgencia."),
        ("12/03/2015", "AZITROMICINA\n500 mg", "Macrólido Azálido (15 átomos)", "Recaída gripe / faringitis", "Con la 1ª pastilla picores en ambos brazos.", "Se pasaron solos y desaparecieron a las 3 horas.", "Tolerancia posterior (en 2017 tolerado OK)."),
        ("20/04/2017", "AMOXICILINA\n750 mg", "Betalactámico\n(Penicilina)", "Extracción muela juicio", "Tomó 11 pastillas; algunos picores y palpitaciones 4ª tarde.", "Picores leves que cedieron al concluir el ciclo.", "Completó ciclo; confirma reactividad."),
        ("27/10/2022\n19/12/2025", "PERMIXON 160\n(Serenoa repens)", "Fitoterapia urológica", "PSA alto / prostatitis", "En 2022: picores aleatorios al 5º día. En 2025: en extremidades.", "En 2022 se quitaron al dejarlo (volvieron al reanudar).", "En 2022 retirada; en 2025 continuación."),
        ("17/03/2023", "PROCTOIAL\nRECTAL", "Ácido hialurónico rectal", "Fisura anal", "Aplicación cada 12 h. Escozor y picor perianal en 2ª dosis.", "Picor circunscrito a la zona de contacto mucoso.", "Uso continuado con ajuste posológico."),
        ("08/02/2024", "NASONEX\n(Mometasona)", "Corticoide nasal tópico spray", "Catarro vías altas", "Pequeños picores aleatorios con la 1ª inhalación.", "Se pasó al poco rato; tomas siguientes de 14 días OK.", "Autolimitado en min; tolerancia completa."),
        ("Mayo 2024", "INFILTRACIÓN\nCORTICOIDES", "Corticoide local\n(Infiltración parenteral)", "Dolor cresta ilíaca izq.", "Picores corporales durante 5 días tras infiltración cresta ilíaca izq.", "Duró 5 días y remitió por completo espontáneamente.", "Autolimitado en 5 días; aclaramiento del depósito."),
        ("15/01/2025", "LEVOFLOXACINO\n500 mg (7 días)", "Fluorquinolona", "Infección resp. La Moraleja", "Picores en brazos/axilas (días 1-3) y piernas (días 4-6).", "El último día ya no tuvo ningún picor.", "Crema de Urea; no precisó Aerius."),
        ("14/08/2026", "EZETIMIBA\n10 mg", "Hipolipemiante\n(Inhib. NPC1L1)", "Control colesterol c-LDL", "Prurito cutáneo generalizado migratorio durante 15 días.", "No se quitó solo; requirió medicación diaria continua.", "Aerius diario y Urea. Suspendido."),
        ("08/10/2026", "PITAVASTATINA\n(Livazo)", "Estatina hipolipemiante", "Control colesterol c-LDL", "Picores corporales difusos a la 3ª semana de tratamiento.", "Se quitó al suspender el tratamiento farmacológico.", "Aerius 1 día y retirada; vuelta a Atorvastatina."),
        ("2022 - 2026\n[CONTROL]", "ATORVASTATINA\n20 mg (Tolerado)", "Estatina hipolipemiante", "Control colesterol c-LDL", "CERO PICORES. Tolerancia cutánea excelente permanente.", "Tolerancia continuada permanente (LDL en 64).", "Fármaco tolerado. Control negativo.")
    ]

    def render_table_header(y_pos):
        pdf.set_fill_color(0.12, 0.23, 0.54) # Navy
        pdf.set_stroke_color(0.8, 0.83, 0.88)
        pdf.set_line_width(0.5)
        pdf.rect(36, y_pos - 18, 540, 18, fill=True, stroke=True)
        for i, h in enumerate(headers):
            pdf.draw_text(col_x[i] + 3, y_pos - 12.5, h, "F2", 7.5, 1, 1, 1)
        return y_pos - 18

    def render_row(y_pos, r_data, is_alt=False, is_control=False):
        wrapped_cols = []
        for c_idx in range(7):
            w_lines = wrap_cell(r_data[c_idx], max_chars_list[c_idx])
            wrapped_cols.append(w_lines)
        max_lines = max(len(w) for w in wrapped_cols)

        line_h = 9.0
        pad_top = 5.0
        pad_bot = 4.0
        h_row = max_lines * line_h + pad_top + pad_bot

        if is_control:
            bg = (0.94, 0.99, 0.95)
        elif is_alt:
            bg = (0.97, 0.98, 0.99)
        else:
            bg = (1.0, 1.0, 1.0)

        pdf.set_fill_color(*bg)
        pdf.set_stroke_color(0.8, 0.83, 0.88)
        pdf.set_line_width(0.5)
        pdf.rect(36, y_pos - h_row, 540, h_row, fill=True, stroke=True)

        for c_idx in range(7):
            cx = col_x[c_idx] + 3
            lines = wrapped_cols[c_idx]
            font = "F2" if (c_idx in [0, 1] or is_control) else "F1"
            size = 6.6 if c_idx in [4, 5] else 6.8
            r_c = 0.05 if is_control else 0.06
            g_c = 0.45 if is_control else 0.09
            b_c = 0.15 if is_control else 0.16

            cur_line_y = y_pos - pad_top - (line_h * 0.75)
            for l in lines:
                pdf.draw_text(cx, cur_line_y, l, font, size, r_c, g_c, b_c)
                cur_line_y -= line_h

        return y_pos - h_row

    # =========================================================
    # PÁGINA 1: ENCABEZADO + FILAS 0 a 8 (1997 a 2006)
    # =========================================================
    pdf.start_page()
    pdf.draw_header_footer(1, total_pages)

    pdf.draw_text(36, 755, "INFORME CLÍNICO PARA CONSULTA DE ALERGOLOGÍA", "F2", 15, 0.06, 0.09, 0.16)
    pdf.draw_text(36, 740, "HISTORIAL SISTEMATIZADO DE MEDICAMENTOS Y REACCIONES CUTÁNEAS (PICORES / SARPULLIDOS)", "F2", 9.0, 0.12, 0.23, 0.54)
    pdf.draw_text(36, 728, "Ubicación: IA TEMAS VARIOS / SEGUMINENTO MEDICINAS JAVI  |  Paciente: Javi (67 años)  |  Noviembre 2026", "F1", 7.5, 0.4, 0.45, 0.55)

    pdf.set_fill_color(0.94, 0.98, 1.0)
    pdf.set_stroke_color(0.01, 0.52, 0.78)
    pdf.set_line_width(1.0)
    pdf.rect(36, 680, 540, 40, fill=True, stroke=True)
    pdf.draw_text(42, 708, "OBJETIVO DE LA INTERCONSULTA ALERGOLÓGICA:", "F2", 8.0, 0.05, 0.29, 0.43)
    pdf.draw_text(42, 696, "Sistematización cronológica de todas las reacciones adversas dérmicas (prurito, sarpullidos, granos) tras la toma de fármacos a lo", "F1", 7.2, 0.05, 0.29, 0.43)
    pdf.draw_text(42, 686, "largo de la vida. Se detallan latencia, intensidad, si cedió espontáneamente o exigió retirada, y control negativo de fármacos tolerados.", "F1", 7.2, 0.05, 0.29, 0.43)

    pdf.draw_text(36, 663, "1. Tabla Maestra Cronológica de Fármacos y Picores (Parte 1: 1997 a 2006)", "F2", 10.0, 0.06, 0.09, 0.16)

    cur_y = 660
    cur_y = render_table_header(cur_y)

    for i in range(0, 9):
        is_alt = (i % 2 == 1)
        cur_y = render_row(cur_y, all_meds[i], is_alt=is_alt)

    pdf.end_page()

    # =========================================================
    # PÁGINA 2: FILAS 9 a 18 (2015 a 2026)
    # =========================================================
    pdf.start_page()
    pdf.draw_header_footer(2, total_pages)

    pdf.draw_text(36, 755, "1. Tabla Maestra Cronológica (Parte 2: 2015 a 2026)", "F2", 10.5, 0.06, 0.09, 0.16)
    pdf.draw_text(36, 742, "Continuación del registro histórico vital y fila de control de contraste (tolerancia sin picores):", "F1", 7.5, 0.4, 0.45, 0.55)

    cur_y = 738
    cur_y = render_table_header(cur_y)

    for i in range(9, len(all_meds)):
        is_alt = (i % 2 == 1)
        is_ctrl = (i == len(all_meds) - 1)
        cur_y = render_row(cur_y, all_meds[i], is_alt=is_alt, is_control=is_ctrl)

    pdf.set_fill_color(0.97, 0.98, 0.99)
    pdf.set_stroke_color(0.8, 0.83, 0.88)
    pdf.set_line_width(0.5)
    pdf.rect(36, cur_y - 34, 540, 28, fill=True, stroke=True)
    pdf.draw_text(42, cur_y - 15, "NOTA CLÍNICA SOBRE LA FILA DE CONTROL [ATORVASTATINA 20 mg]:", "F2", 7.5, 0.06, 0.09, 0.16)
    pdf.draw_text(42, cur_y - 26, "Demuestra que el prurito no es un efecto de clase generalizado, sino que depende de moléculas y excipientes específicos.", "F1", 7.0, 0.3, 0.35, 0.45)

    pdf.end_page()

    # =========================================================
    # PÁGINA 3: PATRONES CLÍNICOS Y PREGUNTAS AL ALERGÓLOGO
    # =========================================================
    pdf.start_page()
    pdf.draw_header_footer(3, total_pages)

    pdf.draw_text(36, 755, "2. Análisis de Patrones por Familias Farmacológicas", "F2", 10.5, 0.06, 0.09, 0.16)
    pdf.draw_text(36, 742, "El análisis sistemático del registro vital permite extraer patrones clave para orientar las pruebas de alergia:", "F1", 7.5, 0.3, 0.35, 0.45)

    # Matriz Familias
    fam_y = 730
    pdf.set_fill_color(0.06, 0.09, 0.16)
    pdf.rect(36, fam_y - 16, 540, 16, fill=True, stroke=True)
    pdf.draw_text(42, fam_y - 12, "Familia Farmacológica", "F2", 7.5, 1, 1, 1)
    pdf.draw_text(160, fam_y - 12, "Fármacos Evaluados y Reacciones Cutáneas", "F2", 7.5, 1, 1, 1)
    pdf.draw_text(365, fam_y - 12, "Hipótesis Diagnóstica / Mecanismo Sugerido", "F2", 7.5, 1, 1, 1)

    fam_rows = [
        ("Betalactámicos\n(Aminopenicilinas)",
         "• Clamoxil (1997): Sarpullido en pecho (suspendido).\n• Amoxicilina 750 (2017): Picores leves y palpitaciones.\n• RAST Amoxicilina (26/11/2002): <0,35 limítrofe.",
         "Hipersensibilidad no mediada por IgE inmediata o reactividad retardada a aminopenicilinas. Exige verificar seguridad de Cefalosporinas de 3ª generación."),
        ("Fluorquinolonas\n(Cipro, Oflo, Levo)",
         "• Ciprofloxacino (1999): Sarpullido en pecho (retirado 3d).\n• Ofloxacino (2001): Picores espalda que cedieron al 6º día.\n• Levofloxacino (2025): Picores brazos/piernas que cedieron.",
         "Degranulación mastocitaria directa no inmunológica (vía receptor MRGPRX2). Explica por qué el prurito puede atenuarse durante la pauta continuada."),
        ("Corticoides\n(Tópico nasal vs\nInfiltración local)",
         "• Nasonex spray (Feb 2024): Picor transitorio en minutos.\n• Infiltración cresta ilíaca izq. (Mayo 2024): Picores corporales\ndurante 5 días que remitieron espontáneamente al aclararse.",
         "Diferencia sustancial entre absorción tópica mucosa (reacción fugaz) y liberación parenteral de depósito (prurito sistémico transitorio autolimitado a 5 días)."),
        ("Macrólidos\n(Claritro vs Azitro)",
         "• Claritromicina (2006): Picores intensos y palpitaciones (3d).\n• Azitromicina (2015, 2017): Picores fugaces de 3 horas;\nexcelente tolerancia en tratamientos posteriores.",
         "Intolerancia al anillo de 14 átomos (Claritromicina) con tolerancia conservada al anillo azálido de 15 átomos (Azitromicina de elección)."),
        ("Hipolipemiantes\n(Ezetimiba, Pitava\nvs Atorvastatina)",
         "• Ezetimiba (2026): Prurito diario 15 días (Aerius + Urea).\n• Pitavastatina (2026): Picores a la 3ª semana (Aerius).\n• Atorvastatina 20 mg (2022-2026): CERO PICORES.",
         "Prurito dependiente de molécula específica y no efecto de clase. Atorvastatina es el fármaco de elección biológicamente neutro.")
    ]

    cur_fam_y = fam_y - 16
    for idx, (f_name, f_reac, f_hip) in enumerate(fam_rows):
        lines1 = wrap_cell(f_name, 18)
        lines2 = wrap_cell(f_reac, 38)
        lines3 = wrap_cell(f_hip, 32)
        max_l = max(len(lines1), len(lines2), len(lines3))
        h_f = max_l * 8.5 + 8

        bg = (0.97, 0.98, 0.99) if idx % 2 == 1 else (1.0, 1.0, 1.0)
        pdf.set_fill_color(*bg)
        pdf.set_stroke_color(0.8, 0.83, 0.88)
        pdf.rect(36, cur_fam_y - h_f, 540, h_f, fill=True, stroke=True)

        ly1 = cur_fam_y - 10
        for l1 in lines1:
            pdf.draw_text(42, ly1, l1, "F2", 7.0, 0.06, 0.09, 0.16)
            ly1 -= 8.5

        ly2 = cur_fam_y - 10
        for l2 in lines2:
            pdf.draw_text(160, ly2, l2, "F1", 6.6, 0.06, 0.09, 0.16)
            ly2 -= 8.5

        ly3 = cur_fam_y - 10
        for l3 in lines3:
            pdf.draw_text(365, ly3, l3, "F1", 6.6, 0.06, 0.09, 0.16)
            ly3 -= 8.5

        cur_fam_y -= h_f

    # Sección 3: Preguntas
    pdf.draw_text(36, cur_fam_y - 14, "3. Puntos Concretos de Consulta y Decisión con el Alergólogo", "F2", 10.0, 0.06, 0.09, 0.16)

    q_box_y = cur_fam_y - 24
    pdf.set_fill_color(0.12, 0.23, 0.54)
    pdf.rect(36, q_box_y - 16, 540, 16, fill=True, stroke=True)
    pdf.draw_text(42, q_box_y - 12, "Punto de Decisión Clínica", "F2", 7.5, 1, 1, 1)
    pdf.draw_text(175, q_box_y - 12, "Pregunta Concreta para la Consulta", "F2", 7.5, 1, 1, 1)
    pdf.draw_text(400, q_box_y - 12, "Impacto en la Salud del Paciente", "F2", 7.5, 1, 1, 1)

    q_rows = [
        ("1. Pruebas Cutáneas para Betalactámicos",
         "¿Procede realizar pruebas cutáneas (Prick / Intradérmica) para penicilina y amoxicilina para confirmar si existe alergia IgE o exclusión formal?",
         "Confirmar si las cefalosporinas de 3ª generación (Ceftriaxona / Cefixima) son seguras ante infecciones de orina o respiratorias."),
        ("2. Mecanismo de Quinolonas (MRGPRX2)",
         "Dado que con Ofloxacino y Levofloxacino el prurito remitió progresivamente al 6º-7º día, ¿se confirma el mecanismo pseudoalérgico no IgE?",
         "Evita vetar toda la familia de quinolonas si se requiere un rescate urológico específico bajo premedicación."),
        ("3. Corticoides Parenterales e Infiltraciones",
         "Valorar la reactividad frente a corticoides depot tras los picores de 5 días por la infiltración en cresta ilíaca izq. de Mayo 2024.",
         "Garantizar la seguridad de futuras infiltraciones osteoarticulares (ej. rodilla o columna) sin brotes de prurito."),
        ("4. Panel Seguro y Control Lipídico",
         "Fijar panel antibiótico autorizado y constatar que el prurito con Ezetimiba no contraindica Atorvastatina ni Ácido Bempedoico.",
         "Tranquilidad absoluta ante prescripciones urgentes y control de c-LDL sin riesgo dérmico ni muscular.")
    ]

    cur_q_y = q_box_y - 16
    for idx, (q_tit, q_desc, q_imp) in enumerate(q_rows):
        lines1 = wrap_cell(q_tit, 22)
        lines2 = wrap_cell(q_desc, 42)
        lines3 = wrap_cell(q_imp, 28)
        max_l = max(len(lines1), len(lines2), len(lines3))
        h_q = max_l * 8.5 + 8

        bg = (0.97, 0.98, 0.99) if idx % 2 == 1 else (1.0, 1.0, 1.0)
        pdf.set_fill_color(*bg)
        pdf.set_stroke_color(0.8, 0.83, 0.88)
        pdf.rect(36, cur_q_y - h_q, 540, h_q, fill=True, stroke=True)

        ly1 = cur_q_y - 10
        for l1 in lines1:
            pdf.draw_text(42, ly1, l1, "F2", 6.8, 0.06, 0.09, 0.16)
            ly1 -= 8.5

        ly2 = cur_q_y - 10
        for l2 in lines2:
            pdf.draw_text(175, ly2, l2, "F1", 6.6, 0.06, 0.09, 0.16)
            ly2 -= 8.5

        ly3 = cur_q_y - 10
        for l3 in lines3:
            pdf.draw_text(400, ly3, l3, "F1", 6.6, 0.06, 0.09, 0.16)
            ly3 -= 8.5

        cur_q_y -= h_q

    pdf.end_page()

    # Guardar archivo
    pdf.write_to_file(out_path)
    print(f"PDF generado con éxito: {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "Informe_Alergologo_Medicinas_Picores.pdf"
    build_pdf_document(target)
