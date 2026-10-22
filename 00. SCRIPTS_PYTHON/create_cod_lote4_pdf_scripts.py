#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
create_cod_lote4_pdf_scripts.py
Crea los 10 scripts generadores de PDF didácticos oficiales ReportLab (Letter 1 Página):
- build_pdf_cod_031.py a build_pdf_cod_040.py
y el orquestador maestro build_cod_lote4_master.py
con sincronización biunívoca 100% estricta entre el simulador y el Prompt de Gemini.
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

PDF_SPECS = [
    {
        "num": 31,
        "code": "COD-031",
        "title": "Taller: Crea tu propio simulador 3D de Arrecife de Coral, Pólipos y Simbiosis Marina",
        "backup_name": "31_COD-031_Taller_Simulador_Arrecife_Coral_3D.pdf",
        "header_color": "#0284C7",
        "mission": "En este taller ordenarás a Gemini construir un laboratorio marino tridimensional de un <b>arrecife de coral</b> (*Acropora* y coral cerebro). Modelarás el esqueleto pétreo de <b>aragonito (CaCO₃)</b>, pólipos cilíndricos con tentáculos y la simbiosis vital con microalgas <b>zooxantelas (*Symbiodiniaceae*)</b>. Simularás el estrés térmico oceánico mediante <b>Grados Días de Calentamiento (DHW)</b> de la NOAA y el fenómeno de <b>blanqueamiento coralino masivo</b> al superar 30.5°C. <b>No requieres saber programar:</b> copia el prompt y ejecútalo.",
        "button_action": "🪸 Abrir Arrecife de Coral 3D ↗",
        "html_file": "SIMULADOR_ARRECIFE_CORAL_3D.html",
        "prompt": """\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D de Arrecife de Coral, Pólipos y Simbiosis Marina (NOAA Coral Reef Watch).
Requisitos del código:
1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.
2. Modela en 3D un arrecife con esqueleto de carbonato de calcio (aragonito CaCO₃), colonias de pólipos tubulares interactivos y corona de tentáculos móviles con nematocistos urticantes para captura de zooplancton.
3. Incorpora microalgas zooxantelas endosimbiontes intracelulares fotosintéticas (Symbiodiniaceae) aportando pigmentación y energía al tejido del pólipo.
4. Añade controles deslizantes para Temperatura del Agua (24°C a 33°C), Grados Días de Calentamiento NOAA (DHW 0 a 16 °C-semanas), Acidificación Oceánica (pH 7.6 a 8.3) y Radiación Solar UV.
5. Simula el blanqueamiento coralino progresivo: al superar 30.5°C o acumular DHW ≥ 4, las zooxantelas dañadas son expulsadas, dejando el tejido translúcido y revelando el esqueleto blanco de CaCO₃.
6. Integra botones de Ciclo Día/Noche (con extensión nocturna de tentáculos), Disparo de Ola Marina Calórica extrema, Restauración simbiótica y telemetría NOAA en tiempo real con audio submarino y voz didáctica.
7. Aplica diseño en modo oscuro (#010712) accesible para seniors, con tipografía grande (16-18px) y sin texto explicativo fuera del código.\""""",
        "extra_challenge": "👉 <b>¡Pídele a Gemini que modifique tu código!</b> Dile: <i>«Añade una colonia de peces payaso interactuando en comensalismo con anémonas de mar e incorpora una alerta sonora cuando la calcificación caiga a cero por acidificación»</i>.",
        "scientific_source": "• <b>NOAA Coral Reef Watch (CRW) & Dinámica de Cnidarios:</b> Umbrales de blanqueamiento basados en Grados Días de Calentamiento (DHW). Un DHW ≥ 4 provoca estrés térmico y blanqueamiento; un DHW ≥ 8 induce mortalidad masiva por pérdida simbiótica de zooxantelas.<br/>• <b>Química del Carbonato de Calcio:</b> Precipitación de aragonito por calcificación biogénica dependiente del estado de saturación del ión carbonato (Ω_arag) y pH oceánico."
    },
    {
        "num": 32,
        "code": "COD-032",
        "title": "Taller: Crea tu propio simulador 3D de la Pirámide Trófica y Red Fluvial",
        "backup_name": "32_COD-032_Taller_Simulador_Red_Trofica_Fluvial_3D.pdf",
        "header_color": "#059669",
        "mission": "En este taller ordenarás a Gemini crear una pirámide trófica tridimensional interactiva y red ecológica fluvial. Visualizarás la <b>Ley del 10% de Raymond Lindeman</b>: solo una décima parte de la energía química almacenada en un nivel trófico se transfiere al siguiente. Explorarás desde productores primarios (diatomeas) hasta el depredador ápice (nutria fluvial), y simularás el colapso por <b>eutrofización</b> y <b>biomagnificación de metales</b>. <b>No requieres programar:</b> copia el prompt y disfruta de la simulación.",
        "button_action": "🏞️ Abrir Pirámide Trófica 3D ↗",
        "html_file": "SIMULADOR_RED_TROFICA_3D.html",
        "prompt": """\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D de la Pirámide Trófica y Red Ecológica Fluvial (Ley del 10% de Lindeman y USGS).
Requisitos del código:
1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.
2. Modela en 3D los 4 niveles tróficos en paralelepípedos elométricos superpuestos: Nivel 1 Productores Primarios (diatomeas/macrófitas 20.000 kcal), Nivel 2 Consumidores 1° (invertebrados 2.000 kcal), Nivel 3 Consumidores 2° (truchas 200 kcal) y Nivel 4 Depredador Ápice (nutria fluvial 20 kcal).
3. Añade partículas tridimensionales que muestren el flujo ascendente de energía y cómo el 90% se disipa como calor metabólico y entropía.
4. Incluye controles deslizantes para Radiación Solar Fotosintética (kcal/m²), Eficiencia de Transferencia Trófica (5% a 20%) y Concentración de Nutrientes Nitrógeno/Fósforo (mg/L).
5. Incorpora botones de impacto antrópico: Eutrofización (anoxia fluvial por colapso de oxígeno disuelto < 3 mg/L), Sobrepesca de carnívoros, Biomagnificación de contaminantes (mercurio acumulativo) y Restauración.
6. Panel de telemetría en tiempo real con Oxígeno Disuelto (DO), biomasa energética por nivel, audio de corriente de río y síntesis de voz en español.
7. Aplica diseño en modo oscuro (#020914) accesible, tipografía grande (16-18px) y sin texto explicativo fuera del código.\""""",
        "extra_challenge": "👉 <b>¡Pídele a Gemini que modifique tu código!</b> Dile: <i>«Añade un nivel descomponedor bentónico con bacterias y hongos saprófagos que reciclen la materia orgánica muerta devolviéndola al sedimento»</i>.",
        "scientific_source": "• <b>Dinámica Trófica de Raymond Lindeman (1942):</b> Eficiencia ecológica de transferencia neta estimada en un promedio de 10% (rango empírico 5%-20%) debido a respiración celular, excreción y pérdidas de calor metabólico.<br/>• <b>Ecología Fluvial del USGS:</b> Relación estequiométrica entre nitratos, proliferación algal de Cladophora y déficit de oxígeno disuelto (curva de caída de oxígeno de Streeter-Phelps)."
    },
    {
        "num": 33,
        "code": "COD-033",
        "title": "Taller: Crea tu propio simulador 3D de la Mitocondria y Nanomotor ATP Sintasa",
        "backup_name": "33_COD-033_Taller_Simulador_Mitocondria_ATP_3D.pdf",
        "header_color": "#7C3AED",
        "mission": "En este taller ordenarás a Gemini crear un simulador 3D del orgánulo bioenergético celular: la <b>Mitocondria</b> y el nanomotor rotacional <b>ATP Sintasa (Complejo V)</b>. Basado en la <b>Teoría Quimiosmótica de Peter Mitchell (Nobel 1978)</b>, observarás cómo el gradiente de protones H⁺ a través de las crestas mitocondriales impulsa la rotación física del rotor F₀ a <b>9.000 revoluciones por minuto</b>, sintetizando ATP a partir de ADP y fosfato. <b>No requieres saber programar:</b> copia el prompt y ejecútalo.",
        "button_action": "⚡ Abrir Nanomotor ATP Sintasa 3D ↗",
        "html_file": "SIMULADOR_MITOCONDRIA_3D.html",
        "prompt": """\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D de la Mitocondria y el Nanomotor Molecular ATP Sintasa (NIH 3D y PDB 6J5I).
Requisitos del código:
1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.
2. Modela en 3D el nanomotor ATP Sintasa incrustado en la bicapa lipídica de la cresta mitocondrial: rotor F₀ transmembrana (anillo subunidad c de 10 lóbulos), tallo central asimétrico γ-ε, estator periférico b₂-OSCP y cabeza catalítica F₁ con hexámero α₃β₃ en la matriz.
3. Anima la rotación física del rotor F₀ impulsada por el flujo de protones H⁺ desde el espacio intermembrana hacia la matriz, produciendo 3 moléculas de ATP por cada vuelta de 360 grados.
4. Añade controles deslizantes para Potencial de Membrana Mitocondrial ΔΨm (-60 mV a -220 mV) y Disponibilidad de ADP + Pi (10% a 100%).
5. Integra inhibidores farmacológicos reales: Oligomicina (bloquea físicamente el canal F₀ deteniendo el motor) y Desacoplador DNP (2,4-dinitrofenol, disipa el gradiente de protones generando calor sin producir ATP).
6. Telemetría con velocidad rotacional del rotor en RPM (hasta 9.000 RPM), tasa de síntesis de ATP en moléculas/s, zumbido acústico sintetizado con Web Audio y voz explicativa.
7. Aplica diseño en modo oscuro (#0a0414) de alto contraste, tipografía grande (16-18px) y sin texto explicativo fuera del código.\""""",
        "extra_challenge": "👉 <b>¡Pídele a Gemini que modifique tu código!</b> Dile: <i>«Añade los 3 estados conformacionales de Boyer (Abierto, Suelto y Tenso/Tight) cambiando dinámicamente el color de cada subunidad beta en la cabeza catalítica F1»</i>.",
        "scientific_source": "• <b>Teoría Quimiosmótica de Peter Mitchell & Mecanismo Rotacional de Boyer (Nobel 1997):</b> La fuerza protón-motriz (Δp = ΔΨ - 60ΔpH) genera torque mecánico en el anillo c que induce cambios conformacionales secuenciales en el sitio activo de la subunidad β.<br/>• <b>Estructura Criogénica PDB 6J5I:</b> Resolución a 2.9Å de la ATP sintasa humana demostrando acoplamiento elastomecánico entre el rotor F₀ y la subunidad central γ."
    },
    {
        "num": 34,
        "code": "COD-034",
        "title": "Taller: Crea tu propio simulador 3D de Telómeros Cromosómicos y Límite de Hayflick",
        "backup_name": "34_COD-034_Taller_Simulador_Telomeros_Hayflick_3D.pdf",
        "header_color": "#0284C7",
        "mission": "En este taller ordenarás a Gemini construir un simulador tridimensional del reloj biológico del envejecimiento celular: los <b>Telómeros Cromosómicos</b> y el <b>Límite de Leonard Hayflick</b>. Basado en las investigaciones de <b>Elizabeth Blackburn y Carol Greider (Nobel 2009)</b>, modelarás un cromosoma metafásico con sus casquetes de ADN repetitivo <b>TTAGGG</b> acortándose en cada mitosis, y explorarás la activación de la enzima <b>Telomerasa</b>. <b>No requieres programar:</b> copia el prompt y ejecútalo.",
        "button_action": "🧬 Abrir Telómeros y Límite de Hayflick 3D ↗",
        "html_file": "SIMULADOR_TELOMEROS_3D.html",
        "prompt": """\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D de Telómeros Cromosómicos, Telomerasa y Límite de Hayflick (Nobel de Medicina 2009 y PDB 6D6V).
Requisitos del código:
1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.
2. Modela en 3D un cromosoma metafásico humano con cromátidas hermanas, centrómero primario y 4 casquetes teloméricos fluorescentes en los extremos de los brazos p y q.
3. Representa los telómeros como bucles protectores T-loop formados por repeticiones hexaméricas 5'-TTAGGG-3' protegidas por el complejo proteico Shelterin.
4. Añade control deslizante de Divisiones Celulares Acumuladas (0 a 65 divisiones) y Estrés Oxidativo por radicales libres (ROS). Con cada división, el telómero se acorta visiblemente perdiendo kilobases (kb).
5. Incorpora interruptor de la enzima Telomerasa (hTERT + molde de ARN hTR) que elonga los telómeros evitando el envejecimiento en células madre o líneas cancerosas inmortales.
6. Simula el Límite de Hayflick: al caer por debajo de 3.5 kb, se activa la respuesta de daño en el ADN (vía p53/p21) induciendo senescencia celular irreversible.
7. Telemetría genómica con longitud en kilobases, conteo de hexámeros TTAGGG, audio interactivo de pulso y síntesis de voz en español en modo oscuro (#030a14) accesible (+65).
8. Entrega exclusivamente el código sin texto explicativo.\""""",
        "extra_challenge": "👉 <b>¡Pídele a Gemini que modifique tu código!</b> Dile: <i>«Añade focos nucleares fluorescentes de daño al ADN (gamma-H2AX) que brillen en rojo sobre el cromosoma cuando los telómeros colapsen»</i>.",
        "scientific_source": "• <b>Genética Molecular de Telómeros (Blackburn, Greider & Szostak 2009):</b> Los telómeros evitan que la maquinaria de reparación reconozca los extremos cromosómicos como roturas de doble cadena de ADN (DSB).<br/>• <b>Límite de Hayflick (1961):</b> Las células somáticas humanas normales tienen una capacidad replicativa finita (~50-60 duplicaciones) dictada por la incapacidad de la ADN polimerasa para replicar el extremo terminal 3' (problema de la replicación del extremo)."
    },
    {
        "num": 35,
        "code": "COD-035",
        "title": "Taller: Crea tu propio simulador 3D del Bioma de Selva Tropical y Estratos de Altura",
        "backup_name": "35_COD-035_Taller_Simulador_Selva_Tropical_3D.pdf",
        "header_color": "#059669",
        "mission": "En este taller ordenarás a Gemini crear un perfil bioclimático tridimensional de la <b>Selva Tropical Neotropical</b> a lo largo de <b>50 metros de altura vertical</b>. Basado en los estudios del <b>Smithsonian Tropical Research Institute (STRI)</b>, ascenderás desde el suelo forestal en penumbra (1% de luz y 98% de humedad) hasta el dosel continuo (*Canopy*) y la cúpula emergente de la Ceiba. Conocerás el fenómeno de los <b>Ríos Voladores</b> de la Amazonía. <b>No requieres programar:</b> copia el prompt y ejecútalo.",
        "button_action": "🌴 Abrir Bioma de Selva Tropical 3D ↗",
        "html_file": "SIMULADOR_SELVA_TROPICAL_3D.html",
        "prompt": """\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D del Bioma de Selva Tropical y Estratos de Altura (Smithsonian Tropical Research Institute - STRI).
Requisitos del código:
1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.
2. Modela en 3D una sección vertical botánica de 50 metros dividida en 4 estratos con vegetación fidedigna: Suelo Forestal (0-5m con raíces tabulares y hongos), Sotobosque/Understory (5-20m con palmas y lianas), Dosel Continuo/Canopy (20-40m con epífitas y orquídeas donde vive el 80% de especies) y Estrato Emergente (40-50m con copa de Ceiba pentandra expuesta al viento).
3. Añade un control deslizante de Altímetro (0 a 50m) que mueva un elevador de telemetría e inspeccione los microclimas in-situ: Radiación PAR (1% a 100%), Humedad Relativa (60% a 98%), Temperatura y Viento.
4. Incorpora botones de Lluvia Monzónica tropical y Ríos Voladores (simulación de evapotranspiración con 1.000 L de vapor de agua diarios por árbol maduro formando nubes orográficas).
5. Botones de salto rápido al Dosel y al Suelo forestal con sonidos de bioacústica de selva tropical mediante Web Audio y voz en español.
6. Aplica diseño en modo oscuro (#010d06) con contrastes verdes esmeralda, tipografía grande (16-18px) y sin texto explicativo fuera del código.\""""",
        "extra_challenge": "👉 <b>¡Pídele a Gemini que modifique tu código!</b> Dile: <i>«Añade microestanques de agua en bromelias epífitas (fitotelmata) que alberguen renacuajos de ranas dardo venenosas en el dosel»</i>.",
        "scientific_source": "• <b>Estructura Forestal Neotropical (Smithsonian Tropical Research Institute):</b> La estratificación vertical atenúa exponencialmente la radiación fotosintéticamente activa (Ley de Beer-Lambert) creando nichos bioclimáticos estables.<br/>• <b>Meteorología Amazónica & Ríos Voladores:</b> La selva amazónica transpira diariamente a la atmósfera más de 20.000 millones de toneladas de vapor de agua, superando el caudal del propio río Amazonas hacia el océano."
    },
    {
        "num": 36,
        "code": "COD-036",
        "title": "Taller: Crea tu propio simulador 3D de Neurotoxinas y Bloqueo de Canales Iónicos",
        "backup_name": "36_COD-036_Taller_Simulador_Canales_Ionicos_TTX_3D.pdf",
        "header_color": "#7C3AED",
        "mission": "En este taller ordenarás a Gemini crear un simulador 3D del impulso nervioso y neurotoxicología molecular basado en el <b>Canal de Sodio Dependiente de Voltaje (Nav1.7)</b> y la <b>Tetrodotoxina (TTX)</b> del pez globo. Descubrirás cómo el sensor de voltaje S4 y el poro <b>DEKA</b> coordinan la entrada de iones Na⁺ para disparar el potencial de acción celular (Hodgkin-Huxley), y cómo una sola molécula de toxina puede paralizar el sistema nervioso. <b>No requieres programar:</b> copia el prompt y ejecútalo.",
        "button_action": "⚡ Abrir Canal de Sodio y Neurotoxina 3D ↗",
        "html_file": "SIMULADOR_CANAL_IONICO_3D.html",
        "prompt": """\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D de Neurotoxinas y Bloqueo de Canales Iónicos de Sodio (PDB 6A95 y Neurofisiología de Hodgkin-Huxley).
Requisitos del código:
1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.
2. Modela en 3D un canal de sodio dependiente de voltaje Nav incrustado en la bicapa lipídica neuronal: 4 dominios homólogos (I-IV), sensor de voltaje S4 con residuos de arginina con carga positiva y filtro exterior de selectividad iónica DEKA (Asp, Glu, Lys, Ala).
3. Simula la compuerta de voltaje: a potencial de reposo (-70 mV) el poro está cerrado; al despolarizarse (> -50 mV), los sensores S4 se desplazan abriendo el poro y permitiendo el flujo de iones Na⁺ al interior axonal.
4. Integra la neurotoxina Tetrodotoxina (TTX del pez globo): se acopla como un tapón rígido exterior bloqueando el paso de sodio y aboliendo la despolarización neuronal (parálisis respiratoria flácida).
5. Incluye fármaco anestésico local (Lidocaína) que bloquea el canal desde el lado intracelular y botón de lavado fisiológico.
6. Osciloscopio con potencial de membrana (mV), conductancia de sodio gNa, corriente iónica, audio de pico de potencial de acción y síntesis de voz en español.
7. Aplica diseño en modo oscuro (#06020e) accesible para mayores, tipografía grande (16-18px) y sin texto fuera del bloque de código.\""""",
        "extra_challenge": "👉 <b>¡Pídele a Gemini que modifique tu código!</b> Dile: <i>«Añade la toxina Batracotoxina de la rana Phyllobates terribilis, que impide el cierre del canal provocando despolarización masiva y convulsiones letales»</i>.",
        "scientific_source": "• <b>Neurofisiología de Hodgkin-Huxley:</b> Modelo biofísico de conductancia dependiente de voltaje y tiempo que describe la fase rápida ascendente del potencial de acción axonal mediante el flujo pasivo de sodio.<br/>• <b>Criomicroscopía Electrónica PDB 6A95:</b> Estructura de Nav1.7 a 3.2Å revelando el bolsillo de unión de alta afinidad del grupo guanidinio de la tetrodotoxina con los carboxilatos del anillo DEKA."
    },
    {
        "num": 37,
        "code": "COD-037",
        "title": "Taller: Crea tu propio simulador 3D de la Piel Humana y Termorregulación",
        "backup_name": "37_COD-037_Taller_Simulador_Piel_Humana_3D.pdf",
        "header_color": "#E11D48",
        "mission": "En este taller ordenarás a Gemini construir un bloque histológico tridimensional de la <b>Piel Humana</b> y sus mecanismos de <b>Termorregulación</b>. Basado en el <b>NIH Visible Human Project</b>, explorarás el corte transversal tri-estratificado: <b>Epidermis</b>, <b>Dermis</b> e <b>Hipodermis</b>. Verás cómo responden los capilares sanguíneos (vasodilatación vs vasoconstricción), los folículos pilosos (reflejo de 'piel de gallina') y las glándulas sudoríparas ante frío polar o calor extremo. <b>No requieres programar:</b> copia el prompt y ejecútalo.",
        "button_action": "🩺 Abrir Piel Humana y Termorregulación 3D ↗",
        "html_file": "SIMULADOR_PIEL_HUMANA_3D.html",
        "prompt": """\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D de la Piel Humana, Capas Tisulares y Termorregulación (NIH Visible Human Project e Histología Médica).
Requisitos del código:
1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.
2. Modela en 3D un bloque tisular cutáneo con sus 3 capas anatómicas: Epidermis superficial queratinizada con melanocitos, Dermis vascular densa con colágeno, folículo piloso, músculo erector del pelo y glándula sudorípara ecrina túbulo-glomerular, e Hipodermis con adipocitos de reserva.
3. Añade control deslizante de Temperatura Ambiental (0°C a 45°C) e Índice Ultravioleta (UVI 0 a 11).
4. Simula respuestas homeostáticas dinámicas: en frío (<15°C) vasoconstricción capilar y erección pilomotora ('piel de gallina'); en calor (>30°C) vasodilatación dérmica masiva aumentando el flujo sanguíneo cutáneo y secreción de gotas de sudor con evaporación latente.
5. Pigmentación adaptativa de la epidermis según radiación UV por síntesis melánica.
6. Telemetría de flujo sanguíneo dérmico (mL/100g/min), tasa de sudoración (L/hora), tono del músculo erector, audio interactivo y síntesis de voz en español.
7. Aplica diseño en modo oscuro (#100604) accesible (+65), tipografía grande (16-18px) y sin texto explicativo fuera del código.\""""",
        "extra_challenge": "👉 <b>¡Pídele a Gemini que modifique tu código!</b> Dile: <i>«Añade corpúsculos sensoriales de Meissner para tacto fino y de Pacini para vibración profunda que respondan cuando pulses sobre el bloque dérmico»</i>.",
        "scientific_source": "• <b>Fisiología Termorreguladora Médica:</b> El centro preóptico hipotalámico coordina la pérdida de calor evaporativo (0.58 kcal por gramo de sudor) y la modulación del tono vasomotor cutáneo (flujo de 1 mL/min a 150 mL/min).<br/>• <b>Arquitectura Tisular del NIH Visible Human:</b> Organización estratificada que proporciona barrera mecánica impermeable gracias al estrato córneo y amortiguación térmica mediante el panículo adiposo hipodérmico."
    },
    {
        "num": 38,
        "code": "COD-038",
        "title": "Taller: Crea tu propio simulador 3D de la Columna Vertebral y Biomecánica Lumbar",
        "backup_name": "38_COD-038_Taller_Simulador_Columna_Vertebral_3D.pdf",
        "header_color": "#0284C7",
        "mission": "En este taller ordenarás a Gemini construir un simulador biomecánico 3D del segmento lumbosacro de la <b>Columna Vertebral (L3 a S1)</b> y sus <b>Discos Intervertebrales</b>. Basado en tomografías del <b>NIH 3D</b> y las ecuaciones de <b>Chaffin y Nachemson</b>, compararás el levantamiento de peso doblando la espalda (brazo de palanca que genera compresiones >4.500 N y hernia discal) frente a la técnica ergonómica con rodillas flexionadas (<1.200 N). <b>No requieres programar:</b> copia el prompt y ejecútalo.",
        "button_action": "🦴 Abrir Columna Vertebral y Biomecánica 3D ↗",
        "html_file": "SIMULADOR_COLUMNA_VERTEBRAL_3D.html",
        "prompt": """\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D de la Columna Vertebral, Discos Intervertebrales y Biomecánica Lumbar (NIH 3D Tomografía Ortopédica y Biomecánica de Chaffin).
Requisitos del código:
1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.
2. Modela en 3D el segmento móvil lumbosacro con vértebras L3, L4, L5 y Sacro S1, con sus cuerpos vertebrales, apófisis espinosas posteriores y discos intervertebrales elásticos (anillo fibroso y núcleo pulposo).
3. Añade control deslizante de Peso Levantado (0 a 35 kg) y botones de técnica ergonómica: Doblando la espalda a 90° vs Flexionando rodillas con torso neutro.
4. Calcula en tiempo real la fuerza compresiva en el disco L5-S1 en Newtons y kgf: doblar la espalda dispara la compresión superando el umbral de lesión de NIOSH (3.400 N).
5. Simula el mecanismo de Hernia Discal: abombamiento posterior del núcleo pulposo que comprime físicamente la raíz del nervio ciático con destellos de dolor irradiado.
6. Telemetría biomecánica con Presión Intradiscal (MPa según Nachemson), estado del canal neural, audio de advertencia por sobrecarga y síntesis de voz en español.
7. Aplica diseño en modo oscuro (#060812) de alto contraste, tipografía grande (16-18px) y sin texto explicativo fuera del código.\""""",
        "extra_challenge": "👉 <b>¡Pídele a Gemini que modifique tu código!</b> Dile: <i>«Añade una opción de degeneración discal senil (Pfirrmann Grado V) que reduzca la altura del disco L5-S1 y muestre osteofitos en los bordes vertebrales»</i>.",
        "scientific_source": "• <b>Biomecánica Musculoesquelética de Chaffin & Andersson:</b> El momento flexor dorsal generado por el torso inclinado a 90° exige una fuerza de contracción reactiva de los músculos erectores espinales multiplicada por la relación de palanca desfavorable de 10:1.<br/>• <b>Estudios Intradiscales In-Vivo de Alf Nachemson:</b> Demostración mediante sensores piezorresistivos de que la presión intradiscal en L3-L4 aumenta hasta un 250% al levantar peso con las rodillas bloqueadas en flexión anterior."
    },
    {
        "num": 39,
        "code": "COD-039",
        "title": "Taller: Crea tu propio simulador 3D de Mimetismo Óptico e Iridiscencia de Mariposa",
        "backup_name": "39_COD-039_Taller_Simulador_Iridiscencia_Mariposa_3D.pdf",
        "header_color": "#0284C7",
        "mission": "En este taller ordenarás a Gemini construir un microscopio y simulador óptico 3D de la <b>Mariposa *Morpho peleides*</b> y sus <b>Nanocristales de Iridiscencia</b>. Basado en fotónica del <b>Natural History Museum de Londres</b>, harás un zoom nanoscópico para descubrir que el deslumbrante azul metálico de sus alas <b>NO es un pigmento químico</b>, sino un color estructural puro producido por láminas de cutícula en forma de 'árbol de Navidad' que interfieren la luz según la <b>Ley de Bragg</b>. <b>No requieres programar:</b> copia el prompt y ejecútalo.",
        "button_action": "🦋 Abrir Iridiscencia y Nanocristales 3D ↗",
        "html_file": "SIMULADOR_IRIDISCENCIA_3D.html",
        "prompt": """\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D de Mimetismo Óptico, Nanocristales e Iridiscencia de Mariposa (Natural History Museum London y Ley de Bragg-Snell).
Requisitos del código:
1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.
2. Modela en 3D un zoom óptico multiescala de 4 niveles: desde el ala de la mariposa Morpho peleides con batido alar hasta las microcrestas nanoscópicas en forma de árbol de Navidad compuestas por lamelas periódicas de cutícula (n=1.56) y aire (n=1.00) separadas 140 nm.
3. Aplica la Ley de Bragg-Snell para interferencia de películas delgadas: calcula la longitud de onda reflejada en función del ángulo de incidencia de la luz (0° a 75°), mostrando cómo el pico de 465 nm (azul metálico) vira hacia el violeta/ultravioleta al aumentar el ángulo.
4. Integra el experimento científico de inmersión en solventes líquidos: al sumergir la escama en etanol (n=1.36), la interferencia desaparece por igualación de índices de refracción, tornando el ala de color marrón de la melanina basal y demostrando que no contiene pigmentos azules.
5. Telemetría con longitud de onda pico (nm), reflectancia espectral (%), índice de refracción del medio, audio interactivo y síntesis de voz en español.
6. Aplica diseño en modo oscuro (#010814), tipografía grande (16-18px) y sin texto explicativo fuera del bloque de código.\""""",
        "extra_challenge": "👉 <b>¡Pídele a Gemini que modifique tu código!</b> Dile: <i>«Añade una gráfica espectrofotométrica interactiva en la esquina inferior que trace la curva de reflectancia gaussiana entre 380 nm y 750 nm»</i>.",
        "scientific_source": "• <b>Fotónica Estructural en la Naturaleza (Natural History Museum):</b> El color del ala de Morpho se genera por difracción y reflexión interferencial constructiva en redes multicapa dieléctricas de queratina/aire (2d cosθ = mλ).<br/>• <b>Experimento de Desplazamiento Dieléctrico:</b> Al sustituir el aire interlamelar por líquidos con índice de refracción similar a la cutícula (n ≈ 1.56), el contraste óptico Δn se aproxima a cero, aboliendo la reflectancia azul."
    },
    {
        "num": 40,
        "code": "COD-040",
        "title": "Taller: Crea tu propio simulador 3D de Regeneración Tisular y Matriz Extracelular",
        "backup_name": "40_COD-040_Taller_Simulador_Regeneracion_Tisular_3D.pdf",
        "header_color": "#0284C7",
        "mission": "En este taller ordenarás a Gemini construir un simulador tridimensional de la <b>Regeneración Tisular Cutánea</b> y la <b>Matriz Extracelular</b>. Basado en modelos de medicina regenerativa del <b>NIH 3D</b>, explorarás la cascada biológica de 28 días: <b>Hemostasia</b> (coágulo de fibrina), <b>Inflamación</b> (fagocitosis de macrófagos M1/M2), <b>Proliferación</b> (migración de fibroblastos y síntesis de colágeno III) y <b>Remodelación</b> (maduración a colágeno I y contracción miofibroblástica). <b>No requieres programar:</b> copia el prompt y ejecútalo.",
        "button_action": "🔬 Abrir Regeneración Tisular 3D ↗",
        "html_file": "SIMULADOR_REGENERACION_TISULAR_3D.html",
        "prompt": """\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D de Regeneración Tisular, Fibroblastos y Matriz Extracelular (NIH 3D y Biología de la Cicatrización de Clark & Singer).
Requisitos del código:
1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.
2. Modela en 3D un lecho de herida tisular con bordes dérmicos sanos y la brecha central que se va cerrando progresivamente a lo largo de una línea de tiempo de 0 a 28 días.
3. Muestra las 4 fases biológicas: 1 Hemostasia (red de fibrina y tapón de plaquetas), 2 Inflamación (infiltrado de neutrófilos y macrófagos limpiadores), 3 Proliferación (migración celular de fibroblastos fusiformes, angiogénesis capilar y depósito de colágeno III) y 4 Remodelación (diferenciación a miofibroblastos con tracción tensil y recambio a colágeno I).
4. Añade control deslizante de Días de Cicatrización (0 a 28) y comorbilidades reales: Hiperglucemia/Diabetes (retrasa severamente el cierre por fallo de macrófagos) y Oxigenoterapia Hiperbárica (acelera la síntesis de colágeno).
5. Telemetría con % de Cierre de la Herida, Resistencia Mecánica a la Tracción (tensile strength), Ratio de Colágeno I/III, audio de pulso tisular y voz didáctica en español.
6. Aplica diseño en modo oscuro (#060a14) accesible (+65), tipografía grande (16-18px) y sin texto explicativo fuera del código.\""""",
        "extra_challenge": "👉 <b>¡Pídele a Gemini que modifique tu código!</b> Dile: <i>«Añade una capa superficial de queratinocitos basales que migren desde los bordes epidérmicos mediante un frente en lengua epitelial para sellar la herida»</i>.",
        "scientific_source": "• <b>Fisiología Tisular de la Cicatrización (Clark & Singer):</b> Transición temporal estrictamente regulada donde los macrófagos M1 proinflamatorios conmutan a fenotipo M2 antiinflamatorio liberando TGF-β1 para reclutar fibroblastos.<br/>• <b>Biomecánica de la Matriz Extracelular:</b> La resistencia mecánica final de la cicatriz no supera el 80% de la piel intacta original, lograda tras meses de reorganización de fibrillas de colágeno tipo I en haces entrecruzados."
    }
]

