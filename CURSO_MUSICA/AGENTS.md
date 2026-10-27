# REGLAS DEL PROYECTO: REPERTORIO KORG EK-50 & ATRIL DIGITAL WEB MIDI (CURSO_MUSICA)

## 1. Regla de Oro Primordial: Flujo de Trabajo Automatizado y Cero Interrupciones (Auto-Execution)
- **PROHIBICIÓN ABSOLUTA DE SUBMITS Y VENTANAS DE APROBACIÓN EN EL CHAT:**
  - El asistente tiene **TERMINANTEMENTE PROHIBIDO** ejecutar comandos o acciones que provoquen la aparición de botones de "Submit", "Aprobar", confirmaciones o ventanas emergentes en la pantalla del usuario.
  - Queda **ESTRICTAMENTE PROHIBIDO** ejecutar herramientas de terminal intermedias (`run_command`) para inspección exploratoria de sistema, red o procesos (`ifconfig`, `lsof`, `ps`, `curl`, scripts de terminal de prueba, etc.) durante el turno de conversación.
  - Toda la lectura, análisis, creación y edición de código debe ejecutarse de forma 100% silenciosa y desatendida dentro del sandbox mediante herramientas de edición de archivos (`read_file`, `edit_file`, `write_file`).
  - Al final de la respuesta, el asistente debe entregar directamente y sin interrupciones previas **UN ÚNICO BLOQUE DE COMANDO DE TERMINAL LIMPIO Y NUMERADO** para que el usuario lo ejecute en su propia terminal externa.
- **Eliminación de Confirmaciones y Botones de Proceed:**
  - El asistente NUNCA debe solicitar confirmación manual ni requerir feedback interactivo para ejecutar planes o artefactos (`RequestFeedback: false`).
  - Todos los planes, modificaciones de código y tareas deben ejecutarse de forma directa, continua e ininterrumpida.

## 2. Regla de Oro: Actualización Obligatoria e Inmediata de la Documentación ante Todo Aprendizaje Nuevo
- **Sincronización del Conocimiento en Tiempo Real:**
  - Cada vez que se descubra, depure, aprenda o ajuste una nueva técnica, comportamiento de hardware, solución de bug, parámetro MIDI o estándar en el proyecto, el asistente DEBE actualizar simultánea e inmediatamente en ese mismo turno toda la documentación técnica correspondiente:
    1. El manual maestro en Markdown (`REPERTORIO_KORG_DOCUMENTACION.md`).
    2. El visor interactivo web (`REPERTORIO_KORG_DOCUMENTACION.html`).
    3. Las reglas de agentes y asistentes (`AGENTS.md` y `GEMINI.md`).
  - Queda terminantemente prohibido dejar descubrimientos, lecciones aprendidas o detalles técnicos aislados en la conversación del chat sin que queden permanentemente sellados y versionados en la documentación oficial del repositorio.

## 3. Regla de Oro de Unificación Canónica y Despliegue (Cero Duplicados en Disco)
- **Carpeta Única Absoluta (`CURSO-IA/CURSO_MUSICA`):**
  - Solo existe **UNA ÚNICA CARPETA FÍSICA** en todo el sistema: `CURSO-IA/CURSO_MUSICA/`.
  - Queda **TERMINANTEMENTE PROHIBIDO** mantener carpetas duplicadas externas, réplicas o enlaces simbólicos. La carpeta externa ha sido eliminada de raíz.
  - Todo el proyecto de música, atril digital, canciones y documentación reside y se ejecuta exclusivamente dentro de `CURSO-IA/CURSO_MUSICA/`.
  - Todo cambio se versiona y sube a GitHub (`git add -A`, `git commit -m "..."`, `git push origin main`) para su despliegue en GitHub Pages.
- **Prohibición Total de Archivos de Herencia en Disco:**
  - Queda **TERMINANTEMENTE PROHIBIDO** crear archivos `HERENCIA.md` (o similares) en el disco.
  - La herencia entre chats se redacta y entrega **exclusivamente como texto dentro de la respuesta del chat** cuando el usuario lo solicite, para su copia y pega directa.
