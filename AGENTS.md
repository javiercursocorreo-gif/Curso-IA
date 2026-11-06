# PROTOCOLO DE ORO: CERO SUBMITS ABSOLUTO (COMPROMISO VITAL)
- Prohibición Total de Ventanas de Aprobación en el Chat: Queda terminantemente prohibido ejecutar acciones o herramientas que hagan saltar botones de "Submit", "Aprobar" o confirmaciones en el editor del usuario.
- Modo Terminal Externa 100% Desatendido: Toda creación de fichas didácticas, reescritura de scripts y edición de mapas se entrega integrada dentro del bloque de comandos de terminal correlativo ([COMANDO XX]) para ejecución desatendida y sin interrupciones.

# REGLA DE ORO: TRABAJO EN SILENCIO, CERO INTERRUPCIONES Y EJECUCIÓN DIRECTA
1. **Trabajar Siempre en Silencio:**
   - El asistente debe trabajar de forma 100% silenciosa: cero charlas, cero explicaciones innecesarias y cero comentarios de relleno.
   - Todas las tareas y modificaciones de código deben ejecutarse directamente de principio a fin sin detenerse.
2. **Eliminación Total de Confirmaciones y Botones de Submit:**
   - NUNCA solicitar confirmación manual ni requerir feedback interactivo para ejecutar planes o artefactos (`RequestFeedback: false`).
   - Prohibido detener la ejecución a la espera de botones de *Submit*, *Proceed* o autorizaciones intermedias.
3. **Ejecución en Sandbox y Entrega del Comando al Final:**
   - Ejecutar siempre prioritariamente dentro del Sandbox (`BypassSandbox: false`) mediante comandos atómicos, directos y limpios para auto-aprobación del sistema.
   - Toda lectura, edición y creación de archivos se realiza desatendida mediante herramientas de edición (`read_file`, `edit_file`, `write_file`).
   - Al finalizar la tarea, entregar directamente un único bloque de comando limpio y numerado para su ejecución desatendida en la terminal externa.
4. **Formato Estricto de Comandos (Título Visible DENTRO de la Terminal):**
   - El título y número de comando NO pueden estar solo fuera del bloque de código. Deben incluirse OBLIGATORIAMENTE DENTRO del comando ejecutable mediante `echo` inicial y final para que, al pegarlo en la terminal externa, el usuario vea con total claridad qué comando está ejecutando y cuándo termina:
     `### [INICIO COMANDO XX: TÍTULO]`
     ```bash
     echo "========================================================"
     echo "=== [INICIO COMANDO XX: TÍTULO] ==="
     echo "========================================================"
     ...
     echo "========================================================"
     echo "=== [FIN COMANDO XX: TÍTULO] (EXITOSO) ==="
     echo "========================================================"
     ```
     `### [FIN COMANDO XX: TÍTULO]`
5. **Cero Herramientas Nuevas ni Instalaciones Externas:**
   - Prohibido instalar paquetes o librerías adicionales (como pip, brew o npm ajenos).
   - Operar exclusivamente con las herramientas nativas preexistentes del sistema macOS (AppleScript / osascript para Microsoft Office, python estándar de la máquina, etc.).

# ESTÁNDARES DIDÁCTICOS Y DE DESARROLLO (CURSO-IA)

## Estándar de Sitios Web Embebidos y Simuladores (Fichas Didácticas Flotantes)
- **Fichas Embebidas a la Derecha:**
  - Al diseñar simuladores, laboratorios o aplicaciones interactivas que embeben visores web externos (como NASA Eyes 3D, visores moleculares, telescopios o mapas), las explicaciones didácticas y fichas de retos deben colocarse **embebidas a la derecha** en un panel flotante HUD (`position: fixed; top: 16px; right: 16px; width: 380px; z-index: 100; max-height: calc(100vh - 32px); overflow-y: auto; background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(12px); border-radius: 12px; padding: 18px; color: #fff; border: 1px solid rgba(255, 255, 255, 0.1);`).
  - Esto garantiza que el alumno pueda leer las instrucciones, misiones y preguntas de Gemini sin obstruir la escena 3D ni los controles de navegación.
- **Gestión Limpia de Parámetros de URL en Iframes (`loadTarget`):**
  - La función JavaScript de carga dinámica debe controlar si la URL ya contiene parámetros para concatenar limpiamente:
    `const sep = target.includes('?') ? '&' : '?'; iframe.src = target + sep + 'embed=true';`
  - Evitar duplicaciones de sintaxis o variables globales sueltas que provoquen `SyntaxError`.

## Estándar Oficial de Navegación y Calibración en NASA Eyes 3D
- **Catálogo Estricto de Identificadores (Prohibición de Abreviaturas Inventadas):**
  - El motor de NASA Eyes requiere estrictamente los nombres exactos registrados en su base de datos de telemetría. Queda prohibido inventar o acortar nombres:
    - Telescopio Roman: `sc_roman_space_telescope` (nunca `sc_roman`).
    - Mars Reconnaissance Orbiter: `sc_mars_reconnaissance_orbiter` (nunca `sc_mro`).
    - Sonda Parker: `sc_parker_solar_probe`.
    - MAVEN: `sc_maven`.
    - BepiColombo: `sc_bepicolombo`.
    - Nave Orión (Artemisa): `sc_artemis_1`.
    - Estación Espacial: `sc_iss`.
    - Telescopio James Webb: `sc_jwst`.
