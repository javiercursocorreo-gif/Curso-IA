#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convierte 'Voice Name List.pdf' a texto plano guardándolo exactamente al lado del PDF
como 'Voice Name List.txt' y extrae las mejores opciones de Strings para Upper 1, 2 y 3.
"""

import os
import sys

carpeta_korg = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO MUSICA/KORG EK50"
pdf_path = os.path.join(carpeta_korg, "Voice Name List.pdf")
txt_path = os.path.join(carpeta_korg, "Voice Name List.txt")

print(f"📄 Origen PDF: {pdf_path}")
print(f"📝 Destino TXT: {txt_path}")

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

paginas = []

if reader:
    print(f"📖 Leyendo {len(reader.pages)} páginas del PDF oficial de Korg...")
    for idx, p in enumerate(reader.pages):
        try:
            t = p.extract_text()
            if t:
                paginas.append((idx + 1, t))
        except Exception:
            pass
else:
    import zlib, re
    print("📖 Leyendo mediante descompresión interna de flujos...")
    with open(pdf_path, "rb") as f:
        data = f.read()
    chunks = re.findall(rb"stream[\r\n]+(.*?)[\r\n]+endstream", data, re.DOTALL)
    pag_num = 1
    for c in chunks:
        decomp = None
        for w in [zlib.MAX_WBITS, -zlib.MAX_WBITS, zlib.MAX_WBITS | 16]:
            try:
                decomp = zlib.decompress(c, w)
                break
            except Exception:
                pass
        if decomp:
            lineas = re.findall(rb"\((.*?)\)", decomp)
            if lineas:
                t = " ".join([l.decode("latin1", errors="ignore") for l in lineas])
                if len(t.strip()) > 35:
                    paginas.append((pag_num, t))
                    pag_num += 1

# Guardar al lado del PDF
with open(txt_path, "w", encoding="utf-8") as f:
    f.write("KORG EK-50 - VOICE NAME LIST COMPLETO (TEXTO PLANO)\n" + "="*80 + "\n\n")
    for num, texto in paginas:
        f.write(f"\n{'='*80}\n--- PÁGINA {num} ---\n{'='*80}\n\n{texto}\n")

print(f"✅ ¡Documento guardado con éxito al lado del PDF!: {txt_path}\n")

# Búsqueda de Strings
keywords = ["string", "strings", "orch", "violin", "cello", "ensemble"]
resultados = []

for num, texto in paginas:
    for linea in texto.split("\n"):
        l = linea.strip()
        if any(k in l.lower() for k in keywords):
            resultados.append((num, l))

print("="*80)
print("🎻 SONIDOS DE STRINGS DETECTADOS EN EL DOCUMENTO:")
print("="*80)
for num, l in resultados[:30]:
    print(f" [Pág {num:02d}] {l}")

print("="*80)
