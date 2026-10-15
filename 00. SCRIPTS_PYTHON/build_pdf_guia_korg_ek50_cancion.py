#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_guia_korg_ek50_cancion.py
Genera una guía didáctica en PDF vectorial de 2 páginas con diseño profesional para:
- Teclado: Korg EK-50
- Canción: «To All The Girls I've Loved Before»
- Ubicaciones de salida:
    1) CURSO MUSICA/GUIA_KORG_EK50_TO_ALL_THE_GIRLS.pdf
    2) CURSO MUSICA/CANCIONES PDF/GUIA_KORG_EK50_TO_ALL_THE_GIRLS.pdf
    3) CURSO-IA/SIMULADORES_INTERACTIVOS/05_ENTRENADOR_CLAVE_SOL/GUIA_KORG_EK50_TO_ALL_THE_GIRLS.pdf
"""

import os
import zlib

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA"
DESTINOS = [
    os.path.join(BASE_DIR, "CURSO MUSICA", "GUIA_KORG_EK50_TO_ALL_THE_GIRLS.pdf"),
    os.path.join(BASE_DIR, "CURSO MUSICA", "CANCIONES PDF", "GUIA_KORG_EK50_TO_ALL_THE_GIRLS.pdf"),
    os.path.join(BASE_DIR, "CURSO-IA", "SIMULADORES_INTERACTIVOS", "05_ENTRENADOR_CLAVE_SOL", "GUIA_KORG_EK50_TO_ALL_THE_GIRLS.pdf"),
]

def pdf_escape(text):
    """Codifica texto UTF-8 a bytes WinAnsi (cp1252) escapados para PDF."""
    b = text.encode('cp1252', errors='replace')
    out = bytearray()
    for ch in b:
        if ch in (40, 41, 92):  # ( ) \
            out.append(92)
            out.append(ch)
        elif ch < 32 or ch > 126:
            out.extend(f"\\{ch:03o}".encode('ascii'))
        else:
            out.append(ch)
    return out.decode('ascii')

def hex_rgb(hex_str):
    h = hex_str.lstrip('#')
    return (int(h[0:2], 16) / 255.0, int(h[2:4], 16) / 255.0, int(h[4:6], 16) / 255.0)

def wrap_text(text, max_chars):
    words = text.split()
    lines = []
    curr = ""
    for w in words:
        if not curr:
            curr = w
        elif len(curr) + 1 + len(w) <= max_chars:
            curr += " " + w
        else:
            lines.append(curr)
            curr = w
    if curr:
        lines.append(curr)
    return lines

class PDFPageStream:
    def __init__(self, w=595.28, h=841.89):
        self.W = w
        self.H = h
        self.cmds = []

    def rect(self, x, y, w, h, fill_hex=None, stroke_hex=None, line_w=0.6, rx=0):
        self.cmds.append("q")
        self.cmds.append(f"{line_w:.2f} w")
        if fill_hex and stroke_hex:
            fr, fg, fb = hex_rgb(fill_hex)
            sr, sg, sb = hex_rgb(stroke_hex)
            self.cmds.append(f"{fr:.3f} {fg:.3f} {fb:.3f} rg {sr:.3f} {sg:.3f} {sb:.3f} RG")
            self.cmds.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re B")
        elif fill_hex:
            fr, fg, fb = hex_rgb(fill_hex)
            self.cmds.append(f"{fr:.3f} {fg:.3f} {fb:.3f} rg")
            self.cmds.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re f")
        elif stroke_hex:
            sr, sg, sb = hex_rgb(stroke_hex)
            self.cmds.append(f"{sr:.3f} {sg:.3f} {sb:.3f} RG")
            self.cmds.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re S")
        self.cmds.append("Q")

    def line(self, x1, y1, x2, y2, stroke_hex="#CBD5E1", line_w=0.6):
        sr, sg, sb = hex_rgb(stroke_hex)
        self.cmds.append("q")
        self.cmds.append(f"{line_w:.2f} w {sr:.3f} {sg:.3f} {sb:.3f} RG")
        self.cmds.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")
        self.cmds.append("Q")

    def text(self, x, y, txt, font="F1", size=9.5, color_hex="#0F172A"):
        r, g, b = hex_rgb(color_hex)
        esc = pdf_escape(txt)
        self.cmds.append("q")
        self.cmds.append(f"{r:.3f} {g:.3f} {b:.3f} rg")
        self.cmds.append(f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({esc}) Tj ET")
        self.cmds.append("Q")

    def get_bytes(self):
        return "\n".join(self.cmds).encode('latin1')

def generate_page_1():
    p = PDFPageStream()
    m = 28.0
    cw = p.W - 2 * m
    y = p.H - 24.0

    # 1. ENCABEZADO PRINCIPAL (AZUL MARINO MUSICAL)
    hdr_h = 56.0
    p.rect(m, y - hdr_h, cw, hdr_h, fill_hex="#1E3A8A")
    p.text(m + 14, y - 20, "GUIA DE ESTUDIO Y CONFIGURACION: KORG EK-50", font="F2", size=15.0, color_hex="#FFFFFF")
    p.text(m + 14, y - 36, "Cancion: 'To All The Girls I've Loved Before' (Julio Iglesias & Willie Nelson)", font="F2", size=11.0, color_hex="#93C5FD")
    p.text(m + 14, y - 48, "Metodo progresivo: Teclado fisico Korg EK-50 + Entrenador interactivo Clave de Sol Web", font="F1", size=8.5, color_hex="#E0E7FF")
    y -= (hdr_h + 10.0)

    # 2. CUADRO DE PARAMETROS MAESTROS (4 COLUMNAS)
    cards_h = 36.0
    col_w = (cw - 18.0) / 4.0
    labels = [
        ("TONALIDAD FACIL", "Sol Mayor (G)", "#047857", "#ECFDF5", "#A7F3D0"),
        ("RITMO / STYLE", "039 Country / 041 Ballad", "#1D4ED8", "#EFF6FF", "#BFDBFE"),
        ("TEMPO RECOMENDADO", "78 BPM (Rango 76-80)", "#B45309", "#FFFBEB", "#FDE68A"),
        ("SONIDO (KEYBOARD SET)", "Piano & Strings / Guitar", "#6D28D9", "#F5F3FF", "#DDD6FE"),
    ]
    for i, (tit, val, text_c, fill_c, stroke_c) in enumerate(labels):
        cx = m + i * (col_w + 6.0)
        p.rect(cx, y - cards_h, col_w, cards_h, fill_hex=fill_c, stroke_hex=stroke_c, line_w=0.8)
        p.text(cx + 6, y - 13, tit, font="F2", size=7.2, color_hex=text_c)
        p.text(cx + 6, y - 26, val, font="F2", size=8.2, color_hex="#0F172A")
    y -= (cards_h + 12.0)

    # 3. BLOQUE PASO A PASO EN EL KORG EK-50
    sec_h = 18.0
    p.rect(m, y - sec_h, cw, sec_h, fill_hex="#0F172A")
    p.text(m + 8, y - 13, "1. PASO A PASO: COMO CONFIGURAR TU KORG EK-50 EN 30 SEGUNDOS", font="F2", size=9.5, color_hex="#FFFFFF")
    y -= (sec_h + 8.0)

    pasos = [
        ("PASO 1", "Elegir el Ritmo (Style)", "Pulsa el boton STYLE y teclea 039 en el teclado numerico (Country Bld). Tambien puedes usar el 041 (Love Ballad). El ritmo incorpora bateria suave y guitarras acusticas que acompanan automaticamente."),
        ("PASO 2", "Ajustar el Tempo Exacto a 78 BPM", "Manten presionado el boton [SHIFT] con la mano izquierda y, SIN SOLTARLO, gira la rueda grande (DIAL) con la derecha hasta ver 78 BPM en la pantalla. Al soltar SHIFT queda fijado. (NO usar golpes de Tap Tempo)."),
        ("PASO 3", "Activar el Acompanamiento Automatico", "Pulsa el boton [ACMP / STYLE] para que la luz quede encendida. Esto indica que cuando toques las teclas graves con la mano izquierda, el Korg generara todo el arreglo instrumental en tiempo real."),
        ("PASO 4", "Dividir el Teclado en 2 Secciones (Split)", "Pulsa el boton [SPLIT]. El teclado se divide en el Do central (Do4): las 2 octavas de la izquierda quedan para tocar los acordes, y las 3 octavas de la derecha quedan para la melodia principal."),
        ("PASO 5", "Asignar el Sonido Optimo (STS / Keyboard Set)", "Manten pulsado [SHIFT] + [KEYBOARD SET] para activar la funcion STS ligada al ritmo. Elige el Set 1 o 2 para tener Piano con Violines de fondo (Piano & Strings) o Guitarra con cuerdas calidas."),
    ]

    for code, tit, desc in pasos:
        box_h = 32.0
        p.rect(m, y - box_h, cw, box_h, fill_hex="#F8FAFC", stroke_hex="#CBD5E1", line_w=0.6)
        # Badge paso
        p.rect(m + 6, y - 22, 44, 14, fill_hex="#2563EB")
        p.text(m + 10, y - 18, code, font="F2", size=7.8, color_hex="#FFFFFF")
        # Titulo paso
        p.text(m + 56, y - 12, tit, font="F2", size=8.8, color_hex="#1E293B")
        # Descripcion
        lines = wrap_text(desc, 106)
        for li, ltxt in enumerate(lines[:2]):
            p.text(m + 56, y - 22 - (li * 8.5), ltxt, font="F1", size=7.6, color_hex="#475569")
        y -= (box_h + 5.0)

    y -= 6.0

    # 4. BLOQUE SOLUCION DE PROBLEMAS FRECUENTES
    sec2_h = 18.0
    p.rect(m, y - sec2_h, cw, sec2_h, fill_hex="#991B1B")
    p.text(m + 8, y - 13, "2. RESOLUCION DE DUDAS Y PROBLEMAS FRECUENTES EN EL PANEL DEL KORG", font="F2", size=9.5, color_hex="#FFFFFF")
    y -= (sec2_h + 8.0)

    dudas = [
        ("¿Por que al pulsar Tempo me salian numeros raros como 38, 67 o 101?", "El boton fisico es TAP TEMPO. Calcula los BPM midiendo el tiempo entre los golpes de tu dedo. Si das dos toques lentos da 38 o 67; si los das rapidos salta a 104. Solucion: No golpees el boton; usa SHIFT + DIAL."),
        ("¿Por que el tempo no sube ni baja al girar la rueda?", "Verifica si hay un pequeno icono de candado (candado de Tempo Lock) en la pantalla. Si esta activo, el tempo esta congelado. Para quitarlo: pulsa [SHIFT] + [TAP TEMPO] una vez y el candado desaparecera."),
        ("¿Por que se encienden UPPER 1 y UPPER 2 al pulsar SHIFT + KEYBOARD SET?", "No son 'Set 1 y 2', sino capas simultaneas (Layers). El Korg mezcla a la vez Upper 1 (sonido principal) y Upper 2 (violines de fondo). Al pulsar una sola tecla suenan ambos timbres juntos para darle un sonido orquestal completo."),
        ("¿Como poner Piano o Guitarra en UPPER 1 manteniendo los violines en UPPER 2?", "Manten presionado [SHIFT] y pulsa el boton [UPPER 1] (parpadeara en pantalla). Gira la rueda (DIAL) para elegir Grand Piano o Ac. Guitar. Pulsa [SHIFT] para confirmar. Ahora tendras tu piano o guitarra solista con el colchon de violines de fondo."),
        ("¿Como elegir otro Keyboard Set o dejar solo el piano sin violines?", "Para cambiar sonido: pulsa [KEYBOARD SET] (sin Shift) y gira la rueda (DIAL) para explorar. Para quitar los violines y dejar solo piano: pulsa el boton fisico [UPPER 2] para apagar su luz (dejando solo UPPER 1 activo)."),
        ("¿Se sale de STS al pulsar Keyboard Set? ¿Puedo usar otras combinaciones?", "¡Si, y es estupendo! Cada uno de los 170+ Keyboard Sets es en si una combinacion ya preparada. Tu ritmo sigue tocando igual, pero ahora eres libre: si marcas el Set 005 tendras 'Piano & Str.' (Piano en Upper 1 y Cuerdas en Upper 2 ya perfectamente calibrados)."),
        ("¿Cuantos STS hay y como se diferencian de los 702 sonidos individuales?", "Hay 280 STS (1 para cada uno de los 280 estilos). En el Korg hay 3 niveles: 1) 702 Sounds individuales (de 1 en 1). 2) 170+ Keyboard Sets combinados (como el 005 Piano&Str o el 081 Trompeta&Trombon impresos en el chasis). 3) 280 STS asociados a cada ritmo. Estan detallados en el catalogo oficial Voice Name List de Korg."),
        ("¿Como lograr el maximo conjunto de violines de pelicula con Upper 1, 2 y 3?", "Enciende las 3 luces: [UPPER 1], [UPPER 2] y [UPPER 3]. Con [SHIFT] + cada boton pon: Upper 1 = St. Strings (brillante arriba), Upper 2 = StringsEns (ensamble orquestal en el medio) y Upper 3 = Analog Str. o Cello (peso grave abajo). ¡Sonara una orquesta sinfonica de cine masiva!"),
        ("¿Por que al girar la rueda me cambia el numero de ritmo en vez del tempo?", "Ocurre si sueltas el boton [SHIFT] antes de girar. La combinacion es simultanea: mantener apretado SHIFT con una mano mientras la otra gira la rueda. Al soltar SHIFT, la rueda vuelve a su funcion normal."),
        ("¿Como subir una octava completa (+12) sin alterar el tono de la cancion?", "¡Los botones de Transporte tienen la funcion de Octava con SHIFT! Manten presionado [SHIFT] y pulsa [TRANSPOSE # / OCTAVE +] para subir 1 octava completa (+12 semitonos). Para bajarla usa [OCTAVE -]. Y para mover el Split: manten pulsado [SPLIT] y toca la tecla deseada."),
        ("¿Como salir del modo KEYBOARD SET para elegir sonidos individuales (por que no se apaga)?", "El boton KEYBOARD SET no es un on/off, es un modo del panel (igual que STYLE o SONG). Para elegir entre los 702 sonidos individuales NO apagues nada: manten pulsado [SHIFT] y pulsa [UPPER 1] (parpadeara en pantalla). Ahi la rueda recorre directamente los 702 sonidos de 1 en 1. Pulsa [SHIFT] para fijar."),
        ("¿A partir de que numero empiezan los Strings y donde esta Stereo Strings?", "Con [SHIFT] + [UPPER 1/2/3], los violines empiezan en el numero 040 (Solo Violin, Viola, Cello...). El gran sonido orquestal amplio es el 048: St. Strings (Stereo Strings). En Keyboard Sets completos van del 096 en adelante. Atajo: usa los botones CATEGORY para saltar directo a Strings."),
        ("¿Para que sirve volver al tempo de fabrica?", "Si mantienes pulsados a la vez los botones [+] y [-], el teclado vuelve instantaneamente al tempo predeterminado del estilo seleccionado (76 BPM para 039 Country Bld, 80 BPM para 041 Love Ballad)."),
    ]

    for p_tit, p_desc in dudas:
        d_box_h = 28.0
        p.rect(m, y - d_box_h, cw, d_box_h, fill_hex="#FEF2F2", stroke_hex="#FECACA", line_w=0.6)
        p.text(m + 8, y - 11, p_tit, font="F2", size=8.0, color_hex="#991B1B")
        lines = wrap_text(p_desc, 114)
        for li, ltxt in enumerate(lines[:2]):
            p.text(m + 8, y - 20 - (li * 8.0), ltxt, font="F1", size=7.4, color_hex="#334155")
        y -= (d_box_h + 4.5)

    # Pie de pagina 1
    p.line(m, 32.0, p.W - m, 32.0, stroke_hex="#CBD5E1", line_w=0.5)
    p.text(m, 22.0, "Curso de Musica y Tecnologia · Korg EK-50 · Pagina 1 de 2", font="F1", size=7.5, color_hex="#64748B")
    p.text(p.W - m - 120, 22.0, "Ficha de Estudio y Configuracion", font="F2", size=7.5, color_hex="#1E3A8A")

    return p.get_bytes()


def generate_page_2():
    p = PDFPageStream()
    m = 28.0
    cw = p.W - 2 * m
    y = p.H - 24.0

    # 1. ENCABEZADO PAGINA 2
    hdr_h = 42.0
    p.rect(m, y - hdr_h, cw, hdr_h, fill_hex="#047857")
    p.text(m + 14, y - 18, "ARMONIA DE LA CANCION Y ENTRENADOR VIRTUAL CLAVE DE SOL", font="F2", size=13.5, color_hex="#FFFFFF")
    p.text(m + 14, y - 32, "Mano izquierda (3 acordes basicos) + Mano derecha (melodia guiada en navegador)", font="F1", size=9.0, color_hex="#D1FAE5")
    y -= (hdr_h + 12.0)

    # 2. SECCION: LOS 3 ACORDES EN SOL MAYOR
    sec_h = 18.0
    p.rect(m, y - sec_h, cw, sec_h, fill_hex="#065F46")
    p.text(m + 8, y - 13, "3. MANO IZQUIERDA: DIGITACIONES COMODAS SIN MOVER LA MANO (TONALIDAD SOL MAYOR)", font="F2", size=9.5, color_hex="#FFFFFF")
    y -= (sec_h + 8.0)

    # 3 Tarjetas de acordes
    card_chord_w = (cw - 12.0) / 3.0
    chord_info = [
        ("SOL MAYOR (G)", "Acorde de Reposo / Tonica", "Notas: Sol - Si - Re", "Dedos: 5 (menique), 3 (corazon), 1 (pulgar)", "Posicion base: el acorde de salida y llegada que da sensacion de hogar y paz.", "#047857", "#F0FDF4", "#BBF7D0"),
        ("LA MENOR (Am)", "Acorde de Paso Melancolico", "Notas: Do - Mi - La  (Inversion)", "Dedos: 5 (Do), 3 (Mi), 1 (La)", "Inversion comoda: subes un poquito los dedos manteniendo la postura sin saltar.", "#1D4ED8", "#EFF6FF", "#BFDBFE"),
        ("RE SEPTIMA (D7)", "Acorde de Tension / Dominante", "Notas: Fa# - Do - Re  (Inversion)", "Dedos: 5 (Fa# tecla negra), 2 (Do), 1 (Re)", "¡Magia de digitacion!: Solo mueves el menique a Fa# y el indice a Do. ¡Sin esfuerzo!", "#B45309", "#FFFBEB", "#FDE68A"),
    ]

    for i, (tit, sub, notas, dedos, desc, col, fill, strk) in enumerate(chord_info):
        cx = m + i * (card_chord_w + 6.0)
        ch_h = 76.0
        p.rect(cx, y - ch_h, card_chord_w, ch_h, fill_hex=fill, stroke_hex=strk, line_w=0.8)
        p.text(cx + 8, y - 14, tit, font="F2", size=9.5, color_hex=col)
        p.text(cx + 8, y - 25, sub, font="F1", size=7.2, color_hex="#64748B")
        p.rect(cx + 6, y - 41, card_chord_w - 12, 13, fill_hex="#FFFFFF", stroke_hex=strk, line_w=0.5)
        p.text(cx + 10, y - 37, notas, font="F2", size=7.8, color_hex="#0F172A")
        p.text(cx + 8, y - 52, dedos, font="F2", size=6.8, color_hex="#334155")
        lines = wrap_text(desc, 32)
        for li, lt in enumerate(lines[:2]):
            p.text(cx + 8, y - 62 - (li * 7.5), lt, font="F1", size=6.8, color_hex="#475569")
    y -= (76.0 + 12.0)

    # 3. ESQUEMA DE COMPASES DE LA ESTROFA
    p.rect(m, y - 16.0, cw, 16.0, fill_hex="#1E293B")
    p.text(m + 8, y - 11.5, "ESTRUCTURA DE COMPASES DE LA ESTROFA (Cada casilla = 1 compas de 4 tiempos)", font="F2", size=8.5, color_hex="#FFFFFF")
    y -= (16.0 + 6.0)

    # 8 compases
    compas_w = (cw - 7.0 * 4.0) / 8.0
    compases = [
        ("Compas 1", "G", "Sol Mayor", "#F0FDF4", "#047857"),
        ("Compas 2", "G", "Sol Mayor", "#F0FDF4", "#047857"),
        ("Compas 3", "Am", "La menor", "#EFF6FF", "#1D4ED8"),
        ("Compas 4", "Am", "La menor", "#EFF6FF", "#1D4ED8"),
        ("Compas 5", "D7", "Re septima", "#FFFBEB", "#B45309"),
        ("Compas 6", "D7", "Re septima", "#FFFBEB", "#B45309"),
        ("Compas 7", "G", "Sol Mayor", "#F0FDF4", "#047857"),
        ("Compas 8", "G", "Sol Mayor", "#F0FDF4", "#047857"),
    ]
    for i, (c_num, c_acorde, c_nom, c_fill, c_col) in enumerate(compases):
        cx = m + i * (compas_w + 4.0)
        c_h = 36.0
        p.rect(cx, y - c_h, compas_w, c_h, fill_hex=c_fill, stroke_hex=c_col, line_w=0.8)
        p.text(cx + 6, y - 11, c_num, font="F1", size=6.5, color_hex="#64748B")
        p.text(cx + 12, y - 24, c_acorde, font="F2", size=11.5, color_hex=c_col)
        p.text(cx + 6, y - 32, c_nom, font="F1", size=6.2, color_hex="#334155")
    y -= (36.0 + 12.0)

    # 4. SECCION ENTRENADOR CLAVE DE SOL (WEB MIDI)
    sec3_h = 18.0
    p.rect(m, y - sec3_h, cw, sec3_h, fill_hex="#1E3A8A")
    p.text(m + 8, y - 13, "4. MANO DERECHA: APRENDER LA MELODIA CON EL ENTRENADOR DE CLAVE DE SOL", font="F2", size=9.5, color_hex="#FFFFFF")
    y -= (sec3_h + 8.0)

    app_steps = [
        ("CONECTAR", "Cable USB Korg EK-50 a Mac/iPad", "Conecta el cable USB del teclado a tu Mac o iPad. En Google Chrome la conexion Web MIDI se reconoce de forma instantanea sin instalar drivers."),
        ("MODO", "Aprender Cancion MIDI (Espera)", "En el menu desplegable de la aplicacion, selecciona el modo 'Aprender Cancion MIDI (Me sigue a mi / Espera)'. La partitura no avanza hasta que toques la nota correcta."),
        ("CANCION", "🌹 To All The Girls I've Loved Before", "En el selector de presets MIDI, elige la cancion. Aparecera la melodia en clave de sol con pentagrama en tiempo real y digitacion sugerida."),
        ("TEMPO APP", "Casilla interactiva de BPM", "Hemos incorporado un control numerico directo [⏱️ 78] en la app: puedes escribir 60 BPM para estudiar muy despacio, o 78 BPM para velocidad normal de concierto."),
    ]

    for c_badge, c_tit, c_txt in app_steps:
        box_h = 27.0
        p.rect(m, y - box_h, cw, box_h, fill_hex="#F8FAFC", stroke_hex="#CBD5E1", line_w=0.6)
        p.rect(m + 6, y - 20, 52, 13, fill_hex="#3B82F6")
        p.text(m + 9, y - 16, c_badge, font="F2", size=7.2, color_hex="#FFFFFF")
        p.text(m + 64, y - 12, c_tit, font="F2", size=8.4, color_hex="#1E293B")
        lines = wrap_text(c_txt, 102)
        for li, lt in enumerate(lines[:2]):
            p.text(m + 64, y - 20 - (li * 7.5), lt, font="F1", size=7.3, color_hex="#475569")
        y -= (box_h + 5.0)

    y -= 5.0

    # 5. METODO DIDACTICO EN 3 NIVELES
    p.rect(m, y - 16.0, cw, 16.0, fill_hex="#334155")
    p.text(m + 8, y - 11.5, "PLAN DE ESTUDIO EN 3 NIVELES DE PROGRESION", font="F2", size=8.5, color_hex="#FFFFFF")
    y -= (16.0 + 6.0)

    niveles = [
        ("NIVEL 1 (Solo Mano Izq)", "Practica cambiar entre G -> Am -> D7 manteniendo cada acorde 4 tiempos con el ritmo 039 encendido."),
        ("NIVEL 2 (Solo Mano Der)", "Sigue las notas de la partitura en el Entrenador Web nota a nota hasta memorizar la melodia de la estrofa."),
        ("NIVEL 3 (Manos Juntas)", "A 60 BPM (muy despacio), pulsa el acorde de la izquierda en el tiempo 1 y canta o toca la melodia a la vez."),
    ]
    for n_tit, n_desc in niveles:
        p.rect(m, y - 16.0, cw, 16.0, fill_hex="#F1F5F9", stroke_hex="#E2E8F0", line_w=0.5)
        p.text(m + 8, y - 11.5, n_tit + ":", font="F2", size=7.6, color_hex="#0F172A")
        p.text(m + 130, y - 11.5, n_desc, font="F1", size=7.4, color_hex="#334155")
        y -= 19.0

    # Pie de pagina 2
    p.line(m, 32.0, p.W - m, 32.0, stroke_hex="#CBD5E1", line_w=0.5)
    p.text(m, 22.0, "Curso de Musica y Tecnologia · Korg EK-50 · Pagina 2 de 2", font="F1", size=7.5, color_hex="#64748B")
    p.text(p.W - m - 120, 22.0, "Ficha de Estudio y Configuracion", font="F2", size=7.5, color_hex="#047857")

    return p.get_bytes()


def build_full_pdf():
    W, H = 595.28, 841.89
    stream1 = generate_page_1()
    stream2 = generate_page_2()

    comp1 = zlib.compress(stream1)
    comp2 = zlib.compress(stream2)

    objs = []
    # 1: Catalog
    objs.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    # 2: Pages
    objs.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R 7 0 R] /Count 2 >>\nendobj\n")
    # 3: Page 1
    objs.append(f"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W:.2f} {H:.2f}] /Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> /Contents 6 0 R >>\nendobj\n".encode("latin1"))
    # 4: F1 Helvetica
    objs.append(b"4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>\nendobj\n")
    # 5: F2 Helvetica-Bold
    objs.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>\nendobj\n")
    # 6: Stream 1
    objs.append(f"6 0 obj\n<< /Length {len(comp1)} /Filter /FlateDecode >>\nstream\n".encode("latin1") + comp1 + b"\nendstream\nendobj\n")
    # 7: Page 2
    objs.append(f"7 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W:.2f} {H:.2f}] /Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> /Contents 8 0 R >>\nendobj\n".encode("latin1"))
    # 8: Stream 2
    objs.append(f"8 0 obj\n<< /Length {len(comp2)} /Filter /FlateDecode >>\nstream\n".encode("latin1") + comp2 + b"\nendstream\nendobj\n")

    pdf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for o in objs:
        offsets.append(len(pdf))
        pdf.extend(o)
    xref_pos = len(pdf)
    pdf.extend(f"xref\n0 {len(objs)+1}\n0000000000 65535 f \n".encode("latin1"))
    for off in offsets[1:]:
        pdf.extend(f"{off:010d} 00000 n \n".encode("latin1"))
    pdf.extend(f"trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode("latin1"))

    # Guardar en todos los destinos solicitados
    for dest in DESTINOS:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as f:
            f.write(pdf)
        print(f"✅ PDF generado con exito ({len(pdf)} bytes) en: {dest}")

if __name__ == "__main__":
    build_full_pdf()
