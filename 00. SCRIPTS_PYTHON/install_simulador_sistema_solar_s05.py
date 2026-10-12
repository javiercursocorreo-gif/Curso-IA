#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
install_simulador_sistema_solar_s05.py
Integra el Simulador 3D del Sistema Solar (Fotogrametría NASA) en:
1. PROBADOR_CODIGO_IA.html (añadiendo el botón 🪐 Sistema Solar 3D y la plantilla exampleSolarTemplate)
2. Catálogo Maestro de las 10 Simulaciones (INDICE_10_SIMULACIONES_INTERACTIVAS_3D.pdf y .html)
3. Ficha Didáctica Oficial COD-005 (05_COD-005_Taller_Simulador_Sistema_Solar_3D.pdf y 05_Sesion/)
"""

import os
import re
import html
import subprocess
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM_PATH = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES", "05_SIMULADOR_SISTEMA_SOLAR_3D.html")
PROBADOR_PATH = os.path.join(ROOT_DIR, "PROBADOR_CODIGO_IA.html")


def update_probador():
    if not os.path.isfile(SIM_PATH) or not os.path.isfile(PROBADOR_PATH):
        print("⚠️ No se encontró el simulador o PROBADOR_CODIGO_IA.html")
        return

    sim_code = open(SIM_PATH, "r", encoding="utf-8").read()
    escaped_sim = html.escape(sim_code)
    prob_html = open(PROBADOR_PATH, "r", encoding="utf-8").read()

    # 1. Añadir botón btnLoadSolar tras btnLoadOjo si no existe
    solar_btn = (
        '            <button class="btn btn-emerald" id="btnLoadSolar" '
        'style="background: rgba(251, 191, 36, 0.2); color: #fbbf24; border-color: rgba(251, 191, 36, 0.45);" '
        'title="Cargar simulador: Sistema Solar 3D Interactivo (Fotogrametría Satelital NASA)">\n'
        '                🪐 Sistema Solar 3D\n'
        '            </button>'
    )
    if 'id="btnLoadSolar"' not in prob_html:
        prob_html = re.sub(
            r'(<button class="btn btn-emerald" id="btnLoadOjo".*?</button>)',
            r'\1\n' + solar_btn,
            prob_html,
            count=1,
            flags=re.DOTALL
        )

    # 2. Añadir o actualizar <textarea id="exampleSolarTemplate">
    solar_textarea = f'    <textarea id="exampleSolarTemplate" style="display:none;">{escaped_sim}</textarea>'
    if 'id="exampleSolarTemplate"' in prob_html:
        prob_html = re.sub(
            r'<textarea id="exampleSolarTemplate" style="display:none;">.*?</textarea>',
            lambda _: solar_textarea.strip(),
            prob_html,
            flags=re.DOTALL
        )
    else:
        prob_html = prob_html.replace(
            '<textarea id="exampleOjoTemplate"',
            solar_textarea + '\n    <textarea id="exampleOjoTemplate"',
            1
        )

    # 3. Añadir listener JS para btnLoadSolar y soporte ?sesion=5
    if 'const btnLoadSolar =' not in prob_html:
        js_target = """        // Cargar simulador Ojo Humano 3D
        const btnLoadOjo = document.getElementById("btnLoadOjo");
        if (btnLoadOjo) {
            btnLoadOjo.addEventListener("click", () => {
                const template = document.getElementById("exampleOjoTemplate");
                editor.value = template.value;
                charCount.textContent = template.value.length + " caracteres";
                runCode(false);
            });
        }"""
        js_replacement = js_target + """

        // Cargar simulador Sistema Solar 3D (NASA)
        const btnLoadSolar = document.getElementById("btnLoadSolar");
        if (btnLoadSolar) {
            btnLoadSolar.addEventListener("click", () => {
                const template = document.getElementById("exampleSolarTemplate");
                editor.value = template.value;
                charCount.textContent = template.value.length + " caracteres";
                runCode(false);
            });
        }"""
        prob_html = prob_html.replace(js_target, js_replacement, 1)

        # Actualizar bloque de filtrado ?sesion=5
        filter_target = "if (sesionParam === '4') {"
        filter_replacement = """if (sesionParam === '5') {
                if (btnLoadPulmones) btnLoadPulmones.style.display = 'none';
                if (btnLoadCorazon) btnLoadCorazon.style.display = 'none';
                if (btnLoadPompeya) btnLoadPompeya.style.display = 'none';
                if (btnLoadOjo) btnLoadOjo.style.display = 'none';
                if (btnLoadSolar) btnLoadSolar.style.display = 'inline-flex';
            } else if (sesionParam === '4') {
                if (btnLoadSolar) btnLoadSolar.style.display = 'none';"""
        prob_html = prob_html.replace(filter_target, filter_replacement, 1)

    with open(PROBADOR_PATH, "w", encoding="utf-8") as f:
        f.write(prob_html)
    print(f"✅ PROBADOR_CODIGO_IA.html actualizado con 🪐 Sistema Solar 3D: {PROBADOR_PATH}")


if __name__ == "__main__":
    update_probador()
    # Regenerar el Catálogo Maestro de 10 Simulaciones, la Ficha COD-005 y los 60 Mapas de Sesión (limpiando lungs.glb del mapa S01)
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    subprocess.run([sys.executable, os.path.join(scripts_dir, "build_pdf_indice_10_simulaciones_3d.py")], check=False)
    subprocess.run([sys.executable, os.path.join(scripts_dir, "build_pdf_cod_005.py")], check=False)
    subprocess.run([sys.executable, os.path.join(scripts_dir, "build_mapas_and_csvs_60_sessions.py")], check=False)

