#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_info_008_sugiyama.py
Genera la Ficha Didáctica Oficial en PDF:
INFO-008: El Misterio de los Atascos Fantasma y el Tráfico Autónomo con IA
(Experimento de Yuki Sugiyama 2008 • Ondas de Choque Retrógradas • Simulación Interactiva)

Destino:
CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/15. [INFO] BLOQUE_15_INFOGRAFIAS_Y_NOVEDADES_IA/Lote_01_al_20/
"""

import os
import sys
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
TARGET_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/15. [INFO] BLOQUE_15_INFOGRAFIAS_Y_NOVEDADES_IA/Lote_01_al_20")
PDF_PATH = os.path.join(TARGET_DIR, "INFO-008_El_Misterio_de_los_Atascos_Fantasma_Experimento_Sugiyama.pdf")
HTML_SIMULATOR = os.path.join(TARGET_DIR, "SIMULADOR_ATASCO_FANTASMA_SUGIYAMA.html")
ROOT_HTML_SIMULATOR = os.path.join(BASE_DIR, "CLASES/SIMULADOR_ATASCO_FANTASMA_SUGIYAMA.html")

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
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(36, 28, letter[0] - 36, 28)
        
        left_text = "CURSO-IA • Bloque 15 [INFO]: Infografías y Novedades de IA — Experimento de Sugiyama"
        page_text = f"Página {self._pageNumber} de {page_count}"
        
        self.drawString(36, 18, left_text)
        self.drawRightString(letter[0] - 36, 18, page_text)
        self.restoreState()

def compilar_pdf():
    print("Compilando Ficha Didáctica INFO-008 en PDF...", flush=True)

    # Copiar también el simulador a la raíz de CLASES para fácil acceso
    if os.path.exists(HTML_SIMULATOR):
        shutil.copy2(HTML_SIMULATOR, ROOT_HTML_SIMULATOR)
        print(f"✅ Copiado simulador a: {ROOT_HTML_SIMULATOR}", flush=True)

    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=30,
        bottomMargin=36
    )

    PAGE_WIDTH = letter[0] - 72 # 540 pt

    styles = getSampleStyleSheet()

    c_navy = colors.HexColor('#0F172A')
    c_blue = colors.HexColor('#0284C7')
    c_green = colors.HexColor('#166534')
    c_amber = colors.HexColor('#B45309')
    c_red = colors.HexColor('#991B1B')
    c_purple = colors.HexColor('#7E22CE')

    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=14, leading=18,
        textColor=c_navy, alignment=1, spaceAfter=2
    )
    sub_style = ParagraphStyle(
        'DocSub', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.5, leading=11.5,
        textColor=c_blue, alignment=1, spaceAfter=6
    )
    h1_style = ParagraphStyle(
        'SecH1', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=13,
        textColor=colors.HexColor('#0369A1'), spaceBefore=6, spaceAfter=2
    )
    body_style = ParagraphStyle(
        'DocBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11,
        textColor=colors.HexColor('#1E293B'), spaceAfter=3
    )
    box_body = ParagraphStyle(
        'BoxBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.5, leading=10.5,
        textColor=colors.HexColor('#1E293B')
    )
    table_th = ParagraphStyle(
        'TH', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=7.5, leading=10,
        textColor=colors.HexColor('#0F172A'), alignment=1
    )
    table_td = ParagraphStyle(
        'TD', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7, leading=9.5,
        textColor=colors.HexColor('#1E293B')
    )

    story = []

    # Cabecera
    story.append(Paragraph("INFO-008 • EL MISTERIO DE LOS ATASCOS FANTASMA Y EL TRÁFICO AUTÓNOMO", title_style))
    story.append(Paragraph("EL EXPERIMENTO DE YUKI SUGIYAMA (2008) • ONDAS DE CHOQUE RETRÓGRADAS • SOLUCIÓN CON IA", sub_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceBefore=0, spaceAfter=5))

    # Introducción
    story.append(Paragraph("1. El Experimento que Desafió la Intuición del Tráfico (Nagoya, 2008)", h1_style))
    story.append(Paragraph(
        "En 2008, el equipo de físicos liderado por <b>Yuki Sugiyama</b> (Universidad de Nagoya, Japón) llevó a cabo un experimento histórico publicado en <i>New Journal of Physics</i>. Construyeron una <b>pista circular cerrada de 230 metros de circunferencia</b> e introdujeron a <b>22 conductores en coches reales</b> con una consigna muy simple: <i>«Circulad todos a 30 km/h constantes, manteniendo la misma distancia con el coche de delante»</i>. No había cruces, semáforos, obras ni peatones. En teoría, todos deberían haber rodado eternamente a 30 km/h. Sin embargo, en pocos minutos <b>se produjo un atasco colosal donde varios coches quedaron detenidos por completo (0 km/h)</b>.",
        body_style
    ))

    # Las 3 Zonas de Densidad
    story.append(Paragraph("2. Las 3 Zonas de Densidad: ¿Por qué con 20 no hay atasco y con 23 surge solo?", h1_style))
    
    zone_data = [
        [
            Paragraph("<b>ZONA 1: ≤ 20 COCHES (Flujo Estable)</b>", ParagraphStyle('Z1', parent=table_th, textColor=c_green)),
            Paragraph("<b>ZONA 2: 22 COCHES (Umbral Sugiyama)</b>", ParagraphStyle('Z2', parent=table_th, textColor=c_amber)),
            Paragraph("<b>ZONA 3: ≥ 23 COCHES (Inestabilidad Espontánea)</b>", ParagraphStyle('Z3', parent=table_th, textColor=c_red))
        ],
        [
            Paragraph("• Espaciado medio: <b>&gt;11.5 metros</b>.<br/>• Régimen <b>linealmente estable</b>.<br/>• Si un coche varía de velocidad o frena suavemente, el espacio es suficiente para que el coche posterior absorba la deceleración sin detenerse.<br/>• <b>Resultado:</b> Flujo uniforme verde.", box_body),
            Paragraph("• Espaciado medio: <b>10.4 metros</b>.<br/>• Régimen <b>metaestable (crítico)</b>.<br/>• Si todos condujeran como robots perfectos rodarían; pero si <b>un solo conductor frena</b> o reacciona tarde, la deceleración se amplifica hacia atrás.<br/>• <b>Resultado:</b> Onda retrógrada a 0 km/h.", box_body),
            Paragraph("• Espaciado medio: <b>&lt;9.5 metros</b>.<br/>• Régimen <b>intrínsecamente inestable</b>.<br/>• <b>¡No hace falta que nadie frene!</b> Las micro-fluctuaciones biológicas inconscientes del ser humano (parpadeo, pulso) desencadenan el atasco en segundos.<br/>• <b>Resultado:</b> Colapso inevitable.", box_body)
        ]
    ]
    t_zones = Table(zone_data, colWidths=[180, 180, 180])
    t_zones.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#F0FDF4')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#FEFCE8')),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor('#FEF2F2')),
        ('BOX', (0,0), (0,-1), 1, colors.HexColor('#4ADE80')),
        ('BOX', (1,0), (1,-1), 1, colors.HexColor('#FBBF24')),
        ('BOX', (2,0), (2,-1), 1, colors.HexColor('#F87171')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_zones)
    story.append(Spacer(1, 4))

    # La Onda de Choque Retrógrada
    story.append(Paragraph("3. La Física de la Onda de Choque Retrógrada (El 'Efecto Acordeón')", h1_style))
    story.append(Paragraph(
        "El atasco fantasma se comporta exactamente igual que una onda de choque en dinámica de fluidos (llamada en física <i>Jamiton</i>). Cuando un coche decelera de 30 a 20 km/h, el coche de atrás no reacciona al instante: <b>tarda entre 0.8 y 1.2 segundos (tiempo de reacción psicomotor humano)</b>. Por culpa de ese retraso, se acerca demasiado y se ve forzado a frenar más fuerte (de 30 a 10 km/h). El tercer coche debe clavar el freno a 0 km/h. La 'mancha' de vehículos detenidos <b>viaja físicamente hacia atrás</b> a unos 15-20 km/h en sentido contrario a la marcha de los coches.",
        body_style
    ))

    # La Solución con Inteligencia Artificial
    story.append(Paragraph("4. La Revolución del Tráfico Autónomo Conectado con IA (V2V / CACC)", h1_style))
    ai_box_data = [[
        Paragraph(
            "<b>¿Por qué la IA soluciona el problema de raíz?</b><br/>"
            "El fallo nunca estuvo en los coches ni en la carretera: <b>estuvo en el tiempo de reacción humano</b>.<br/>"
            "1. <b>Reacción en 1 milisegundo (V2V):</b> Los vehículos autónomos conectados por radio V2V (Vehicle-to-Vehicle) saben en tiempo real cuándo acelera o frena el vehículo delantero y el que va tres puestos por delante.<br/>"
            "2. <b>Control de Crucero Adaptativo Coordinado (CACC):</b> En lugar de frenazos bruscos, la IA modula aceleraciones predictivas en milisegundos, amortiguando cualquier perturbación.<br/>"
            "3. <b>Eliminación del Atasco con 25 y 28 Coches:</b> En el simulador, al conmutar a <i>Modo Autónomo IA</i>, el atasco desaparece de inmediato y todos los coches circulan uniformemente a 30 km/h constantes sin detenerse jamás.",
            box_body
        )
    ]]
    t_ai = Table(ai_box_data, colWidths=[PAGE_WIDTH])
    t_ai.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FAF5FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#C084FC')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_ai)
    story.append(Spacer(1, 4))

    # Taller Práctico con el Simulador
    story.append(Paragraph("5. Taller Interactivo en Clase con el Simulador HTML", h1_style))
    story.append(Paragraph(
        "Abre el archivo interactivo <code>SIMULADOR_ATASCO_FANTASMA_SUGIYAMA.html</code> en tu navegador Chrome/Edge y experimenta los 4 pasos clave:",
        body_style
    ))

    steps_table = [
        [Paragraph("Paso 1: 20 Coches", table_th), Paragraph("Paso 2: 22 Coches + Frenazo", table_th), Paragraph("Paso 3: 25 Coches Espontáneo", table_th), Paragraph("Paso 4: Conmutar a Modo IA", table_th)],
        [
            Paragraph("Pulsa <b>20 Coches</b> y luego el botón <i>'Provocar Frenazo'</i>. Observa cómo la frenada se disipa en 2 vueltas y el tráfico se recupera en verde.", table_td),
            Paragraph("Pulsa <b>22 Coches</b> y pulsa <i>'Provocar Frenazo'</i>. Comprueba cómo los coches de atrás caen a <b>0 km/h</b> y la onda roja viaja en sentido antihorario.", table_td),
            Paragraph("Pulsa <b>25 Coches</b> <u>sin tocar el freno</u>. Mira cómo en 10 segundos nace un atasco completo únicamente por el micro-ruido humano.", table_td),
            Paragraph("Con el atasco activo en 25 coches, activa <b>Modo Autónomo IA</b>. Observa cómo en 5 segundos la IA disuelve el atasco por completo.", table_td)
        ]
    ]
    t_steps = Table(steps_table, colWidths=[135, 135, 135, 135])
    t_steps.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_steps)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✅ Ficha didáctica PDF generada: {PDF_PATH}", flush=True)

if __name__ == "__main__":
    compilar_pdf()
