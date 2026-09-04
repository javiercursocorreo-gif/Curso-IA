# -*- coding: utf-8 -*-
"""
Generador de Fichas y Materiales para la Clase Monográfica 3:
"3. Cómo hacer un cuento con NLM"
Crea las fichas PDF con el formato idéntico a las ternas de las sesiones y los archivos complementarios.
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(BASE_DIR, "CLASES", "3. COMO_HACER_UN_CUENTO_CON_NLM")
os.makedirs(TARGET_DIR, exist_ok=True)

# Título y tema del nuevo cuento para este monográfico
CUENTO_TITULO = "El Viaje en Globo del Abuelo y la Gata Luna"
CUENTO_VALORES = "Curiosidad, aventura compartida, confianza mutua y amor a la naturaleza"
ESTILO_VISUAL = "PRESET: ANIMACIÓN 3D TIPO PIXAR (Personajes 3D entrañables, iluminación cinematográfica cálida, texturas suaves de tela y pelaje, máxima expresividad facial)"

# ==============================================================================
# PROMPT MAESTRO DEL PASO 2 (IDÉNTICO A LAS TERNAS)
# ==============================================================================
PROMPT_PASO_2_GUION = """Toma el texto de la respuesta anterior y genera el guión de un comic secuencial según las siguientes instrucciones.

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

ESTRUCTURA DE CADA PÁGINA
Cada página debe estructurarse con la siguiente fórmula:

[PÁGINA X: TÍTULO DE LA ESCENA]
Resumen narrativo (1 línea)

[PÁGINA X]
- Página de apertura / Viñeta única
- Escena clave: [Momento de la historia]
- Tipo de plano: [Plano general / Plano medio / Primer plano]
- Descripción visual: [Acción clara y personajes con vestimenta idéntica]
- Iluminación: [Ambiente]
- Texto:
  - Diálogo: "[Línea de diálogo obligatoria]"
  - Pensamiento: "[Pensamiento del personaje]"

CONTENIDO DE CADA VIÑETA
Para cada viñeta, incluye SIEMPRE:
[VIÑETA X]
- Tipo de toma y ángulo
- Descripción visual (Qué ocurre y qué se ve. IMPORTANTE: Mantén la apariencia física, vestimenta y rasgos de los personajes estables y consistentes a lo largo de todas las viñetas de la historia)
- Iluminación / atmósfera
- Texto (Diálogo y Pensamiento OBLIGATORIOS)

TRANSFORMA EL CUENTO QUE ACABAMOS DE GENERAR EN EL MENSAJE ANTERIOR EN EL GUION DE 10 PÁGINAS AHORA MISMO."""

# ==============================================================================
# PROMPT MAESTRO DEL PASO 3 (NOTEBOOKLM - IDÉNTICO A LAS TERNAS)
# ==============================================================================
PROMPT_PASO_3_NLM = f"""PROMPT FINAL PARA NOTEBOOKLM

Aplica estrictamente los siguientes parámetros visuales y estéticos para generar la presentación visual de este cómic, basándote en el guion adjunto en las fuentes.
No resumas ni recortes la historia. Genera las 10 páginas manteniendo este estilo visual de forma estricta:

{ESTILO_VISUAL}

INSTRUCCIÓN CRÍTICA 1 (CONTENIDO): NO generes diapositivas de análisis, ni curvas de color, ni explicación de personajes, ni dirección de arte. Limítate a generar ÚNICAMENTE las páginas narrativas del cómic.

INSTRUCCIÓN CRÍTICA 2 (DISEÑO Y MAQUETACIÓN): Cada página generada debe ocupar el 100% del lienzo (canvas). NO dejes mitades de la pantalla en blanco ni columnas vacías. Las viñetas deben llenar todo el ancho de la diapositiva.

INSTRUCCIÓN CRÍTICA 3 (CONSISTENCIA DE PERSONAJES): Mantén la apariencia, vestimenta, colores y raza (si son animales) de todos los personajes idénticos y consistentes en todas las páginas de principio a fin. El mismo personaje no puede cambiar de aspecto entre viñetas.

