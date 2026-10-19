#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extractor universal de voces y estilos para Korg EK-50 desde Voice Name List.pdf
Convierte el PDF a texto plano completo y localiza todos los instrumentos de Strings (Cuerdas).
"""

import os
import sys

pdf_path = os.path.join(os.path.dirname(__file__), "KORG EK50", "Voice Name List.pdf")
out_full_txt = os.path.join(os.path.dirname(__file__), "VOICE_NAME_LIST_COMPLETO.txt")
out_strings_txt = os.path.join(os.path.dirname(__file__), "STRINGS_KORG_EK50.txt")

if not os.path.exists(pdf_path):
    # Buscar alternativo si se ejecuta desde otra carpeta
    alt_path = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO MUSICA/KORG EK50/Voice Name List.pdf"
    if os.path.exists(alt_path):
        pdf_path = alt_path

print(f"📄 Procesando PDF: {pdf_path}")

reader = None
try:
    import pypdf
    reader = pypdf.PdfReader(pdf_path)
except Exception:
    try:
        import PyPDF2 as pypdf
        reader = pypdf.PdfReader(pdf_path)
    except Exception:
        pass

texto_paginas = []

if reader:
    print(f"📖 Leyendo {len(reader.pages)} páginas con motor pypdf...")
    for idx, page in enumerate(reader.pages):
        try:
            t = page.extract_text()
            if t:
                texto_paginas.append((idx + 1, t))
        except Exception as e:
            pass
else:
    # Fallback nativo zlib con decompresores múltiples
    import zlib
    import re
    print("📖 Leyendo mediante extracción directa de flujos zlib...")
    with open(pdf_path, "rb") as f:
        content = f.read()
    
    stream_chunks = re.findall(rb"stream[\r\n]+(.*?)[\r\n]+endstream", content, re.DOTALL)
    print(f"Bloques detectados: {len(stream_chunks)}")
    
    pag_idx = 1
    for s in stream_chunks:
        decomp = None
        for wbits in [zlib.MAX_WBITS, -zlib.MAX_WBITS, zlib.MAX_WBITS | 16]:
            try:
                decomp = zlib.decompress(s, wbits)
                break
            except Exception:
                continue
        if decomp:
            lineas = re.findall(rb"\((.*?)\)", decomp)
            if lineas:
                t = " ".join([l.decode("latin1", errors="ignore") for l in lineas])
                if len(t.strip()) > 30:
                    texto_paginas.append((pag_idx, t))
                    pag_idx += 1

# Guardar texto completo en archivo legible
with open(out_full_txt, "w", encoding="utf-8") as f:
    for num, txt in texto_paginas:
        f.write(f"\n{'='*70}\n--- PÁGINA {num} ---\n{'='*70}\n{txt}\n")

print(f"✅ ¡PDF completamente convertido a texto plano!: {out_full_txt}")

# Buscar todos los instrumentos de Strings / Cuerdas
keywords = ["string", "strings", "violin", "viola", "cello", "orchestra", "ensemble", "arco", "tremolo", "pizz"]
coincidencias = []

for num, txt in texto_paginas:
    for line in txt.split("\n"):
        line_clean = line.strip()
        if any(kw in line_clean.lower() for kw in keywords):
            coincidencias.append((num, line_clean))

with open(out_strings_txt, "w", encoding="utf-8") as f:
    f.write(f"LISTA DE INSTRUMENTOS DE STRINGS / CUERDAS (KORG EK-50)\n{'='*70}\n")
    for pag, l in coincidencias:
        f.write(f"[Pág. {pag:02d}] {l}\n")

print(f"\n🎻 ENCONTRADOS {len(coincidencias)} SONIDOS DE STRINGS / CUERDAS:")
print("-" * 70)
for pag, l in coincidencias[:25]:
    print(f"  • [Pág. {pag:02d}] {l}")
if len(coincidencias) > 25:
    print(f"  ... y {len(coincidencias) - 25} más guardados en: {out_strings_txt}")
print("-" * 70)
