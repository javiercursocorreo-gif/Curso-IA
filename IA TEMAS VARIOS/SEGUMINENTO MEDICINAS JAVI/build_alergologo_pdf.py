#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_alergologo_pdf.py
Genera el informe médico y alergológico actualizado en PDF:
'Informe_Alergologo_Medicinas_Picores.pdf'
dentro de 'IA TEMAS VARIOS/SEGUMINENTO MEDICINAS JAVI/'.
Sistematiza todos los medicamentos que han provocado picores, sarpullidos o prurito,
con fecha, fármaco, características de la reacción cutánea, desenlace clínico y medidas tomadas.
"""

import os
import sys

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "Informe_Alergologo_Medicinas_Picores.pdf")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#1E3A8A"))
            self.drawString(36, letter[1] - 28, "HISTORIAL DE FARMACOVIGILANCIA CUTÁNEA: MEDICAMENTOS Y PICORES")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawRightString(letter[0] - 36, letter[1] - 28, "Consulta de Alergología • Paciente: Javi (67 a)")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(36, letter[1] - 32, letter[0] - 36, letter[1] - 32)
            
        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(36, 32, letter[0] - 36, 32)
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(36, 20, "Documento Clínico Estructurado para Alergología • Registro Histórico Vital de Tratamientos")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(letter[0] - 36, 20, page_str)
        self.restoreState()


def build_pdf(output_path=PDF_PATH):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=32,
        rightMargin=32,
        topMargin=38,
        bottomMargin=38
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=21,
        textColor=colors.HexColor("#0F172A")
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#1E3A8A")
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#64748B")
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=8,
        spaceAfter=3
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=5,
        spaceAfter=2
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#334155")
    )

    body_bold = ParagraphStyle(
        'Body_Bold_Custom',
        parent=body_style,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor("#0F172A")
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=10,
        firstLineIndent=-7,
        spaceAfter=2
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.white,
        alignment=1
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9.5,
        textColor=colors.HexColor("#1E293B")
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor("#0F172A")
    )

    callout_text = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor("#0C4A6E")
    )

    story = []
    
    # ---------------------------------------------------------
    # HEADER BANNER (Page 1)
    # ---------------------------------------------------------
    story.append(Paragraph("INFORME CLÍNICO PARA CONSULTA DE ALERGOLOGÍA", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("HISTORIAL SISTEMATIZADO DE MEDICAMENTOS Y REACCIONES CUTÁNEAS (PICORES / PRURITO / SARPULLIDOS)", subtitle_style))
    story.append(Paragraph("<b>Ubicación:</b> IA TEMAS VARIOS / SEGUMINENTO MEDICINAS JAVI &nbsp;|&nbsp; <b>Paciente:</b> Javi (Varón, 67 años) &nbsp;|&nbsp; <b>Fecha:</b> Noviembre 2026", meta_style))
    story.append(Spacer(1, 5))

    # Notice Box
    notice_data = [[
        Paragraph("<b>OBJETIVO DE LA INTERCONSULTA:</b> Aportar al especialista en Alergología un dossier exhaustivo de las reacciones adversas dérmicas (prurito, sarpullidos, erupciones y sensación de picor) manifestadas tras la ingesta de medicamentos a lo largo de la vida. Se detallan con precisión la latencia, intensidad, si cedió espontáneamente o exigió retirada/antihistamínicos, y el control negativo de fármacos bien tolerados.", callout_text)
    ]]
    notice_table = Table(notice_data, colWidths=[548])
    notice_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0F9FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#0284C7")),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(notice_table)
    story.append(Spacer(1, 6))

    # ---------------------------------------------------------
    # SECCIÓN 1: TABLA MAESTRA CRONOLÓGICA (PARTE 1)
    # ---------------------------------------------------------
    story.append(Paragraph("1. Tabla Maestra Cronológica de Medicamentos y Reacciones Cutáneas", h1_style))
    
    # Column Widths: total 548 pt
    # Col widths: Fecha: 52, Med: 85, Fam: 75, Motivo: 68, Caracteristicas: 110, Se quitó: 88, Medidas: 70
    col_w = [52, 85, 75, 68, 110, 88, 70]
    
    master_rows_p1 = [
        [
            Paragraph("Fecha / Año", table_header),
            Paragraph("Medicamento y Dosis", table_header),
            Paragraph("Familia Farmacológica", table_header),
            Paragraph("Motivo", table_header),
            Paragraph("Características del Picor / Reacción", table_header),
            Paragraph("¿Se Quitó / Se Pasó? (Evolución)", table_header),
            Paragraph("Medidas Adoptadas", table_header)
        ],
        [
            Paragraph("<b>1997</b>", table_cell_bold),
            Paragraph("<b>CLAMOXIL</b><br/>(Amoxicilina 500)", table_cell),
            Paragraph("Betalactámico<br/>(Aminopenicilina)", table_cell),
            Paragraph("Amigdalitis aguda", table_cell),
            Paragraph("<b>Sarpullido eritematoso difuso en el pecho.</b>", table_cell),
            Paragraph("Se quitó al suspender. En 2017 tomó Amoxicilina 750 y volvieron a brotar <i>algunos picores</i>.", table_cell),
            Paragraph("Suspensión inmediata. Sospecha firme de reactividad a penicilinas.", table_cell)
        ],
        [
            Paragraph("<b>01/02/1999</b>", table_cell_bold),
            Paragraph("<b>VELMONIT 500</b><br/>(Ciprofloxacino)", table_cell),
            Paragraph("Fluorquinolona", table_cell),
            Paragraph("Amigdalitis aguda", table_cell),
            Paragraph("<b>Sarpullido pruriginoso en el pecho</b> + nerviosismo agudo.", table_cell),
            Paragraph("Se quitó tras suspender el fármaco a los 3 días.", table_cell),
            Paragraph("<b>Suspendido a los 3 días</b> de inicio.", table_cell)
        ],
        [
            Paragraph("<b>07/05/1999</b>", table_cell_bold),
            Paragraph("<b>BRONGENIT</b><br/>(Cotrimoxazol)", table_cell),
            Paragraph("Sulfamida<br/>(Sulfametoxazol+Trimet.)", table_cell),
            Paragraph("Prostatitis", table_cell),
            Paragraph("<b>Picores cutáneos a la 3ª pastilla.</b> Agitación a la 5ª y 6ª.", table_cell),
            Paragraph("Se resolvieron completamente los picores al interrumpir el fármaco.", table_cell),
            Paragraph("<b>Suspendido a la 6ª pastilla</b> por prurito creciente.", table_cell)
        ],
        [
            Paragraph("<b>11/05/1999</b>", table_cell_bold),
            Paragraph("<b>VIBRACINA</b><br/>(Doxiciclina)", table_cell),
            Paragraph("Tetraciclina", table_cell),
            Paragraph("Prostatitis", table_cell),
            Paragraph("Tomado 7 días completos. <b>El último día brotó sarpullido en el costado.</b>", table_cell),
            Paragraph("El sarpullido remitió en los días posteriores a terminar el ciclo de 7 días.", table_cell),
            Paragraph("Fin de pauta; posterior disbiosis gastrointestinal transitoria tratada.", table_cell)
        ],
        [
            Paragraph("<b>08/10/2001</b>", table_cell_bold),
            Paragraph("<b>SURNOX</b><br/>(Ofloxacino)", table_cell),
            Paragraph("Fluorquinolona", table_cell),
            Paragraph("Prostatitis", table_cell),
            Paragraph("A la 2ª pastilla <b>picores notables en la espalda</b> + agitación nerviosa.", table_cell),
            Paragraph("<b>Al 6º día se pasaron por completo los picores.</b> Pudo completar 18 comp. con Orfidal.", table_cell),
            Paragraph("Coadministración de Orfidal; el prurito cedió espontáneamente al 6º día.", table_cell)
        ],
        [
            Paragraph("<b>01/12/2003<br/>01/04/2004</b>", table_cell_bold),
            Paragraph("<b>BENERVA</b><br/>(Vitamina B1)", table_cell),
            Paragraph("Vitamina hidrosoluble<br/>(Tiamina)", table_cell),
            Paragraph("Suplemento vitamínico", table_cell),
            Paragraph("2003: <b>Prurito en 1ª pastilla; granos frente y pecho.</b> 2004: <b>Picadura roja pruriginosa dedo pie.</b>", table_cell),
            Paragraph("<b>Se quitó por completo a los 5 días aproximadamente.</b>", table_cell),
            Paragraph("Retirada de la vitamina B1; remisión espontánea.", table_cell)
        ],
        [
            Paragraph("<b>01/06/2004</b>", table_cell_bold),
            Paragraph("<b>MICOSPORT</b><br/>(Bifonazol)", table_cell),
            Paragraph("Antifúngico Imidazólico", table_cell),
            Paragraph("Micosis (hongos)", table_cell),
            Paragraph("Eficaz a los 7 días, pero el <b>7º día brotaron granos en frente y pecho.</b>", table_cell),
            Paragraph("Erupción papulosa tardía que remitió tras suspender al curar la micosis.", table_cell),
            Paragraph("Suspensión al séptimo día tras finalizar el tratamiento del hongo.", table_cell)
        ],
        [
            Paragraph("<b>01/08/2004</b>", table_cell_bold),
            Paragraph("<b>ALPRAZOLAM 0,25</b>", table_cell),
            Paragraph("Benzodiazepina", table_cell),
            Paragraph("Ansiedad / insomnio", table_cell),
            Paragraph("<b>Picores sin granos visibles, como pinchitos</b> en antebrazos y cabeza.", table_cell),
            Paragraph("<b>Duró 5 días y se pasó por completo.</b>", table_cell),
            Paragraph("Autolimitado; remisión en 5 días sin fármacos adicionales.", table_cell)
        ]
    ]
    
    t_p1 = Table(master_rows_p1, colWidths=col_w)
    t_p1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E3A8A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 3.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_p1)

    # Page Break to Page 2
    story.append(PageBreak())

    # ---------------------------------------------------------
    # TABLA MAESTRA CRONOLÓGICA (PARTE 2)
    # ---------------------------------------------------------
    story.append(Paragraph("1. Tabla Maestra Cronológica (Continuación: 2006 a 2026)", h1_style))
    
    master_rows_p2 = [
        [
            Paragraph("Fecha / Año", table_header),
            Paragraph("Medicamento y Dosis", table_header),
            Paragraph("Familia Farmacológica", table_header),
            Paragraph("Motivo", table_header),
            Paragraph("Características del Picor / Reacción", table_header),
            Paragraph("¿Se Quitó / Se Pasó? (Evolución)", table_header),
            Paragraph("Medidas Adoptadas", table_header)
        ],
        [
            Paragraph("<b>26/12/2006</b>", table_cell_bold),
            Paragraph("<b>KLACID UNIDIA 500</b><br/>(Claritromicina)", table_cell),
            Paragraph("Macrólido (14-C)", table_cell),
            Paragraph("Infección respiratoria", table_cell),
            Paragraph("<b>Picores crecientes e intensos en piernas</b>, taquicardia y nerviosismo.", table_cell),
            Paragraph("Desapareció tras la interrupción inmediata del antibiótico.", table_cell),
            Paragraph("<b>Suspendido a la 3ª pastilla</b> de forma obligatoria por severidad.", table_cell)
        ],
        [
            Paragraph("<b>12/03/2015</b>", table_cell_bold),
            Paragraph("<b>AZITROMICINA 500</b>", table_cell),
            Paragraph("Macrólido Azálido (15-C)", table_cell),
            Paragraph("Recaída gripe / faringitis", table_cell),
            Paragraph("Con la 1ª pastilla <b>picores en ambos brazos.</b>", table_cell),
            Paragraph("<b>Se pasaron solos y desaparecieron a las 3 horas.</b> Pastillas 2 y 3 sin síntomas.", table_cell),
            Paragraph("Ninguna; tolerancia adquirida (en 2017 tolerado sin efectos).", table_cell)
        ],
        [
            Paragraph("<b>20/04/2017</b>", table_cell_bold),
            Paragraph("<b>AMOXICILINA 750</b>", table_cell),
            Paragraph("Betalactámico<br/>(Aminopenicilina)", table_cell),
            Paragraph("Extracción muela", table_cell),
            Paragraph("Tomó 11 pastillas; <b>algunos picores leves</b> y palpitaciones la 4ª tarde.", table_cell),
            Paragraph("Picores leves transitorios que cedieron al concluir el ciclo.", table_cell),
            Paragraph("Completó la pauta con molestias leves; confirma reactividad a aminopenicilinas.", table_cell)
        ],
        [
            Paragraph("<b>27/10/2022<br/>19/12/2025</b>", table_cell_bold),
            Paragraph("<b>PERMIXON 160</b><br/>(Serenoa repens)", table_cell),
            Paragraph("Fitoterapia urológica", table_cell),
            Paragraph("PSA alto / prostatitis", table_cell),
            Paragraph("2022: Al 5º día <b>picores aleatorios</b>. 2025: Al 7º día <b>picores en brazos y piernas</b>.", table_cell),
            Paragraph("En 2022 se quitaron al retirar Permixon (al reanudar volvieron). En 2025 continuó.", table_cell),
            Paragraph("En 2022 suspensión transitoria; en 2025 continuación vigilada.", table_cell)
        ],
        [
            Paragraph("<b>17/03/2023</b>", table_cell_bold),
            Paragraph("<b>PROCTOIAL RECTAL</b>", table_cell),
            Paragraph("Ácido hialurónico tópico", table_cell),
            Paragraph("Fisura anal", table_cell),
            Paragraph("Aplicación cada 12 h. <b>Escozor y picor perianal local</b> en 2ª aplicación.", table_cell),
            Paragraph("Picor circunscrito estrictamente a la zona de contacto mucoso.", table_cell),
            Paragraph("Ajuste posológico / aplicación local vigilada.", table_cell)
        ],
        [
            Paragraph("<b>08/02/2024</b>", table_cell_bold),
            Paragraph("<b>NASONEX</b><br/>(Mometasona)", table_cell),
            Paragraph("Corticoide nasal tópico", table_cell),
            Paragraph("Catarro vías altas", table_cell),
            Paragraph("<b>Pequeños picores aleatorios</b> con la 1ª inhalación.", table_cell),
            Paragraph("<b>Se pasó al poco rato.</b> En la 2ª toma y siguientes 14 días no produjo ningún picor.", table_cell),
            Paragraph("Ninguna; autolimitado en minutos. Tolerancia completa posterior.", table_cell)
        ],
        [
            Paragraph("<b>15/01/2025</b>", table_cell_bold),
            Paragraph("<b>LEVOFLOXACINO 500</b>", table_cell),
            Paragraph("Fluorquinolona", table_cell),
            Paragraph("Infección respiratoria La Moraleja", table_cell),
            Paragraph("<b>Picores en brazos y axilas (pastillas 1-3); en piernas (pastillas 4-6).</b>", table_cell),
            Paragraph("<b>El último día ya no tuvo ningún picor.</b>", table_cell),
            Paragraph("<b>Aplicación de crema de Urea hidratante</b>; no precisó antihistamínico (Aerius).", table_cell)
        ],
        [
            Paragraph("<b>14/08/2026</b>", table_cell_bold),
            Paragraph("<b>EZETIMIBA 10 mg</b>", table_cell),
            Paragraph("Hipolipemiante<br/>(Inhibidor NPC1L1)", table_cell),
            Paragraph("Control colesterol c-LDL", table_cell),
            Paragraph("<b>Prurito cutáneo generalizado migratorio</b> durante los primeros 15 días.", table_cell),
            Paragraph("<b>No se quitó solo; requirió tratamiento farmacológico diario.</b>", table_cell),
            Paragraph("<b>Toma diaria de antihistamínico (Aerius) y crema de urea.</b> Suspendido por ineficacia y prurito.", table_cell)
        ],
        [
            Paragraph("<b>08/10/2026</b>", table_cell_bold),
            Paragraph("<b>PITAVASTATINA</b>", table_cell),
            Paragraph("Estatina hipolipemiante", table_cell),
            Paragraph("Control colesterol c-LDL", table_cell),
            Paragraph("<b>Picores corporales difusos</b> a la 3ª semana de tratamiento continuo.", table_cell),
            Paragraph("Se quitó al suspender el tratamiento farmacológico.", table_cell),
            Paragraph("<b>Toma de antihistamínico Aerius (1 día) y suspensión definitiva</b>; retorno a Atorvastatina.", table_cell)
        ],
        [
            Paragraph("<b>2022 - 2026</b><br/><i>[CONTROL]</i>", table_cell_bold),
            Paragraph("<b>ATORVASTATINA 20</b><br/><i>(Tolerancia Óptima)</i>", table_cell_bold),
            Paragraph("Estatina hipolipemiante", table_cell),
            Paragraph("Control colesterol c-LDL", table_cell),
            Paragraph("<b>CERO PICORES («No me da picores»). Tolerancia cutánea excelente permanente.</b>", table_cell_bold),
            Paragraph("Tolerancia continuada permanente sin ninguna manifestación dérmica (LDL en 64).", table_cell),
            Paragraph("<b>Fármaco de elección tolerado.</b> Demuestra que el prurito no es de clase, sino selectivo.", table_cell)
        ]
    ]
    
    t_p2 = Table(master_rows_p2, colWidths=col_w)
    t_p2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E3A8A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, colors.HexColor("#F8FAFC")]),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#F0FDF4")), # Fila de control en verde suave
        ('PADDING', (0,0), (-1,-1), 3.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_p2)

    # Page Break to Page 3
    story.append(PageBreak())

    # ---------------------------------------------------------
    # SECCIÓN 2: PATRONES DE REACTIVIDAD POR FAMILIAS CLÍNICAS
    # ---------------------------------------------------------
    story.append(Paragraph("2. Patrones de Reactividad y Análisis por Familias Farmacológicas", h1_style))
    story.append(Paragraph("El análisis sistemático del registro permite extraer 4 patrones claros para orientar el diagnóstico inmuno-alergológico:", body_style))
    story.append(Spacer(1, 4))

    # Table of Clinical Families
    fam_data = [
        [Paragraph("Familia Farmacológica", table_header), Paragraph("Fármacos Evaluados y Hallazgos", table_header), Paragraph("Hipótesis Diagnóstica / Mecanismo Sugerido", table_header)],
        [
            Paragraph("<b>Betalactámicos<br/>(Aminopenicilinas)</b>", table_cell_bold),
            Paragraph("<b>• Clamoxil (1997):</b> Sarpullido en pecho (suspendido).<br/><b>• Amoxicilina 750 (2017):</b> Picores leves + palpitaciones.<br/><i>(RAST Amoxicilina previo 26/11/2002: <0,35 limítrofe).</i>", table_cell),
            Paragraph("Hipersensibilidad retardada tipo IV o reactividad no mediada por IgE a la cadena lateral aminopenicilina. Precaución con aminopenicilinas.", table_cell)
        ],
        [
            Paragraph("<b>Fluorquinolonas<br/>(Cipro, Oflo, Levo)</b>", table_cell_bold),
            Paragraph("<b>• Ciprofloxacino (1999):</b> Sarpullido en pecho (3 días).<br/><b>• Ofloxacino (2001):</b> Picores espalda que <u>cedieron al 6º día</u>.<br/><b>• Levofloxacino (2025):</b> Picores brazos/piernas que <u>desaparecieron el 7º día</u> (tratados con Urea).", table_cell),
            Paragraph("<b>Degranulación mastocitaria directa no inmunológica (vía receptor MRGPRX2).</b> Explica por qué el prurito puede remitir durante la toma continuada sin shock anafiláctico.", table_cell)
        ],
        [
            Paragraph("<b>Macrólidos<br/>(Claritro vs Azitro)</b>", table_cell_bold),
            Paragraph("<b>• Claritromicina (2006):</b> Picores crecientes e intolerables en piernas (retirada obligatoria a la 3ª toma).<br/><b>• Azitromicina (2015, 2017):</b> Picores de 3 horas que <u>desaparecieron solos</u>; buena tolerancia posterior.", table_cell),
            Paragraph("Intolerancia al anillo de 14 átomos (Claritromicina) con tolerancia conservada al anillo azálido de 15 átomos (Azitromicina).", table_cell)
        ],
        [
            Paragraph("<b>Hipolipemiantes<br/>(Ezetimiba, Pitava vs Atorva)</b>", table_cell_bold),
            Paragraph("<b>• Ezetimiba (2026):</b> Prurito diario 15 días (Aerius + Urea).<br/><b>• Pitavastatina (2026):</b> Picores a la 3ª semana (Aerius).<br/><b>• Atorvastatina 20 mg (2022-2026): CERO PICORES.</b>", table_cell),
            Paragraph("Prurito dependiente de molécula/vehículo y no efecto de clase. Atorvastatina es el fármaco de elección biológicamente neutro.", table_cell)
        ]
    ]
    fam_table = Table(fam_data, colWidths=[120, 218, 210])
    fam_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0F172A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(fam_table)
    story.append(Spacer(1, 8))

    # ---------------------------------------------------------
    # SECCIÓN 3: PREGUNTAS Y PUNTOS DE DECISIÓN PARA EL ALERGÓLOGO
    # ---------------------------------------------------------
    story.append(Paragraph("3. Puntos Concretos de Consulta y Decisión con el Alergólogo", h1_style))
    
    preguntas_data = [
        [Paragraph("Punto de Decisión Clínica", table_header), Paragraph("Detalle de la Consulta Especializada", table_header), Paragraph("Impacto en la Salud del Paciente", table_header)],
        [
            Paragraph("<b>1. Pruebas Cutáneas para Betalactámicos</b>", table_cell_bold),
            Paragraph("¿Procede realizar pruebas en prick o intradérmicas con determinantes mayores (PPL) y menores (MDM) de penicilina y amoxicilina para confirmar si existe alergia IgE mediada o exclusión formal?", table_cell),
            Paragraph("Permitiría saber si las <b>cefalosporinas de 3ª generación (Ceftriaxona / Cefixima)</b> son seguras ante infecciones de orina o respiratorias.", table_cell)
        ],
        [
            Paragraph("<b>2. Clasificación de Quinolonas (MRGPRX2)</b>", table_cell_bold),
            Paragraph("Dado que con Ofloxacino y Levofloxacino el prurito remitió progresivamente al 6º-7º día sin anafilaxia, ¿se confirma el mecanismo pseudoalérgico no IgE de degranulación directa?", table_cell),
            Paragraph("Evita vetar innecesariamente toda la familia de quinolonas si se requiere un rescate urológico específico bajo premedicación.", table_cell)
        ],
        [
            Paragraph("<b>3. Panel Antibiótico Seguro de Rescate</b>", table_cell_bold),
            Paragraph("Definir un listado oficial de antibióticos de rescate plenamente autorizados (ej. Fosfomicina, Azitromicina, Cefixima) que figuren en la historia clínica del paciente.", table_cell),
            Paragraph("Tranquilidad absoluta ante prescripciones urgentes en centros de salud, urgencias hospitalarias o intervenciones.", table_cell)
        ],
        [
            Paragraph("<b>4. Manejo del Prurito por Hipolipemiantes</b>", table_cell_bold),
            Paragraph("Constatar que el prurito con Ezetimiba y Pitavastatina no contraindica el uso de <b>Atorvastatina (excelente tolerancia sin picores)</b> ni de <b>Ácido Bempedoico (Nexletol)</b>.", table_cell),
            Paragraph("Permite coordinar con Medicina Interna el control del colesterol sin inducir mialgias ni prurito cutáneo.", table_cell)
        ]
    ]
    preguntas_table = Table(preguntas_data, colWidths=[130, 238, 180])
    preguntas_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E3A8A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(preguntas_table)

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado exitosamente en: {output_path}")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else PDF_PATH
    build_pdf(out)