Genera el cómic ahora."""

# ==============================================================================
# GENERADOR DE LAS FICHAS PDF IDÉNTICAS A LAS TERNAS
# ==============================================================================
def create_pdf_ficha(filename, title, content, is_step2=False):
    file_path = os.path.join(TARGET_DIR, filename)
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)
    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=15, textColor=colors.HexColor('#FF1493'), spaceAfter=14)
    style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#2C3E50'), spaceAfter=8)
    style_prompt = ParagraphStyle('PromptStyle', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=10, leading=15, textColor=colors.HexColor('#1A0A2E'))
    
    story = []
    story.append(Paragraph(title, style_title))
    
    if "PASO 0" in title:
        paso0_text = (
            "En esta clase monográfica vamos a hacer magia pura. Vamos a combinar el poder narrativo de Gemini con el motor de generación visual de NotebookLM para crear un cómic ilustrado de 10 páginas para tus nietos (o para ti mismo).<br/><br/>"
            "Para lograrlo, siempre seguiremos estos 3 pasos (verás que en esta carpeta hay fichas de prompts, una para cada paso):<br/><br/>"
            "- <b>PASO 1 (Gemini): CREAR EL CUENTO.</b> Aquí le damos a Gemini el tema y le pedimos que redacte el cuento adaptado a la edad del niño.<br/>"
            "- <b>PASO 2 (Gemini): GENERADOR DE GUION.</b> Usamos a Gemini como guionista para que transforme el cuento del Paso 1 en un guion estructurado en 10 páginas.<br/>"
            "- <b>PASO 3 (NotebookLM): ILUSTRADOR VISUAL.</b> Nos llevamos el guion entero a NotebookLM y le pasamos el último prompt para que dibuje y maquete el cómic visualmente."
        )
        story.append(Paragraph(paso0_text, style_body))
    elif "PASO 1" in title:
        story.append(Paragraph("📝 INSTRUCCIONES GUÍA (1/3): Selecciona todo este texto y pégalo en Gemini. Añade al principio del prompt: \"Este cuento es para un niño de X años\".", style_body))
    elif "PASO 2" in title:
        story.append(Paragraph("📝 INSTRUCCIONES GUÍA (2/3): Una vez que Gemini haya escrito tu cuento en la pantalla, pega el prompt del PASO 2. Con esto, le estás pidiendo a Gemini que transforme tu historia en un guion detallado para un cómic.", style_body))
    elif "PASO 3" in title:
        story.append(Paragraph('📝 INSTRUCCIONES GUÍA (3/3): Copia el GUION que te acaba de hacer Gemini (el texto entero) y pégalo como "Texto Copiado" en las fuentes de un nuevo cuaderno de NotebookLM.<br/>Luego, copia el PROMPT FINAL que tienes justo debajo de estas instrucciones y pégalo en el botón "Presentación" de NotebookLM para generar por fin la magia de tu cómic ilustrado.', style_body))
        
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CCCCCC'), spaceAfter=14))
    
    if is_step2:
        prompt_2 = (
            f"PROMPT FINAL PARA NOTEBOOKLM<br/><br/>"
            f"Aplica estrictamente los siguientes parámetros visuales y estéticos para generar la presentación visual de este cómic, basándote en el guion adjunto en PDF.<br/>"
            f"No resumas ni recortes la historia. Genera las 10 páginas manteniendo este estilo visual de forma estricta:<br/><br/>"
            f"{ESTILO_VISUAL}<br/><br/>"
            f"INSTRUCCIÓN CRÍTICA 1 (CONTENIDO): NO generes diapositivas de análisis, ni curvas de color, ni explicación de personajes, ni dirección de arte. Limítate a generar ÚNICAMENTE las páginas narrativas del cómic.<br/><br/>"
            f"INSTRUCCIÓN CRÍTICA 2 (DISEÑO Y MAQUETACIÓN): Cada página generada debe ocupar el 100% del lienzo (canvas). NO dejes mitades de la pantalla en blanco ni columnas vacías. Las viñetas deben llenar todo el ancho de la diapositiva.<br/><br/>"
            f"INSTRUCCIÓN CRÍTICA 3 (CONSISTENCIA DE PERSONAJES): Mantén la apariencia, vestimenta, colores y raza (si son animales) de todos los personajes idénticos y consistentes en todas las páginas de principio a fin. El mismo personaje no puede cambiar de aspecto entre viñetas.<br/><br/>"
            f"Genera el cómic ahora."
        )
        for blk in prompt_2.split("<br/>"):
            story.append(Paragraph(blk, style_prompt))
    else:
        for blk in content.split("\n"):
            if blk.strip():
                story.append(Paragraph(blk.strip(), style_prompt))
            else:
                story.append(Spacer(1, 4))
            
    doc.build(story)
    return file_path

# ==============================================================================
# EJEMPLO REAL DE CUENTO Y GUION (PASOS 1 Y 2 EJECUTADOS)
# ==============================================================================
TEXTO_CUENTO_EJEMPLO = f"""EL VIAJE EN GLOBO DEL ABUELO Y LA GATA LUNA

