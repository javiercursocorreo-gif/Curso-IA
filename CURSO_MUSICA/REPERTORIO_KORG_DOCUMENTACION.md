# 🎼 MANUAL MAESTRO Y DOCUMENTACIÓN TÉCNICA: REPERTORIO KORG EK-50
> **Proyecto:** Sistema de Atril Digital, Control Web MIDI y Repertorio Pedagógico Interactivo  
> **Ubicación:** `CURSO_MUSICA/` · **Repositorio:** `CURSO-IA`  
> **Dispositivo Principal:** Teclado Korg EK-50 Entertainer Keyboard conectado a iPad / Mac  
> **Versión del Sistema:** v131 (Cuerdas Románticas Intro en Botón 2 + STS String Ensemble en Botón 3)

---

## 1. VISIÓN GENERAL Y OBJETIVOS DEL PROYECTO

El proyecto **Repertorio Korg EK-50** nace para transformar el aprendizaje y la interpretación musical en directo eliminando la fricción técnica del teclado. En lugar de obligar al músico a navegar por complejas pantallas de menús, ruedas de selección o botones físicos combinados (como *Shift + Transpose* o selección manual de capas), el sistema proporciona un **atril digital interactivo táctil** (diseñado a medida para iPadOS y Google Chrome) que comunica bidireccionalmente con el teclado mediante la **Web MIDI API**.

### Pilares Fundamentales:
1. **Control 1-Tap por Web MIDI:** Con un solo toque en pantalla se configuran el estilo de acompañamiento, los sonidos (Upper 1, Upper 2, Upper 3), los volúmenes, la transposición armónica y el tempo del teclado.
2. **Sincronización Total e Híbrida:** Todo el repertorio dispone de partituras oficiales descargadas (visor PDF integrado), guías armónicas completas compás a compás, y reproductores de audio sintetizados directamente en el navegador con la Web Audio API (para ensayar en cualquier parte sin cables).
3. **Resistencia a la Caché en iPad:** Arquitectura web con invalidación dinámica de caché para garantizar que cualquier ajuste se refleje de inmediato en el iPad.

---

## 2. ARQUITECTURA TÉCNICA Y PROTOCOLO WEB MIDI (KORG EK-50)

El Korg EK-50 se conecta al iPad o Mac mediante un cable USB estándar (USB tipo B a USB-C o Lightning con adaptador Apple Camera Kit). La comunicación se realiza sin controladores adicionales gracias al protocolo estándar **Web MIDI API (W3C)**.

### 2.1. Mapa de Canales MIDI del Korg EK-50
| Canal MIDI | Sección del Korg | Función en el Sistema |
|:---|:---|:---|
| **Canal 1** | **Upper 1** | Voz solista melódica principal (teclado mano derecha) |
| **Canal 2** | **Upper 2** | Segunda capa sonora (colchón de cuerdas, pianos o armonías) |
| **Canal 3** | **Upper 3** | Tercera capa (silenciada en el sistema para evitar saturaciones) |
| **Canal 4** | **Lower** | Parte izquierda del teclado (acompañamiento manual / división) |
| **Canal 16** | **Keyboard Set / Style** | Control de estilos de acompañamiento y configuraciones globales |

### 2.2. Comandos MIDI Clave Implementados
* **Selección de Banco y Programa:**  
  * `0xB0 | canal, 0x00, MSB` (Control Change 0: Bank Select MSB)  
  * `0xB0 | canal, 0x20, LSB` (Control Change 32: Bank Select LSB)  
  * `0xC0 | canal, ProgramChange` (Program Change)
* **Control de Volumen por Pistas:**  
  * `0xB0 | canal, 0x07, Volumen (0–127)`
* **Reloj de Sincronización (MIDI Timing Clock):**  
  * Mensaje Real-Time `0xF8` emitido a una tasa de 24 ticks por negra según el tempo ($msPerTick = \frac{60000}{BPM \times 24}$).
* **Triggers de Acompañamiento en Directo:**  
  * `0xFA` (MIDI Real-Time START): Arranca el ritmo de acompañamiento en el Korg desde la pantalla táctil.  
  * `0xFC` (MIDI Real-Time STOP): Detiene el ritmo inmediatamente.
* **Transposición Global por SysEx y RPN:**  
  * Master Coarse Tuning universal: `[0xF0, 0x7F, 0x7F, 0x04, 0x04, 0x00, semitonos, 0xF7]`  
  * Envío suplementario RPN 0,2 en los 16 canales para máxima compatibilidad.

---

## 3. ANÁLISIS DETALLADO DEL REPERTORIO OFICIAL

### 🎵 Canción 1: "To All The Girls I've Loved Before"
* **Intérpretes:** Julio Iglesias & Willie Nelson
* **Tonalidad:** Sol Mayor ($G$) en la 1ª parte ➔ Mi bemol Mayor ($E\flat$) en la 2ª parte.
* **Compás y Tempo:** 4/4 Country Ballad a **100 BPM**.
* **Estilo Korg EK-50 Asignado:** **`041 Love Ballad`** (MSB 32, LSB 2, PC 8).
* **Sonidos:**
  * Opción 1: *The Strings* (Keyboard Set 61) con St. Strings sutiles.
  * Opción 2: *Violines Agudos* (Keyboard Set 62, Bow Strings solistas brillantes).
* **Problema Resuelto (Depuración Sonora):**  
  Las capas de fábrica del Korg incluían un acordeón y cellos graves en Upper 2 y 3 que ensuciaban el sonido. El script web silencia Upper 2 y 3 al 0% y fija únicamente violines nítidos.
* **Innovación del Transposer 1-Tap:**  
  En lugar de obligar al pianista a aprender la armonía compleja en Mi bemol Mayor ($E\flat$, $Fm7$, $B\flat7$, $A\flat$) para la estrofa de Willie Nelson, la web incluye un botón que baja 4 semitonos (`-4 st`). El músico sigue tocando con los dedos los acordes fáciles de Sol Mayor ($G$, $Am7$, $D7$, $C$) y el público escucha la tonalidad original de Willie Nelson.

---

