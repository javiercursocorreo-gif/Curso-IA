# -*- coding: utf-8 -*-
"""
Exportador de Fichas PDF para [MOVIL] y [MEM] e Inserción en las 60 Sesiones
Genera:
- 60 Fichas PDF de [MOVIL] (Paso 12: El Salvavidas del Móvil)
- 60 Fichas PDF de [MEM] (Paso 13: Cápsula de la Memoria: Mi Infancia, Mi Barrio y Mi Pueblo)
Y las copia automáticamente a cada carpeta de sesión (01_Sesion a 60_Sesion_Cierre).
Luego regenera los 5 Paneles CSV para Google Classroom.
"""

import os
import re
import shutil
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

from build_movil_60_master import get_movil_items
from build_memoria_60_master import get_memoria_items

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT_BASE = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF")
SESSIONS_DIR = os.path.join(EXPORT_BASE, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

MOVIL_DIR = os.path.join(EXPORT_BASE, "12. [MOVIL] BLOQUE_12_EL_SALVAVIDAS_DEL_MOVIL")
MEM_DIR = os.path.join(EXPORT_BASE, "13. [MEM] BLOQUE_13_CAPSULA_DE_LA_MEMORIA")

os.makedirs(MOVIL_DIR, exist_ok=True)
os.makedirs(MEM_DIR, exist_ok=True)

def sanitize_name(name):
    clean = re.sub(r'[/\\:*?"<>|]', '_', name)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:65]

def create_pdf_card(file_path, block_name, item_id, item_title, concept_text, prompt_data, tips_text, is_movil=True):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if os.path.exists(file_path):
        try: os.remove(file_path)
        except Exception: pass

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45
    )

    styles = getSampleStyleSheet()

    theme_color = colors.HexColor('#008080') if is_movil else colors.HexColor('#B8860B')
    bg_color = colors.HexColor('#EBF6F6') if is_movil else colors.HexColor('#FAF6E8')

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5,
        textColor=theme_color, spaceAfter=4, alignment=1
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=11,
        textColor=colors.HexColor('#1A0A2E'), spaceAfter=12, alignment=1
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=14, leading=18,
        textColor=colors.HexColor('#1A0A2E'), spaceAfter=12
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=11, leading=14,
        textColor=theme_color, spaceBefore=8, spaceAfter=5
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=9.5, leading=14,
        textColor=colors.HexColor('#2C3E50'), spaceAfter=6
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=9.5, leading=14,
        textColor=colors.HexColor('#1A0A2E')
    )
    style_reto = ParagraphStyle(
        'RetoStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9.5, leading=14,
        textColor=colors.HexColor('#2C3E50')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph(block_name.upper(), style_block))
    story.append(HRFlowable(width="100%", thickness=2, color=theme_color, spaceAfter=12))

    story.append(Paragraph(f"{item_id} {item_title}", style_title))

    # Contexto
    section_title = "💡 Utilidad Cotidiana y Objetivo Didáctico" if is_movil else "💡 Vínculo Familiar y Memoria Intergeneracional"
    story.append(Paragraph(section_title, style_section_h))
    clean_c = str(concept_text).replace('\n', '<br/>')
    story.append(Paragraph(clean_c, style_body))
    story.append(Spacer(1, 4))

    # Prompt PC
    prompt_sec_title = "🖥️ Paso 1: Generar la Imagen del Reto en el Ordenador (PC)" if is_movil else "📸 Paso 1: Recrear la Escena con IA en el Ordenador"
    story.append(Paragraph(prompt_sec_title, style_section_h))
    
    p_rows = [
        [Paragraph("<b>• Copia este prompt exacto y pégalo en Gemini Web (gemini.google.com):</b>", style_prompt)],
        [Paragraph(f'"{str(prompt_data)}"', style_prompt)]
    ]
    p_table = Table(p_rows, colWidths=[letter[0] - 90], splitByRow=1)
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_color),
        ('BORDER', (0,0), (-1,-1), 1.5, theme_color),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 8))

    # Reto Móvil / Pregunta Nietos
    tips_sec_title = "📱 Paso 2: El Salvavidas con tu Móvil (Cámara y Voz)" if is_movil else "💬 Paso 2: Para Preguntar y Contar a los Nietos"
    story.append(Paragraph(tips_sec_title, style_section_h))
    
    t_rows = [
        [Paragraph(f"<b>{tips_text}</b>", style_reto)]
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

def main():
    print("🚀 Generando Fichas PDF para Bloque 12 [MOVIL] y Bloque 13 [MEM]...")
    
    movil_items = get_movil_items()
    mem_items = get_memoria_items()
    
    movil_files = {}
    mem_files = {}

    # 1. Generar PDFs de MOVIL
    print("\n📱 Generando 60 Fichas de [MOVIL]...")
    for idx, it in enumerate(movil_items, 1):
        safe_t = sanitize_name(it['title'])
        filename = f"12. {it['id_code']}_{safe_t}.pdf"
        full_path = os.path.join(MOVIL_DIR, filename)
        create_pdf_card(full_path, it['block_name'], it['id_code'], it['title'], it['concept'], it['prompt'], it['tips'], is_movil=True)
        movil_files[idx] = (full_path, filename)
        if idx % 15 == 0:
            print(f"   ✓ Generados {idx}/60 PDFs de [MOVIL]")

    # 2. Generar PDFs de MEMORIA
    print("\n⏳ Generando 60 Fichas de [MEM]...")
    for idx, it in enumerate(mem_items, 1):
        safe_t = sanitize_name(it['title'])
        filename = f"13. {it['id_code']}_{safe_t}.pdf"
        full_path = os.path.join(MEM_DIR, filename)
        create_pdf_card(full_path, it['block_name'], it['id_code'], it['title'], it['concept'], it['prompt'], it['tips'], is_movil=False)
        mem_files[idx] = (full_path, filename)
        if idx % 15 == 0:
            print(f"   ✓ Generados {idx}/60 PDFs de [MEM]")

    # 3. Copiar a cada una de las 60 carpetas de Sesión
    print("\n📂 Distribuyendo Fichas 12 y 13 en las 60 carpetas de Sesión...")
    all_session_folders = sorted([d for d in os.listdir(SESSIONS_DIR) if os.path.isdir(os.path.join(SESSIONS_DIR, d)) and not d.startswith('.')], key=lambda s: [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', s)])

    for s_folder in all_session_folders:
        m = re.match(r'^(\d+)_', s_folder)
        if not m:
            continue
        s_num = int(m.group(1))
        if s_num < 1 or s_num > 60:
            continue

        target_dir = os.path.join(SESSIONS_DIR, s_folder)

        # Copiar MOVIL
        if s_num in movil_files:
            src_m, fname_m = movil_files[s_num]
            dst_m = os.path.join(target_dir, fname_m)
            shutil.copy2(src_m, dst_m)

        # Copiar MEM
        if s_num in mem_files:
            src_mem, fname_mem = mem_files[s_num]
            dst_mem = os.path.join(target_dir, fname_mem)
            shutil.copy2(src_mem, dst_mem)

    print("   ✓ Las 60 carpetas de sesión han recibido su ficha 12.[MOVIL] y 13.[MEM]!")

    # 4. Re-generar los 5 Paneles CSV
    print("\n📊 Re-generando los 5 Paneles CSV para Google Classroom...")
    import generate_multiple_csvs
    generate_multiple_csvs.main()
    print("\n🎉 ¡PROCESO COMPLETADO AL 100%! Los 5 Paneles CSV ahora contienen los 13 pasos por sesión.")

if __name__ == "__main__":
    main()

