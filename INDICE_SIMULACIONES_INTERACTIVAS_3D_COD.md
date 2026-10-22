# 🌌 ÍNDICE MAESTRO DE SIMULACIONES INTERACTIVAS 3D Y LABORATORIOS DE CÓDIGO [COD]
## Plan de Despliegue de las 60 Sesiones • Curso de Inteligencia Artificial
### Estándar Científico Babylon.js • Modelos Oficiales NIH, NASA y Museos • Triple Salvaguarda Pedagógica

---

## 🏛️ 1. FILOSOFÍA Y ESTÁNDAR TÉCNICO DE LA ETIQUETA [COD]

La etiqueta **`[COD]`** representa el componente de **creación activa y experimentación científica** del curso. En cada sesión, los alumnos no solo contemplan la tecnología o la ciencia, sino que aprenden a programar, probar y modificar simulaciones interactivas tridimensionales de alta fidelidad empleando inteligencia artificial (Gemini) como copiloto de código.

### 📐 Reglas Técnicas Inviolables:
1. **Motor 3D Predeterminado:** Babylon.js (`babylon.js` + `babylonjs.loaders.min.js`) con renderizado PBR (Physically Based Rendering), cámaras orbitales suaves (`ArcRotateCamera`), iluminación médica/científica sin sombras duras y optimización para 60 FPS en cualquier navegador.
2. **Prohibición de Mallas Inventadas Procedurales:** Queda prohibido el uso de esferas, conos o cilindros deformados para simular órganos o artefactos. Todos los modelos 3D son réplicas de datos científicos reales (`.glb` / `.gltf`) de repositorios oficiales:
   - **NIH 3D Print Exchange / U.S. National Library of Medicine:** Tomografías axiales (TC), resonancias (RM) y mallas anatómicas humanas reales.
   - **NASA / JPL / ESA / LRO:** Fotogrametría satelital, mapas altimétricos láser LOLA y naves espaciales de exploración real.
   - **Museos Científicos y Fondos Paleontológicos (Met Museum, FMNH Chicago, Smithsonian):** Fotogrametrías de alta precisión de fósiles, instrumentos históricos y patrimonio universal.
   - **Sociedades de Ingeniería (Khronos Group, CAD Industrial):** Modelos fidedignos de ingeniería aeroespacial y automoción.
3. **Autonomía 100% Offline (Base64 + CDN Fallback):** Para evitar fallos de CORS o caídas de conexión en el aula, los modelos científicos prioritarios se respaldan en archivos `_b64.js` dentro de `03_ASSETS_3D_Y_DATOS/`.
4. **La Triple Salvaguarda Pedagógica en [COD]:**
   - **Nivel 1 (Experiencia Activa):** *Prompt Semilla en 2 Pasos* en lenguaje humano para dictar a Gemini.
   - **Nivel 2 (Red Intermedia):** *Plano Maestro Técnico Detallado* (anexo en la ficha PDF) con las especificaciones de código.
   - **Nivel 3 (Garantía Total):** *Simulador Oficial Terminado y Desplegado* (`SIMULADOR_..._3D.html`) alojado en la carpeta de la sesión para que ningún alumno se quede rezagado.

---

## 🗺️ 2. RESUMEN EJECUTIVO DE LOS 6 LOTES DE SIMULACIONES 3D

| Lote | Rango de Sesiones | Eje Temático Científico | Simuladores Existentes | Simuladores por Desarrollar | Estado de Despliegue |
| :---: | :---: | :--- | :---: | :---: | :---: |
| **LOTE 1** | Sesiones 01 a 10 | Anatomía Humana, Paleontología, Mecánica & Astronomía Lunar | 6 / 10 | 4 / 10 | 🟡 En consolidación |
| **LOTE 2** | Sesiones 11 a 20 | Microcosmos, Acústica, Genética, Astrofísica & Órganos Vitales | 5 / 10 | 5 / 10 | 🟡 En consolidación |
| **LOTE 3** | Sesiones 21 a 30 | Física Teórica, Escalas Cósmicas, Espacio-Tiempo & Materia | 1 / 10 | 9 / 10 | ⚪ Programado (Próximo Lote) |
| **LOTE 4** | Sesiones 31 a 40 | Biología Marina, Fisiología Humana, Columna & Células | 0 / 10 | 10 / 10 | ⚪ Programado |
| **LOTE 5** | Sesiones 41 a 50 | Supercómputo, Transistores FinFET, Robótica & Fibra Óptica | 0 / 10 | 10 / 10 | ⚪ Programado |
| **LOTE 6** | Sesiones 51 a 60 | Arquitectura Monumental, Ingeniería Clásica, Medicina & Legado | 0 / 10 | 10 / 10 | ⚪ Programado |

---

## 📋 3. CATÁLOGO COMPLETO DE LAS 60 SESIONES [COD-001] A [COD-060]

---

### 📦 LOTE 1 (SESIONES 01 A 10): FUNDAMENTOS, ANATOMÍA Y GRANDES HITOS