def generate_script(spec):
    num_str = f"{spec['num']:03d}"
    sesion_str = f"{spec['num']:02d}_Sesion"
    filename = f"build_pdf_cod_{num_str}.py"
    filepath = os.path.join(SCRIPT_DIR, filename)

    content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_{num_str}.py
Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-{num_str}_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
Sesión {spec['num']}: {spec['title']}
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/{sesion_str}"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-{num_str}_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/{spec['backup_name']}"

def build_cod_{num_str}_taller_3d_pdf(output_path=PDF_PATH):
    dest_path = output_path
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as _: pass
    except Exception:
        dest_path = LOCAL_BACKUP
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(dest_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=22, bottomMargin=20)
    styles = getSampleStyleSheet()

    style_header = ParagraphStyle('HStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.0, textColor=colors.HexColor('{spec['header_color']}'), alignment=1, spaceAfter=1)
    style_block = ParagraphStyle('BStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.8, textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4)
    style_title = ParagraphStyle('TStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=11.6, leading=14.0, textColor=colors.HexColor('#0F172A'), spaceAfter=3)
    style_section_h = ParagraphStyle('SecStyle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=8.8, leading=11.2, textColor=colors.HexColor('{spec['header_color']}'), spaceBefore=3, spaceAfter=2)
    style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=7.8, leading=10.4, textColor=colors.HexColor('#1E293B'), spaceAfter=2)
    style_task = ParagraphStyle('TaskStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=7.6, leading=10.0, textColor=colors.HexColor('#0F172A'))
    style_prompt = ParagraphStyle('PromptStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=7.2, leading=9.5, textColor=colors.HexColor('#0F172A'))

    story = [
        Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header),
        Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block),
        HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('{spec['header_color']}'), spaceAfter=4),
        Paragraph("<b>[{spec['code']}] {spec['title']}</b>", style_title),
        Paragraph("💡 <b>Misión Didáctica • Ciencia Rigurosa & Modelado Interactivo con Gemini:</b>", style_section_h),
        Paragraph("{spec['mission']}", style_body)
    ]

    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> Abre Gemini (<i>gemini.google.com</i>). Copia el Prompt Maestro inferior, pégalo y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado:</b> Pulsa <b>«Copiar código»</b> en la esquina superior del bloque HTML de Gemini.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller de Pruebas (Pestaña 2):</b> En el mapa de la Sesión {spec['num']}, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y ejecuta:</b> Pega el código con <b>Ctrl+V</b> y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Tu simulación cobrará vida!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Prueba la Demo Oficial:</b> Pulsa <b>«{spec['button_action']}»</b> en el mapa para contrastar los resultados.", style_task)]
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#34D399')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(t_table)
    story.append(Spacer(1, 3))

    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_text = (
        "<b>Copia exactamente este texto en Gemini:</b><br/>"
        "<i>" + {repr(spec['prompt'])}[1:-1].replace('\\n', '<br/>') + "</i>"
    )
    p_table = Table([[Paragraph(prompt_text, style_prompt)]], colWidths=[letter[0] - 72])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5), ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(p_table)
    story.append(Spacer(1, 3))

    story.append(Paragraph("🌟 <b>El Reto Extra (Para Alumnos Curiosos):</b>", style_section_h))
    story.append(Paragraph("{spec['extra_challenge']}", style_body))
    story.append(Spacer(1, 2))

    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_table = Table([[Paragraph("{spec['scientific_source']}", style_task)]], colWidths=[letter[0] - 72])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 2.0), ('BOTTOMPADDING', (0,0), (-1,-1), 2.0),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(tech_table)

    doc.build(story)
    print(f"✅ Ficha PDF [{spec['code']}] generada: {{dest_path}}")

