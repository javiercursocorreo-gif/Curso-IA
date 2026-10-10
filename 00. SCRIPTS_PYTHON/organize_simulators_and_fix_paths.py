#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
organize_simulators_and_fix_paths.py
Reorganiza la carpeta SIMULADORES_INTERACTIVOS en 3 subcarpetas:
  - 01_SIMULADORES/
  - 02_INDICES_Y_CATALOGOS/
  - 03_ASSETS_3D_Y_DATOS/

Actualiza todos los paths internos de los archivos HTML, PDF scripts y el script maestro
build_mapas_and_csvs_60_sessions.py para que todo funcione sin errores.
"""

import os
import shutil
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS")

DIR_SIMS = os.path.join(SIM_DIR, "01_SIMULADORES")
DIR_INDICES = os.path.join(SIM_DIR, "02_INDICES_Y_CATALOGOS")
DIR_ASSETS = os.path.join(SIM_DIR, "03_ASSETS_3D_Y_DATOS")

def main():
    print("🚀 Iniciando reorganización de SIMULADORES_INTERACTIVOS...")

    os.makedirs(DIR_SIMS, exist_ok=True)
    os.makedirs(DIR_INDICES, exist_ok=True)
    os.makedirs(DIR_ASSETS, exist_ok=True)

    # 1. Definición de distribución de archivos
    indices_files = [
        "INDICE_10_SIMULACIONES_INTERACTIVAS_3D.pdf",
        "INDICE_MODELOS_ANATOMICOS_3D.html",
        "INDICE_MODELOS_ANATOMICOS_3D_NIH.pdf"
    ]

    assets_exts = [".glb", ".js", ".mp3", ".jpg", ".png"]

    # Mover archivos existentes en la raíz de SIMULADORES_INTERACTIVOS
    all_files = [f for f in os.listdir(SIM_DIR) if os.path.isfile(os.path.join(SIM_DIR, f)) and not f.startswith(".")]

    for fname in all_files:
        src = os.path.join(SIM_DIR, fname)
        ext = os.path.splitext(fname)[1].lower()

        if fname in indices_files or fname.startswith("INDICE_"):
            dst = os.path.join(DIR_INDICES, fname)
            print(f"📦 [Índices] {fname} -> 02_INDICES_Y_CATALOGOS/")
            shutil.move(src, dst)
        elif ext in assets_exts:
            dst = os.path.join(DIR_ASSETS, fname)
            print(f"📦 [Assets] {fname} -> 03_ASSETS_3D_Y_DATOS/")
            shutil.move(src, dst)
        elif ext == ".html":
            dst = os.path.join(DIR_SIMS, fname)
            print(f"📦 [Simulador] {fname} -> 01_SIMULADORES/")
            shutil.move(src, dst)
        else:
            print(f"ℹ️ Archivo no clasificado: {fname}")

    # 2. Ajustar rutas relativas dentro de los simuladores en 01_SIMULADORES/
    print("\n🔧 Ajustando rutas en los HTML de 01_SIMULADORES/...")
    sim_htmls = [f for f in os.listdir(DIR_SIMS) if f.endswith(".html")]
    
    asset_names = [
        "heart.glb", "heart_b64.js", "heartbeat.mp3", "heartbeat_audio_b64.js",
        "lungs.glb", "lungs_b64.js",
        "pompeii_photos_b64.js", "pompeii_ruins_hd.jpg", "pompeii_reconstructed_hd.jpg",
        "pompeii_ruins.jpg", "pompeii_ruins_2x.jpg", "pompeii_reconstructed.jpg",
        "pompeii_reconstructed_2x.jpg", "pompeii_reconstructed_clean.jpg",
        "pompeii_real_ruins.jpg", "pompeii_cyark_recon.jpg"
    ]

    for hf in sim_htmls:
        hpath = os.path.join(DIR_SIMS, hf)
        with open(hpath, "r", encoding="utf-8") as f:
            content = f.read()

        changed = False

        # Actualizar llamadas src="..." o referencias directas a archivos locales
        for asset in asset_names:
            # Reemplazar src="asset" por src="../03_ASSETS_3D_Y_DATOS/asset" (sin tocar urls https://)
            pattern1 = f'src="{asset}"'
            replace1 = f'src="../03_ASSETS_3D_Y_DATOS/{asset}"'
            if pattern1 in content:
                content = content.replace(pattern1, replace1)
                changed = True

            pattern2 = f'src=\'{asset}\''
            replace2 = f'src=\'../03_ASSETS_3D_Y_DATOS/{asset}\''
            if pattern2 in content:
                content = content.replace(pattern2, replace2)
                changed = True

            # Reemplazar "asset" suelto si es fallback local: || "asset"
            pattern3 = f'|| "{asset}"'
            replace3 = f'|| "../03_ASSETS_3D_Y_DATOS/{asset}"'
            if pattern3 in content:
                content = content.replace(pattern3, replace3)
                changed = True

            # Caso especial lungs.glb en array de carga local
            pattern4 = f'"{asset}",'
            replace4 = f'"../03_ASSETS_3D_Y_DATOS/{asset}",'
            if pattern4 in content:
                content = content.replace(pattern4, replace4)
                changed = True

        if changed:
            with open(hpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✅ Rutas actualizadas en: 01_SIMULADORES/{hf}")

    # 3. Ajustar enlaces en 02_INDICES_Y_CATALOGOS/INDICE_MODELOS_ANATOMICOS_3D.html
    idx_html = os.path.join(DIR_INDICES, "INDICE_MODELOS_ANATOMICOS_3D.html")
    if os.path.exists(idx_html):
        with open(idx_html, "r", encoding="utf-8") as f:
            idx_content = f.read()

        idx_content = idx_content.replace('href="01_SIMULADOR_LATIDO_CARDIACO_3D_REALISTA.html"', 'href="../01_SIMULADORES/01_SIMULADOR_LATIDO_CARDIACO_3D_REALISTA.html"')
        idx_content = idx_content.replace('href="SIMULADOR_PULMONES_3D.html"', 'href="../01_SIMULADORES/SIMULADOR_PULMONES_3D.html"')
        idx_content = idx_content.replace('href="SIMULADOR_CORAZON_3D.html"', 'href="../01_SIMULADORES/SIMULADOR_CORAZON_3D.html"')
        idx_content = idx_content.replace('href="SIMULADOR_POMPEYA_3D.html"', 'href="../01_SIMULADORES/SIMULADOR_POMPEYA_3D.html"')

        with open(idx_html, "w", encoding="utf-8") as f:
            f.write(idx_content)
        print("  ✅ Enlaces a simuladores actualizados en 02_INDICES_Y_CATALOGOS/INDICE_MODELOS_ANATOMICOS_3D.html")

    # 4. Actualizar rutas en 00. SCRIPTS_PYTHON/build_pdf_indice_10_simulaciones_3d.py
    script_10_sim = os.path.join(ROOT_DIR, "00. SCRIPTS_PYTHON", "build_pdf_indice_10_simulaciones_3d.py")
    if os.path.exists(script_10_sim):
        with open(script_10_sim, "r", encoding="utf-8") as f:
            s_content = f.read()
        s_content = s_content.replace('OUT_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS")', 'OUT_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "02_INDICES_Y_CATALOGOS")')
        with open(script_10_sim, "w", encoding="utf-8") as f:
            f.write(s_content)
        print("  ✅ build_pdf_indice_10_simulaciones_3d.py actualizado a carpeta 02_INDICES_Y_CATALOGOS")

    # 5. Actualizar rutas en 00. SCRIPTS_PYTHON/build_pdf_indice_modelos_3d.py
    script_mod_3d = os.path.join(ROOT_DIR, "00. SCRIPTS_PYTHON", "build_pdf_indice_modelos_3d.py")
    if os.path.exists(script_mod_3d):
        with open(script_mod_3d, "r", encoding="utf-8") as f:
            s_content = f.read()
        s_content = s_content.replace('OUT_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS")', 'OUT_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "02_INDICES_Y_CATALOGOS")')
        with open(script_mod_3d, "w", encoding="utf-8") as f:
            f.write(s_content)
        print("  ✅ build_pdf_indice_modelos_3d.py actualizado a carpeta 02_INDICES_Y_CATALOGOS")

    # 6. Actualizar rutas en build_mapas_and_csvs_60_sessions.py
    master_script = os.path.join(ROOT_DIR, "00. SCRIPTS_PYTHON", "build_mapas_and_csvs_60_sessions.py")
    if os.path.exists(master_script):
        with open(master_script, "r", encoding="utf-8") as f:
            m_content = f.read()

        # Actualizar origen de copias para sesiones
        m_content = m_content.replace(
            'pulm_src = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "SIMULADOR_PULMONES_3D.html")',
            'pulm_src = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES", "SIMULADOR_PULMONES_3D.html")'
        )
        m_content = m_content.replace(
            'ex_src = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", extra)',
            'ex_src = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "03_ASSETS_3D_Y_DATOS", extra)\n                if not os.path.exists(ex_src):\n                    ex_src = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES", extra)'
        )
        m_content = m_content.replace(
            'cor_src = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "SIMULADOR_CORAZON_3D.html")',
            'cor_src = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES", "SIMULADOR_CORAZON_3D.html")'
        )

        with open(master_script, "w", encoding="utf-8") as f:
            f.write(m_content)
        print("  ✅ build_mapas_and_csvs_60_sessions.py actualizado con rutas hacia las nuevas subcarpetas")

    print("\n🎉 Reorganización completada con éxito total.")

if __name__ == "__main__":
    main()