- **Prohibición Total de Rovers y Activos de Suelo en el Motor Orbital:**
  - El motor `apps/solar-system/` de NASA Eyes renderiza exclusivamente cuerpos celestes y naves en órbita o vuelo espacial; NO renderiza rovers en tierra ni mallas sobre la superficie marciana (Perseverance, Curiosity). Intentar cargarlos produce un lienzo vacío o inerte.
  - Toda sesión que involucre vehículos de superficie queda sustituida de inmediato por cuerpos y lunas reales orbitantes (ej. Fobos y Deimos).
- **Calibración Temporal Obligatoria de Sondas Históricas (`time=YYYY-MM-DDTHH:MM:SS`):**
  - Cuando una sonda histórica fue lanzada o desplegada desde órbita terrestre (ej. Magallanes desplegada por el transbordador espacial Atlantis en 1989), sin un parámetro temporal el visor la muestra en su inicio sobrevolando la Tierra (azul con nubes).
  - Para situarla en su planeta destino, es obligatorio inyectar la marca temporal UTC de su misión activa (ej. Magallanes en órbita de Venus: `sc_magellan?time=1991-01-01T12:00:00.000+00:00`).
- **Diferenciación de Motores: Solar System vs Eyes on Asteroids (Didymos, NEOs e Impactos):**
  - El motor `apps/solar-system/` solo indexa cuerpos celestes mayores y protoplanetas (Ceres, Vesta, Bennu, Psyche). Los asteroides cercanos a la Tierra (NEOs) menores como **Didymos (780 m) y Dimorphos (160 m)** no disponen de ruta directa en `solar-system` y residen en el motor dedicado **`apps/asteroids/#/asteroids/didymos`** y **`apps/asteroids/#/missions/sc_dart?time=2022-09-26T23:14:08.000+00:00`**. La función `loadTarget` debe enrutar limpiamente a cada motor correspondiente según el cuerpo seleccionado.
- **Diseño Minimalista de Barra Inferior de Navegación (Planeta + Sondas de la Misión + Sistema Solar):**
  - La barra inferior debe ser minimalista, limpia y contener EXCLUSIVAMENTE (3 a 4 botones máximo):
    1. El **propio planeta o cuerpo principal** de la sesión (activo al cargar).
    2. Las **sondas o naves orbitales DIRECTAMENTE vinculadas a esa misión**.
    3. El **Sistema Solar Global** (`home`).
- **Obligación de Autocomprobación Previa y Poda Temprana (Cero Trabajo de Depuración para el Usuario):**
  - El asistente tiene la obligación estricta de autocomprobar y verificar que cada identificador y enlace funciona realmente en el motor de NASA Eyes antes de entregar la tarea.
  - Si una sonda o activo no se mueve, no carga o no existe como malla 3D, **NO SE INVENTA, NO SE COMPLICA LA VIDA, SE ELIMINA Y SE SUSTITUYE DE INMEDIATO POR UN CUERPO O NAVE ORBITAL QUE SÍ FUNCIONE AL 100%**.
  - El usuario jamás debe realizar tareas de depuración ni probar enlaces rotos: todo lo entregado debe funcionar impecablemente al primer clic.

## Regla de Fidelidad Científica e Hiperrealismo (Prohibición de Babylon.js)
- **Prohibición Total de Babylon.js:** Jamás renderizar con Babylon.js en ningún simulador ni ficha didáctica. Todo visor 3D debe programarse exclusivamente en **Three.js** o mediante un **visor fotográfico interactivo de alta resolución (HTML5 Canvas / SVG)**.
- **Fuentes Científicas Reales e Hiperrealistas:** Prohibido el uso de geometrías toscas, esferas lisas o modelos abstractos ("huevos"). Todos los activos visuales deben ser fotografías científicas de alta resolución o escaneos reales procedentes de repositorios científicos acreditados (NIH, NASA, microtomografía CT, microscopía electrónica TEM, CyArk, etc.).
- **Prohibición Total de Imágenes Generadas por IA (GenAI):** Queda terminantemente prohibido generar o incrustar imágenes falsas o aproximaciones artísticas de IA cuando se trata de contenidos biológicos, anatómicos o astronómicos. Búsqueda obligatoria en repositorios abiertos de ciencia real (Wikimedia Commons, NASA JPL, USGS, NIH).

## Metodología Didáctica: La Triple Salvaguarda Pedagógica
1. **Taller Interactivo de Pruebas:** Para que el alumno experimente la generación de código con Gemini y vea su aplicación nacer en directo.
2. **Simulador 3D Oficial Garantizado:** Botón directo a la aplicación final hiperrealista depurada, asegurando que el 100% de los alumnos disfrute de la experiencia completa sin atascos ni dependencias de variabilidad de la IA.

