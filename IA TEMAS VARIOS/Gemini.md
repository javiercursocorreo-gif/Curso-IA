# Gemini Directives & Workspace Protocol: IA TEMAS VARIOS

Instrucciones de comportamiento, perfil y protocolos de trabajo para el modelo Gemini dentro del proyecto matriz **IA TEMAS VARIOS**.

---

## 🔒 1. Directiva Principal: Ejecución en Sandbox

* **Modo Estricto:** Ejecuta todas las herramientas bajo el Sandbox estándar (`BypassSandbox: false`).
* **Sin Interrupciones / Sin Popups:** No uses mecanismos que obliguen al usuario a pulsar botones de aprobación o ventanas modales intermedias (`BypassSandbox: true` no solicitado, formularios interactivos innecesarios). Resuelve todo de manera autónoma con las capacidades internas.
* **Comando Terminal de Cierre:** Si hay tareas que requieren acceso al sistema operativo fuera del sandbox (por ejemplo, abrir documentos con Vista Previa/Preview, sincronizar carpetas en iCloud Drive o listar directorios externos), **proporciona al final de la respuesta el comando exacto de terminal (zsh/bash)** para que el usuario solo tenga que copiarlo y ejecutarlo.

---

## 📁 2. Organización del Espacio de Trabajo

* **Carpeta Matriz:** `IA TEMAS VARIOS` es el directorio central del proyecto.
* **Gobierno de la Raíz:** Los archivos de directrices (`Agents.md` y `Gemini.md`) residen en la raíz de `IA TEMAS VARIOS`.
* **Segmentación por Carpetas Temáticas:** Cada consulta, patología o temática se creará dentro de su respectiva subcarpeta (`INFECCIONES DE ORINA/`, `ESPALDA/`, etc.). Ningún archivo de consulta debe quedar suelto en la raíz si corresponde a una subtemática.

---

## ⚕️ 3. Directivas de Contenido Médico y Salud

1. **Interpretación Rigurosa:**
   - Categorizar siempre según criterios clínicos establecidos (**Sensible**, **Intermedio / Sensible con exposición incrementada**, **Resistente**).
   - Las CMI no son comparables entre diferentes familias de antibióticos.
   - Resaltar resistencias intrínsecas (ej. *Proteus* frente a Nitrofurantoína).
2. **Estructura y Claridad:**
   - Emplear tablas comparativas de fácil lectura distinguiendo fármacos orales de primera línea frente a hospitalarios/intravenosos.
   - Indicar claramente signos de alarma (fiebre, dolor lumbar, malestar general) que diferencien procesos leves de infecciones altas o complicadas.

---

## 📄 4. Estándares de Salida y Generación de Documentos

* **Documentación PDF:** Acabado editorial profesional: encabezados, números de página ("Página X de Y"), márgenes limpios, tablas visuales y bloques de alerta.
* **Navegabilidad:** Proporcionar enlaces en formato Markdown con esquema `file://` para que el usuario pueda abrir directamente cualquier archivo creado o editado.
