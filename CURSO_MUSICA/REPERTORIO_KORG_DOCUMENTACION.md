# 🎼 MANUAL MAESTRO Y DOCUMENTACIÓN TÉCNICA: REPERTORIO KORG EK-50
> **Proyecto:** Sistema de Atril Digital, Control Web MIDI y Repertorio Pedagógico Interactivo  
> **Ubicación:** `CURSO_MUSICA/` · **Repositorio:** `CURSO-IA`  
> **Dispositivo Principal:** Teclado Korg EK-50 Entertainer Keyboard conectado a iPad / Mac  
> **Versión del Sistema:** v76 (Modo Atril Pantalla Completa + Botones Maestros 1 y 2)

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
* **Melodía Oficial Asignada:** **`STS Armónica`** (Harmonica acústica GM PC 21 en Upper 1).
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

---

## 5. ESTRUCTURA DE ARCHIVOS Y FLUJO DE SINCRONIZACIÓN

El proyecto opera con una arquitectura de archivos correlativa donde la documentación queda agrupada junto a los archivos ejecutables:

```
📁 CURSO-IA/
├── 📁 CURSO_MUSICA/                         <-- Repositorio de desarrollo bajo Git
│   ├── index.html                          <-- Menú principal del repertorio
│   ├── REPERTORIO_KORG_EK50.html           <-- Lista oficial de repertorio
│   ├── REPERTORIO_KORG_DOCUMENTACION.md    <-- Manual maestro en Markdown
│   ├── REPERTORIO_KORG_DOCUMENTACION.html  <-- Manual maestro visor Web PWA
│   ├── CANCION_01_TO_ALL_THE_GIRLS.html    <-- Ficha interactiva Canción 1
│   ├── CANCION_02_HALLELUJAH.html          <-- Ficha interactiva Canción 2
│   ├── CANCION_03_HYMN_TO_THE_FALLEN.html  <-- Ficha interactiva Canción 3
│   └── 📁 CANCIONES PDF/                   <-- Partituras oficiales en PDF
│       ├── Hallelujah- Leonard Cohen.pdf
│       └── Himno a los caidos.pdf
│
📁 CURSO MUSICA/                            <-- Carpeta sincronizada de acceso iPad
    ├── (Réplica idéntica 100% de los archivos anteriores)
```

---
*Manual redactado y sellado para el proyecto CURSO-IA / CURSO_MUSICA. Todos los derechos reservados.*