## Estándar de la Etiqueta [NIV]: Micro-Aplicaciones de Diagnóstico y Vida Real
- Micro-herramientas funcionales de autodiagnóstico, cálculo biomédico o simulación de la vida real orientadas a la toma de decisiones prácticas mediante IA y lógica interactiva.

## Regla de Despliegue: Todo se Sube a GitHub Siempre (GitHub Pages & Classroom)
- Todo cambio en mapas, simuladores, fichas y paneles CSV debe subirse y sincronizarse con GitHub para que los alumnos tengan acceso inmediato a través de GitHub Pages y los enlaces correspondientes en Google Classroom.

# SEGUIMIENTO DE CLASES Y CALENDARIO (CURSO-ROBOTICA-IA-COMUN)
- **Alternancia Oficial de Clases:**
  - Clases de Robótica (ROB) los martes y Clases de Inteligencia Artificial (IA) los jueves (ajustándose al calendario lectivo y festivos oficiales).
- **Actualización de Bitácora y Excel Nativo:**
  - La bitácora `BITACORA_SEGUIMIENTO_CLASES.md` y el libro Excel oficial de seguimiento se actualizan desatendidamente mediante scripts de AppleScript nativo (`generar_bitacora_completa_nativa.py`), asegurando el formateo estricto por bimestres sin requerir dependencias externas.

# TAREAS PENDIENTES POR LOTES (RITMO: 1 LOTE POR DÍA)
- **Reducción a 14 Slides de T1. TEORÍA (CURSO-ROBOTICA-V2):**
  - Reducir todas las presentaciones PPTX y PDFs de teoría de robótica al formato ágil de 14 diapositivas adaptado a seniors, creando backup previo `T1.TEORIA_ORIGINAL_XXslides`.
  - **Estado de avance:**
    - ✅ **Bloque 1 (1.1 a 1.4):** Completado al 100% (reducido a 14/15 diapositivas con backups).
    - ✅ **Bloque 2 (2.1 a 2.5):** Completado al 100% (reducido a 15 diapositivas con backups).
    - ✅ **Bloque 3 (3.1 a 3.5):** Completado al 100% (reducido a 15 diapositivas con backups).
    - ✅ **Bloque 4 (4.1 a 4.5):** Completado al 100% (reducido a 15 diapositivas con backups).
    - ⏳ **Bloque 5 (5.1 y 5.2):** Siguiente lote pendiente de ejecución (5.3, 5.5 y 5.6 ya optimizadas).

# MÓDULO ESPECIALIZADO DE MÚSICA Y WEB MIDI (CURSO_MUSICA)
- **Repertorio Korg EK-50 & Atril Digital Web MIDI:**
  - Cero intervención manual del usuario en el teclado Korg EK-50: todos los cambios de instrumento, volumen, estilo y efectos se automatizan mediante Web MIDI (mensajes SysEx, Program Change y Bank Select CC00/CC32).
  - Canales MIDI canónicos: Upper 1 (Ch 1), Upper 2 (Ch 2), Lower (Ch 3).
  - Servidor local Wi-Fi persistente a 0 segundos: `cd CURSO_MUSICA && nohup python3 -m http.server 8888 > /tmp/korg_server_8888.log 2>&1 &`, con detección dinámica de IP local (`ipconfig getifaddr en0`) y alias mDNS `$(hostname -s).local` para acceso instantáneo desde iPad.
  - Validación visual exclusiva en iPad sin saturar la pantalla del Mac.

# PROTOCOLO DE CIERRE DE CHAT Y ENTREGA DE HERENCIA UNIVERSAL
- **Activación:** Cuando el usuario indique que quiere cerrar el chat (ej. *"quiero cerrar el chat"*, *"cierra el chat"*, *"dame la frase de cierre"*, *"vamos a pasar a otro chat"*, etc.):
  1. **Actualización Obligatoria del Documento Vivo:** El asistente debe actualizar inmediatamente [`ESTADO_GLOBAL_PROYECTOS.md`](file:///Users/externo/Library/Mobile%20Documents/com~apple~CloudDocs/PERSONAL/CLASES%20DE%20TECNOLOG%C3%8DA/ESTADO_GLOBAL_PROYECTOS.md) en la raíz con los últimos avances realizados en la sesión y los números actualizados de ambos contadores:
     - Contador General: `[COMANDO XX]`
     - Contador Música: `[COMANDO MÚSICA XX]`
  2. **Entrega de la Frase Única de Herencia:** Entregar al usuario la frase formateada en negrita y bloque de cita para copiarla directamente al nuevo chat:
     > **"Revisa `ESTADO_GLOBAL_PROYECTOS.md` y continuamos según lo que te vaya pidiendo (Contador General: COMANDO [XX] / Contador Música: COMANDO MÚSICA [YY])."**
