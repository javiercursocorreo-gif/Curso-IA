# REGLAS DEL PROYECTO (CURSO-IA)

## Flujo de Trabajo Automatizado y Cero Interrupciones (Auto-Execution)
- **Eliminación de Confirmaciones y Botones de Submit/Proceed:**
  - El asistente NUNCA debe solicitar confirmación manual ni requerir feedback interactivo para ejecutar planes o artefactos (`RequestFeedback: false`).
  - Todos los planes, modificaciones de código y tareas deben ejecutarse de forma directa, continua e ininterrumpida.
- **Ejecución de Comandos y Terminal Sandbox:**
  - Ejecutar prioritariamente todos los comandos en modo estándar dentro del Sandbox (`BypassSandbox: false`) para permitir la auto-ejecución inmediata sin interrupciones al usuario.
  - Mantener comandos limpios, atómicos y directos (sin envoltorios innecesarios como `eval`, `xargs` o subshells complejas `$()`) para garantizar la auto-aprobación del sistema.
  - Cuando se requiera interactuar con el sistema (como abrir Chrome o gestionar procesos/scripts), hacerlo de forma concisa y directa.
- **PROHIBICIÓN TOTAL DE SUBMITS Y RÁFAGAS DE COMANDOS EN EL CHAT:**
  - El asistente tiene **TERMINANTEMENTE PROHIBIDO** encadenar comandos de terminal de prueba, inspección o scripts pesados en el chat que provoquen solicitudes de Submit / Aprobación en la pantalla del usuario.
  - Cuando se requiera procesar, inspeccionar o extraer información de archivos pesados (como PDFs, scripts complejos o tareas de sistema), el asistente NUNCA intentará ejecutar scripts exploratorios en bucle.
  - El asistente debe generar directamente el bloque de comando terminal limpio para que el usuario lo ejecute en su propia terminal externa sin ninguna interrupción en la interfaz.

## Regla de Oro: Sincronización Inmediata Simulador 3D ⟷ Prompt de Gemini en Ficha [COD]
- **Sincronización Biunívoca en Tiempo Real:**
  - Cada vez que se agregue, modifique, elimine o ajuste cualquier característica técnica, visual, botón o funcionalidad interactiva en un simulador (o en el probador de código), el asistente DEBE actualizar simultáneamente en ese mismo turno el **Prompt Maestro para Gemini** en el script generador de la ficha didáctica `build_pdf_cod_XXX.py` y regenerar el PDF oficial del alumno.
  - El alumno debe poder copiar el prompt de su ficha en Gemini y obtener exactamente el 100% de las funciones implementadas en el simulador oficial.
  - Confirmar explícitamente en la respuesta al usuario que dicha sincronización ha quedado sellada en la ficha.

## Regla de Despliegue: Todo se Sube a GitHub Siempre (GitHub Pages & Classroom)
- **Subida Obligatoria a GitHub en Cada Turno:**
  - Todo cambio, corrección, regeneración de PDF, mapa o simulador DEBE incluir siempre e indefectiblemente el bloque de subida a GitHub (`git add -A`, `git commit` y `git push origin main`) en el comando del terminal para el usuario, aunque el usuario no lo pida explícitamente.
  - Esto garantiza que Google Classroom y GitHub Pages reflejen en tiempo real el estado real del proyecto sin desfases ni versiones obsoletas en caché.
- **Formato Estándar y Numeración Correlativa Obligatoria de Comandos en Terminal:**
  - **Título en Canvas / Chat:** Cada bloque de comandos entregado al usuario debe llevar un título claro y visible en Markdown destacando su numeración correlativa (ej. `### 💻 [COMANDO 01] - Título Descriptivo`).
  - **Título y Numeración Correlativa DENTRO del Comando:** Es VITAL y obligatorio que dentro del propio bloque de script el encabezado con `#` y los mensajes `echo` lleven exactamente la misma numeración correlativa secuencial (`[COMANDO 01]`, `[COMANDO 02]`, etc.) y el título descriptivo para que el usuario pueda identificar y seguir de forma inequívoca qué tarea se ejecuta en el scroll de su terminal externa cuando ejecuta varios comandos seguidos:
    ```bash
    # ==============================================================================
    # [COMANDO XX] - TÍTULO DESCRIPTIVO DE LA TAREA
    # ==============================================================================
    cd "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
    echo "=== [COMANDO XX] INICIANDO: TÍTULO DESCRIPTIVO ==="
    # ... instrucciones ...
    echo "=== [COMANDO XX] FINALIZADO CON ÉXITO ==="
    ```

## Estándar de Simulaciones 3D: Motor Babylon.js y Modelos Científicos Hiperrealistas
- **Prohibición de Mallas Inventadas o Procedurales Primitivas:**
  - Queda terminantemente prohibido generar órganos o artefactos mediante esferas, conos o cilindros básicos deformados por código (evitar acabados toscos o irreales).
  - Toda simulación anatómica o científica debe emplear modelos 3D hiperrealistas reales (`.glb` / `.gltf`) procedentes de fuentes y repositorios científicos contrastados (NIH 3D Print Exchange, resonancias médicas reales, fotogrametría PBR 4K, NASA).
- **Motor 3D Predeterminado (Babylon.js):**
  - El motor estándar y prioritario para los laboratorios y simuladores 3D es **Babylon.js** (`babylon.js` + `babylonjs.loaders.min.js`), con sistema PBR, iluminación médica y shaders orgánicos.
- **Arquitectura de Carga y Autonomía (Base64 + CDN Fallback):**
  - Los modelos científicos deben estar respaldados en archivos `_b64.js` en `03_ASSETS_3D_Y_DATOS/` (ej. `brain_b64.js`, `heart_b64.js`, `lungs_b64.js`) para garantizar funcionamiento 100% offline y autónomo sin problemas de CORS ni caídas de servidor.

## Validación Visual Inmediata: Lanzamiento Automático en Google Chrome
- **Apertura Local Inmediata en Navegador:**
  - En cada turno donde se cree, ajuste, corrija o modifique cualquier simulador, probador de código o mapa interactivo, el asistente DEBE lanzar/abrir siempre automáticamente dicho archivo HTML en **Google Chrome** en local (ej. `open -a "Google Chrome" "/ruta/al/archivo.html"`).
  - Esto permite al usuario inspeccionar, interactuar y validar visualmente el resultado de inmediato en su pantalla en 2 segundos, sin demoras y sin tener que esperar los minutos que toma la subida pesada y despliegue en Google Classroom / GitHub Pages.




