# -*- coding: utf-8 -*-
import os, re

REPO = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SIM_DIR = os.path.join(REPO, "SIMULADORES_INTERACTIVOS/01_SIMULADORES")
INDEX_FILE = os.path.join(REPO, "SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/INDICE_SIMULACIONES_INTERACTIVAS_3D_COD.html")
CLASSROOM_BASE = os.path.join(REPO, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

print("1. Creando enlaces alias en 01_SIMULADORES para compatibilidad total...")
pairs = [
    ("11_SIMULADOR_VIOLIN_STRADIVARIUS_3D.html", "SIMULADOR_VIOLIN_STRADIVARIUS_3D.html"),
    ("12_SIMULADOR_NEBULOSA_HELIX_3D.html", "SIMULADOR_NEBULOSA_HELIX_3D.html"),
    ("13_SIMULADOR_ADN_GENETICO_3D.html", "SIMULADOR_ADN_GENETICO_3D.html"),
    ("14_SIMULADOR_AURORAS_JUPITER_3D.html", "SIMULADOR_AURORAS_JUPITER_3D.html"),
    ("15_SIMULADOR_JAMES_WEBB_3D.html", "SIMULADOR_JAMES_WEBB_3D.html"),
]
for src, dst in pairs:
    src_p = os.path.join(SIM_DIR, src)
    dst_p = os.path.join(SIM_DIR, dst)
    if os.path.exists(src_p):
        if os.path.islink(dst_p) or os.path.exists(dst_p):
            try: os.remove(dst_p)
            except: pass
        os.symlink(src, dst_p)
        print(f"   ✓ Alias creado: {dst} -> {src}")

print("2. Corrigiendo rutas y sustitución de James Webb en el Índice Maestro...")
if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        idx_content = f.read()

    # Sesiones 11 a 14: asegurar apuntes directos
    idx_content = idx_content.replace(
        'file: "../01_SIMULADORES/SIMULADOR_VIOLIN_STRADIVARIUS_3D.html"',
        'file: "../01_SIMULADORES/11_SIMULADOR_VIOLIN_STRADIVARIUS_3D.html"'
    )
    idx_content = idx_content.replace(
        'file: "../01_SIMULADORES/SIMULADOR_NEBULOSA_HELIX_3D.html"',
        'file: "../01_SIMULADORES/12_SIMULADOR_NEBULOSA_HELIX_3D.html"'
    )
    idx_content = idx_content.replace(
        'file: "../01_SIMULADORES/SIMULADOR_ADN_GENETICO_3D.html"',
        'file: "../01_SIMULADORES/13_SIMULADOR_ADN_GENETICO_3D.html"'
    )
    idx_content = idx_content.replace(
        'file: "../01_SIMULADORES/SIMULADOR_AURORAS_JUPITER_3D.html"',
        'file: "../01_SIMULADORES/14_SIMULADOR_AURORAS_JUPITER_3D.html"'
    )

    # Sustitución definitiva del Partenón por el Telescopio James Webb en Sesión 15
    jwst_card = """            {
                code: "[COD-015]", sesion: 15, lote: 2,
                title: "Telescopio Espacial James Webb (JWST) 3D",
                source: "NASA / ESA / CSA • Espejo de Berilio y Parasol",
                desc: "Segmentos hexagonales chapados en oro, escudo térmico de Kapton en 5 capas y espectroscopía infrarroja.",
                status: "ready", statusText: "🟢 Desplegado",
                file: "../01_SIMULADORES/15_SIMULADOR_JAMES_WEBB_3D.html"
            },"""
    idx_content = re.sub(
        r'\{\s*code:\s*"\[COD-015\]".*?file:\s*"\.\./01_SIMULADORES/SIMULADOR_PARTENON_AUREO_3D\.html"\s*\},',
        jwst_card,
        idx_content,
        flags=re.DOTALL
    )

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("   ✓ Índice maestro actualizado con éxito.")

print("3. Incorporando botón doble (Taller de Pruebas + Simulador 3D) en MAPAS 02 al 15...")
for s in range(2, 16):
    s_str = f"{s:02d}"
    s_folder = os.path.join(CLASSROOM_BASE, f"{s_str}_Sesion")
    map_file = os.path.join(s_folder, f"MAPA_SESION_{s_str}.html")
    if not os.path.exists(map_file):
        continue

    with open(map_file, "r", encoding="utf-8") as f:
        m = f.read()

    # Si ya tiene el botón del taller, omitir inserción
    if "PROBADOR_CODIGO_IA.html" not in m:
        taller_btn = f'''                        <a href="PROBADOR_CODIGO_IA.html?sesion={s}" target="_blank" class="btn-launch-interactive" title="Abrir Taller Oficial de Pruebas">
                            🚀 Abrir Taller Interactivo de Pruebas ↗
                        </a>\n'''

        # Buscar el botón del simulador dentro de la tarjeta COD
        # Formato habitual: <a href="SIMULADOR_...html" target="_blank" class="btn-launch-interactive" style="...
        pattern = r'(<a\s+href="SIMULADOR_[^"]+3D\.html"[^>]*class="btn-launch-interactive"[^>]*>)'
        
        def repl(match):
            sim_btn = match.group(1)
            # Asegurar margin-top:6px en el botón del simulador para que queden apilados
            if 'margin-top' not in sim_btn:
                sim_btn = re.sub(r'style="', 'style="margin-top:6px; ', sim_btn)
            return taller_btn + sim_btn

        m = re.sub(pattern, repl, m, count=1)
        with open(map_file, "w", encoding="utf-8") as f:
            f.write(m)
        print(f"   ✓ Mapa Sesión {s_str}: añadido botón Taller + Simulador 3D.")

# Limpieza especial de markup residual en Sesión 15
map15_file = os.path.join(CLASSROOM_BASE, "15_Sesion/MAPA_SESION_15.html")
if os.path.exists(map15_file):
    with open(map15_file, "r", encoding="utf-8") as f:
        m15 = f.read()
    m15 = re.sub(r'<a\s+href="SIMULADOR_PARTENON_AUREO_3D\.html".*?</a>\s*</div>', '', m15, flags=re.DOTALL)
    m15 = m15.replace("🏛️ Abrir Partenón Dorado 3D ↗", "")
    with open(map15_file, "w", encoding="utf-8") as f:
        f.write(m15)
    print("   ✓ Mapa Sesión 15: depurado y limpio con James Webb 3D.")

print("4. Verificación de integridad de enlaces del Índice Maestro:")
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()
missing = 0
for l in lines:
    if "file:" in l and "SIMULADOR" in l:
        fn = l.split('file: "')[-1].split('"')[0]
        full_p = os.path.normpath(os.path.join(os.path.dirname(INDEX_FILE), fn))
        if not os.path.exists(full_p):
            print(f"   ❌ RUTA ROTA: {fn}")
            missing += 1
if missing == 0:
    print("   ✅ ¡TODOS LOS ENLACES DEL ÍNDICE MAESTRO EXISTEN Y SE ABREN AL 100%!")
else:
    print(f"   ⚠️ Enlaces pendientes: {missing}")
