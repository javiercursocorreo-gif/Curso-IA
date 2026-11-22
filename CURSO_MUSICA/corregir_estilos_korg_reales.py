#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
corregir_estilos_korg_reales.py
Corrige todos los números, nombres y parámetros MIDI de los estilos de acompañamiento (Línea 1 del HUD flotante)
en todas las canciones de CURSO_MUSICA, alineándolos al 100% con la Voice Name List oficial del Korg EK-50:

1. CANCION_37_PARLAMI_DAMORE_MARIU.html:
   - 012 Italian Waltz (que en realidad es 012 LightRock 1) -> 054 Slow Waltz1 (y 055 Slow Waltz2)
2. Boleros (CANCION_09, CANCION_19, CANCION_21, CANCION_36):
   - 171 Bolero Latino (que en realidad es 171 ChaCha Funk) -> 176 Slow Bolero
3. CANCION_01_TO_ALL_THE_GIRLS.html:
   - 042 Slow Ballad (que en realidad es 042 NaturalBeat) -> 023 Slow Ballad
4. CANCION_02_HALLELUJAH.html:
   - 052 Slow Rock 3 -> 052 Unpl.SlRock (nombre oficial real)
5. CANCION_38_YOULL_BE_IN_MY_HEART.html:
   - 043 Pop Ballad (que en realidad es 043 Celtic Bld) -> 037 PopBallad 2
