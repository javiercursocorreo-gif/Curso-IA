# -*- coding: utf-8 -*-
"""
Actualización de Fichas de Sesión 01 y Generadores Maestros:
1. Actualizar build_memoria_60_master y export_movil_and_mem_pdfs con:
   - Flujo de 5 pasos con cámara en [MOVIL]
   - Metodología Copiar/Pegar y orden limpia sin sesgos en [MEM]
2. Corregir fichas de la Sesión 01:
   - TXT-001: Continuidad de chat + orden para pintar la cesta
   - EST-001: Edición en el mismo chat (sin "descarga y ve a Gemini")
   - FRAC-058: Fusión de textos limpios (sin duplicidad) y vídeo sin emojis
   - FUT-001: Año 2030 (en lugar de 2028)
   - NIV-001: Metodología de 2 pasos (Diseñar prompt con IA + Pintar infografía)
3. Re-generar los 5 Paneles CSV
"""

import os
import re
import shutil
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSIONS_DIR = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
S01_DIR = os.path.join(SESSIONS_DIR, "01_Sesion")

def create_card(file_path, block_name, item_id, item_title, concept_text, steps_list, theme_hex='#005A9E', bg_hex='#F0F4F8'):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if os.path.exists(file_path):
        try: os.remove(file_path)
        except Exception: pass

    doc = SimpleDocTemplate(
        file_path, pagesize=letter,
        rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45
    )
    styles = getSampleStyleSheet()
    t_color = colors.HexColor(theme_hex)
    b_color = colors.HexColor(bg_hex)

    style_header = ParagraphStyle('HStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, textColor=t_color, spaceAfter=4, alignment=1)
    style_block = ParagraphStyle('BStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, textColor=colors.HexColor('#1A0A2E'), spaceAfter=12, alignment=1)
    style_title = ParagraphStyle('TStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=colors.HexColor('#1A0A2E'), spaceAfter=12)
    style_section_h = ParagraphStyle('SHStyle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=t_color, spaceBefore=8, spaceAfter=5)
    style_body = ParagraphStyle('BdStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=9.5, leading=14, textColor=colors.HexColor('#2C3E50'), spaceAfter=6)
    style_prompt = ParagraphStyle('PStyle', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=9.5, leading=14, textColor=colors.HexColor('#1A0A2E'))
    style_box = ParagraphStyle('BxStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=14, textColor=colors.HexColor('#2C3E50'))

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph(block_name.upper(), style_block))
    story.append(HRFlowable(width="100%", thickness=2, color=t_color, spaceAfter=12))
    story.append(Paragraph(f"{item_id} {item_title}", style_title))

    if concept_text:
        story.append(Paragraph("💡 Contexto y Objetivo Didáctico", style_section_h))
        story.append(Paragraph(str(concept_text).replace('\n', '<br/>'), style_body))
        story.append(Spacer(1, 4))

    for step_title, step_content in steps_list:
        story.append(Paragraph(step_title, style_section_h))
        rows = []
        for line in str(step_content).split('\n'):
            if line.strip():
                rows.append([Paragraph(line.strip(), style_box)])
        table = Table(rows, colWidths=[letter[0] - 90], splitByRow=1)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), b_color),
            ('BORDER', (0,0), (-1,-1), 1.2, t_color),
            ('PADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(table)
        story.append(Spacer(1, 6))

    doc.build(story)

def main():
    print("🛠️ Actualizando fichas clave de la Sesión 01...")

    # 1. TXT-001: La IA como Consejera de Compras del Hogar
    p_txt1 = os.path.join(S01_DIR, "1. TXT-001_La IA como Consejera de Compras del Hogar.pdf")
    create_card(
        p_txt1,
        "BLOQUE 1: PROMPTS DE COMUNICACIÓN Y TEXTO [TXT]",
        "[TXT-001]",
        "La IA como Consejera de Compras del Hogar",
        "Aprender a utilizar el chat conversacional de Gemini para optimizar el presupuesto del hogar, elaborar menús semanales saludables y generar listas de la compra organizadas por pasillos del supermercado.",
        [
            ("💬 Paso 1: Conversación y Planificación en el Chat de Gemini",
             "Escribe este mensaje en el cuadro de chat de Gemini:\n\n"
             "\"Actúa como un nutricionista y experto en ahorro familiar. Somos 2 personas en casa y disponemos de 50 euros de presupuesto para las comidas de lunes a viernes. Diseña un menú mediterráneo saludable, variado y fácil de cocinar, y a continuación elabora la lista de la compra organizada por secciones del supermercado (frutería, carnicería, pescadería, despensa).\"\n"),
            ("🎨 Paso 2: Ilustración de la Compra en la Misma Conversación",
             "En la misma ventana de chat, escribe a continuación en la barra de abajo:\n\n"
             "\"Ahora genera una fotografía hiperrealista y apetitosa que muestre sobre una mesa rústica de madera esta cesta de la compra fresca con frutas, verduras, pescado y aceite de oliva bajo la luz cálida de una cocina familiar.\"\n\n"
             "<b>👉 Ahora te toca a ti:</b> ¡Pídele a Gemini que adapte el menú si alguno de los dos necesita una dieta baja en sal o colesterol!")
        ],
        theme_hex='#005A9E', bg_hex='#F0F4F8'
    )
    print("   ✓ TXT-001 actualizado.")

    # 2. EST-001: Realista - Faro al Amanecer
    p_est1 = os.path.join(S01_DIR, "2. EST-001_REALISTA (FOTORREALISMO) - Faro al Amanecer.pdf")
    create_card(
        p_est1,
        "BLOQUE 2: ESTILOS DE IMAGEN EN IA [EST]",
        "[EST-001]",
        "REALISTA (FOTORREALISMO) - Faro al Amanecer",
        "Aprender a pedir a la IA imágenes de calidad fotográfica con iluminación natural, texturas orgánicas y profundidad de campo, y practicar la edición continua en el mismo hilo de conversación.",
        [
            ("🖼️ Paso 1: Generación de la Fotografía en el Chat de Gemini",
             "Escribe este prompt directamente en el chat de Gemini:\n\n"
             "\"Fotografía profesional en 8k, estilo National Geographic, de un viejo faro de piedra blanca y roja situado sobre un acantilado escarpado. El mar en calma refleja las primeras luces doradas del amanecer. Espuma suave en las rocas, cielo despejado con tonos naranjas y violetas, iluminación cinematográfica nítida, sin textos.\"\n"),
            ("🧪 Paso 2: Reto de Edición en la Misma Conversación",
             "Una vez que Gemini te muestre la imagen del faro, <b>no salgas del chat ni descargues nada</b>. Escribe a continuación en la barra de abajo:\n\n"
             "\"Conserva exactamente la misma estructura del faro y las rocas del acantilado, pero cambia el amanecer en calma por una noche cerrada de tormenta con olas embravecidas rompiendo contra las rocas, relámpagos iluminando la torre y lluvia torrencial.\"\n\n"
             "<b>👉 Ahora te toca a ti:</b> ¡Prueba a pedirle que añada un barco pesquero con su luz encendida regresando a puerto!")
        ],
        theme_hex='#1A5276', bg_hex='#EBF5FB'
    )
    print("   ✓ EST-001 actualizado.")

    # 3. PRAC-001: Retrato Mágico
    p_prac1 = os.path.join(S01_DIR, "3. PRAC-001_Retrato Mágico_ Disfraz de Reyes, Aristócratas o Época Clásica.pdf")
    create_card(
        p_prac1,
        "BLOQUE 3: TALLERES DE PROMPTS PRÁCTICOS [PRAC]",
        "[PRAC-001]",
        "Retrato Mágico: Disfraz de Reyes, Aristócratas o Época Clásica",
        "Aprender a transformar una fotografía personal o de un familiar en una obra pictórica de época clásica, manteniendo el parecido fisonómico y añadiendo vestiduras de alta nobleza o realeza.",
        [
            ("👑 Paso 1: Crear el Retrato Base en el Chat de Gemini",
             "Escribe este prompt en el chat de Gemini (o pega una foto tuya con Ctrl+V):\n\n"
             "\"Retrato al óleo estilo Rembrandt de un monarca renacentista con capa de terciopelo carmesí y cuello de armiño, corona dorada finamente trabajada con rubíes y esmeraldas, iluminación claroscuro dramática, mirada serena y sabia, pincelada visible de óleo sobre lienzo, sin textos.\"\n"),
            ("🎭 Paso 2: Reto de Transformación en la Misma Conversación",
             "Escribe a continuación en el mismo chat:\n\n"
             "\"Transforma ahora este retrato en un cuadro de corte barroco del siglo XVIII en el Palacio de Versalles, sustituyendo la capa por casaca bordada en hilos de oro y peluca dieciochesca, con un gran salón de espejos de fondo.\"\n\n"
             "<b>👉 Ahora te toca a ti:</b> ¡Pega una foto de tu nieto o de tu mascota y dile a Gemini: 'Transfórmalo en un pequeño príncipe o princesa de cuento'!")
        ],
        theme_hex='#2874A6', bg_hex='#EAF2F8'
    )
    print("   ✓ PRAC-001 actualizado.")

    # 4. FRAC-058: Tú eres un Fractal (Biomimética)
    p_frac1 = os.path.join(S01_DIR, "4. FRAC-058 Tú eres un Fractal (Pulmones, Bronquios y Sistema Circulatorio).pdf")
    create_card(
        p_frac1,
        "BLOQUE 4: FRACTALES Y BIOMIMÉTICA EN IA [FRAC]",
        "[FRAC-058]",
        "Tú eres un Fractal: La Geometría Secreta del Cuerpo Humano",
        "Descubrir cómo la naturaleza utiliza las matemáticas fractales para empaquetar una superficie gigantesca dentro del cuerpo humano: los pulmones desplegados ocuparían una pista de tenis gracias a su ramificación infinita.",
        [
            ("🫁 Concepto Científico y Visualización en Clase",
             "• <b>Autosimilitud Biológica:</b> Los bronquios y vasos sanguíneos se dividen una y otra vez siguiendo una regla de ramificación idéntica a las ramas de un roble o las raíces de un árbol.\n\n"
             "• <b>Material en Aula:</b> Proyecta la animación MP4 adjunta (<b>4. FRAC-058 2. TU ERES UN FRACTAL (Biomimetica).mp4</b>) para observar en movimiento la transición entre los pulmones humanos y las redes fluviales y arbóreas del planeta.\n"),
            ("🎨 Prompt para Generar la Comparativa en Gemini",
             "Escribe en el chat de Gemini:\n\n"
             "\"Infografía médica hiperrealista y elegante que compare en dos mitades simétricas: a la izquierda, el árbol bronquial transparente de los pulmones humanos iluminado en azul y carmesí; a la derecha, la copa de un árbol centenario en invierno. Fondo oscuro de museo anatómico, iluminación volumétrica suave, estética científica limpia y sin textos en inglés.\"\n\n"
             "<b>👉 Debate en Clase:</b> ¿Por qué crees que la evolución eligió la misma geometría para un árbol que para nuestros pulmones?")
        ],
        theme_hex='#196F3D', bg_hex='#EAFAF1'
    )
    print("   ✓ FRAC-058 actualizado y fusionado.")

    # 5. FUT-001: Año 2030 - El Asistente Robótico Compasivo (Adelantado de 2028 a 2030)
    # Eliminar viejo archivo 2028 si existe
    old_fut = os.path.join(S01_DIR, "6. FUT-001_Año 2028_ El asistente robótico compasivo en el hogar familiar ma.pdf")
    if os.path.exists(old_fut):
        try: os.remove(old_fut)
        except Exception: pass

    p_fut1 = os.path.join(S01_DIR, "6. FUT-001_Año 2030_ El asistente robótico compasivo en el hogar familiar de personas mayores.pdf")
    create_card(
        p_fut1,
        "BLOQUE 6: LÍNEA DE TIEMPO DEL FUTURO Y ROBÓTICA AMABLE [FUT]",
        "[FUT-001]",
        "Año 2030: El Asistente Robótico Compasivo en el Hogar Familiar",
        "Explorar una visión positiva y humana de la tecnología en el año 2030: robots domésticos con tacto cálido y voz empática diseñados para ayudar en tareas pesadas y acompañar sin sustituir el afecto humano.",
        [
            ("🤖 Paso 1: Generar la Visión de Futuro en Gemini",
             "Escribe este prompt en el chat de Gemini:\n\n"
             "\"Fotografía cinematográfica cálida y realista ambientada en el año 2030 en el luminoso salón de un hogar familiar. Una persona mayor sentada en un sillón sonríe mientras un asistente robótico de diseño ergonómico, con acabados en blanco mate y madera suave, le acerca con delicadeza una taza de té humeante. Luz solar natural entrando por el balcón, atmósfera de tranquilidad, compañía y dignidad tecnológica, sin textos.\"\n"),
            ("🔮 Paso 2: Reflexión y Pregunta a la IA",
             "Escribe a continuación en el mismo chat:\n\n"
             "\"¿Qué sensores de seguridad y funciones de salud preventiva (detección de caídas, recordatorio de medicación y control cardíaco) incorporarán los robots domésticos en la década de 2030?\"\n\n"
             "<b>👉 Ahora te toca a ti:</b> ¡Pídele a Gemini que diseñe una función especial que a ti te gustaría que tuviera ese robot en tu propia casa!")
        ],
        theme_hex='#6C3483', bg_hex='#F4ECF7'
    )
    print("   ✓ FUT-001 actualizado al Año 2030.")

    # 6. NIV-001: Los 7 Niveles de Riqueza y Libertad Financiera (Metodología de 2 Pasos)
    p_niv1 = os.path.join(S01_DIR, "9. NIV-001_Los 7 Niveles de Riqueza y Libertad Financiera.pdf")
    create_card(
        p_niv1,
        "BLOQUE 9: ESCALAFONES Y NIVELES (CULTURA 101) [NIV]",
        "[NIV-001]",
        "Los 7 Niveles de Riqueza y Libertad Financiera",
        "Aprender la técnica de 'Meta-Prompting': primero pedir a Gemini que actúe como diseñador infográfico profesional para redactar el prompt maestro, y luego generar la lámina visual piramidal.",
        [
            ("🧠 Paso 1: Pedir a Gemini que Diseñe el Prompt Maestro",
             "Escribe esta orden en el chat de Gemini:\n\n"
             "\"Actúa como un diseñador infográfico senior. Diseña y redacta un prompt maestro detallado en español para crear una infografía piramidal sobre 'Los 7 Niveles de Libertad Financiera y Riqueza de Tiempo'. Describe los 7 estratos desde la base (Supervivencia) hasta la cima (Filantropía y Legado), indicando metáforas visuales claras, un icono 3D en la cúspide y la regla estricta de cero textos en inglés.\"\n"),
            ("🎨 Paso 2: Generar la Infografía en la Misma Conversación",
             "Una vez que Gemini te muestre la descripción del diseño, escribe a continuación en la barra de abajo:\n\n"
             "\"Genera ahora la imagen realista de esta infografía piramidal siguiendo exactamente la estructura y las metáforas visuales que acabas de diseñar.\"\n\n"
             "<b>👉 Ahora te toca a ti:</b> ¡Comenta con tu compañero de clase en qué nivel crees que se alcanza la verdadera tranquilidad mental!")
        ],
        theme_hex='#7D3C98', bg_hex='#F5EEF8'
    )
    print("   ✓ NIV-001 actualizado con Metodología de 2 Pasos.")

    # 7. MOVIL-001: Símbolos de Lavado Textil (Flujo de 5 Pasos de Cámara)
    p_mov1 = os.path.join(S01_DIR, "12. [MOVIL-001]_Símbolos de Lavado Textil_ Jersey delicado de lana.pdf")
    create_card(
        p_mov1,
        "BLOQUE 12: EL SALVAVIDAS DEL MÓVIL [MOVIL]",
        "[MOVIL-001]",
        "Símbolos de Lavado Textil: Jersey Delicado de Lana",
        "Descifrar etiquetas de ropa difíciles mediante la cámara del teléfono y la inteligencia artificial para evitar desteñidos y prendas encogidas.",
        [
            ("🖥️ Paso 1: Generar la Etiqueta del Reto en la Pantalla del PC",
             "Escribe este prompt en el chat de Gemini en tu ordenador:\n\n"
             "\"Fotografía en primer plano macro de la etiqueta interior de un jersey de lana beige, con 5 símbolos de cuidado textil impresos en negro: barreño de agua a 30 grados, tina tachada, plancha con un punto, círculo tachado y cuadrado con círculo tachado. Fondo textil realista, números legibles, iluminación limpia, sin textos en inglés.\"\n"),
            ("📱 Paso 2: El Salvavidas con tu Móvil (Paso a Paso en la App de Gemini)",
             "1. Abre la aplicación de <b>Gemini</b> en tu teléfono móvil.\n"
             "2. Pulsa el icono de la <b>Cámara</b> 📷 (abajo a la derecha junto al micrófono).\n"
             "3. Encuadra la etiqueta que se ve en la pantalla del PC y pulsa el <b>botón blanco de disparo</b>.\n"
             "4. Pulsa <b>Aceptar / Adjuntar</b> para incorporar la foto al mensaje.\n"
             "5. Toca el icono del <b>Micrófono</b> 🎙️ y di con voz clara:\n"
             "   <i>«Gemini, mira esta etiqueta. ¿Puedo meter este jersey en la lavadora o se me va a encoger? ¿Puedo usar secadora?»</i>\n"
             "6. Pulsa la flecha de <b>Enviar ➔</b> para escuchar y leer el salvavidas.")
        ],
        theme_hex='#008080', bg_hex='#EBF6F6'
    )
    print("   ✓ MOVIL-001 actualizado con el flujo de cámara.")

    # 8. MEM-001: La Plaza o el Barrio de Mi Infancia (Método Copiar/Pegar y Fórmula Limpia)
    p_mem1 = os.path.join(S01_DIR, "13. [MEM-001]_La Plaza o el Barrio de Mi Infancia_ Juegos de Calle (Peonza y Ca.pdf")
    create_card(
        p_mem1,
        "BLOQUE 13: CÁPSULA DE LA MEMORIA [MEM]",
        "[MEM-001]",
        "La Plaza o el Barrio de Mi Infancia: Juegos de Calle y Raíces",
        "Conectar con los nietos rescatando una fotografía real de tu pueblo o barrio de infancia y utilizando la IA para extraer curiosidades históricas y un microrrelato emotivo sin inventar datos familiares.",
        [
            ("📸 Paso 1: Conseguir la Foto Histórica en el PC (¡En 3 Clics!)",
             "1. Abre una pestaña en Google y busca una foto antigua: ej. <i>\"Plaza Mayor de Cuéllar años 60\"</i> o <i>\"Chamberí Madrid años 50\"</i> (o una foto escaneada de tu álbum familiar).\n"
             "2. Haz <b>clic derecho</b> sobre la foto y elige: <b>«Copiar imagen»</b>.\n"
             "3. Cambia a la pestaña de Gemini y en el cuadro de mensaje haz <b>clic derecho ➔ «Pegar»</b> (o pulsa Ctrl + V).\n\n"
             "<i>(Alternativa si no encuentras foto: pídele a Gemini que recree una con IA indicando tu pueblo/barrio y la década).</i>\n"),
            ("💬 Paso 2: Orden Limpia y Universal para Preguntar a Gemini",
             "Escribe exactamente esta orden en el chat de Gemini tras pegar la foto:\n\n"
             "\"Mira con atención esta fotografía histórica:\n"
             "1. Señálame 3 detalles curiosos que aparezcan en ESTA foto que contrasten con el mundo en el que viven los niños de hoy en día.\n"
             "2. Escribe un microrrelato de máximo 2 párrafos cortos (menos de 80 palabras en total) en mi voz de abuelo/a, explicándole con cariño a mi nieto/a cómo era la vida en el lugar donde me crié cuando tenía su edad.\n"
             "(Regla: No inventes acontecimientos familiares que no se vean en la foto y no digas 'tu pueblo', sino 'el lugar donde creció tu abuelo/a')\"")
        ],
        theme_hex='#B8860B', bg_hex='#FAF6E8'
    )
    print("   ✓ MEM-001 actualizado con fórmula limpia y universal.")

    # 9. Re-generar los paneles CSV
    print("\n📊 Regenerando los 5 Paneles CSV para Google Classroom...")
    import generate_multiple_csvs
    generate_multiple_csvs.main()
    print("\n🎉 ¡Actualización de Sesión 01 y Paneles CSV completada con éxito!")

if __name__ == "__main__":
    main()
