# PROTOCOLO DE ORO: CERO SUBMITS ABSOLUTO (COMPROMISO VITAL)
- Prohibición Total de Ventanas de Aprobación en el Chat: Queda terminantemente prohibido ejecutar acciones o herramientas que hagan saltar botones de "Submit", "Aprobar" o confirmaciones en el editor del usuario.
- Modo Terminal Externa 100% Desatendido: Toda creación de fichas didácticas, reescritura de scripts y edición de mapas se entrega integrada dentro del bloque de comandos de terminal correlativo ([COMANDO XX]) para ejecución desatendida y sin interrupciones.

# PROTOCOLO DE ARRANQUE MATUTINO: RECORDATORIO OBLIGATORIO DE TAREAS PENDIENTES
- **Aviso Matutino Obligatorio en el Primer Mensaje del Día:**
  - Al recibir el **primer mensaje de cada jornada** (tanto si se abre un chat nuevo como si el usuario continúa en un hilo de días anteriores), el asistente debe anteponer obligatoriamente en su respuesta el **Cuadro de Mando Diario de Tareas Pendientes**:
    1. 📌 **Lote Programado del Día:** La sesión y tareas exactas que corresponden realizar hoy (ej. ampliación Google Flow en 5 fichas de imagen, visualización directa en `[COD]` y `[NIV]`).
    2. 📊 **Estado de Avance:** Resumen de sesiones completadas al 100% y siguientes en el calendario.
    3. ⏳ **Contabilidad de Infografías NLM en Cola:** Estado exacto de las infografías asignadas y pendientes para que el usuario decida si ese día aporta una nueva infografía de impacto o se procede con el lote técnico sin infografía.
  - *Excepción Autorizada a la Regla de Silencio:* Este cuadro de mando matutino es un requerimiento operativo indispensable de seguimiento; NO constituye charla ni relleno y debe emitirse siempre sin excepción al comenzar la jornada.

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

## Protocolo de Doble Verificación Elephant-Goldfish (Subagente Efímero sin Sesgo de Contexto)
- **Definición y Objetivo:** Para evitar la «ceguera de contexto» o fatiga cognitiva en sesiones largas (donde el modelo acumula miles de tokens y pasa por alto sus propios fallos de maquetación, sintaxis o enlaces), se adopta la arquitectura oficial *Elephant-Goldfish* de Google.
- **El Elefante (Coordinador con Memoria):** Es el agente principal del chat. Conoce la historia completa, el calendario, las reglas de oro y las necesidades del usuario. Diseña, planifica y genera el código, ficha o script.
- **El Pez de Colores / Goldfish (Auditor con Mente Limpia):** Es un subagente independiente (`invoke_subagent`) que nace con **cero memoria previa** (mente virgen). Recibe ÚNICAMENTE el archivo recién compilado y una lista de control estricta (ej. número de páginas exacto, solapamientos, sintaxis de código, identificadores canónicos de NASA Eyes).
- **Ciclo de Vida Efímero (Cero Residuos ni Fósiles):** Una vez emitido su veredicto en pocos segundos, el subagente se destruye de inmediato mediante la acción `kill` (`manage_subagents`), eliminando sus procesos, liberando memoria y asegurando que no quede ningún archivo residual ni proceso zombi en el sistema.

## Metodología Didáctica: La Triple Salvaguarda Pedagógica y Visualización Directa (Cero Código Intermedio)
- **Cero Código Intermedio para Alumnos Sénior (+65):** Queda terminantemente prohibido obligar al alumno sénior a manipular, leer, copiar o ejecutar bloques de código fuente (HTML, JavaScript, Three.js). Los bloques de código generan ansiedad tecnológica y fricción innecesaria.
- **Visualización Directa en Pantalla (Canvas / Vista Previa):** El prompt que el alumno copia en Gemini solicita directamente: *«Diseña y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un simulador visual sobre... Muestra directamente el simulador en funcionamiento sin obligarme a revisar el código fuente.»*
- **Estructura Didáctica Oficial en 2 Pasos:**
  1. **Paso 1 (Creación Directa):** Pegar el prompt en Gemini ➔ La aplicación interactiva nace directamente en pantalla lista para interactuar.
  2. **Paso 2 (Diálogo y Reflexión):** El alumno explora los controles y plantea a Gemini las 3 preguntas clave de reflexión formuladas en la ficha.