6. Actualización del objeto CANONICAL_STYLE_MAP en todas las canciones.
7. Sincronización idéntica entre REPERTORIO_KORG_EK50.html e index.html.
"""

import os
import re
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mapa canónico oficial 100% real del Korg EK-50
# Fórmula: MSB=32, LSB=Math.floor((N-1)/16), PC=(N-1)%16
OFFICIAL_KORG_STYLES = {
    "12":  {"msb": 32, "lsb": 0, "pc": 11, "name": "012 LightRock 1"},
    "012": {"msb": 32, "lsb": 0, "pc": 11, "name": "012 LightRock 1"},
    "19":  {"msb": 32, "lsb": 1, "pc": 2,  "name": "019 8Bt Analog 1"},
    "019": {"msb": 32, "lsb": 1, "pc": 2,  "name": "019 8Bt Analog 1"},
    "23":  {"msb": 32, "lsb": 1, "pc": 6,  "name": "023 Slow Ballad"},
    "023": {"msb": 32, "lsb": 1, "pc": 6,  "name": "023 Slow Ballad"},
    "37":  {"msb": 32, "lsb": 2, "pc": 4,  "name": "037 PopBallad 2"},
    "037": {"msb": 32, "lsb": 2, "pc": 4,  "name": "037 PopBallad 2"},
    "41":  {"msb": 32, "lsb": 2, "pc": 8,  "name": "041 Love Ballad"},
    "041": {"msb": 32, "lsb": 2, "pc": 8,  "name": "041 Love Ballad"},
    "42":  {"msb": 32, "lsb": 2, "pc": 9,  "name": "042 NaturalBeat"},
    "042": {"msb": 32, "lsb": 2, "pc": 9,  "name": "042 NaturalBeat"},
    "49":  {"msb": 32, "lsb": 3, "pc": 0,  "name": "049 Slow Pop"},
    "049": {"msb": 32, "lsb": 3, "pc": 0,  "name": "049 Slow Pop"},
    "50":  {"msb": 32, "lsb": 3, "pc": 1,  "name": "050 Slow Rock 1"},
    "050": {"msb": 32, "lsb": 3, "pc": 1,  "name": "050 Slow Rock 1"},
    "51":  {"msb": 32, "lsb": 3, "pc": 2,  "name": "051 Slow Rock 2"},
    "051": {"msb": 32, "lsb": 3, "pc": 2,  "name": "051 Slow Rock 2"},
    "52":  {"msb": 32, "lsb": 3, "pc": 3,  "name": "052 Unpl.SlRock"},
    "052": {"msb": 32, "lsb": 3, "pc": 3,  "name": "052 Unpl.SlRock"},
    "54":  {"msb": 32, "lsb": 3, "pc": 5,  "name": "054 Slow Waltz1"},
    "054": {"msb": 32, "lsb": 3, "pc": 5,  "name": "054 Slow Waltz1"},
    "55":  {"msb": 32, "lsb": 3, "pc": 6,  "name": "055 Slow Waltz2"},
    "055": {"msb": 32, "lsb": 3, "pc": 6,  "name": "055 Slow Waltz2"},
    "93":  {"msb": 32, "lsb": 5, "pc": 12, "name": "093 Pop Shuffle"},
    "093": {"msb": 32, "lsb": 5, "pc": 12, "name": "093 Pop Shuffle"},
    "106": {"msb": 32, "lsb": 6, "pc": 9,  "name": "106 MotownShufl"},
    "111": {"msb": 32, "lsb": 6, "pc": 14, "name": "111 Motown"},
    "151": {"msb": 32, "lsb": 9, "pc": 6,  "name": "151 Bolero"},
    "154": {"msb": 32, "lsb": 9, "pc": 9,  "name": "154 New Age"},
    "171": {"msb": 32, "lsb": 10, "pc": 10, "name": "171 ChaCha Funk"},
    "172": {"msb": 32, "lsb": 10, "pc": 11, "name": "172 Latin Rock"},
    "174": {"msb": 32, "lsb": 10, "pc": 13, "name": "174 Beguine 1"},
    "175": {"msb": 32, "lsb": 10, "pc": 14, "name": "175 Beguine 2"},
    "176": {"msb": 32, "lsb": 10, "pc": 15, "name": "176 Slow Bolero"},
    "247": {"msb": 32, "lsb": 15, "pc": 6,  "name": "247 ViennaWaltz"},
}

def serialize_map_js(style_map):
    import json
    return "const CANONICAL_STYLE_MAP = " + json.dumps(style_map, ensure_ascii=False) + ";"

def update_song_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    orig_content = content
    fname = os.path.basename(filepath)

    # 1. CANCION_37_PARLAMI_DAMORE_MARIU.html
    if "CANCION_37" in fname:
        # Reemplazar 012 Italian Waltz por 054 Slow Waltz1
        content = re.sub(
            r'<button[^>]*data-style=[\'"]12[\'"][^>]*>.*?012\s+Italian\s+Waltz.*?</button>',
            '<button class="hud-style-btn" data-style="054" onclick="activarEstilo(\'054\', this)" style="background:linear-gradient(180deg, #b91c1c 0%, #7f1d1d 100%); color:#ffffff; border:1px solid #ef4444; padding:7px 14px; min-height:36px; border-radius:7px; font-weight:800; font-size:0.84rem; cursor:pointer; touch-action:manipulation; min-width:135px; text-align:center; pointer-events: auto;">054 Slow Waltz1</button>',
            content,
            flags=re.DOTALL
        )
        # Reemplazar 042 Slow Waltz por 055 Slow Waltz2
        content = re.sub(
            r'<button[^>]*data-style=[\'"]42[\'"][^>]*>.*?042\s+Slow\s+Waltz.*?</button>',
            '<button class="hud-style-btn" data-style="055" onclick="activarEstilo(\'055\', this)" style="background:#1e293b; color:#cbd5e1; border:1px solid #475569; padding:7px 14px; min-height:36px; border-radius:7px; font-weight:800; font-size:0.84rem; cursor:pointer; touch-action:manipulation; min-width:135px; text-align:center; pointer-events: auto;">055 Slow Waltz2</button>',
            content,
            flags=re.DOTALL
        )
        # Actualizar comentario
        content = content.replace("012 ITALIAN WALTZ & 042 SLOW WALTZ", "054 SLOW WALTZ 1 & 055 SLOW WALTZ 2")
        print(f"  [OK] {fname}: Reemplazados 012/042 por 054 Slow Waltz1 y 055 Slow Waltz2")

    # 2. Canciones con 171 Bolero Latino -> 176 Slow Bolero
    if any(k in fname for k in ["CANCION_09", "CANCION_19", "CANCION_21", "CANCION_36"]):
        content = re.sub(
            r'<button[^>]*data-style=[\'"]171[\'"][^>]*>.*?171\s+Bolero\s+Latino.*?</button>',
            lambda m: m.group(0).replace('data-style="171"', 'data-style="176"').replace("activarEstilo('171'", "activarEstilo('176'").replace("activarEstilo(171", "activarEstilo(176").replace("171 Bolero Latino", "176 Slow Bolero"),
            content,
            flags=re.DOTALL
        )
        print(f"  [OK] {fname}: Reemplazado 171 Bolero Latino por 176 Slow Bolero")

    # 3. CANCION_01_TO_ALL_THE_GIRLS.html
    if "CANCION_01" in fname:
        content = re.sub(
            r'<button[^>]*data-style=[\'"]42[\'"][^>]*>.*?042\s+Slow\s+Ballad.*?</button>',
            lambda m: m.group(0).replace('data-style="42"', 'data-style="023"').replace("activarEstilo('42'", "activarEstilo('023'").replace("activarEstilo(42", "activarEstilo(023").replace("042 Slow Ballad", "023 Slow Ballad"),
            content,
            flags=re.DOTALL
        )
        print(f"  [OK] {fname}: Reemplazado 042 Slow Ballad por 023 Slow Ballad")

    # 4. CANCION_02_HALLELUJAH.html
    if "CANCION_02" in fname:
        content = re.sub(
            r'052\s+Slow\s+Rock\s+3',
            '052 Unpl.SlRock',
            content
        )
        print(f"  [OK] {fname}: Actualizado 052 Slow Rock 3 a 052 Unpl.SlRock")

    # 5. CANCION_38_YOULL_BE_IN_MY_HEART.html
    if "CANCION_38" in fname:
        content = re.sub(
            r'<button[^>]*data-style=[\'"]43[\'"][^>]*>.*?043\s+Pop\s+Ballad.*?</button>',
            lambda m: m.group(0).replace('data-style="43"', 'data-style="037"').replace("activarEstilo('43'", "activarEstilo('037'").replace("activarEstilo(43", "activarEstilo(037").replace("043 Pop Ballad", "037 PopBallad 2"),
            content,
            flags=re.DOTALL
        )
        print(f"  [OK] {fname}: Reemplazado 043 Pop Ballad por 037 PopBallad 2")

    # 6. Actualizar CANONICAL_STYLE_MAP si está presente
    if "CANONICAL_STYLE_MAP" in content:
        pattern = r'(?:var|const|let)\s+CANONICAL_STYLE_MAP\s*=\s*\{.*?\};'
        new_js = serialize_map_js(OFFICIAL_KORG_STYLES)
        content = re.sub(pattern, new_js, content, flags=re.DOTALL)
        print(f"  [OK] {fname}: CANONICAL_STYLE_MAP sincronizado con catálogo oficial")

    if content != orig_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def main():
    print("==================================================================")
    print("=== [CORRECCIÓN INTEGRAL DE ESTILOS KORG EK-50 EN CANCIONES] ===")
    print("==================================================================")

    import glob
    files = sorted(glob.glob(os.path.join(BASE_DIR, "CANCION_*.html")))
    updated = 0
    for f in files:
        if update_song_file(f):
            updated += 1

    print(f"\n[RESUMEN] Canciones modificadas: {updated}/{len(files)}")

    # 7. Sincronización idéntica de REPERTORIO_KORG_EK50.html con index.html
    rep_path = os.path.join(BASE_DIR, "REPERTORIO_KORG_EK50.html")
    idx_path = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(rep_path) and os.path.exists(idx_path):
        # Actualizar enlaces si hubiese menciones en el repertorio
        with open(rep_path, "r", encoding="utf-8") as rf:
            rep_text = rf.read()
        rep_text = rep_text.replace("042 Slow Waltz", "054 Slow Waltz")
        rep_text = rep_text.replace("171 Bolero Latino", "176 Slow Bolero")
        with open(rep_path, "w", encoding="utf-8") as rf:
            rf.write(rep_text)

        shutil.copy2(rep_path, idx_path)
        print("✅ REPERTORIO_KORG_EK50.html sincronizado al 100% con index.html")

if __name__ == "__main__":
    main()