### 🎵 Canción 2: "Hallelujah"
* **Compositor:** Leonard Cohen
* **Tonalidad:** Fa Mayor ($F$).
* **Compás y Tempo:** Compás 12/8 (o 6/8 Balada) a **56 BPM** ($\♩. = 56$).
* **Estilo Korg EK-50 Asignado:** **`042`** (MSB 32, LSB 2, PC 9).
* **Melodía Oficial Asignada:** **`STS Armónica`** (Harmonica acústica GM PC 22 en Upper 1 con Vibrato CC01=50, CC77=68, Eco CC91=115 y Lower Voces PC 52).
* **Sonidos Escénicos:**
  * Opción 1: `STS Armónica (Melodía Principal) + Estilo 042`: Armónica protagonista con 56 BPM.
  * Opción 2: `Armónica & Piano (Capa Dual) + Estilo 042`: Armónica en Upper 1 con fondo de Grand Piano acústico en Upper 2.
* **Acompañamiento Web Audio Sintetizado (Offline / iPad):**  
  Generador de audio con osciladores triangulares, senoidales y filtros de decaimiento natural de macillo de piano que reproduce el arpegio 6/8 en oleadas continuas de 6 corcheas:
  * **F:** $Fa3 – La3 – Do4 – Fa4 – Do4 – La3$ (Bajo: $Fa2$ y $Do3$)
  * **Dm:** $Re3 – Fa3 – La3 – Re4 – La3 – Fa3$ (Bajo: $Re2$ y $La2$)
  * **Bb:** $Re3 – Fa3 – Si\flat3 – Re4 – Si\flat3 – Fa3$ (Bajo: $Si\flat1$ y $Fa2$)
  * **C:** $Do3 – Mi3 – Sol3 – Do4 – Sol3 – Mi3$ (Bajo: $Do2$ y $Sol2$)
  * **A:** $Do\sharp3 – Mi3 – La3 – Do\sharp4 – La3 – Mi3$ (Bajo: $La1$ y $Mi2$)
* **Visor PDF:** Partitura oficial de 3 páginas de Leonard Cohen integrada con botón de visualización conmutable sin recargar página.

---

### 🎵 Canción 3: "Hymn to the Fallen"
* **Compositor:** John Williams (BSO *Salvar al Soldado Ryan*)
* **Tonalidad:** Sol Mayor ($G$).
* **Compás y Tempo:** 4/4 Largo Solemne a **60 BPM** (Ritmo de marcha a **58 BPM**).
* **Estilo Korg EK-50 Asignado:** **`218 Military March`**.
* **Sonidos Escénicos:**
  * Opción 1: *Metales Heroicos & Coro* (Trompas solistas en Upper 1 con gran masa coral en Upper 2).
  * Opción 2: *Cuerdas Solemnes* (The Strings orquestal completo).
* **El Redoble Militar (Field Snare Drum):**
  La canción comienza con el célebre redoble militar continuo en crescendo. Se documentaron e implementaron 3 métodos de ejecución:
  1. **Manual por Teclado:** En *Orchestra Kit*, manteniendo pulsada la tecla **Re# 1 (D#1)** el Korg ejecuta automáticamente el redoble sostenido continuo.
  2. **Modo Split:** Lower = Orchestra Kit (mano izquierda mantiene el redoble), Upper = Classical Brass (mano derecha entra con la trompa en Si).
  3. **Estilo de Marcha:** Estilo 218 silenciando el acompañamiento armónico para dejar únicamente la caja sinfónica.
* **Estructura Armónica Oficial:** Desglose riguroso de las 6 frases del tema principal con notas melódicas exactas compás a compás.

---

### 🎵 Canción 4: "Cuando Calienta el Sol" (Oficial · v97)
* **Autores:** Carlos y Mario Rigual (1961 · Popularizada también por Luis Miguel).
* **Género Rítmico Musical:** Beguine / Bolero Rítmico Latino a **112 BPM**.
* **Estilo Korg EK-50 Asignado:** **`174 Beguine 1`** (Canal 16: `MSB 32, LSB 6, PC 13`).
* **Sonidos Escénicos (1-Tap Web MIDI):**
  * **Opción 1 (`🎵 1. Beguine Playero - Guitarra`):** Upper 1 = *Nylon Guitar* acústica (GM PC 24) a volumen 120, Reverb Send 105, Chorus ambiental 50 y Lower con *Choir Aahs* (PC 52, vol 110).
  * **Opción 2 (`🎻 2. Guitarra & Cuerdas - Dúo`):** Inyección de Keyboard Set 61 (*The Strings*) que enciende automáticamente los botones físicos `[UPPER 1]` y `[UPPER 2]`. Upper 1 = Guitarra Española (vol 125); Upper 2 = *St. Strings* orquestales (vol 95, Reverb 110) dando gran calidez playera sin tapar la guitarra.
* **Acompañamiento Web Audio Sintetizado (Offline / iPad):**
  * Motor sintetizador integrado en el navegador con patrón de conga sincopada latina y bajo Beguine en 4/4 con visualizador dinámico de compás.
* **Progresión Armónica Base (Tonalidad: Fa Mayor · $F$):**
  * Típica rueda de bolero latino: $F \rightarrow Dm \rightarrow Gm \rightarrow C7$.
* **Modo Atril Pantalla Completa:**
  * Barra fija superior translúcida con los botones maestros 1 y 2 para cambiar sonidos y ritmo en directo sin perder de vista la letra y los acordes.

---

### 🎵 Clasificación Temática Oficial de las 24 Obras (v109)

