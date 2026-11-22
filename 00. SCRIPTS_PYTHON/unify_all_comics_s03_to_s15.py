#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unify_all_comics_s03_to_s15.py
Unifica los proyectos de cómic de las Sesiones 03 a 15 de 4 archivos/ítems separados
(Paso 0, Paso 1, Paso 2, Paso 3) en 1 ÚNICO ÍTEM didáctico completo:
- Ficha PDF unificada: 11.CUENT-0XX_Proyecto_Comic_Ilustrado.pdf (2 páginas completas, maquetación profesional).
- Tarjeta única en los mapas interactivos (MAPA_SESION_XX.html y MAPA_CLASE_SESION_XX.html).
- Renumeración correlativa limpia de todas las tarjetas del mapa (#01, #02, #03...).
- Purga de los 4 PDFs fragmentados antiguos en carpetas de sesión y Bloque 11.
"""

import os
import sys
import re
import shutil
import pypdf

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SESSIONS_BASE = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
B11_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/11. [CUENT] BLOQUE_11_CUENTOS_PARA_NIETOS/Lote_01_al_20")

def sanitize_text(text):
    if not text:
        return ""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return text

def build_unified_comic_pdf(output_path, session_num, cuent_id, title, story_prompt, style_preset):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=36,
        bottomMargin=36
    )
    styles = getSampleStyleSheet()

    # Custom styles
    style_header_tag = ParagraphStyle('HeaderTag', fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=colors.HexColor('#BE185D'))
    style_title = ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=14, leading=17, textColor=colors.HexColor('#831843'), spaceAfter=8)
    style_sec_title = ParagraphStyle('SecTitle', fontName='Helvetica-Bold', fontSize=10.5, leading=13, textColor=colors.HexColor('#9D174D'), spaceAfter=5)
    style_body = ParagraphStyle('DocBody', fontName='Helvetica', fontSize=9, leading=12.5, textColor=colors.HexColor('#1E293B'))
    style_body_bold = ParagraphStyle('DocBodyBold', fontName='Helvetica-Bold', fontSize=9, leading=12.5, textColor=colors.HexColor('#0F172A'))
    style_prompt = ParagraphStyle('PromptBox', fontName='Helvetica-Oblique', fontSize=8.5, leading=12, textColor=colors.HexColor('#312E81'))
    style_callout = ParagraphStyle('Callout', fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=colors.HexColor('#475569'))
    style_footer = ParagraphStyle('DocFooter', fontName='Helvetica', fontSize=7.5, leading=10, textColor=colors.HexColor('#64748B'))

    story = []

    # ================= PAGE 1 =================
    # Cabecera institucional
    story.append(Paragraph(f"SESIÓN {session_num:02d} • PROYECTO CÓMIC &amp; NARRATIVA ILUSTRADA CON IA [{cuent_id}]", style_header_tag))
    story.append(Paragraph(f"Proyecto Cómic Ilustrado: {sanitize_text(title)}", style_title))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#E11D48'), spaceAfter=8))

    # Caja Estrategia Didáctica de Aula
    aula_intro = (
        "<b>ESTRATEGIA DIDÁCTICA DE AULA (LANZAMIENTO TEMPRANO EN SEGUNDO PLANO):</b><br/>"
        "La generación visual completa de 10 diapositivas en <b>Gemini Notebook</b> tarda unos minutos en renderizarse. "
        "Por eso, <b>iniciamos el cómic al arrancar la sesión</b>, realizamos los Pasos 1 y 2 en el chat de Gemini y lanzamos la presentación en NotebookLM. "
        "La dejamos procesando en segundo plano mientras hacemos el resto de actividades de la clase y, al finalizar, volvemos a Gemini Notebook para proyectar y disfrutar el cómic terminado a pantalla completa."
    )
    t_aula = Table([[Paragraph(aula_intro, style_callout)]], colWidths=[532])
    t_aula.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FDF2F8')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F472B6')),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_aula)
    story.append(Spacer(1, 8))

    # PASO 1: CREAR LA HISTORIA
    story.append(Paragraph("PASO 1: CREAR LA HISTORIA (EN GEMINI CHAT O CUADERNO CUENTOS)", style_sec_title))
    p1_desc = (
        "Abre Gemini e indica la edad de tu nieto o destinatario para calibrar la narrativa:<br/>"
        "• <b>Si el nieto es menor de 6 años:</b> Tono dulce, sensorial, mágico y con final tranquilo reconfortante para dormir.<br/>"
        "• <b>Si el nieto es mayor de 6 años:</b> Añade aventura, misterio, dilemas éticos y afán de superación sin infantilismo.<br/>"
        "<i>(Nota: Usa nombres de personajes originales sin marcas comerciales para evitar restricciones de derechos).</i>"
    )
    story.append(Paragraph(p1_desc, style_body))
    story.append(Spacer(1, 4))

    # Prompt Paso 1
    clean_story_prompt = sanitize_text(story_prompt.strip())
    p1_prompt_box = f"<b>PROMPT MAESTRO - PASO 1 (Copiar y pegar en Gemini):</b><br/>\"{clean_story_prompt}\""
    t_p1 = Table([[Paragraph(p1_prompt_box, style_prompt)]], colWidths=[532])
    t_p1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EEF2FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#A5B4FC')),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_p1)
    story.append(Spacer(1, 8))

    # PASO 2: GENERADOR DE GUIÓN SECUENCIAL
    story.append(Paragraph("PASO 2: GENERAR EL GUIÓN SECUENCIAL DE 10 VIÑETAS", style_sec_title))
    p2_desc = (
        "En la misma conversación de Gemini donde se acaba de generar la historia, pega el siguiente prompt. "
        "Gemini actuará como director audiovisual y estructurará el guion exacto de 10 viñetas completas:"
    )
    story.append(Paragraph(p2_desc, style_body))
    story.append(Spacer(1, 4))

    p2_prompt_text = (
        "<b>PROMPT MAESTRO - PASO 2 (Copiar en la misma conversación):</b><br/>"
        "\"Toma el cuento que acabamos de generar y transfórmalo en el guion de un cómic secuencial de EXACTAMENTE 10 PÁGINAS ([PÁGINA 1] a [PÁGINA 10]). "
        "Para cada viñeta incluye SIEMPRE: 1) Tipo de toma y ángulo de cámara; 2) Descripción visual detallada (mantén apariencia física, vestuario y colores de personajes 100% estables y consistentes); "
        "3) Iluminación y atmósfera de época; 4) Textos de Diálogo y Pensamiento obligatorios. Genera el guion de 10 páginas ahora.\""
    )
    t_p2 = Table([[Paragraph(p2_prompt_text, style_prompt)]], colWidths=[532])
    t_p2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#86EFAC')),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_p2)

    # Pie de página 1
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#CBD5E1'), spaceAfter=4))
    story.append(Paragraph(f"CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESIÓN {session_num:02d} • PÁGINA 1 DE 2", style_footer))

    # Salto de página para la Página 2
    story.append(Spacer(1, 20))

    # ================= PAGE 2 =================
    story.append(Paragraph(f"SESIÓN {session_num:02d} • PROYECTO CÓMIC &amp; NARRATIVA ILUSTRADA CON IA [{cuent_id}]", style_header_tag))
    story.append(Paragraph("PASO 3: ILUSTRACIÓN Y PRESENTACIÓN EN GEMINI NOTEBOOK", style_sec_title))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#E11D48'), spaceAfter=8))

    p3_desc = (
        "1. Abre <b>Gemini Notebook</b> (NotebookLM) con tu cuenta e ingresa en tu cuaderno <b>CUENTOS</b>. "
        "La conversación de Gemini donde creaste la historia y el guion ya aparece automáticamente conectada como fuente.<br/>"
        "2. Pulsa en la barra lateral el botón <b>\"Presentación\"</b> (o diapositivas de Studio).<br/>"
        "3. En el cuadro de petición visual, pega el siguiente prompt con el estilo visual asignado a esta sesión:"
    )
    story.append(Paragraph(p3_desc, style_body))
    story.append(Spacer(1, 6))

    clean_preset = sanitize_text(style_preset.strip())
    p3_prompt_text = (
        "<b>PROMPT MAESTRO - PASO 3 (Pegar en el botón Presentación de Gemini Notebook):</b><br/>"
        "\"Aplica estrictamente los siguientes parámetros visuales y estéticos para generar la presentación visual de este cómic, basándote en el guion adjunto en la fuente.<br/>"
        "No resumas ni recortes la historia. Genera las 10 páginas manteniendo este estilo visual de forma estricta:<br/><br/>"
        f"<b>{clean_preset}</b><br/><br/>"
        "• <b>INSTRUCCIÓN CRÍTICA 1 (CONTENIDO):</b> NO generes diapositivas de análisis, ni curvas de color, ni explicación de personajes. Limítate a generar ÚNICAMENTE las páginas narrativas del cómic.<br/>"
        "• <b>INSTRUCCIÓN CRÍTICA 2 (DISEÑO Y MAQUETACIÓN):</b> Cada página generada debe ocupar el 100% del lienzo (canvas). NO dejes mitades de la pantalla en blanco ni columnas vacías. Las viñetas deben llenar todo el ancho.<br/>"
        "• <b>INSTRUCCIÓN CRÍTICA 3 (CONSISTENCIA DE PERSONAJES):</b> Mantén la apariencia, vestimenta, colores y rasgos de todos los personajes idénticos y consistentes de la viñeta 1 a la 10.<br/><br/>"
        "Genera la presentación del cómic ahora.\""
    )
    t_p3 = Table([[Paragraph(p3_prompt_text, style_prompt)]], colWidths=[532])
    t_p3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#FCD34D')),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_p3)
    story.append(Spacer(1, 10))

    # Caja de Consejos y Proyección
    cierre_text = (
        "<b>🎉 CÓMO DISFRUTAR Y COMPARTIR TU CÓMIC AL FINALIZAR LA CLASE:</b><br/>"
        "• <b>Proyección a pantalla completa:</b> Haz clic en la presentación dentro de Gemini Notebook y pulsa el icono de pantalla completa para pasar las viñetas como un cómic digital interactivo.<br/>"
        "• <b>Descargar y guardar:</b> Puedes exportar la presentación como archivo PDF o compartir el enlace con tus hijos y nietos para que lo lean en su móvil o tablet.<br/>"
        "• <b>Opción Cuento Propio:</b> Si tienes una anécdota familiar real, puedes usar este mismo método sustituyendo la historia del Paso 1 por tu propio relato escrito."
    )
    t_cierre = Table([[Paragraph(cierre_text, style_callout)]], colWidths=[532])
    t_cierre.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_cierre)

    # Pie de página 2
    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#CBD5E1'), spaceAfter=4))
    story.append(Paragraph(f"CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESIÓN {session_num:02d} • GUÍA MAESTRA UNIFICADA DEL CÓMIC [CUENT-{session_num:03d}]", style_footer))

    doc.build(story)
    return output_path

def renumber_map_html(content):
    """
    Renumera correlativamente todas las tarjetas en el HTML:
    Busca <span class="file-num">#(\d+)([A-Z]?)(\s*\[[^\]]+\])?</span>
    Si tiene sufijo 'B' (ej: #01B [INFO]), mantiene la letra o ajusta.
    Para tarjetas estándar: #01, #02, #03...
    """
    card_counter = 1
    
    def replace_num(match):
        nonlocal card_counter
        full_num = match.group(1) # ej: 01, 01B, 03
        tag_part = match.group(2) or "" # ej:  [INFO],  [COMIC]
        
        # Si es #01B, lo mantenemos como #01B sin incrementar el contador principal
        if "B" in full_num:
            return f'<span class="file-num">#{full_num}{tag_part}</span>'
        
        formatted = f"{card_counter:02d}"
        card_counter += 1
        return f'<span class="file-num">#{formatted}{tag_part}</span>'
        
    pattern = r'<span class="file-num">#(\d+[A-Z]?)(\s*\[[^\]]+\])?</span>'
    new_content = re.sub(pattern, replace_num, content)
    
    # Actualizar contador de recursos en la cabecera si existe
    # ej: <span class="branch-count">10 recursos</span> -> calcular total de tarjetas
    # Encontramos los bloques de columna
    return new_content

def process_session(s):
    s_dir = os.path.join(SESSIONS_BASE, f"{s:02d}_Sesion")
    if not os.path.exists(s_dir):
        print(f"❌ No existe carpeta: {s_dir}")
        return

    # Buscar archivos CUENT antiguos
    files = os.listdir(s_dir)
    f_p1 = [os.path.join(s_dir, f) for f in files if "Paso_1" in f]
    f_p3 = [os.path.join(s_dir, f) for f in files if "Paso_3" in f]
    
    if not f_p1 or not f_p3:
        print(f"⚠️ Sesión {s:02d}: No se encontraron archivos Paso_1 y Paso_3")
        return

    # Extraer texto de Paso 1 y Paso 3
    r1 = pypdf.PdfReader(f_p1[0])
    r3 = pypdf.PdfReader(f_p3[0])
    t1 = r1.pages[0].extract_text()
    t3 = r3.pages[0].extract_text()

    # Extraer título limpio
    raw_title = os.path.basename(f_p1[0]).split("Paso_1_")[-1].replace(".pdf", "").strip()
    title_clean = raw_title.replace("_", ": ")

    # Extraer prompt de la historia de t1
    story_prompt = ""
    if "Actúa como" in t1:
        story_prompt = "Actúa como" + t1.split("Actúa como", 1)[1]
        # Cortar en advertencias o pies
        if "■" in story_prompt:
            story_prompt = story_prompt.split("■")[0]
        if "INSTRUCCIONES" in story_prompt:
            story_prompt = story_prompt.split("INSTRUCCIONES")[0]
    else:
        # Extraer líneas después de INSTRUCCIÓN PEDAGÓGICA
        lines = t1.split("\n")
        prompt_lines = []
        capture = False
        for l in lines:
            if "REGLA DE ORIGINALIDAD" in l or "prompt:" in l.lower():
                capture = True
                continue
            if capture:
                prompt_lines.append(l)
        story_prompt = " ".join(prompt_lines).strip()
        if not story_prompt:
            story_prompt = t1.strip()

    # Extraer preset de estilo de t3
    style_preset = ""
    if "PRESET" in t3:
        p_part = "PRESET" + t3.split("PRESET", 1)[1]
        if "INSTRUCCIÓN CRÍTICA" in p_part:
            style_preset = p_part.split("INSTRUCCIÓN CRÍTICA")[0].strip()
        else:
            style_preset = p_part[:250].strip()
    else:
        style_preset = "PRESET OFICIAL: ILUSTRACIÓN NARRATIVA DE ALTA CALIDAD (Viñetas de gran detalle, composición equilibrada y coherencia cromática)"

    cuent_id = f"CUENT-{s:03d}"
    unified_pdf_name = f"11.{cuent_id}_Proyecto_Comic_Ilustrado.pdf"
    unified_pdf_path = os.path.join(s_dir, unified_pdf_name)

    # 1. Generar el PDF unificado en s_dir
    build_unified_comic_pdf(unified_pdf_path, s, cuent_id, title_clean, story_prompt, style_preset)
    print(f"✅ [S{s:02d}] Ficha unificada generada: {unified_pdf_name}")

    # 2. Copiar al Bloque 11
    b11_path = os.path.join(B11_DIR, unified_pdf_name)
    shutil.copy2(unified_pdf_path, b11_path)
    print(f"  📦 Copiada a Bloque 11: {unified_pdf_name}")

    # 3. Eliminar los 4 archivos viejos en s_dir y Bloque 11
    old_files_s = [f for f in files if re.search(r'CUENT.*Paso_[0-3]', f)]
    for old_f in old_files_s:
        try:
            os.remove(os.path.join(s_dir, old_f))
        except Exception:
            pass

    if os.path.exists(B11_DIR):
        old_files_b = [f for f in os.listdir(B11_DIR) if f"CUENT-{s:03d}" in f and "Paso_" in f]
        for old_f in old_files_b:
            try:
                os.remove(os.path.join(B11_DIR, old_f))
            except Exception:
                pass

    print(f"  🗑️ Eliminados {len(old_files_s)} archivos antiguos fragmentados en S{s:02d}")

    # 4. Actualizar MAPA_SESION_{s:02d}.html y MAPA_CLASE_SESION_{s:02d}.html
    new_card_html = f'''                    <a href="{unified_pdf_name}" target="_blank" class="file-card file-card-special" style="background: rgba(225, 29, 72, 0.08); border-color: rgba(225, 29, 72, 0.35);">
                        <div class="file-card-special-top">
                            <div class="file-left">
                                <span class="file-num">#XX [COMIC]</span>
                                <span class="file-tag tag-pdf" style="background:#e11d48; color:#fff;">PROYECTO CÓMIC</span>
                                <div class="file-details">
                                    <span class="file-title">Proyecto Cómic: {sanitize_text(title_clean)}</span>
                                    <span class="file-desc">Guía Completa en 3 Pasos • Creación de Historia, Guión de 10 Viñetas e Ilustración en Gemini Notebook</span>
                                </div>
                            </div>
                            <span class="file-arrow">↗</span>
                        </div>
                    </a>'''

    map_names = [f"MAPA_SESION_{s:02d}.html", f"MAPA_CLASE_SESION_{s:02d}.html"]
    for m_name in map_names:
        m_path = os.path.join(s_dir, m_name)
        if not os.path.exists(m_path):
            continue

        with open(m_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Reemplazar el bloque de las 4 tarjetas CUENT por la nueva tarjeta única
        # Patrón que busca desde la primera tarjeta con CUENT.*Paso_0 hasta el cierre de la tarjeta Paso_3
        cuent_block_pattern = r'<a\s+href="[^"]*CUENT[^"]*Paso_0[^"]*"[^>]*>.*?</a>\s*<a\s+href="[^"]*CUENT[^"]*Paso_1[^"]*"[^>]*>.*?</a>\s*<a\s+href="[^"]*CUENT[^"]*Paso_2[^"]*"[^>]*>.*?</a>\s*<a\s+href="[^"]*CUENT[^"]*Paso_3[^"]*"[^>]*>.*?</a>'
        
        match = re.search(cuent_block_pattern, content, re.DOTALL)
        if match:
            content = content[:match.start()] + new_card_html + content[match.end():]
            print(f"  🎯 Sustituido bloque de 4 tarjetas por 1 en {m_name}")
        else:
            # Búsqueda más flexible si no coinciden exactamente los saltos
            pattern_flexible = r'<a\s+href="[^"]*CUENT[^"]*Paso_0[^"]*"[^>]*>.*?</a>.*?<a\s+href="[^"]*CUENT[^"]*Paso_3[^"]*"[^>]*>.*?</a>'
            match_flex = re.search(pattern_flexible, content, re.DOTALL)
            if match_flex:
                content = content[:match_flex.start()] + new_card_html + content[match_flex.end():]
                print(f"  🎯 Sustituido bloque flexible de tarjetas por 1 en {m_name}")
            else:
                print(f"  ⚠️ No se encontró patrón de 4 tarjetas en {m_name}")

        # Renumerar todas las tarjetas correlativamente
        renumbered_content = renumber_map_html(content)
        
        # Guardar mapa actualizado
        with open(m_path, "w", encoding="utf-8") as f:
            f.write(renumbered_content)
        print(f"  🔢 {m_name} renumerado correlativamente y guardado.")

def main():
    print("==================================================================")
    print("=== [UNIFICACIÓN DE CÓMICS A 1 SOLO ÍTEM EN SESIONES 03 A 15] ===")
    print("==================================================================")
    
    for s in range(3, 16):
        print(f"\n--- PROCESANDO SESIÓN {s:02d} ---")
        process_session(s)
        
    print("\n🎉 ¡TODAS LAS SESIONES 03 A 15 HAN SIDO UNIFICADAS A 1 SOLO ÍTEM CON ÉXITO!")

if __name__ == "__main__":
    main()
