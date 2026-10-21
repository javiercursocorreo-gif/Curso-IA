# -*- coding: utf-8 -*-
import os
import re
import shutil
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.units import cm

import build_niv_60_master as build_niv

LEGACY_NIV_NAMES = {
    1: "9. NIV-001_Los 7 Niveles de Riqueza y Libertad Financiera.pdf",
    2: "9. NIV-002_Los 6 Niveles de las Pirámides y Fraudes Financieros Históricos.pdf",
    3: "9. NIV-003_Los 5 Niveles del Poder Geopolítico y Hegemonía Mundial.pdf",
    4: "9. NIV-004_Los 6 Niveles de Aporte de Valor en una Empresa.pdf",
    5: "9. NIV-005_Los 5 Niveles de la Evolución del Dinero.pdf",
    6: "9. NIV-006_Los 6 Niveles del Poder Adquisitivo y Coste de Vida Global.pdf",
    7: "9. NIV-007_Los 5 Niveles de Automatización del Trabajo Humano.pdf",
    8: "9. NIV-008_Los 6 Niveles de Persuasión e Influencia de Masas.pdf",
    9: "9. NIV-009_Los 5 Niveles de Seguridad Ciudadana y Prevención Urbana.pdf",
    10: "9. NIV-010_Los 6 Niveles de Alfabetización Financiera Personal.pdf",
    11: "9. NIV-011_Los 7 Niveles de Inteligencia Cognitiva y Conciencia.pdf",
    12: "9. NIV-012_Los 6 Niveles de Conciencia y Alerta Neurológica.pdf",
    13: "9. NIV-013_Los 5 Niveles de la Memoria y Retención Biológica.pdf",
    14: "9. NIV-014_Los 6 Niveles de Toma de Decisiones y Sesgos Cognitivos.pdf",
    15: "9. NIV-015_Los 5 Niveles de Resiliencia y Salud Mental.pdf",
    16: "9. NIV-016_Los 6 Niveles de Adicción y Dependencia Neuroquímica.pdf",
    17: "9. NIV-017_Los 5 Niveles de Empatía e Inteligencia Emocional.pdf",
    18: "9. NIV-018_Los 6 Niveles de Disciplina y Formación de Hábitos.pdf",
    19: "9. NIV-019_Los 5 Niveles de la Comunicación y Lenguaje Biológico.pdf",
    20: "9. NIV-020_Los 6 Niveles de Creatividad e Innovación Humana.pdf",
    21: "9. NIV-021_La Escala del Universo (De lo Subatómico a lo Macroscópico).pdf",
    22: "9. NIV-022_La Escala de Kardashev (Los 5 Niveles de Civilización Energética).pdf",
    23: "9. NIV-023_Los 7 Niveles de Temperatura en el Cosmos.pdf",
    24: "9. NIV-024_Los 6 Niveles de la Gravedad en el Espacio-Tiempo.pdf",
    25: "9. NIV-025_Los 5 Niveles de Velocidad y Cinética en el Universo.pdf",
    26: "9. NIV-026_Los 6 Niveles del Espectro Electromagnético y Frecuencia.pdf",
    27: "9. NIV-027_Los 5 Niveles del Tiempo Biológico, Geológico y Cósmico.pdf",
    28: "9. NIV-028_Los 6 Niveles de Presión Físico-Química.pdf",
    29: "9. NIV-029_Los 5 Niveles de los Estados Físicos de la Materia.pdf",
    30: "9. NIV-030_Los 6 Niveles de Radioactividad e Impacto Ionizante.pdf"
}

def create_niv_fichas():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_repo_dir = os.path.abspath(os.path.join(script_dir, ".."))
    classroom_dir = os.path.join(base_repo_dir, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF")
    base_out_dir = os.path.join(classroom_dir, "[NIV] BLOQUE_10_ESCALAFONES_Y_NIVELES_CULTURA101")
    sessions_dir = os.path.join(classroom_dir, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
    
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
            
        # Limpieza de título para nombre de archivo seguro
        clean_code = re.sub(r'[^A-Za-z0-9_-]', '', id_code)
        clean_title = re.sub(r'[^A-Za-z0-9_ -]', '', title).strip().replace(' ', '_')
        clean_title = re.sub(r'_+', '_', clean_title)[:40].rstrip('_')
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

        # Copiar también a la carpeta de sesión correspondiente
        sess_name = f"{idx:02d}_Sesion" if idx < 60 else "60_Sesion_Cierre"
        sess_folder = os.path.join(sessions_dir, sess_name)
        os.makedirs(sess_folder, exist_ok=True)
        
        # 1. Copia principal con el nombre nuevo normalizado
        dst_sess_pdf = os.path.join(sess_folder, f"9. NIV-{idx:03d}_{clean_title}.pdf")
        shutil.copy2(file_path, dst_sess_pdf)
        
        # 2. Copia de compatibilidad total con el nombre legado (garantiza cero 404 en Classroom y cachés)
        if idx in LEGACY_NIV_NAMES:
            legacy_pdf = os.path.join(sess_folder, LEGACY_NIV_NAMES[idx])
            shutil.copy2(file_path, legacy_pdf)
            print(f"  ✓ Replicado en {sess_name}: {os.path.basename(dst_sess_pdf)} (+ copia de compatibilidad)")
        else:
            print(f"  ✓ Replicado en {sess_name}: {os.path.basename(dst_sess_pdf)}")
        
    print(f"\n¡Éxito total! Las 60 fichas PDF [NIV] han sido exportadas y distribuidas en las 60 sesiones.")

if __name__ == '__main__':
    import shutil
    create_niv_fichas()
