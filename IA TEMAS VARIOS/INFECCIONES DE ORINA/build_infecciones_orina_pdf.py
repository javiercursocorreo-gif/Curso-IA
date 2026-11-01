#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_infecciones_orina_pdf.py
Genera el informe médico actualizado en PDF:
'Infecciones de orina.pdf'
dentro de 'IA TEMAS VARIOS/INFECCIONES DE ORINA/'.
Incorpora los resultados del nuevo cultivo de E. coli (Hospital La Moraleja, 28/10/2026),
el antibiograma detallado, la explicación médica del urólogo sobre Cefixima / Ceftazidima / Cefuroxima,
y la comparativa histórica con Proteus mirabilis.
"""

import os
import sys

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

PDF_PATH = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/IA TEMAS VARIOS/INFECCIONES DE ORINA/Infecciones de orina.pdf"

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
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawString(36, letter[1] - 30, "INFORME MÉDICO: INFECCIONES DE ORINA, ANTIBIOGRAMAS Y CRITERIO CLÍNICO")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(36, letter[1] - 34, letter[0] - 36, letter[1] - 34)
            
        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(36, 32, letter[0] - 36, 32)
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(36, 20, "Documento Resumen Informativo y Clínico • Consulta Médica Requerida")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(letter[0] - 36, 20, page_str)
        self.restoreState()


def build_pdf(output_path=PDF_PATH):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 36pt = 0.5 in margins
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=42,
        bottomMargin=42
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A")
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#475569")
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=10,
        spaceAfter=4
    )
    
    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=6,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#334155")
    )
    
    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#1E293B")
    )
    
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell,
        fontName='Helvetica-Bold'
    )
    
    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )
    
    callout_text = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1E3A8A")
    )
    
    alert_text = ParagraphStyle(
        'AlertText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#991B1B")
    )

    story = []
    
    # ---------------------------------------------------------
    # PÁGINA 1: ENCABEZADO, CONCEPTOS CLAVE Y CULTIVO ACTUAL
    # ---------------------------------------------------------
    story.append(Paragraph("Infecciones del Tracto Urinario", title_style))
    story.append(Paragraph("Guía Interpretativa de Antibiogramas, Criterio Clínico y Selección Terapéutica Personalizada", subtitle_style))
    story.append(Spacer(1, 6))
    
    # Box Conceptos Clave
    concept_html = (
        "<b>Conceptos Clave de Microbiología Clínica y Regla de Equivalencias:</b><br/>"
        "• <b>La CMI no es una escala directa de eficacia:</b> Cada fármaco alcanza concentraciones distintas según el tejido y tiene puntos de corte clínicos diferentes. Un valor numérico más bajo de CMI no significa mayor potencia, sino que la bacteria está catalogada como <b>Sensible (S)</b> en dosis estándar.<br/>"
        "• <b>Infección Baja (Cistitis) vs. Infección Alta (Pielonefritis):</b> La cistitis se limita a la vejiga (escozor, polaquiuria, sin fiebre); se trata con fármacos de alta eliminación urinaria. La pielonefritis afecta al riñón (fiebre, dolor lumbar, escalofríos) y exige antibióticos con penetración tisular y sistémica.<br/>"
        "• <b>El Principio de Marcadores Subrogados de Clase:</b> Los laboratorios no analizan todos los antibióticos comerciales; prueban cabezas de serie. La sensibilidad a <b>Ceftazidima y Cefotaxima</b> (3.ª gen) y a <b>Cefuroxima</b> (2.ª gen) avala y confirma microbiológicamente la plena eficacia de la <b>Cefixima oral</b> (3.ª gen)."
    )
    concept_p = Paragraph(concept_html, callout_text)
    concept_table = Table([[concept_p]], colWidths=[540])
    concept_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#3B82F6")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(concept_table)
    story.append(Spacer(1, 8))
    
    # SECCIÓN 1: Episodio Actual E. coli
    story.append(Paragraph("1. Caso Actual: Escherichia coli (Cultivo 28/10/2026 - Hospital La Moraleja)", h1_style))
    story.append(Paragraph(
        "Aislamiento reciente de <i>E. coli</i> en muestra de orina (informe del 30/10/2026). La cepa es <b>multisensible a cefalosporinas</b>, fosfomicina y nitrofurantoína, pero presenta <b>resistencia cruzada a quinolonas (Ciprofloxacino), cotrimoxazol y amoxicilina/clavulánico oral</b>.",
        body_style
    ))
    story.append(Spacer(1, 4))
    
    # Tabla Antibiograma Actual
    t1_data = [
        [
            Paragraph("Antibiótico", table_header),
            Paragraph("Categoría", table_header),
            Paragraph("CMI", table_header),
            Paragraph("Vía", table_header),
            Paragraph("Comentario Clínico / Utilidad en Orina", table_header)
        ],
        [
            Paragraph("<b>Cefixima</b><br/><i>(Tratamiento activo)</i>", table_cell_bold),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("Subrogada", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("<b>Pauta prescrita por el urólogo (10 días).</b> Sensible por equivalencia directa con Ceftazidima / Cefotaxima de 3.ª gen.", table_cell)
        ],
        [
            Paragraph("Cefuroxima axetil (orina)", table_cell_bold),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("= 4.0", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("Cefalosporina oral de 2.ª gen. Sensible en orina. Confirma la vulnerabilidad del germen a betalactámicos.", table_cell)
        ],
        [
            Paragraph("Ceftazidima", table_cell_bold),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 0.12", table_cell),
            Paragraph("IV", table_cell),
            Paragraph("Marcador oficial de cefalosporinas de 3.ª gen. Avala la actividad bactericida de Cefixima frente a este <i>E. coli</i>.", table_cell)
        ],
        [
            Paragraph("Cefotaxima", table_cell),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 0.25", table_cell),
            Paragraph("IV", table_cell),
            Paragraph("Cefalosporina de 3.ª gen hospitalaria. Excelente sensibilidad sin presencia de BLEE.", table_cell)
        ],
        [
            Paragraph("Cefepima", table_cell),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 0.12", table_cell),
            Paragraph("IV", table_cell),
            Paragraph("Cefalosporina de 4.ª gen. Activa.", table_cell)
        ],
        [
            Paragraph("Fosfomicina (Monurol)", table_cell_bold),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 4.0", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("1.ª elección en cistitis aguda no complicada. Dosis estándar 3 g.", table_cell)
        ],
        [
            Paragraph("Nitrofurantoína", table_cell),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("= 16.0", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("1.ª elección clásica en cistitis (solo actúa en vejiga; pauta habitual 5 días).", table_cell)
        ],
        [
            Paragraph("Ertapenem / Meropenem", table_cell),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 0.12", table_cell),
            Paragraph("IV", table_cell),
            Paragraph("Carbapenémicos. De estricta reserva hospitalaria para sepsis o bacterias multirresistentes.", table_cell)
        ],
        [
            Paragraph("Gentamicina / Tobramicina", table_cell),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 1.0", table_cell),
            Paragraph("IV/IM", table_cell),
            Paragraph("Aminoglucósidos activos en vía parenteral.", table_cell)
        ],
        [
            Paragraph("Ciprofloxacino", table_cell_bold),
            Paragraph("<font color='#B91C1C'><b>RESISTENTE</b></font>", table_cell),
            Paragraph("≥ 4.0", table_cell),
            Paragraph("Oral/IV", table_cell),
            Paragraph("<b>NO USAR.</b> Quinolona completamente ineficaz por resistencia de la cepa.", table_cell)
        ],
        [
            Paragraph("Amoxicilina/Clavulánico (Oral)", table_cell_bold),
            Paragraph("<font color='#B91C1C'><b>RESISTENTE</b></font>", table_cell),
            Paragraph("= 16.0", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("<b>NO USAR (Augmentine).</b> Cepa resistente en toma oral (solo alcanza sensibilidad en dosis urinarias forzadas).", table_cell)
        ],
        [
            Paragraph("Trimetoprima/Sulfametoxazol", table_cell),
            Paragraph("<font color='#B91C1C'><b>RESISTENTE</b></font>", table_cell),
            Paragraph("≥ 320.0", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("<b>NO USAR (Septrin).</b> Resistencia masiva de alto nivel.", table_cell)
        ],
        [
            Paragraph("Ampicilina", table_cell),
            Paragraph("<font color='#B91C1C'><b>RESISTENTE</b></font>", table_cell),
            Paragraph("≥ 32.0", table_cell),
            Paragraph("Oral/IV", table_cell),
            Paragraph("Ineficaz por betalactamasas simples.", table_cell)
        ]
    ]
    
    t1 = Table(t1_data, colWidths=[105, 55, 45, 40, 295])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0284C7")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(t1)
    
    # ---------------------------------------------------------
    # PÁGINA 2: CRITERIO DEL URÓLOGO Y CASO HISTÓRICO PROTEUS
    # ---------------------------------------------------------
    story.append(PageBreak())
    
    story.append(Paragraph("2. Criterio Clínico del Urólogo: Resolución de Dudas Farmacológicas", h1_style))
    story.append(Paragraph(
        "<b>Pregunta de la Paciente:</b> En el informe de cultivo no figura la <i>Cefixima</i> que estoy tomando, pero el urólogo me indicó: <i>«Si es sensible a ceftazidima, es sensible a cefuroxima. Completamos 7 días con la cefixima...»</i>. ¿Por qué menciona dos antibióticos que no tomo y me ordena seguir con Cefixima?",
        body_style
    ))
    story.append(Spacer(1, 4))
    
    # Explicación del Urólogo
    uro_box_html = (
        "<b>Explicación Médica y Farmacológica:</b><br/>"
        "<b>1. Parentesco de Familia (Cefalosporinas):</b> La <b>Cefuroxima</b> es una cefalosporina de 2.ª generación; la <b>Ceftazidima</b> es de 3.ª generación (inyectable); y la <b>Cefixima</b> (lo que tomas) es exactamente una <b>cefalosporina de 3.ª generación por vía oral</b>.<br/>"
        "<b>2. La Deducción del Especialista:</b> En los antibiogramas estandarizados (normas EUCAST/CLSI), la <i>Ceftazidima</i> actúa como <b>marcador oficial de 3.ª generación</b>. Al ver que tu <i>E. coli</i> dio <b>Sensible (≤ 0.12) a Ceftazidima</b> y <b>Sensible a Cefuroxima</b>, el urólogo sabe con certeza científica absoluta que la bacteria <b>carece de enzimas BLEE</b> (betalactamasas de espectro extendido) y que la <b>Cefixima la destruye eficazmente</b>.<br/>"
        "<b>3. Regla de Oro (No cambiar de antibiótico a mitad de curso):</b> Como ya habías iniciado Cefixima y la bacteria está plenamente cubierta, cambiar ahora a otro fármaco solo alteraría tu flora digestiva y aumentaría riesgos de intolerancia sin aportar ninguna ventaja. La indicación correcta es <b>completar 7 días</b> y evaluar síntomas una semana tras finalizar."
    )
    uro_p = Paragraph(uro_box_html, callout_text)
    uro_table = Table([[uro_p]], colWidths=[540])
    uro_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDF4")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#22C55E")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(uro_table)
    story.append(Spacer(1, 8))
    
    # SECCIÓN 3: Caso 2 Histórico Proteus mirabilis
    story.append(Paragraph("3. Episodio Previo: Proteus mirabilis (> 100.000 UFC/ml)", h1_style))
    story.append(Paragraph(
        "<i>Proteus mirabilis</i> es un bacilo gramnegativo con capacidad para producir <b>ureasa</b>, enzima que alcaliniza la orina y favorece cálculos de estruvita. A diferencia de <i>E. coli</i>, presenta <b>resistencias naturales intrínsecas</b> muy marcadas:",
        body_style
    ))
    story.append(Spacer(1, 4))
    
    t2_data = [
        [
            Paragraph("Antibiótico", table_header),
            Paragraph("Categoría", table_header),
            Paragraph("CMI", table_header),
            Paragraph("Vía", table_header),
            Paragraph("Comentario Clínico en Proteus", table_header)
        ],
        [
            Paragraph("Cefuroxima axetil (orina)", table_cell_bold),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 1.0", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("Opción oral de alta eficacia y excelente tolerancia en este germen.", table_cell)
        ],
        [
            Paragraph("Trimetoprima/Sulfam. (Cotrim.)", table_cell_bold),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 20.0", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("Muy eficaz en <i>Proteus</i> (Septrin). Totalmente opuesto al <i>E. coli</i> actual.", table_cell)
        ],
        [
            Paragraph("Amoxicilina/Clavulánico (Urine)", table_cell),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 4.0", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("Sensible en orina en <i>Proteus</i> (en sistémico requiere exposición incrementada).", table_cell)
        ],
        [
            Paragraph("Ciprofloxacino", table_cell),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 0.06", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("Sensible en este cultivo; se aconseja reservar para evitar resistencias.", table_cell)
        ],
        [
            Paragraph("Ampicilina", table_cell),
            Paragraph("<font color='#15803D'><b>SENSIBLE</b></font>", table_cell),
            Paragraph("≤ 2.0", table_cell),
            Paragraph("Oral/IV", table_cell),
            Paragraph("Sensible a penicilinas simples.", table_cell)
        ],
        [
            Paragraph("Nitrofurantoína", table_cell_bold),
            Paragraph("<font color='#B91C1C'><b>INTRÍNSECA</b></font>", table_cell),
            Paragraph("—", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("<b>CONTRAINDICADO:</b> <i>Proteus</i> posee resistencia genética natural intrínseca.", table_cell)
        ],
        [
            Paragraph("Fosfomicina", table_cell_bold),
            Paragraph("<font color='#B91C1C'><b>NO ELECCIÓN</b></font>", table_cell),
            Paragraph("—", table_cell),
            Paragraph("Oral", table_cell),
            Paragraph("<b>NO RECOMENDADO:</b> Sensibilidad biológica natural muy reducida en esta especie.", table_cell)
        ]
    ]
    
    t2 = Table(t2_data, colWidths=[110, 65, 45, 40, 280])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0284C7")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(t2)
    
    # ---------------------------------------------------------
    # PÁGINA 3: COMPARATIVA ENTRE CULTIVOS Y SIGNOS DE ALARMA
    # ---------------------------------------------------------
    story.append(PageBreak())
    
    story.append(Paragraph("4. Comparativa Terapéutica Directa: E. coli Actual vs. Proteus Previo", h1_style))
    story.append(Paragraph(
        "Esta tabla sintetiza por qué la estrategia antibiótica varía radicalmente cuando cambia la bacteria causante, justificando por qué las cefalosporinas han sido el escudo común más fiable:",
        body_style
    ))
    story.append(Spacer(1, 4))
    
    t3_data = [
        [
            Paragraph("Fármaco Oral Común", table_header),
            Paragraph("Caso 1: E. coli (Actual)", table_header),
            Paragraph("Caso 2: Proteus mirabilis (Previo)", table_header),
            Paragraph("Comportamiento Comparado y Utilidad Práctica", table_header)
        ],
        [
            Paragraph("<b>Cefalosporinas Orales</b><br/>(Cefixima / Cefuroxima)", table_cell_bold),
            Paragraph("<font color='#15803D'><b>SÍ (Sensible)</b></font><br/>Pauta de 10 días activa", table_cell),
            Paragraph("<font color='#15803D'><b>SÍ (Sensible)</b></font><br/>Cefuroxima sensible", table_cell),
            Paragraph("<b>FÁRMACO REY:</b> Eficaz y activo en ambos cultivos. Excelente opción oral con cobertura de espectro seguro sin resistencias.", table_cell)
        ],
        [
            Paragraph("Fosfomicina (Monurol)", table_cell_bold),
            Paragraph("<font color='#15803D'><b>SÍ (Sensible)</b></font><br/>CMI ≤ 4.0", table_cell),
            Paragraph("<font color='#B91C1C'><b>NO (Baja eficacia)</b></font>", table_cell),
            Paragraph("Muy eficaz en <i>E. coli</i>; ineficaz en <i>Proteus</i> por falta de transporte del fármaco en pared bacteriana.", table_cell)
        ],
        [
            Paragraph("Nitrofurantoína", table_cell_bold),
            Paragraph("<font color='#15803D'><b>SÍ (Sensible)</b></font><br/>CMI = 16.0", table_cell),
            Paragraph("<font color='#B91C1C'><b>NO (Resistencia Intrínseca)</b></font>", table_cell),
            Paragraph("Excelente en vejiga para <i>E. coli</i>; totalmente inútil en <i>Proteus</i> por resistencia genética congénita.", table_cell)
        ],
        [
            Paragraph("Cotrimoxazol (Septrin)", table_cell),
            Paragraph("<font color='#B91C1C'><b>NO (Resistente ≥ 320)</b></font>", table_cell),
            Paragraph("<font color='#15803D'><b>SÍ (Sensible ≤ 20)</b></font>", table_cell),
            Paragraph("Comportamientos inversos: gran opción en el <i>Proteus</i> previo, pero prohibido en el <i>E. coli</i> actual.", table_cell)
        ],
        [
            Paragraph("Amoxicilina/Clavulánico", table_cell),
            Paragraph("<font color='#B91C1C'><b>NO (Resistente oral)</b></font>", table_cell),
            Paragraph("<font color='#15803D'><b>SÍ (Sensible en orina)</b></font>", table_cell),
            Paragraph("Resistente en la cepa actual de <i>E. coli</i>. No indicado en este episodio.", table_cell)
        ],
        [
            Paragraph("Ciprofloxacino", table_cell),
            Paragraph("<font color='#B91C1C'><b>NO (Resistente ≥ 4.0)</b></font>", table_cell),
            Paragraph("<font color='#15803D'><b>SÍ (Sensible)</b></font>", table_cell),
            Paragraph("Resistencia adquirida por <i>E. coli</i>. Inutilizable en este episodio.", table_cell)
        ]
    ]
    
    t3 = Table(t3_data, colWidths=[120, 110, 110, 200])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0284C7")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(t3)
    story.append(Spacer(1, 10))
    
    # SECCIÓN 5: Plan de Acción y Signos de Alarma
    alarm_html = (
        "<b>Plan Terapéutico en Curso, Recomendaciones y Signos de Alarma:</b><br/>"
        "• <b>Cumplimiento Estricto de la Pauta:</b> Completar los <b>10 días completos de Cefixima</b> pautados por el urólogo, sin suspender el fármaco aunque desaparezcan las molestias urinarias, para erradicar cualquier reservorio vesical.<br/>"
        "• <b>Seguimiento Post-Tratamiento:</b> Contactar con el urólogo una semana tras finalizar el ciclo antibiótico, informando de la ausencia de síntomas o de cualquier molestia residual.<br/>"
        "• <b>Signos de Alarma de Infección Alta (Pielonefritis):</b> Si aparece <b>fiebre (> 38 ºC)</b>, dolor en la zona lumbar/espalda baja, escalofríos intensos, náuseas o vómitos, se debe acudir de inmediato a Urgencias Médicas.<br/>"
        "• <b>Hidratación y Soporte de Microbiota:</b> Mantener una ingesta abundante de líquidos (1,5 a 2 litros diarios de agua) para favorecer el lavado vesical. Al finalizar el ciclo antibiótico, se recomienda restaurar la flora vaginal y vesical mediante probióticos específicos ricos en <i>Lactobacillus</i>.<br/>"
        "• <b>Aviso Facultativo:</b> Documento elaborado con fines informativos y de educación clínica. La pauta terapéutica definitiva corresponde exclusivamente a su médico especialista."
    )
    alarm_p = Paragraph(alarm_html, alert_text)
    alarm_table = Table([[alarm_p]], colWidths=[540])
    alarm_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF2F2")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#EF4444")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(alarm_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✅ PDF generado con éxito en: {output_path}")

if __name__ == '__main__':
    build_pdf()