- **Formato Estándar y Numeración Correlativa Obligatoria de Comandos en Terminal:**
  - **Título en Canvas / Chat:** Cada bloque entregado debe llevar su numeración correlativa secuencial (ej. `### 💻 [COMANDO 141] - Título Descriptivo`).
  - **Título y Numeración Correlativa DENTRO del Script:** El encabezado con `#` y los mensajes `echo` deben llevar exactamente la misma numeración correlativa:
    ```bash
    # ==============================================================================
    # [COMANDO XX] - TÍTULO DESCRIPTIVO DE LA TAREA
    # ==============================================================================
    cd "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
    echo "=== [COMANDO XX] INICIANDO: TÍTULO DESCRIPTIVO ==="
    # ... instrucciones ...
    echo "=== [COMANDO XX] FINALIZADO CON ÉXITO ==="
    ```

## 4. Lanzamiento y Validación Visual Dual (iMac + iPad)
- **Apertura Automática en el iMac:**
  - En cada turno donde se ajuste, modifique o cree una ficha de canción, índice o visor, el comando de terminal entregado al usuario DEBE incluir siempre la apertura automática del archivo HTML en el iMac (`open -a "Safari" "CURSO_MUSICA/..."` o navegador predeterminado).
  - Esto permite al usuario inspeccionar de inmediato en su pantalla de iMac la maquetación y cambios en 0 segundos mientras se realiza el despliegue a GitHub y prueba en iPad.
- **Simplificación Escénica (Sin Módulos Redundantes de Transposición):**
  - Mantener la pantalla limpia de selectores de transposición armónica innecesarios que ocupen espacio visual en el iPad, salvo petición expresa del usuario.
- **Acceso en iPadOS (Doble Vía):**
  - **Vía Rápida Local (Wi-Fi 0 segundos):** Mediante el servidor local Python en el puerto 8888 (`INICIAR_SERVIDOR_LOCAL.command`), accesible en el iPad desde `http://192.168.1.130:8888/`.
  - **Vía Web MIDI por Cable USB en iPad:** Ejecutando la URL en la app `Web MIDI Browser` (App Store) con `{ sysex: false }`.

## 5. Reglas de Oro del Control Web MIDI para Korg EK-50
- **Regla 1: CERO Intervención Manual en el Hardware del Teclado:**
  - El usuario NUNCA debe verse obligado a activar capas, presionar botones físicos de efectos, girar perillas ni buscar números de sonido en menús del teclado.
  - TODO (estilos, capas Upper 1/2/3, división Lower, transposición, volúmenes, efectos de reverberación, modulación/vibrato y tempo) debe configurarse al 100% de forma desatendida mediante mensajes Web MIDI enviados desde la interfaz táctil.
- **Regla 2: Protocolo Anti-Bloqueo de Arranque y Protección de Búfer USB:**
  - *Causa del Parpadeo Infinito de Botones:* Si el Korg EK-50 se enciende mientras está conectado por USB al iPad/Mac con Web MIDI activo, CoreMIDI bombardea el bus USB durante la carga de la ROM y satura el procesador del teclado, provocando un bucle de calibración de emergencia (todos los LEDs parpadean).
  - *Causa del Congelamiento "Power Off See You":* Emitir trenes continuos de reloj MIDI (`0xF8`) cada 25–40 ms en reposo desborda la memoria FIFO del Korg y bloquea su apagado.
  - *Solución Obligatoria:*
    1. Queda TERMINANTEMENTE PROHIBIDO enviar ráfagas infinitas de `0xF8` en reposo. El tempo se define en el Style y el bus MIDI permanece en silencio total.
    2. El protocolo de arranque exige: Encender siempre el Korg EK-50 primero ➔ Esperar 5 segundos a que la pantalla LCD quede fija ➔ Conectar el cable USB o abrir la página web del atril.
- **Regla 3: Mapeo General MIDI Estricto y Evitación de Trampas de Banco:**
  - *La Trampa del Acordeón vs Armónica:* En el estándar General MIDI (0–127), el Program Change 21 corresponde a **Accordion** (Acordeón). La verdadera **Harmonica** oficial es estrictamente **PC 22**. Enviar PC 21 hace que el teclado suene a acordeón.
  - *La Trampa de Caída a Grand Piano:* Enviar números de banco exóticos o códigos MSB 33 erróneos sin handshake SysEx hace que el motor sonoro del Korg rechace el patch y caiga por defecto en el Sonido 001 (*Stereo Grand Piano*), desconfigurando el efecto.
  - *Solución Oficial:* Usar `Bank 0, LSB 0, PC 22` en Upper 1 (Canal 1). Esto garantiza sonido 100% armónica pura y muestra con total fidelidad **`Harmonica`** en la pantalla LCD del teclado.