#### 🔹 [COD-001] • Sesión 01: Árbol Traqueobronquial y Pulmones 3D
- **Archivo Oficial:** `SIMULADOR_PULMONES_3D.html`
- **Ficha PDF:** `4. COD-001_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D Print Exchange (TC torácica real en alta resolución).
- **Interactividad:** Rotación orbital 360°, selector de corte frontal coronal, visualización de árbol bronquial izquierdo y derecho, simulación de ventilación mecánica pulmonar (inhalación/exhalación) e inspección de alvéolos.
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-002] • Sesión 02: Latido Cardíaco y Anatomía del Corazón Humano 3D
- **Archivo Oficial:** `SIMULADOR_CORAZON_3D.html` *(+ Simulador complementario `SIMULADOR_MAINFRAME_COBOL_CICS.html`)*
- **Ficha PDF:** `4. COD-002_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D Print Exchange / Resonancia cardíaca humana 4D.
- **Interactividad:** Animación cíclica de sístole y diástole (60 a 100 LPM ajustable por deslizador), transparencia de ventrículos y aurículas, flujo de sangre oxigenada (roja) y desoxigenada (azul), y corte de miocardio.
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-003] • Sesión 03: Reconstrucción Arqueológica 3D de Pompeya y la Domus Romana
- **Archivo Oficial:** `SIMULADOR_POMPEYA_3D.html`
- **Ficha PDF:** `4. COD-003_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Fotogrametría Arqueológica de las Ruinas de Pompeya (Soprintendenza Archeologica).
- **Interactividad:** Comparador deslizante temporal (Año 79 d.C. con mosaicos y frescos completos vs Ruinas excavadas actuales), cámara en primera persona por el Atrio y peristilo, y explicación de arquitectura antisísmica clásica.
- **Estado:** 🟡 **EN CONSOLIDACIÓN DE FICHA**

#### 🔹 [COD-004] • Sesión 04: Anatomía del Ojo Humano, Cristalino y Óptica Biomédica 3D
- **Archivo Oficial:** `SIMULADOR_OJO_HUMANO_3D.html`
- **Ficha PDF:** `4. COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D / Banco de Óptica Biomédica.
- **Interactividad:** Simulación de haz de luz refractándose a través de córnea y cristalino, ajuste de acomodación focal (enfoque de cerca vs lejos), corte anatómico de retina, fóvea y nervio óptico, y simulación de miopía/presbicia.
- **Estado:** 🟡 **EN CONSOLIDACIÓN DE FICHA**

#### 🔹 [COD-005] • Sesión 05: Sistema Solar Interactivo y Planetario Orbital 3D
- **Archivo Oficial:** `SIMULADOR_SISTEMA_SOLAR_3D.html`
- **Ficha PDF:** `5. COD-005_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NASA Jet Propulsion Laboratory (JPL) • Efemérides orbitales Keplerianas y texturas PBR oficiales de planetas y Sol.
- **Interactividad:** Escala orbital cinemática real, selector de planetas (Mercurio a Neptuno), inclinación axial, velocidad del tiempo acelerada (1 seg = 10 días), y cámara orbital centrada en cada mundo.
- **Estado:** 🟡 **EN CONSOLIDACIÓN DE FICHA**

#### 🔹 [COD-006] • Sesión 06: Cerebro Humano, Lóbulos Corticales y Red Sináptica 3D
- **Archivo Oficial:** `SIMULADOR_CEREBRO_HUMANO_3D.html`
- **Ficha PDF:** `6. COD-006_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D / Human Connectome Project (Resonancia Magnética con tractografía funcional).
- **Interactividad:** Separación de hemisferios (izquierdo analítico / derecho intuitivo), iluminación diferencial de lóbulos (frontal, parietal, temporal, occipital), activación del hipocampo (memoria) y disparo de impulsos sinápticos luminosos.
- **Estado:** 🟡 **EN CONSOLIDACIÓN DE FICHA**

#### 🔹 [COD-007] • Sesión 07: Atlas de la Luna y Cráteres de Impacto 3D
- **Archivo Oficial:** `SIMULADOR_LUNA_3D.html`
- **Ficha PDF:** `4. COD-007_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NASA Lunar Reconnaissance Orbiter (LRO) / Altimetría Láser LOLA.
- **Interactividad:** Relieve de alta definición con sombreado dinámico del Sol (simulador de fases lunares), marcadores interactivos en Mare Tranquillitatis (Apolo 11), Cráter Tycho y Copérnico, y cara oculta de la Luna.
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-008] • Sesión 08: Motor Turbofán Aeronáutico y Mecánica CAD 3D
- **Archivo Oficial:** `SIMULADOR_MOTOR_3D.html`
- **Ficha PDF:** `4. COD-008_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Khronos Group CAD Repository / Ingeniería Aeronáutica.
- **Interactividad:** Despiece en explosión (Exploded View) de alabes del ventilador frontal, etapas de compresión de alta/baja presión, cámara de combustión, turbina y tobera de escape; control de revoluciones por minuto (RPM) y corte longitudinal transparente.
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-009] • Sesión 09: Cráneo de Tyrannosaurus Rex y Mandíbula Biomecánica 3D
- **Archivo Oficial:** `SIMULADOR_TREX_3D.html`
- **Ficha PDF:** `4. COD-009_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Field Museum of Natural History (Chicago) / Escaneo láser del espécimen fósil 'Sue' (PR2081).
- **Interactividad:** Movimiento de apertura y cierre de mandíbula con cálculo de fuerza de mordida (hasta 35.000 Newtons), inspección de dientes aserrados, fenestras temporales y comparador de escala con cráneo humano contemporáneo.
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-010] • Sesión 10: Molar Humano y Odontología Biomédica 3D
- **Archivo Oficial:** `SIMULADOR_MOLAR_3D.html`
- **Ficha PDF:** `4. COD-010_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Fotogrametría Médica Micro-CT / Odontología Quirúrgica.
- **Interactividad:** Sección transversal de corona y raíces: inspección de esmalte protector, dentina porosa, cámara pulpar vascularizada, conductos radiculares y simulación de caries incipiente vs empaste cerámico de composite.
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

---

### 📦 LOTE 2 (SESIONES 11 A 20): INSTRUMENTOS, MICROCOSMOS Y COSMOS PROFUNDO

