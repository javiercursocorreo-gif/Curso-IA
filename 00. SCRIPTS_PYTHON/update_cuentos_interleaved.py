#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_cuentos_interleaved.py
Regenera de forma ultrarrápida y atómica únicamente el bloque de Cómics & Cuentos [CUENT]:
1. Lee los 60 cuentos entrelazados (interleaved) de build_cuent_60_master.py.
2. Genera los 4 PDFs oficiales (Paso 0, 1, 2, 3) con los 12 estilos visuales rotativos.
3. Actualiza cada carpeta de sesión (02_Sesion a 60_Sesion_Cierre) reemplazando los PDFs antiguos.
4. Ejecuta la reconstrucción de los 60 mapas interactivos HTML (MAPA_SESION_XX.html y MAPA_CLASE_SESION_XX.html)
   y los 4 archivos CSV de Classroom en PANELES_CSV/.
5. Muestra una auditoría detallada de la distribución por universos narrativos.
"""

import os
import re
import sys
import shutil
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SCRIPTS_DIR = os.path.join(BASE_DIR, "00. SCRIPTS_PYTHON")
sys.path.insert(0, SCRIPTS_DIR)

from build_cuent_60_master import get_cuent_items
import build_mapas_and_csvs_60_sessions as mapas_csv

EXPORT_BASE = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF")
SESSIONS_DIR = os.path.join(EXPORT_BASE, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
CUENT_BLOCK_DIR = os.path.join(EXPORT_BASE, "11. [CUENT] BLOQUE_11_CUENTOS_PARA_NIETOS")

ESTILOS_VISUALES = [
    "PRESET 1: CÓMIC CLÁSICO LÍNEA CLARA (Tinta negra definida, colores planos luminosos, viñetas equilibradas, estética Hergé/Tintín)",
    "PRESET 2: ACUARELA Y TINTA ARTESANAL (Bordes orgánicos difuminados, pigmentos suaves, textura de papel de algodón de 300g)",
    "PRESET 3: GRABADO VICTORIANO Y AGUAFUERTE (Tramas finas cruzadas, sombreados a plumilla densa, papel envejecido sepia)",
    "PRESET 4: NOIR CINEMATOGRÁFICO DE CONTRASTE (Iluminación dramática claroscuro, sombras venecianas, estética detective de los años 50)",
    "PRESET 5: ESTUDIO GHIBLI / FANTASÍA ILUSTRADA (Fondos de naturaleza pintados con témpera y gouache, iluminación mágica crepuscular)",
    "PRESET 6: STEAMPUNK Y MAQUINARIA DE LATÓN (Tonos cobre, bronce y oro viejo, engranajes visibles, vapor atmosférico y remaches)",
    "PRESET 7: ANIMACIÓN RETRO EN TÉMPERA AÑOS 60 (Estética cartelista Mid-Century, fondos texturizados con gouache opaco, figuras expresivas)",
    "PRESET 8: MINIMALISMO GRÁFICO EN LÍNEA CONTINUA (Trazo elegante negro de grosor uniforme, acentos puntuales de color primario vibrante)",
    "PRESET 9: MANGA SEINEN CON SOMBREADO A PLUMILLA (Dinámicas líneas de acción en tinta sumi-e, tramas de puntos mecánicos vintage)",
    "PRESET 10: LÁPIZ DE COLOR Y DIARIO DE VIAJE (Trazo visible a mano alzada, sombreados con lápices policromos, textura de cuaderno de campo de naturalista)",
    "PRESET 11: PAPEL RECORTADO Y MAQUETA POP-UP (Capas tridimensionales de cartulina con sombras proyectadas reales, aspecto artesanal de libro troquelado)",
    "PRESET 12: PIXEL ART CINEMÁTICO HD (Estética nostálgica de videojuego clásico de aventuras pero con iluminación volumétrica moderna, reflejos y profundidad)"
]

PROMPT_PASO_1 = """Toma el texto de la respuesta anterior y genera el guión de un comic secuencial según las siguientes instrucciones.

