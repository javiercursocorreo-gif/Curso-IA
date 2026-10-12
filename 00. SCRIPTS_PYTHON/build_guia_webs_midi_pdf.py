#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_guia_webs_midi_pdf.py
Genera en Python puro (sin dependencias externas, 100% compatible con Sandbox)
el documento PDF profesional:
  - CURSO-IA/GUIA_WEBS_DESCARGAR_MIDI_GRATIS.pdf
  - CURSO-IA/SIMULADORES_INTERACTIVOS/05_ENTRENADOR_CLAVE_SOL/GUIA_WEBS_DESCARGAR_MIDI_GRATIS.pdf
  - CURSO-IA/SIMULADORES_INTERACTIVOS/05_ENTRENADOR_CLAVE_SOL/ARCHIVOS_MIDI/GUIA_WEBS_DESCARGAR_MIDI_GRATIS.pdf
con enlaces clicables (anotaciones PDF /URI) a las mejores webs gratuitas para bajar archivos .MID / .MIDI.
"""

import os
import shutil

ROOT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
OUT_MAIN = os.path.join(ROOT_DIR, "GUIA_WEBS_DESCARGAR_MIDI_GRATIS.pdf")
OUT_CLAVE_SOL = os.path.join(
    ROOT_DIR, "SIMULADORES_INTERACTIVOS", "05_ENTRENADOR_CLAVE_SOL", "GUIA_WEBS_DESCARGAR_MIDI_GRATIS.pdf"
)
OUT_ARCHIVOS_MIDI = os.path.join(
    ROOT_DIR, "SIMULADORES_INTERACTIVOS", "05_ENTRENADOR_CLAVE_SOL", "ARCHIVOS_MIDI", "GUIA_WEBS_DESCARGAR_MIDI_GRATIS.pdf"
)


def pdf_escape(text):
    """Codifica texto UTF-8 a bytes WinAnsi (cp1252) escapados para literales PDF."""
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


class PurePDFCanvas:
    def __init__(self, width=595.28, height=841.89):
        self.W = width
        self.H = height
        self.cmds = []
        self.links = []  # (x1, y1, x2, y2, url)

    def rect_fill_stroke(self, x, y, w, h, fill_hex=None, stroke_hex=None, line_w=0.6):
        self.cmds.append("q")
        self.cmds.append(f"{line_w:.2f} w")
        if fill_hex and stroke_hex:
            fr, fg, fb = hex_rgb(fill_hex)
            sr, sg, sb = hex_rgb(stroke_hex)
            self.cmds.append(f"{fr:.3f} {fg:.3f} {fb:.3f} rg")
            self.cmds.append(f"{sr:.3f} {sg:.3f} {sb:.3f} RG")
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

    def add_link(self, x, y, w, h, url):
        self.links.append((x, y, x + w, y + h, url))

    def save(self, filepath):
        stream_data = "\n".join(self.cmds).encode('latin1')

        objects = []

        # 1: Catalog
        objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
        # 2: Pages
        objects.append(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")

        # Prepare link annotation object IDs (starting from 7)
        annot_ids = list(range(7, 7 + len(self.links)))
        annots_ref = " ".join(f"{aid} 0 R" for aid in annot_ids)
        annots_entry = f"/Annots [{annots_ref}]" if annot_ids else ""

        # 3: Page
        page_dict = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.W:.2f} {self.H:.2f}] "
            f"/Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> "
            f"/Contents 6 0 R {annots_entry} >>"
        ).encode('latin1')
        objects.append(page_dict)

        # 4: Font F1 (Helvetica)
        objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
        # 5: Font F2 (Helvetica-Bold)
        objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")

        # 6: Content Stream
        stream_obj = (
            f"<< /Length {len(stream_data)} >>\nstream\n".encode('latin1')
            + stream_data
            + b"\nendstream"
        )
        objects.append(stream_obj)

        # 7+: Link Annotations
        for (x1, y1, x2, y2, url) in self.links:
            annot_str = (
                f"<< /Type /Annot /Subtype /Link /Rect [{x1:.2f} {y1:.2f} {x2:.2f} {y2:.2f}] "
                f"/Border [0 0 0] /A << /Type /Action /S /URI /URI ({url}) >> >>"
            ).encode('latin1')
            objects.append(annot_str)

        # Assemble PDF
        out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = []
        for idx, obj_bytes in enumerate(objects, start=1):
            offsets.append(len(out))
            out.extend(f"{idx} 0 obj\n".encode('latin1'))
            out.extend(obj_bytes)
            out.extend(b"\nendobj\n")

        xref_pos = len(out)
        out.extend(f"xref\n0 {len(objects) + 1}\n".encode('latin1'))
        out.extend(b"0000000000 65535 f \n")
        for off in offsets:
            out.extend(f"{off:010d} 00000 n \n".encode('latin1'))

        out.extend(
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode('latin1')
        )

        with open(filepath, 'wb') as f:
            f.write(out)


def generate_midi_guide_pdf(out_path):
    c = PurePDFCanvas()
    margin = 28.0
    content_w = c.W - 2 * margin
    y = c.H - 24.0

    # 1. CABECERA AZUL REAL
    header_h = 46.0
    c.rect_fill_stroke(margin, y - header_h, content_w, header_h, fill_hex="#1E3A8A")
    c.text(margin + 14, y - 20, "GUÍA DE WEBS PARA DESCARGAR ARCHIVOS MIDI GRATIS (.MID)", font="F2", size=14.0, color_hex="#FFFFFF")
    c.text(
        margin + 14,
        y - 36,
        "Directorio de repositorios gratuitos para el Entrenador de Clave de Sol (Teclado MIDI, Voz e iPad) · Enlaces clicables",
        font="F1",
        size=8.8,
        color_hex="#DBEAFE"
    )
    y -= (header_h + 12.0)

    sections = [
        (
            "1. DESCARGA DIRECTA EN 1 CLIC (SIN REGISTRO · POP, CINE, SERIES Y TEMAS CONOCIDOS)",
            "#1E40AF",
            "#F8FAFC",
            [
                (
                    "1. BitMidi (+113.000 MIDIs)",
                    "https://bitmidi.com",
                    "Pop / Cine / Juegos / General",
                    "La más rápida y limpia. Buscador instantáneo con reproductor web de escucha previa y botón directo 'Download MIDI' sin registro. Ideal para melodías populares y bandas sonoras."
                ),
                (
                    "2. FreeMidi.org",
                    "https://freemidi.org",
                    "Pop / Rock / Éxitos / Bandas Sonoras",
                    "Catálogo organizado por géneros, décadas y artistas de la A a la Z. Excelente para encontrar canciones famosas de pop, rock, jazz, televisión y cine listas en formato .mid."
                ),
                (
                    "3. MidiWorld",
                    "https://www.midiworld.com",
                    "Clásica / Pop / Cine / Tradicional",
                    "Uno de los archivos históricos más completos de Internet. Incluye secciones específicas de compositores clásicos (Bach, Mozart, Beethoven) y temas de películas."
                ),
                (
                    "4. CoolMidi",
                    "https://www.coolmidi.com",
                    "Pop / TV / Melodías sencillas",
                    "Canciones organizadas por categorías con descarga directa gratuita. Muy útil para melodías vocales claras que funcionan muy bien en el pentagrama."
                ),
            ]
        ),
        (
            "2. MÚSICA CLÁSICA, PIANO Y PARTITURAS DIDÁCTICAS (ESPECIALES PARA CLAVE DE SOL)",
            "#0F766E",
            "#F0FDFA",
            [
                (
                    "5. 8notes.com (Especial Clave de Sol)",
                    "https://www.8notes.com/piano/",
                    "Didáctico / Principiantes / Melodías",
                    "¡La mejor para aprender! Filtra por instrumento (Piano, Flauta o Violín, que usan Clave de Sol) y nivel (Easy / Beginner). Permite bajar el archivo MIDI limpio de una sola línea melódica."
                ),
                (
                    "6. Kunst der Fuge",
                    "https://www.kunstderfuge.com",
                    "Música Clásica / Barroco / Romanticismo",
                    "La mayor enciclopedia mundial de música clásica en MIDI (+19.000 obras de Bach, Mozart, Chopin, Vivaldi). Permite descargar hasta 5 archivos diarios totalmente gratis."
                ),
                (
                    "7. ClassicalArchives (MIDIs)",
                    "https://www.classicalarchives.com/midi.html",
                    "Repertorio Clásico / Estudios de Piano",
                    "Gran colección de estudios de piano (Czerny, Burgmüller, Álbum de Ana Magdalena Bach) secuenciados con precisión rítmica para practicar lectura musical."
                ),
                (
                    "8. Mutopia Project",
                    "https://www.mutopiaproject.org",
                    "Dominio Público / Libre (CC0)",
                    "Biblioteca libre donde cada obra ofrece conjuntamente la partitura en PDF y su archivo .mid exacto para seguirlo en el Entrenador."
                ),
                (
                    "9. IMSLP (Petrucci Music Library)",
                    "https://imslp.org",
                    "Enciclopedia Mundial de Partituras",
                    "En la pestaña 'Arreglos y Transcripciones' o 'Sintetizados' de miles de obras clásicas incluye el fichero MIDI gratuito junto con la partitura original."
                ),
                (
                    "10. MuseScore.com",
                    "https://musescore.com",
                    "Partituras + Exportación a .MID",
                    "Millones de partituras. Las obras de Dominio Público (Public Domain) permiten bajar el .mid directo o abrirlas en el programa gratuito MuseScore Studio para exportar solo la mano derecha."
                ),
            ]
        ),
        (
            "3. MELODÍAS MONOFÓNICAS (UNA SOLA VOZ) Y MÚSICA DE VIDEOJUEGOS",
            "#6D28D9",
            "#F5F3FF",
            [
                (
                    "11. ABC Notation (+700.000 melodías)",
                    "https://abcnotation.com/search",
                    "Melodías de 1 sola línea (Clave de Sol)",
                    "Joya oculta para el Entrenador: buscador de melodías tradicionales y populares escritas a una sola voz (sin acordes complejos), por lo que sus MIDIs se ven limpísimos en el pentagrama."
                ),
                (
                    "12. VGMusic (Video Game Music)",
                    "https://www.vgmusic.com",
                    "Bandas Sonoras de Videojuegos (+30.000)",
                    "Archivo gratuito sin registro con más de 30.000 melodías míticas (Super Mario, Zelda, Tetris, etc.) muy motivadoras para practicar lectura y ritmo."
                ),
            ]
        ),
    ]

    col1_w = 195.0
    col2_w = content_w - col1_w

    for sec_title, sec_hex, row_bg_hex, items in sections:
        # Barra de título de sección
        sec_h = 17.0
        c.rect_fill_stroke(margin, y - sec_h, content_w, sec_h, fill_hex=sec_hex)
        c.text(margin + 8, y - 12.2, sec_title, font="F2", size=8.8, color_hex="#FFFFFF")
        y -= sec_h

        for name, url, cat, desc in items:
            desc_lines = wrap_text(desc, 64)
            row_h = max(36.0, 10.0 + len(desc_lines) * 10.5)

            # Fondo de fila y división vertical
            c.rect_fill_stroke(margin, y - row_h, content_w, row_h, fill_hex=row_bg_hex, stroke_hex="#CBD5E1", line_w=0.5)
            c.line(margin + col1_w, y, margin + col1_w, y - row_h, stroke_hex="#CBD5E1", line_w=0.5)

            # Columna izquierda: Nombre + URL clicable + Categoría
            c.text(margin + 7, y - 11.5, name, font="F2", size=8.8, color_hex="#0F172A")
            c.text(margin + 7, y - 22.0, url, font="F2", size=8.0, color_hex="#2563EB")
            # Subrayado de enlace y área clicable
            url_w = min(col1_w - 14, len(url) * 4.3)
            c.line(margin + 7, y - 23.5, margin + 7 + url_w, y - 23.5, stroke_hex="#2563EB", line_w=0.5)
            c.add_link(margin + 6, y - 25.0, col1_w - 12, 14.0, url)

            c.text(margin + 7, y - 32.0, cat, font="F1", size=7.3, color_hex="#64748B")

            # Columna derecha: Descripción envuelta
            ty = y - 11.5
            for dline in desc_lines:
                c.text(margin + col1_w + 8, ty, dline, font="F1", size=8.2, color_hex="#334155")
                ty -= 10.2

            y -= row_h

        y -= 8.0

    # 4. RECUADRO INFERIOR DE INSTRUCCIONES PRÁCTICAS
    box_h = 62.0
    c.rect_fill_stroke(margin, y - box_h, content_w, box_h, fill_hex="#FEF3C7", stroke_hex="#F59E0B", line_w=1.0)
    c.text(
        margin + 10,
        y - 13,
        "CÓMO USAR ESTOS ARCHIVOS .MID EN TU ENTRENADOR DE CLAVE DE SOL (MAC E IPAD):",
        font="F2",
        size=8.8,
        color_hex="#92400E"
    )
    tips = [
        "1. Guarda los ficheros .mid descargados en: SIMULADORES_INTERACTIVOS/05_ENTRENADOR_CLAVE_SOL/ARCHIVOS_MIDI/",
        "2. En el Entrenador de Clave de Sol, pulsa el botón 'Cargar .MID' (o arrastra el archivo sobre los pentagramas).",
        "3. Consejo didáctico: Elige preferiblemente piezas de instrumentos de una sola voz (Flauta, Violín, Voz o Piano",
        "   de nivel 'Easy/Beginner' en 8notes.com o abcnotation.com) para obtener una melodía limpia nota a nota."
    ]
    ty = y - 25.0
    for tline in tips:
        c.text(margin + 10, ty, tline, font="F1", size=8.1, color_hex="#1E293B")
        ty -= 10.5

    c.save(out_path)


if __name__ == "__main__":
    generate_midi_guide_pdf(OUT_MAIN)
    os.makedirs(os.path.dirname(OUT_CLAVE_SOL), exist_ok=True)
    os.makedirs(os.path.dirname(OUT_ARCHIVOS_MIDI), exist_ok=True)
    shutil.copy2(OUT_MAIN, OUT_CLAVE_SOL)
    shutil.copy2(OUT_MAIN, OUT_ARCHIVOS_MIDI)
    print(f"✅ PDF generado con éxito en:\n  • {OUT_MAIN}\n  • {OUT_CLAVE_SOL}\n  • {OUT_ARCHIVOS_MIDI}")