Había una vez, en lo alto de una colina salpicada de olivos centenarios, un abuelo llamado Tomás que construía en su cobertizo algo asombroso: una cesta de mimbre gigante atada a una vela de seda de mil colores. A su lado siempre estaba Luna, una gatita gris de ojos verdes y bigotes curiosos que no se separaba de sus botas ni un solo segundo.

Una mañana soleada, mientras el rocío aún brillaba en las hojas, el abuelo encendió el quemador con un suave suspiro de aire caliente. Luna dio un brinco ágil y se acurrucó justo en el borde de la barquilla. Lentamente, como si la tierra se despidiera en silencio, la colina empezó a hacerse pequeña. Las ovejas parecían motas de algodón y los ríos cintas de plata reflejando el cielo.

Luna levantó la naricilla y vio cómo pasaba flotando una nube esponjosa con forma de pez. Con una pata juguetona intentó atrapar la niebla, sorprendiéndose de que solo fuera vapor fresco y risueño. El abuelo Tomás sonrió con ternura y ajustó la brújula dorada: «No temas, Luna, en el cielo no hay prisa, solo horizontes por descubrir».

Al atardecer, cuando el sol tiñó el cielo de tonos dorados y violetas, el globo descendió suavemente sobre un prado repleto de margaritas. Luna bostezó agradecida y se enroscó en el regazo del abuelo mientras el mundo se apagaba despacio, sabiendo que las mejores aventuras son las que se comparten con quien más quieres."""

GUION_10_PAGINAS_EJEMPLO = """[PÁGINA 1: EL TALLER DEL ABUELO]
Resumen: El abuelo Tomás y la gatita Luna preparan el globo en el cobertizo.
[PÁGINA 1]
- Viñeta de apertura / Gran plano general
- Escena clave: El abuelo Tomás (70 años, pelo blanco, chaleco de lana marrón y gafas redondas) cosiendo una gran tela de colores mientras Luna (gatita gris de ojos verdes) juega con los ovillos de cuerda.
- Iluminación: Luz dorada de mañana entrando por los ventanales de madera del taller.
- Texto:
  - Diálogo: "¡Cuidado con esa cuerda, Luna! Hoy el viento sopla a nuestro favor."
  - Pensamiento: "El abuelo siempre cumple lo que promete; hoy tocaremos el cielo."

[PÁGINA 2: EL ENCENDIDO DEL FUEGO]
Resumen: El quemador llena de aire caliente la tela multicolor en el prado.
[PÁGINA 2]
- Viñeta completa / Plano medio
- Escena clave: El abuelo Tomás acciona la válvula del quemador produciendo una llamarada naranja cálida. Luna contempla el fuego fascinada desde dentro de la cesta de mimbre.
- Iluminación: Resplandor cálido de la llama iluminando los rostros y la cesta.
- Texto:
  - Diálogo: "Sujétate bien a la barquilla, pequeña astronauta."
  - Pensamiento: "Ese rugido suave huele a aventura."

[PÁGINA 3: EL DESPEGUE SOBRE LA COLINA]
Resumen: La barquilla se despega del suelo y asciende sobre el valle.
[PÁGINA 3]
- Viñeta completa / Plano general en contrapicado
- Escena clave: El globo asciende suavemente. Abajo quedan los olivos y la casita del pueblo. El abuelo saluda a los pastores que se ven pequeños abajo.
- Iluminación: Cielo azul limpio de mediodía con luz brillante.
- Texto:
  - Diálogo: "¡Adiós colina! ¡Volvemos para la hora de la merienda!"
  - Pensamiento: "¡Las ovejas de abajo parecen diminutas bolas de algodón!"

[PÁGINA 4: EL ENCUENTRO CON LAS AVES]
Resumen: Una bandada de golondrinas acompaña el vuelo del globo.
[PÁGINA 4]
- Viñeta completa / Plano entero dinámico
- Escena clave: Un grupo de golondrinas vuela en círculos alrededor de la cesta. Luna asoma la cabecita entre los barrotes de mimbre intentando tocarlas con la patita.
- Iluminación: Destellos de sol en las plumas y en el pelaje gris de Luna.
- Texto:
  - Diálogo: "Son nuestras compañeras de ruta, Luna. Nos están enseñando el camino del viento."
  - Pensamiento: "Vuelan tan cerca que casi puedo escuchar su aleteo."

