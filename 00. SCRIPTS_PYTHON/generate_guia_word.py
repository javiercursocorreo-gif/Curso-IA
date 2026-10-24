#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_guia_word.py
Genera la Guía de Publicación en formato HTML y RTF con diseño profesional,
para que Microsoft Word y Pages la abran 100% limpia sin errores de 'texto legible'.
"""

import os
import sys

COMUN_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-IA-COMUN"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>GUÍA DE PUBLICACIÓN EN GITHUB Y CLASSROOM</title>
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.6;
    max-width: 900px;
    margin: 40px auto;
    padding: 0 24px;
  }
  h1 {
    color: #0369a1;
    font-size: 26px;
    border-bottom: 3px solid #0284c7;
    padding-bottom: 12px;
    text-align: center;
  }
  .subtitulo {
    text-align: center;
    color: #64748b;
    font-size: 15px;
    margin-bottom: 30px;
    font-style: italic;
  }
  .box-info {
    background-color: #f0f9ff;
    border-left: 5px solid #0284c7;
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 4px;
  }
  .box-alert {
    background-color: #fef2f2;
    border-left: 5px solid #ef4444;
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 4px;
  }
  h2 {
    color: #0f172a;
    font-size: 19px;
    margin-top: 32px;
    background: #f8fafc;
    padding: 10px 14px;
    border-radius: 6px;
    border-left: 4px solid #3b82f6;
  }
  h3 {
    color: #334155;
    font-size: 16px;
    margin-top: 20px;
  }
  ul, ol {
    padding-left: 24px;
  }
  li {
    margin-bottom: 8px;
  }
  code {
    background-color: #f1f5f9;
    color: #d97706;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: Menlo, Monaco, Consolas, monospace;
    font-size: 14px;
  }
  pre {
    background-color: #1e293b;
    color: #f8fafc;
    padding: 16px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 13px;
    line-height: 1.45;
  }
  .id-badge {
    background-color: #10b981;
    color: white;
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: bold;
    font-size: 14px;
  }
  .id-badge-ia {
    background-color: #6366f1;
    color: white;
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: bold;
    font-size: 14px;
  }
</style>
</head>
<body>

<h1>GUÍA DE PUBLICACIÓN EN GITHUB Y CLASSROOM</h1>
<div class="subtitulo">Workflow de Trabajo en Equipo: Tú (Profesor) y Antigravity (Asistente IA)</div>

<div class="box-info">
  <strong>💡 Introducción al Sistema Unificado:</strong><br>
  Este flujo de trabajo garantiza que todo el material educativo (teoría, simuladores interactivos, fichas [COD] y monográficos) viaje desde tu Mac hasta Google Classroom sin coste de almacenamiento en Google Drive y con una experiencia 100% limpia para los alumnos mediante <strong>Mapas Interactivos HTML únicos</strong>.
</div>

<h2>FASE 1: PREPARACIÓN LOCAL EN EL MAC 🧑🏻‍🏫 TAREA TUYA</h2>
<ol>
  <li>Escribe tu teoría, genera tus PDFs, graba los vídeos y organiza todo en la carpeta correspondiente de tu Mac.</li>
  <li>Nombra los archivos correctamente (ej: <code>T0.DEBATE.pdf</code>, <code>T2.VIDEO.mp4</code>, etc.).</li>
</ol>

<h2>FASE 2: SINCRONIZACIÓN AL SERVIDOR (GITHUB) 🤖 TAREA DE LA IA</h2>
<p>Tú me dices: <em>"Ya he metido todos los archivos nuevos en la carpeta del Mac, súbelos a GitHub"</em>.</p>
<p>Yo (la IA) me encargo de:</p>
<ul>
  <li>Añadir los archivos creados o modificados.</li>
  <li>Hacer el commit y enviarlos a la nube (<code>git push</code>) mediante el bloque de comandos correlativo.</li>
  <li><strong>Objetivo:</strong> Alojarlos gratis en GitHub Pages para que Google Classroom pueda enlazarlos sin gastar espacio en tu Google Drive. Si algún día editas un archivo, solo tienes que pedirme que lo vuelva a subir y se actualizará automáticamente para todos tus alumnos sin tocar Classroom.</li>
</ul>

<h2>FASE 3: CREACIÓN DEL PANEL UNIFICADO DE ENLACES 🤖 TAREA DE LA IA</h2>
<p>Tú me dices: <em>"Genera el CSV unificado con los enlaces actualizados"</em>.</p>
<p>Yo (la IA) me encargo de:</p>
<ul>
  <li>Escanear las carpetas y generar el archivo maestro <strong><code>CURSO_IA_UNIFICADO.csv</code></strong> (dentro de <code>PANELES_CSV/</code>).</li>
  <li><strong>Arquitectura de Mapa Único:</strong> En lugar de saturar Classroom con docenas de enlaces sueltos, cada sección cuenta con un <strong>Mapa Interactivo HTML único</strong> (<code>MAPA_MONOGRAFICOS.html</code> para todos los monográficos y <code>MAPA_SESION_XX.html</code> para cada sesión).</li>
</ul>

<h2>FASE 4: PREPARACIÓN DE GOOGLE CLASSROOM 🧑🏻‍🏫 TAREA TUYA</h2>
<ol>
  <li>Entra en <code>classroom.google.com</code> con tu cuenta de profesor.</li>
  <li>Trabajamos con las <strong>Clases Maestras Unificadas Anuales</strong>:
    <ul>
      <li><strong>CLASE DE IA (Curso Completo Anual):</strong> Nombre: <code>IA.</code> &nbsp;--->&nbsp; <span class="id-badge-ia">ID REAL: 890436514251</span></li>
      <li><strong>CLASE DE ROBÓTICA (Curso Completo Anual):</strong> Nombre: <code>ROBÓTICA.</code> &nbsp;--->&nbsp; <span class="id-badge">ID REAL: 890435922022</span></li>
    </ul>
  </li>
</ol>

<h2>FASE 5: INGESTA DE DATOS (GOOGLE SHEETS) 🧑🏻‍🏫 TAREA TUYA</h2>
<ol>
  <li>Abre tu navegador en <strong>Modo Incógnito / Ventana Privada</strong> (vital para evitar conflictos entre cuentas de Google).</li>
  <li>Entra a Google Drive y abre tu hoja permanente: <strong><code>0.PANEL_CLASSROOM</code></strong>.</li>
  <li>Ve a <strong>Archivo &gt; Importar &gt; Subir</strong> y arrastra el archivo maestro:
    <ul>
      <li>Para IA: <strong><code>PANELES_CSV/CURSO_IA_UNIFICADO.csv</code></strong></li>
    </ul>
  </li>
  <li>Selecciona <strong>Reemplazar hoja de cálculo actual</strong> y pulsa <strong>Importar</strong>.</li>
  <li>En la <strong>Columna A (<code>ID_CURSO</code>)</strong>, pega el ID real de la clase:
    <ul>
      <li>Para IA: <code>890436514251</code></li>
      <li>Arrastra el número hacia abajo para que todas las filas tengan el ID.</li>
    </ul>
  </li>
</ol>

<h2>FASE 6: PUBLICACIÓN AUTOMÁTICA 🧑🏻‍🏫 TAREA TUYA</h2>
<ol>
  <li>Dentro de la hoja de Google Sheets, ve a <strong>Extensiones &gt; Apps Script</strong>.</li>
  <li>Selecciona la función <strong><code>publicarTodoConTemas</code></strong> y pulsa <strong>Ejecutar</strong>.</li>
  <li>El script creará automáticamente los Temas en Classroom (<code>MONOGRAFICOS</code> y <code>SESIÓN 1</code> a <code>SESIÓN 60</code>) y cargará todos los mapas interactivos en modo <strong>BORRADOR</strong> (DRAFT).</li>
  <li>¡Listo! Ya puedes ir publicándolos a los alumnos según avance el calendario de clases.</li>
</ol>

<div class="box-alert">
  <h2>🚨 ANEXO 1: EL BOTÓN DEL PÁNICO (RESET COMPLETO DE CLASE) 🧑🏻‍🏫 TAREA TUYA</h2>
  <p>Si la subida ha quedado desfasada o necesitas borrar TODO de Classroom para empezar de cero:</p>
  <ol>
    <li>Asegúrate de que el ID de la clase está puesto en la celda <strong>A2</strong> de la hoja (ej: <code>890436514251</code>).</li>
    <li>Ve a <strong>Extensiones &gt; Apps Script</strong>, selecciona la función <strong><code>borrarAbsolutamenteTodo</code></strong> y pulsa <strong>Ejecutar</strong>.</li>
    <li>Toda la clase (Temas, Materiales y Borradores) quedará borrada en segundos.</li>
  </ol>
</div>

<h2>📋 ANEXO 2: LISTADO MAESTRO DE IDs DE TUS CLASES</h2>

<h3>🟢 CLASES MAESTRAS VIGENTES (MODELO UNIFICADO ANUAL)</h3>
<ul>
  <li><strong>IA (Curso Completo Anual):</strong> <code>ID REAL: 890436514251</code></li>
  <li><strong>ROBÓTICA (Curso Completo Anual):</strong> <code>ID REAL: 890435922022</code></li>
</ul>

<h3>📦 HISTORIAL DE CLASES Y LOTES ANTERIORES (ARCHIVADAS / FÓSILES)</h3>
<ul>
  <li><em>IA.MONOGRÁFICOS:</em> <code>ID REAL: 877999132773</code></li>
  <li><em>IA1 (Sesiones 01 a 15):</em> <code>ID REAL: 826134766630</code></li>
  <li><em>IA2 (Sesiones 16 a 30):</em> <code>ID REAL: 877174620039</code></li>
  <li><em>IA3 (Sesiones 31 a 45):</em> <code>ID REAL: 877172188045</code></li>
  <li><em>IA4 (Sesiones 46 a 60):</em> <code>ID REAL: 826136245220</code></li>
  <li><em>IA.ÍNDICE:</em> <code>ID REAL: 877993104492</code></li>
  <li><em>ROB+IA. Introducción:</em> <code>ID REAL: 876317836453</code></li>
  <li><em>Bloque 1: ROB1.Un motor:</em> <code>ID REAL: 876316970006</code></li>
  <li><em>Bloque 2: ROB2.Sensores-Decisiones:</em> <code>ID REAL: 876801831599</code></li>
  <li><em>Bloque 3: ROB3.Mov Avanzado:</em> <code>ID REAL: 876804534725</code></li>
  <li><em>Bloque 4: ROB4.Brazo robótico:</em> <code>ID REAL: 876848630130</code></li>
  <li><em>Bloque 5: ROB5.Androides:</em> <code>ID REAL: 876849927384</code></li>
  <li><em>Bloque 6: ROB6.Naves espaciales:</em> <code>ID REAL: 876845244997</code></li>
  <li><em>Bloque 7: ROB7.Exploracion Espacial:</em> <code>ID REAL: 869853775914</code></li>
</ul>

<h2>⚙️ ANEXO 3: EL CÓDIGO MAESTRO DE APPS SCRIPT (Copia de Seguridad)</h2>
<pre>
// 1. AVERIGUAR IDs
function dimeMisIDs() {
  var cursos = Classroom.Courses.list().courses;
  if (cursos && cursos.length > 0) {
    for (var i = 0; i < cursos.length; i++) {
      Logger.log("Curso: " + cursos[i].name + "  --->  ID REAL: " + cursos[i].id);
    }
  } else {
    Logger.log("No tienes cursos en esta cuenta.");
  }
}

// 2. PUBLICAR AGRUPADO POR TEMAS (EN BORRADOR)
function publicarTodoConTemas() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = sheet.getDataRange().getValues();
  var temasCacheados = {}; 
  for (var i = 1; i < data.length; i++) {
    var fila = data[i];
    var cursoId = String(fila[0]).trim();
    var claseNombre = String(fila[1]).trim();
    var titulo = fila[2];
    var descripcion = fila[3];
    var urlGitHub = fila[4];
    
    if (!cursoId || cursoId === "") continue; 
    
    var topicId = null;
    if (claseNombre !== "") {
      var cacheKey = cursoId + "_" + claseNombre;
      if (temasCacheados[cacheKey]) {
        topicId = temasCacheados[cacheKey];
      } else {
        var existe = false;
        try {
          var response = Classroom.Courses.Topics.list(cursoId);
          var temas = response.topic || [];
          for (var t = 0; t < temas.length; t++) {
            if (temas[t].name === claseNombre) {
              topicId = temas[t].topicId;
              existe = true;
              break;
            }
          }
        } catch(e) {}
        
        if (!existe) {
          try {
            var nuevoTema = Classroom.Courses.Topics.create({name: claseNombre}, cursoId);
            topicId = nuevoTema.topicId;
          } catch(e) {}
        }
        if (topicId) temasCacheados[cacheKey] = topicId;
      }
    }
    
    var material = {
      title: titulo,
      description: descripcion,
      materials: [{ link: { url: urlGitHub } }],
      state: "DRAFT"
    };
    
    if (topicId) material.topicId = topicId;
    
    try {
      Classroom.Courses.CourseWorkMaterials.create(material, cursoId);
    } catch(e) {}
  }
}

// 3. BOTÓN DEL PÁNICO (BORRAR TODO)
function borrarAbsolutamenteTodo() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var cursoId = String(sheet.getRange("A2").getValue()).trim();
  
  if (!cursoId || cursoId === "") {
    SpreadsheetApp.getUi().alert("Error: Introduce el ID del curso en la celda A2 antes de borrar.");
    return;
  }
  
  var pageTokenMats = null;
  do {
    try {
      var params = { courseWorkMaterialStates: ["DRAFT", "PUBLISHED"] };
      if (pageTokenMats) params.pageToken = pageTokenMats;
      
      var response = Classroom.Courses.CourseWorkMaterials.list(cursoId, params);
      var mats = response.courseWorkMaterial || [];
      for (var i = 0; i < mats.length; i++) {
        Classroom.Courses.CourseWorkMaterials.remove(cursoId, mats[i].id);
      }
      pageTokenMats = response.nextPageToken;
    } catch(e){
      break;
    }
  } while (pageTokenMats);
  
  var pageTokenTemas = null;
  do {
    try {
      var paramsTemas = {};
      if (pageTokenTemas) paramsTemas.pageToken = pageTokenTemas;
      
      var responseTemas = Classroom.Courses.Topics.list(cursoId, paramsTemas);
      var temas = responseTemas.topic || [];
      for (var t = 0; t < temas.length; t++) {
        Classroom.Courses.Topics.remove(cursoId, temas[t].topicId);
      }
      pageTokenTemas = responseTemas.nextPageToken;
    } catch(e){
      break;
    }
  } while (pageTokenTemas);
}
</pre>

</body>
</html>
"""

def main():
    destinos = [
        os.path.join(COMUN_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.html"),
        os.path.join(IA_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.html"),
    ]
    for d in destinos:
        os.makedirs(os.path.dirname(d), exist_ok=True)
        with open(d, "w", encoding="utf-8") as f:
            f.write(HTML_TEMPLATE)
        print(f"✅ HTML generado: {d}")

if __name__ == "__main__":
    main()

