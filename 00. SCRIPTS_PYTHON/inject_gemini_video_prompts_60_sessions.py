# -*- coding: utf-8 -*-
"""
Script Maestro: Inyección de Retos de Vídeo de 10 Segundos en Gemini en las 60 Sesiones.
Flujo 100% conversacional continuo (sin descargas ni subidas de archivos).
Rotación equilibrada entre 6 categorías: [EST], [NAT], [CUENT], [FUT], [MEM], [ARTE].
"""

import os
import re
import sys
import shutil
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT_BASE = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF")
SESSIONS_DIR = os.path.join(EXPORT_BASE, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

sys.path.append(os.path.join(ROOT_DIR, "00. SCRIPTS_PYTHON"))
import build_repositorio_maestro as b

# Mapeo de las 60 sesiones: (Etiqueta_Prefijo, Id_Code, Prompt_Video)
VIDEO_CHALLENGES_60 = {
    1: ("2. EST", "[EST-001]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde se aprecie la luz del faro girando suavemente y las olas del mar rompiendo contra las rocas con espuma blanca."),
    2: ("7. NAT", "[NAT-002]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos mostrando al leopardo avanzando sigilosamente a cámara lenta entre la hierba alta de la sabana."),
    3: ("11.CUENT", "[CUENT-003]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde las carabelas naveguen sobre el océano azul con las velas hinchadas por el viento."),
    4: ("6. FUT", "[FUT-004]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el coche autónomo circule de noche por una avenida futurista iluminada por neones."),
    5: ("13. MEM", "[MEM-005]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde las manos de los niños muevan con ilusión las fichas de madera sobre el tablero de parchís."),
    6: ("8. ARTE", "[ARTE-006]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la niebla fluya como un mar blanco entre las montañas bajo el viento."),
    7: ("2. EST", "[EST-007]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde los carruajes y transeúntes crucen el arco monumental bajo una suave lluvia."),
    8: ("7. NAT", "[NAT-008]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos mostrando al águila desplegar sus alas y emprender el vuelo sobre las montañas nevadas."),
    9: ("11.CUENT", "[CUENT-009]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la avioneta bimotor vuele entre nubes de algodón doradas al atardecer."),
    10: ("6. FUT", "[FUT-010]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde un rover lunar avance levantando polvo sobre la superficie con la Tierra brillando al fondo."),
    11: ("13. MEM", "[MEM-011]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la rueda de afilar gire despidiendo chispas brillantes mientras el afilador trabaja."),
    12: ("8. ARTE", "[ARTE-012]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la joven parpadee con suavidad y sonría con misterio bajo la luz tenue de la ventana."),
    13: ("2. EST", "[EST-013]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el agua de lluvia corra por los adoquines medievales reflejando los faroles antiguos."),
    14: ("7. NAT", "[NAT-014]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el águila descienda en planeo majestuoso con sus plumas vibrando con el aire."),
    15: ("11.CUENT", "[CUENT-015]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos mostrando la primera pisada del astronauta en cámara lenta sobre la superficie lunar."),
    16: ("6. FUT", "[FUT-016]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la cabina del ascensor ascienda a lo largo del cable gigante saliendo de la atmósfera terrestre."),
    17: ("13. MEM", "[MEM-017]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde los periódicos colgados se muevan con el viento y un cliente compre el tebeo con una sonrisa."),
    18: ("8. ARTE", "[ARTE-018]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el haz de luz dorada entre por la ventana iluminando el polvo en suspensión de la estancia."),
    19: ("2. EST", "[EST-019]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el dirigible gigante surque el cielo entre las nubes con sus hélices girando."),
    20: ("7. NAT", "[NAT-020]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el cóndor planee en círculos sobre los picos nevados de la cordillera andina."),
    21: ("11.CUENT", "[CUENT-021]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la caravana de camellos avance lentamente por las dunas doradas del desierto."),
    22: ("6. FUT", "[FUT-022]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde las cúpulas aerostáticas se mezan suavemente sobre el mar de nubes del planeta."),
    23: ("13. MEM", "[MEM-023]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el sereno camine por la acera empedrada con su farol titilando en la noche."),
    24: ("8. ARTE", "[ARTE-024]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde las ondas del agua del puerto reflejen el sol rojo mientras una barca rema despacio."),
    25: ("2. EST", "[EST-025]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde las esferas de cristal giren lentamente proyectando destellos de arcoíris en la estancia."),
    26: ("7. NAT", "[NAT-026]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el tiburón nade de forma imponente a través de las aguas cristalinas del arrecife."),
    27: ("11.CUENT", "[CUENT-027]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el dragón baje la cabeza dócilmente para que la princesa acaricie sus escamas."),
    28: ("6. FUT", "[FUT-028]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la locomotora vuele entre las nubes soltando chorros de vapor y con sus engranajes de bronce girando."),
    29: ("13. MEM", "[MEM-029]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el tranvía rojo avance sobre los raíles haciendo sonar su campana."),
    30: ("8. ARTE", "[ARTE-030]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde las góndolas naveguen por el canal con el agua meciéndose contra los palacios de mármol."),
    31: ("2. EST", "[EST-031]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde las cascadas caigan con fuerza por el acantilado hacia el mar."),
    32: ("7. NAT", "[NAT-032]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el canguro dé saltos ágiles por la tierra roja australiana levantando polvo."),
    33: ("11.CUENT", "[CUENT-033]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el prototipo de alas mecánicas de Leonardo bata en el aire sobre las colinas de Florencia."),
    34: ("6. FUT", "[FUT-034]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el coche volador cromado despegue en vertical y vuele entre rascacielos retrofuturistas."),
    35: ("13. MEM", "[MEM-035]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la aguja de la máquina suba y baje con ritmo preciso mientras la tela de flores avanza."),
    36: ("8. ARTE", "[ARTE-036]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde los bocetos de pergamino sobre la mesa se agiten levemente con el viento de la ventana."),
    37: ("2. EST", "[EST-037]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la lluvia caiga sobre los paraguas transparentes y los neones parpadeen."),
    38: ("7. NAT", "[NAT-038]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la ballena emerja del océano, expulse un chorro de vapor y vuelva a sumergir su cola."),
    39: ("11.CUENT", "[CUENT-039]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el llavero espacial flote dando vueltas en gravedad cero junto a la escotilla."),
    40: ("6. FUT", "[FUT-040]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la cápsula futurista cruce a toda velocidad el tubo transparente sobre el desierto."),
    41: ("13. MEM", "[MEM-041]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde una madre sople con cariño la rodilla raspada de su hijo antes de ponerle la tirita."),
    42: ("8. ARTE", "[ARTE-042]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde los remolinos azules y amarillos del cielo giren con vida sobre el pueblo dormido."),
    43: ("2. EST", "[EST-043]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde las líneas luminosas de la esfera fluyan y respiren con luz dorada."),
    44: ("7. NAT", "[NAT-044]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la ola se curve a cámara lenta formando un túnel de agua turquesa perfecta."),
    45: ("11.CUENT", "[CUENT-045]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde los dedos del niño toquen con agilidad las teclas del clavecín mientras sonríe a la corte."),
    46: ("7. NAT", "[NAT-046]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la lava incandescente fluya lentamente ladera abajo soltando chispas al cielo nocturno."),
    47: ("13. MEM", "[MEM-047]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el agua de la manguera riegue las matas de tomate haciendo brillar las gotas bajo el sol."),
    48: ("8. ARTE", "[ARTE-048]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde los motivos dorados de los mantos brillen con reflejos de luz mientras las flores del suelo se mecen."),
    49: ("2. EST", "[EST-049]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde los caballos al galope tiren del carro levantando una gran polvareda en la arena."),
    50: ("7. NAT", "[NAT-050]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde una pequeña hoja caiga sobre el agua cristalina creando círculos concéntricos perfectos."),
    51: ("11.CUENT", "[CUENT-051]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el tren avance entre abetos nevados con el humo blanco saliendo por la chimenea."),
    52: ("2. EST", "[EST-052]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el gato parpadee con suavidad, mueva con curiosidad las orejas y respire plácidamente."),
    53: ("13. MEM", "[MEM-053]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el joven aprendiz golpee con cuidado el metal candente en el yunque despidiendo chispas."),
    54: ("8. ARTE", "[ARTE-054]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde las manecillas de los relojes derretidos giren despacio bajo la luz del atardecer en Cadaqués."),
    55: ("2. EST", "[EST-055]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la silueta del lobo respire mientras las nubes y cascadas se mueven en su interior."),
    56: ("7. NAT", "[NAT-056]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde una mamá canguro asome a su cría de la bolsa y salte con potencia por la llanura."),
    57: ("11.CUENT", "[CUENT-057]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde decenas de operarios egipcios deslicen un bloque de piedra sobre troncos bajo el sol del desierto."),
    58: ("2. EST", "[EST-058]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde el coche deportivo acelere por la autopista luminosa hacia el sol morado del horizonte."),
    59: ("13. MEM", "[MEM-059]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde los vecinos sentados en sillas de mimbre conversen y se abaniquen bajo la luz de una farola."),
    60: ("8. ARTE", "[ARTE-060]", "A partir de esta imagen que acabas de generar arriba, crea un vídeo corto de 10 segundos donde la gran cresta de la ola se eleve con espuma y las barcas se deslicen sobre la corriente con el Monte Fuji sereno al fondo.")
}

def render_video_card(pdf_path, it, video_prompt):
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=45, leftMargin=45, topMargin=40, bottomMargin=40
    )
    styles = getSampleStyleSheet()

    block_name = it.get('block_name', 'BLOQUE DE PRÁCTICA CON IA')
    item_id = it.get('id_code', '')
    item_title = it.get('title', '')
    concept_text = it.get('concept', '')
    prompt_data = it.get('prompt', '')
    tips_text = it.get('tips', '')

    t_color = colors.HexColor('#005A9E')
    b_color = colors.HexColor('#F0F4F8')
    if "[ARTE-" in str(item_id):
        t_color = colors.HexColor('#8B4513')
        b_color = colors.HexColor('#FDFBF7')
    elif "[NAT-" in str(item_id):
        t_color = colors.HexColor('#0B6623')
        b_color = colors.HexColor('#F0F8F0')
    elif "[CUENT-" in str(item_id):
        t_color = colors.HexColor('#8E24AA')
        b_color = colors.HexColor('#F8F0FC')
    elif "[MEM-" in str(item_id):
        t_color = colors.HexColor('#B8860B')
        b_color = colors.HexColor('#FAF6E8')

    style_header = ParagraphStyle('H', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, textColor=t_color, spaceAfter=4, alignment=1)
    style_block = ParagraphStyle('B', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, textColor=colors.HexColor('#1A0A2E'), spaceAfter=10, alignment=1)
    style_title = ParagraphStyle('T', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=colors.HexColor('#1A0A2E'), spaceAfter=10)
    style_section_h = ParagraphStyle('SH', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=t_color, spaceBefore=8, spaceAfter=4)
    style_body = ParagraphStyle('Bd', parent=styles['BodyText'], fontName='Helvetica', fontSize=9.5, leading=14, textColor=colors.HexColor('#2C3E50'), spaceAfter=6)
    style_prompt = ParagraphStyle('Pr', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=9.5, leading=14, textColor=colors.HexColor('#1A0A2E'))
    style_reto = ParagraphStyle('Rt', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=14, textColor=colors.HexColor('#2C3E50'))

    style_vid_title = ParagraphStyle('VT', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=colors.HexColor('#004D40'))
    style_vid_inst = ParagraphStyle('VI', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=13.5, textColor=colors.HexColor('#1C2833'))
    style_vid_prompt = ParagraphStyle('VP', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=14, textColor=colors.HexColor('#005A9E'))
    style_vid_tip = ParagraphStyle('VTip', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=8.5, leading=12, textColor=colors.HexColor('#566573'))

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph(block_name.upper(), style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=t_color, spaceAfter=8))
    story.append(Paragraph(f"{item_id} {item_title}", style_title))

    if concept_text:
        story.append(Paragraph("💡 Contexto y Objetivo Didáctico", style_section_h))
        story.append(Paragraph(str(concept_text).replace('\n', '<br/>'), style_body))
        story.append(Spacer(1, 4))

    # Prompt principal
    story.append(Paragraph("🎨 Prompt Maestro para Crear tu Imagen en Gemini", style_section_h))
    p_rows = []
    raw_p_blocks = re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(prompt_data))
    for blk in raw_p_blocks:
        if not blk.strip(): continue
        for sub in re.split(r'\n|<br\s*/?>', blk):
            if sub.strip():
                p_rows.append([Paragraph(sub.strip(), style_prompt)])
    if not p_rows:
        p_rows = [[Paragraph(str(prompt_data), style_prompt)]]

    p_table = Table(p_rows, colWidths=[letter[0] - 90], splitByRow=1)
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), b_color),
        ('BORDER', (0,0), (-1,-1), 1.2, t_color),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 6))

    # Reto de Vídeo en la misma conversación
    story.append(Paragraph("🎬 Reto de Vídeo (10 segundos en Gemini)", style_section_h))
    v_rows = [
        [Paragraph("<b>¡Pon tu imagen en movimiento sin descargar nada!</b>", style_vid_title)],
        [Paragraph("En la <b>misma conversación de chat</b> de Gemini, justo después de ver la imagen que te acaba de generar arriba, escribe a continuación este segundo mensaje:", style_vid_inst)],
        [Paragraph(f"<b>«{video_prompt}»</b>", style_vid_prompt)],
        [Paragraph("💡 <i>Espera unos segundos a que Gemini procese la animación y pulsa el botón de reproducir para ver tu imagen cobrar vida.</i>", style_vid_tip)]
    ]
    v_table = Table(v_rows, colWidths=[letter[0] - 90], splitByRow=1)
    v_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#E0F2F1')),
        ('BORDER', (0,0), (-1,-1), 1.2, colors.HexColor('#00796B')),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(v_table)
    story.append(Spacer(1, 8))

    # Reto Práctico / Modificación opcional
    if tips_text:
        story.append(Paragraph("🧪 El Reto Práctico / Modificación Opcional", style_section_h))
        t_rows = []
        raw_t_blocks = re.split(r'\n\n|<br\s*/?>\s*<br\s*/?>', str(tips_text))
        for blk in raw_t_blocks:
            if not blk.strip(): continue
            for sub in re.split(r'\n|<br\s*/?>', blk):
                if sub.strip():
                    t_rows.append([Paragraph(sub.strip(), style_reto)])
        if not t_rows:
            t_rows = [[Paragraph(str(tips_text), style_reto)]]

        t_table = Table(t_rows, colWidths=[letter[0] - 90], splitByRow=1)
        t_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FAF5FF')),
            ('BORDER', (0,0), (-1,-1), 1, colors.HexColor('#8B008B')),
            ('PADDING', (0,0), (-1,-1), 5),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(t_table)
        story.append(Spacer(1, 6))

    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CBD5E1'), spaceAfter=6))
    story.append(Paragraph("<i>Material didáctico adaptado pedagógicamente para enriquecimiento digital y agilidad mental.</i>", ParagraphStyle('Ft', fontName='Helvetica-Oblique', fontSize=8, textColor=colors.HexColor('#7F8C8D'), alignment=1)))

    doc.build(story)

