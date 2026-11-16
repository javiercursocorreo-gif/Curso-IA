#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_modo_aula_limpia.py
Añade a GESTOR_CONTENIDOS_BACKEND.html el botón de "Vaciar Datos de Prueba (Aula Limpia)"
para que el profesor pueda resetear la base de datos con 1 clic antes de la clase del Día 2.
Añade en WEB_PUBLICA_CENTRO_MAYORES.html el botón directo para volver al Gestor (Backend).
"""

import os

DIR_PATH = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/GRUPO DE TRABAJO. WEB DEL CENTRO DE MAYORES"
BACKEND_FILE = os.path.join(DIR_PATH, "GESTOR_CONTENIDOS_BACKEND.html")
FRONTEND_FILE = os.path.join(DIR_PATH, "WEB_PUBLICA_CENTRO_MAYORES.html")

# 1. ACTUALIZAR GESTOR_CONTENIDOS_BACKEND.HTML
with open(BACKEND_FILE, "r", encoding="utf-8") as f:
    back_html = f.read()

old_nav_back = '''      <a href="WEB_PUBLICA_CENTRO_MAYORES.html" target="_blank" class="btn-nav">
        🌐 Ver Web Pública ➔
      </a>'''

new_nav_back = '''      <a href="WEB_PUBLICA_CENTRO_MAYORES.html" target="_blank" class="btn-nav">
        🌐 Ver Web Pública ➔
      </a>
      <button onclick="resetClassroomDatabase()" class="btn-nav" style="background: rgba(239, 68, 68, 0.2); border-color: #ef4444; color: #fca5a5; cursor: pointer;">
        🗑️ Vaciar Datos (Aula Limpia)
      </button>'''

reset_js = '''
    // ========================================================
    // MODO AULA LIMPIA: VACIAR BASE DE DATOS DE PRUEBAS
    // ========================================================
    function resetClassroomDatabase() {
      const confirmReset = confirm("⚠️ ¿Deseas VACIAR la base de datos de pruebas?\\n\\nTodo quedará limpio para que los 3 grupos de alumnos empiecen a publicar desde cero en el aula.");
      if (confirmReset) {
        localStorage.removeItem('centro_mayores_noticias_v1');
        alert("✨ Base de datos vaciada con éxito.\\nEl cascarón está 100% limpio y listo para las pruebas de los alumnos.");
        location.reload();
      }
    }
'''

if old_nav_back in back_html and "resetClassroomDatabase" not in back_html:
    back_html = back_html.replace(old_nav_back, new_nav_back)
    # inyectar función reset_js antes de </script>
    last_script_idx = back_html.rfind("</script>")
    back_html = back_html[:last_script_idx] + reset_js + back_html[last_script_idx:]
    with open(BACKEND_FILE, "w", encoding="utf-8") as f:
        f.write(back_html)
    print("✅ Botón de 'Vaciar Datos (Aula Limpia)' añadido al Backend")

# 2. ACTUALIZAR WEB_PUBLICA_CENTRO_MAYORES.HTML
with open(FRONTEND_FILE, "r", encoding="utf-8") as f:
    front_html = f.read()

old_header_front = '''      <div>
        <div class="brand-title">🏛️ Centro de Mayores</div>
        <div class="brand-subtitle">Tablón Digital Oficial • Madrid</div>
      </div>
      
    </div>'''

new_header_front = '''      <div>
        <div class="brand-title">🏛️ Centro de Mayores</div>
        <div class="brand-subtitle">Tablón Digital Oficial • Madrid</div>
      </div>
      <div style="display:flex; gap:10px; align-items:center;">
        <a href="GESTOR_CONTENIDOS_BACKEND.html" target="_blank" style="background: rgba(251, 146, 60, 0.2); border: 1px solid #fb923c; color: #fdba74; padding: 8px 14px; border-radius: 8px; text-decoration: none; font-size: 0.9rem; font-weight: 700; display: flex; align-items: center; gap: 6px;">
          ✍️ Abrir Gestor (Backend) ➔
        </a>
      </div>
    </div>'''

if old_header_front in front_html:
    front_html = front_html.replace(old_header_front, new_header_front)
    with open(FRONTEND_FILE, "w", encoding="utf-8") as f:
        f.write(front_html)
    print("✅ Botón de 'Abrir Gestor (Backend)' añadido a la cabecera de la Web Pública")

print("✨ Ambas herramientas actualizadas para el circuito de pruebas de los alumnos")
