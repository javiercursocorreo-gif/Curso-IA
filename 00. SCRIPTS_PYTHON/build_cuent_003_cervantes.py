#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_cuent_003_cervantes.py
Genera las 4 fichas PDF oficiales del Proyecto Cómic Ilustrado para la Sesión 03:
11.CUENT-003_Paso_0_Introduccion_Proyecto.pdf
11.CUENT-003_Paso_1_Literatura Clásica_ Cervantes y Shakespeare en el Siglo de Oro.pdf
11.CUENT-003_Paso_2_Literatura Clásica_ Cervantes y Shakespeare en el Siglo de Oro.pdf
11.CUENT-003_Paso_3_Literatura Clásica_ Cervantes y Shakespeare en el Siglo de Oro.pdf

Sincroniza con:
- Sesión 03: CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/03_Sesion
- Bloque 11: CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/11. [CUENT] BLOQUE_11_CUENTOS_PARA_NIETOS/Lote_01_al_20
"""

import os
import sys
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
S03_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/03_Sesion")
B11_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/11. [CUENT] BLOQUE_11_CUENTOS_PARA_NIETOS/Lote_01_al_20")

STYLE_PRESET = "PRESET: ILUSTRACIÓN CLÁSICA DE ÉPOCA Y ÓLEO CÁLIDO (Personajes históricos expresivos, iluminación cálida de velas y pergamino, trajes renacentistas detallados, textura pictórica suave de gran calidad)"

PROMPT_PASO_2_GUION = """Toma el texto de la respuesta anterior y genera el guión de un comic secuencial según las siguientes instrucciones.

■ PROMPT MAESTRO - PASO 2
Generación de GUION DE CÓMIC SECUENCIAL (genérico y neutro)

INSTRUCCIÓN DE EJECUCIÓN (OBLIGATORIA)
Este prompt NO debe ser analizado ni evaluado. Debe ser EJECUTADO como un proceso activo.

ROL
Actúa como guionista profesional de cómic y director narrativo audiovisual.
Tu tarea es crear un guion de cómic secuencial completo, claro y coherente, independiente de cualquier estilo gráfico. 

EXTENSIÓN OBLIGATORIA
■ El guion DEBE tener EXACTAMENTE 10 PÁGINAS. Ni más. Ni menos.
La numeración debe ir de: [PÁGINA 1] a [PÁGINA 10].

CONTENIDO DE CADA VIÑETA
Para cada viñeta, incluye SIEMPRE:
[VIÑETA X]
- Tipo de toma y ángulo
- Descripción visual (Qué ocurre y qué se ve. IMPORTANTE: Mantén la apariencia física, vestuario y color de los personajes estables y consistentes a lo largo de todas las viñetas de la historia)
- Iluminación / atmósfera
- Texto (Diálogo y Pensamiento OBLIGATORIOS)