- **Regla 4: Inyección Automática de Efectos (Vibrato y Eco de Concierto):**
  - Las muestras acústicas de fábrica del Korg son planas y secas. Para dotarlas de calidez y tridimensionalidad sin tocar el teclado, inyectar obligatoriamente por canal:
    * `CC 01 = 50` (Modulación / Vibrato LFO activo).
    * `CC 77 = 68` (Profundidad del vibrato).
    * `CC 91 = 115` (Reverb Send - Eco acústico de sala amplia).
    * `CC 93 = 60` (Chorus / Ambiente estéreo tridimensional).
    * `CC 72 = 76` (Release suave para evitar cortes secos de nota).
- **Regla 5: Encendido Físico Automático de Capas en el Panel Frontal:**
  - Para que el Korg reproduzca capas simultáneas (ej. Upper 1 Cuerdas + Upper 2 Coro/Voces en el Botón 2) sin requerir que el usuario pulse botones en el panel, el script debe inyectar el comando de **Keyboard Set 61** (*The Strings*, `MSB 33, LSB 6, PC 0` en canales 1 y 16). Este comando enciende físicamente los botones retroiluminados `[UPPER 1]` y `[UPPER 2]` en el hardware del Korg de forma automática.
- **Regla 6: Acompañamiento en Lower (Mano Izquierda) Siempre Activo:**
  - El canal 4 (Lower) debe venir siempre configurado con volumen (`CC 7 = 115`), expresión (`CC 11 = 127`), reverberación (`CC 91 = 90`) y un colchón cálido (ej. `Bank 0, LSB 0, PC 52 - Choir Aahs` para voces celestiales), permitiendo que la mano izquierda acompañe con riqueza armónica.
- **Regla 7: Activación Escénica 100% Silenciosa:**
  - Al pulsar los botones maestros 1 o 2 en el atril táctil, el sistema configura estilos, parches, bancos, efectos y tempos en silencio absoluto, sin disparar ráfagas de notas espurias (*Note On*). El teclado solo emite sonido cuando el pianista posa sus dedos en las teclas.
- **Regla 8: Difusión Multi-Salida Global (`enviarMidiGlobal`):**
  - Para neutralizar las trampas de enrutamiento de CoreMIDI (donde puertos virtuales o de red ocupan la posición 0), los comandos deben enviarse en paralelo a todas las salidas USB activas (`outputs.forEach(...)`).
- **Regla 9: Modo Atril Anti-Apagado Inteligente (25 Minutos de Reposo):**
  - Implementación híbrida `WakeLock API` + `Canvas Video Loop` para mantener el iPad encendido mientras se toca, liberando el bloqueo de pantalla tras 25 minutos de inactividad total para proteger la batería.

## 6. Resumen de Canales MIDI del Korg EK-50
| Canal MIDI | Sección Korg | Función en el Repertorio | Configuración Estándar |
|:---|:---|:---|:---|
| **Canal 1 (0)** | **Upper 1** | Voz melódica principal (mano derecha) | Vol 118–127, Expr 127, Reverb 115, Vibrato CC1=50 / CC77=68 |
| **Canal 2 (1)** | **Upper 2** | Capa secundaria (cuerdas, pianos, coros) | Vol 0 (si es solo) o Vol 125 (modo dual) |
| **Canal 3 (2)** | **Upper 3** | Tercera capa | Silenciada al 0% (`CC 7 = 0`) para evitar barullo sonoro |
| **Canal 4 (3)** | **Lower** | Mano izquierda (zona de acompañamiento split) | Vol 115, PC 52 (Choir Aahs), Reverb 90 |
| **Canal 16 (15)**| **Style / KbdSet**| Control de Estilos de Acompañamiento | MSB 32, LSB 2, PC según estilo (ej. PC 9 = Estilo 042) |

