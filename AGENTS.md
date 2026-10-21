# REGLAS DEL PROYECTO (CURSO-IA)

## Flujo de Trabajo Automatizado y Cero Interrupciones (Auto-Execution)
- **PROHIBICIÓN ABSOLUTA DE SUBMITS Y VENTANAS DE APROBACIÓN EN EL CHAT:**
  - El asistente tiene **TERMINANTEMENTE PROHIBIDO** ejecutar comandos o acciones que provoquen la aparición de botones de "Submit", "Aprobar", confirmaciones o ventanas emergentes en la pantalla del usuario.
  - Queda **ESTRICTAMENTE PROHIBIDO** ejecutar herramientas de terminal intermedias (`run_command`) para inspección exploratoria de sistema, red o procesos (`ifconfig`, `lsof`, `ps`, `curl`, scripts de terminal de prueba, etc.) durante el turno de conversación.
  - Toda la lectura, análisis, creación y edición de código debe ejecutarse de forma 100% silenciosa y desatendida mediante herramientas de edición de archivos (`read_file`, `edit_file`, `write_file`).
  - Al final de la respuesta, el asistente debe entregar directamente y sin interrupciones previas **UN ÚNICO BLOQUE DE COMANDO DE TERMINAL LIMPIO Y NUMERADO** para que el usuario lo ejecute en su propia terminal externa.
- **Eliminación de Confirmaciones y Botones de Proceed:**
  - El asistente NUNCA debe solicitar confirmación manual ni requerir feedback interactivo para ejecutar planes o artefactos (`RequestFeedback: false`).
  - Todos los planes, modificaciones de código y tareas deben ejecutarse de forma directa, continua e ininterrumpida.

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

## Validación Visual Inmediata: Lanzamiento Automático en Safari (Respeto de Reposo de Pantalla)
- **Apertura Local Inmediata en Navegador Nativo (Safari):**
  - En cada turno donde se cree, ajuste, corrija o modifique cualquier simulador, probador de código o mapa interactivo, el asistente DEBE lanzar/abrir siempre automáticamente dicho archivo HTML en **Safari** en local (ej. `open -a "Safari" "/ruta/al/archivo.html"`).
  - Esto garantiza que el motor WebKit de Safari respete al 100% el apagado y reposo automático de las pantallas (`displaysleep`) sin generar bloqueos de `Blink Wake Lock` (reservando Google Chrome exclusivamente para entornos con soporte Web MIDI en cursos musicales).
  - Permite al usuario inspeccionar, interactuar y validar visualmente el resultado de inmediato en su pantalla en 2 segundos, sin demoras y sin tener que esperar los minutos que toma la subida pesada y despliegue en Google Classroom / GitHub Pages.

## Estándar de Activos Visuales: Prohibición Total de Imágenes Generadas por IA (GenAI) y Búsqueda Exclusiva en Repositorios Científicos Oficiales
- **PROHIBICIÓN TOTAL DE IMÁGENES GENERADAS POR IA:**
  - Queda TERMINANTEMENTE PROHIBIDO utilizar modelos generadores de imágenes por IA (Midjourney, DALL-E, Imagen, subagentes `image-generator`, etc.) para crear o inventar fotografías científicas.
  - Ninguna simulación ni recurso didáctico puede contener fotografías sintéticas o generadas por IA.