- **Copia de Respaldo Garantizada (BKP Oficial en el Mapa):** En el mapa interactivo se eliminan los botones y archivos residuales de talleres intermedios (`PROBADOR_CODIGO_IA.html`) y se conserva exclusivamente el botón de respaldo oficial BKP (`Ver Simulador 3D (BKP) ↗` o `Abrir Micro-App (HTML) ↗`), asegurando que el 100% de los alumnos disfrute de la experiencia completa sin atascos de red o servidor.
- **Orden de Botones en Tarjetas Especiales:** En las tarjetas `[NIV]`: 1º Ficha Guía & Prompt de Gemini (PDF), 2º Abrir Micro-Aplicación Oficial BKP (HTML). En las tarjetas `[FRAC]`: 1º Vídeo MP4, 2º Ficha Didáctica PDF.

## Estándar de la Etiqueta [NIV]: Micro-Aplicaciones de Diagnóstico y Vida Real
- Micro-herramientas funcionales de autodiagnóstico, cálculo biomédico o simulación de la vida real orientadas a la toma de decisiones prácticas mediante IA y lógica interactiva.

## Regla de Despliegue: Subida Automática e Inmediata a GitHub (GitHub Pages & Classroom)
- **Subida Automática Obligatoria en Cada Corrección:** Cada vez que se cree, modifique o corrija cualquier recurso de los cursos (fichas PDF, HTML, simuladores, mapas interactivos, temarios o paneles CSV), el asistente debe dejar los archivos compilados, commiteados y proporcionar OBLIGATORIAMENTE el bloque correlativo con `git push origin main` al final del turno para que los cambios se reflejen de inmediato en GitHub Pages y Google Classroom sin que el usuario tenga que recordarlo.
- **Aseguramiento Estricto de Commits y Verificación de Subida (Cero Fallos de Despliegue):**
  - **Problema Histórico:** En varias ocasiones se han generado recursos corregidos o nuevos que no quedaron subidos efectivamente al repositorio remoto de GitHub, provocando que los alumnos y el usuario sigan visualizando archivos antiguos o descalibrados.
  - **Protocolo de Verificación Obligatorio:**
    1. **Pre-Commit Total en el Asistente:** Antes de cerrar la respuesta, el asistente debe añadir y commitear todos los archivos modificados (`git add -A && git commit -m "..."`).
    2. **Pipeline de Subida Blindado en el Bloque de Terminal:** Cada bloque ejecutable debe incluir la sincronización completa y la comprobación final de estado:
       ```bash
       git add -A
       git commit -m "..." || true
       git push origin main
       echo "=== VERIFICACIÓN DE SUBIDA A GITHUB ==="
       git status -s
       git log -1 --oneline
       ```
    3. **Cero Commits Huérfanos:** Prohibido dejar la rama local por delante de `origin/main` (`ahead of origin/main`). Todo cambio debe quedar reflejado de inmediato en el remoto.
- Jamás dejar una corrección de clase pendiente de sincronización con GitHub.

# SEGUIMIENTO DE CLASES Y CALENDARIO (CURSO-ROBOTICA-IA-COMUN)
- **Alternancia Oficial de Clases:**
  - Clases de Robótica (ROB) los martes y Clases de Inteligencia Artificial (IA) los jueves (ajustándose al calendario lectivo y festivos oficiales).
- **Actualización de Bitácora y Excel Nativo:**
  - La bitácora `BITACORA_SEGUIMIENTO_CLASES.md` y el libro Excel oficial de seguimiento se actualizan desatendidamente mediante scripts de AppleScript nativo (`generar_bitacora_completa_nativa.py`), asegurando el formateo estricto por bimestres sin requerir dependencias externas.

# TAREAS PENDIENTES POR LOTES (RITMO: 1 LOTE POR DÍA)
- **Reducción a 14 Slides de T1. TEORÍA (CURSO-ROBOTICA-V2):**
  - Reducir todas las presentaciones PPTX y PDFs de teoría de robótica al formato ágil de 14 diapositivas adaptado a seniors, creando backup previo `T1.TEORIA_ORIGINAL_XXslides`.
  - **Estado de avance:**
    - ✅ **Bloques 1 a 5 (1.1 a 5.6):** Completados al 100% (reducidos y sincronizados a 15 diapositivas con backups, PPTX y PDFs).
    - ✅ **Bloque 6 (6.1 y 6.2):** Completados al 100% (15 diapositivas con PPTX y PDFs).
    - ⏳ **Bloque 6 (6.3 a 6.7):** Pendiente crear PPTX y PDFs desde cero directamente en el estándar de 15 diapositivas (Star Trek, Interstellar, SpaceX, Transbordador e ISS).
