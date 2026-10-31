# PROTOCOLO DE ORO: CERO SUBMITS ABSOLUTO (COMPROMISO VITAL)
- Prohibición Total de Ventanas de Aprobación en el Chat: Queda terminantemente prohibido ejecutar acciones o herramientas que hagan saltar botones de "Submit", "Aprobar" o confirmaciones en el editor del usuario.
- Modo Terminal Externa 100% Desatendido: Toda creación de fichas didácticas, reescritura de scripts y edición de mapas se entrega integrada dentro del bloque de comandos de terminal correlativo ([COMANDO XX]) para ejecución desatendida y sin interrupciones.

# REGLA DE ORO: TRABAJO EN SILENCIO, CERO INTERRUPCIONES Y EJECUCIÓN DIRECTA
1. **Trabajar Siempre en Silencio:**
   - El asistente debe trabajar de forma 100% silenciosa: cero charlas, cero explicaciones innecesarias y cero comentarios de relleno.
   - Todas las tareas y modificaciones de código deben ejecutarse directamente de principio a fin sin detenerse.
2. **Eliminación Total de Confirmaciones y Botones de Submit:**
   - NUNCA solicitar confirmación manual ni requerir feedback interactivo para ejecutar planes o artefactos (RequestFeedback: false).
   - Prohibido detener la ejecución a la espera de botones de Submit, Proceed o autorizaciones intermedias.
3. **Ejecución en Sandbox y Entrega del Comando al Final:**
   - Ejecutar siempre prioritariamente dentro del Sandbox (BypassSandbox: false) mediante comandos atómicos, directos y limpios para auto-aprobación del sistema.
   - Al finalizar la tarea, entregar de forma concisa el comando exacto o enlace necesario para que el usuario pueda verificar o lanzar el resultado.

# REGLAS DEL PROYECTO (CURSO-IA)

## Protocolo de Asistente Personal Proactivo (Briefing Diario al Iniciar Sesión)
- **Briefing Matutino / Inicio de Chat:**
  - En el primer turno de cada día o al iniciar una conversación, el asistente debe actuar como un auténtico Asistente Personal proactivo.
  - Debe consultar la fecha actual y el estado de `PLAN_MAESTRO_SIMULADORES_Y_TALLERES_COD.md`, e informar de inmediato al usuario en un recuadro claro:
    1. Qué lote de 5 sesiones toca hacer hoy del Plan COD (o si ya está completado).
    2. Si es martes o jueves, recordar la bitácora de clases de las 14:00.
    3. Entregarle directamente el bloque de trabajo o herencia listo sin que el usuario tenga que recordar buscarlo.

## Flujo de Trabajo Automatizado y Cero Interrupciones (Auto-Execution)
- **PROHIBICIÓN ABSOLUTA DE SUBMITS Y VENTANAS DE APROBACIÓN EN EL CHAT:**
  - El asistente tiene **TERMINANTEMENTE PROHIBIDO** ejecutar comandos o acciones que provoquen la aparición de botones de "Submit", "Aprobar", confirmaciones o ventanas emergentes en la pantalla del usuario.
  - Queda **ESTRICTAMENTE PROHIBIDO** ejecutar herramientas de terminal intermedias (`run_command`) para inspección exploratoria de sistema, red o procesos (`ifconfig`, `lsof`, `ps`, `curl`, scripts de terminal de prueba, etc.) durante el turno de conversación.
  - Toda la lectura, análisis, creación y edición de código debe ejecutarse de forma 100% silenciosa y desatendida mediante herramientas de edición de archivos (`read_file`, `edit_file`, `write_file`).
  - Al final de la respuesta, el asistente debe entregar directamente y sin interrupciones previas **UN ÚNICO BLOQUE DE COMANDO DE TERMINAL LIMPIO Y NUMERADO** para que el usuario lo ejecute en su propia terminal externa.
- **Eliminación de Confirmaciones y Botones de Proceed:**
  - El asistente NUNCA debe solicitar confirmación manual ni requerir feedback interactivo para ejecutar planes o artefactos (`RequestFeedback: false`).
  - Todos los planes, modificaciones de código y tareas deben ejecutarse de forma directa, continua e ininterrumpida.

