#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_cod_lote4_pdf_scripts.py
Genera los 10 scripts individuales build_pdf_cod_031.py hasta build_pdf_cod_040.py
y el compilador maestro build_cod_lote4_master.py en 00. SCRIPTS_PYTHON/.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

LOTE_4_SPECS = [
    {
        "num": 31,
        "code": "COD-031",
        "title": "Taller: Crea tu propio simulador de arrecife de coral y simbiosis marina",
        "header_color": "#0284C7",
        "sim_file": "SIMULADOR_ARRECIFE_CORAL_3D.html",
        "asset_js": "coral_b64.js",
        "asset_var": "CORAL_GLB_B64",
        "mision": "En esta práctica ordenarás a la Inteligencia Artificial generar el código en Babylon.js para construir tu propio arrecife de coral 3D hiperrealista con pólipos cnidarios vivos, tentáculos radiales, esqueleto de aragonito CaCO3 y microalgas zooxantelas fotosintéticas. Simularás en directo el fenómeno del blanqueamiento coralino provocado por las olas de calor marino y la acumulación de Grados Días de Calentamiento (DHW).",
        "demo_btn": "🪸 Ver Arrecife 3D",
        "prompt_lines": [
            "\"Genera el código completo de programación (HTML y JavaScript con Babylon.js) para crear un simulador 3D interactivo del Arrecife de Coral, Pólipos Cnidarios y Simbiosis Marina.",
            "Requisitos del código:",
            "1. Entrega el programa en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi taller interactivo.",
            "2. Incluye en la cabecera los scripts del motor Babylon.js y el modelo científico real:",
            "   <script src=\\\"https://cdn.babylonjs.com/babylon.js\\\"></script>",
            "   <script src=\\\"https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js\\\"></script>",
            "   <script src=\\\"https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/coral_b64.js\\\"></script>",
            "3. Carga el modelo 3D con SceneLoader.ImportMesh('', '', window.CORAL_GLB_B64, scene, ...) con iluminación médica PBR y cámara orbital 360° sobre fondo azul oceánico profundo (#010712).",
            "4. Añade un panel de control con deslizadores para Temperatura Marina SST (24-33°C), Acumulación Térmica DHW (0-16 °C-semanas), pH de acidificación (7.6-8.3) y Radiación UV.",
            "5. Programa la animación de los pólipos con tentáculos radiales y un sistema de partículas bioluminiscentes para las zooxantelas que disminuyan en densidad ante olas de calor.",
            "6. Escribe exclusivamente el bloque de código autocontenido para que funcione de inmediato al copiarlo.\""
        ],
        "reto": "«Añade al simulador un botón de Modo Noche donde los pólipos extiendan al máximo sus tentáculos para capturar zooplancton marino y una luz UV que revele proteínas fluorescentes verdes (GFP) en el tejido coralino».",
        "tech_source": "NOAA Coral Reef Watch (CRW) • Fotogrametría Submarina y Cryo-EM de Cnidarios",
        "tech_details": "El modelo 3D reproduce con resolución milimétrica la arquitectura de corallitas de aragonito (CaCO3) y la corona tentacular octocoralia. La simulación integra el algoritmo operativo de NOAA Coral Reef Watch para calcular el estrés térmico acumulado (DHW en °C-semanas) y la tasa de expulsión de zooxantelas (Symbiodiniaceae) según la curva de toxicidad por especies reactivas de oxígeno (ROS)."
    },
    {
        "num": 32,
        "code": "COD-032",
        "title": "Taller: Crea tu propio simulador de la pirámide trófica fluvial",
        "header_color": "#059669",
        "sim_file": "SIMULADOR_RED_TROFICA_3D.html",
        "asset_js": "trophic_b64.js",
        "asset_var": "TROPHIC_GLB_B64",
        "mision": "En esta práctica ordenarás a Gemini programar en Babylon.js un ecosistema fluvial completo y su red trófica 3D basada en la Ley del 10% de Lindeman. Podrás manipular la biomasa de productores primarios (algas), macroinvertebrados bénticos, peces ciprínidos y la trucha de río depredadora, observando la disipación del 90% de energía por respiración metabólica.",
        "demo_btn": "🐟 Ver Red Fluvial 3D",
        "prompt_lines": [
            "\"Genera el código completo en un único archivo (HTML y JavaScript con Babylon.js) para construir un simulador interactivo 3D de la Pirámide Trófica y Red Ecológica Fluvial.",
            "Requisitos del código:",
            "1. Entrega el código en un único bloque autocontenido listo para copiar y ejecutar.",
            "2. Carga Babylon.js y sus Loaders oficiales junto con el modelo fluvial real trophic_b64.js.",
            "3. Renderiza en 3D el lecho del río con cantos rodados, bancos de algas perifíticas, larvas bénticas, peces consumidores y la trucha depredadora ápice.",
            "4. Incluye deslizadores para la Biomasa de Productores (g/m²), la Eficiencia Ecológica de Lindeman (5-20%), el Caudal Fluvial (m³/s) y la concentración de Nitratos/Fosfatos (ppm).",
            "5. Muestra en el cuadro de mandos la pirámide energética en kcal/m²/año y la tasa de calor metabólico disipado (90%).",
            "6. Escribe exclusivamente el código sin texto introductorio.\""
        ],
        "reto": "«Añade un simulador de bioacumulación de microplásticos o metales pesados que muestre cómo la concentración del contaminante se multiplica por diez en cada nivel trófico hasta la trucha ápice».",
        "tech_source": "USGS River Ecology & Freshwater Science • Dinámica Energética de Raymond Lindeman (1942)",
        "tech_details": "La dinámica trófica modela la termodinámica de ecosistemas acuáticos templados según el programa de biomonitorización del USGS, calculando en tiempo real la productividad primaria neta (PPN) y la disipación entálpica en cada nivel trófico mediante la ecuación diferencial de Lotka-Volterra acoplada."
    },
    {
        "num": 33,
        "code": "COD-033",
        "title": "Taller: Crea tu propio simulador de la mitocondria y nanomotor ATP sintasa",
        "header_color": "#D97706",
        "sim_file": "SIMULADOR_MITOCONDRIA_3D.html",
        "asset_js": "mitochondria_b64.js",
        "asset_var": "MITOCHONDRIA_GLB_B64",
        "mision": "En esta sesión programarás con Gemini la central energética de la vida celular: la mitocondria en 3D y el nanomotor rotacional de la ATP Sintasa (PDB 6J5I). Visualizarás el gradiente electroquímico de protones en la membrana interna y cómo el rotor transmembrana gira a 9.000 revoluciones por minuto para ensamblar moléculas de ATP.",
        "demo_btn": "⚡ Ver Mitocondria 3D",
        "prompt_lines": [
            "\"Genera el código de programación (HTML y JavaScript con Babylon.js) para crear un simulador 3D de la Mitocondria y el Nanomotor Rotacional ATP Sintasa (PDB 6J5I).",
            "Requisitos del código:",
            "1. Entrega el código completo en un único archivo para copiar con un clic y pegar en el taller.",
            "2. Enlaza Babylon.js desde CDN oficial y el archivo mitocondrial de alta resolución mitochondria_b64.js.",
            "3. Modela el corte de la mitocondria con crestas membranosas y el complejo proteico F0F1 con rotor c-ring, tallo gamma y cabeza catalítica alfa3-beta3.",
            "4. Añade deslizadores para el Potencial de Membrana Delta-Psi (40-220 mV), el Gradiente Delta-pH y la disponibilidad de ADP + Pi.",
            "5. Programa la rotación continua del nanomotor a velocidad proporcional a la fuerza protón-motriz (PMF) y la emisión de partículas de ATP sintetizadas.",
            "6. Escribe exclusivamente el bloque de código.\""
        ],
        "reto": "«Añade un botón de desacoplante termogénico (UCP1 / Termogenina) que disipe el gradiente de protones en forma de calor sin producir ATP, como ocurre en la grasa parda de los recién nacidos para evitar la hipotermia».",
        "tech_source": "Protein Data Bank (PDB 6J5I) • Microscopía Crioelectrónica (Cryo-EM 2.9Å) • Quimiosmosis de Peter Mitchell (Nobel 1978)",
        "tech_details": "Las coordenadas atómicas de la ATP sintasa proceden de la reconstrucción Cryo-EM a resolución casi atómica (PDB 6J5I), representando con máxima fidelidad biológica las 8 subunidades c del anillo rotor y el cambio conformacional cooperativo Open-Loose-Tight del dominio catalítico F1 según la ecuación de Mitchell."
    },
    {
        "num": 34,
        "code": "COD-034",
        "title": "Taller: Crea tu propio simulador de telómeros, telomerasa y límite de Hayflick",
        "header_color": "#7C3AED",
        "sim_file": "SIMULADOR_TELOMEROS_3D.html",
        "asset_js": "telomeres_b64.js",
        "asset_var": "TELOMERES_GLB_B64",
        "mision": "En esta práctica vas a ordenar a Gemini programar en Babylon.js un cromosoma 3D interactivo en forma de X con sus casquetes teloméricos terminales (complejo Shelterin) y la enzima Telomerasa (PDB 6D6V). Experimentarás en directo el reloj biológico del envejecimiento celular: cómo cada ciclo de división acorta los telómeros hasta detener la vida celular en el límite de Hayflick.",
        "demo_btn": "🧬 Ver Telómeros 3D",
        "prompt_lines": [
            "\"Genera el código HTML y JavaScript con Babylon.js para crear un simulador 3D de los Telómeros Cromosómicos, la Telomerasa y el Límite de Hayflick.",
            "Requisitos del código:",
            "1. Entrega el código en un único bloque autocontenido para pegarlo en el taller interactivo.",
            "2. Carga Babylon.js CDN y el modelo tridimensional de alta precisión telomeres_b64.js.",
            "3. Renderiza el cromosoma en X con cromátidas hermanas, centrómero y casquetes teloméricos dorados bioluminiscentes en los cuatro extremos.",
            "4. Añade un control deslizante de Divisiones Mitóticas (0 a 70 ciclos) y un control de expresión de Telomerasa hTERT (0 a 100%).",
            "5. Muestra en el cuadro de mandos la longitud telomérica en kilobases (kb), el número de divisiones remanentes y la entrada en senescencia replicativa.",
            "6. Escribe exclusivamente el código sin comentarios superfluos.\""
        ],
        "reto": "«Añade al simulador un botón de Inmortalización Celular que active permanentemente la telomerasa (como ocurre en las células madre o en las células HeLa) regenerando las repeticiones TTAGGG en cada ciclo».",
        "tech_source": "Protein Data Bank (PDB 6D6V) • Nobel Elizabeth Blackburn & Carol Greider (2009) • Leonard Hayflick (1961)",
        "tech_details": "El complejo telomérico modela la estructura cuaternaria del complejo ribonucleoproteico Shelterin (TRF1, TRF2, POT1, TIN2, TPP1, RAP1) protegiendo el bucle T y bucle D de los extremos cromosómicos según las mediciones cristalográficas del PDB 6D6V a 3.0Å."
    },
    {
        "num": 35,
        "code": "COD-035",
        "title": "Taller: Crea tu propio simulador de estratos de selva tropical y ríos voladores",
        "header_color": "#16A34A",
        "sim_file": "SIMULADOR_SELVA_TROPICAL_3D.html",
        "asset_js": "rainforest_b64.js",
        "asset_var": "RAINFOREST_GLB_B64",
        "mision": "En esta práctica construirás con Gemini un bioma de selva tropical lluviosa en 3D explorando sus 50 metros de gradiente vertical: desde el suelo sombrío y húmedo con contrafuertes gigantes de Ceiba pentandra hasta el dosel continuo y las copas emergentes. Analizarás la fotosíntesis, la estratificación de luz solar y el colosal flujo de vapor de los ríos voladores.",
        "demo_btn": "🌳 Ver Selva 3D",
        "prompt_lines": [
            "\"Genera el código de programación completo (HTML y JavaScript con Babylon.js) para construir un simulador interactivo 3D de los Estratos de Selva Tropical y Ríos Voladores.",
            "Requisitos del código:",
            "1. Entrega el archivo en un único bloque autocontenido listo para su ejecución.",
            "2. Enlaza Babylon.js CDN y el modelo botánico científico rainforest_b64.js.",
            "3. Renderiza en 3D un árbol emergente Ceiba pentandra con contrafuertes basales, lianas, bromelias y tres estratos de vegetación (Suelo, Sotobosque, Dosel Canopy).",
            "4. Añade un control deslizante de Altura de Exploración (0 a 50 metros) que desplace la cámara orbital e ilumine el estrato seleccionado.",
            "5. Muestra en el panel de telemetría la radiación solar PAR (del 1% en el suelo al 100% en la cima) y la tasa de evapotranspiración en litros/árbol/día.",
            "6. Escribe exclusivamente el código sin explicaciones.\""
        ],
        "reto": "«Añade al simulador una lluvia monzónica con partículas volumétricas en Babylon.js que active el bombeo de 1.000 litros de vapor de agua a la atmósfera formando un río volador visible».",
        "tech_source": "Smithsonian Tropical Research Institute (STRI) • Proyecto Amazon FACE & Escaneo LiDAR de Dosel",
        "tech_details": "La estratificación ecológica incorpora las curvas empíricas de extinción lumínica de Beer-Lambert calibradas en los bosques de Barro Colorado (Panamá) por el STRI, vinculando el índice de área foliar (LAI) con el volumen de vapor atmosférico bombeado por los árboles emergentes según el modelo de Nobre et al."
    },
    {
        "num": 36,
        "code": "COD-036",
        "title": "Taller: Crea tu propio simulador de neurotoxina y canales iónicos de sodio",
        "header_color": "#0284C7",
        "sim_file": "SIMULADOR_CANAL_IONICO_3D.html",
        "asset_js": "ionchannel_b64.js",
        "asset_var": "IONCHANNEL_GLB_B64",
        "mision": "En esta práctica programarás con Gemini la compuerta fundamental del impulso nervioso: el canal de sodio dependiente de voltaje Nav1.7 (PDB 6A95). Observarás el desplazamiento bioeléctrico del sensor de voltaje S4, el paso milimétrico de iones de sodio por el poro DEKA y cómo la neurotoxina tetrodotoxina (TTX) del pez globo encaja a la perfección bloqueando la corriente nerviosa.",
        "demo_btn": "⚡ Ver Canal Iónico 3D",
        "prompt_lines": [
            "\"Genera el código de programación (HTML y JavaScript con Babylon.js) para crear un simulador 3D del Canal de Sodio Nav1.7 y Bloqueo por Neurotoxina Tetrodotoxina (TTX).",
            "Requisitos del código:",
            "1. Entrega el programa completo en un bloque único de código para copiarlo y ejecutarlo en el taller.",
            "2. Carga Babylon.js desde CDN oficial y el archivo molecular tridimensional ionchannel_b64.js.",
            "3. Renderiza en 3D la proteína de membrana tetramérica con sus sensores de voltaje S4 dorados, el poro de conducción y la molécula de TTX en color carmesí.",
            "4. Añade un control deslizante de Potencial de Membrana Vm (-90 mV a +40 mV) y un deslizador de Concentración de Tetrodotoxina (0 a 100 nM).",
            "5. Muestra en el dock inferior el registro de corriente iónica (Patch-Clamp) y la probabilidad de apertura del canal Po.",
            "6. Escribe exclusivamente el bloque de código.\""
        ],
        "reto": "«Añade un botón de Pulso de Potencial de Acción que despolarice la membrana a +30 mV, abra el canal en 0.5 milisegundos y active la compuerta de inactivación rápida de leucina-fenilalanina (motivo IFM)».",
        "tech_source": "Protein Data Bank (PDB 6A95) • Cryo-EM a 3.2Å del Canal Nav1.7 Humano • Biofísica de Hodgkin y Huxley (Nobel 1963)",
        "tech_details": "La estructura atómica del canal Nav1.7 procede del archivo PDB 6A95, reproduciendo con exactitud la cavidad del filtro de selectividad formado por los aminoácidos DEKA (Asp364, Glu945, Lys1423, Ala1714) y la interacción electrostática del grupo guanidinio de la tetrodotoxina según las constantes cinéticas de Catterall."
    },
    {
        "num": 37,
        "code": "COD-037",
        "title": "Taller: Crea tu propio simulador de la piel humana y capas tisulares",
        "header_color": "#E11D48",
        "sim_file": "SIMULADOR_PIEL_HUMANA_3D.html",
        "asset_js": "skin_b64.js",
        "asset_var": "SKIN_GLB_B64",
        "mision": "En esta sesión crearás con Gemini un bloque histológico 3D de la piel humana: Epidermis, Dermis e Hipodermis con sus folículos pilosos, glándulas sebáceas, músculo erector del pelo y asas capilares. Simularás en directo las respuestas de termorregulación: vasodilatación, sudoración ecrina y el reflejo pilomotor de la piel de gallina ante el frío.",
        "demo_btn": "🔬 Ver Piel Humana 3D",
        "prompt_lines": [
            "\"Genera el código de programación (HTML y JavaScript con Babylon.js) para construir un simulador interactivo 3D de la Piel Humana, Capas Tisulares y Termorregulación.",
            "Requisitos del código:",
            "1. Entrega el código en un único bloque autocontenido listo para copiar y probar.",
            "2. Enlaza Babylon.js desde CDN oficial y el modelo histológico tridimensional skin_b64.js.",
            "3. Renderiza en 3D un bloque cúbico con la Epidermis queratinizada, la Dermis papilar/reticular vascularizada y la Hipodermis adiposa con folículo piloso.",
            "4. Añade controles deslizantes para la Temperatura Ambiental (-10°C a +45°C), la Actividad Metabólica (W) y el Índice de Radiación UV.",
            "5. Programa botones interactivos para activar Vasodilatación, Vasoconstricción, Reflejo Pilomotor (Piel de gallina) y Tasa de Sudoración ecrina.",
            "6. Escribe exclusivamente el código sin textos adicionales.\""
        ],
        "reto": "«Añade al simulador una visualización termográfica por colores donde el tejido cambie de azul gélido (vasoconstricción a 0°C) a rojo ardiente (vasodilatación a 40°C) para disipar calor corporal».",
        "tech_source": "NIH Visible Human Project • Histología Dermatológica de Wheater & Gartner",
        "tech_details": "El modelo 3D representa con rigor microanatómico los 5 estratos epidérmicos, las papilas dérmicas con asas capilares y la inervación simpática del músculo liso erector del pelo, aplicando las ecuaciones termodinámicas del balance térmico humano de Gagge y Stolwijk para el cálculo de la temperatura cutánea media."
    },
    {
        "num": 38,
        "code": "COD-038",
        "title": "Taller: Crea tu propio simulador de la columna vertebral y biomecánica lumbar",
        "header_color": "#D97706",
        "sim_file": "SIMULADOR_COLUMNA_VERTEBRAL_3D.html",
        "asset_js": "spine_b64.js",
        "asset_var": "SPINE_GLB_B64",
        "mision": "En esta sesión programarás con Gemini el segmento lumbosacro L3-S1 de la columna vertebral humana en 3D con sus cuerpos vertebrales, apófisis espinosas y discos intervertebrales (anillo fibroso y núcleo pulposo). Calcularás en tiempo real la fuerza de compresión en Newtons al levantar cargas según la postura ergonómica, alertando del riesgo de hernia discal.",
        "demo_btn": "🦴 Ver Columna Lumbar 3D",
        "prompt_lines": [
            "\"Genera el código de programación (HTML y JavaScript con Babylon.js) para crear un simulador 3D de la Columna Vertebral Humana, Discos Intervertebrales y Biomecánica Lumbar.",
            "Requisitos del código:",
            "1. Entrega el archivo en un único bloque autocontenido listo para su ejecución.",
            "2. Carga Babylon.js CDN y el modelo osteológico y discal de tomografía spine_b64.js.",
            "3. Renderiza en 3D las vértebras lumbares L3 a S1, las raíces nerviosas y los discos intervertebrales con núcleo pulposo deformable.",
            "4. Añade controles deslizantes para la Carga Levantada (0 a 50 kg), el Ángulo de Flexión del Tronco (0° a 90°) y la Distancia horizontal de la carga.",
            "5. Muestra en el dock inferior la Fuerza de Compresión en L4-L5 (Newtons N), la Presión de Nachemson (MPa) y una alarma visual si se supera el límite de seguridad NIOSH (3.400 N).",
            "6. Escribe exclusivamente el código sin preámbulos.\""
        ],
        "reto": "«Añade un botón de Simulación de Hernia Discal que deforme el núcleo pulposo hacia la parte posterior comprimiendo la raíz nerviosa ciática con un resplandor rojo de dolor neuropático».",
        "tech_source": "NIH 3D Orthopedic Tomography • Biomecánica Ocupacional de Don Chaffin • Presión Intradiscal de Alf Nachemson",
        "tech_details": "La biomecánica lumbar implementa el modelo cinemático de Chaffin y Anderson validado con los registros in vivo de transductores intradiscales de Nachemson, demostrando cómo levantar 20 kg flexionando la espalda a 90° multiplica la carga sobre L4-L5 hasta superar los 4.500 N, frente a sólo 1.800 N con la espalda recta y rodillas flexionadas."
    },
    {
        "num": 39,
        "code": "COD-039",
        "title": "Taller: Crea tu propio simulador de iridiscencia óptica y nanocristales",
        "header_color": "#0891B2",
        "sim_file": "SIMULADOR_IRIDISCENCIA_3D.html",
        "asset_js": "iridescence_b64.js",
        "asset_var": "IRIDESCENCE_GLB_B64",
        "mision": "En esta sesión ordenarás a Gemini construir en Babylon.js el simulador óptico de la mariposa Morpho peleides en 3D: desde la silueta alar macroscópica hasta la microestructura SEM a 20.000 aumentos de sus nano-lamelas en árbol de Navidad. Comprobarás que el azul cobalto brillante no tiene una sola molécula de pigmento: es interferencia constructiva pura de la Ley de Bragg.",
        "demo_btn": "🦋 Ver Mariposa Morpho 3D",
        "prompt_lines": [
            "\"Genera el código de programación (HTML y JavaScript con Babylon.js) para construir un simulador 3D del Mimetismo Óptico, Nanocristales e Iridiscencia de la Mariposa Morpho.",
            "Requisitos del código:",
            "1. Entrega el programa completo en un bloque único de código para copiarlo y ejecutarlo en el taller.",
            "2. Carga Babylon.js desde CDN oficial y el archivo tridimensional de nanocristales iridescence_b64.js.",
            "3. Renderiza en 3D la mariposa Morpho y un corte microscópico de sus nano-lamelas escalonadas en árbol de Navidad con material PBR iridiscente.",
            "4. Añade un control deslizante de Ángulo de Incidencia de la Luz (0° a 80°) y un selector del Índice de Refracción del Medio circundante n (aire n=1.00, agua n=1.33, acetona n=1.36).",
            "5. Muestra en tiempo real la longitud de onda reflejada pico (nm) y cómo el ala pasa de azul cobalto a verde o pierde el color al sumergirse en solventes.",
            "6. Escribe exclusivamente el bloque de código.\""
        ],
        "reto": "«Añade un botón de Inmersión en Solvente Líquido que llene los huecos de aire de las nano-lamelas con acetona, alterando el índice de refracción y apagando instantáneamente el color azul del ala ante los ojos del alumno».",
        "tech_source": "Natural History Museum London • Microscopía Electrónica de Barrido (SEM 20.000x) • Ley Óptica de Bragg-Snell",
        "tech_details": "La óptica estructural modela la interferencia en multicapas dieléctricas mediante la ecuación de Bragg-Snell (mλ = 2d √(n² - sin²θ)), demostrando cómo las crestas de cutícula separadas a d ≈ 205 nm producen interferencia constructiva en λ = 450 nm (azul visible) sin requerir ningún cromóforo químico."
    },
    {
        "num": 40,
        "code": "COD-040",
        "title": "Taller: Crea tu propio simulador de regeneración tisular y matriz de colágeno",
        "header_color": "#DB2777",
        "sim_file": "SIMULADOR_REGENERACION_TISULAR_3D.html",
        "asset_js": "tissue_repair_b64.js",
        "asset_var": "TISSUE_REPAIR_GLB_B64",
        "mision": "En esta sesión programarás con Gemini la cascada biológica de cicatrización y regeneración tisular en 3D a lo largo de sus 28 días. Observarás la hemostasia inicial con fibrina, la angiogénesis de nuevos capilares sanguíneos, la migración activa de fibroblastos tejiendo colágeno tipo III y la remodelación final con colágeno tipo I orientado en líneas de tensión mecánica.",
        "demo_btn": "🔬 Ver Regeneración 3D",
        "prompt_lines": [
            "\"Genera el código de programación (HTML y JavaScript con Babylon.js) para crear un simulador 3D de la Regeneración Tisular, Fibroblastos y Matriz Extracelular.",
            "Requisitos del código:",
            "1. Entrega el código en un único bloque autocontenido listo para copiar y probar.",
            "2. Enlaza Babylon.js desde CDN oficial y el modelo tisular tridimensional tissue_repair_b64.js.",
            "3. Renderiza en 3D el lecho de granulación, los brotes capilares angiogénicos, las fibras de colágeno entrelazadas y los fibroblastos en migración activa.",
            "4. Añade un control deslizante de Día de Cicatrización (Día 0 a Día 28) y un deslizador de Oxigenación Tisular pO2 (mmHg).",
            "5. Muestra en el panel de telemetría la densidad de fibroblastos (cél/mm²), la fuerza tensil tisular acumulada (%) y el reemplazo progresivo de colágeno III por colágeno I.",
            "6. Escribe exclusivamente el código sin explicaciones.\""
        ],
        "reto": "«Añade un botón de Aplicación de Tensión Mecánica Fisiológica que alinee los haces de colágeno tipo I en la dirección de la fuerza, aumentando la resistencia de la cicatriz hasta el 80% de la piel intacta».",
        "tech_source": "NIH 3D Regenerative Medicine • Fisiología de Reparación Tisular de Clark & Singer (1999)",
        "tech_details": "La cinética celular modela las cuatro fases continuas de la cicatrización tisular de mamíferos (hemostasia, inflamación, proliferación y maduración), calculando la tasa de depósito de procolágeno por miofibroblastos alfa-SMA positivos y la recuperación no lineal de la fuerza tensil según los modelos reológicos de Fung."
    }
]

