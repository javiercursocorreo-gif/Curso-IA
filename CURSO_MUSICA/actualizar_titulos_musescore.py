#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de resolución y extracción automática de títulos reales desde MuseScore
Actualiza REPERTORIO_KORG_EK50.html, index.html y la documentación con los títulos exactos.
"""

import os
import re
import subprocess
import sys
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCORES = []

TITULOS_FIJOS = {
    1: "To All The Girls I've Loved Before",
    2: "Hallelujah",
    3: "Hymn to the Fallen",
    4: "Cuando Calienta el Sol",
    5: "Con te partirò (Time to Say Goodbye)",
    6: "Volare (Nel blu dipinto di blu)",
    7: "Ave Maria",
    8: "Flashdance... What a Feeling",
    9: "Amor, Amor, Amor",
    10: "Adagio en Sol menor",
    11: "Senza Luce (A Whiter Shade of Pale)",
    12: "Romeo y Julieta (Tema de Amor)",
    13: "Canon en Re Mayor",
    14: "Air - Suite Orquestal nº 3 (Aria en Sol)",
    15: "Only You (And You Alone)",
    16: "My Heart Will Go On",
    17: "Morning Has Broken",
    18: "Piano Man",
    19: "Perfidia",
    20: "Nights in White Satin",
    21: "Amapola",
    22: "Killing Me Softly with His Song",
    23: "La Vie en Rose",
    24: "Stand by Me",
}

def obtener_html(url):
    # Intento 1: urllib con cabeceras de navegador
    try:
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            }
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception:
        pass

    # Intento 2: curl con Safari User-Agent y cabeceras completas
    try:
        res = subprocess.run([
            'curl', '-sL', '--max-time', '12',
            '-H', 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15',
            '-H', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            '-H', 'Accept-Language: it-IT,it;q=0.9,es-ES;q=0.8,en;q=0.7',
            '-H', 'Sec-Fetch-Dest: document',
            '-H', 'Sec-Fetch-Mode: navigate',
            '-H', 'Sec-Fetch-Site: none',
            '-H', 'Upgrade-Insecure-Requests: 1',
            url
        ], capture_output=True, text=True)
        return res.stdout
    except Exception:
        return ""

def extraer_titulo(html):
    if not html:
        return None
    # 1. Probar meta og:title
    m = re.search(r'<meta property="og:title" content="([^"]+)"', html)
    if m:
        t = m.group(1).strip()
        t = re.sub(r'\s*\|\s*Musescore\.com.*$', '', t, flags=re.I)
        t = re.sub(r'\s+sheet music for\s+.*$', '', t, flags=re.I)
        t = re.sub(r'^\s*Free sheet music\s*:\s*', '', t, flags=re.I)
        if t and len(t) > 2 and 'musescore' not in t.lower():
            return t

    # 2. Probar <title>
    m = re.search(r'<title>([^<]+)</title>', html)
    if m:
        t = m.group(1).strip()
        t = re.sub(r'\s*\|\s*Musescore\.com.*$', '', t, flags=re.I)
        t = re.sub(r'\s+sheet music for\s+.*$', '', t, flags=re.I)
        t = re.sub(r'^\s*Free sheet music\s*:\s*', '', t, flags=re.I)
        if t and len(t) > 2 and 'musescore' not in t.lower():
            return t

    # 3. Probar JSON-LD o meta name="title"
    m = re.search(r'<meta name="title" content="([^"]+)"', html)
    if m:
        t = m.group(1).strip()
        t = re.sub(r'\s*\|\s*Musescore\.com.*$', '', t, flags=re.I)
        t = re.sub(r'\s+sheet music for\s+.*$', '', t, flags=re.I)
        if t and len(t) > 2 and 'musescore' not in t.lower():
            return t

    # 4. Probar JSON embebido de MuseScore ("title":"...")
    m = re.search(r'"score":\{[^}]*?"title":"([^"]+)"', html)
    if m:
        t = m.group(1).strip()
        if t and len(t) > 2 and 'musescore' not in t.lower():
            return t

    m = re.search(r'"custom_url":[^,]+,"title":"([^"]+)"', html)
    if m:
        t = m.group(1).strip()
        if t and len(t) > 2 and 'musescore' not in t.lower():
            return t

    return None

def main():
    print("==============================================================================")
    print("🔍 LEYENDO Y RESOLVIENDO TÍTULOS REALES DE MUSESCORE...")
    print("==============================================================================")
    
    resultados = {}
    
    # 1. Cargar títulos oficiales confirmados
    for num, titulo in TITULOS_FIJOS.items():
        resultados[f"fijo_{num}"] = (num, titulo)

    for num, url, score_id in SCORES:
        print(f"📡 Consultando Obra {num} (Score #{score_id})...", end=" ", flush=True)
        html = obtener_html(url)
        titulo = extraer_titulo(html)
        if titulo:
            print(f"✅ ¡ENCONTRADO!: \"{titulo}\"")
            resultados[score_id] = (num, titulo)
        else:
            print(f"⚠️ No se pudo extraer título directo (manteniendo enlace).")

    if not resultados:
        print("\nℹ️ No se detectaron títulos nuevos por respuesta de red. Los enlaces directos permanecen activos.")
        return

    # Archivos HTML a actualizar
    archivos = [
        os.path.join(BASE_DIR, 'REPERTORIO_KORG_EK50.html'),
        os.path.join(BASE_DIR, 'index.html'),
    ]

    for archivo in archivos:
        if not os.path.exists(archivo):
            continue
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()

        cambios = 0
        for score_id, (num, titulo) in resultados.items():
            # Buscar el bloque del enlace con su número y reemplazar el texto del span
            patron = rf'(<span class="song-num"[^>]*>\s*{num}\.\s*</span>\s*<span[^>]*>)([^<]+)(</span>)'
            if re.search(patron, contenido):
                contenido = re.sub(patron, rf'\g<1>{titulo}\g<3>', contenido)
                cambios += 1

        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"📝 Archivo '{os.path.basename(archivo)}' actualizado con {cambios} títulos.")

    print("==============================================================================")
    print("🎉 ACTUALIZACIÓN DE TÍTULOS COMPLETADA")
    print("==============================================================================")

if __name__ == '__main__':
    main()