## Regla de Fidelidad Científica e Hiperrealismo (Prohibición de Babylon.js)
- **PROHIBICIÓN TOTAL DE BABYLON.JS:** Jamás renderizar con Babylon.js en ningún simulador ni ficha didáctica. Todo visor 3D debe programarse exclusivamente en **Three.js** o mediante un **visor fotográfico interactivo de alta resolución (HTML5 Canvas / SVG)**.
- **Fuentes Científicas Reales e Hiperrealistas:** Prohibido el uso de geometrías toscas, esferas lisas o modelos abstractos ("huevos"). Todos los activos visuales deben ser fotografías científicas de alta resolución o escaneos reales procedentes de repositorios científicos acreditados (NIH, NASA, microtomografía CT, microscopía electrónica TEM, CyArk, etc.).
- **Almacenamiento Centralizado y Portabilidad:** Todas las fotografías y escaneos deben guardarse en `SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/` en formato original (`.jpg`/`.png`/`.glb`) y disponer de su correspondiente contenedor autónomo Base64 (`_photo_b64.js`) para garantizar el funcionamiento 100% offline sin dependencias externas.

## Nueva Estructura Oficial de las Fichas Científicas [COD] (Sin Talleres ni Copia de Código)
- **Fichas Orientadas a la Exploración Científica Directa:**
  - Tras la supresión de los antiguos 'Talleres de Pruebas' para dejar exclusivamente los **Simuladores 3D Científicos Interactivos**, las fichas didácticas oficiales del bloque `[COD]` eliminan las listas de tareas de copiado de código y los prompts técnicos de programación.
  - La estructura oficial estándar de 1 página se compone de:
    1. **Explicación didáctica y científica del simulador:** qué fenómeno reproduce en tiempo real, órganos/estructuras visibles y controles de interacción 360°, corte y parámetros.
    2. **Procedencia oficial y fuentes científicas:** acreditación rigurosa de las instituciones científicas (NIH, NASA, Z-Anatomy, CyArk, etc.), técnicas de captura médica/orbital (MRI 7T, tomografía, fotogrametría LiDAR) y calidad de datos.
    3. **Guía de exploración en el aula & preguntas para conversar con Gemini:** preguntas de reflexión y aprendizaje para que los alumnos dialoguen con Gemini mientras observan el modelo en pantalla.

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

## Estándar de Simuladores Científicos: Visores Fotográficos Interactivos de Alta Resolución (Three.js / HTML5 Canvas)
- **Prohibición Total de Dibujos Animados y Mallas Procedurales Inventadas:**
  - Queda terminantemente prohibido generar dibujos animados, trazados vectoriales Bézier ficticios en canvas 2D, o mallas primitivas deformadas por código.
  - Toda simulación debe ser un **Visor Fotográfico Interactivo de Alta Resolución** o una escena Three.js basada en escaneos y fotografías científicas reales (microscopía confocal, resonancias magnéticas, tomografías axiales, fotografías orbitales de NASA/ESA, fotogrametrías de museos).
- **Prohibición Total de Babylon.js:**
  - Babylon.js queda estrictamente prohibido en todo el proyecto. Se utiliza exclusivamente Three.js o el motor nativo de visualización fotográfica interactiva en HTML5 Canvas con zoom, rotación, filtros y puntos de interés anatómicos.
- **Arquitectura de Carga y Autonomía (Base64 Offline):**
  - Todas las fotografías y escaneos de alta resolución deben estar respaldados en archivos `_photo_b64.js` en `SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/` para garantizar funcionamiento 100% offline, sin dependencias externas ni bloqueos de CORS.

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

## Regla de Oro: Actualización Obligatoria e Inmediata de Documentación ante Todo Aprendizaje Nuevo
- **Sincronización del Conocimiento en Tiempo Real:**
  - Cada vez que se descubra, depure, aprenda o ajuste una nueva técnica, comportamiento de hardware, solución de bug o parámetro técnico en cualquier módulo del proyecto, el asistente DEBE actualizar simultánea e inmediatamente en ese mismo turno toda la documentación técnica correspondiente (`.md` y `.html`), bitácoras y archivos de reglas (`AGENTS.md` y `GEMINI.md`).
  - Queda terminantemente prohibido dejar descubrimientos o lecciones aprendidas aisladas en el chat sin que queden permanentemente selladas y versionadas en la documentación oficial.