#### 🔹 [COD-011] • Sesión 11: Violín Stradivarius 'The Gould 1693' y Acústica 3D
- **Archivo Oficial:** `SIMULADOR_STRADIVARIUS_3D.html`
- **Ficha PDF:** `4. COD-011_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** The Metropolitan Museum of Art (Met Museum, New York) / Escaneo oficial de archivo.
- **Interactividad:** Rotación sobre la madera de arce y abeto barnizado, visualización de la tapa armónica, efes (f-holes), puente acústico, alma interior (soundpost) y propagación de ondas sonoras de resonancia armónica a 440 Hz (La).
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-012] • Sesión 12: Nebulosa Planetaria Helix 'El Ojo de Dios' 3D
- **Archivo Oficial:** `SIMULADOR_HELIX_3D.html`
- **Ficha PDF:** `4. COD-012_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NASA / ESA / Hubble Space Telescope & Spitzer Infrared Telescope.
- **Interactividad:** Navegación volumétrica en 3 dimensiones a través de las capas de gas ionizado (hidrógeno rojo en periferia, oxígeno azul en el centro), enana blanca remanente en el núcleo y simulación de la muerte de una estrella similar a nuestro Sol.
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-013] • Sesión 13: Estructura Genética de la Doble Hélice de ADN 3D
- **Archivo Oficial:** `SIMULADOR_ADN_3D.html`
- **Ficha PDF:** `4. COD-013_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Protein Data Bank (PDB 1BNA) / Cristalografía de rayos X de Watson y Crick.
- **Interactividad:** Giros sobre el eje helicoidal, código de colores estricto para pares de bases complementarias (Adenina-Timina / Citosina-Guanina), esqueleto de azúcar-fosfato, y simulación de apertura de la hebra por la enzima helicasa para replicación.
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-014] • Sesión 14: Júpiter, Gran Mancha Roja y Tormentas Atmosféricas 3D
- **Archivo Oficial:** `SIMULADOR_JUPITER_3D.html`
- **Ficha PDF:** `4. COD-014_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NASA Juno Mission / Mapas globales cilíndricos de alta resolución.
- **Interactividad:** Bandas atmosféricas zonales moviéndose en sentidos opuestos, vórtice anticiclónico de la Gran Mancha Roja (tormenta mayor que la Tierra), auroras ultravioletas en los polos y visualización orbital de los 4 satélites Galileanos (Ío, Europa, Ganimedes, Calisto).
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-015] • Sesión 15: El Partenón de Atenas, Orden Dórico y Proporción Áurea 3D
- **Archivo Oficial:** `SIMULADOR_PARTENON_3D.html`
- **Ficha PDF:** `4. COD-015_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Reconstrucción Arqueológica Digital del Acrópolis de Atenas (Herencia Cultural Griega).
- **Interactividad:** Superposición interactiva de la espiral dorada de Fibonacci (\(\Phi \approx 1,618\)), curvatura sutil de estilóbatos para corrección óptica, éntasis de las columnas dóricas y recorrido virtual por la cella que albergaba la estatua de Atenea Pártenos.
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-016] • Sesión 16: Hígado Humano y Sistema Hepatobiliar 3D
- **Archivo Oficial:** `SIMULADOR_HIGADO_3D.html`
- **Ficha PDF:** `4. COD-016_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D Print Exchange / Anatomía Hepática Quirúrgica.
- **Interactividad:** Lóbulo derecho e izquierdo, vesícula biliar y conducto colédoco, red de la vena porta y arteria hepática; simulación del proceso de filtrado de toxinas, metabolización de nutrientes y producción de bilis para digestión de grasas.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 2 COD**

#### 🔹 [COD-017] • Sesión 17: Red Neuronal Sináptica y Neurotransmisores 3D
- **Archivo Oficial:** `SIMULADOR_NEURONA_SINAPSIS_3D.html`
- **Ficha PDF:** `4. COD-017_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Allen Brain Institute / Neurobiología Celular 3D.
- **Interactividad:** Soma neuronal, axón recubierto por vaina de mielina, botón sináptico microscópico liberando vesículas de dopamina y serotonina hacia receptores dendríticos, con pulsos bioeléctricos de potencial de acción en tiempo real.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 2 COD**

#### 🔹 [COD-018] • Sesión 18: Articulación de la Rodilla y Meniscos en Movimiento 3D
- **Archivo Oficial:** `SIMULADOR_RODILLA_3D.html`
- **Ficha PDF:** `4. COD-018_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D / Biomecánica Ortopédica.
- **Interactividad:** Cinemática de flexión y extensión (0° a 130°), tensión de ligamentos cruzados (anterior y posterior), amortiguación de meniscos lateral y medial sobre la meseta tibial, y simulación de desgaste de cartílago por artrosis.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 2 COD**

#### 🔹 [COD-019] • Sesión 19: Oído Medio, Tímpano y Cadena de Huesecillos 3D
- **Archivo Oficial:** `SIMULADOR_OIDO_MEDIO_3D.html`
- **Ficha PDF:** `4. COD-019_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D / Otorrinolaringología Microquirúrgica.
- **Interactividad:** Membrana timpánica vibrando por ondas acústicas de audio, transmisión mecánica de vibración por la cadena osicular (Martillo, Yunque y Estribo: los huesos más diminutos del cuerpo humano) y estimulación de la cóclea auditiva.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 2 COD**

#### 🔹 [COD-020] • Sesión 20: Péndulo Doble Caótico y Fractales de Fase 3D
- **Archivo Oficial:** `SIMULADOR_PENDULO_CAOTICO_3D.html`
- **Ficha PDF:** `4. COD-020_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Física Computacional No Lineal y Sistemas Dinámicos.
- **Interactividad:** Dos varillas articuladas con masas en los extremos; trazado tridimensional de la trayectoria estocástica del extremo libre (sensibilidad extrema a condiciones iniciales / Efecto Mariposa), con selector de gravedad terrestre, lunar o cero.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 2 COD**

---

### 📦 LOTE 3 (SESIONES 21 A 30): FÍSICA FUNDAMENTAL, ESCALAS CÓSMICAS Y EL UNIVERSO