## 7. Bitácora de Aprendizaje y Trampas Técnicas Resueltas
- **Lección 6.1 (SysEx en iOS):** Usar siempre `{ sysex: false }` para evitar bloqueos de seguridad en WebKit / Web MIDI Browser.
- **Lección 6.2 (Retardo CoreMIDI 350ms):** Esperar 350 ms tras DOMContentLoaded para permitir que iOS inicialice el enlace físico USB.
- **Lección 6.3 (Falso Verde):** No confiar en entradas detectadas; exigir `outputs.length > 0` para activar el estado verde de conexión.
- **Lección 6.4 (Enrutamiento CoreMIDI):** No apuntar a `outputs[0]`; enviar a todas las salidas USB con `enviarMidiGlobal()`.
- **Lección 6.5 (Silencio Escénico):** Cero notas de prueba al cambiar de preset en vivo.
- **Lección 6.6 (Calibración Dinámica):** Volúmenes solistas entre 100–120; capas entre 75–85 para evitar distorsión armónica en el preamplificador.
- **Lección 6.7 (Rompe-Caché Safari):** Headers anti-caché + parámetros dinámicos `?t=Date.now()` + distintivos de versión visibles (`vXX`).
- **Lección 6.8 (Búfer USB & Power Off):** Eliminar bucles `0xF8` en reposo; protocolo de encendido secuencial (Korg primero 5s, luego USB).
- **Lección 6.9 (Servidor Local 8888):** Servir localmente con Python para validación instantánea sin latencia de despliegue en la nube.
- **Lección 6.10 (Reposo 25 Minutos):** Balance perfecto entre atril encendido en directo y apagado automático en inactividad mediante canvas video stream.
- **Lección 6.11 (Encendido Físico de Capas):** Usar Keyboard Set 61 para encender físicamente los botones `[UPPER 1]` y `[UPPER 2]` del Korg.
- **Lección 6.12 (Armónica General MIDI):** Harmonica es PC 22 (PC 21 es Acordeón); inyectar modulación `CC 01 = 50`, `CC 77 = 68` y reverb `CC 91 = 115`.
- **Lección 6.13 (Matemática de Estilos en Korg EK-50):** Cada banco LSB agrupa 16 estilos: `Estilo = 16 * LSB + PC + 1`. Estilo 174 Beguine 1 requiere `LSB 10, PC 13` en Canal 16 a 112 BPM.
- **Lección 6.14 (Blindaje de Botón 1 con GM2 MSB 121):** Para órganos y patches melódicos, usar `Bank MSB 121` (GM2 oficial) en Canal 1 para evitar caídas a Grand Piano (MSB 0). Aislar Canal 16 exclusivamente para el estilo de acompañamiento.
- **Lección 6.15 (Motor Anti-Apagado Continuo 25 min):** Reproductor `<video>` con `canvas.captureStream(1)` invisible para iOS Safari HTTP + WakeLock en HTTPS + reposo inteligente tras 25 minutos.
- **Lección 6.16 (Inicialización Asíncrona Blindada CoreMIDI):** Para evitar que la barra quede fija en `Iniciando Web MIDI...`, verificar `document.readyState !== 'loading'` (evita listeners muertos si el DOM ya cargó), encapsular `requestMIDIAccess` en `Promise` con timeout de 3.5s, reintentar automáticamente hasta 4 veces y permitir re-escaneo con un toque (`onclick="conectarMIDI(true)"`).
- **Lección 6.17 (Repertorio Expandido a 24 Obras en 5 Categorías Temáticas):** Organización armónica con bloque italiano unificado en cabeza (1. Italianos [5], 2. Clásica [4], 3. Baladas Pop & Rock [8], 4. Latinos [4], 5. Cine & Chanson [3]).
- **Lección 6.18 (Índice Ultra-Compacto en Doble Columna sin Autores - v111):** Menú para iPad con supresión total de nombres de autores e instrumentos en portada (se mantienen dentro de cada ficha individual) y cuadrícula simétrica de 2 columnas de 33px por fila para abarcar el 100% del catálogo en una sola pantalla sin necesidad de scroll.
- **Lección 6.19 (Arquitectura de Fichas de Canción Autónomas con Botones de Instrumentos & MuseScore):** Cada obra dispone de su ficha interactiva con botones 1-Tap para configurar timbres, ritmos, volúmenes y efectos en el Korg EK-50, enlazando directamente a la partitura oficial en MuseScore sin duplicar partituras locales innecesarias.
- **Lección 6.20 (Trampa del STS Link y Aislamiento de Canal 16):** Si se reenvía Program Change a Canal 16 una vez iniciado el ritmo, el Korg EK-50 resetea Upper 1 a los instrumentos STS de fábrica. Para evitar saltos no deseados de timbre, aislar Canal 16 con la función `asegurarEstilo...()` y mantener **APAGADO** el botón físico `[STS LINK]` en el panel del Korg para que las variaciones o el fin de la intro no fuercen el sonido inicial.
- **Lección 6.21 (Estratificación Acústica Bell Piano + Ambient Warm Pad con Eco):** Para que las campanas resuenen con espacio y eco envolvente sin ser tapadas ni perder su brillo percusivo, se configura Upper 1 (FM Bell Piano) a volumen alto 122 con reverb amplia, y se acopla en Upper 2 un Ambient Warm Pad (PC 89) a volumen moderado 92 con ataque suave (CC 73 = 60), filtro cálido (CC 74 = 82), release largo (CC 72 = 105), reverb al 100% (CC 91 = 127) y chorus dimensional (CC 93 = 90). El ataque suave permite que la campana suene primero con total nitidez y el pad florezca detrás como un halo de resonancia sin enmascararla.
- **Lección 6.22 (Feedback Táctil Inmediato con Destello Visual en iPad):** Para eliminar la incertidumbre táctil en pantallas de iPad (donde la latencia de click provoca pulsaciones múltiples involuntarias), todos los botones de la ficha, HUD flotante sobre partituras y menú del repertorio disponen de feedback visual instantáneo mediante evento `pointerdown` (0 ms), reflow síncrono del DOM (`void el.offsetWidth`) y animación CSS `@keyframes destelloPulsacion` (brillo `2.8x`, halo blanco/dorado/cian y retorno suave en 450 ms).
- **Lección 6.23 (Arreglo Ramón Arcusa en Amor, Amor, Amor):** En la versión clásica de Julio Iglesias (1982), la intro melódica combina campana brillante (FM Bell Piano / Celesta) superpuesta a un lecho de violines románticos (Warm Bowed Strings) arropando cada nota con ataque suave y reverb amplia.
- **Lección 6.24 (Motor Anti-Apagado en Redes Locales HTTP sin WakeLock):** En conexiones HTTP locales (`http://192.168.1.130:8888`), iOS Safari bloquea la API `navigator.wakeLock` (solo permitida en HTTPS). Para evitar que la pantalla se apague, el stream de video de canvas (`captureStream`) requiere un generador activo de fotogramas (`setInterval` 1 fps dibujando en canvas); de lo contrario WebKit suspende el reproductor y apaga la pantalla tras 30-60 segundos. Se añade pulso activo continuo y re-activación de reproducción en cada evento `pointerdown`.
- **Lección 6.25 (Prohibición Estricta de Enviar Banco MSB 33 a Canal 16 - Causa de Bloqueo Total del Korg EK-50):** En el Korg EK-50, el Canal 16 está dedicado exclusivamente al procesador de Estilos de acompañamiento (`MSB = 32`). Enviar comandos de Keyboard Set como `MSB 33` a Canal 16 desborda la memoria de punteros de estilos del teclado, provocando un cuelgue completo del microcontrolador de la placa base (congelamiento de todos los botones y teclas del teclado). Para recuperar el teclado bloqueado, se debe reiniciar físicamente el Korg (apagar y encender tras 5 segundos). En el código MIDI, Canal 16 debe permanecer 100% aislado (`MSB 32` únicamente) y las asignaciones tímbricas de Upper 1 y Upper 2 deben realizarse con mensajes estándar GM2 (`MSB 121`) en Canal 1 y Canal 2 exclusivamente. Para activar la escucha física de Upper 2 desde el teclado, basta pulsar una vez el botón físico `[UPPER 2]` en el frontal del Korg.
- **Lección 6.26 (Arquitectura Korg EK-50: STS vs Keyboard Sets y Botón Shift):**
  1. *Keyboard Sets:* Son los más de 170 sonidos de fábrica impresos en la serigrafía del plástico negro del teclado (`011 Piano`, `031 Organ`, `061 Strings`...). Se eligen pulsando el botón físico `[KEYBOARD SET]` (se enciende su LED y la pantalla muestra `KbdSet 031`). NO llevan la palabra `STS` porque son bancos globales independientes del ritmo.
  2. *STS (Single Touch Settings):* Son las 4 combinaciones sonoras (STS 1 a 4) asociadas a cada uno de los 280 Estilos (ritmos). No tienen numeración global independiente. Se activan con los 4 botones rectangulares `[1]`, `[2]`, `[3]`, `[4]` situados bajo la pantalla LCD.
  3. *Función de SHIFT + KEYBOARD SET:* El botón físico dice `KEYBOARD SET` arriba y `STS` abajo en letra secundaria. Al pulsar `[SHIFT] + [KEYBOARD SET]`, el Korg conmuta los 4 botones inferiores para que actúen como selectores directos de `[STS 1]`, `[STS 2]`, `[STS 3]` y `[STS 4]`. En el ritmo 175 Beguine 2: Botón 1 = `STS Noisy Tenor`, Botón 3 = `STS Strings Ens`.