- **BÚSQUEDA EXCLUSIVA EN REPOSITORIOS CIENTÍFICOS OFICIALES Y DATOS REALES:**
  - Todas las fotografías, tomografías, fotogrametrías, cortes histológicos y mapas de textura deben ser **AUTÉNTICOS DATOS CIENTÍFICOS REALES** procedentes de fuentes institucionales y académicas oficiales:
    - **NASA / JPL / LRO / ESA:** Fotografía satelital astronómica real, mapas altimétricos láser LOLA, misiones espaciales.
    - **NIH (National Institutes of Health) / U.S. National Library of Medicine:** Escaneos médicos y anatómicos reales, tomografías axiales computarizadas (TC/TAC), resonancias magnéticas (RM), microtomografías y cortes histológicos de tejido humano real (como los usados para corazón, pulmones y anatomía médica).
    - **Museos Científicos y Repositorios Paleontológicos (AMNH, FMNH Chicago, Smithsonian, Natural History Museum):** Fotogrametrías y fotografías de archivo de fósiles y especímenes de colección reales.
    - **Sociedades de Ingeniería Mecánica y Archivos Técnicos (SAE, ISO, esquemas de corte fidedignos de automoción):** Fotografía y planos de sección real de ingeniería mecánica.
  - Los activos obtenidos de estas fuentes deben respaldarse en Base64 en `03_ASSETS_3D_Y_DATOS/` para garantizar funcionamiento autónomo y 100% offline sin dependencias externas.

## Metodología Didáctica: La Triple Salvaguarda Pedagógica (Terna de Seguridad Total)
- **Las Tres Capas de Seguridad en Cada Sesión:**
  Para evitar que la variabilidad de Gemini o fallos técnicos en los PCs dejen rezagado a ningún alumno en el aula, toda sesión debe articularse bajo la Triple Salvaguarda:
  1. **Nivel 1 (Experiencia Activa): El Prompt Semilla en 2 Pasos:**
     - En lenguaje humano natural, conceptual y sin jerga técnica (4 a 6 líneas).
     - El alumno define el "QUÉ" y pide a la IA que explique en 3 viñetas su enfoque antes de entregar el código HTML.
  2. **Nivel 2 (Red Intermedia): El Prompt Maestro Técnico Detallado:**
     - El plano de especificaciones exhaustivo de ingeniería de software incluido en el anexo de la ficha como respaldo técnico si Gemini duda.
  3. **Nivel 3 (Garantía Total): La App / Simulador Oficial Terminado:**
     - El archivo HTML oficial completo, 100% depurado, probado y desplegado en Classroom y GitHub Pages. Si a un alumno se le corta o bloquea su IA, abre directamente el enlace oficial y sigue la clase sin frustración.

## Estándar de la Etiqueta [NIV]: Micro-Aplicaciones de Diagnóstico y Vida Real
- **Naturaleza de la Etiqueta [NIV]:**
  - La etiqueta `[NIV]` aloja Micro-Aplicaciones interactivas de utilidad práctica cotidiana organizadas por escalas o niveles (Jubilación y finanzas familiares, radar de fraudes y estafas para seniors, semáforo de salud/nutrición).
- **Adaptación a Personas Mayores (Seniors 65+):**
  - **Lenguaje cercano:** Prohibidos anglicismos y jerga fría de Silicon Valley (nada de FIRE, cashflow, ratios). Usar "Pensión mensual", "Gastos de la casa", "Ahorros de toda la vida", "Viviendas e inmuebles".
  - **Lógica Matemática Realista:** Considerar siempre que la pensión es vitalicia y que los ahorros no se tocan si la pensión cubre los gastos (cero contradicciones de tiempo). Incluir el patrimonio inmobiliario como escudo familiar.
  - **Diseño Accesible:** Tipografía grande (16px - 18px), alto contraste, botones amplios y mensajes tranquilizadores.

## Ejecución por Lotes de 10 Sesiones y Bitácora Maestra
- **Trabajo Autónomo y Desatendido por Lotes:**
  - El trabajo de actualización de las 60 sesiones se aborda en 6 lotes de 10 sesiones (Lote 1: 01-10, Lote 2: 11-20, etc.).
  - El asistente trabaja en silencio, sin interrupciones intermedias al usuario, registrando cada avance en `ESTADO_60_SESIONES.md`.
  - Al finalizar cada lote, entrega un único comando de terminal limpio y numerado para sincronizar GitHub y desplegar Classroom.






