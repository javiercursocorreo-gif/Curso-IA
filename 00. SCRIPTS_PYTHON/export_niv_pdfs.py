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
        is_senior = item.get('is_senior_microapp', False)
        
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
        
        if is_senior:
            # =================================================================
            # FORMATO TRIPLE SALVAGUARDA PEDAGÓGICA (SENIORS +65)
            # =================================================================
            sim_file = item.get('sim_file', 'SIMULADOR.html')
            sim_title = item.get('sim_title', title)
            seed_step1 = item.get('seed_step1', '')
            seed_step2 = item.get('seed_step2', '')
            blueprint = item.get('blueprint', '')

            # 1. Header Box (Verde Esmeralda Micro-App)
            header_p1 = Paragraph(f"<b>{id_code} — {title}</b>", title_style)
            header_p2 = Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL — MICRO-APLICACIÓN INTERACTIVA (+65) — LA TRIPLE SALVAGUARDA", subtitle_style)
            
            header_table = Table([[header_p1], [header_p2]], colWidths=[18*cm])
            header_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#065F46')), # Emerald Dark
                ('PADDING', (0,0), (-1,-1), 10),
                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                ('BOTTOMPADDING', (0,0), (-1,-1), 10),
            ]))
            story.append(header_table)
            story.append(Spacer(1, 10))

            # 2. Utilidad Práctica
            story.append(Paragraph("<b>1. UTILIDAD PRÁCTICA Y BENEFICIO EN EL HOGAR</b>", sec_title_style))
            story.append(Paragraph(concept, body_style))
            story.append(Spacer(1, 10))

            # 3. Experiencia Activa (Prompt Semilla en 2 Pasos)
            story.append(Paragraph("<b>2. EXPERIENCIA ACTIVA: EL PROMPT SEMILLA HUMANO (EN 2 PASOS)</b>", sec_title_style))
            
            step1_html = f"<b>Paso 1 (Dicta o escribe a Gemini):</b><br/>{seed_step1.replace(chr(10), '<br/>')}"
            step2_html = f"<b>Paso 2 (Tras la respuesta de Gemini):</b><br/>{seed_step2.replace(chr(10), '<br/>')}"
            
            steps_table = Table([[Paragraph(step1_html, body_style)], [Paragraph(step2_html, body_style)]], colWidths=[18*cm])
            steps_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (0,0), colors.HexColor('#ECFDF5')), # Soft emerald
                ('BACKGROUND', (0,1), (0,1), colors.HexColor('#F0FDF4')), # Lighter green
                ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#10B981')),
                ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#A7F3D0')),
                ('PADDING', (0,0), (-1,-1), 8),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ]))
            story.append(steps_table)
            story.append(Spacer(1, 10))

            # 4. Respaldo Técnico (Plano Maestro Detallado)
            story.append(Paragraph("<b>3. RESPALDO TÉCNICO: PLANO MAESTRO DETALLADO (NIVEL 2)</b>", sec_title_style))
            bp_html = blueprint.replace(chr(10), '<br/>')
            bp_table = Table([[Paragraph(bp_html, prompt_code_style)]], colWidths=[18*cm])
            bp_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
                ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
                ('PADDING', (0,0), (-1,-1), 8),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ]))
            story.append(bp_table)
            story.append(Spacer(1, 10))

            # 5. Garantía Total en el Aula (Nivel 3)
            guarantee_html = (
                f"<b>🛡️ NIVEL 3: GARANTÍA OFICIAL EN EL AULA (CERO FRUSTRACIÓN)</b><br/>"
                f"Si tu ordenador o Gemini tardan en generar el código, no te preocupes ni te quedes rezagado: abre directamente la aplicación oficial ya programada y probada al 100%:<br/>"
                f"• <b>Archivo en Classroom:</b> <font color='#065F46'><b>{sim_file}</b></font><br/>"
                f"• <b>Acceso directo:</b> Pulsa sobre el botón verde esmeralda <b>[{sim_title}]</b> en el Mapa Interactivo de la Sesión."
            )
            story.append(KeepTogether([
                Table([[Paragraph(guarantee_html, tips_style)]], colWidths=[18*cm], style=[
                    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF3C7')), # Soft amber
                    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#D97706')),
                    ('PADDING', (0,0), (-1,-1), 8),
                    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                ])
            ]))

        else:
            # =================================================================
            # FORMATO ESTÁNDAR INFOGRAFÍAS CULTURA 101
            # =================================================================
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
            
            # 3. Prompt Maestro V2 Box
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
        
        doc.build(story)
        print(f"[{idx}/60] Generado: {file_name}")

        # Copiar también a la carpeta de sesión correspondiente
        sessions_dir = os.path.join(os.path.dirname(base_out_dir), "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
        sess_name = f"{idx:02d}_Sesion" if idx < 60 else "60_Sesion_Cierre"
        sess_folder = os.path.join(sessions_dir, sess_name)
        if os.path.exists(sess_folder):
            # Eliminar cualquier ficha NIV anterior en la carpeta
            for ef in os.listdir(sess_folder):
                if ef.startswith("9. NIV-") or ef.startswith("9. [NIV-"):
                    try: os.remove(os.path.join(sess_folder, ef))
                    except Exception: pass
            dst_sess_pdf = os.path.join(sess_folder, f"9. NIV-{idx:03d}_{clean_title}.pdf")
            shutil.copy2(file_path, dst_sess_pdf)
        
    print(f"\n¡Éxito total! Las 60 fichas PDF [NIV] han sido exportadas y distribuidas en las 60 sesiones.")

if __name__ == '__main__':
    import shutil
    create_niv_fichas()