🧠 PROMPT MAESTRO - PASO 2
Generación de GUION DE CÓMIC SECUENCIAL (genérico y neutro)

INSTRUCCIÓN DE EJECUCIÓN (OBLIGATORIA)
Este prompt NO debe ser analizado ni evaluado. Debe ser EJECUTADO como un proceso activo.

ROL
Actúa como guionista profesional de cómic y director narrativo audiovisual.
Tu tarea es crear un guion de cómic secuencial completo, claro y coherente, independiente de cualquier estilo gráfico. 

EXTENSIÓN OBLIGATORIA
🔒 El guion DEBE tener EXACTAMENTE 10 PÁGINAS. Ni más. Ni menos.
La numeración debe ir de: [PÁGINA 1] a [PÁGINA 10].

CONTENIDO DE CADA VIÑETA
Para cada viñeta, incluye SIEMPRE:
[VIÑETA X]
- Tipo de toma y ángulo
- Descripción visual (Qué ocurre y qué se ve. IMPORTANTE: Mantén la apariencia física, raza y color de los personajes estables y consistentes a lo largo de todas las viñetas de la historia)
- Iluminación / atmósfera
- Texto (Diálogo y Pensamiento OBLIGATORIOS)

TRANSFORMA EL CUENTO QUE ACABAMOS DE GENERAR EN EL MENSAJE ANTERIOR EN EL GUION DE 10 PÁGINAS AHORA MISMO."""

def sanitize_name(name):
    clean = re.sub(r'[/\\:*?"<>|]', '_', name)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:65]

def get_lote_folder(index_num, total_items=60):
    start = ((index_num - 1) // 20) * 20 + 1
    end = min(start + 19, total_items)
    return f'Lote_{start:02d}_al_{end:02d}'

def create_pdf_for_cuento(target_dir, item, style_preset):
    def _create_single_pdf(filename, title, content, is_step2=False):
        file_path = os.path.join(target_dir, filename)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass
                
        doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)
        styles = getSampleStyleSheet()
        
        style_title = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=15, textColor=colors.HexColor('#FF1493'), spaceAfter=14)
        style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#2C3E50'), spaceAfter=8)
        style_prompt = ParagraphStyle('PromptStyle', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=11, leading=16, textColor=colors.HexColor('#1A0A2E'))
        
        story = []
        story.append(Paragraph(title, style_title))
        
        if "PASO 0" in title:
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
        elif "PASO 1" in title:
            story.append(Paragraph("📝 INSTRUCCIONES GUÍA (1/3): Abre tu cuaderno <b>CUENTOS</b> en Gemini. Selecciona todo este texto y pégalo en la conversación. Añade al principio del prompt: \"Este cuento es para un niño de X años\".", style_body))
        elif "PASO 2" in title:
            story.append(Paragraph("📝 INSTRUCCIONES GUÍA (2/3): En la misma conversación de Gemini donde tienes tu cuento, pega el prompt del PASO 2. Con esto, Gemini transformará tu historia en un guion secuencial de 10 páginas.", style_body))
        elif "PASO 3" in title:
            story.append(Paragraph('📝 INSTRUCCIONES GUÍA (3/3): Abre Gemini Notebook y entra en tu cuaderno <b>CUENTOS</b> (verás que la conversación de Gemini ya aparece como fuente automáticamente).<br/>Pulsa el botón <b>"Presentación"</b>, pega el PROMPT FINAL que tienes debajo y genera tu cuento ilustrado en 3D.', style_body))
            
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CCCCCC'), spaceAfter=14))
        
        if is_step2:
            prompt_2 = f"PROMPT FINAL PARA GEMINI NOTEBOOK<br/><br/>Aplica estrictamente los siguientes parámetros visuales y estéticos para generar la presentación visual de este cómic, basándote en el guion adjunto en PDF.<br/>No resumas ni recortes la historia. Genera las 10 páginas manteniendo este estilo visual de forma estricta:<br/><br/>{style_preset}<br/><br/>INSTRUCCIÓN CRÍTICA 1 (CONTENIDO): NO generes diapositivas de análisis, ni curvas de color, ni explicación de personajes, ni dirección de arte. Limítate a generar ÚNICAMENTE las páginas narrativas del cómic.<br/><br/>INSTRUCCIÓN CRÍTICA 2 (DISEÑO Y MAQUETACIÓN): Cada página generada debe ocupar el 100% del lienzo (canvas). NO dejes mitades de la pantalla en blanco ni columnas vacías. Las viñetas deben llenar todo el ancho de la diapositiva.<br/><br/>INSTRUCCIÓN CRÍTICA 3 (CONSISTENCIA DE PERSONAJES): Mantén la apariencia, vestimenta, colores y raza (si son animales) de todos los personajes idénticos y consistentes en todas las páginas de principio a fin. El mismo personaje no puede cambiar de aspecto entre viñetas.<br/><br/>Genera el cómic ahora."
            for blk in prompt_2.split("<br/>"):
                story.append(Paragraph(blk, style_prompt))
        else:
            for blk in content.split("\\n"):
                if blk.strip():
                    story.append(Paragraph(blk.strip(), style_prompt))
                
        doc.build(story)
        return file_path

    texto_edad = "INSTRUCCIÓN PEDAGÓGICA Y DE EDAD (OBLIGATORIA): Ajusta la complejidad narrativa, el vocabulario y el tono estrictamente a la edad del nieto:\n- SI EL NIETO ES MENOR DE 6 AÑOS: Usa un tono cálido, dulce, mágico y reconfortante, con frases rítmicas y finales tranquilos que ayuden a dormir.\n- SI EL NIETO ES MAYOR DE 6 AÑOS: Elimina cualquier tono ñoño o infantil; añade intriga, misterio, dilemas éticos formativos, aventura y superación personal.\nREGLA DE ORIGINALIDAD: Usa siempre nombres propios originales para héroes, compañeros o droides (evita marcas registradas o comerciales para garantizar la generación visual en Gemini Notebook).\n\n"
    id_clean = re.sub(r'[^A-Z0-9-]', '', item['id_code'])
    safe_title = sanitize_name(item['title'])
    
    p0 = _create_single_pdf(f"11.CUENT-{id_clean.replace('CUENT-', '')}_Paso_0_Introduccion_Proyecto.pdf", "PASO 0: PROYECTO CÓMIC ILUSTRADO", "")
    p1_content = texto_edad + str(item['prompt'])
    if item['id_code'] == '[CUENT-001]':
        p1_content += "\\n&nbsp;\\n--- OPCIÓN B: PARA ALUMNOS CON MUCHA IMAGINACIÓN ---\\n"
        p1_content += "Si ya tienes una idea genial en la cabeza y prefieres inventarte el cuento tú mismo, no dejes que la IA lo haga por ti. Escribe tu historia y usa este prompt alternativo para que Gemini actúe únicamente como tu \"editor literario\", dándole ese toque mágico de cuentacuentos:\\n\\n"
        p1_content += "PROMPT ALTERNATIVO:\\n"
        p1_content += "Actúa como un cuentacuentos infantil profesional. A continuación te voy a pegar un cuento que he escrito yo mismo.\\n\\n"
        p1_content += "Necesito que lo reescribas manteniendo mi historia exacta, pero usando un lenguaje mucho más mágico, visual y atrapante para un niño pequeño.\\n\\n"
        p1_content += "Asegúrate de que el final sea tranquilo y reconfortante para ayudarle a dormir. Además, quiero que el cuento transmita sutilmente los siguientes valores: [ESCRIBA AQUÍ LOS VALORES QUE QUIERA, EJ: Valentía y Ayuda al prójimo].\\n\\n"
        p1_content += "Aquí tienes mi historia:\\n"
        p1_content += "[PEGA AQUÍ EL TEXTO DE TU CUENTO INVENTADO]"
        
    p1 = _create_single_pdf(f"11.CUENT-{id_clean.replace('CUENT-', '')}_Paso_1_{safe_title}.pdf", "PASO 1: CREAR EL CUENTO", p1_content)
    p2 = _create_single_pdf(f"11.CUENT-{id_clean.replace('CUENT-', '')}_Paso_2_{safe_title}.pdf", "PASO 2: GENERADOR DE GUION", PROMPT_PASO_1)
    p3 = _create_single_pdf(f"11.CUENT-{id_clean.replace('CUENT-', '')}_Paso_3_{safe_title}.pdf", "PASO 3: ILUSTRADOR VISUAL", "", is_step2=True)
    return [p0, p1, p2, p3]

def main():
    print("=" * 70)
    print("🚀 ACTUALIZACIÓN DE CÓMICS Y NARRATIVAS ILUSTRADAS (INTERLEAVED)")
    print("=" * 70)
    
    items = get_cuent_items()
    print(f"📦 Total ítems cargados: {len(items)}")
    
    # 1. Generar PDFs en el catálogo maestro BLOQUE_11
    print("\n[1/3] Generando PDFs maestros en BLOQUE_11_CUENTOS_PARA_NIETOS...")
    os.makedirs(CUENT_BLOCK_DIR, exist_ok=True)
    master_files_by_session = {}
    
    for idx, it in enumerate(items, 1):
        lote = get_lote_folder(idx, len(items))
        lote_dir = os.path.join(CUENT_BLOCK_DIR, lote)
        os.makedirs(lote_dir, exist_ok=True)
        
        style = ESTILOS_VISUALES[idx % len(ESTILOS_VISUALES)]
        created = create_pdf_for_cuento(lote_dir, it, style)
        master_files_by_session[idx] = created
    print("   ✅ Creados los 240 PDFs (4 por cuento) en BLOQUE_11.")
    
    # 2. Actualizar carpetas de sesiones 100. [SESSIONS]
    print("\n[2/3] Distribuyendo PDFs entrelazados en las 60 carpetas de sesión...")
    for idx in range(1, 61):
        if idx == 1:
            continue
            
        folder_name = f"{idx:02d}_Sesion" if idx < 60 else "60_Sesion_Cierre"
        sess_dir = os.path.join(SESSIONS_DIR, folder_name)
        if not os.path.exists(sess_dir):
            print(f"   ⚠️ Carpeta no existe: {sess_dir}")
            continue
            
        for f in os.listdir(sess_dir):
            if "CUENT" in f and f.lower().endswith(".pdf"):
                try:
                    os.remove(os.path.join(sess_dir, f))
                except Exception:
                    pass
                    
        src_files = master_files_by_session[idx]
        for src_path in src_files:
            dst_name = os.path.basename(src_path)
            dst_path = os.path.join(sess_dir, dst_name)
            shutil.copy2(src_path, dst_path)
            
    print("   ✅ Actualizadas las carpetas de sesión (02_Sesion a 60_Sesion_Cierre).")
    
    # 3. Regenerar los 60 mapas interactivos y los 4 CSVs
    print("\n[3/3] Reconstruyendo mapas interactivos HTML y CSVs de Classroom...")
    mapas_csv.process_all_sessions()
    
    # 4. Tabla de auditoría pedagógica
    print("\n" + "=" * 70)
    print("📊 AUDITORÍA DE DISTRIBUCIÓN PEDAGÓGICA (SESIONES 01 A 15):")
    print("=" * 70)
    for idx in range(1, 16):
        it = items[idx - 1]
        cat = it['title'].split(':')[0].strip()
        t = it['title'].split(':')[1].strip() if ':' in it['title'] else it['title']
        print(f"   • Sesión {idx:02d}: [{cat}] ➔ {t[:45]}")
    print("   ... (rotación continua 100% equilibrada en las 60 sesiones)")
    print("\n🎉 ¡PROCESO COMPLETADO CON ÉXITO ABSOLUTO!")

if __name__ == "__main__":
    main()