[PÁGINA 5: LA NUBE CON FORMA DE PEZ]
Resumen: Luna intenta cazar una nube que parece un gran pez blanco.
[PÁGINA 5]
- Viñeta completa / Primer plano compartido
- Escena clave: Una nube esponjosa atraviesa la barquilla. Luna alarga la pata hacia la silueta con forma de trucha mientras se le humedece la naricilla. El abuelo ríe con ganas.
- Iluminación: Atmósfera etérea, vapor blanquecino y luz difusa de ensueño.
- Texto:
  - Diálogo: "¿Querías pescar en el cielo, pillina? ¡Las nubes solo están hechas de aire y gotas!"
  - Pensamiento: "¡Qué fresca y suave es la niebla de las alturas!"

[PÁGINA 6: LA BRÚJULA DORADA]
Resumen: El abuelo consulta una brújula antigua para orientar el rumbo.
[PÁGINA 6]
- Viñeta completa / Detalle en primer plano
- Escena clave: Las manos arrugadas y cariñosas del abuelo sosteniendo una brújula de bronce reluciente. Luna apoya una pata delantera sobre la esfera de cristal.
- Iluminación: Reflejos dorados del metal bajo el sol de la tarde.
- Texto:
  - Diálogo: "Esta brújula me la regaló mi padre hace sesenta años. Siempre señala hacia casa."
  - Pensamiento: "Con el abuelo al mando jamás tendré miedo a perderme."

[PÁGINA 7: EL VALLE DE LOS MOLINOS]
Resumen: El globo sobrevuela un río azul y viejos molinos de viento.
[PÁGINA 7]
- Viñeta completa / Gran plano panorámico cenital
- Escena clave: Vista espectacular desde la barquilla: campos de trigo amarillos, un río serpenteante y molinos girando sus aspas al viento.
- Iluminación: Tonos anaranjados y ocres de la caída de la tarde.
- Texto:
  - Diálogo: "Mira abajo, Luna. El mundo desde aquí parece una manta de parches de colores."
  - Pensamiento: "Qué grande y hermoso es el mundo cuando lo miras con calma."

[PÁGINA 8: LA PUESTA DE SOL MÁGICA]
Resumen: El cielo se vuelve púrpura y magenta mientras preparan el descenso.
[PÁGINA 8]
- Viñeta completa / Plano general frontal
- Escena clave: El sol gigantesco poniéndose en el horizonte. Las siluetas del abuelo y la gata recortadas contra un cielo espectacular de tonos fuego y violeta.
- Iluminación: Claroscuro crepuscular con tonos magenta, ámbar y sombras suaves.
- Texto:
  - Diálogo: "El día se acaba, compañera. Es hora de buscar un buen prado para descansar."
  - Pensamiento: "El cielo se ha vestido con los colores de un cuadro."

[PÁGINA 9: EL ATERRIZAJE ENTRE MARGARITAS]
Resumen: La cesta toca tierra suavemente en un claro verde.
[PÁGINA 9]
- Viñeta completa / Plano medio a ras de suelo
- Escena clave: La barquilla se posa entre flores silvestres. La tela del globo desciende despacio desinflándose. Luna salta al césped y huele una margarita.
- Iluminación: Luz serena del anochecer, cielo estrellándose en el horizonte.
- Texto:
  - Diálogo: "¡Misión cumplida! Bienvenidas sean las patas a tierra firme."
  - Pensamiento: "La hierba huele a menta y a tierra fresca."

[PÁGINA 10: REGRESO Y SUEÑO EN EL REGAZO]
Resumen: Junto a la chimenea de casa, el abuelo y Luna duermen felices.
[PÁGINA 10]
- Viñeta final / Plano íntimo acogedor
- Escena clave: El abuelo sentado en su sillón orejero con una taza de chocolate caliente. Luna duerme plácidamente hecha un ovillo en sus rodillas, ronroneando.
- Iluminación: Calidez del fuego de la chimenea con sombras tranquilas.
- Texto:
  - Diálogo: "Buenas noches, Luna. Mañana pensaremos cuál será nuestro próximo viaje."
  - Pensamiento: "En los brazos del abuelo todos los sueños vuelan alto."