- **Carruseles de Partituras por Estilos y Sonidos Afines (CURSO_MUSICA):**
  - ✅ **Carrusel 1 Baladas Lentas 6/8:** Completado en `CARRUSEL_01_BALADAS_6_8.html` (#25 Can't Help Falling in Love + #26 Unchained Melody).
  - ⏳ **Regla de Migración y Nuevos Carruseles:** Conforme se crean nuevos carruseles (Boleros Latinos, Clásicos Italianos, Baladas 4/4, Cine), las canciones incorporadas **desaparecen de la lista general suelta** y quedan integradas en el bloque de su carrusel. En el repertorio (2 columnas optimizadas para iPad vertical), el **título del bloque es el enlace directo al carrusel**, manteniendo acceso individual debajo a cada partitura.
- **Actualización Diaria de Sesión Integral: Pareja Fractal + Visualización Directa + Ampliación Google Flow + Infografías [INFO] (Sesiones 01 a 15 de CURSO-IA):**
  - Cada mañana al recibir el primer mensaje del día (tanto si el usuario continúa en el mismo chat del día anterior como si abre uno nuevo), el asistente debe incluir el recordatorio del lote pendiente del día:
    1. **Pareja Fractal del Día:** 1º Fractal de la Naturaleza + 2º Fractal Matemático Puro (unificados en tarjetas PACK: 1º Vídeo MP4, 2º Ficha PDF).
    2. **Actualización al Estándar de Visualización Directa (Cero Código):**
       - **Ítem `[COD]`:** Prompt en Gemini pidiendo directamente ejecutar en pantalla (Canvas / Vista previa sin código intermedio), ficha PDF a 2 pasos didácticos con `NativePDFWriter`, purga de probador intermedio (`PROBADOR_CODIGO_IA.html`) y conservación exclusiva del botón BKP oficial (`Ver Simulador 3D (BKP) ↗`).
       - **Ítem `[NIV]`:** Ficha PDF con prompt de visualización directa, micro-app con ergonomía senior (letra grande 18.5px, voz `es-ES`, reset, sin solapamientos) y orden de botones (1º Ficha/Prompt PDF, 2º Abrir App BKP).
    3. **Ampliación Oficial a Vídeo con Google Flow (50 Créditos Diarios):**
       - En las **5 fichas de imagen de la sesión** (`[EST]`, `[PRAC]`, `[INT]`, `[FUT]`, `[ARTE]`), incluir el bloque inferior de ampliación a vídeo:
         * 📌 Pasos recordatorio rápidos (descargar imagen de Gemini, subir a `https://labs.google/flow`, pegar prompt y generar).
         * 💬 Prompt de movimiento cinemático calibrado para esa imagen exacta (consumo de 10 créditos por clip).
    4. **Integración de Infografías NLM [INFO]:** Preguntar activamente al usuario si tiene nuevas infografías o resúmenes visuales de NotebookLM para catalogarlas en el Bloque 15 (`15. [INFO] BLOQUE_15_INFOGRAFIAS_Y_NOVEDADES_IA`) e inyectarlas correlativamente en las sesiones correspondientes (`INFO-001`, `INFO-002`...).
  - **Estado de avance (1 sesión por día):**
    - ✅ **Sesión 01:** Pulmones 3D `[COD-001]` + Tranquilidad Jubilación `[NIV-001]` (Visualización directa, purga de probador y BKP).
    - ✅ **Sesión 02:** Corazón 3D `[COD-002]` + Radar Anti-Estafas `[NIV-002]` (Visualización directa, purga de probador y BKP).
    - ✅ **Sesión 03:** Novedades Gemini/Gmail `[INFO-003]` + Google Flow Cámara `[INFO-003B]` + Cómic con IA `[CUENT-003]` (Cervantes y Shakespeare - 4 fichas) + Pompeya 3D `[COD-003]` + Vivienda `[NIV-003]`.
    - ✅ **Sesión 04:** Cómics con NLM `[CUENT-004]` + Infografía NLM `[INFO-004]` (*«La IA es la Máquina Más Grande de la Historia»* - 7 pisos y 4 frenos físicos) + PDF Widescreen 16:9 + Visor HD.
    - ✅ **Sesión 05:** Google Flow oficial `[INFO-005]` (50 créditos diarios) + Ampliación a vídeo en sus 5 fichas de imagen (`EST-005`, `PRAC-005`, `INT-005`, `FUT-005`, `ARTE-005`) + Visualización Directa en `[COD-005]` Sistema Solar 3D y `[NIV-005]` Evolución del Dinero (+65).
    - ✅ **Sesión 06:** Ampliación Google Flow en 5 fichas de imagen (`EST-006`, `PRAC-006`, `INT-006`, `FUT-006`, `ARTE-006`) + Visualización Directa en `[COD-006]` Simulador Cerebro 3D y `[NIV-006]` Calculadora de Poder Adquisitivo y Cesta (+65) + Infografía NLM Widescreen 16:9 y Visor HD `[INFO-006]` *«El Plan Maestro de Integración Vertical en IA»*.
    - ⏳ **Próxima sesión (Lote de mañana): Sesión 07:**
      * Incorporar la **Ampliación Google Flow** en sus 5 fichas de imagen (`EST-007`, `PRAC-007`, `INT-007`, `FUT-007`, `ARTE-007`).
      * Visualización Directa en `[COD-007]` y `[NIV-007]`.
    - ⏳ **Sesiones 08 a 15 (Actualización Integral Completa en Bloque):** Visualización Directa (`[COD]` + `[NIV]` + BKP) + Ampliación Google Flow (5 fichas) + Infografía `[INFO]`.
    - ✅ **Sesiones 03 a 15 (Catálogo Oficial de Fractales [FRAC] Unificado):** Completado al 100% en todas las sesiones.

  - **Contabilidad Oficial y Cola de Infografías NLM [INFO] (Backlog Dinámico):**
    * Solo se generan e inyectan infografías cuando el usuario encuentra y entrega noticias de IA de alto impacto que llamen la atención. Las infografías pendientes quedan en cola ordenada para ser inyectadas conforme se aporten:
      - `[INFO-001]` (Sesión 01): ⏳ Pendiente infografía NLM de impacto
      - `[INFO-002]` (Sesión 02): ⏳ Pendiente infografía NLM de impacto
      - `[INFO-003]` (Sesión 03): ✅ Ficha temática Novedades Gemini, Gmail y Buscador IA + Taller Google Flow [INFO-003B] + Cómic [CUENT-003]
      - `[INFO-004]` (Sesión 04): ✅ Infografía NLM *«La IA es la Máquina Más Grande de la Historia»* (7 pisos y 4 frenos físicos) + PDF Widescreen 16:9 + Visor HD
      - `[INFO-005]` (Sesión 05): ✅ Ficha Didáctica Taller Oficial Google Flow (50 créditos diarios)
      - `[INFO-006]` (Sesión 06): ✅ Infografía NLM *«El Plan Maestro de Integración Vertical en IA»* + PDF Widescreen 16:9 + Visor HD
      - `[INFO-007]` (Sesión 07): ⏳ Reserva disponible: *«La Ruptura de Internet: Agentes de IA vs Modelo Publicitario»* (lista para asignar o sustituir por nueva noticia de impacto)
      - `[INFO-008]` a `[INFO-015]`: ⏳ Cola de infografías pendientes de nuevas noticias que llamen la atención (se inyectarán correlativamente conforme el usuario las entregue).

# MÓDULO ESPECIALIZADO DE MÚSICA Y WEB MIDI (CURSO_MUSICA)
- **Repertorio Korg EK-50 & Atril Digital Web MIDI:**
  - Cero intervención manual del usuario en el teclado Korg EK-50: todos los cambios de instrumento, volumen, estilo y efectos se automatizan mediante Web MIDI (mensajes SysEx, Program Change y Bank Select CC00/CC32).
  - Canales MIDI canónicos: Upper 1 (Ch 1), Upper 2 (Ch 2), Lower (Ch 3).
  - Servidor local Wi-Fi persistente a 0 segundos: `cd CURSO_MUSICA && nohup python3 -m http.server 8888 > /tmp/korg_server_8888.log 2>&1 &`, con detección dinámica de IP local (`ipconfig getifaddr en0`) y alias mDNS `$(hostname -s).local` para acceso instantáneo desde iPad.
  - Validación visual exclusiva en iPad sin saturar la pantalla del Mac.
  - **Sincronización Dual Automática (Wi-Fi Local & GitHub Pages Nube):**
    * En cada creación o corrección de partituras, carruseles, sonidos o repertorio en `CURSO_MUSICA`, mantener obligatoriamente `index.html` 100% idéntico y sincronizado con `REPERTORIO_KORG_EK50.html`.
    * Compilar, commitear y proveer de forma automática el bloque correlativo con `git push origin main` al final del turno para que la nube pública de GitHub Pages esté permanentemente actualizada tanto si el usuario toca en casa (Wi-Fi local `:8888`) como en la calle (GitHub Pages en iPad).
- **Estándar Canónico Oficial de Keyboard Sets del Korg EK-50 (1-170):**
  - **Identidad de Pantalla LCD y Sonido 100% Real:** Los 170 timbres de la placa frontal son **Keyboard Sets compuestos multicapa**, gobernados obligatoriamente por el **Banco Maestro MSB = 33**.
  - **Transmisión de Control Dual:** El selector `[0xB0 | ch, 0x00, 33]`, `[0xB0 | ch, 0x20, LSB]`, `[0xC0 | ch, PC]` debe enviarse en **Canal 1 (Upper 1) y Canal 16 (Global)** para que el Korg EK-50 cambie en tiempo real el nombre y número en su propia pantalla LCD.
  - **Configuración Espejo de las 4 Capas de Fábrica (Voice Name List):**
    * `029 Harmonica`: Banco 33, LSB 2, PC 8. Upper 1: `Sweet Harm.` (`121, 1, 22`, Vol 127, Reverb 42) + Upper 2: `Sweet Harm.` (`121, 1, 22`, Vol 110, ¡doble capa activa obligatoria para cuerpo acústico!) + Lower: `i3 Strings` (`121, 5, 48`, Vol 95). **Octava 0 natural obligatoria** (prohibido transponer +12 st a las armónicas).
    * `066 Oct.Strings`: Banco 33, LSB 6, PC 5. Upper 1: `St. Strings` (`121, 3, 48`, Vol 125) + Upper 2: `St. Strings` (`121, 3, 48`, Vol 110) + Upper 3: `StringQuart` (`121, 9, 48`, Vol 95) + Lower: `Oh-AhVoices` (`121, 9, 52`, Vol 85).
    * `071 Oooh&Aahs`: Banco 33, LSB 7, PC 0. Upper 1: `Oooh Choir` (`121, 6, 52`, Vol 122) + Upper 2: `Choir Aahs` (`121, 0, 52`, Vol 95) + Lower: `Dark Pad` (`121, 6, 89`, Vol 75).
    * `101 Tenor Sax`: Banco 33, LSB 10, PC 0. Upper 1: `Tenor Noise` (`121, 1, 66`, Vol 127) + Lower: `Dark Pad` (`121, 6, 89`, Vol 85).
  - **Numeración Estricta de 3 Dígitos por Delante:** Todo botón, HUD y etiqueta debe incluir obligatoriamente el número oficial por delante (`029 Harmonica`, `066 Oct.Strings`, `071 Oooh&Aahs`, `101 Tenor Sax`).
  - **Fidelidad Textual Absoluta al Requerimiento del Usuario:** Prohibido renombrar, alterar o sustituir los nombres y sonidos solicitados por el usuario.
  - **Parámetros Acústicos Realistas:** Reverb CC91 entre 38 y 44, expresión al 127 y cero recortes artificiales de modulación o chorus de fábrica.
  - **Arquitectura de Interfaz Canónica (Cero Botones de Sonido/Estilo en Pantalla Principal):**
    - En la pantalla principal de la ficha didáctica NO se colocan botones de sonidos ni de estilos.
    - El control de estilos, timbres, tempo y ritmos reside EXCLUSIVAMENTE en el panel flotante HUD de la partitura a pantalla completa (`#modal-score-scroll-container`), manteniendo la ficha principal limpia, despejada y enfocada en la guía armónica y el botón de apertura a pantalla completa.
  - **Evolución de la Regla de STS de Teclados de Alta Gama (Curaduría y Desduplicación a 8 Sonidos Únicos):**
    - **Punto de partida de referencia:** Los 4 STS de fábrica de los teclados de alta gama (gama Korg Pa / EK-50) se toman como referencia musical inicial de cada estilo.
    - **Modificación y personalización obligatoria:** A continuación, se comparan ambas líneas y **se modifican los STS que sean comunes o redundantes**, sustituyéndolos por timbres alternativos de alta calidad de la lista oficial del EK-50 (guitarras, órganos, metales, voces, cuerdas).
    - **Resultado final:** En las fichas HUD de 2 líneas de estilos, los 4 instrumentos asignados a cada línea deben ser **100% diferentes entre sí** (4 en Línea 1 + 4 en Línea 2 = **8 sonidos únicos y complementarios**). Queda prohibido repetir un mismo Keyboard Set en ambas líneas, garantizando que el intérprete disponga de 8 timbres distintos y complementarios, pudiendo combinarlos libremente con cualquiera de los 2 estilos sin botones redundantes ni desperdicio de espacio.
- **Protocolo Anti-Bloqueo "442" y Botón Canónico `⚡ Reset Korg` (`desbloquearKorgEK50()`):**
  - **Causa Raíz de Enmudecimiento / Error 442:** El Korg EK-50 enmudece o se descalibra si recibe mensajes de Banco GM 121 en capas secundarias (`MSB 121, LSB 5, PC 89` = Sound #442 Money Pad). Queda TERMINANTEMENTE PROHIBIDO enviar comandos en Banco 121 a nivel individual.
  - **Gobierno Exclusivo de Keyboard Sets por Banco Maestro MSB = 33:** Los 170 timbres oficiales deben seleccionarse estrictamente mediante el Banco Maestro MSB = 33 en Canal 1 (Upper 1) y Canal 16 (Global): `[0xB0 | ch, 0x00, 33], [0xB0 | ch, 0x20, LSB], [0xC0 | ch, PC]`.
  - **Inclusión Obligatoria del Botón `⚡ Reset Korg`:** En toda cabecera flotante HUD o atril digital debe incluirse el botón de emergencia `⚡ Reset Korg` (`desbloquearKorgEK50()`). Este botón emite una ráfaga inmediata de pánico en los 16 canales MIDI (CC120 All Sound Off, CC123 All Notes Off, CC121 Reset All Controllers, CC7 Vol 127, CC11 Expr 127) y retransmite el Keyboard Set activo en Banco 33, restaurando el sonido al instante sin necesidad de apagar ni reiniciar físicamente el teclado.
- **Estándar Canónico de Fichas "Sin Partitura" (Tocar de Oído / Acordes OLED):**
  - Para canciones u obras que no disponen de partitura tradicional o están destinadas a la interpretación de oído con guía armónica (ej. `CANCION_16_MY_HEART_WILL_GO_ON.html`, `CANCION_27_VIVO.html`, `CANCION_30_BOLERO_RAVEL.html`, `CANCION_31_ME_OLVIDE_DE_VIVIR.html`), la vista a pantalla completa adopta un cuadro de mando armónico sobre fondo negro puro OLED (`#000000`).
  - Cada sección musical se organiza en compases visuales (`measure-box`) con acordes en tipografía grande y clara (`chord-name`), grado armónico (`chord-degree`), guías melódicas o de letra (`melody-notes` / `lyrics-hint`), y la cabecera fija HUD idéntica de 2 líneas con estilos y timbres, botones discretos `[ R ]` y `[ X ]`, Triple Escudo Anti-Apagado para iPad y Smart Dimming (60s).
- **Estándar de Paleta Sinfónica de Vientos y Violines (BSO Maestosas):**
  - En grandes obras orquestales y cinematográficas (John Williams, John Barry, Maurice Ravel), la cabecera HUD debe desglosar y proveer una paleta tímbrica rica que cubra tanto los **Vientos** (`095 Horns&Ens.`, `118 Wind Sect.`, `113 ThreeFlutes`, `092 Orch Brass`, `107 EnglishHorn`) como los **Violines y Cuerdas** (`061 The Strings`, `066 Oct.Strings`, `062 Bow Strings`, `068 Str.&Winds`), permitiendo al intérprete alternar entre la majestuosidad de los metales/maderas y la calidez de las cuerdas sinfónicas.
- **Estándar Canónico de Transiciones Armónicas e Inversiones (Estándar Cuaderno):**
  - **Prohibición Total de Tablas Teóricas Complejas:** Prohibido incluir tablas densas con columnas teóricas o explicaciones académicas ("1ª inversión", "2ª inversión", "Posición Origen", "Posición Destino", "Principio de Conducción Suave").
  - **Diseño Visual Directo (Notas en Teclas):** Cada transición se presenta en una sola fila compacta y de lectura instantánea desde el atril en iPad:
    * Etiqueta del par de acordes: `[ C ] ➔ [ Em ]`
    * Diagrama de teclas con letras anglosajonas espaciadas: `[ G · C · E ] ➔ [ G · B · E ]`
    * Resaltado cromático funcional:
      - **Notas fijas / pivote (que no se mueven):** Destacadas en **verde esmeralda** (`#34d399`) con brillo suave.
      - **Nota(s) en movimiento:** En gris claro (`#cbd5e1`).
      - **Nota(s) destino (donde cae el dedo):** Destacadas en **ámbar** (`#f59e0b`).
    * Píldora explicativa mínima al final: `G y E fijos · Solo baja C a B (1 semitono)`.
  - **Cero Distracción:** Diseñado para lectura rápida a 50 cm de distancia mientras se toca el teclado, sin desviar la atención de la partitura.
- **Estándar Cifra Club (`cifraclub.com`) para Letras y Acordes (Atril Digital / 2ª Página):**
  - **Fuente de Referencia Armónica Canónica:** Para las canciones del repertorio de entrenamiento activo, la fuente oficial para la colocación de acordes y letra es **Cifra Club (`cifraclub.com`)**.
  - **Sustitución de Partituras Complejas por Letras con Acordes:** En la segunda página / modal a pantalla completa (`modal-score-scroll-container` o `modal-atril-fullscreen`), en lugar de partituras gráficas tradicionales densas, se presenta la letra completa con los acordes superpuestos exactamente encima de cada palabra y compás tal como vienen en Cifra Club.
  - **Ergonomía OLED para iPad:** Fondo negro puro OLED (`#000000`), acordes en color contrastado y tipografía grande (18px-24px), letra blanca nítida, cabecera fija HUD Korg EK-50 con los 2 estilos y timbres, botón `⚡ Reset Korg` y control de batería seguro.
- **Estándar Oficial de Navegación del Repertorio por Botones de Estilo (2 Capas para iPad):**
  - **Primera Página Limpia (Solo Botones de Estilo):** La vista inicial de `REPERTORIO_KORG_EK50.html` e `index.html` se mantiene 100% limpia y sin listas sueltas de canciones desplegadas. Muestra exclusivamente la cuadrícula táctil con los botones interactivos por estilo/categoría:
    1. `🇮🇹 Grandes Clásicos Italianos`
    2. `🏛️ Música Clásica & Sacra`
    3. `🌴 Boleros & Ritmos Latinos`
    4. `🎡 Carrusel 1 · Baladas 6/8`
    5. `🌊 Baladas Pop, Soul & Rock 4/4`
    6. `🎬 Bandas Sonoras de Cine & Chanson`
    7. `📖 Manual Maestro & Guía Técnica`
  - **Segunda Capa (Listado de Canciones por Estilo):** Al pulsar un botón de estilo, se despliega la lista interior correspondiente con las canciones seleccionadas/trabajadas en **ROJO** (`song-row song-red`) y el resto en blanco (`song-row`). Incluye barra fija superior e inferior con `◀ Volver a Estilos` y soporte de URL hash (`#italianos`, `#boleros`, etc.) compatible con el botón de retroceso del navegador/iPad.
  - **Retiro de "Mis 10 Canciones" y `REPERTORIO_ACTIVO.html`:** Al ampliarse el repertorio activo a más de 10 obras, se prescinde de `REPERTORIO_ACTIVO.html`. Todas las canciones trabajadas se identifican unificadamente en rojo en el repertorio general.
  - **Botón `R` Universal en Fichas:** En todas las fichas de canciones, el botón superior izquierdo `[ R ]` redirige siempre al repertorio general: `REPERTORIO_KORG_EK50.html?v=218`.
- **Regla de 2 Ritmos Seleccionables Obligatorios en el HUD Flotante (Línea 1):**
  - Toda ficha musical en estándar Louis Armstrong (`CANCION_34_WHAT_A_WONDERFUL_WORLD.html`) debe ofrecer obligatoriamente en la Línea 1 de su cabecera HUD flotante **dos ritmos de acompañamiento a elegir** (ej. `041 Love Ballad` y `051 Slow Rock 2`, o `174 Beguine 1` y `171 Bolero Latino`, o `154 New Age` y `041 Love Ballad`) junto al botón de recarga `🔄 v218`. La Línea 2 se reserva para los Keyboard Sets Korg canónicos (MSB 33).
- **Consolidación de Comandos Acumulativos a Petición del Usuario:**
  - Cuando el usuario indique agrupar comandos pendientes desde una ejecución anterior (ej. desde el comando 149), el asistente debe sintetizarlos en un único bloque de terminal correlativo para ejecución desatendida.
- **Estándar Canónico Oficial de Fichas de Atril Virtual (Plantilla Maestra Louis Armstrong):**
  - **Plantilla Oficial Universal:** La ficha de **What a Wonderful World (`CANCION_34_WHAT_A_WONDERFUL_WORLD.html`)** es el **modelo de referencia absoluto** para todas las canciones seleccionadas en el repertorio y para cualquier nueva canción que se incorpore en el futuro.
  - **Estructura Arquitectónica Obligatoria en 5 Bloques:**
    1. **Cabecera `header-banner`:** Título y autor, badge de tonalidad y barra de navegación superior con 5 botones: `🎼 1. Partitura Cifra Club (con Botonera Korg)`, `🎼 2. Modo Atril Grande (sin Botonera)`, `🌐 MuseScore Web`, `◀ Volver al Repertorio` (hacia `REPERTORIO_KORG_EK50.html?v=218`) y recarga de versión sin caché (`🔄 vXXX`).
    2. **Calibración Web MIDI:** Selector de registro de octava (Estándar 0 y +12 st) y caja didáctica `Recordatorio Sencillo: Formación de Acordes Tríada` (Mayor 4+3, Menor 3+4, Suspendido 5+2, Disminuido 3+3).
    3. **Guía Didáctica y Modo Fingered:** Instrucciones concisas para activar el modo `Fingered` en la pantalla LCD del Korg EK-50 (`Setting` -> `Chord Scan` -> `Fingered`) y particularidades armónicas de la obra.
    4. **Progresión Armónica Canónica en Cajas Didácticas:** Desglose por secciones (Tema A, Tema B, etc.) con cajas `.part-card` y tiras de píldoras `.chord-strip` con `.chord-pill` por compás.
    5. **Modal Fullscreen con HUD en 2 Líneas Equilibradas:**
       - **Línea 1:** Estilo 1 + Estilo 2 (ambos en Canal 16) + Botón de recarga de versión `🔄 vXXX`.
       - **Línea 2:** Timbres Korg canónicos (Banco Maestro MSB 33) + Botón de emergencia `⚡ Reset Korg` (o `X` cerrar).
       - **Visor Cifra Club OLED:** Fondo negro puro (`#000000`), acordes en amarillo/ámbar (`#fbbf24`), texto en blanco nítido, sin cortes, Smart Dimming de batería a 45 minutos y NoSleep activo.

# PROTOCOLO DE CIERRE DE CHAT Y ENTREGA DE HERENCIA UNIVERSAL
- **Activación:** Cuando el usuario indique que quiere cerrar el chat (ej. *"quiero cerrar el chat"*, *"cierra el chat"*, *"dame la frase de cierre"*, *"vamos a pasar a otro chat"*, etc.):
  1. **Actualización Obligatoria del Documento Vivo:** El asistente debe actualizar inmediatamente [`ESTADO_GLOBAL_PROYECTOS.md`](file:///Users/externo/Library/Mobile%20Documents/com~apple~CloudDocs/PERSONAL/CLASES%20DE%20TECNOLOG%C3%8DA/ESTADO_GLOBAL_PROYECTOS.md) en la raíz con los últimos avances realizados en la sesión y los números actualizados de ambos contadores:
     - Contador General: `[COMANDO XX]`
     - Contador Música: `[COMANDO MÚSICA XX]`
  2. **Entrega de la Frase Única de Herencia:** Entregar al usuario la frase formateada en negrita y bloque de cita para copiarla directamente al nuevo chat:
     > **"Revisa `ESTADO_GLOBAL_PROYECTOS.md` y continuamos según lo que te vaya pidiendo (Contador General: COMANDO [XX] / Contador Música: COMANDO MÚSICA [YY])."**