#### 🔹 [COD-021] • Sesión 21: Escala Cósmica 3D: Del Quark a los Filamentos Galácticos
- **Archivo Oficial:** `SIMULADOR_ESCALA_UNIVERSO_3D.html`
- **Ficha PDF:** `4. COD-021_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Astrofísica Computacional / Potencias de 10 del Cosmos.
- **Interactividad:** Zoom logarítmico continuo de 61 órdenes de magnitud: desde la longitud de Planck (\(10^{-35}\) m) y quarks en el protón, pasando por células, humanos y la Tierra, hasta cúmulos de galaxias y el universo observable (\(10^{26}\) m).
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 3 COD**

#### 🔹 [COD-022] • Sesión 22: Esfera de Dyson y Megaestructuras Energéticas Kardashev 3D
- **Archivo Oficial:** `SIMULADOR_ESFERA_DYSON_3D.html`
- **Ficha PDF:** `4. COD-022_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Modelado Astrofísico Teórico / Civilizaciones Tipo II de Kardashev.
- **Interactividad:** Enjambre de espejos solares colectores orbitando a 1 Unidad Astronómica de una estrella semejante al Sol, cálculo de captura energética (\(3,8 \times 10^{26}\) W) y radiación infrarroja residual emitida al espacio.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 3 COD**

#### 🔹 [COD-023] • Sesión 23: Cero Absoluto vs Centro Solar: Termodinámica Molecular 3D
- **Archivo Oficial:** `SIMULADOR_TERMODINAMICA_MOLECULAR_3D.html`
- **Ficha PDF:** `4. COD-023_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Física Térmica y Dinámica Molecular (NIST).
- **Interactividad:** Cámara de gas donde se regula la temperatura desde 0 Kelvin (-273,15 °C: congelación cinética total de átomos) hasta 15 millones de Kelvin (plasma solar de fusión de núcleos de hidrógeno), con gráfica de energía cinética media en vivo.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 3 COD**

#### 🔹 [COD-024] • Sesión 24: Las 11 Dimensiones del Universo y Variedades Calabi-Yau 3D
- **Archivo Oficial:** `SIMULADOR_11_DIMENSIONES_3D.html`
- **Ficha PDF:** `4. COD-024_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Geometría Compleja de Supercuerdas / Variedades de Calabi-Yau (CERN).
- **Interactividad:** Proyección 3D de una sección hiperdimensional de 6 dimensiones compactificadas de la Teoría M, rotación en 4 ejes espaciales, vibración de cuerdas microscópicas abiertas y cerradas, y demostración intuitiva de dimensiones adicionales.
- **Estado:** 🟢 **100% IMPLEMENTADO Y VALIDADO**

#### 🔹 [COD-025] • Sesión 25: Relatividad Especial: Deformación Espacio-Temporal 3D
- **Archivo Oficial:** `SIMULADOR_RELATIVIDAD_LORENTZ_3D.html`
- **Ficha PDF:** `4. COD-025_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Ecuaciones de Transformación de Lorentz y Relatividad de Einstein.
- **Interactividad:** Viaje en nave espacial a velocidades relativistas (\(0,1c\) a \(0,999c\)): contracción de longitud física en la dirección del avance, dilatación temporal comparada con un reloj fijo en la Tierra y aberración relativista del campo visual estelar.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 3 COD**

#### 🔹 [COD-026] • Sesión 26: Prisma Óptico y Descomposición del Espectro Electromagnético 3D
- **Archivo Oficial:** `SIMULADOR_PRISMA_OPTICO_3D.html`
- **Ficha PDF:** `4. COD-026_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Óptica Física de Newton / Dispersión y Ley de Snell.
- **Interactividad:** Haz de luz blanca colimado incidiendo sobre un prisma triangular de cristal de cuarzo, refracción angular según longitud de onda (del rojo 700 nm al violeta 400 nm), e inspección de bandas invisibles contiguas (infrarrojo y ultravioleta).
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 3 COD**

#### 🔹 [COD-027] • Sesión 27: El Mecanismo de Anticitera y los Engranajes del Tiempo 3D
- **Archivo Oficial:** `SIMULADOR_MECANISMO_ANTICITERA_3D.html`
- **Ficha PDF:** `4. COD-027_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Reconstrucción Tomográfica del Museo Arqueológico Nacional de Atenas.
- **Interactividad:** Tren de más de 30 engranajes de bronce de dientes triangulares operando en sincronía para predecir eclipses solares y lunares según el ciclo de Saros (18 años), fases lunares con esfera bimodal y calendario de los Juegos Panhelénicos.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 3 COD**

#### 🔹 [COD-028] • Sesión 28: Fosa de las Marianas y Presión Hidrostática a 11.000 m 3D
- **Archivo Oficial:** `SIMULADOR_FOSA_MARIANAS_3D.html`
- **Ficha PDF:** `4. COD-028_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Batimetría NOAA / Módulo de descenso del batiscafo Trieste / Deepsea Challenger.
- **Interactividad:** Descenso submarino vertical estratificado (Epipelágica, Mesopelágica, Batipelágica, Abisal y Hadal en el abismo Challenger): incremento de presión hasta 1.100 atmósferas (\(1.100 \text{ kg/cm}^2\)), deformación de una lata de refresco y fauna bioluminiscente.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 3 COD**

#### 🔹 [COD-029] • Sesión 29: Transición de Fase: Hielo, Agua Líquida, Vapor y Plasma 3D
- **Archivo Oficial:** `SIMULADOR_ESTADOS_MATERIA_3D.html`
- **Ficha PDF:** `4. COD-029_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Cristalografía Molecular y Física del Estado Sólido.
- **Interactividad:** Red cristalina hexagonal de puentes de hidrógeno en el hielo (explicación de por qué el hielo flota al expandirse su volumen), ruptura a estado líquido desordenado, dispersión libre gaseosa de vapor y disociación electrónica en plasma incandescente.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 3 COD**

#### 🔹 [COD-030] • Sesión 30: Núcleo Atómico de Uranio-235 y Fisión en Cadena 3D
- **Archivo Oficial:** `SIMULADOR_FISION_NUCLEAR_3D.html`
- **Ficha PDF:** `4. COD-030_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Física Nuclear / Laboratorio Nacional de Los Álamos (LANL).
- **Interactividad:** Impacto de un neutrón térmico lento contra un núcleo inestable de U-235, oscilación y fragmentación en Bario-141 y Criptón-92 con liberación de 200 MeV de energía nuclear y 3 neutrones rápidos que desencadenan la reacción en cadena controlada en un reactor.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 3 COD**

