# -*- coding: utf-8 -*-
import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.units import cm

import build_niv_60_master as build_niv

def create_niv_fichas():
    base_out_dir = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/[NIV] BLOQUE_10_ESCALAFONES_Y_NIVELES_CULTURA101"
    
    lote1 = os.path.join(base_out_dir, "Lote_01_al_20")
    lote2 = os.path.join(base_out_dir, "Lote_21_al_40")
    lote3 = os.path.join(base_out_dir, "Lote_41_al_60")
    
    for folder in [lote1, lote2, lote3]:
        os.makedirs(folder, exist_ok=True)
        
    items = build_niv.get_niv_items()
    print(f"Exportando {len(items)} fichas PDF [NIV] Oficiales de Google Classroom V2...")
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'HeaderTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=1 # Center
    )
    
    subtitle_style = ParagraphStyle(
        'HeaderSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#E2E8F0'),
        alignment=1
    )
    
    sec_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#1E3A8A'), # Deep Blue
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1F2937')
    )
    
    prompt_code_style = ParagraphStyle(
        'PromptCodeText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#0F172A')
    )
    
    tips_style = ParagraphStyle(
        'TipsText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1E293B')
    )

    for idx, item in enumerate(items, 1):
        id_code = item['id_code'] # e.g. [NIV-001]
        title = item['title']
        concept = item['concept_text']
        prompt = item['prompt_data']
        tips = item['tips_text']
        
        # Determine lot folder
        if idx <= 20:
            dest_dir = lote1
        elif idx <= 40:
            dest_dir = lote2
        else:
            dest_dir = lote3
            
        clean_code = re.sub(r'[^A-Za-z0-9_-]', '', id_code)
        clean_title = re.sub(r'[^A-Za-z0-9_-]', '_', title)[:35]
        file_name = f"{clean_code}_{clean_title}.pdf"
        file_path = os.path.join(dest_dir, file_name)
        
        doc = SimpleDocTemplate(
            file_path,
            pagesize=A4,
            leftMargin=1.5*cm,
            rightMargin=1.5*cm,
            topMargin=1.5*cm,
            bottomMargin=1.5*cm
        )
        
        story = []
        
        # 1. Header Box
        header_p1 = Paragraph(f"<b>{id_code} — {title}</b>", title_style)
        header_p2 = Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL — GOOGLE CLASSROOM — BLOQUE 10: ESCALAFONES Y NIVELES (ESTILO CULTURA 101)", subtitle_style)
        
        header_table = Table([[header_p1], [header_p2]], colWidths=[18*cm])
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1E3A8A')),
            ('PADDING', (0,0), (-1,-1), 10),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ]))
        story.append(header_table)
        story.append(Spacer(1, 12))
        
        # 2. Conceptualization Section
        story.append(Paragraph("<b>1. CONCEPTUALIZACIÓN CIENTÍFICO-ENCICLOPÉDICA</b>", sec_title_style))
        story.append(Paragraph(concept, body_style))
        story.append(Spacer(1, 10))
        
        # 3. Prompt Maestro V2 Box (Multi-row table so it splits across pages gracefully)
        story.append(Paragraph("<b>2. PROMPT MAESTRO DE INFOGRAFÍA V2 (COPIAR Y PEGAR EN GEMINI / IMAGEN 3)</b>", sec_title_style))
        
        prompt_parts = [p.strip().replace('\n', '<br/>') for p in prompt.split('\n\n') if p.strip()]
        prompt_rows = [[Paragraph(part, prompt_code_style)] for part in prompt_parts]
        
        prompt_table = Table(prompt_rows, colWidths=[18*cm])
        prompt_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
            ('PADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(prompt_table)
        story.append(Spacer(1, 12))
        
        # 4. Dinámica y Reto Práctico Box
        story.append(KeepTogether([
            Paragraph("<b>3. DINÁMICA DE AULA Y RETO PRÁCTICO EN GOOGLE CLASSROOM</b>", sec_title_style),
            Table([[Paragraph(tips, tips_style)]], colWidths=[18*cm], style=[
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF3C7')), # Light Amber
                ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F59E0B')),
                ('PADDING', (0,0), (-1,-1), 8),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ])
        ]))
        
        doc.build(story)
        print(f"[{idx}/60] Generado: {file_name}")
        
    print(f"\n¡Éxito total! Las 60 fichas PDF [NIV] han sido exportadas a {base_out_dir}")

if __name__ == '__main__':
    create_niv_fichas()
