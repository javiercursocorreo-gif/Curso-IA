# -*- coding: utf-8 -*-
"""
Generador de la Ficha/Infografía de Bienvenida del Alumno para la Clase 0 (Inaugural)
Diseño editorial limpio, tipografía grande, colores de la identidad del curso y estructura en 5 bloques.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import cm

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PDF = os.path.join(ROOT_DIR, "CLASES", "0. INTRODUCCION A LA IA", "CLASE_0_Infografia_Bienvenida_Alumno.pdf")

def create_welcome_infographic():
    os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
    if os.path.exists(OUT_PDF):
        try: os.remove(OUT_PDF)
        except Exception: pass

    doc = SimpleDocTemplate(
        OUT_PDF,
        pagesize=A4,
        leftMargin=1.5*cm,
        rightMargin=1.5*cm,
        topMargin=1.2*cm,
        bottomMargin=1.2*cm
    )

    styles = getSampleStyleSheet()

    # Colores corporativos
    c_primary = colors.HexColor('#1A0A2E')   # Morado profundo
    c_accent = colors.HexColor('#4F46E5')    # Azul IA / Índigo
    c_dark = colors.HexColor('#0F172A')      # Texto oscuro
    c_green = colors.HexColor('#16A34A')     # Verde éxito
    c_amber = colors.HexColor('#D97706')     # Ámbar dorado

    title_h1 = ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.white,
        alignment=1
    )

    subtitle_h1 = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#E0E7FF'),
        alignment=1
    )

    sec_title = ParagraphStyle(
        'SecTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=c_primary,
        spaceAfter=3
    )

    sec_body = ParagraphStyle(
        'SecBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=c_dark
    )

    sec_quote = ParagraphStyle(
        'SecQuote',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=16,
        textColor=colors.HexColor('#78350F'),
        alignment=1
    )

    story = []

    # 1. Cabecera Principal
    h1 = Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL PARA PERSONAS MAYORES", title_h1)
    h2 = Paragraph("CLASE 0 · GUÍA DE BIENVENIDA: ¿POR QUÉ LA INTELIGENCIA ARTIFICIAL ES PARA TI?", subtitle_h1)
    header_table = Table([[h1], [h2]], colWidths=[18*cm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_primary),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('PADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 10))

    # 2. Bloque 1: La Idea Central
    b1_title = Paragraph("💡 1. LA IDEA CENTRAL: TU ASISTENTE INCANSABLE", sec_title)
    b1_body = Paragraph(
        "Imagina que tienes a tu disposición a un <b>ayudante de confianza que ha leído millones de libros</b> de cocina, "
        "salud, historia, mecánica y viajes. Nunca se cansa, no duerme, tiene paciencia infinita y está esperando a que "
        "tú le hagas preguntas con tus propias palabras.", sec_body
    )
    t1 = Table([[b1_title], [b1_body]], colWidths=[18*cm], style=[
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EEF2FF')),
        ('BOX', (0,0), (-1,-1), 1.2, c_accent),
        ('PADDING', (0,0), (-1,-1), 8),
    ])
    story.append(t1)
    story.append(Spacer(1, 9))

    # 3. Bloque 2: Tres Mitos Desmontados
    b2_title = Paragraph("❌ 2. TRES MITOS DESMONTADOS (QUÉ NO ES LA IA)", sec_title)
    mito1 = Paragraph("• <b>No es magia ni peligro:</b> Son matemáticas avanzadas procesando millones de datos en milésimas de segundo.", sec_body)
    mito2 = Paragraph("• <b>No es un robot con cuerpo:</b> No tiene ojos ni sentimientos; es un programa en pantalla que comprende el lenguaje humano.", sec_body)
    mito3 = Paragraph("• <b>No es infalible (se equivoca):</b> Tú siempre tienes el mando, la experiencia de vida y el sentido común para decidir si te convence su respuesta.", sec_body)
    t2 = Table([[b2_title], [mito1], [mito2], [mito3]], colWidths=[18*cm], style=[
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF1F2')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#E11D48')),
        ('PADDING', (0,0), (-1,-1), 8),
    ])
    story.append(t2)
    story.append(Spacer(1, 9))

    # 4. Bloque 3: Cómo se le habla
    b3_title = Paragraph("💬 3. CÓMO HABLARLE: EL SECRETO DEL WHATSAPP", sec_title)
    b3_body = Paragraph(
        "<b>No necesitas saber informática ni utilizar palabras técnicas.</b><br/>"
        "Hablarle a la IA (lo que los técnicos llaman <i>«Prompt»</i>) es exactamente igual que <b>escribirle o dictarle un mensaje a un amigo por WhatsApp</b>. "
        "Cuantos más detalles cotidianos le des sobre lo que necesitas, más útil y acertada será su respuesta.", sec_body
    )
    t3 = Table([[b3_title], [b3_body]], colWidths=[18*cm], style=[
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 1.2, c_green),
        ('PADDING', (0,0), (-1,-1), 8),
    ])
    story.append(t3)
    story.append(Spacer(1, 9))

    # 5. Bloque 4: La Regla de Oro
    b4_title = Paragraph("⭐ 4. LA REGLA DE ORO DE NUESTRA CLASE", sec_title)
    b4_quote = Paragraph("«EN ESTE CURSO NO EXISTEN LAS PREGUNTAS TONTAS»", sec_quote)
    b4_desc = Paragraph(
        "La Inteligencia Artificial nunca se impacienta, nunca se cansa y <b>jamás te juzgará</b>. "
        "Puedes preguntarle lo mismo veinte veces, pedirle que te lo explique como si tuvieras 10 años, "
        "o pedirle que repita un paso con total tranquilidad.", sec_body
    )
    t4 = Table([[b4_title], [b4_quote], [b4_desc]], colWidths=[18*cm], style=[
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF9C3')),
        ('BOX', (0,0), (-1,-1), 1.2, c_amber),
        ('ALIGN', (0,1), (-1,1), 'CENTER'),
        ('PADDING', (0,0), (-1,-1), 8),
    ])
    story.append(t4)
    story.append(Spacer(1, 9))

    # 6. Bloque 5: Misión para la Clase 1
    b5_title = Paragraph("🎯 5. TU PEQUEÑA MISIÓN PARA LA PRÓXIMA SESIÓN", sec_title)
    b5_body = Paragraph(
        "Piensa en una <b>duda, curiosidad o necesidad real de tu día a día</b>:<br/>"
        "• Un trámite que no entiendes bien, una receta con los ingredientes de tu nevera, el significado de un análisis médico o cómo era tu barrio hace 50 años.<br/>"
        "<b>Tráela anotada en un papel:</b> ¡En la próxima clase nos daremos de alta en Gemini y se lo preguntaremos en directo!", sec_body
    )
    t5 = Table([[b5_title], [b5_body]], colWidths=[18*cm], style=[
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FAF5FF')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#9333EA')),
        ('PADDING', (0,0), (-1,-1), 8),
    ])
    story.append(t5)

    doc.build(story)
    print(f"✅ Infografía de bienvenida creada con éxito: {OUT_PDF}")

if __name__ == '__main__':
    create_welcome_infographic()
