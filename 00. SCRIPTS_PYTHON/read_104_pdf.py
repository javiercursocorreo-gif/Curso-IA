#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
read_104_pdf.py
Inspecciona la carpeta '104 ESTILO ANIMADOS SIN PROGRAMAR', localiza el PDF
de los 100 Prompts de utilidades animadas, extrae su contenido y estructura
un análisis detallado en Markdown para clasificar y seleccionar las mejores utilidades.
"""

import os
import sys
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
TARGET_DIR = os.path.join(BASE_DIR, "104 ESTILO ANIMADOS SIN PROGRAMAR")
OUTPUT_MD = os.path.join(BASE_DIR, "104 ESTILO ANIMADOS SIN PROGRAMAR", "INDICE_Y_ANALISIS_100_PROMPTS.md")
OUTPUT_MD_BACKUP = os.path.join(SCRIPT_DIR, "104_PROMPTS_ANALISIS.md")

def extract_text_from_pdf(pdf_path):
    text = ""
    # Intento 1: pypdf / PyPDF2
    try:
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        print(f"  📄 Leyendo con pypdf: {len(reader.pages)} páginas encontradas.")
        for idx, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            text += f"\n--- [PÁGINA {idx+1}] ---\n" + page_text
        return text
    except Exception:
        pass

    try:
        import PyPDF2
        reader = PyPDF2.PdfReader(pdf_path)
        print(f"  📄 Leyendo con PyPDF2: {len(reader.pages)} páginas encontradas.")
        for idx, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            text += f"\n--- [PÁGINA {idx+1}] ---\n" + page_text
        return text
    except Exception:
        pass

    # Intento 2: pdfplumber
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            print(f"  📄 Leyendo con pdfplumber: {len(pdf.pages)} páginas encontradas.")
            for idx, page in enumerate(pdf.pages):
                page_text = page.extract_text() or ""
                text += f"\n--- [PÁGINA {idx+1}] ---\n" + page_text
        return text
    except Exception:
        pass

    # Intento 3: pdftotext (utilidad nativa de poppler en macOS si está disponible)
    try:
        import subprocess
        res = subprocess.run(["pdftotext", pdf_path, "-"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0 and res.stdout:
            print("  📄 Leyendo con pdftotext del sistema.")
            return res.stdout
    except Exception:
        pass

    return text

def main():
    print("=" * 80)
    print("🔍 INSPECCIÓN DE LA CARPETA: 104 ESTILO ANIMADOS SIN PROGRAMAR")
    print("=" * 80)

    if not os.path.exists(TARGET_DIR):
        print(f"❌ La carpeta no existe en: {TARGET_DIR}")
        return

    # Listar todos los archivos en la carpeta
    all_files = os.listdir(TARGET_DIR)
    print(f"\n📂 Contenido detectado en la carpeta ({len(all_files)} elementos):")
    pdf_files = []
    for f in all_files:
        full_p = os.path.join(TARGET_DIR, f)
        size_kb = os.path.getsize(full_p) / 1024 if os.path.isfile(full_p) else 0
        is_pdf = f.lower().endswith(".pdf")
        tag = "📕 [PDF]" if is_pdf else "📁 [DIR]" if os.path.isdir(full_p) else "📄 [FILE]"
        print(f"   {tag} {f} ({size_kb:.1f} KB)")
        if is_pdf:
            pdf_files.append(full_p)

    if not pdf_files:
        print("\n⚠️ No se encontraron archivos .pdf en la carpeta.")
        return

    for target_pdf in pdf_files:
        pdf_name = os.path.basename(target_pdf)
        print(f"\n==============================================================================")
        print(f"📖 EXTRAYENDO CONTENIDO DE: {pdf_name}")
        print(f"==============================================================================")

        raw_text = extract_text_from_pdf(target_pdf)
        if not raw_text.strip():
            print("⚠️ No se pudo extraer texto seleccionable del PDF (podría ser un escaneo de imagen).")
            continue

        print(f"✅ Texto extraído con éxito ({len(raw_text)} caracteres, ~{len(raw_text.split())} palabras).")

        # Generar archivo Markdown con el texto íntegro e índice
        md_content = f"# ÍNDICE Y ANÁLISIS DE PROMPTS: {pdf_name}\n\n"
        md_content += f"> **Origen:** `{target_pdf}`  \n"
        md_content += f"> **Extracción automática:** {len(raw_text.splitlines())} líneas de texto.  \n\n"
        md_content += "---\n\n"
        md_content += "## 📋 TEXTO COMPLETO EXTRAÍDO DEL DOCUMENTO\n\n"
        md_content += "```text\n"
        md_content += raw_text
        md_content += "\n```\n"

        for dest in [OUTPUT_MD, OUTPUT_MD_BACKUP]:
            try:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "w", encoding="utf-8") as f:
                    f.write(md_content)
                print(f"💾 Guardado informe y texto en: {dest}")
            except Exception as e:
                print(f"❌ Error al guardar en {dest}: {e}")

        # Mostrar las primeras 40 líneas en consola para vista previa inmediata
        print("\n--- [VISTA PREVIA DEL DOCUMENTO] ---")
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        for l in lines[:40]:
            print(f"  • {l}")
        if len(lines) > 40:
            print(f"  ... [y {len(lines) - 40} líneas más en el archivo Markdown]")

if __name__ == "__main__":
    main()

