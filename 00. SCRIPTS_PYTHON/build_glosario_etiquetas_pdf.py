#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_glosario_etiquetas_pdf.py
Genera el PDF oficial del Glosario de Etiquetas del Curso de IA para Mayores
y actualiza los archivos CSV (IA_INDICE.csv y IA_INDICE_COMPLETO_60_SESIONES.csv)
para que figure como material destacado al inicio de Google Classroom.
"""

import os
import csv
import urllib.parse
import unicodedata
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

ROOT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
OUTPUT_DIR_PDF = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "00. [GUIA] GLOSARIO_DE_ETIQUETAS")
PDF_FILENAME = "00. GLOSARIO_ETIQUETAS_DEL_CURSO.pdf"
PDF_FULL_PATH = os.path.join(OUTPUT_DIR_PDF, PDF_FILENAME)
BASE_URL = "https://javiercursocorreo-gif.github.io/Curso-IA/"

ETIQUETAS_DATA = [
    {
        "sigla": "[TXT]",
        "nombre": "Prompts de Comunicación y Texto",
        "area": "Lenguaje, Redacción y Asistencia Personal",
        "descripcion": "El poder de la palabra en la IA. Aprender a dialogar de tú a tú con la IA en lenguaje natural y sin tecnicismos.",
        "ejemplos": "Cartas de reclamación formales, comparativas de compras, menús para la salud, correos de comunidad y resúmenes."
    },
    {
        "sigla": "[EST]",
        "nombre": "Estilos Visuales de Imagen",
        "area": "Creatividad Visual y Dirección de Arte",
        "descripcion": "Aprender a pedir estilos artísticos y fotográficos precisos para conseguir exactamente la imagen que imaginas.",
        "ejemplos": "Fotorrealismo, acuarela, óleo renacentista, ilustración editorial, cómic vintage e iluminación cinematográfica."
    },
    {
        "sigla": "[PRAC]",
        "nombre": "Talleres Prácticos con Gemini",
        "area": "Práctica Dinámica y Creatividad en Vivo",
        "descripcion": "Ejercicios dinámicos guiados para perder el miedo a la herramienta y obtener resultados sorprendentes en pocos minutos.",
        "ejemplos": "Retrato mágico de época (reyes, aristócratas), disfraces digitales y transformaciones artísticas personalizadas."
    },
    {
        "sigla": "[FRAC]",
        "nombre": "Fractales en IA (Vídeos y Fichas)",
        "area": "Geometría Natural y Asombro Visual",
        "descripcion": "La matemática secreta de la naturaleza explicada visualmente. Estimula la agudeza visual y la curiosidad científica.",
        "ejemplos": "Fractales de Mandelbrot y Julia, biomimética en el cuerpo humano (pulmones, vasos sanguíneos) y zooms en vídeo."
    },
    {
        "sigla": "[FUNC]",
        "nombre": "Funciones 3D y Gráficos Matemáticos",
        "area": "Visualización Espacial e Intuición Matemática",
        "descripcion": "Representación tridimensional de curvas y superficies matemáticas complejas con texturas realistas mediante IA.",
        "ejemplos": "Paraboloides, sillas de montar, ondas sinusoidales en 3D y superficies de revolución artística."
    },
    {
        "sigla": "[INT]",
        "nombre": "El Mundo por Dentro y Reconstrucción",
        "area": "Corte Transversal, Arquitectura e Historia",
        "descripcion": "Inspeccionar las grandes obras de la humanidad por dentro y viajar al pasado mediante reconstrucciones históricas.",
        "ejemplos": "La Gran Biblioteca de Alejandría, catedrales góticas por dentro, pirámides egipcias y barcos históricos seccionados."
    },
    {
        "sigla": "[FUT]",
        "nombre": "Línea de Tiempo del Futuro (Sci-Fi 2030+)",
        "area": "Prospectiva y Tecnología Amable",
        "descripcion": "Explorar el futuro tecnológico desde una perspectiva optimista, cercana y centrada en el bienestar de las personas.",
        "ejemplos": "El robot asistencial en el hogar de 2028, ciudades verdes sostenibles, medicina preventiva y transporte inteligente."
    },
    {
        "sigla": "[NAT]",
        "nombre": "Naturaleza Fascinante y Biodiversidad",
        "area": "Zoología, Botánica e Infografías Científicas",
        "descripcion": "Descubrir los prodigios del reino animal y vegetal con infografías de alta resolución generadas por IA.",
        "ejemplos": "Biomecánica del galope del caballo, anatomía de aves rapaces, bosques milenarios y ecosistemas submarinos."
    },
    {
        "sigla": "[ARTE]",
        "nombre": "Obras Maestras del Arte Universal",
        "area": "Historia del Arte y Apreciación Cultural",
        "descripcion": "Análisis profundo de los cuadros más célebres de la historia: composición, contexto histórico y reinterpretación creativa.",
        "ejemplos": "La Gioconda de Da Vinci, Las Meninas de Velázquez, La Noche Estrellada de Van Gogh y El Guernica de Picasso."
    },
    {
        "sigla": "[NIV]",
        "nombre": "Escalafones y Niveles (Cultura 101)",
        "area": "Clasificaciones del Mundo y Pensamiento Lógico",
        "descripcion": "Entender cómo se jerarquiza y estructura el conocimiento humano en escalas, etapas y categorías universales.",
        "ejemplos": "Los 7 niveles de riqueza financiera, escalas sísmicas, evolución del universo, escalas de dureza y grados de maestría."
    },
    {
        "sigla": "[TRUC]",
        "nombre": "Trucos y Soluciones Cotidianas",
        "area": "Vida Práctica, Hogar y Autosuficiencia",
        "descripcion": "Soluciones ingeniosas y comprobadas a problemas domésticos del día a día empleando la IA como aliada experta.",
        "ejemplos": "Eliminación ecológica de manchas difíciles, recetas con restos de nevera, orden del hogar y cuidado de plantas."
    },
    {
        "sigla": "[CUENT]",
        "nombre": "Cuentos Ilustrados para Nietos",
        "area": "Narrativa Familiar y Vínculo Afectivo",
        "descripcion": "Metodología integral para crear cuentos infantiles personalizados con valores educativos, guiones e ilustraciones.",
        "ejemplos": "El perro bombero valiente, aventuras espaciales con el nieto de protagonista y fábulas sobre la generosidad."
    },
    {
        "sigla": "[MOVIL]",
        "nombre": "El Salvavidas del Móvil (Cámara y Voz)",
        "area": "Autonomía en Smartphones y Gemini Multimodal",
        "descripcion": "Aprender a usar la cámara y el micrófono del teléfono móvil para resolver dudas en el momento exacto en que surgen.",
        "ejemplos": "Descifrar símbolos de lavado en etiquetas de ropa, traducir prospectos médicos o identificar objetos antiguos."
    },
    {
        "sigla": "[MEM]",
        "nombre": "Cápsula de la Memoria",
        "area": "Historia de Vida y Legado Familiar",
        "descripcion": "Recuperar vivencias, anécdotas de juventud y la historia viva de nuestros pueblos y barrios para las nuevas generaciones.",
        "ejemplos": "Juegos populares de calle (peonza, canicas), el barrio en los años 50, oficios tradicionales y fotografías familiares."
    },
    {
        "sigla": "[MEC]",
        "nombre": "Cómo Funcionan las Cosas (Vídeo 3D)",
        "area": "Ingeniería Cotidiana y Mecánica Divulgativa",
        "descripcion": "Comprender los ingenios mecánicos del mundo moderno mediante animaciones 3D generadas por IA de 10 segundos.",
        "ejemplos": "El cilindro del motor de 4 tiempos, el sistema de frenos hidráulicos, turbinas de avión y engranajes de reloj."
    }
]

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
            self.draw_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_decorations(self, page_count):
        self.saveState()
        # Top banner
        self.setFillColor(colors.HexColor("#0A2540"))
        self.rect(0, letter[1] - 32, letter[0], 32, stroke=0, fill=1)
        
        self.setFillColor(colors.white)
        self.setFont("Helvetica-Bold", 9)
        self.drawString(35, letter[1] - 20, "CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES — DOCUMENTO MAESTRO")
        
        # Bottom rule & footer
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(35, 38, letter[0] - 35, 38)
        
        self.setFillColor(colors.HexColor("#64748B"))
        self.setFont("Helvetica", 8.5)
        self.drawString(35, 24, "Guía de Consulta: Significado y Objetivo Pedagógico de las Etiquetas del Curso")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(letter[0] - 35, 24, page_str)
        self.restoreState()

def build_pdf():
    os.makedirs(OUTPUT_DIR_PDF, exist_ok=True)
    doc = SimpleDocTemplate(
        PDF_FULL_PATH,
        pagesize=letter,
        leftMargin=35,
        rightMargin=35,
        topMargin=46,
        bottomMargin=48
    )
    
    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#0A2540"),
        alignment=TA_CENTER,
        spaceAfter=4
    )
    
    style_subtitle = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#E65C00"),
        alignment=TA_CENTER,
        spaceAfter=12
    )
    
    style_intro = ParagraphStyle(
        'IntroText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#334155"),
        alignment=TA_JUSTIFY,
        spaceAfter=10
    )
    
    style_badge = ParagraphStyle(
        'BadgeStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=colors.HexColor("#0A2540")
    )
    
    style_cat = ParagraphStyle(
        'CatStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#E65C00")
    )
    
    style_desc = ParagraphStyle(
        'DescStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#1E293B")
    )
    
    style_ejemplos = ParagraphStyle(
        'EjemplosStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#475569")
    )
    
    elements = []
    
    elements.append(Paragraph("GLOSARIO OFICIAL DE ETIQUETAS DEL CURSO", style_title))
    elements.append(Paragraph("Guía Rápida de Identificación y Metodología de las Sesiones", style_subtitle))
    
    intro_html = (
        "<b>¿Por qué usamos etiquetas en el curso?</b> Para organizar el aprendizaje de forma clara y amena, "
        "cada actividad y material del curso se identifica con una sigla de 3 o 4 letras entre corchetes "
        "(ej: <code>[TXT]</code>, <code>[EST]</code>, <code>[CUENT]</code>). De este modo, tanto el profesor como los alumnos "
        "saben al instante qué habilidad se entrena en cada ficha: redacción, creatividad visual, solución de problemas cotidianos "
        "o rescate de memorias familiares."
    )
    
    # Caja de introducción destacada
    intro_table = Table(
        [[Paragraph(intro_html, style_intro)]],
        colWidths=[letter[0] - 70]
    )
    intro_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F1F5F9")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ]))
    elements.append(intro_table)
    elements.append(Spacer(1, 10))
    
    # Tabla de etiquetas
    table_data = [
        [
            Paragraph("<b>Sigla y Nombre</b>", ParagraphStyle('TH1', fontName='Helvetica-Bold', fontSize=9, textColor=colors.white, alignment=TA_CENTER)),
            Paragraph("<b>Significado, Objetivo y Ejemplos de Actividades</b>", ParagraphStyle('TH2', fontName='Helvetica-Bold', fontSize=9, textColor=colors.white, alignment=TA_CENTER))
        ]
    ]
    
    for idx, item in enumerate(ETIQUETAS_DATA):
        col1_content = [
            Paragraph(f"<b>{item['sigla']}</b>", style_badge),
            Spacer(1, 2),
            Paragraph(f"<b>{item['nombre']}</b>", style_desc),
            Spacer(1, 3),
            Paragraph(f"📌 {item['area']}", style_cat)
        ]
        
        col2_content = [
            Paragraph(f"<b>Objetivo:</b> {item['descripcion']}", style_desc),
            Spacer(1, 3),
            Paragraph(f"<b>Ejemplos prácticos:</b> {item['ejemplos']}", style_ejemplos)
        ]
        
        table_data.append([col1_content, col2_content])
    
    col_w1 = 175
    col_w2 = (letter[0] - 70) - col_w1
    
    glossary_table = Table(table_data, colWidths=[col_w1, col_w2], repeatRows=1)
    
    t_style = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0A2540")),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#0A2540")),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]
    
    # Alternating row colors
    for r in range(1, len(table_data)):
        bg = colors.HexColor("#FFFFFF") if r % 2 != 0 else colors.HexColor("#F8FAFC")
        t_style.append(('BACKGROUND', (0, r), (-1, r), bg))
        
    glossary_table.setStyle(TableStyle(t_style))
    elements.append(glossary_table)
    
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"✅ PDF generado con éxito: {PDF_FULL_PATH}")

def update_csv_indices():
    # URL de GitHub para el nuevo fichero
    rel_path = os.path.relpath(PDF_FULL_PATH, ROOT_DIR)
    rel_path_nfc = unicodedata.normalize('NFC', rel_path)
    url_pdf = BASE_URL + urllib.parse.quote(rel_path_nfc)
    
    glosario_row = [
        '',
        '00. [GUÍA] Glosario de Etiquetas y Metodología',
        'Glosario de Etiquetas del Curso (Qué significa cada sigla: TXT, EST, PRAC...) (PDF)',
        'Guía oficial de referencia rápida. Explica el significado pedagógico, objetivo y ejemplos de las 15 etiquetas del curso.',
        url_pdf
    ]
    
    target_csvs = [
        os.path.join(ROOT_DIR, "PANELES_CSV", "IA_INDICE.csv"),
        os.path.join(ROOT_DIR, "PANELES_CSV", "IA_INDICE_COMPLETO_60_SESIONES.csv")
    ]
    
    for csv_path in target_csvs:
        if not os.path.exists(csv_path):
            continue
            
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = list(csv.reader(f))
            
        if not reader:
            continue
            
        header = reader[0]
        rows = reader[1:]
        
        # Eliminar si ya existía una fila de glosario previa
        filtered_rows = [r for r in rows if not ('Glosario de Etiquetas' in r[2] or '00. [GUÍA]' in r[1])]
        
        # Insertar al principio justo tras el header
        new_rows = [glosario_row] + filtered_rows
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(new_rows)
            
        print(f"✅ CSV actualizado con la fila del Glosario: {os.path.basename(csv_path)}")

if __name__ == "__main__":
    build_pdf()
    update_csv_indices()
