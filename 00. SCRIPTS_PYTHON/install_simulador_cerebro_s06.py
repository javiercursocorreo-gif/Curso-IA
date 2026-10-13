#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
install_simulador_cerebro_s06.py
Integra el Simulador 3D del Cerebro Humano & Red Sináptica en:
1. PROBADOR_CODIGO_IA.html (añadiendo el botón 🧠 Cerebro 3D y la plantilla exampleBrainTemplate)
2. Catálogo Maestro de Simulaciones (INDICE_10_SIMULACIONES_INTERACTIVAS_3D.pdf y .html) pasando S06 a "Activo en S06"
3. Ficha Didáctica Oficial COD-006 (06_COD-006_Taller_Simulador_Cerebro_Humano_3D.pdf)
4. Sincronización en build_mapas_and_csvs_60_sessions.py para el botón del mapa de Sesión 06
"""

import os
import re
import html
import subprocess
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM_PATH = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES", "06_SIMULADOR_CEREBRO_3D.html")
PROBADOR_PATH = os.path.join(ROOT_DIR, "PROBADOR_CODIGO_IA.html")


def update_probador():
    if not os.path.isfile(SIM_PATH) or not os.path.isfile(PROBADOR_PATH):
        print("⚠️ No se encontró el simulador o PROBADOR_CODIGO_IA.html")
        return

    sim_code = open(SIM_PATH, "r", encoding="utf-8").read()
    escaped_sim = html.escape(sim_code)
    prob_html = open(PROBADOR_PATH, "r", encoding="utf-8").read()

    # 1. Añadir botón btnLoadBrain tras btnLoadSolar si no existe
    brain_btn = (
        '            <button class="btn btn-emerald" id="btnLoadBrain" '
        'style="background: rgba(192, 132, 252, 0.2); color: #c084fc; border-color: rgba(192, 132, 252, 0.45);" '
        'title="Cargar simulador: Cerebro Humano 3D & Red Sináptica">\n'
        '                🧠 Cerebro 3D\n'
        '            </button>'
    )
    if 'id="btnLoadBrain"' not in prob_html:
        prob_html = re.sub(
            r'(<button class="btn btn-emerald" id="btnLoadSolar".*?</button>)',
            r'\1\n' + brain_btn,
            prob_html,
            count=1,
            flags=re.DOTALL
        )

    # 2. Añadir o actualizar <textarea id="exampleBrainTemplate">
    brain_textarea = f'    <textarea id="exampleBrainTemplate" style="display:none;">{escaped_sim}</textarea>'
    if 'id="exampleBrainTemplate"' in prob_html:
        prob_html = re.sub(
            r'<textarea id="exampleBrainTemplate" style="display:none;">.*?</textarea>',
            lambda _: brain_textarea.strip(),
            prob_html,
            flags=re.DOTALL
        )
    else:
        prob_html = prob_html.replace(
            '<textarea id="exampleSolarTemplate"',
            brain_textarea + '\n    <textarea id="exampleSolarTemplate"',
            1
        )

    # 3. Añadir listener JS para btnLoadBrain y soporte ?sesion=6
    if 'const btnLoadBrain =' not in prob_html:
        js_target = """        // Cargar simulador Sistema Solar 3D (NASA)
        const btnLoadSolar = document.getElementById("btnLoadSolar");
        if (btnLoadSolar) {
            btnLoadSolar.addEventListener("click", () => {
                const template = document.getElementById("exampleSolarTemplate");
                editor.value = template.value;
                charCount.textContent = template.value.length + " caracteres";
                runCode(false);
            });
        }"""
        js_replacement = js_target + """

        // Cargar simulador Cerebro Humano 3D
        const btnLoadBrain = document.getElementById("btnLoadBrain");
        if (btnLoadBrain) {
            btnLoadBrain.addEventListener("click", () => {
                const template = document.getElementById("exampleBrainTemplate");
                editor.value = template.value;
                charCount.textContent = template.value.length + " caracteres";
                runCode(false);
            });
        }"""
        prob_html = prob_html.replace(js_target, js_replacement, 1)

        # Actualizar bloque de filtrado ?sesion=6
        filter_target = "if (sesionParam === '5') {"
        filter_replacement = """if (sesionParam === '6') {
                if (btnLoadPulmones) btnLoadPulmones.style.display = 'none';
                if (btnLoadCorazon) btnLoadCorazon.style.display = 'none';
                if (btnLoadPompeya) btnLoadPompeya.style.display = 'none';
                if (btnLoadOjo) btnLoadOjo.style.display = 'none';
                if (btnLoadSolar) btnLoadSolar.style.display = 'none';
                if (btnLoadBrain) btnLoadBrain.style.display = 'inline-flex';
            } else if (sesionParam === '5') {
                if (btnLoadBrain) btnLoadBrain.style.display = 'none';"""
        prob_html = prob_html.replace(filter_target, filter_replacement, 1)

    with open(PROBADOR_PATH, "w", encoding="utf-8") as f:
        f.write(prob_html)
    print(f"✅ PROBADOR_CODIGO_IA.html actualizado con 🧠 Cerebro 3D: {PROBADOR_PATH}")


def update_catalog():
    cat_script = os.path.join(ROOT_DIR, "00. SCRIPTS_PYTHON", "build_pdf_indice_10_simulaciones_3d.py")
    if not os.path.isfile(cat_script):
        return

    content = open(cat_script, "r", encoding="utf-8").read()
    # Actualizar estado de Sesión 06 a "Activo en S06" y enlazar archivo
    old_entry = '("06", "[COD-006]", "Salud & Neurociencia", "Cerebro Humano & Red Sináptica",\n     "Resonancia magnética médica cortical, vías neuronales, pulsos lumínicos bioeléctricos y selector de lóbulos cerebrales.",\n     "Ver Simulador Cerebro 3D", "#", "Plan S06"),'
    new_entry = '("06", "[COD-006]", "Salud & Neurociencia", "Cerebro Humano & Red Sináptica",\n     "Resonancia magnética médica cortical, vías neuronales, pulsos lumínicos bioeléctricos y selector de lóbulos cerebrales.",\n     "Ver Simulador Cerebro 3D", "../01_SIMULADORES/06_SIMULADOR_CEREBRO_3D.html", "Activo en S06"),'

    if old_entry in content:
        content = content.replace(old_entry, new_entry)
        with open(cat_script, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Catálogo Maestro actualizado: S06 ahora está Activo en S06")


def update_maps_script():
    maps_script = os.path.join(ROOT_DIR, "00. SCRIPTS_PYTHON", "build_mapas_and_csvs_60_sessions.py")
    if not os.path.isfile(maps_script):
        return

    content = open(maps_script, "r", encoding="utf-8").read()

    # 1. En clean_title_from_filename
    if "'SIMULADOR_CEREBRO' in f_up" not in content:
        content = content.replace(
            "    if 'SIMULADOR_SISTEMA_SOLAR' in f_up:",
            "    if 'SIMULADOR_CEREBRO' in f_up:\n        return 'Simulador 3D del Cerebro Humano y Red Sináptica'\n    if 'SIMULADOR_SISTEMA_SOLAR' in f_up:"
        )

    # 2. En build_html_map botón COD
    s6_btn_target = """                elif session_num == 5:
                    sim_btn = \"\"\"
                        <a href="SIMULADOR_SISTEMA_SOLAR_3D.html" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background:linear-gradient(135deg, #d97706, #b45309); border-color:#fbbf24;" title="Abrir Simulador 3D del Sistema Solar (Fotogrametría Satelital NASA)">
                            🪐 Ver Simulador Sistema Solar 3D ↗
                        </a>\"\"\""""

    s6_btn_replacement = s6_btn_target + """
                elif session_num == 6:
                    sim_btn = \"\"\"
                        <a href="SIMULADOR_CEREBRO_3D.html" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background:linear-gradient(135deg, #7c3aed, #6d28d9); border-color:#c084fc;" title="Abrir Simulador 3D del Cerebro Humano y Red Sináptica">
                            🧠 Ver Simulador Cerebro 3D ↗
                        </a>\"\"\""""

    if "session_num == 6:" not in content and s6_btn_target in content:
        content = content.replace(s6_btn_target, s6_btn_replacement, 1)

    # 3. En generate_custom_probador
    s6_prob_target = """    elif session_num == 5:
        btn_html = \"\"\"            <button class="btn btn-emerald" id="btnLoadSolar" style="background: rgba(251, 191, 36, 0.2); color: #fbbf24; border-color: rgba(251, 191, 36, 0.45);" title="Cargar simulador: Sistema Solar 3D Interactivo (Fotogrametría Satelital NASA)">
                🪐 Sistema Solar 3D
            </button>\"\"\"
        empty_prompt = "prueba el botón <strong>«🪐 Sistema Solar 3D»</strong>"
        ph_text = "1. Pide a Gemini que programe el simulador 3D del Sistema Solar con texturas de la NASA.\\\\n2. Haz clic en «Copiar código» en la respuesta de Gemini.\\\\n3. Pulsa Ctrl+V (o Cmd+V en Mac) aquí para pegar el código.\\\\n4. Pulsa '▶️ Ejecutar Creación' para verlo funcionar.\""""

    s6_prob_replacement = s6_prob_target + """
    elif session_num == 6:
        btn_html = \"\"\"            <button class="btn btn-emerald" id="btnLoadBrain" style="background: rgba(192, 132, 252, 0.2); color: #c084fc; border-color: rgba(192, 132, 252, 0.45);" title="Cargar simulador: Cerebro Humano 3D & Red Sináptica">
                🧠 Cerebro 3D
            </button>\"\"\"
        empty_prompt = "prueba el botón <strong>«🧠 Cerebro 3D»</strong>"
        ph_text = "1. Pide a Gemini que programe el simulador 3D del cerebro humano con red de sinapsis.\\\\n2. Haz clic en «Copiar código» en la respuesta de Gemini.\\\\n3. Pulsa Ctrl+V (o Cmd+V en Mac) aquí para pegar el código.\\\\n4. Pulsa '▶️ Ejecutar Creación' para verlo funcionar.\""""

    if "session_num == 6:" not in content and s6_prob_target in content:
        content = content.replace(s6_prob_target, s6_prob_replacement, 1)

    # Actualizar regexp en generate_custom_probador para abarcar btnLoadBrain
    content = content.replace(
        'id="btnLoad(?:Solar|Ojo)"',
        'id="btnLoad(?:Brain|Solar|Ojo)"'
    )

    # 4. En process_all_sessions sincronizar archivo SIMULADOR_CEREBRO_3D.html
    s6_copy_target = """        elif session_num == 5:
            solar_src = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES", "05_SIMULADOR_SISTEMA_SOLAR_3D.html")
            if os.path.exists(solar_src):
                try:
                    shutil.copy2(solar_src, os.path.join(session_path, "SIMULADOR_SISTEMA_SOLAR_3D.html"))
                    shutil.copy2(solar_src, os.path.join(session_path, "05_SIMULADOR_SISTEMA_SOLAR_3D.html"))
                except Exception:
                    pass"""

    s6_copy_replacement = s6_copy_target + """
        elif session_num == 6:
            brain_src = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES", "06_SIMULADOR_CEREBRO_3D.html")
            if os.path.exists(brain_src):
                try:
                    shutil.copy2(brain_src, os.path.join(session_path, "SIMULADOR_CEREBRO_3D.html"))
                    shutil.copy2(brain_src, os.path.join(session_path, "06_SIMULADOR_CEREBRO_3D.html"))
                except Exception:
                    pass"""

    if "session_num == 6:" not in content and s6_copy_target in content:
        content = content.replace(s6_copy_target, s6_copy_replacement, 1)

    with open(maps_script, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ build_mapas_and_csvs_60_sessions.py actualizado con soporte para Sesión 06")


if __name__ == "__main__":
    update_probador()
    update_catalog()
    update_maps_script()

    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    subprocess.run([sys.executable, os.path.join(scripts_dir, "build_pdf_indice_10_simulaciones_3d.py")], check=False)
    subprocess.run([sys.executable, os.path.join(scripts_dir, "build_pdf_cod_006.py")], check=False)