- **Lección 6.27 (El Secreto de la Intro de Ramón Arcusa: Balance 80/20 Campanas vs Cuerdas):** Si en una capa dual (Upper 1 + Upper 2) se configuran cuerdas con volumen alto (>100), el sustain continuo de los violines opaca por completo el ataque y definición de las campanas melódicas. El equilibrio acústico exacto de la producción de Ramón Arcusa (Julio Iglesias 1982) exige: Upper 1 con campanas cristalinas (Glockenspiel GM2 PC 9) a volumen máximo (127), brillo total (Cutoff 120) y ataque rápido (15); y Upper 2 con violines tenues (Warm Strings PC 49) a volumen muy bajo (40, sólo un 30%), ataque retardado (CC 73 = 75) y filtro cerrado sin agudos (CC 74 = 65). Las campanas protagonizan la melodía y las cuerdas aportan resonancia lejana sin enmascararlas.
- **Lección 6.28 (Anatomía del Frontal del Korg EK-50: SET LIST vs STS vs KEYBOARD SET):**
  1. *4 Botones bajo la Pantalla LCD:* Son exclusivamente las Variaciones de ritmo y los STS 1 a 4 del estilo activo.
  2. *Bloque SET LIST (con botón [BANK] y 10 botones numéricos):* NO son los STS. Son los 4 bancos x 10 memorias de usuario (40 registros) para guardar repertorios completos para conciertos.
  3. *Plantilla en Plástico Negro (011, 031 Organ...):* Son los Keyboard Sets del catálogo de 702 sonidos sueltos de fábrica.
  4. *Atril Digital con Web MIDI:* Elimina toda necesidad de interactuar manualmente con el panel físico del teclado; cada botón en el iPad inyecta de forma silenciosa e instantánea los códigos MIDI precisos.