---

### 📦 LOTE 4 (SESIONES 31 A 40): BIOLOGÍA, FISIOLOGÍA HUMANA, ECOSISTEMAS Y VIDA MARINA

#### 🔹 [COD-031] • Sesión 31: Arrecife de Coral, Pólipos y Simbiosis Marina 3D
- **Archivo Oficial:** `SIMULADOR_ARRECIFE_CORAL_3D.html`
- **Ficha PDF:** `4. COD-031_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NOAA Coral Reef Conservation Program / Fotogrametría submarina PBR.
- **Interactividad:** Estructura de carbonato cálcico de coral cerebro y cuerno de alce, micro-zoom al pólipo transparente con tentáculos urticantes y zooxantelas fotosintéticas; simulación del blanqueamiento coralino por subida de 2°C en la temperatura del agua.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 4 COD**

#### 🔹 [COD-032] • Sesión 32: Pirámide Trófica y Red Ecológica en un Ecosistema Fluvial 3D
- **Archivo Oficial:** `SIMULADOR_RED_TROFICA_3D.html`
- **Ficha PDF:** `4. COD-032_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Ecología Fluvial y Modelado de Ecosistemas Terrestres.
- **Interactividad:** Visualización estratificada de biomasa (Productores primarios de algas y plantas fluviales \(\rightarrow\) Consumidores primarios de macroinvertebrados \(\rightarrow\) Truchas \(\rightarrow\) Nutrias y Águilas pescadoras), con simulador de alteración por sobrepesca o sequía.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 4 COD**

#### 🔹 [COD-033] • Sesión 33: Mitocondria: La Central Energética Celular y Cadena de ATP 3D
- **Archivo Oficial:** `SIMULADOR_MITOCONDRIA_3D.html`
- **Ficha PDF:** `4. COD-033_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D / Biología Celular y Microscopía Electrónica Criogénica.
- **Interactividad:** Doble membrana mitocondrial, crestas internas replegadas, matriz celular y rotor molecular de la ATP sintasa girando mecánicamente impulsado por el gradiente de protones (\(H^+\)) para sintetizar trifosfato de adenosina (ATP).
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 4 COD**

#### 🔹 [COD-034] • Sesión 34: Telómeros Cromosómicos y Envejecimiento Celular 3D
- **Archivo Oficial:** `SIMULADOR_TELOMEROS_ADN_3D.html`
- **Ficha PDF:** `4. COD-034_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D / Genética Molecular Humana.
- **Interactividad:** Cromosoma condensado en forma de X, casquetes protectores terminales de telómeros (secuencias TTAGGG), visualización del acortamiento progresivo por cada ronda de división celular (Límite de Hayflick) y acción protectora de la enzima telomerasa.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 4 COD**

#### 🔹 [COD-035] • Sesión 35: Bioma de Selva Tropical: Estratos de Altura Vegetal 3D
- **Archivo Oficial:** `SIMULADOR_SELVA_TROPICAL_3D.html`
- **Ficha PDF:** `4. COD-035_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Smithsonian Tropical Research Institute / Fotogrametría Botánica.
- **Interactividad:** Corte vertical de 50 metros de jungla amazónica: suelo sombrío y hojarasca (\(2\%\) de luz solar), sotobosque de hojas gigantes, dosel continuo arbóreo (hábitat del \(80\%\) de las especies) y capa emergente de ceibas gigantes que perforan el cielo.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 4 COD**

#### 🔹 [COD-036] • Sesión 36: Molécula de Neurotoxina y Bloqueo de Canales Iónicos 3D
- **Archivo Oficial:** `SIMULADOR_NEUROTOXINA_CANAL_3D.html`
- **Ficha PDF:** `4. COD-036_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Protein Data Bank (PDB) / Toxicología Bioquímica.
- **Interactividad:** Canal iónico transmembrana de sodio (\(Na^+\)) en estado abierto conduciendo iones a través de la membrana celular de la neurona, y acoplamiento molecular de la tetrodotoxina (veneno del pez globo) taponando físicamente el poro del canal.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 4 COD**

#### 🔹 [COD-037] • Sesión 37: Piel Humana, Glándulas Sudoríparas y Termorregulación 3D
- **Archivo Oficial:** `SIMULADOR_PIEL_HUMANA_3D.html`
- **Ficha PDF:** `4. COD-037_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D / Histología Médica Cutánea.
- **Interactividad:** Las 3 capas anatómicas: epidermis con estrato córneo impermeable, dermis con vasos sanguíneos y folículos pilosos, e hipodermis grasa; simulación de vasoconstricción y temblor muscular ante frío vs sudoración y vasodilatación ante calor.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 4 COD**

#### 🔹 [COD-038] • Sesión 38: Columna Vertebral, Discos Intervertebrales y Ergonomía 3D
- **Archivo Oficial:** `SIMULADOR_COLUMNA_VERTEBRAL_3D.html`
- **Ficha PDF:** `4. COD-038_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D / Escaneo CT Ortopédico Espinal Completo.
- **Interactividad:** Segmentos cervical (C1-C7), dorsal (D1-D12) y lumbar (L1-L5); simulación dinámica de levantamiento de una caja de 10 kg con piernas rectas flexionando la cintura (fuerza destructiva de 350 kg sobre L5-S1) vs flexión correcta con rodillas (fuerza reducida a 50 kg).
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 4 COD**