TRANSFORMA EL CUENTO QUE ACABAMOS DE GENERAR EN EL MENSAJE ANTERIOR EN EL GUION DE 10 PÁGINAS AHORA MISMO."""

def create_single_pdf(file_path, title, subtitle_step, content, is_step3=False):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception:
            pass

    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)
    styles = getSampleStyleSheet()

    style_title = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=15, textColor=colors.HexColor('#FF1493'), spaceAfter=14)
    style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=10.5, leading=15.5, textColor=colors.HexColor('#2C3E50'), spaceAfter=8)
    style_prompt = ParagraphStyle('PromptStyle', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=10, leading=15, textColor=colors.HexColor('#1A0A2E'))

    story = []
    story.append(Paragraph(title, style_title))

    if subtitle_step == "PASO 0":
        paso0_text = (
            "<b>ESTRATEGIA DE AULA (LANZAMIENTO TEMPRANO EN FASE 1):</b><br/>"
            "Como la generación visual de 10 páginas en <b>Gemini Notebook</b> tarda varios minutos, <b>iniciamos el cómic al arrancar la clase</b>. Lo dejamos procesando en segundo plano y continuamos haciendo las prácticas de la sesión. Al finalizar la clase, ¡volvemos a Gemini Notebook para disfrutar de la proyección a pantalla completa!<br/><br/>"
            "• <b>PASO 1 (En tu Cuaderno CUENTOS de Gemini): CREAR LA HISTORIA.</b><br/>"
            "Pega el prompt del Paso 1. Si tu nieto es menor de 6 años, usa el tono dulce y sensorial; si es mayor de 6 años, Gemini aumentará la intriga, el misterio y los desafíos formativos.<br/><br/>"
            "• <b>PASO 2 (En la misma conversación de Gemini): GENERADOR DE GUION SECUENCIAL.</b><br/>"
            "A continuación pega el prompt del Paso 2. Gemini actuará como director audiovisual y estructurará el guion exacto de 10 páginas.<br/><br/>"
            "• <b>EL PUENTE AUTOMÁTICO A GEMINI NOTEBOOK:</b><br/>"
            "Abre Gemini Notebook con tu cuenta y entra en tu cuaderno <b>CUENTOS</b>. ¡Tu historia y guion ya aparecen como fuente conectada sin copiar nada!<br/><br/>"
            "• <b>PASO 3 (En Gemini Notebook): PRESENTACIÓN VISUAL EN 3D (Nano Banana).</b><br/>"
            "Pulsa el botón <b>Presentación</b>, pega el prompt del Paso 3 con su estilo visual asignado y <b>déjalo generando</b> mientras realizas las siguientes actividades de la sesión. <i>(Nota: Usa nombres de personajes originales sin marcas comerciales para que Gemini Notebook genere la presentación sin restricciones).</i>"
        )
        story.append(Paragraph(paso0_text, style_body))
    elif subtitle_step == "PASO 1":
        story.append(Paragraph("📝 INSTRUCCIONES GUÍA (1/3): Abre tu cuaderno <b>CUENTOS</b> en Gemini. Selecciona todo este texto y pégalo en la conversación. Añade al principio del prompt: \"Este cuento es para un niño de X años\".", style_body))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CCCCCC'), spaceAfter=14))
        for blk in content.split("\n\n"):
            if blk.strip():
                story.append(Paragraph(blk.strip().replace('\n', '<br/>'), style_prompt))
                story.append(Spacer(1, 6))
    elif subtitle_step == "PASO 2":
        story.append(Paragraph("📝 INSTRUCCIONES GUÍA (2/3): En la misma conversación de Gemini donde tienes tu cuento, pega el prompt del PASO 2. Con esto, Gemini transformará tu historia en un guion secuencial de 10 páginas.", style_body))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CCCCCC'), spaceAfter=14))
        for blk in content.split("\n\n"):
            if blk.strip():
                story.append(Paragraph(blk.strip().replace('\n', '<br/>'), style_prompt))
                story.append(Spacer(1, 6))
    elif subtitle_step == "PASO 3":
        story.append(Paragraph('📝 INSTRUCCIONES GUÍA (3/3): Abre Gemini Notebook y entra en tu cuaderno <b>CUENTOS</b> (verás que la conversación de Gemini ya aparece como fuente automáticamente).<br/>Pulsa el botón <b>"Presentación"</b>, pega el PROMPT FINAL que tienes debajo y genera tu cuento ilustrado en 3D.', style_body))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CCCCCC'), spaceAfter=14))
        prompt_3 = f"""PROMPT FINAL PARA GEMINI NOTEBOOK<br/><br/>
