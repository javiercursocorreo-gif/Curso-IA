#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_006.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 6. COD-006_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 06)
- 06_COD-006_Taller_Simulador_Cerebro_Humano_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/06_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "6. COD-006_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/06_COD-006_Taller_Simulador_Cerebro_Humano_3D.pdf"

def build_pdf(dest_path):
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    doc = SimpleDocTemplate(
        dest_path,
        pagesize=letter,
        rightMargin=36, leftMargin=36, topMargin=24, bottomMargin=20
    )
    styles = getSampleStyleSheet()

    accent = colors.HexColor('#0284C7') # Tono cyan/azul neurocientífico

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.2, leading=10.0,
        textColor=accent, alignment=1, spaceAfter=2
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=12.0,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=12.0, leading=14.5,
        textColor=colors.HexColor('#0F172A'), spaceAfter=4
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=9.2, leading=12.0,
        textColor=accent, spaceBefore=4, spaceAfter=3
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=8.0, leading=11.2,
        textColor=colors.HexColor('#1E293B'), spaceAfter=3
    )
    style_box_text = ParagraphStyle(
        'BoxText', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.8, leading=10.8,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    # Encabezado Oficial
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & SIMULADORES CIENTÍFICOS 3D [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent, spaceAfter=5))

    story.append(Paragraph("<b>[COD-006] Guía Neurocientífica • El Encéfalo Humano: Lóbulos Corticales y Conectoma 3D</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🧠 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador biomédico interactivo en 3D permite explorar el <b>encéfalo humano bilateral completo</b>, estructurado en sus regiones corticales funcionales "
        "y sus vías de comunicación bioeléctrica. En pantalla se distinguen los cuatro grandes lóbulos de la corteza cerebral: el <b>Lóbulo Frontal</b> "
        "(sede de las funciones ejecutivas, planificación y corteza motora), el <b>Lóbulo Parietal</b> (integración somatosensorial del tacto, temperatura y dolor), "
        "el <b>Lóbulo Temporal</b> (audición, comprensión del lenguaje e hipocampo de la memoria) y el <b>Lóbulo Occipital</b> (centro primario de procesamiento visual), "
        "junto con el <b>Cerebelo</b> (coordinación motora fina y equilibrio) y el <b>Tronco Encefálico</b> vital.<br/>"
        "El modelo incorpora un <b>conectoma dinámico de 320 haces axonales internos con 380 potenciales de acción luminiscentes</b> que viajan a 40 Hz (ondas Gamma). "
        "Puedes <b>rotar el encéfalo 360°</b>, graduar la <b>opacidad cortical</b> para descubrir las sinapsis profundas en tiempo real, "
        "pulsar sobre las <b>chinchetas 3D</b> para enfocar cada lóbulo y regular la <b>velocidad de disparo bioeléctrico</b>.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Anatómico Oficial:</b> El modelo tridimensional procede del atlas biomédico abierto <b>Z-Anatomy Open-Source Project</b> y de las bases de datos "
        "del proyecto internacional <b>Human Connectome Project</b> (dependiente del <i>National Institutes of Health - NIH</i> y de la Universidad de Tokio - <i>BodyParts3D</i>).<br/>"
        "• <b>Técnica de Adquisición Médica:</b> Reconstrucción volumétrica de alta fidelidad obtenida mediante <b>resonancia magnética nuclear estructural (MRI de 7 Tesla) "
        "y tractografía por tensor de difusión (DTI)</b>. El archivo contiene <b>437 estructuras anatómicas reales</b> (surcos, cisuras, circunvoluciones y red arterial completa), "
        "sin aproximaciones ni geometrías esféricas artificiales.<br/>"
        "• <b>Color Tisular y Parámetros Bioeléctricos:</b> Los materiales PBR reproducen el tono tisular gris-rosáceo de la corteza humana (código tisular <i>#d59b8c</i>) con "
        "vasos sanguíneos destacados en carmesí, sincronizados con la frecuencia fisiológica de disparo axonal a 40 Hz de los circuitos talamocorticales."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1.2, accent),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_box)
    story.append(Spacer(1, 4))

    # Bloque 3: Guía de Exploración & Retos de Conversación con Gemini
    story.append(Paragraph("💬 <b>3. Guía de Exploración en el Aula & Conversación con Gemini</b>", style_section_h))
    story.append(Paragraph(
        "Abre el simulador en tu pantalla (en el mapa pulsa <i>«🧠 Ver Simulador Cerebro 3D»</i>) y utilízalo como laboratorio interactivo mientras conversas con "
        "Gemini (<i>gemini.google.com</i>):",
        style_body
    ))

    prompts_text = (
        "<b>1. Neuroplasticidad:</b> <i>«Estoy mirando un modelo 3D del cerebro humano. ¿Cómo consiguen las personas mayores de 60 años crear nuevas conexiones neuronales (neuroplasticidad) al aprender tecnología o tocar un instrumento?»</i><br/>"
        "<b>2. Vías y Conectoma:</b> <i>«Al reducir la opacidad en el simulador 3D contemplo las redes bioeléctricas internas. ¿Cómo se comunican ambos hemisferios a través del cuerpo calloso para coordinar el pensamiento lógico y la intuición?»</i><br/>"
        "<b>3. Salud Cerebral y Memoria:</b> <i>«¿Por qué el ejercicio físico moderado y el descanso nocturno profundo son tan determinantes para la salud de las neuronas de nuestro lóbulo temporal e hipocampo?»</i>"
    )
    p_box = Table([[Paragraph(prompts_text, style_box_text)]], colWidths=[letter[0] - 72])
    p_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(p_box)
    story.append(Spacer(1, 4))

    story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor('#CBD5E1'), spaceAfter=3))
    style_footer = ParagraphStyle(
        'FooterStyle', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=7.0, leading=8.5,
        textColor=colors.HexColor('#64748B'), alignment=1
    )
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Neurociencia visual y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-006 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-006 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
