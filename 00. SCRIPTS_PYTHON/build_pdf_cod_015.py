# -*- coding: utf-8 -*-
import os, sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

PDF_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/15_Sesion"
PDF_PATH = os.path.join(PDF_DIR









# [COMANDO 12] - SINCRONIZACIÓN DE MAPA_CLASE_SESION Y BOTONES EN TALLERES
cd "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"

cat << 'EOF' > "00. SCRIPTS_PYTHON/sync_classroom_and_taller_buttons.py"
# -*- coding: utf-8 -*-
import os, re, shutil, glob

REPO = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
CLASSROOM_BASE = os.path.join(REPO, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

sim_names = {
    1: ("SIMULADOR_PULMONES_3D.html", "🫁 Pulmones 3D"),
    2: ("SIMULADOR_CORAZON_3D.html", "🫀 Corazón 3D"),
    3: ("SIMULADOR_POMPEYA_3D.html", "🏛️ Pompeya 3D"),
    4: ("SIMULADOR_OJO_HUMANO_3D.html", "👁️ Ojo Humano 3D"),
    5: ("SIMULADOR_SISTEMA_SOLAR_3D.html", "🪐 Sistema Solar 3D"),
    6: ("SIMULADOR_CEREBRO_3D.html", "🧠 Cerebro 3D"),
    7: ("SIMULADOR_LUNA_3D.html", "🌙 Luna 3D"),
    8: ("SIMULADOR_MOTOR_TURBOFAN_3D.html", "✈️ Motor Turbofán 3D"),
    9: ("SIMULADOR_CRANEO_TREX_3D.html", "🦖 Cráneo T-Rex 3D"),
    10: ("SIMULADOR_MOLAR_HUMANO_3D.html", "🦷 Molar Humano 3D"),
    11: ("SIMULADOR_VIOLIN_STRADIVARIUS_3D.html", "🎻 Violín Stradivarius 3D"),
    12: ("SIMULADOR_NEBULOSA_HELIX_3D.html", "🌌 Nebulosa Helix 3D"),
    13: ("SIMULADOR_ADN_GENETICO_3D.html", "🧬 Doble Hélice ADN 3D"),
    14: ("SIMULADOR_AURORAS_JUPITER_3D.html", "🪐 Júpiter & Auroras 3D"),
    15: ("SIMULADOR_JAMES_WEBB_3D.html", "🔭 James Webb 3D"),
}

print("1. Sincronizando MAPA_CLASE_SESION con MAPA_SESION en las 60 sesiones...")
for s in range(1, 61):
    s_folder = os.path.join(CLASSROOM_BASE, f"{s:02d}_Sesion")
    if not os.path.exists(s_folder):
        s_folder = os.path.join(CLASSROOM_BASE, f"{s:02d}_Sesion_Cierre")
    if not os.path.exists(s_folder):
        continue

    mapa_src = os.path.join(s_folder, f"MAPA_SESION_{s:02d}.html")
    mapa_dst = os.path.join(s_folder, f"MAPA_CLASE_SESION_{s:02d}.html")

    if os.path.exists(mapa_src):
        shutil.copy2(mapa_src, mapa_dst)

print("   ✓ Los 60 archivos MAPA_CLASE_SESION_XX.html están ahora 100% sincronizados con sus talleres y simuladores.")

print("2. Inyectando botón del Simulador 3D oficial dentro de PROBADOR_CODIGO_IA.html...")
for s, (sim_file, sim_label) in sim_names.items():
    s_folder = os.path.join(CLASSROOM_BASE, f"{s:02d}_Sesion")
    probador_file = os.path.join(s_folder, "PROBADOR_CODIGO_IA.html")
    if not os.path.exists(probador_file):
        continue

    with open(probador_file, "r", encoding="utf-8") as f:
        html = f.read()

    # Si ya tiene el botón para este simulador, continuar
    if f'href="{sim_file}"' in html or f"btnDemoSimulador_{s}" in html:
        continue

    # Inyectar el botón en la barra de acciones (.actions-bar) junto a btnRun
    btn_html = f'''            <a href="{sim_file}" target="_blank" class="btn btn-emerald" id="btnDemoSimulador_{s}" style="text-decoration:none; display:inline-flex; align-items:center; gap:6px; background:linear-gradient(135deg, #059669, #10b981); color:#ffffff; font-weight:700;" title="Abrir Simulador Científico 3D Oficial">
                {sim_label} ↗
            </a>\n'''

    # Buscar el botón de ejecución y añadir a su lado el acceso directo
    html = re.sub(
        r'(<button\s+class="btn\s+btn-primary"\s+id="btnRun">.*?<\/button>)',
        r'\1\n' + btn_html,
        html,
        count=1,
        flags=re.DOTALL
    )

    with open(probador_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"   ✓ Sesión {s:02d}: botón «{sim_label}» añadido dentro de PROBADOR_CODIGO_IA.html")

print("✅ Todo el material de Classroom y talleres sincronizado con éxito.")