"""

def build_all():
    print("🚀 Generando Fichas de la Clase Monográfica 3 idénticas a las ternas...")
    
    # 1. PASO 0
    create_pdf_ficha(
        "0. Paso_0_Introduccion_Proyecto.pdf",
        "PASO 0: PROYECTO CÓMIC ILUSTRADO",
        ""
    )
    
    # 2. PASO 1
    texto_edad = "INSTRUCCIÓN INICIAL OBLIGATORIA: Ajusta la complejidad narrativa, el vocabulario y el tono emocional estrictamente a su nivel cognitivo. Si es mayor de 6 años, elimina por completo cualquier tono excesivamente infantil o 'ñoño', añadiendo más aventura, misterio y dilemas maduros.\n\n"
    prompt_p1 = (
        f"{texto_edad}"
        f"Actúa como un cuentacuentos infantil profesional. Escribe un cuento de buenas noches de unos 3 o 4 párrafos sobre '{CUENTO_TITULO}'. "
        f"El cuento debe transmitir de forma sutil los valores de '{CUENTO_VALORES}'. "
        f"Usa un lenguaje mágico, visual y atrapante para un niño pequeño, y asegúrate de que el final sea tranquilo y reconfortante para ayudarle a dormir.\n\n"
        f"--- OPCIÓN B: PARA ALUMNOS CON MUCHA IMAGINACIÓN ---\n"
        f"Si ya tienes una idea genial en la cabeza y prefieres inventarte el cuento tú mismo, no dejes que la IA lo haga por ti. Escribe tu historia y usa este prompt alternativo para que Gemini actúe únicamente como tu \"editor literario\", dándole ese toque mágico de cuentacuentos:\n\n"
        f"PROMPT ALTERNATIVO:\n"
        f"Actúa como un cuentacuentos infantil profesional. A continuación te voy a pegar un cuento que he escrito yo mismo.\n\n"
        f"Necesito que lo reescribas manteniendo mi historia exacta, pero usando un lenguaje mucho más mágico, visual y atrapante para un niño pequeño.\n\n"
        f"Asegúrate de que el final sea tranquilo y reconfortante para ayudarle a dormir. Además, quiero que el cuento transmita sutilmente los siguientes valores: [{CUENTO_VALORES}].\n\n"
        f"Aquí tienes mi historia:\n"
        f"[PEGA AQUÍ EL TEXTO DE TU CUENTO INVENTADO]"
    )
    create_pdf_ficha(
        "1. Paso_1_Crear_el_Cuento.pdf",
        "PASO 1: CREAR EL CUENTO",
        prompt_p1
    )
    
    # 3. PASO 2
    create_pdf_ficha(
        "2. Paso_2_Generador_de_Guion.pdf",
        "PASO 2: GENERADOR DE GUION",
        PROMPT_PASO_2_GUION
    )
    
    # 4. PASO 3
    create_pdf_ficha(
        "3. Paso_3_Ilustrador_Visual.pdf",
        "PASO 3: ILUSTRADOR VISUAL",
        "",
        is_step2=True
    )
    
    # PDF del guion para quien prefiera subirlo como PDF a NotebookLM
    guion_pdf_path = os.path.join(TARGET_DIR, "EJEMPLO_A_FUENTE_GUION_PARA_NOTEBOOKLM.pdf")
    doc_g = SimpleDocTemplate(guion_pdf_path, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    st_title = ParagraphStyle('GTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=14, textColor=colors.HexColor('#2C3E50'), spaceAfter=12)
    st_body = ParagraphStyle('GBody', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#333333'))
    
    st_story = [Paragraph(f"GUION DE CÓMIC: {CUENTO_TITULO.upper()}", st_title), HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2C3E50'), spaceAfter=10)]
    for line in GUION_10_PAGINAS_EJEMPLO.split("\n"):
        if line.startswith("[PÁGINA"):
            st_story.append(Spacer(1, 6))
            st_story.append(Paragraph(f"<b>{line}</b>", ParagraphStyle('Sub', parent=st_body, fontSize=10, textColor=colors.HexColor('#8B008B'))))
        elif line.strip():
            st_story.append(Paragraph(line.replace('"', '&quot;'), st_body))
        else:
            st_story.append(Spacer(1, 3))
    doc_g.build(st_story)
    
    print("✅ Generados todos los archivos de la Clase Monográfica 3 correctamente.")

if __name__ == "__main__":
    build_all()