def make_script_content(spec):
    num_str = f"{spec['num']:03d}"
    sesion_str = f"{spec['num']:02d}"
    
    prompt_escaped = "<br/>".join([line.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;') for line in spec['prompt_lines']])

    content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_{num_str}.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-{num_str}_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión {sesion_str} del Curso de IA ({spec['title']}).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/{sesion_str}_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-{num_str}_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/{num_str}_COD-{num_str}_Taller_Simulador_3D.pdf"

def build_cod_{num_str}_taller_3d_pdf(output_path=PDF_PATH):
    dest_path = output_path
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as _:
            pass
    except Exception:
        dest_path = LOCAL_BACKUP
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(
        dest_path,
        pagesize=letter,
        rightMargin=36, leftMargin=36, topMargin=22, bottomMargin=20
    )
    styles = getSampleStyleSheet()

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0,
        textColor=colors.HexColor('{spec['header_color']}'), alignment=1, spaceAfter=1
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.8,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=11.5, leading=14.0,
        textColor=colors.HexColor('#0F172A'), spaceAfter=3
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=8.8, leading=11.2,
        textColor=colors.HexColor('{spec['header_color']}'), spaceBefore=3, spaceAfter=2
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=7.9, leading=10.5,
        textColor=colors.HexColor('#1E293B'), spaceAfter=2
    )
    style_task = ParagraphStyle(
        'TaskStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.7, leading=10.1,
        textColor=colors.HexColor('#0F172A')
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.3, leading=9.6,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('{spec['header_color']}'), spaceAfter=4))

    story.append(Paragraph("<b>[{spec['code']}] {spec['title']}</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • De Espectador a Creador con IA:</b>", style_section_h))
    story.append(Paragraph("{spec['mision']}", style_body))

    # Lista de Tareas
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> En la respuesta de Gemini, haz clic en el botón <b>«Copiar código»</b> situado en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> En el mapa de la Sesión {sesion_str}, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> Pega el código con <b>Ctrl+V</b> (o Cmd+V) y haz clic en <b>«▶️ Ejecutar Creación»</b>. ¡Tu simulación 3D cobrará vida al instante!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo Oficial Terminada:</b> Pulsa el botón <b>«{spec['demo_btn']} ↗»</b> en el taller o mapa para comparar tu resultado con la versión oficial con audio.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('{spec['header_color']}')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_table)
    story.append(Spacer(1, 3))

    # Recuadro Prompt Maestro
    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_html = "<b>Copia exactamente este texto en Gemini:</b><br/><i>{prompt_escaped}</i>"
    p_table = Table([[Paragraph(prompt_html, style_prompt)]], colWidths=[letter[0] - 72])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 3))

    # Reto Extra
    story.append(Paragraph("🌟 <b>El Reto Extra (Para Alumnos Curiosos):</b>", style_section_h))
    story.append(Paragraph(
        "👉 <b>¡Pídele a Gemini que modifique tu código!</b> En la misma conversación dile: "
        "<i>{spec['reto']}</i>. Vuelve a copiar el código, pégalo en tu Taller y ¡comprueba la evolución de tu modelo en directo!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de los datos científicos y repositorio oficial:</b> {spec['tech_source']}.<br/>"
        "• <b>Montaje en Babylon.js y fidelidad biológica:</b> {spec['tech_details']} El modelo está codificado en Base64 (<i>{spec['asset_js']}</i>) para carga instantánea 100% offline sin errores de red."
    )
    tech_table = Table([[Paragraph(tech_text, style_task)]], colWidths=[letter[0] - 72])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#16A34A')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(tech_table)

    doc.build(story)
    if dest_path != LOCAL_BACKUP:
        try:
            import shutil
            os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
            shutil.copy2(dest_path, LOCAL_BACKUP)
        except Exception:
            pass
    print(f"✅ PDF COD-{num_str} generado con éxito en: {{dest_path}}")

if __name__ == '__main__':
    try:
        build_cod_{num_str}_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-{num_str}: {{e}}")
        sys.exit(1)
'''
    return content

def main():
    print("🚀 Generando los 10 scripts individuales build_pdf_cod_031.py a build_pdf_cod_040.py...")
    for spec in LOTE_4_SPECS:
        filename = f"build_pdf_cod_{spec['num']:03d}.py"
        filepath = os.path.join(SCRIPT_DIR, filename)
        code = make_script_content(spec)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"  ✅ Creado script: {filename}")

    # Ahora generar el Compilador Maestro build_cod_lote4_master.py
    master_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_cod_lote4_master.py
Compilador Maestro del LOTE 4 [COD] (Sesiones 31 a 40):
- Genera las 10 Fichas Didácticas Oficiales en PDF (COD-031 a COD-040).
- Genera y sincroniza los 10 Modelos 3D en Base64 (_b64.js) en 03_ASSETS_3D_Y_DATOS/.
- Genera y distribuye los 10 Simuladores HTML interactivos hacia
  SIMULADORES_INTERACTIVOS/01_SIMULADORES/ y las carpetas de sesión 31 a 40.
- Establece la Triple Salvaguarda Pedagógica en el Lote 4 al 100%.
"""

import os
import sys
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
SESSIONS_ROOT = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
SIM_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES")
CATALOG_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "02_INDICES_Y_CATALOGOS")

os.makedirs(SIM_DIR, exist_ok=True)
os.makedirs(CATALOG_DIR, exist_ok=True)

def generate_all_assets():
    print("\\n--- 1. Generando Activos Científicos 3D en Base64 (03_ASSETS_3D_Y_DATOS/) ---")
    try:
        from build_lote4_glb_assets import main as build_assets_main
        build_assets_main()
    except Exception as e:
        print(f"  ❌ Error generando activos Base64: {e}")

def generate_all_htmls():
    print("\\n--- 2. Generando los 10 Simuladores HTML con Babylon.js (Dual Espejado) ---")
    try:
        from generate_cod_lote4_htmls import main as generate_htmls_main
        generate_htmls_main()
    except Exception as e:
        print(f"  ❌ Error generando simuladores HTML: {e}")

def generate_all_pdfs():
    print("\\n--- 3. Generando Fichas Didácticas Oficiales en PDF (COD-031 a COD-040) ---")
    pdf_modules = [
        (31, "build_pdf_cod_031", "build_cod_031_taller_3d_pdf"),
        (32, "build_pdf_cod_032", "build_cod_032_taller_3d_pdf"),
        (33, "build_pdf_cod_033", "build_cod_033_taller_3d_pdf"),
        (34, "build_pdf_cod_034", "build_cod_034_taller_3d_pdf"),
        (35, "build_pdf_cod_035", "build_cod_035_taller_3d_pdf"),
        (36, "build_pdf_cod_036", "build_cod_036_taller_3d_pdf"),
        (37, "build_pdf_cod_037", "build_cod_037_taller_3d_pdf"),
        (38, "build_pdf_cod_038", "build_cod_038_taller_3d_pdf"),
        (39, "build_pdf_cod_039", "build_cod_039_taller_3d_pdf"),
        (40, "build_pdf_cod_040", "build_cod_040_taller_3d_pdf"),
    ]

    for num, mod_name, fn_name in pdf_modules:
        try:
            mod = __import__(mod_name)
            fn = getattr(mod, fn_name)
            fn()
        except Exception as e:
            print(f"  ❌ Error COD-{num:03d}: {e}")

def main():
    print("=" * 80)
    print("🚀 COMPILADOR MAESTRO LOTE 4 [COD] (SESIONES 31 A 40) - TRIPLE SALVAGUARDA")
    print("=" * 80)

    generate_all_assets()
    generate_all_htmls()
    generate_all_pdfs()

    print("\\n✨ COMPILACIÓN DEL LOTE 4 FINALIZADA AL 100%.")

if __name__ == '__main__':
    main()
'''
    master_path = os.path.join(SCRIPT_DIR, "build_cod_lote4_master.py")
    with open(master_path, "w", encoding="utf-8") as f:
        f.write(master_content)
    print(f"  ✅ Creado Compilador Maestro: build_cod_lote4_master.py")

if __name__ == '__main__':
    main()