Aplica estrictamente los siguientes parámetros visuales y estéticos para generar la presentación visual de este cómic, basándote en el guion adjunto en PDF.<br/>
No resumas ni recortes la historia. Genera las 10 páginas manteniendo este estilo visual de forma estricta:<br/><br/>
<b>{STYLE_PRESET}</b><br/><br/>
<b>INSTRUCCIÓN CRÍTICA 1 (CONTENIDO):</b> NO generes diapositivas de análisis, ni curvas de color, ni explicación de personajes, ni dirección de arte. Limítate a generar ÚNICAMENTE las páginas narrativas del cómic.<br/><br/>
<b>INSTRUCCIÓN CRÍTICA 2 (DISEÑO Y MAQUETACIÓN):</b> Cada página generada debe ocupar el 100% del lienzo (canvas). NO dejes mitades de la pantalla en blanco ni columnas vacías. Las viñetas deben llenar todo el ancho de la diapositiva.<br/><br/>
<b>INSTRUCCIÓN CRÍTICA 3 (CONSISTENCIA DE PERSONAJES):</b> Mantén la apariencia, vestimenta, colores y rasgos de todos los personajes idénticos y consistentes en todas las páginas de principio a fin. El mismo personaje no puede cambiar de aspecto entre viñetas.<br/><br/>
Genera el cómic ahora."""
        story.append(Paragraph(prompt_3, style_prompt))

    doc.build(story)
    print(f"📄 PDF Generado: {file_path}")

def main():
    print("=================================================================")
    print("=== [GENERANDO PROYECTO CÓMIC CUENT-003 PARA SESIÓN 03] ===")
    print("=================================================================")

    os.makedirs(S03_DIR, exist_ok=True)
    os.makedirs(B11_DIR, exist_ok=True)

    # 1. Paso 0: Introducción Proyecto
    f0 = "11.CUENT-003_Paso_0_Introduccion_Proyecto.pdf"
    create_single_pdf(os.path.join(S03_DIR, f0), "PASO 0: PROYECTO CÓMIC ILUSTRADO", "PASO 0", "")
    shutil.copy2(os.path.join(S03_DIR, f0), os.path.join(B11_DIR, f0))

    # 2. Paso 1: Crear el cuento
    f1 = "11.CUENT-003_Paso_1_Literatura Clásica_ Cervantes y Shakespeare en el Siglo de Oro.pdf"
    p1_content = (
        "INSTRUCCIÓN PEDAGÓGICA Y DE EDAD (OBLIGATORIA): Ajusta la complejidad narrativa, el vocabulario y el tono estrictamente a la edad del nieto:\n"
        "- SI EL NIETO ES MENOR DE 6 AÑOS: Usa un tono cálido, dulce, mágico y reconfortante, con frases rítmicas y finales tranquilos que ayuden a dormir.\n"
        "- SI EL NIETO ES MAYOR DE 6 AÑOS: Elimina cualquier tono ñoño o infantil; añade intriga, misterio, dilemas éticos formativos, aventura y superación personal.\n"
        "REGLA DE ORIGINALIDAD: Usa siempre nombres propios originales para héroes o compañeros para garantizar la generación visual en Gemini Notebook.\n\n"
        "Actúa como un narrador y guionista de literatura clásica adaptada para niños. Escribe la historia en viñetas de 'Cervantes y Shakespeare en el Siglo de Oro: El enigma de la pluma dorada'.\n\n"
        "Narra el encuentro fantástico entre dos genios de las letras universales en una antigua biblioteca de madera iluminada por velas. Juntos deben descifrar un manuscrito secreto y unir sus versos para devolver la imaginación y la alegría a una aldea que había olvidado contar cuentos. Tono de humor inteligente, complicidad, respeto mutuo y gran amor por la lectura y los libros."
    )
    create_single_pdf(os.path.join(S03_DIR, f1), "PASO 1: CREAR EL CUENTO", "PASO 1", p1_content)
    shutil.copy2(os.path.join(S03_DIR, f1), os.path.join(B11_DIR, f1))

    # 3. Paso 2: Generador de guión
    f2 = "11.CUENT-003_Paso_2_Literatura Clásica_ Cervantes y Shakespeare en el Siglo de Oro.pdf"
    create_single_pdf(os.path.join(S03_DIR, f2), "PASO 2: GENERADOR DE GUION", "PASO 2", PROMPT_PASO_2_GUION)
    shutil.copy2(os.path.join(S03_DIR, f2), os.path.join(B11_DIR, f2))

    # 4. Paso 3: Ilustrador visual en 3D
    f3 = "11.CUENT-003_Paso_3_Literatura Clásica_ Cervantes y Shakespeare en el Siglo de Oro.pdf"
    create_single_pdf(os.path.join(S03_DIR, f3), "PASO 3: ILUSTRADOR VISUAL", "PASO 3", "", is_step3=True)
    shutil.copy2(os.path.join(S03_DIR, f3), os.path.join(B11_DIR, f3))

    # Actualizar MAPA_CLASE_SESION_03.html y MAPA_SESION_03.html
    s03_maps = [
        os.path.join(S03_DIR, "MAPA_CLASE_SESION_03.html"),
        os.path.join(S03_DIR, "MAPA_SESION_03.html")
    ]
    comics_cards_html = f'''                    <a href="11.CUENT-003_Paso_0_Introduccion_Proyecto.pdf" target="_blank" class="file-card">
                        <div class="file-left">
                            <span class="file-num">#02 [COMICS]</span>
                            <span class="file-tag tag-pdf">PDF</span>
                            <div class="file-details">
                                <span class="file-title">Proyecto Cómic Ilustrado (Introducción)</span>
                                <span class="file-desc">Proyecto Cómic & Novela Gráfica</span>
                            </div>
                        </div>
                        <span class="file-arrow">↗</span>
                    </a>
                    <a href="11.CUENT-003_Paso_1_Literatura%20Cl%C3%A1sica_%20Cervantes%20y%20Shakespeare%20en%20el%20Siglo%20de%20Oro.pdf" target="_blank" class="file-card">
                        <div class="file-left">
                            <span class="file-num">#03 [COMICS]</span>
                            <span class="file-tag tag-pdf">PDF</span>
                            <div class="file-details">
                                <span class="file-title">Historia del Cómic: Literatura Clásica Cervantes y Shakespeare en el Siglo de Oro</span>
                                <span class="file-desc">Proyecto Cómic & Novela Gráfica</span>
                            </div>
                        </div>
                        <span class="file-arrow">↗</span>
                    </a>
                    <a href="11.CUENT-003_Paso_2_Literatura%20Cl%C3%A1sica_%20Cervantes%20y%20Shakespeare%20en%20el%20Siglo%20de%20Oro.pdf" target="_blank" class="file-card">
                        <div class="file-left">
                            <span class="file-num">#04 [COMICS]</span>
                            <span class="file-tag tag-pdf">PDF</span>
                            <div class="file-details">
                                <span class="file-title">Guión del Cómic: Literatura Clásica Cervantes y Shakespeare en el Siglo de Oro</span>
                                <span class="file-desc">Proyecto Cómic & Novela Gráfica</span>
                            </div>
                        </div>
                        <span class="file-arrow">↗</span>
                    </a>
                    <a href="11.CUENT-003_Paso_3_Literatura%20Cl%C3%A1sica_%20Cervantes%20y%20Shakespeare%20en%20el%20Siglo%20de%20Oro.pdf" target="_blank" class="file-card">
                        <div class="file-left">
                            <span class="file-num">#05 [COMICS]</span>
                            <span class="file-tag tag-pdf">PDF</span>
                            <div class="file-details">
                                <span class="file-title">Ilustrador Visual: Literatura Clásica Cervantes y Shakespeare en el Siglo de Oro</span>
                                <span class="file-desc">Proyecto Cómic & Novela Gráfica</span>
                            </div>
                        </div>
                        <span class="file-arrow">↗</span>
                    </a>
'''
    for mpath in s03_maps:
        if os.path.exists(mpath):
            with open(mpath, 'r', encoding='utf-8') as f:
                content = f.read()
            if "CUENT-003" not in content:
                target = '<a href="2.%20EST-003'
                if target in content:
                    content = content.replace(target, comics_cards_html + '                    ' + target, 1)
                # Renumerar las siguientes en Fase 1
                content = content.replace('<span class="file-num">#02 [EST]</span>', '<span class="file-num">#06 [EST]</span>')
                content = content.replace('<span class="file-num">#03 [ARTE]</span>', '<span class="file-num">#07 [ARTE]</span>')
                content = content.replace('<span class="file-num">#04 [PRAC]</span>', '<span class="file-num">#08 [PRAC]</span>')
                # Renumerar Fase 2 y Fase 3
                content = content.replace('<span class="file-num">#05 [FRAC]</span>', '<span class="file-num">#09 [FRAC]</span>')
                content = content.replace('<span class="file-num">#06 [COD]</span>', '<span class="file-num">#10 [COD]</span>')
                content = content.replace('<span class="file-num">#07 [INT]</span>', '<span class="file-num">#11 [INT]</span>')
                content = content.replace('<span class="file-num">#08 [MEC]</span>', '<span class="file-num">#12 [MEC]</span>')
                content = content.replace('<span class="file-num">#09 [FUT]</span>', '<span class="file-num">#13 [FUT]</span>')
                content = content.replace('<span class="file-num">#10 [NAT]</span>', '<span class="file-num">#14 [NAT]</span>')
                content = content.replace('<span class="file-num">#11 [TXT]</span>', '<span class="file-num">#15 [TXT]</span>')
                content = content.replace('<span class="file-num">#12 [NIV]</span>', '<span class="file-num">#16 [NIV]</span>')
                content = content.replace('<span class="file-num">#13 [TRUC]</span>', '<span class="file-num">#17 [TRUC]</span>')
                content = content.replace('<span class="file-num">#14 [PAT]</span>', '<span class="file-num">#18 [PAT]</span>')
                content = content.replace('<span class="file-num">#15 [MOVIL]</span>', '<span class="file-num">#19 [MOVIL]</span>')
                content = content.replace('<span class="file-num">#16 [MEM]</span>', '<span class="file-num">#20 [MEM]</span>')
                # Actualizar branch-count de Fase 1 (de 5 a 9)
                content = content.replace('<span class="branch-count">5 recursos</span>', '<span class="branch-count">9 recursos</span>')
                with open(mpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"🗺️ Mapa actualizado: {os.path.basename(mpath)}")

    print("\n🎉 ¡PROYECTO CÓMIC CUENT-003 DESPLEGADO CON ÉXITO EN SESIÓN 03!")

if __name__ == '__main__':
    main()
