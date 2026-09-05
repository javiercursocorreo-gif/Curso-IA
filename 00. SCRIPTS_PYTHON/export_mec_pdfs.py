# -*- coding: utf-8 -*-
"""
Exportador de Fichas PDF para [MEC] e Inserción en las 60 Sesiones
Genera:
- 60 Fichas PDF de [MEC] (Paso 14: Cómo Funcionan las Cosas - Ingeniería y Mecánica en Vídeo 3D)
  en CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/14. [MEC] BLOQUE_14_COMO_FUNCIONAN_LAS_COSAS/
  distribuidas en Lote_01_al_20, Lote_21_al_40 y Lote_41_al_60.
- Copia automáticamente cada ficha a cada carpeta de sesión (01_Sesion a 60_Sesion_Cierre)
  con prefijo "14. MEC-xxx_...pdf".
- Regenera los 5 Paneles CSV para Google Classroom.
"""

import os
import re
import shutil
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

from build_mec_60_master import get_mecanica_items

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT_BASE = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF")
SESSIONS_DIR = os.path.join(EXPORT_BASE, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
MEC_BASE_DIR = os.path.join(EXPORT_BASE, "14. [MEC] BLOQUE_14_COMO_FUNCIONAN_LAS_COSAS")

LOTE_1 = os.path.join(MEC_BASE_DIR, "Lote_01_al_20")
LOTE_2 = os.path.join(MEC_BASE_DIR, "Lote_21_al_40")
LOTE_3 = os.path.join(MEC_BASE_DIR, "Lote_41_al_60")

for d in [LOTE_1, LOTE_2, LOTE_3]:
    os.makedirs(d, exist_ok=True)

def sanitize_name(name):
    clean = re.sub(r'[/\\:*?"<>|]', '_', name)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:65]

def create_mec_pdf(file_path, block_name, id_code, title, concept, prompt, tips):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception:
            pass

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        rightMargin=45, leftMargin=45, topMargin=40, bottomMargin=40
    )

    styles = getSampleStyleSheet()

    theme_color = colors.HexColor('#0F4C81')  # Steel / Classic Blue
    accent_color = colors.HexColor('#1B365D') # Deep Navy
    bg_color = colors.HexColor('#F0F4F8')     # Soft Slate Ice

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9,
        textColor=theme_color, spaceAfter=3, alignment=1
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10.5,
        textColor=accent_color, spaceAfter=10, alignment=1
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=13.5, leading=17,
        textColor=accent_color, spaceAfter=10
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=10.5, leading=14,
        textColor=theme_color, spaceBefore=6, spaceAfter=4
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=9, leading=13.5,
        textColor=colors.HexColor('#2C3E50'), spaceAfter=5
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=9, leading=13.5,
        textColor=colors.HexColor('#1A252F')
    )
    style_reto = ParagraphStyle(
        'RetoStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9, leading=13.5,
        textColor=colors.HexColor('#2C3E50')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph(block_name.upper(), style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=theme_color, spaceAfter=10))

    clean_code = id_code.replace('[', '').replace(']', '')
    story.append(Paragraph(f"<b>[{clean_code}] {title}</b>", style_title))

    # 1. Concepto
    story.append(Paragraph("💡 Contexto y Maravilla Mecánica", style_section_h))
    story.append(Paragraph(str(concept).replace('\n', '<br/>'), style_body))
    story.append(Spacer(1, 4))

    # 2. Prompt Vídeo 3D en Gemini
    story.append(Paragraph("🎬 Prompt Maestro para Generar el Vídeo 3D en Gemini (gemini.google.com)", style_section_h))
    p_rows = [
        [Paragraph("<b>• Instrucción en Gemini:</b> Abre un chat nuevo en <b>gemini.google.com</b>, copia este texto exacto y pulsa Enter. Gemini generará un vídeo de 10 segundos en corte transversal animado:", style_prompt)],
        [Paragraph(f'"{str(prompt)}"', style_prompt)]
    ]
    p_table = Table(p_rows, colWidths=[letter[0] - 90], splitByRow=1)
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_color),
        ('BORDER', (0,0), (-1,-1), 1.2, theme_color),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 6))

    # 3. Reto y Pregunta Didáctica
    story.append(Paragraph("🧪 El Reto Práctico / Pregunta de Curiosidad y Debate", style_section_h))
    t_rows = [
        [Paragraph(f"<b>{tips}</b>", style_reto)]
    ]
    t_table = Table(t_rows, colWidths=[letter[0] - 90], splitByRow=1)
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
        ('BORDER', (0,0), (-1,-1), 1.2, theme_color),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_table)

    doc.build(story)

def purge_conflicts():
    for root, dirs, _ in os.walk(EXPORT_BASE):
        for d in dirs:
            if re.search(r'\s+\d+$', d):
                conflict_path = os.path.join(root, d)
                try:
                    shutil.rmtree(conflict_path)
                    print(f"🧹 Eliminada carpeta de conflicto iCloud: {d}")
                except Exception:
                    pass

def main():
    print("🚀 Generando 60 Fichas PDF para Bloque 14 [MEC] (Cómo Funcionan las Cosas)...")
    purge_conflicts()
    
    items = get_mecanica_items()
    mec_files = {}

    for it in items:
        idx = it['num_int']
        clean_code = it['id_code'].replace('[', '').replace(']', '')
        safe_t = sanitize_name(it['title'])
        base_filename = f"{clean_code}_{safe_t}.pdf"

        if idx <= 20:
            target_lote = LOTE_1
        elif idx <= 40:
            target_lote = LOTE_2
        else:
            target_lote = LOTE_3

        full_path = os.path.join(target_lote, base_filename)
        create_mec_pdf(
            full_path,
            it['block_name'],
            it['id_code'],
            it['title'],
            it['concept'],
            it['prompt'],
            it['tips']
        )

        session_filename = f"14. {clean_code}_{safe_t}.pdf"
        mec_files[idx] = (full_path, session_filename)

        if idx % 10 == 0:
            print(f"   ✓ Generadas {idx}/60 Fichas [MEC]")

    print("\n📂 Distribuyendo Ficha 14 en las 60 carpetas de Sesión...")
    all_session_folders = sorted(
        [d for d in os.listdir(SESSIONS_DIR) if os.path.isdir(os.path.join(SESSIONS_DIR, d)) and not d.startswith('.')],
        key=lambda s: [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', s)]
    )

    for s_folder in all_session_folders:
        m = re.match(r'^(\d+)_', s_folder)
        if not m:
            continue
        s_num = int(m.group(1))
        if s_num < 1 or s_num > 60:
            continue

        target_dir = os.path.join(SESSIONS_DIR, s_folder)
        if s_num in mec_files:
            src_path, dst_name = mec_files[s_num]
            dst_path = os.path.join(target_dir, dst_name)
            shutil.copy2(src_path, dst_path)

    print("   ✓ ¡Las 60 carpetas de sesión tienen asignado su Paso 14 [MEC]!")

    print("\n📊 Actualizando Paneles CSV de Google Classroom...")
    import generate_multiple_csvs
    generate_multiple_csvs.main()
    print("\n🎉 ¡PROCESO FINALIZADO CON ÉXITO! Fichas 14 integradas en catálogo y en CSV.")

if __name__ == "__main__":
    main()