#### 🇮🇹 Categoría 1: Grandes Clásicos Italianos (Pop, Clásica & Cine) — 5 Obras
* **6. Volare (Nel blu dipinto di blu)** (Domenico Modugno & Franco Migliacci): Do Mayor ($C$) · Beguine / Bossa a 126 BPM · Acordeón Italiano, Saxo Alto & Cuerdas. Score MuseScore [#28739830](https://musescore.com/user/33531210/scores/28739830).
* **5. Con te partirò (Time to Say Goodbye)** (Andrea Bocelli / Sartori & Quarantotto): Sol Mayor ($G$) / Do Mayor ($C$) · Balada lírica a 70 BPM · Grand Piano & Cuerdas. Score MuseScore [#28816700](https://musescore.com/user/33531210/scores/28816700).
* **10. Adagio en Sol menor** (Tomaso Albinoni / Remo Giazotto - Venecia): Sol menor ($Gm$) · Orchestral Slow a 58 BPM · Órgano de tubos y cuerdas solemnes. Score MuseScore [#27905737](https://musescore.com/user/33531210/scores/27905737).
* **11. Senza Luce (A Whiter Shade of Pale)** (I Dik Dik / Mogol / Procol Harum): Do Mayor ($C$) · 60s Soul Ballad a 68 BPM · Órgano Hammond (PC 17 con Reverb 115). Score MuseScore [#27874576](https://musescore.com/user/33531210/scores/27874576).
* **12. Romeo y Julieta (Tema de Amor / A Time for Us)** (Nino Rota - BSO *Romeo and Juliet*): Mi menor ($Em$) · Balada Lírica a 70 BPM · Guitarra Clásica, Mandolina & Cuerdas. Score MuseScore [#27870430](https://musescore.com/user/33531210/scores/27870430).

#### 🏛️ Categoría 2: Música Clásica, Sacra & Solemne — 4 Obras
* **7. Ave Maria** (Franz Schubert): Sib Mayor ($B\flat$) · Adagio a 56 BPM · Flauta, cuerdas y gran órgano sacro con coro. Score MuseScore [#28530133](https://musescore.com/user/33531210/scores/28530133).
* **13. Canon en Re Mayor** (Johann Pachelbel): Re Mayor ($D$) · Classical a 56 BPM · Cuerdas barrocas de cámara & clavecín. Score MuseScore [#6325230](https://musescore.com/user/4592916/scores/6325230).
* **14. Air - Suite Orquestal nº 3 en Re Mayor (Aria en Sol)** (Johann Sebastian Bach - BWV 1068): Re Mayor ($D$) · Classical a 50 BPM · Violines solistas & cuerdas orquestales. Score MuseScore [#27651577](https://musescore.com/user/33531210/scores/27651577).
* **3. Hymn to the Fallen** (John Williams - BSO *Salvar al Soldado Ryan*): Marcha solemne a 58 BPM · Metales & Snare Roll continuo.

#### 🌊 Categoría 3: Grandes Baladas Pop, Soul & Rock Universal — 8 Obras
* **1. To All The Girls I've Loved Before** (Julio Iglesias & Willie Nelson): Sol Mayor ($G$) / Mib ($E\flat$) · Love Ballad a 100 BPM · Transposer 1-Tap.
* **2. Hallelujah** (Leonard Cohen): Fa Mayor ($F$) · Compás 12/8 a 56 BPM · STS Harmonica GM (PC 22) + Cuerdas + Coro.
* **15. Only You (And You Alone)** (The Platters): Sol Mayor ($G$) · Estilo: 042 Slow Rock 6/8 a 80 BPM · Grand Piano & Slow Strings. Score MuseScore [#26692978](https://musescore.com/user/33531210/scores/26692978).
* **17. Morning Has Broken** (Cat Stevens): Do Mayor ($C$) · Estilo: 125 Traditional / Folk Waltz a 128 BPM · Piano Acústico & Cuerdas. Score MuseScore [#26692870](https://musescore.com/user/33531210/scores/26692870).
* **18. Piano Man** (Billy Joel): Do Mayor ($C$) · Vals Pop Rock 3/4 a 176 BPM · Armónica GM (PC 22), Grand Piano & Acordeón. Score MuseScore [#26692240](https://musescore.com/user/33531210/scores/26692240).
* **20. Nights in White Satin** (The Moody Blues): Mi menor ($Em$) · Estilo: 042 60s Soul / Slow Rock a 54 BPM · Flauta Traversa & Cuerdas Sinfónicas. Score MuseScore [#26691493](https://musescore.com/user/33531210/scores/26691493).
* **22. Killing Me Softly with His Song** (Roberta Flack): Lab Mayor ($A\flat$) / Fa menor ($Fm$) · Estilo: 041 Love Ballad a 92 BPM · Piano Acústico & Flauta. Score MuseScore [#26680561](https://musescore.com/user/33531210/scores/26680561).
* **24. Stand by Me** (Ben E. King): La Mayor ($A$) · Estilo: 042 60s Soul a 118 BPM · Bajo Acústico, Cuerdas Staccato & Saxo. Score MuseScore [#26693062](https://musescore.com/user/33531210/scores/26693062).

#### 🌴 Categoría 4: Boleros & Ritmos Latinos — 4 Obras
* **4. Cuando Calienta el Sol** (Los Hermanos Rigual / Luis Miguel): Do Mayor ($C$) · Estilo 174 Beguine 1 a 112 BPM · Órgano de Percusión & Cuerdas.
* **9. Amor, Amor, Amor** (Julio Iglesias / Gabriel Ruiz): Do Mayor ($C$) · Estilo 175 Beguine 2 a 100 BPM · Terna Escénica Web MIDI: 1. STS Noisy Tenor (Saxo solista) / 2. Bell Piano (Upper 1) & Ambient Pad (Upper 2) con eco y resonancia / 3. String Ensemble Gran Final. Score MuseScore [#28063213](https://musescore.com/user/33531210/scores/28063213).
* **19. Perfidia** (Alberto Domínguez / Los Panchos): Do Mayor ($C$) · Estilo 174 Beguine 1 / Cha-cha a 112 BPM · Guitarra Acústica & Metales. Score MuseScore [#26692024](https://musescore.com/user/33531210/scores/26692024).
* **21. Amapola** (José María Lacalle): Fa Mayor ($F$) · Estilo 174 Beguine 1 / Canción a 108 BPM · Guitarra Clásica & Cuerdas. Score MuseScore [#26600806](https://musescore.com/user/33531210/scores/26600806).

#### 🎬 Categoría 5: Bandas Sonoras de Cine & Chanson — 3 Obras
* **8. Flashdance... What a Feeling** (Irene Cara / Giorgio Moroder): Sib Mayor ($B\flat$) · 80s Dance a 124 BPM · Synth Lead (PC 80) & Poly Synth (PC 90). Score MuseScore [#28103443](https://musescore.com/user/33531210/scores/28103443).
* **16. My Heart Will Go On** (Céline Dion / James Horner - BSO *Titanic*): Mi Mayor ($E$) · Estilo: 041 Love Ballad a 99 BPM · Tin Whistle / Flauta Celta & Cuerdas. Score MuseScore [#26692912](https://musescore.com/user/33531210/scores/26692912).
* **23. La Vie en Rose** (Édith Piaf / Louiguy): Do Mayor ($C$) · Estilo: 174 Beguine / French Musette a 92 BPM · Acordeón Musette & Violines. Score MuseScore [#26680726](https://musescore.com/user/33531210/scores/26680726).

---

## 4. INGENIERÍA WEB Y COMPATIBILIDAD CON IPADOS / SAFARI

### 4.1. El Reto de la Caché Persistente en iPad
Safari en iPadOS almacena intensamente en memoria los archivos HTML de las aplicaciones Web Clip (PWA). Para resolver definitivamente que el iPad mostrara versiones antiguas desfasadas, se aplicó una arquitectura de 4 capas:
1. **Metaetiquetas Anti-Caché:**  
   `Cache-Control: no-cache, no-store, must-revalidate` y `Pragma: no-cache`.
2. **Parámetros Dinámicos de Tiempo:**  
   Los botones de recarga ejecutan `window.location.href = window.location.pathname + '?t=' + Date.now()`, obligando a Safari a solicitar una copia fresca al servidor.
3. **Enlaces Inter-Canciones con Parámetro de Versión:**  
   Todos los enlaces navegan hacia `archivo.html?v=XX`, evitando el uso de páginas en caché local.
4. **Distintivos Visuales de Confirmación:**  
   Inclusión de badges coloreados en cabecera (`✅ Versión vXX: Canción 2 con Estilo 042 y STS Armónica`) para que el usuario verifique visualmente en 1 segundo que está en la última versión.

### 4.2. Iconografía Retina PWA
Inclusión de generación de iconos táctiles en alta resolución (192x192 px) generados dinámicamente mediante `<canvas>` e incrustados como Data URIs SVG para que al añadir el Repertorio a la pantalla de inicio del iPad luzca como una aplicación nativa de Apple.

### 4.3. Modo Escenario: Botonera Flotante (HUD) sobre Partituras vs SongBook
Uno de los grandes desafíos de la interpretación en directo es leer la partitura oficial en PDF sin perder el control de los cambios de sonido ni los ritmos del teclado:
* **El Problema en Visores Tradicionales:** Al abrir un PDF estándar en Safari o hacer scroll hacia abajo, los botones de instrumentos quedan fuera de la pantalla.
* **La Solución en SongBook / ForScore:** Aplicaciones comerciales de atril utilizan barras de herramientas flotantes que envían eventos MIDI preconfigurados. Sin embargo, SongBook requiere pago, configuración manual de textos complejos (MSB/LSB/PC) y no soporta comandos exclusivos de Korg (reloj en tiempo real `0xF8` o SysEx).
* **Nuestra Solución (Modo Atril Pantalla Completa con Botones Maestros 1 y 2):**
  1. **Pantalla Completa Real al 100%:** Al pulsar `🎼 Ver Partitura a Pantalla Completa`, se despliega un visor modal a pantalla completa total (100vw x 100vh) que maximiza la partitura oficial en el iPad sin barras del navegador.
  2. **Solo los Botones Maestros 1 y 2 (Sin Botoneras Dispersas):** En lugar de botones secundarios individuales confusos, la barra superior translúcida fija contiene exactamente los 2 botones maestros que cambian todo de golpe:
     * `[🎵 1. STS Armónica + Estilo 042]` (Carga Upper 1 Armónica + Estilo 042 + 56 BPM en 1 tap).
     * `[🎹 2. Armónica & Piano + Estilo 042]` (Carga Upper 1 Armónica + Upper 2 Piano + Estilo 042 + 56 BPM en 1 tap).
     * `[✕ Volver a la Ficha]` (Cierra el modo atril y regresa instantáneamente a la ficha didáctica).
  3. **Control 1-Tap Táctil:** El músico lee la partitura a pantalla completa y con un simple toque de dedo sobre el botón 1 o 2 cambia toda la orquestación del Korg EK-50 en vivo sin perder el compás.

### 4.4. Compatibilidad Web MIDI en iPadOS vs Mac/PC (El porqué del Botón 'R' en Safari)
Existe una diferencia técnica crucial entre el ecosistema iOS/iPadOS y los ordenadores de sobremesa:
1. **El Icono 'R' en la Pantalla de Inicio del iPad:**  
   Cuando se pulsa *"Añadir a pantalla de inicio"* en iPadOS, el sistema operativo de Apple crea un Web Clip gestionado obligatoriamente por el motor **WebKit de Safari**. Apple no permite que un acceso directo de pantalla de inicio use navegadores de terceros.
2. **La Política de Apple con Web MIDI en WebKit (iOS/iPadOS):**  
   Apple no implementa `navigator.requestMIDIAccess` en el motor WebKit de iOS ni iPadOS alegando motivos de privacidad y *fingerprinting*. Como Apple obliga a **todos los navegadores de iOS** (incluyendo Google Chrome para iPad) a usar WebKit internamente, **ni Safari ni Chrome en iPad soportan Web MIDI de forma nativa**.
3. **Las Soluciones Reales de Conexión:**
   * **Control MIDI por Cable desde iPad:** Abrir la web dentro de la app gratuita **`Web MIDI Browser`** (disponible en la App Store de Apple), la cual inyecta la API CoreMIDI en el navegador y permite que los botones 1 y 2 controlen el Korg EK-50 por cable USB.
   * **Modo Atril Visual en iPad (con el Botón 'R'):** En Safari, el iPad actúa como atril visual inteligente perfecto (partituras 100% pantalla completa, acordes, digitaciones y reproductor de acompañamiento Web Audio sin cables).
   * **Control Directo en Mac/PC:** Si se conecta el Korg EK-50 por USB al Mac o PC, abrir la web en **Google Chrome** otorga control MIDI nativo 100% inmediato sin apps adicionales.

---

## 5. ESTRUCTURA DE ARCHIVOS Y FLUJO DE SINCRONIZACIÓN

El proyecto opera con una arquitectura de archivos correlativa donde la documentación queda agrupada junto a los archivos ejecutables:

```
📁 CURSO-IA/
├── 📁 CURSO_MUSICA/                         <-- Repositorio de desarrollo bajo Git
│   ├── index.html                          <-- Menú principal del repertorio
│   ├── REPERTORIO_KORG_EK50.html           <-- Lista oficial de repertorio
│   ├── REPERTORIO_KORG_DOCUMENTACION.md    <-- Manual maestro en Markdown (Este archivo)
│   ├── REPERTORIO_KORG_DOCUMENTACION.html  <-- Manual maestro visor Web PWA
│   ├── CANCION_01_TO_ALL_THE_GIRLS.html    <-- Ficha interactiva Canción 1
│   ├── CANCION_02_HALLELUJAH.html          <-- Ficha interactiva Canción 2
│   ├── CANCION_03_HYMN_TO_THE_FALLEN.html  <-- Ficha interactiva Canción 3
│   └── 📁 CANCIONES PDF/                   <-- Partituras oficiales en PDF
│       ├── Hallelujah- Leonard Cohen.pdf
│       └── Himno a los caidos.pdf
│
📁 CURSO MUSICA/                            <-- Carpeta sincronizada de acceso iPad
    ├── (Réplica idéntica 100% de los archivos anteriores para acceso local)
```

---

## 6. LECCIONES APRENDIDAS Y BITÁCORA TÉCNICA DE DEPURACIÓN (v75 - v83)

Esta sección recopila los descubrimientos críticos de ingeniería realizados durante las sesiones de prueba con el Korg EK-50 conectado físicamente al iPad:

### 6.1. La Trampa de los Permisos SysEx en iOS/iPadOS
* **Problema:** Al invocar `navigator.requestMIDIAccess({ sysex: true })`, la app *Web MIDI Browser* en el iPad rechazaba la conexión o arrojaba errores indefinidos de seguridad.
* **Causa:** WebKit e iOS tienen bloqueados por defecto los permisos para mensajes de sistema exclusivo (*System Exclusive*) salvo configuración de certificados especiales.
* **Solución:** Pasar siempre `{ sysex: false }`. Todas las funciones esenciales (cambio de banco MSB/LSB, cambio de programa, volúmenes CC7, expresión CC11, inicio/parada de ritmo `0xFA`/`0xFC` y reloj `0xF8`) operan bajo el estándar de canal MIDI sin requerir SysEx.

### 6.2. El Retardo de Inicialización del Puente CoreMIDI (350 ms)
* **Problema:** Si JavaScript solicita el acceso MIDI inmediatamente al cargar el DOM, CoreMIDI en iOS aún no ha terminado de enlazar los puertos, arrojando "Driver Web MIDI no listo".
* **Solución:** Introducir un retardo deliberado de 350 ms en el evento `DOMContentLoaded` antes de llamar a `conectarMIDI()`, acompañado de un sistema de reintentos escalonados a los 600 ms, 1500 ms y 3000 ms.

### 6.3. La Falsa Conexión por Entrada Única (False Green)
* **Problema:** En ciertas versiones preliminares, si se detectaba un puerto de entrada pero ninguna salida USB, la barra mostraba erróneamente `🟢 Conectado`, pero la variable `midiOutput` quedaba en `null`, provocando que los botones parecieran "rotos".
* **Solución:** `bindPorts()` ahora exige explícitamente `outputs.length > 0` para activar el estado verde. Si solo hay entrada, se muestra aviso amarillo (`🟡 Entrada detectada, sin salida USB`).

### 6.4. El Enrutamiento de CoreMIDI y la Difusión Multi-Salida Global (`enviarMidiGlobal`)
* **Problema:** En iOS, CoreMIDI lista frecuentemente puertos virtuales o sesiones de red Wi-Fi (`Network Session 1`) en la posición 0 (`outputs[0]`). Enviar únicamente al primer puerto mandaba las órdenes al vacío en lugar del cable USB del Korg.
* **Solución:** Implementación de la función `enviarMidiGlobal(bytes)`, que itera y transmite cada evento a **todas las salidas USB activas simultáneamente**. Así, sin importar cómo nombre CoreMIDI al teclado (`KEYBOARD`, `KORG EK-50`, etc.) ni qué índice ocupe, la orden llega con fiabilidad del 100%.

### 6.5. Activación Escénica 100% Silenciosa (Sin Notas Espurias)
* **Problema:** Al enviar un acorde automático de confirmación auditiva al tocar los botones 1 y 2, el sonido atronaba los altavoces de forma repentina antes de que el pianista colocara las manos sobre las teclas.
* **Solución:** Los botones de escenario 1 y 2 deben ser **completamente silenciosos**. Modifican el estilo, el banco, el patch, los volúmenes y el tempo en segundo plano, sin disparar ningún evento *Note On*. El teclado solo suena cuando el músico toca físicamente las teclas.

### 6.6. Calibración de Volúmenes Digitales
* **Problema:** Enviar volumen máximo (`CC7 = 127`) saturaba el preamplificador digital del teclado, perdiendo rango dinámico.
* **Solución:** Fijar volúmenes equilibrados estándar: voz principal solista a `100–120`, capas secundarias a `75–80` y expresión a `127`.

### 6.7. El Ciclo de Despliegue en GitHub Pages y Rompe-Caché
* **Problema:** La lentitud de propagación de GitHub Pages (60 a 120 segundos) hacía creer que el iPad no se actualizaba.
* **Solución:** Distintivo de versión correlativo (`vXX`) visible en la barra y botón de recarga con marca de tiempo dinámica (`?t=Date.now()`). En cuanto la pantalla muestra la versión actual, el usuario tiene la certeza absoluta de que el código activo es el último generado.

### 6.8. Saturación de Buffer USB y Congelación de Arranque (Power Off See You & Botones Parpadeantes)
* **Problema:** El Korg EK-50 se quedaba bloqueado con todos los botones parpadeando al encenderlo, o no se apagaba mostrando permanentemente "Power Off See You".
* **Causa:** 
  1. Un temporizador infinito enviaba pulsos de reloj MIDI (`0xF8`) cada 25–40 ms, saturando el búfer USB del Korg.
  2. Si el teclado se enciende con el cable USB ya conectado al iPad y la página web activa, CoreMIDI interroga al Korg antes de que su procesador termine de cargar la ROM, entrando en bucle de calibración de emergencia.
* **Solución:**
  1. Se eliminó la emisión continua de `0xF8`: el tempo se fija en el estilo de acompañamiento y el canal USB queda completamente silencioso en reposo.
  2. **Protocolo de encendido oficial:** Enceder siempre el Korg EK-50 primero (esperar 5 segundos a que la pantalla quede fija) y luego conectar el cable USB / abrir el atril en el iPad.

### 6.9. Servidor Local Wi-Fi de Alta Velocidad (Puerto 8888)
* **Problema:** Depender de GitHub Pages obligaba a esperar 1 a 2 minutos en cada iteración de prueba.
* **Solución:** Creación del script ejecutable `INICIAR_SERVIDOR_LOCAL.command` en el Mac. Lanza un servidor Python en el puerto `8888` sirviendo la carpeta `CURSO_MUSICA/`. El iPad accede al instante a través de `http://192.168.1.130:8888/` con latencia cero y actualización en 0 segundos.

### 6.10. Modo Atril Híbrido Anti-Apagado con Reposo Inteligente a los 5 Minutos
* **Problema:** El iPad entraba en modo reposo y apagaba la pantalla a mitad de la interpretación musical, pero mantener la pantalla encendida indefinidamente agotaba la batería si el usuario se alejaba del atril.
* **Solución:** Motor híbrido `WakeLock API` + `Canvas Video Loop` (100% compatible con HTTP y Safari/MIDIWeb). Mantiene la pantalla encendida mientras se toca y apaga automáticamente el motor tras **5 minutos de inactividad total** para ahorrar batería. Cualquier toque en pantalla o tecla reinicia el contador.

### 6.11. Activación Física de Capas en Panel (Upper 1 + Upper 2 Auto)
* **Problema:** Al enviar sonidos a Upper 2 (Canal 2), el teclado no los reproducía si el botón físico `[UPPER 2]` del panel frontal del Korg estaba apagado.
* **Solución:** En el botón 2 (*Voces & Strings*), se inyecta el comando del Keyboard Set 61 (*The Strings*), que enciende físicamente los botones `[UPPER 1]` y `[UPPER 2]` en el panel frontal del Korg de forma 100% automática.

### 6.12. Anatomía de la Armónica y el Eco en Korg EK-50 (Mapeo General MIDI)
* **Problema:** Intentos de forzar presets internos del Korg mediante bancos extendidos provocaban caídas a *Accordion* o *GrandPiano* en la pantalla, perdiéndose el eco y el vibrato.
* **Causa:** En General MIDI estándar (0–127), el patch 21 corresponde a *Accordion* (acordeón), mientras que la verdadera *Harmonica* se ubica en el patch **22**.
* **Solución Definitiva (v96):**
  1. **Banco y Sonido Oficial:** `Bank 0, LSB 0, PC 22`. El teclado selecciona de forma nativa e indestructible la **Harmonica** oficial y su pantalla LCD muestra fielmente **`Harmonica`**.
  2. **Vibrato Expresivo:** Inyección de `CC 01 = 50` (Modulación / Vibrato LFO) y `CC 77 = 68` (Profundidad) para que cada nota oscile con calidez y dulzura natural.
  3. **Eco y Reverberación:** Envío de `CC 91 = 115` (Reverb Send) y `CC 93 = 60` (Chorus/Ambiente espacial), logrando la amplitud de sala de concierto que el tema requiere.
  4. **Acompañamiento en Lower (Mano Izquierda):** Canal 4 configurado con `Choir Aahs` (PC 52, vol 115, Reverb CC91=90) para que la mano izquierda toque acordes arropados por un coro celestial.

### 6.13. Fórmula Matemática de Selección de Estilos y Órgano de Percusión (v97)
* **El Misterio del Estilo 110 en lugar de 174:** Al enviar `LSB 6` y `PC 13`, la pantalla del Korg EK-50 mostró inesperadamente el Estilo 110 (*Memphis Soul* a 120 BPM).
* **Descubrimiento Matemático:** En la arquitectura interna del Korg EK-50, **cada banco LSB agrupa exactamente 16 estilos** (no 32 ni 128):
  $$\text{Número de Estilo} = 16 \times \text{LSB} + \text{PC} + 1$$
  * *Verificación con Estilo 110:* $16 \times 6 + 13 + 1 = 96 + 14 = 110$.
  * *Cálculo exacto para Estilo 174 (Beguine 1):*
    $$174 - 1 = 173 \implies 173 / 16 = 10 \text{ (resto 13)}$$
    Por lo tanto: **`LSB = 10`** y **`PC = 13`** en Canal 16 (`0xB0 | 15, 0x20, 10` y `0xC0 | 15, 13`).
* **Sincronización del Tempo a 112 BPM:** Al cargar el Estilo 174 con LSB 10, el procesador del Korg fija automáticamente su tempo nativo de **112 BPM** en el teclado, eliminando el tempo de 120 BPM del Estilo 110. Además, la botonera de velocidad (100, 112, 120 BPM) transmite trenes de pulsos `0xF8` dinámicos en directo al arrancar el acompañamiento.

### 6.14. Blindaje del Botón 1: GM2 Bank MSB 121 y Aislamiento Estricto de Canales (v99)
* **Problema:** En el Botón 1 de *Cuando Calienta el Sol*, a veces el teclado volvía a sonar como un piano o se perdía el estilo de acompañamiento.
* **Causa Identificada:**
  1. Si se enviaba un cambio de banco general (`Bank MSB 33`) al Canal 16, el Korg interpretaba que se modificaba el propio generador de estilos en lugar de la voz solista, desconfigurando el estilo 174.
  2. En el Upper 1, enviar `Bank MSB 0` hacía que el motor sonoro del Korg recurriera al banco de fábrica de pianos acústicos (Grand Piano).
* **Solución Definitiva (v99):**
  1. **Aislamiento del Canal 16:** El Canal 16 se reserva **única y exclusivamente** para la selección del estilo (`MSB 32, LSB 10, PC 13`). No se envía ningún otro mensaje de banco a este canal.
  2. **Banco Oficial GM2 en Upper 1 (Canal 1):** Se inyecta `Bank MSB 121, LSB 0, PC 17` (*Percussive Organ*). El banco 121 es el estándar GM2 universal del Korg EK-50 que blinda el timbre del órgano sin caer jamás en piano.
  3. **Volumen y Expresión:** Canal 1 fijado a Volumen 125, Expresión 127, Reverb Send 105 y Chorus/Rotary 60.

### 6.15. Motor Anti-Apagado Continuo de 25 Minutos para iPadOS en HTTP (v99)
* **Problema:** El iPad apagaba la pantalla a mitad de canción o tras 5 minutos de atril si el músico no tocaba físicamente la pantalla táctil mientras tocaba con ambas manos en el teclado físico. Además, `navigator.wakeLock` estándar es rechazado por Safari en conexiones HTTP (`http://192.168.1.130:8888`).
* **Solución Definitiva (v99):**
  1. **Loop de Video Invisible mediante Canvas Stream:** Se crea dinámicamente un elemento `<video playsinline webkit-playsinline muted loop>` invisible alimentado por un `canvas.captureStream(1)`. WebKit de iOS interpreta la reproducción de este stream continuo como una tarea multimedia activa de primer plano, impidiendo que el sistema operativo suspenda la pantalla.
  2. **Doble Capa con W3C WakeLock:** Si la conexión es segura (HTTPS), se activa complementariamente el WakeLock nativo.
  3. **Ventana de 25 Minutos de Atril Ininterrumpido:** La duración del atril se amplió de 5 a 25 minutos. Cualquier toque en pantalla, scroll o pulsación reinicia el contador de 25 minutos.

### 6.16. Adopción de la Tonalidad Oficial Do Mayor (C) y Enlaces MuseScore / YouTube (v102)
* **Motivación:** Las ediciones y arreglos oficiales de mayor difusión pedagógica (como la edición de *The Ray Charles Singers* en MuseScore [#6959865](https://musescore.com/official_scores/scores/6959865) y el arreglo de *francescobern* [#27983731](https://musescore.com/user/33531210/scores/27983731)) están estructurados en la tonalidad canónica de **Do Mayor (C)**.
* **Ventajas en el Korg EK-50:**
  1. Todos los acordes fundamentales de la rueda armónica (**C – Am – Dm – G7**) se ejecutan de manera natural sin alteraciones sostenidas ni bemoles en las notas base.
  2. Simplifica la lectura a primera vista en el atril digital y la ejecución fluida del acompañamiento latino Beguine a 112 BPM.
* **Integración Multimedia:** Se añadieron tarjetas interactivas de acceso directo a las partituras oficiales en MuseScore y a las interpretaciones históricas en YouTube (Los Hermanos Rigual 1962 y Luis Miguel 1987).

### 6.17. Ampliación del Catálogo a 20 Obras Musicales con Sincronización Web MIDI & MuseScore (v104)
* **Objetivo:** Integrar un nuevo bloque de piezas de música clásica, pop lírico y tradicional directamente en el atril interactivo, proporcionando fichas autónomas con control Web MIDI para el Korg EK-50 y enlaces de 1 toque a las partituras interactivas de MuseScore.
* **Aspectos Técnicos Implementados:**
  1. **Fichas Autónomas con Mutex Web MIDI:** Se generaron páginas interactivas (`CANCION_05_CON_TE_PARTIRO.html`, `CANCION_06_VOLARE.html`, `CANCION_07_AVE_MARIA.html`, `CANCION_08_FLASHDANCE.html`, `CANCION_09_AMOR_AMOR_AMOR.html`, `CANCION_10_ADAGIO_ALBINONI.html`, `CANCION_11_A_WHITER_SHADE_OF_PALE.html`) con el motor anti-bloqueo USB y el reproductor canvas keep-awake de 25 minutos.
  2. **Indexación y Categorización en el Menú Principal:** En `REPERTORIO_KORG_EK50.html` e `index.html` se organizó el catálogo en bloques limpios.
  3. **Resistencia a Caché en iPad:** Se elevó el parámetro de versión a `v104` en toda la botonera y enlaces.

### 6.18. Reorganización Temática en 5 Categorías con Bloque Italiano Unificado (v108)
* **Objetivo:** Agrupar armónicamente el repertorio en 5 bloques conceptuales claros (Clásicos Italianos, Música Clásica y Sacra, Baladas Pop y Rock, Ritmos Latinos y Boleros, y Bandas Sonoras de Cine), situando el bloque italiano en cabecera prioritaria.

### 6.19. Ampliación a 24 Obras Maestras con Títulos Internacionales Auténticos (v109)
* **Objetivo:** Incorporar 4 nuevas grandes obras mundiales (Amapola, Killing Me Softly with His Song, La Vie en Rose, Stand by Me) y reemplazar cualquier título genérico de estudio por su denominación oficial de éxito mundial contrastada en MuseScore.

### 6.20. Rediseño del Índice de Repertorio Compacto a 1 Sola Línea por Canción (v110)
* **Objetivo:** Optimizar la ergonomía visual del menú principal en iPad eliminando subtítulos explicativos de autor, instrumentos, tempo y estilo en la vista de lista.

### 6.21. Índice Ultra-Compacto en Doble Columna y Supresión Total de Autores (v111)
* **Objetivo:** Eliminar cualquier indicación de autores en los títulos para dejar exclusivamente el nombre limpio de la canción, y organizar las 5 categorías temáticas en una cuadrícula simétrica de 2 columnas (13 obras a la izquierda y 12 elementos a la derecha) con filas ultra-compactas de 33px de altura.
* **Resultado:** El 100% del catálogo de 24 obras maestras queda visible y accesible de forma instantánea a pantalla completa en el iPad sin necesidad de realizar scroll.

### 6.22. Destello Neón Táctil Escénico en iPadOS (v129)
* **Problema:** En el escenario o durante el estudio, el músico pulsa un botón en la pantalla táctil del iPad y, ante la ausencia de vibración o clic mecánico físico, no tiene certeza visual de si el botón se ha activado, pulsándolo repetidamente por error.
* **Solución Técnica:**
  1. Implementación de una animación CSS `@keyframes destelloPulsacion` de alta luminosidad (brillo 2.8x, contraste 1.4x, aureola neón dual blanca y dorada `#f59e0b` y anillo blanco interior `inset`).
  2. Función JavaScript `dispararDestelloBoton(el)` con reseteo de clase y forzado de reflow en el motor WebKit (`void el.offsetWidth`), garantizando que cada pulsación consecutiva dispare el destello visual de 450 ms de manera inequívoca.
  3. Aplicado a todos los botones de la ficha y a los botones flotantes del visor de partitura a pantalla completa.

### 6.23. Blindaje Anti-Apagado Continuo en iPadOS sobre HTTP mediante Generador Activo de Fotogramas (v130)
* **Problema:** Al servir las fichas musicales en red local bajo protocolo HTTP (`http://192.168.1.130:8888`), la API estándar `navigator.wakeLock` está bloqueada por las políticas de seguridad de WebKit. Además, un `<video>` alimentado por `canvas.captureStream()` se congela si el canvas no actualiza activamente sus fotogramas, permitiendo que iPadOS suspenda la pantalla tras unos minutos.
* **Solución Definitiva:**
  1. Creación de un temporizador de baja frecuencia (1 fotograma por segundo) que dibuja un píxel imperceptible en el canvas oculto, forzando la emisión ininterrumpida de video activo en el pipeline de WebKit.
  2. WebKit de iOS reconoce una reproducción de video activa de primer plano y bloquea por completo la suspensión automática de pantalla (`displaysleep`) sin importar la duración de la sesión.

### 6.24. Desbloqueo y Protección Total del Procesador Korg EK-50 (v131)
* **Problema:** Tras ciertas llamadas de cambio de sonido, el teclado Korg EK-50 quedaba completamente bloqueado: ni respondían los botones del panel ni sonaban las teclas físicas, requiriendo apagar y encender el instrumento.
* **Causa Identificada:** Enviar mensajes de selección de banco con `Bank MSB 33` (asociado a registros internos o variaciones de acompañamiento) hacia los canales melódicos Upper 1 (Canal 1) o Canal 16 desbordaba el buffer del microprocesador del teclado, entrando en un estado de fallo de firmware.
* **Regla de Blindaje:** Prohibición absoluta de enviar `Bank MSB 33` a Canal 1 o Canal 16. La selección de voces en Upper 1/2/3 se realiza exclusivamente mediante el estándar General MIDI 2 (`Bank MSB 121, LSB 0..1`), garantizando estabilidad absoluta y cero cuelgues.

### 6.25. Terna Escénica de 3 Botones para Amor, Amor, Amor (v131)
* **Diseño para Directo:**
  1. **Botón 1 (🎷 STS Noisy Tenor):** Saxo Tenor solista con garra y cuerpo (STS 1 del estilo Beguine 2 a 100 BPM).
  2. **Botón 2 (🔔 Campanas Julio Iglesias - Ramón Arcusa):** Tímbrica característica de la legendaria introducción de 1982.
  3. **Botón 3 (🎻 STS String Ensemble):** Gran sección de cuerdas sinfónicas (STS 3 de Beguine 2) para el estribillo épico y la coda final.

### 6.26. El Secreto de la Intro de Ramón Arcusa para Julio Iglesias (1982): Balance 80/20 (v132)
* **El Problema del Balance:** Si se colocan campanas y cuerdas al mismo nivel de volumen (ej. 120 y 118), la densidad armónica y el sustain de los violines opacan por completo el ataque de las campanas, perdiéndose la melodía.
* **La Solución Acústica de Ramón Arcusa:**
  1. **Upper 1 (Canal 1 - Protagonista Absoluta):** Campanas cristalinas melódicas (`GM2 PC 9: Glockenspiel` / Pop Bell) a **Volumen Máximo 127**, Expresión 127, Attack percusivo rápido (`CC 73 = 15`) y Cutoff brillante abierto (`CC 74 = 120`).
  2. **Upper 2 (Canal 2 - Lecho Orquestal Suave):** Violines cálidos (`GM2 PC 49: Warm Strings`) a **Volumen 40** (sólo un 30% del volumen solista), Attack retardado suave (`CC 73 = 75`) para entrar como un colchón detrás de cada nota sin golpe percusivo, y Cutoff cerrado (`CC 74 = 65`) sin agudos para no chocar de frecuencias con las campanas.
  3. **Resultado:** Las campanas brillan nítidas y claras en primer plano con un 300% más de presencia que las cuerdas, mientras que el colchón tenue de violines aporta la resonancia, calidez y majestuosidad de la producción de 1982.

### 6.27. Anatomía y Desmitificación del Panel Frontal del Korg EK-50: STS vs Keyboard Sets vs Set List (v132)
* **Confusión Habitual del Músico:** Dificultad para localizar los STS desde el teclado físico o confusión con las plantillas numéricas impresas en el frontal.
* **Estructura Físca Canónica del Korg EK-50:**
  1. **Los 4 Botones DEBAJO del Cristal LCD = [VARIATION / STS 1 a 4]:** Son los 4 botones alargados horizontales situados directamente debajo de la pantalla. En modo normal controlan las variaciones de batería 1 a 4; al pulsar el botón `[STS]` se convierten en los 4 sonidos de fábrica exclusivos del estilo en reproducción.
  2. **La Rótula Numérica en Plástico Negro (011, 031 Organ, 061...) = [KEYBOARD SET]:** Son los números de acceso rápido a los 702 sonidos sueltos generales de fábrica del teclado. Al pulsar `[KEYBOARD SET]` y teclear un número (ej. 013), se elige un sonido del catálogo general, por lo que **no aparece la palabra STS** en pantalla.
  3. **El Bloque [SET LIST] (con botón [BANK] y 10 botones numéricos):** Son los **bancos de memoria de usuario** (4 bancos x 10 memorias = 40 casillas). No son los STS del ritmo; sirven para que el usuario guarde sus propias combinaciones de repertorio completas para actuar en directo.
  4. **Ventaja con Web MIDI e iPad:** La botonera interactiva en el atril digital del iPad envía directamente los códigos MIDI correctos a los microprocesadores del teclado sin que el músico tenga que navegar por menús ni pulsar botones físicos en el instrumento.

---
*Manual redactado y sellado para el proyecto CURSO-IA / CURSO_MUSICA. Todos los derechos reservados.*