if __name__ == '__main__':
    build_cod_{num_str}_taller_3d_pdf()
'''

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Creado script: {filename}")

def generate_master_compiler():
    filepath = os.path.join(SCRIPT_DIR, "build_cod_lote4_master.py")
    imports = []
    tasks = []
    for s in PDF_SPECS:
        num_str = f"{s['num']:03d}"
        imports.append(f"from build_pdf_cod_{num_str} import build_cod_{num_str}_taller_3d_pdf")
        tasks.append(f'    ("{s["code"]} ({s["title"][:30]}...)", build_cod_{num_str}_taller_3d_pdf),')

    content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_cod_lote4_master.py
Compilador Maestro del LOTE 4 [COD] (Sesiones 31 a 40).
Ejecuta la generación de las 10 Fichas Didácticas Oficiales en PDF:
- COD-031 a COD-040
"""

import sys
import os

{chr(10).join(imports)}

TASKS = [
{chr(10).join(tasks)}
]

def main():
    print("=" * 80)
    print("🚀 INICIANDO COMPILACIÓN MAESTRA DE FICHAS DIDÁCTICAS LOTE 4 [COD] (SESIONES 31 A 40)")
    print("=" * 80)
    
    total = len(TASKS)
    success = 0
    errors = []

    for idx, (label, func) in enumerate(TASKS, 1):
        try:
            print(f"[{{idx:02d}}/{{total:02d}}] Generando {{label}}...")
            func()
            success += 1
        except Exception as e:
            print(f"❌ Error en {{label}}: {{e}}")
            errors.append((label, str(e)))

    print("\\n" + "=" * 80)
    print(f"📊 RESUMEN: {{success}}/{{total}} FICHAS PDF GENERADAS CORRECTAMENTE.")
    if errors:
        print("⚠️ ERRORES DETECTADOS:")
        for label, err in errors:
            print(f"  - {{label}}: {{err}}")
        sys.exit(1)
    else:
        print("✅ 100% DE LAS FICHAS DEL LOTE 4 COMPILADAS Y SELLADAS.")
        print("=" * 80)

if __name__ == '__main__':
    main()
'''
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Creado script maestro: build_cod_lote4_master.py")

def main():
    for spec in PDF_SPECS:
        generate_script(spec)
    generate_master_compiler()
    print("🎉 Scripts creados con éxito.")

if __name__ == '__main__':
    main()