#### 🔹 [COD-039] • Sesión 39: Mimetismo Animal: Escamas Iridiscentes de Mariposa Morpho 3D
- **Archivo Oficial:** `SIMULADOR_MIMETISMO_OPTICO_3D.html`
- **Ficha PDF:** `4. COD-039_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Microscopía Electrónica de Barrido (SEM) / Museo de Historia Natural de Londres.
- **Interactividad:** Escamas microscópicas de la mariposa azul Morpho: demostración de que su color no es pigmento químico, sino interferencia estructural de nanocrestas de queratina que reflejan exclusivamente la longitud de onda azul bajo luz blanca.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 4 COD**

#### 🔹 [COD-040] • Sesión 40: Regeneración Tisular y Cicatrización Celular 3D
- **Archivo Oficial:** `SIMULADOR_CICATRIZACION_TISULAR_3D.html`
- **Ficha PDF:** `4. COD-040_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NIH 3D / Biología Regenerativa y Matriz Extracelular.
- **Interactividad:** Simulación cronológica de una herida cutánea: formación del tapón de plaquetas y fibrina, llegada de macrófagos para fagocitar bacterias, migración de fibroblastos sintetizando colágeno nuevo y reepitelización de la superficie en 7 días.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 4 COD**

---

### 📦 LOTE 5 (SESIONES 41 A 50): COMPUTACIÓN, REDES, ENERGÍA Y ALTA TECNOLOGÍA

#### 🔹 [COD-041] • Sesión 41: Cable Submarino Transatlántico y Señal Láser por Fibra Óptica 3D
- **Archivo Oficial:** `SIMULADOR_FIBRA_OPTICA_SUBMARINA_3D.html`
- **Ficha PDF:** `4. COD-041_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Ingeniería de Telecomunicaciones Oceánicas (Submarine Telecoms Forum).
- **Interactividad:** Sección multicapa de un cable intercontinental (núcleo de fibra de vidrio puro, tubo de cobre de alimentación, armadura de hilos de acero trenzado y polietileno hidrófugo), reflexión interna total de pulsos láser luminosos a 200.000 km/s y repetidores ópticos de erbio submarinos.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 5 COD**

#### 🔹 [COD-042] • Sesión 42: Criptografía Asimétrica: Algoritmo RSA y Cajas Fuertes Matemáticas 3D
- **Archivo Oficial:** `SIMULADOR_CRIPTOGRAFIA_RSA_3D.html`
- **Ficha PDF:** `4. COD-042_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Criptografía Matemática y Ciencias de la Computación.
- **Interactividad:** Metáfora visual en 3D de candados y llaves: una llave pública de candado abierto enviada libremente por la red para que cualquiera encierre un mensaje cifrado, y una llave privada matemáticamente vinculada (factorización de números primos gigantes) que solo el destinatario posee para abrirlo.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 5 COD**

#### 🔹 [COD-043] • Sesión 43: Sensor Digital CMOS, Matriz de Filtros Bayer y Fotones 3D
- **Archivo Oficial:** `SIMULADOR_SENSOR_CMOS_BAYER_3D.html`
- **Ficha PDF:** `4. COD-043_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Fotónica y Semiconductores de Imagen Digital (IEEE).
- **Interactividad:** Matriz de fotodiodos de silicio cubiertos por el mosaico de microfiltros de color RGGB (50% verdes por sensibilidad del ojo humano, 25% rojos y 25% azules), conversión de fotones de luz en electrones y algoritmo de demosaicing para componer una imagen RGB a color.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 5 COD**

#### 🔹 [COD-044] • Sesión 44: Disco Duro Mecánico: Cabezal Magnético a Escala Nanométrica 3D
- **Archivo Oficial:** `SIMULADOR_DISCO_DURO_3D.html`
- **Ficha PDF:** `4. COD-044_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Ingeniería de Grabación Magnética (Storage Networking Industry Association).
- **Interactividad:** Platos de aleación de aluminio pulido como espejos girando a 7.200 RPM, brazo actuador de bobina electromagnética y deslizador de cabezal volando sobre un cojín de aire a solo 3 nanómetros de altura sobre la superficie grabando bits magnéticos 0 y 1.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 5 COD**

#### 🔹 [COD-045] • Sesión 45: Transistor FinFET de 3 nm y Litografía Ultravioleta Extrema (EUV) 3D
- **Archivo Oficial:** `SIMULADOR_TRANSISTOR_FINFET_3D.html`
- **Ficha PDF:** `4. COD-045_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Semiconductores Nanométricos / Arquitectura FinFET y Gate-All-Around (GAA).
- **Interactividad:** Aleta de silicio vertical tridimensional rodeada por tres lados por la puerta de control metálica (evita fugas cuánticas de corriente a escala nanométrica), conmutación de encendido/apagado al aplicar voltaje de compuerta y haz láser EUV de 13,5 nm reflejado en espejos Bragg.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 5 COD**

#### 🔹 [COD-046] • Sesión 46: Brazo Robótico Industrial de 6 Ejes y Cinemática Inversa 3D
- **Archivo Oficial:** `SIMULADOR_BRAZO_ROBOTICO_3D.html`
- **Ficha PDF:** `4. COD-046_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Robótica Industrial y Automatización CAD (ISO 9283).
- **Interactividad:** Seis articulaciones rotacionales independientes (Base, Hombro, Codo, Tres muñecas de orientación); puntero interactivo en el espacio 3D para probar algoritmos de cinemática inversa en tiempo real mientras el efector final sigue una trayectoria de soldadura o ensamblaje.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 5 COD**

