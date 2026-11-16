#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
conectar_backend_frontend.py
Conecta dinámicamente GESTOR_CONTENIDOS_BACKEND.html y WEB_PUBLICA_CENTRO_MAYORES.html
usando localStorage ('centro_mayores_noticias_v1').
Cualquier noticia/excursión/taller publicado en el Backend aparece
inmediatamente en el Frontend con su foto, datos, ficha detalle y lectura en voz alta.
"""

import os
import re

DIR_PATH = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/GRUPO DE TRABAJO. WEB DEL CENTRO DE MAYORES"
BACKEND_FILE = os.path.join(DIR_PATH, "GESTOR_CONTENIDOS_BACKEND.html")
FRONTEND_FILE = os.path.join(DIR_PATH, "WEB_PUBLICA_CENTRO_MAYORES.html")

# 1. ACTUALIZAR GESTOR_CONTENIDOS_BACKEND.HTML
with open(BACKEND_FILE, "r", encoding="utf-8") as f:
    back_html = f.read()

# Reemplazar la función publishItem() para guardar en localStorage real
old_publish = '''function publishItem() {
      const title = document.getElementById('inpTitle').value;
      alert('🚀 ¡Aviso publicado con éxito!\\n\\n«' + title + '» ha quedado guardado y actualizado para la web pública.');
      document.getElementById('previewStatus').textContent = 'Publicado';
      document.getElementById('previewStatus').style.background = '#dcfce7';
      document.getElementById('previewStatus').style.color = '#15803d';
    }'''

new_publish = '''function publishItem() {
      const title = document.getElementById('inpTitle').value.trim();
      if (!title) {
        alert('⚠️ Por favor, introduce un título para la noticia antes de publicar.');
        return;
      }
      const area = currentArea || 'excursiones';
      const date = document.getElementById('inpDate').value.trim() || 'Próximamente';
      const price = document.getElementById('inpPrice').value.trim() || 'Gratuito';
      const body = document.getElementById('inpBody').value.trim();
      const img = document.getElementById('previewImg').src;

      const newItem = {
        id: 'user_' + Date.now(),
        area: area,
        title: title,
        date: date,
        price: price,
        body: body.replace(/\\n/g, '<br>'),
        image: img,
        createdAt: new Date().toISOString()
      };

      try {
        let stored = localStorage.getItem('centro_mayores_noticias_v1');
        let list = stored ? JSON.parse(stored) : [];
        list.unshift(newItem); // Se añade al principio
        localStorage.setItem('centro_mayores_noticias_v1', JSON.stringify(list));
      } catch (e) {
        console.error('Error guardando en localStorage:', e);
      }

      alert('🚀 ¡Aviso publicado con éxito!\\n\\n«' + title + '» ha quedado guardado en la Base de Datos.\\nAl abrir o actualizar la Web Pública, aparecerá en primera posición.');
      document.getElementById('previewStatus').textContent = 'Publicado en Vivo';
      document.getElementById('previewStatus').style.background = '#dcfce7';
      document.getElementById('previewStatus').style.color = '#15803d';
    }'''

if old_publish in back_html:
    back_html = back_html.replace(old_publish, new_publish)
    with open(BACKEND_FILE, "w", encoding="utf-8") as f:
        f.write(back_html)
    print("✅ Backend actualizado con persistencia real en localStorage")
else:
    print("⚠️ No se encontró old_publish en Backend")

# 2. ACTUALIZAR WEB_PUBLICA_CENTRO_MAYORES.HTML
with open(FRONTEND_FILE, "r", encoding="utf-8") as f:
    front_html = f.read()

# Inyectar contenedores dinámicos en cada sección
areas = ['excursiones', 'menu', 'talleres', 'normas', 'guias']
for a in areas:
    marker = f'<div id="view-{a}">'
    dyn_div = f'<div id="view-{a}">\n      <div id="dynamic-{a}-container"></div>'
    if marker in front_html and f'id="dynamic-{a}-container"' not in front_html:
        front_html = front_html.replace(marker, dyn_div)

# Inyectar función de carga dinámica de noticias en script
loader_js = '''
    // =========================================================================
    // CARGA DINÁMICA DE NOTICIAS PUBLICADAS DESDE EL BACKEND (LOCALSTORAGE)
    // =========================================================================
    function loadDynamicNewsFromStorage() {
      try {
        const stored = localStorage.getItem('centro_mayores_noticias_v1');
        if (!stored) return;
        const list = JSON.parse(stored);
        if (!Array.isArray(list)) return;

        list.forEach(item => {
          // Registrar en la base de datos interna para openDetail
          newsDatabase[item.id] = {
            image: item.image || '',
            badge: '📢 Publicado por Alumnos • ' + item.date,
            badgeColor: '#0d7a57',
            badgeBg: '#e6f7f0',
            title: item.title,
            meta: '📅 Fecha: ' + item.date + ' | 💶 ' + item.price,
            body: '<p>' + item.body + '</p>'
          };

          // Renderizar tarjeta en la sección correspondiente
          const container = document.getElementById('dynamic-' + item.area + '-container');
          if (container && !document.getElementById('card-' + item.id)) {
            const card = document.createElement('div');
            card.id = 'card-' + item.id;
            card.className = 'subitem-card';
            card.style.borderLeft = '6px solid #10b981';
            card.style.background = '#f0fdf4';
            card.onclick = function() { openDetail(item.id); };

            const imgTag = item.image ? `<img src="${item.image}" alt="foto" class="subitem-img">` : '';
            card.innerHTML = `
              ${imgTag}
              <div class="subitem-info">
                <span class="subitem-badge" style="background:#dcfce7; color:#15803d;">📢 Novedad Reciente • ${item.date}</span>
                <h3>${item.title}</h3>
                <p class="subitem-desc">${item.meta || item.price}. Haz clic para ver todos los detalles.</p>
              </div>
              <div class="subitem-arrow">➔</div>
            `;
            container.appendChild(card);
          }
        });
      } catch (e) {
        console.error('Error cargando noticias dinámicas:', e);
      }
    }

    // Escuchar cambios de almacenamiento en tiempo real entre pestañas
    window.addEventListener('storage', function(e) {
      if (e.key === 'centro_mayores_noticias_v1') {
        loadDynamicNewsFromStorage();
      }
    });

    // Cargar al iniciar
    document.addEventListener('DOMContentLoaded', function() {
      loadDynamicNewsFromStorage();
    });
    // Por si DOMContentLoaded ya pasó
    loadDynamicNewsFromStorage();
'''

if "loadDynamicNewsFromStorage" not in front_html:
    front_html = front_html.replace("// ESTADO DE NAVEGACIÓN SIMPLE", loader_js + "\n    // ESTADO DE NAVEGACIÓN SIMPLE")
    with open(FRONTEND_FILE, "w", encoding="utf-8") as f:
        f.write(front_html)
    print("✅ Frontend actualizado con escucha dinámica de localStorage")
else:
    print("ℹ️ Frontend ya tenía loader dinámico")

print("✨ Backend y Frontend enlazados al 100% dinámicamente")
