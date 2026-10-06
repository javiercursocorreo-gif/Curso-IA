# -*- coding: utf-8 -*-
"""
export_nat_pdfs.py
Genera las 60 Fichas Oficiales PDF de [NAT] (Naturaleza en Acción, Biomecánica y Fauna Fascinante)
con la metodología pedagógica en 3 pasos:
1. Paso 1: Prompt Corto y Natural (con Sujeto, Estilo, Soporte/Papel y Particiones).
2. Paso 2: Gemini redacta el Súper Prompt Maestro en inglés (con módulos y rigor enciclopédico).
3. Paso 3: El alumno ordena 'Genera la imagen con este prompt'.
4. Reto Práctico: Consulta biológica empoderada y desafío de autonomía para el alumno.

Guarda los PDFs en:
- EXPORTACION_FICHAS_CLASSROOM_PDF/07. [NAT] BLOQUE_7_NATURALEZA_EN_ACCION_FAUNA_Y_FLORA (Lotes 01_20, 21_40, 41_60)
- EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM (01_Sesion a 60_Sesion_Cierre)
- Y regenera los mapas interactivos MAPA_SESION_XX.html y MAPA_CLASE_SESION_XX.html.
"""

import os
import re
import shutil
import unicodedata
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

from build_nat_60_master import get_nat_items
import build_mapas_and_csvs_60_sessions as build_mapas

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT_BASE = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF")
SESSIONS_DIR = os.path.join(EXPORT_BASE, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
NAT_BLOCK_DIR = os.path.join(EXPORT_BASE, "07. [NAT] BLOQUE_7_NATURALEZA_EN_ACCION_FAUNA_Y_FLORA")

os.makedirs(NAT_BLOCK_DIR, exist_ok=True)
for sub in ["Lote_01_al_20", "Lote_21_al_40", "Lote_41_al_60"]:
    os.makedirs(os.path.join(NAT_BLOCK_DIR, sub), exist_ok=True)

def sanitize_filename(name):
    clean = re.sub(r'[/\\:*?"<>|]', '_', name)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:65]

def create_nat_pdf(file_path, item):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if os.path.exists(file_path):
        try: os.remove(file_path)
        except Exception: pass

    # Eliminar duplicados de conflicto si existieran
    conflict_path = f"{os.path.splitext(file_path)[0]} 2.pdf"
    if os.path.exists(conflict_path):
        try: os.remove(conflict_path)
        except Exception: pass

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        rightMargin=40, leftMargin=40, topMargin=36, bottomMargin=36
    )

    styles = getSampleStyleSheet()

    theme_green = colors.HexColor('#0B6623')
    accent_dark = colors.HexColor('#1E3A1E')
    bg_green = colors.HexColor('#F4F9F4')
    box_border = colors.HexColor('#2E7D32')

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9,
        textColor=theme_green, spaceAfter=2, alignment=1
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10.5,
        textColor=accent_dark, spaceAfter=6, alignment=1
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=13,
        leading=16, textColor=theme_green, spaceAfter=8
    )
    style_section_h = ParagraphStyle(
        'SectionH', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10.5,
        leading=13, textColor=theme_green, spaceBefore=6, spaceAfter=3
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9,
        leading=12.5, textColor=colors.HexColor('#222222'), spaceAfter=4
    )
    style_meta = ParagraphStyle(
        'MetaStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5,
        leading=11.5, textColor=colors.HexColor('#334433'), spaceAfter=2
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5,
        leading=11.5, textColor=colors.HexColor('#112211')
    )

    story = []

    # Cabecera
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE VIII: NATURALEZA EN ACCIÓN, BIOMECÁNICA Y SERES VIVOS [NAT]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=theme_green, spaceAfter=10))

    # Título
    story.append(Paragraph(f"<b>[{item['id']}] {item['title']}</b>", style_title))

    # Ficha Técnica y Metadatos Didácticos
    story.append(Paragraph("🌿 <b>Los 4 Ingredientes de la Lámina (Tu Receta Maestra):</b>", style_section_h))
    meta_table_data = [
        [Paragraph(f"• <b>Sujeto Biológico:</b> {item['subject']} ({item['category']})", style_meta)],
        [Paragraph(f"• <b>Estilo Artístico:</b> {item['style_art']}", style_meta)],
        [Paragraph(f"• <b>Soporte / Papel:</b> {item['paper']}", style_meta)],
        [Paragraph(f"• <b>Composición & Viñetas:</b> {item['layout']} ({item['details_es']})", style_meta)],
    ]
    meta_table = Table(meta_table_data, colWidths=[letter[0] - 80])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EBF4EB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#A3C9A8')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    # Metodología en 3 Pasos
    story.append(Paragraph("✍️ <b>El Método del Alumno en 3 Pasos (Sin Complicaciones):</b>", style_section_h))
    
    prompt_rows = [
        [Paragraph("<b>🟢 PASO 1: Copia y pega esta orden corta en tu chat de Gemini:</b>", style_prompt)],
        [Paragraph(f'<i>"{item["short_prompt"]}"</i>', style_prompt)],
        [Paragraph("<br/><b>⚙️ PASO 2: Gemini actuará como tu redactor científico y generará este Súper Prompt Maestro:</b>", style_prompt)],
        [Paragraph(f'<font color="#004d20"><b>{item["master_prompt_en"]}</b></font>', style_prompt)],
        [Paragraph("<br/><b>🎨 PASO 3: En el mismo chat, solo tienes que escribir:</b>", style_prompt)],
        [Paragraph('<b>"Perfecto. Ahora genera la imagen con ese prompt."</b> <i>(Y Gemini pintará tu lámina de museo con máxima nitidez y en español).</i>', style_prompt)]
    ]

    p_table = Table(prompt_rows, colWidths=[letter[0] - 80])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_green),
        ('BOX', (0,0), (-1,-1), 1, box_border),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 8))

    # Reto Práctico & Desafío de Autonomía
    story.append(Paragraph("💡 <b>El Reto Práctico / Consulta Científica Empoderada:</b>", style_section_h))
    story.append(Paragraph(f"• <b>Pregunta a tu IA:</b> {item['scientific_tip']}", style_body))
    story.append(Paragraph(f"• <b>🚀 Desafío de Autonomía:</b> {item['creative_challenge']}", style_body))

    doc.build(story)