- **Lección 6.29 (La Tímbrica Definitiva de Ramón Arcusa: Capa Dual Piano Eléctrico FM & Piano de Campanas - v133):** La intro de *Amor, Amor, Amor* (Julio Iglesias 1982) se basa en la icónica textura ochentera de piano eléctrico con campanillas. Se implementa como una capa dual perfectamente empastada: Upper 1 (Canal 1) con `Electric Piano 2` (FM Bell Piano GM2 PC 5, vol 124, Cutoff 115, Chorus 65, Reverb 110) aportando el cuerpo cálido del piano eléctrico, y Upper 2 (Canal 2) con `Glockenspiel` (GM2 PC 9, vol 114, Cutoff 122, Reverb 118) inyectando el tintineo percusivo y cristalino en el ataque de cada nota. Ambas voces suenan en estéreo simultáneo con elevación de +1 Octava, logrando el timbre legendario de la producción de Ramón Arcusa.
- **Lección 6.30 (La Revelación del Grand Piano 011 con Eco y Reverb de Concierto - v134):** El sonido 011 de fábrica del Korg EK-50 (`Acoustic Grand Piano` GM2 PC 0) se convierte en un majestuoso piano de concierto al ser procesado por Web MIDI: Upper 1 a volumen máximo (127), Reverb de sala al 100% (`CC 91 = 127`), Eco/Chorus estéreo (`CC 93 = 85`), Release prolongado (`CC 72 = 104`) y Cutoff brillante (118), con toque armónico sutil de campanilla (45) en Upper 2. Esto dota al piano acústico clásico de la profundidad, resonancia y eco característicos de las baladas románticas de Ramón Arcusa sin sonar seco.
- **Lección 6.31 (Fusión Sonora Grand Piano 011 & Campanas Glockenspiel al Unísono - v135):** Para que el timbre de la introducción de *Amor, Amor, Amor* resulte exacto al arreglo orquestal, el **Grand Piano 011** (Upper 1, vol 126, Reverb 115, Eco 70) y las **Campanas Glockenspiel** (Upper 2, vol 120, Cutoff 124, Reverb 120) deben sonar simultáneamente con volúmenes equilibrados y alta presencia, sin que ninguna de las dos voces quede reducida a un mero suspiro. Asimismo, la eliminación estricta de cualquier código residual fuera de función garantiza que el script JS no arroje syntax errors y que el modal de partitura a pantalla completa responda de inmediato al tacto.
- **Lección 6.32 (La Tetralogía de Estilos de Autor 031 a 034: Alternativa Contemporánea para Baladas Pop y Cine - v136):**
  1. *Identificación y Códigos MIDI (Canal 16):*
     - `Estilo 031 (Windy Beat)`: 8/16 Beat 2 · `MSB 32, LSB 1, PC 14` · STS: *Phase EP*. Pulso moderno con dinamismo aéreo.
     - `Estilo 032 (Home Beat)`: 8/16 Beat 2 · `MSB 32, LSB 1, PC 15` · STS: *Piano & Pad*. Calidez orgánica y base acústica íntima.
     - `Estilo 033 (Groove Bld)`: Ballad · `MSB 32, LSB 2, PC 0` · STS: *EP & VoxPad*. Balada groove sofisticada con colchón vocal.
     - `Estilo 034 (Diva)`: Ballad · `MSB 32, LSB 2, PC 1` · STS: *Pad & Ac.Gtr*. Arreglo orquestal y cinematográfico con guitarras acústicas arpegiadas.
  2. *Versatilidad Transversal:* Estos 4 estilos rompen la monotonía de los ritmos estándar y permiten versionar con aire fresco y moderno tanto obras lentas/espirituales como *Hallelujah* (Cohen), boleros/baladas latinas como *Amor, Amor, Amor* (Julio Iglesias) o grandes temas de cine como *Titanic* (Céline Dion).