#### 🔹 [COD-047] • Sesión 47: Visor de Realidad Virtual: Lentes Fresnel y Rastreo Espacial 6DOF 3D
- **Archivo Oficial:** `SIMULADOR_OPTICA_VR_6DOF_3D.html`
- **Ficha PDF:** `4. COD-047_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Óptica de Realidad Extendida (XR) y Sistemas Sensoriales Espaciales.
- **Interactividad:** Trayectoria de los rayos de luz desde dos micro-pantallas OLED de alta densidad a través de los anillos concéntricos de una lente Fresnel que expande el campo visual a 110°, y diagrama de los 6 grados de libertad (Pitch, Yaw, Roll, X, Y, Z).
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 5 COD**

#### 🔹 [COD-048] • Sesión 48: Reactor de Fusión Nuclear Tokamak y Confinamiento de Plasma 3D
- **Archivo Oficial:** `SIMULADOR_TOKAMAK_FUSION_3D.html`
- **Ficha PDF:** `4. COD-048_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Proyecto ITER (International Thermonuclear Experimental Reactor) / Física de Plasmas.
- **Interactividad:** Cámara de vacío toroidal en forma de donut, bobinas superconductoras magnéticas de campo poloidal y toroidal conteniendo un plasma de Deuterio-Tritio a 150 millones de grados centígrados sin que toque las paredes refrigeradas de berilio y tungsteno.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 5 COD**

#### 🔹 [COD-049] • Sesión 49: Arquitectura de Supercomputador y Clúster Exaescalar Líquido 3D
- **Archivo Oficial:** `SIMULADOR_SUPERCOMPUTADOR_3D.html`
- **Ficha PDF:** `4. COD-049_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** TOP500 Supercomputing / Arquitecturas HPC y Refrigeración por Inmersión Dieléctrica.
- **Interactividad:** Racks de servidores con placas aceleradoras de IA conectadas por switches de interconexión óptica de ultra-baja latencia (InfiniBand a 800 Gbps), circulación de refrigerante líquido transparente no conductor extrayendo kilovatios de calor a 1 ExaFLOP.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 5 COD**

#### 🔹 [COD-050] • Sesión 50: Topología de Internet: Paquetes TCP/IP y Ruteo Troncal 3D
- **Archivo Oficial:** `SIMULADOR_RUTEO_INTERNET_TCP_3D.html`
- **Ficha PDF:** `4. COD-050_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Protocolos de Red IETF / Mapeo de Sistemas Autónomos (BGP).
- **Interactividad:** Emisión de un archivo fraccionado en 50 paquetes numerados; visualización de cada paquete tomando rutas geográficas independientes y divergentes por nodos intermedios de fibra para esquivar enlaces saturados, y ensamblaje perfecto en destino por el protocolo TCP.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 5 COD**

---

### 📦 LOTE 6 (SESIONES 51 A 60): ARQUITECTURA MONUMENTAL, INGENIERÍA CLÁSICA Y LEGADO HUMANO

#### 🔹 [COD-051] • Sesión 51: Catedral Gótica: Arbotantes, Bóvedas de Crucería y Cargas 3D
- **Archivo Oficial:** `SIMULADOR_CATEDRAL_GOTICA_3D.html`
- **Ficha PDF:** `4. COD-051_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Arquitectura e Ingeniería Estructural Medieval / Catedral de Chartres y Notre Dame.
- **Interactividad:** Vectorización tridimensional de empujes gravitatorios y diagonales: cómo los arcos apuntados dirigen las toneladas de peso de la piedra hacia los arbotantes exteriores y contrafuertes con pináculos de plomo, liberando los muros para abrir gigantescos vitrales luminosos.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 6 COD**

#### 🔹 [COD-052] • Sesión 52: La Ciudad Romana: Cardo Máximo, Decumano e Insulae 3D
- **Archivo Oficial:** `SIMULADOR_CIUDAD_ROMANA_3D.html`
- **Ficha PDF:** `4. COD-052_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Urbanismo Clásico Romano / Timgad (Argelia) y Ostia Antica.
- **Interactividad:** Traza hipodámica ortogonal centrada en el cruce del Cardo y el Decumano, plaza del Foro con basílica civil y templo, termas públicas con hipocausto de suelo radiante bajo el caldarium, y bloques de viviendas colectivas de varios pisos (insulae).
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 6 COD**

#### 🔹 [COD-053] • Sesión 53: Locomotora de Vapor de George Stephenson (1829): La 'Rocket' 3D
- **Archivo Oficial:** `SIMULADOR_LOCOMOTORA_VAPOR_3D.html`
- **Ficha PDF:** `4. COD-053_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Science Museum Group (Londres) / Escaneo oficial de la locomotora 'The Rocket'.
- **Interactividad:** Hogar de fuego de carbón, caldera tubular de evaporación múltiple, cilindros de expansión de vapor alternativo empujando pistones acoplados a bielas mecánicas conectadas directamente a las grandes ruedas motrices de fundición de hierro.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 6 COD**

#### 🔹 [COD-054] • Sesión 54: Acueducto Romano de Segovia: Sillería en Seco y Sifón 3D
- **Archivo Oficial:** `SIMULADOR_ACUEDUCTO_SEGOVIA_3D.html`
- **Ficha PDF:** `4. COD-054_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Fotogrametría Arquitectónica del Acueducto de Segovia (Patrimonio de la Humanidad UNESCO).
- **Interactividad:** Los 167 arcos dobles de granito de la sierra de Guadarrama colocados 'a hueso' (sin mortero ni cemento, sostenidos exclusivamente por el equilibrio de fuerzas de compresión), canal superior (specus) con pendiente constante milimétrica del \(1\%\) y desarenador inicial.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 6 COD**

