#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_espalda_pdf.py
Genera el informe médico y biomecánico actualizado en PDF:
'Resumen Clinico Espalda y Columna.pdf'
dentro de 'IA TEMAS VARIOS/ESPALDA/'.
Incorpora los resultados oficiales de la Resonancia Magnética Lumbar (Sanitas Costa Rica, 12/03/2026),
los cambios Modic tipo 1 en L5-S1, la estenosis foraminal asimétrica izquierda,
el análisis biomecánico del dolor matutino (Modic 1 + colchón/topper), la rodilla, pie cavo,
y la farmacovigilancia de estatinas / ácido bempedoico.
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
PDF_PATH = os.path.join(BASE_DIR, "Resumen Clinico Espalda y Columna.pdf")

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
            self.drawString(36, letter[1] - 28, "EXPEDIENTE CLÍNICO INTEGRADO: TRAUMATOLOGÍA, BIOMECÁNICA Y RM LUMBAR")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawRightString(letter[0] - 36, letter[1] - 28, "Sanitas Costa Rica (12/03/2026) • Paciente: Javi (67 a)")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(36, letter[1] - 32, letter[0] - 36, letter[1] - 32)
            
        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(36, 32, letter[0] - 36, 32)
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(36, 20, "Documento Clínico Estructurado • Información para Consulta Médica Especializada")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(letter[0] - 36, 20, page_str)
        self.restoreState()