- **Lección 6.33 (Caso Práctico en Amor, Amor, Amor: Style 032 con KbdSets 101 y 066 - v137):**
  1. *Estilo 032 (Home Beat) + Keyboard Set 101 (Tenor Sax):* Convierte la canción en una balada de **Smooth Jazz / Lounge nocturno** (estilo Stan Getz o Sade), sustituyendo el aire de orquesta clásica por una atmósfera íntima y aterciopelada donde el saxo respira con aire y expresividad.
  2. *Estilo 032 (Home Beat) + Keyboard Set 066 (Oct.Strings):* Transforma la obra en un **Pop Sinfónico Cinemático**, donde las cuerdas en octavas (*St. Strings* + *StringQuart* + *Oh-Ah Voices*) arropan la melodía con amplitud épica sobre el lecho acústico contemporáneo.
- **Lección 6.34 (Arquitectura Sonora del Korg EK-50: Sonidos Sueltos vs Keyboard Sets vs STS - v138):**
  1. *Sonidos Individuales (702 Sounds):* Tonos atómicos básicos de fábrica (un piano solo, una flauta sola).
  2. *Keyboard Sets (Panel / Plástico negro: 011, 031 Organ, 066 Oct.Strings, 101 Tenor Sax):* **SÍ son instrumentos compuestos**. Son preajustes universales que combinan hasta 4 capas (Upper 1, Upper 2, Upper 3 y Lower) con efectos, octavas y balances de fábrica.
  3. *STS (Single Touch Settings):* Son las 4 combinaciones compuestas exclusivas asociadas a cada Ritmo concreto (en los 4 botones bajo la pantalla LCD). Con el atril digital en iPad, Web MIDI configura las capas y efectos automáticamente sin manipulación física del teclado.
- **Lección 6.35 (Anatomía Física de Panel: LEDs de Partes, Set List y Persistencia Sonora - v139):**
  1. *LEDs de Partes (Lower, Upper 1, 2, 3):* Cada Keyboard Set define qué partes enciende: `066 (Oct.Strings)` activa las 4 a la vez por ser un colchón orquestal completo; mientras que `031 (Organ)` y `101 (Tenor Sax)` activan únicamente `Upper 1` como voces solistas melódicas.
  2. *Bloque Set List:* El botón negro `BANK/WRITE` (bancos A-J) y los 4 botones numéricos contiguos son las 40 memorias de usuario para conciertos (no son los STS del ritmo).
  3. *Persistencia Sonora:* Al elegir manualmente un Keyboard Set, el Korg preserva ese sonido al cambiar de estilo. Para que el teclado adopte el STS de fábrica del nuevo estilo, se debe pulsar `[SHIFT] + [KEYBOARD SET / STS]`. Con Web MIDI, esto se programa a 1 toque sin tocar el teclado físico.