#### 🔹 [COD-055] • Sesión 55: Brazo Quirúrgico Laparoscópico Da Vinci y Cirugía Robótica 3D
- **Archivo Oficial:** `SIMULADOR_ROBOT_QUIRURGICO_3D.html`
- **Ficha PDF:** `4. COD-055_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Cirugía Asistida por Computador y Robótica Médica de Precisión (Intuitive Surgical).
- **Interactividad:** Los cuatro brazos articulados con pinzas microquirúrgicas EndoWrist de 7 grados de libertad (capaces de girar más que la muñeca humana sin temblor fisiológico), cámara estereoscópica 3D endoscópica y simulación de sutura microscópica en modelo de prueba.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 6 COD**

#### 🔹 [COD-056] • Sesión 56: Granja Vertical Hidropónica y Espectro LED Agronómico 3D
- **Archivo Oficial:** `SIMULADOR_GRANJA_VERTICAL_3D.html`
- **Ficha PDF:** `4. COD-056_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Agronomía Espacial y Agricultura Urbana en Ambiente Controlado (CEA).
- **Interactividad:** Módulos apilados en estanterías verticales de 6 metros donde crecen lechugas y fresas con raíces sumergidas en una película recirculante de agua y nutrientes minerales (\(95\%\) de ahorro de agua respecto al campo tradicional), con luces LED regulables entre azul vegetativo (450 nm) y rojo de floración (660 nm).
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 6 COD**

#### 🔹 [COD-057] • Sesión 57: Puente Colgante de Acero: Cables Catentarios y Tensión 3D
- **Archivo Oficial:** `SIMULADOR_PUENTE_COLGANTE_3D.html`
- **Ficha PDF:** `4. COD-057_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Ingeniería Estructural de Puentes de Gran Luz (Golden Gate / Akashi Kaikyō).
- **Interactividad:** Dos torres gigantescas de acero cimentadas en el lecho marino soportando los cables maestros principales curvados en catenaria natural hiperbólica; péndolas verticales que suspenden el tablero vehicular y simulación de oscilaciones aerodinámicas ante ráfagas de viento.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 6 COD**

#### 🔹 [COD-058] • Sesión 58: Módulo Lunar Eagle (Apolo 11) en el Mar de la Tranquilidad 3D
- **Archivo Oficial:** `SIMULADOR_APOLO11_EAGLE_3D.html`
- **Ficha PDF:** `4. COD-058_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** NASA 3D Resources / National Air and Space Museum (Smithsonian).
- **Interactividad:** Desglose del Módulo de Descenso (con las cuatro patas articuladas envueltas en láminas doradas de mylar y tobera de descenso) y el Módulo de Ascenso donde viajaban Armstrong y Aldrin; recreación de la escalerilla y la placa conmemorativa: *"Here men from the planet Earth first set foot upon the Moon. July 1969 AD. We came in peace for all mankind."*
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 6 COD**

#### 🔹 [COD-059] • Sesión 59: Criogenia y Liofilización al Vacío: Sublimación de Alimentos 3D
- **Archivo Oficial:** `SIMULADOR_LIOFILIZACION_CRIOGENICA_3D.html`
- **Ficha PDF:** `4. COD-059_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Biotecnología de Alimentos y Tecnología Aeroespacial de Preservación.
- **Interactividad:** Diagrama de fases tridimensional del agua mostrando el punto triple (\(0,01\) °C y \(611,65\) Pa): congelación instantánea a -50 °C y aplicación de bomba de vacío para que los cristales de hielo del alimento sublimen directamente a gas vapor sin pasar por estado líquido, manteniendo al 100% las vitaminas y forma por 25 años.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 6 COD**

#### 🔹 [COD-060] • Sesión 60: La Imprenta de Gutenberg (1440): Prensa de Husillo y Tipos Móviles 3D
- **Archivo Oficial:** `SIMULADOR_IMPRENTA_GUTENBERG_3D.html`
- **Ficha PDF:** `4. COD-060_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf`
- **Fuente del Modelo:** Gutenberg Museum Mainz / Reconstrucción Histórica Oficial.
- **Interactividad:** Prensa mecánica de madera de roble con husillo de hierro, caja de componer con tipos móviles individuales de aleación de plomo, estaño y antimonio, tampones de cuero para untar la tinta al óleo negra, tímpano y frasqueta sujetando el pliego de papel de trapo, y palanca manual de presión para estampar la página de la Biblia de 42 líneas.
- **Estado:** ⚪ **PROGRAMADO PARA LOTE 6 COD**

---

## 🎯 4. HOJA DE RUTA DE EJECUCIÓN (METODOLOGÍA POR LOTES EN CHATS INDEPENDIENTES)

Siguiendo la instrucción estricta del usuario:
> *"y después vamos a implementar las que quedan en lotes como hemos hecho hasta ahora. Tu trabajo será en silencio y cada lote será en un chat nuevo."*

El despliegue se estructurará de la siguiente forma ordenada y metódica:

1. **LOTE 1 [COD] (Sesiones 01 a 10):**
   - Consolidar las 10 fichas técnicas `build_pdf_cod_001.py` a `010.py` y sus simuladores 3D oficiales correspondientes.
2. **LOTE 2 [COD] (Sesiones 11 a 20):**
   - Consolidar las 5 simulaciones existentes (Stradivarius, Helix, ADN, Júpiter, Partenón) e implementar las 5 restantes (Hígado, Sinapsis, Rodilla, Oído Medio, Péndulo Caótico).
3. **LOTE 3 [COD] (Sesiones 21 a 30):**
   - Implementar las 9 simulaciones 3D de física y cosmología (Escala Cósmica, Dyson, Cero Absoluto, Lorentz, Prisma, Anticitera, Marianas, Materia, Fisión) junto al ya existente `SIMULADOR_11_DIMENSIONES_3D.html`.
4. **LOTE 4 [COD] (Sesiones 31 a 40):**
   - Implementar las 10 simulaciones 3D de biología, fisiología y ecosistemas.
5. **LOTE 5 [COD] (Sesiones 41 a 50):**
   - Implementar las 10 simulaciones 3D de supercómputo, fibra óptica, transistores y robótica.
6. **LOTE 6 [COD] (Sesiones 51 a 60):**
   - Implementar las 10 simulaciones 3D monumentales de arquitectura, ingeniería histórica, exploración espacial y legado de Gutenberg.

*En cada chat nuevo se ejecutará un único lote de forma 100% desatendida y silenciosa, entregando al final el bloque de terminal numerado y la validación inmediata en Safari.*