def purge_conflicts(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for d in dirs:
            if d.endswith(' 2') or d.endswith(' 3'):
                try: shutil.rmtree(os.path.join(root, d))
                except Exception: pass
        for f in files:
            if f.endswith(' 2.pdf') or f.endswith(' 3.pdf') or f.endswith(' 2.mp4') or f.endswith(' 3.mp4'):
                try: os.remove(os.path.join(root, f))
                except Exception: pass

def inject_all_video_prompts():
    print("🚀 Inyectando Retos de Vídeo de 10 segundos en Gemini (60 Sesiones)...")
    purge_conflicts(SESSIONS_DIR)

    items_by_id = {it['id_code']: it for it in b.classroom_export_items}
    total_injected = 0

    for s_idx in range(1, 61):
        prefix, item_id, v_prompt = VIDEO_CHALLENGES_60[s_idx]
        s_dir_name = f"{s_idx:02d}_Sesion" if s_idx < 60 else "60_Sesion_Cierre"
        target_dir = os.path.join(SESSIONS_DIR, s_dir_name)

        if not os.path.exists(target_dir):
            print(f"   ⚠️ Sesión {s_idx:02d}: No existe la carpeta {s_dir_name}")
            continue

        clean_code = item_id.replace('[','').replace(']','')
        files = [f for f in os.listdir(target_dir) if f.endswith('.pdf') and not re.search(r'\s[23]\.pdf$', f)]

        # Buscar el archivo correspondiente en la carpeta de la sesión
        matching_file = None
        if "CUENT" in item_id:
            # Preferir Paso_1 (narrativa e imagen)
            paso_1_candidates = [f for f in files if clean_code in f and "Paso_1" in f]
            if paso_1_candidates:
                matching_file = paso_1_candidates[0]
        
        if not matching_file:
            candidates = [f for f in files if clean_code in f]
            if candidates:
                matching_file = candidates[0]
            else:
                prefix_candidates = [f for f in files if f.startswith(prefix)]
                if prefix_candidates:
                    matching_file = prefix_candidates[0]

        if not matching_file:
            print(f"   ⚠️ Sesión {s_idx:02d}: No se encontró archivo para {prefix} {item_id} en {s_dir_name}")
            continue

        item_data = items_by_id.get(item_id)
        if not item_data:
            for it in b.classroom_export_items:
                if item_id in it.get('id_code', ''):
                    item_data = it
                    break

        if not item_data:
            print(f"   ⚠️ Sesión {s_idx:02d}: Datos no encontrados en catálogo para {item_id}")
            continue

        pdf_full_path = os.path.join(target_dir, matching_file)
        render_video_card(pdf_full_path, item_data, v_prompt)
        total_injected += 1
        print(f"   ✅ Sesión {s_idx:02d} [{s_dir_name}]: Inyectado Reto de Vídeo en {matching_file}")
    print(f"\n🎉 ¡Finalizado! Total de fichas con Reto de Vídeo actualizadas: {total_injected}/60")

if __name__ == "__main__":
    inject_all_video_prompts()