## Blindaje de Texturas y Modelos 3D en Prompts [COD] (Prohibición de Invención en Canvas y URLs Directas Obligatorias)
- **Diagnóstico del "Tablero de Ajedrez" y Ceguera de Gemini:**
  - Gemini no tiene conexión a internet en tiempo de generación ni acceso al sistema de archivos local, ni dispone de ojos para ver el canvas renderizado.
  - Si un prompt solicita "aplica una textura satelital de la NASA" sin proporcionar una URL web directa, Gemini intentará "dibujar la superficie matemáticamente" mediante un `<canvas>` procedural, generando bucles de cuadrículas (`(fila + columna) % 2 === 0`) que producen un tablero de ajedrez irreal y frustrante.
- **Suministro Obligatorio de URLs Públicas Libres de CORS:**
  - En todo Prompt Maestro para Gemini que requiera texturas o modelos 3D, DEBE incluirse taxativamente la URL web pública oficial y libre de CORS (ej. `https://assets.babylonjs.com/textures/moon.jpg` en el CDN oficial de Babylon.js, NIH, NASA, etc.).
  - El prompt debe ordenar explícitamente: *"Prohibido generar texturas en canvas o cuadrículas procedurales: aplica directamente la textura/modelo oficial desde [URL]"*.
- **El Doble Botón como Salvavidas Pedagógico:**
  - Toda sesión del bloque [COD] en mapas y Classroom mantiene la doble vía de acceso:
    1. **Taller Interactivo de Pruebas:** Para que el alumno experimente la generación de código con Gemini y vea su aplicación nacer en directo.
    2. **Simulador 3D Oficial Garantizado:** Botón directo a la aplicación final hiperrealista depurada, asegurando que el 100% de los alumnos disfrute de la experiencia completa sin atascos ni dependencias de variabilidad de la IA.

## Módulo Especializado de Música y Web MIDI (CURSO_MUSICA)
- Para cualquier trabajo en el módulo `CURSO_MUSICA/` (Atril Digital, Korg EK-50, Web MIDI, partituras y canciones), rigen de forma prioritaria las reglas de oro y arquitectura establecidas en `CURSO_MUSICA/AGENTS.md` y `CURSO_MUSICA/GEMINI.md`:
  - Cero intervención manual del usuario en el teclado Korg EK-50 (todo automatizado por Web MIDI).
  - Unificación Canónica Absoluta: Solo existe una única carpeta física en el sistema (`CURSO-IA/CURSO_MUSICA`), sin enlaces simbólicos ni réplicas externas.
  - Prohibición Total de Archivos de Herencia en Disco: Nunca crear `HERENCIA.md` en disco; la herencia se redacta en el texto del chat para copiar y pegar.
  - Validación exclusiva en iPad (prohibido abrir navegadores o pestañas en el Mac).
  - Protocolo anti-bloqueo USB (prohibición de `0xF8` en reposo; encendido secuencial de Korg primero 5s).
  - Mapeo General MIDI estricto (Harmonica = PC 22; Acordeón = PC 21; inyección de Vibrato CC1/CC77 y Reverb CC91=115).
  - Activación física de capas en panel frontal mediante Keyboard Set 61 (The Strings).
  - Índice ultra-compacto en 2 columnas sin autores (v111) para abarcar el catálogo completo de 24 obras a pantalla completa en el iPad sin scroll.
  - Creación de fichas autónomas para cada canción con botones 1-Tap para instrumentos y estilos del Korg EK-50, enlazando directamente a las partituras oficiales de MuseScore.
  - Tetralogía de estilos contemporáneos 031 a 034 (Windy Beat, Home Beat, Groove Bld, Diva) catalogada para baladas pop, cine y versiones modernas.