def build_pdf(output_path=PDF_PATH):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#0F172A")
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#1E3A8A")
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#64748B")
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=10,
        spaceAfter=4
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=6,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
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
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=1
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
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
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#0C4A6E")
    )

    alert_box_text = ParagraphStyle(
        'AlertBoxText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#991B1B")
    )

    story = []
    
    # ---------------------------------------------------------
    # HEADER BANNER (Page 1)
    # ---------------------------------------------------------
    story.append(Paragraph("EXPEDIENTE CLÍNICO DE TRAUMATOLOGÍA Y BIOMECÁNICA", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("VALORACIÓN INTEGRAL: COLUMNA VERTEBRAL, ARTICULACIONES DE CARGA Y FARMACOVIGILANCIA", subtitle_style))
    story.append(Paragraph("<b>Ubicación:</b> IA TEMAS VARIOS / ESPALDA &nbsp;|&nbsp; <b>Paciente:</b> Javi (Varón, 67 años) &nbsp;|&nbsp; <b>Fecha RM:</b> 12/03/2026 (Informe: 17/03/2026)", meta_style))
    story.append(Spacer(1, 6))

    # Notice Box
    notice_data = [[
        Paragraph("<b>AVISO DE SUPERVISIÓN FACULTATIVA:</b> Este documento sistematiza formalmente las interconsultas médicas, la Resonancia Magnética oficial de Sanitas, el análisis biomecánico de columna y rodilla, la ergonomía del descanso y el perfil farmacológico. Su fin es aportar una visión médica estructurada para la toma de decisiones con sus especialistas presenciales (Traumatología, Medicina Interna y Medicina de Familia).", callout_text)
    ]]
    notice_table = Table(notice_data, colWidths=[540])
    notice_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0F9FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#0284C7")),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(notice_table)
    story.append(Spacer(1, 8))

    # ---------------------------------------------------------
    # SECCIÓN 1: INTEGRACIÓN OFICIAL INFORME RADIODIAGNÓSTICO
    # ---------------------------------------------------------
    story.append(Paragraph("1. Integración Oficial del Informe de Radiodiagnóstico (Sanitas)", h1_style))
    
    # Ficha Técnica Table
    ficha_data = [
        [
            Paragraph("<b>Prueba:</b> Resonancia Magnética Columna Lumbar<br/><b>Fecha:</b> 12/03/2026 (Informe: 17/03/2026)", table_cell),
            Paragraph("<b>Centro:</b> Sanitas Costa Rica (Madrid)<br/><b>Episodio:</b> 1602561722", table_cell),
            Paragraph("<b>Facultativo:</b> Dra. Ana María Rambla Sanz<br/><b>Nº Colegiado:</b> 282881172", table_cell)
        ]
    ]
    ficha_table = Table(ficha_data, colWidths=[180, 180, 180])
    ficha_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(ficha_table)
    story.append(Spacer(1, 6))

    # Hallazgos Table
    hallazgos_data = [
        [Paragraph("Segmento / Región", table_header), Paragraph("Hallazgos Oficiales de la RM (Literal y Desglose)", table_header), Paragraph("Traducción Médica Directa", table_header)],
        [
            Paragraph("<b>Alineación y Cuerpos</b>", table_cell_bold),
            Paragraph("Altura de cuerpos conservada. Sin alteraciones significativas de alineación.", table_cell),
            Paragraph("Ausencia de espondilolistesis franca o aplastamientos vertebrales.", table_cell)
        ],
        [
            Paragraph("<b>Hidratación Discal</b>", table_cell_bold),
            Paragraph("Signos de <b>deshidratación discal lumbar generalizada</b> (pérdida de señal T2).", table_cell),
            Paragraph("Pérdida de elasticidad biológica para absorber fuerzas compresivas axiales.", table_cell)
        ],
        [
            Paragraph("<b>Segmento L4-L5</b>", table_cell_bold),
            Paragraph("Mínimo abombamiento discal posterior difuso. Cambios degenerativos facetarios bilaterales. Condiciona <b>estenosis leve forámenes bilaterales</b> sin compromiso directo raíz.", table_cell),
            Paragraph("Artrosis en articulaciones posteriores. Forámenes estrechados levemente pero con espacio radicular suficiente.", table_cell)
        ],
        [
            Paragraph("<b>Segmento L5-S1<br/>(Foco Lesional Central)</b>", table_cell_bold),
            Paragraph("<b>• Moderada disminución de altura discal</b> (pinzamiento).<br/><b>• Marcada irregularidad platillos con cambios Modic 1</b> (edema e inflamación ósea subcondral activa).<br/><b>• Complejo disco-osteofitario posterior</b>.<br/><b>• Estenosis moderada del foramen izquierdo con escaso margen libre para raíz L5/S1</b> (frente a estenosis derecha leve).", table_cell),
            Paragraph("<b>Lesión diana explicativa del cuadro:</b><br/>Inflamación ósea aguda de platillos + osteofitos que estrangulan el foramen izquierdo y comprometen la raíz nerviosa.", table_cell)
        ],
        [
            Paragraph("<b>Cono y Cauda Equina</b>", table_cell_bold),
            Paragraph("Morfología, calibre y señal normales. Cauda equina libre sin compresión central.", table_cell),
            Paragraph("Canal medular central permeable; compromiso circunscrito a foramen radicular izquierdo.", table_cell)
        ]
    ]
    hallazgos_table = Table(hallazgos_data, colWidths=[110, 260, 170])
    hallazgos_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E3A8A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(hallazgos_table)
    story.append(Spacer(1, 6))

    # Literal Conclusion Callout
    conclusion_data = [[
        Paragraph("<b>CONCLUSIÓN RADIOLÓGICA OFICIAL:</b> <i>«Espondilosis y osteoartrosis L5-S1 que condiciona estenosis moderada del foramen izquierdo con escaso margen para la salida de la raíz. Resto de estenosis leves ver en informe.»</i> — Dra. Ana María Rambla Sanz.", body_bold)
    ]]
    conclusion_table = Table(conclusion_data, colWidths=[540])
    conclusion_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF2F2")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#DC2626")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(conclusion_table)
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SECCIÓN 2: IMPACTO EN DIAGNÓSTICO INTEGRADO Y BIOMECÁNICA
    # ---------------------------------------------------------
    story.append(Paragraph("2. Impacto de la Resonancia en el Diagnóstico Integrado y Biomecánica", h1_style))
    story.append(Paragraph("La confirmación por imagen replantea radicalmente el manejo biomecánico y farmacológico:", body_style))
    story.append(Spacer(1, 4))

    # Correlation Matrix Table
    corr_data = [
        [Paragraph("Hallazgo RM (12/03/2026)", table_header), Paragraph("Expresión Clínica en el Paciente", table_header), Paragraph("Repercusión Terapéutica Directa", table_header)],
        [
            Paragraph("<b>Cambios Modic 1 en L5-S1</b><br/>Edema óseo subcondral e inflamación activa en platillos vertebrales.", table_cell),
            Paragraph("Dolor lumbar profundo y punzante muy intenso al levantarse por la mañana (primeros 30-45 min).", table_cell),
            Paragraph("<b>PROHIBIDO TOPPER BLANDO:</b> Exige colchón de firmeza alta (Aspol Tambre) + cojín poplíteo y calor local.", table_cell)
        ],
        [
            Paragraph("<b>Estenosis Foraminal Izquierda con Escaso Margen</b><br/>Compromiso mecánico de raíz L5/S1 izquierda.", table_cell),
            Paragraph("Ciatalgia, tirantez, calambres y fasciculaciones con claro predominio en miembro inferior izquierdo.", table_cell),
            Paragraph("<b>PROTECCIÓN FORAMEN IZQ:</b> Evitar basculación pélvica izq.; sillón Zero Gravity; no sofás blandos.", table_cell)
        ],
        [
            Paragraph("<b>Complejo Disco-Osteofitario</b><br/>Protrusión discal endurecida con crestas de hueso degenerativo.", table_cell),
            Paragraph("Estrechez anatómica fija que no se reabsorbe con el tiempo a diferencia de hernias blandas.", table_cell),
            Paragraph("<b>DESCOMPRESIÓN CRÓNICA:</b> Natación suave con pull-buoy, marcha fraccionada, control de peso.", table_cell)
        ],
        [
            Paragraph("<b>Afectación Facetaria L4-L5</b><br/>Abombamiento y artrosis posterior bilateral.", table_cell),
            Paragraph("Rigidez matutina en torsión lumbar y riesgo de sobrecarga del nivel adyacente a L5-S1.", table_cell),
            Paragraph("<b>CERO ROTACIONES FORZADAS:</b> Prohibido yoga/pilates con torsiones bruscas o flexión extrema.", table_cell)
        ]
    ]
    corr_table = Table(corr_data, colWidths=[150, 195, 195])
    corr_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0F172A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(corr_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>1. El Origen Real del Dolor Matutino (La Trampa Biomecánica del Topper Blando):</b> Antes se atribuía exclusivamente a una postura nocturna defectuosa. La RM demuestra la causa biológica: <b>los platillos vertebrales tienen edema óseo inflamatorio (Modic 1)</b>. Durante 8 horas en un colchón o topper viscoelástico blando, la pelvis se hunde (efecto hamaca) forzando la columna en flexión lumbar continuada y aplastando los platillos inflamados. Al incorporarse, la gravedad descarga en seco sobre el hueso edematoso. La firmeza ortopédica alta (Aspol Tambre sin topper) es un tratamiento biológico para despresurizar el hueso subcondral.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>2. Asimetría del Dolor y Síndrome Piramidal Izquierdo:</b> El foramen derecho es amplio (estenosis leve sin roce), mientras que el foramen izquierdo presenta estenosis moderada con escaso margen libre. Cuando el paciente se sienta en butacas o sofás convencionales que basculan la pelvis hacia atrás y a la izquierda, la raíz se pinza mecánicamente, disparando el espasmo reflejo del músculo piramidal izquierdo y las fasciculaciones distales.", body_style))

    # Page Break to Page 2
    story.append(PageBreak())

    # ---------------------------------------------------------
    # SECCIÓN 3: CUADRO CLÍNICO INTEGRAL DEL PACIENTE
    # ---------------------------------------------------------
    story.append(Paragraph("3. Cuadro Clínico Integral del Paciente", h1_style))
    
    # 3.1 Columna
    story.append(Paragraph("A. Columna Lumbo-Sacra (Diagnóstico Consolidado con RM 12/03/2026)", h2_style))
    story.append(Paragraph("• <b>Espondilosis y osteoartrosis lumbar multinivel (L4-L5 y L5-S1):</b> Artrosis en articulaciones posteriores y deshidratación discal.", bullet_style))
    story.append(Paragraph("• <b>Segmento L5-S1 con cambios Modic 1:</b> Pinzamiento discal moderado con edema subcondral e inflamación biológica activa en platillos vertebrales.", bullet_style))
    story.append(Paragraph("• <b>Estenosis foraminal moderada izquierda con escaso margen radicular:</b> Causa anatómica demostrada de la radiculopatía y ciatalgia izquierda.", bullet_style))
    story.append(Paragraph("• <b>Síndrome piramidal secundario izquierdo:</b> Contractura muscular reactiva que atrapa secundariamente el nervio ciático en la escotadura ciática.", bullet_style))
    story.append(Paragraph("• <b>Claudicación neurógena vespertina:</b> Fatiga y pesadez en piernas tras bipedestación estática prolongada o marcha continua no fraccionada.", bullet_style))
    story.append(Spacer(1, 4))

    # 3.2 Articulaciones de Carga
    story.append(Paragraph("B. Articulaciones de Carga y Miembros Inferiores", h2_style))
    story.append(Paragraph("• <b>Rodilla derecha — Condromalacia Rotuliana Grado 4:</b> Ausencia completa de cartílago en la carilla retro-rotuliana (contacto hueso con hueso en flexión). Infiltrada con ácido hialurónico con buena evolución sintomática. <i>Reserva funcional nula ante flexiones profundas (>40°) o impacto.</i>", bullet_style))
    story.append(Paragraph("• <b>Caderas — Coxartrosis bilateral incipiente:</b> Desgaste mecánico moderado sin limitación funcional severa, sensible a posturas estáticas.", bullet_style))
    story.append(Paragraph("• <b>Complejo Tobillo-Pie — Pie cavo bilateral y antecedente de fascitis plantar severa:</b> Tratada exitosamente con ondas de choque extracorpóreas (espesor de fascia normalizado a 3,8 mm). Requiere calzado con drop alto y sujeción de arco para compensar la rigidez.", bullet_style))
    story.append(Spacer(1, 4))

    # 3.3 Farmacovigilancia
    story.append(Paragraph("C. Perfil Metabólico y Farmacovigilancia (Miopatía por Estatinas)", h2_style))
    story.append(Paragraph("• <b>Dislipidemia mixta en seguimiento:</b> Antecedente de Atorvastatina 20 mg retirada por sospecha fundada de miopatía tóxica inducida por estatinas (calambres difusos y astenia muscular).", bullet_style))
    story.append(Paragraph("• <b>Ensayo con Ezetimiba 10 mg:</b> Descenso insuficiente de c-LDL con aparición de prurito cutáneo migratorio.", bullet_style))
    story.append(Paragraph("• <b>Estrategia de Consenso con Medicina Interna:</b> Valoración de <b>Ácido Bempedoico (Nexletol / Nustendi)</b>, profármaco con activación exclusivamente hepática que no se metaboliza en el músculo esquelético, o en su defecto <b>Pitavastatina (Livazo)</b> a dosis mínimas.", bullet_style))
    story.append(Spacer(1, 8))

    # ---------------------------------------------------------
    # SECCIÓN 4: ERGONOMÍA DEL DESCANSO Y MOBILIARIO
    # ---------------------------------------------------------
    story.append(Paragraph("4. Ergonomía del Descanso y Mobiliario (Adaptada a Modic 1)", h1_style))
    
    ergo_data = [
        [Paragraph("Ámbito", table_header), Paragraph("Pauta Ergonómica y Ortopédica Obligatoria", table_header), Paragraph("Fundamento Biomecánico y Radiológico", table_header)],
        [
            Paragraph("<b>Colchón Nocturno</b>", table_cell_bold),
            Paragraph("<b>Colchón de muelles ensacados de muy alta firmeza (Aspol Tambre).</b><br/><u>PROHIBIDO el topper viscoelástico (Pikolin Sapporo).</u>", table_cell),
            Paragraph("Evita que la pelvis bascule en flexión forzada nocturna. El topper blando genera efecto hamaca y comprime el edema óseo Modic 1.", table_cell)
        ],
        [
            Paragraph("<b>Postura al Dormir:<br/>Boca Arriba</b>", table_cell_bold),
            Paragraph("<b>Decúbito supino con cojín cilíndrico firme bajo las rodillas (huecos poplíteos).</b>", table_cell),
            Paragraph("Flexiona suavemente caderas y rodillas, relaja la tensión del músculo psoas-ilíaco y <b>abre los forámenes entre un 12% y 18%</b>.", table_cell)
        ],
        [
            Paragraph("<b>Postura al Dormir:<br/>De Lado</b>", table_cell_bold),
            Paragraph("<b>Decúbito lateral con almohada firme entre ambas rodillas.</b>", table_cell),
            Paragraph("Mantiene la pelvis paralela al eje vertebral y suprime las torsiones que estrangulan el foramen izquierdo.", table_cell)
        ],
        [
            Paragraph("<b>Mobiliario Diurno:<br/>Descanso</b>", table_cell_bold),
            Paragraph("<b>Sillón basculante Gravedad Cero (Zero Gravity)</b> o butaca articulada en bloque.", table_cell),
            Paragraph("Pivota asiento y respaldo juntos elevando piernas a la altura del corazón; despresuriza L5-S1 y relaja el piramidal.", table_cell)
        ],
        [
            Paragraph("<b>Sofás Convencionales<br/>(Alerta)</b>", table_cell_bold),
            Paragraph("Nunca hundirse en sofás profundos y blandos. Si se usa, colocar cojín lumbar y cojín bajo muslos.", table_cell),
            Paragraph("La basculación pélvica en retroversión impacta directamente contra el foramen estenosado.", table_cell)
        ],
        [
            Paragraph("<b>Pauta Dinámica</b>", table_cell_bold),
            Paragraph("<b>Regla de los 45 minutos:</b> Levantarse a caminar al menos 1 minuto por cada 45 minutos sentado.", table_cell),
            Paragraph("Restaura la perfusión microvascular de las raíces nerviosas y previene la isquemia foraminal.", table_cell)
        ]
    ]
    ergo_table = Table(ergo_data, colWidths=[105, 225, 210])
    ergo_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E3A8A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(ergo_table)

    # Page Break to Page 3
    story.append(PageBreak())

    # ---------------------------------------------------------
    # SECCIÓN 5: MATRIZ DE ACTIVIDAD FÍSICA Y EJERCICIOS
    # ---------------------------------------------------------
    story.append(Paragraph("5. Matriz de Actividad Física y Ejercicios (Zona de Seguridad Neutra)", h1_style))
    story.append(Paragraph("El paciente presenta un reto biomecánico dual: <b>la estenosis lumbar agradece una discreta descompresión, pero el disco L5-S1 y los cambios Modic 1 se agravan con la flexión extrema; asimismo, la espalda requiere actividad aeróbica pero la rodilla derecha (Grado 4 hueso con hueso) no tolera impactos ni sentadillas</b>. Se establece la siguiente matriz estricta:", body_style))
    story.append(Spacer(1, 6))

    ejercicios_data = [
        [
            Paragraph("⛔ EJERCICIOS TERMINANTEMENTE PROHIBIDOS", table_header),
            Paragraph("✅ EJERCICIOS PERMITIDOS Y RECOMENDADOS", table_header)
        ],
        [
            Paragraph("<b>1. Estiramiento de isquiotibiales de pie con flexión de tronco</b><br/>(Tocarse los dedos de los pies de pie: aplasta los discos y tracciona brutalmente la raíz L5 estenosada).", table_cell),
            Paragraph("<b>1. Natación dorsal suave con Pull-Buoy entre los muslos</b><br/>(Mantiene el cuerpo a flote sin dar patadas; elimina la carga articular de la rodilla y descomprime la columna en flotación neutra).", table_cell)
        ],
        [
            Paragraph("<b>2. Postura de 'Superman' o extensiones lumbares hacia atrás</b><br/>(Cierra los forámenes intervertebrales y estruja la raíz nerviosa izquierda).", table_cell),
            Paragraph("<b>2. Caminata dentro del agua templada a nivel del pecho</b><br/>(El empuje del agua reduce el 75% del peso corporal, permitiendo marcha articular segura sin fricción ósea en rodilla).", table_cell)
        ],
        [
            Paragraph("<b>3. Sentadillas profundas o Zancadas (Langes)</b><br/>(Provocan contacto y roce de hueso con hueso en la rótula derecha sin cartílago).", table_cell),
            Paragraph("<b>3. Marcha diaria fraccionada en 2 tandas de 2.500 a 3.000 pasos</b><br/>(Nunca tiradas únicas de 6.000 pasos seguidos; previene la claudicación neurógena vespertina).", table_cell)
        ],
        [
            Paragraph("<b>4. Torsiones de tronco bruscas en suelo (Yoga/Pilates agresivo)</b><br/>(Someten a cizallamiento la artrosis facetaria de L4-L5 y L5-S1).", table_cell),
            Paragraph("<b>4. Calzado Nike Vomero con plantillas ortopédicas de gel</b><br/>(Absorbe las ondas de impacto en el talón protegiendo el arco rígido del pie cavo).", table_cell)
        ],
        [
            Paragraph("<b>5. Peso muerto o levantamiento de cargas desde el suelo</b><br/>(Multiplica por 10 la presión axial sobre los platillos inflamados Modic 1).", table_cell),
            Paragraph("<b>5. Puente de glúteos isométrico en el suelo</b><br/>(Elevación suave de pelvis manteniendo rodillas alineadas a 90° sin gomas elásticas).", table_cell)
        ],
        [
            Paragraph("<b>6. Caminar lento arrastrando los pies ('modo escaparates')</b><br/>(Produce estasis venoso pélvico, fatiga postural y dolor lumbar sordo).", table_cell),
            Paragraph("<b>6. Estiramiento del músculo piramidal sentado en 4</b><br/>(Cruzar tobillo izquierdo sobre rodilla derecha en silla e inclinar torso neutro para descomprimir el nervio ciático).", table_cell)
        ]
    ]
    ejercicios_table = Table(ejercicios_data, colWidths=[270, 270])
    ejercicios_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor("#991B1B")),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor("#15803D")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(ejercicios_table)
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SECCIÓN 6: CHECKLIST PARA CONSULTAS MÉDICAS
    # ---------------------------------------------------------
    story.append(Paragraph("6. Checklist Estructurado para Consultas Médicas Especializadas", h1_style))
    
    check_data = [
        [Paragraph("Especialidad Médica", table_header), Paragraph("Puntos Concretos de Consulta e Intervención", table_header), Paragraph("Objetivo Terapéutico", table_header)],
        [
            Paragraph("<b>A. Traumatología /<br/>Unidad de Columna</b>", table_cell_bold),
            Paragraph("• <b>Presentar RM 12/03/2026:</b> Destacar <b>cambios Modic 1 en L5-S1</b> y <b>estenosis foraminal moderada izquierda con escaso margen radicular</b>.<br/>• <b>Evolución con colchón firme:</b> Confirmar la mejoría del dolor matutino tras retirar el topper y usar soporte poplíteo.<br/>• <b>Protección radicular L5 izq.:</b> Valorar neuroprotectores (complejo B) o pauta SOS ante brotes radiculares.<br/>• <b>Revisión de rodilla derecha Grado 4:</b> Calendario de mantenimiento articular (infiltraciones viscoelásticas periódicas).", table_cell),
            Paragraph("Optimizar control de síntomas mecánicos sin cirugía invasiva y proteger la reserva articular.", table_cell)
        ],
        [
            Paragraph("<b>B. Medicina Interna /<br/>Riesgo Cardiovascular</b>", table_cell_bold),
            Paragraph("• <b>Analítica de control lipídico:</b> Constatar que Ezetimiba 10 mg sola resulta insuficiente y desencadenó prurito cutáneo.<br/>• <b>Confirmar intolerancia muscular a Atorvastatina:</b> Cuadro de dolor y mialgias previo.<br/>• <b>Proponer formalmente Ácido Bempedoico (Nexletol 180 mg):</b> Fármaco sin metabolismo muscular (seguro en pacientes con mialgias previas) o Livazo a dosis bajas.", table_cell),
            Paragraph("Alcanzar diana terapéutica de c-LDL sin inducir toxicidad muscular en un paciente con ciatalgia.", table_cell)
        ]
    ]
    check_table = Table(check_data, colWidths=[120, 280, 140])
    check_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0F172A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(check_table)
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SECCIÓN 7: CRITERIOS DE ALERTA ROJA (URGENCIA HOSPITALARIA)
    # ---------------------------------------------------------
    story.append(Paragraph("7. Criterios de Alerta Roja (Urgencia Hospitalaria)", h1_style))
    
    red_data = [[
        Paragraph("<b>🚨 SIGNOS DE ALERTA ROJA (ACUDIR INMEDIATAMENTE A URGENCIAS):</b><br/>"
                  "<b>1. Pérdida súbita de fuerza en la pierna o pie izquierdo:</b> Imposibilidad de ponerse de puntillas, caminar sobre los talones o caída del pie al andar ('pie caído' por denervación motora L5/S1).<br/>"
                  "<b>2. Síndrome de Cola de Caballo (Cauda Equina):</b> Anestesia o acorchamiento en 'silla de montar' (genitales, ingles y glúteos), incontinencia urinaria/fecal repentina o imposibilidad brusca para orinar (retención aguda de orina).<br/>"
                  "<b>3. Dolor ciático incoercible:</b> Dolor radicular de intensidad máxima que no responde a medicación y persiste incluso en reposo absoluto horizontal.", alert_box_text)
    ]]
    red_table = Table(red_data, colWidths=[540])
    red_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF2F2")),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor("#DC2626")),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(red_table)

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado exitosamente en: {output_path}")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else PDF_PATH
    build_pdf(out)