def run_export():
    items = get_nat_items()
    print(f"🚀 Iniciando exportación de {len(items)} Fichas PDF oficiales de [NAT]...")

    # 1. Borrar PDFs antiguos de NAT en el bloque oficial y en las carpetas de sesión
    print("🧹 Limpiando versiones anteriores de NAT...")
    for root, dirs, files in os.walk(NAT_BLOCK_DIR):
        for f in files:
            if f.endswith(".pdf"):
                try: os.remove(os.path.join(root, f))
                except Exception: pass

    # Limpiar en las 60 carpetas de sesión
    for sess_idx in range(1, 61):
        sess_name = f"{sess_idx:02d}_Sesion" if sess_idx < 60 else "60_Sesion_Cierre"
        sess_path = os.path.join(SESSIONS_DIR, sess_name)
        if os.path.exists(sess_path):
            for f in os.listdir(sess_path):
                if ("NAT-" in f or "AVES-" in f) and f.endswith(".pdf"):
                    try: os.remove(os.path.join(sess_path, f))
                    except Exception: pass

    # 2. Generar los 60 PDFs en los lotes del Bloque 7 y copiarlos a las sesiones correspondientes
    for item in items:
        num = item["num"]
        code = item["id"]
        title_san = sanitize_filename(item["title"])
        pdf_filename = f"{code}_{title_san}.pdf"

        # Asignar lote en BLOQUE 7
        if num <= 20:
            lote_dir = os.path.join(NAT_BLOCK_DIR, "Lote_01_al_20")
        elif num <= 40:
            lote_dir = os.path.join(NAT_BLOCK_DIR, "Lote_21_al_40")
        else:
            lote_dir = os.path.join(NAT_BLOCK_DIR, "Lote_41_al_60")

        lote_pdf_path = os.path.join(lote_dir, pdf_filename)
        create_nat_pdf(lote_pdf_path, item)

        # Copiar a la carpeta de sesión con el prefijo "7. " (Paso 7/Fase 2)
        sess_name = f"{num:02d}_Sesion" if num < 60 else "60_Sesion_Cierre"
        sess_path = os.path.join(SESSIONS_DIR, sess_name)
        os.makedirs(sess_path, exist_ok=True)
        session_pdf_name = f"7. {code}_{title_san}.pdf"
        session_pdf_path = os.path.join(sess_path, session_pdf_name)

        shutil.copy2(lote_pdf_path, session_pdf_path)

    print("✅ Generadas con éxito las 60 fichas PDF en el Bloque 7 y en las 60 sesiones.")

    # 3. Regenerar Mapas de Sesión y CSVs
    print("🗺️ Regenerando los 60 Mapas de Sesión (MAPA_SESION_XX.html) y Paneles CSV...")
    build_mapas.process_all_sessions()
    print("🎉 ¡TODO EL BLOQUE DE NATURALEZA HA SIDO ACTUALIZADO Y SINCRONIZADO AL 100%!")

if __name__ == "__main__":
    run_export()

