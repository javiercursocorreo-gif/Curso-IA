#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
actualizar_memoria_construcciones_historicas.py
Actualiza el Bloque 13 [MEM] de la Sesión 03 a la Sesión 15 (MEM-003 a MEM-015):
Sustituye los antiguos temas costumbristas (pupitres, ultramarinos, televisión, chapas, etc.)
por Grandes Monumentos y Obras Emblemáticas de Madrid y España en PLENA CONSTRUCCIÓN HISTÓRICA:
- Estado a mitad de construcción (cimbras, arcos, sillares, esqueletos metálicos).
- Entorno histórico real de la época (caminos de tierra, carretas de bueyes, tranvías, barrancos).
- Herramientas, ingenios mecánicos y grúas de época (jaula de ardilla, ingenios de Herrera, trispastos romanos, grúas de vapor, remachadoras al rojo vivo).
- Retos y preguntas de ingeniería y vida cotidiana para pedirle a Gemini y reflexionar en el aula.
"""

import os
import re
import sys
import shutil

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SESSIONS_DIR = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
MEM_DIR_LOTE1 = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "13. [MEM] BLOQUE_13_CAPSULA_DE_LA_MEMORIA", "Lote_01_al_20")

MEM_NUEVOS_ITEMS = [
    {
        "num": 3,
        "id_code": "[MEM-003]",
        "titulo_corto": "La Puerta de Alcalá en Construcción",
        "titulo_completo": "La Puerta de Alcalá en Construcción: Cantería y Andamios de Sabatini (1774-1778, Madrid)",
        "lugar_epoca": "Madrid (1774-1778) • Reinado de Carlos III • Arquitecto Francesco Sabatini",
        "concepto": "Explorar la construcción del monumento neoclásico por encargo de Carlos III, con sus arcos de medio punto apeados por cimbras de madera, canteros labrando granito de Colmenar a golpe de cincel y carretas de bueyes en el camino de tierra del Retiro.",
        "prompt": "Fotografía histórica hiperrealista en color sepia documental o grabado de época de la Puerta de Alcalá en Madrid a mitad de construcción (año 1776, diseño de Francesco Sabatini). Muestra los arcos centrales de medio punto a medio cerrar, rodeados de monumentales andamios de vigas de pino de Guadarrama y cuerdas de cáñamo. Canteros con mandiles de cuero labrando pesados sillares de granito berroqueño a golpe de maza y cincel, y poleas de madera izando capiteles jónicos. En el suelo de tierra sin adoquinar, carretas de bueyes descargando bloques de piedra, y de fondo la tapia del Real Sitio del Buen Retiro con campos abiertos y arrabales de la época. Luz natural diáfana, polvo en suspensión y atmósfera de gran obra civil histórica.",
        "pregunta1": "Explícame qué técnicas de cantería, tipos de grúas de madera (cabrestantes y poleas de tracción animal) y qué morteros se emplearon en Madrid en el siglo XVIII para levantar la Puerta de Alcalá sin maquinaria moderna.",
        "pregunta2": "¿Por qué Carlos III ordenó derribar la antigua puerta del siglo XVI y cómo era el camino de Alcalá y el entorno rural del Retiro en 1778 comparado con la plaza actual?"
    },
    {
        "num": 4,
        "id_code": "[MEM-004]",
        "titulo_corto": "El Palacio de Cibeles en Construcción",
        "titulo_completo": "El Palacio de Cibeles en Construcción: Acero y Cantería de Palacios y Otamendi (1907-1919, Madrid)",
        "lugar_epoca": "Madrid (1907-1919) • Arquitectos Antonio Palacios y Joaquín Otamendi",
        "concepto": "Descubrir el colosal esqueleto de vigas de hierro remachado del Palacio de Comunicaciones (Correos), con grúas de vapor, bloques de piedra de Novelda y los primeros tranvías eléctricos rodeando la Fuente de Cibeles.",
        "prompt": "Fotografía histórica en blanco y negro de época de la construcción del Palacio de Comunicaciones (actual Palacio de Cibeles) en Madrid entre 1908 y 1912 (arquitectos Antonio Palacios y Joaquín Otamendi). El monumental edificio se muestra a medio levantar, con el imponente entramado de vigas de acero y columnas remachadas al descubierto y grúas de pluma movidas por vapor en la parte alta. En la base, cientos de bloques de piedra blanca de Novelda acopiados sobre la plaza de Castelar, operarios con boina y chaleco trabajando entre andamios de madera. En primer plano, la Fuente de Cibeles presenciando la obra, carruajes de caballos y los primeros tranvías eléctricos de Madrid pasando cerca. Máxima fidelidad de época y detalle arquitectónico.",
        "pregunta1": "Describe los retos de ingeniería estructural que supuso combinar el esqueleto moderno de acero laminado con la fachada monumental de piedra en el Palacio de Comunicaciones de Madrid a principios del siglo XX.",
        "pregunta2": "¿Cómo funcionaban las grúas de vapor y los hornillos de remachado al rojo vivo en las grandes construcciones de Madrid de 1910?"
    },
    {
        "num": 5,
        "id_code": "[MEM-005]",
        "titulo_corto": "La Gran Vía de Madrid: La Gran Demolición",
        "titulo_completo": "La Gran Vía de Madrid: La Gran Demolición y Apertura del Bulevar (1910-1920)",
        "lugar_epoca": "Madrid (1910-1920) • Reinado de Alfonso XIII • Gran Reforma Urbana",
        "concepto": "Presenciar la transformación urbana más radical de Madrid: la piqueta de Alfonso XIII derribando más de 300 edificios, apisonadoras de vapor y el alzamiento de los primeros rascacielos entre nubes de escombros.",
        "prompt": "Fotografía histórica documental de la apertura de la Gran Vía de Madrid hacia 1912, tras el inicio de las obras con la piqueta de Alfonso XIII. Vista panorámica de la gran brecha abierta en el corazón de Madrid: solares de escombros de las más de 300 casas demolidas, apisonadoras de rodillos de vapor humeantes alisando el terreno y mulas retirando cascotes en carros de madera. A los lados, medianeras de casas antiguas al descubierto y los andamios de madera de los primeros edificios modernos en construcción (como el Metrópolis o el edificio Grassy) con grúas mecánicas de celosía. Trabajadores picando adoquines y transeúntes con bombín y trajes de época observando fascinados la llegada de la modernidad.",
        "pregunta1": "Detalla cómo se organizó la gigantesca demolición urbana de la Gran Vía de Madrid a partir de 1910: cuántas calles y casas desaparecieron y qué maquinaria de vapor y tracción animal se combinaron.",
        "pregunta2": "¿Qué edificios emblemáticos se levantaron en el primer tramo (Red de San Luis a Alcalá) y cómo cambió el transporte con el nuevo bulevar?"
    },
    {
        "num": 6,
        "id_code": "[MEM-006]",
        "titulo_corto": "La Catedral de Burgos: Agujas Góticas",
        "titulo_completo": "La Catedral de Burgos: Grúas Medievales y Alzamiento de las Agujas Góticas (Siglo XIII y XV)",
        "lugar_epoca": "Burgos (Siglo XIII y XV) • Fernando III y Obispo Mauricio • Juan de Colonia",
        "concepto": "Revivir la ingeniería gótica con grúas de rueda de pisar ('jaula de ardilla'), arbotantes apeados por cimbras de madera y canteros elevando agujas caladas a 80 metros sobre el río Arlanzón.",
        "prompt": "Grabado o recreación histórica fotorrealista de la construcción de la Catedral de Burgos en la Edad Media (alzamiento de las agujas góticas caladas de Juan de Colonia en el siglo XV o las naves del siglo XIII). La catedral se ve a mitad de edificación, con arcos ojivales y arbotantes sostenidos por complejas cimbras de madera. En lo alto de las torres, colosales grúas medievales de rueda de pisar ('jaula de ardilla') donde operarios caminan dentro de una gran rueda de madera para izar bloques de piedra caliza de Hontoria con poleas y sogas gruesas. En la explanada, talleres de cantería a cielo abierto con maestros artesanos tallando tracerías, carros de bueyes y el río Arlanzón con el caserío medieval de Burgos al fondo. Realismo técnico e histórico riguroso.",
        "pregunta1": "¿Cómo funcionaban las grúas de rueda de pisar (jaula de ardilla) en la arquitectura medieval y qué ventaja mecánica ofrecían para subir dovelas de piedra a 80 metros de altura en catedrales góticas?",
        "pregunta2": "¿Cómo calculaban los maestros constructores medievales el equilibrio de los arbotantes y contrafuertes sin ordenadores ni fórmulas matemáticas modernas?"
    },
    {
        "num": 7,
        "id_code": "[MEM-007]",
        "titulo_corto": "El Monasterio de El Escorial: Ingenios de Herrera",
        "titulo_completo": "El Monasterio de El Escorial: Los Ingenios de Herrera y la Sierra de Guadarrama (1563-1584, Madrid)",
        "lugar_epoca": "San Lorenzo de El Escorial (1563-1584) • Felipe II y Juan de Herrera",
        "concepto": "Conocer la mayor obra renacentista de Europa: las grúas y cabrestantes mecánicos diseñados por Juan de Herrera ('Los Ingenios'), subiendo colosales sillares de granito con decenas de bueyes en la ladera de Guadarrama.",
        "prompt": "Fotografía histórica hiperrealista o pintura al óleo técnica de la construcción del Monasterio de San Lorenzo de El Escorial hacia 1575 (bajo la dirección de Juan de Herrera y Felipe II). El inmenso cuadrante de granito gris se observa a medio erigir, con los patios interiores y muros exteriores rodeados de monumentales andamiajes de madera atados con cáñamo. En primer plano, una de las célebres grúas mecánicas de Juan de Herrera ('el ingenio') con tornos, engranajes de bronce y poleas múltiples izando un colosal sillar de granito de varias toneladas. Yuntas de bueyes arrastrando carros de tiro pesado por rampas de tierra, cientos de canteros y albañiles trabajando, y de fondo la ladera boscosa de la sierra de Guadarrama bajo el cielo azul castellano.",
        "pregunta1": "¿En qué consistían exactamente las grúas mecánicas denominadas 'Los Ingenios de Juan de Herrera' y qué innovaciones introdujeron en la construcción del Monasterio de El Escorial?",
        "pregunta2": "¿Cómo se abastecía de piedra, madera y agua a los miles de operarios que trabajaban en plena sierra en el siglo XVI?"
    },
    {
        "num": 8,
        "id_code": "[MEM-008]",
        "titulo_corto": "El Acueducto de Segovia: Montaje Romano a Hueso",
        "titulo_completo": "El Acueducto de Segovia: El Montaje Romano de Granito a Hueso (Siglo I-II d.C.)",
        "lugar_epoca": "Segovia (Siglos I-II d.C.) • Época Flavia o Trajano • Ingeniería Romana",
        "concepto": "Asombrarse ante la obra cumbre de la ingeniería romana: arquerías dobles alzadas a casi 30 metros sin una gota de cemento ni argamasa, mediante poleas romanas trispastos y tenazas de hierro autotensantes.",
        "prompt": "Recreación histórica fotorrealista de la construcción del Acueducto de Segovia por ingenieros y legionarios romanos (siglos I-II d.C., época de los Flavios o Trajano). La monumental arquería doble de la plaza del Azoguejo se observa a mitad de montaje: pilares de granito gris almohadillado alzándose sobre cimbras de madera de roble que sostienen los arcos de medio punto. Grúas romanas trispastos y polispastos de madera con tornos de mano y cabrestantes izando pesados sillares mediante tenazas de hierro ('olivas' o 'louves') que dejan muescas visibles en la piedra. Ingenieros romanos con togas y túnicas comprobando niveles con corobates y plomadas, y al fondo el valle segoviano y el campamento romano con tiendas de cuero.",
        "pregunta1": "Explica el principio físico y arquitectónico por el cual el Acueducto de Segovia se mantiene en pie desde hace 2.000 años 'a hueso' (sin mortero ni argamasa) y qué herramientas romanas se usaban para izar los sillares.",
        "pregunta2": "¿Cómo medían los ingenieros romanos la pendiente milimétrica constante a lo largo de los más de 15 kilómetros de canalización desde la sierra?"
    },
    {
        "num": 9,
        "id_code": "[MEM-009]",
        "titulo_corto": "El Palacio de Cristal del Retiro",
        "titulo_completo": "El Palacio de Cristal del Retiro: Ensamblaje de Hierro Curvado y Vidrio (1887, Madrid)",
        "lugar_epoca": "Madrid (1887) • Parque del Retiro • Arquitecto Ricardo Velázquez Bosco",
        "concepto": "Vivir la arquitectura del hierro del siglo XIX: montaje de cerchas de fundición, arcos esbeltos y miles de láminas de cristal sobre el estanque del Retiro por Ricardo Velázquez Bosco.",
        "prompt": "Fotografía documental histórica en blanco y negro o tonos sepia de la construcción del Palacio de Cristal en el Parque del Retiro de Madrid (1887, arquitecto Ricardo Velázquez Bosco). La ligera estructura de hierro fundido curvado y columnas jónicas de fundición se muestra en pleno montaje, con operarios con chaleco y gorra caminando sin arneses sobre las esbeltas cerchas metálicas de la cúpula central. Andamios de madera cruzados alrededor del basamento de ladrillo y cerámica vidriada de Daniel Zuloaga. En la orilla del estanque artificial, cajas de madera abiertas con cientos de planchas de cristal fino desembaladas con paja protectora. Árboles del Retiro alrededor y reflejos en el agua con una atmósfera limpia de la Revolución Industrial española.",
        "pregunta1": "¿Qué significó el Palacio de Cristal del Retiro dentro de la arquitectura del hierro y vidrio en España y cómo se fabricaban y ensamblaban esas piezas de fundición curvada en 1887?",
        "pregunta2": "¿Cómo se resolvió el reto de la dilatación térmica del metal y la ventilación para evitar que el calor rompiera los miles de cristales?"
    },
    {
        "num": 10,
        "id_code": "[MEM-010]",
        "titulo_corto": "La Gran Marquesina de Atocha",
        "titulo_completo": "La Gran Marquesina de la Estación de Atocha: Récord de Hierro sin Columnas (1888-1892, Madrid)",
        "lugar_epoca": "Madrid (1888-1892) • Estación de Mediodía • Alberto de Palacio",
        "concepto": "La proeza técnica de Alberto de Palacio (discípulo de Eiffel): una bóveda de 152 metros de longitud y 48 metros de luz libre sin soportes centrales, con remachadores al rojo vivo y grúas móviles.",
        "prompt": "Fotografía histórica de época (hacia 1890) del montaje de la gran marquesina de hierro de la Estación de Mediodía (Atocha) en Madrid, diseñada por Alberto de Palacio. La colosal estructura en arco de 152 metros de largo se muestra a medio techar, con su imponente bóveda de celosía metálica que cubre un espacio libre gigantesco de 48 metros de ancho sin una sola columna intermedia. Enormes andamios de madera móviles sobre rieles, remachadores golpeando pernos incandescentes con mazas entre nubes de chispas y humo de fraguas portátiles de carbón. En las vías de la explanada, locomotoras de vapor primitivas maniobrando vagones con vigas de hierro laminadas en Bélgica y obreros ferroviarios uniformados. Épica industrial finisecular.",
        "pregunta1": "¿Por qué la marquesina histórica de Atocha fue un hito mundial de ingeniería en 1892 al salvar 48 metros de luz sin columnas intermedias y cómo influyó la escuela de Gustave Eiffel en Alberto de Palacio?",
        "pregunta2": "¿Cómo se colocaban los miles de remaches al rojo vivo y qué papel jugaban los equipos de calentadores y remachadores en las obras ferroviarias?"
    },
    {
        "num": 11,
        "id_code": "[MEM-011]",
        "titulo_corto": "El Puente de Vizcaya: Primer Transbordador",
        "titulo_completo": "El Puente de Vizcaya: El Primer Puente Transbordador del Mundo (1890-1893, Bilbao)",
        "lugar_epoca": "Portugalete / Las Arenas (1890-1893) • Alberto de Palacio y Ferdinand Arnodin",
        "concepto": "Patrimonio de la Humanidad de la UNESCO: el alzamiento de cuatro torres de hierro de 61 metros sobre la ría del Nervión y el tendido de cables de acero sin interrumpir la navegación marítima.",
        "prompt": "Fotografía histórica vintage de época (1892) de la construcción del Puente Colgante de Vizcaya (Puente de Portugalete), diseñado por Alberto de Palacio y Ferdinand Arnodin. Vista sobre la ría del Nervión con las cuatro colosales torres de celosía de hierro de 61 metros ya levantadas en Portugalete y Las Arenas, con operarios tendiendo los colosales cables de acero trenzado sobre la pasarela superior suspendida a gran altura. Andamiajes ligeros en la cima de las torres, barcazas y gabarras de vapor cargadas de mineral de hierro cruzando por debajo sin interrupción. Humo de chimeneas industriales a lo largo de la ría y atmósfera brumosa del Bilbao de la industrialización. Gran rigor técnico y paisajístico.",
        "pregunta1": "¿Por qué el Puente de Vizcaya fue una solución revolucionaria mundial que mereció ser declarado Patrimonio de la Humanidad por la UNESCO y por qué se descartó un puente levadizo o un viaducto tradicional?",
        "pregunta2": "¿Cómo se realizaba el cálculo del tendido y tensión de los cables de acero de Ferdinand Arnodin a finales del siglo XIX?"
    },
    {
        "num": 12,
        "id_code": "[MEM-012]",
        "titulo_corto": "El Teatro Real de Madrid",
        "titulo_completo": "El Teatro Real de Madrid: Tres Décadas de Construcción en la Plaza de Oriente (1818-1850)",
        "lugar_epoca": "Madrid (1818-1850) • Antonio López Aguado y Custodio Moreno",
        "concepto": "La larga aventura del colosal teatro de ópera frente al Palacio Real: muros ciclópeos de ladrillo y granito, cerchas monumentales de madera y la transformación de la antigua plazuela en la majestuosa Plaza de Oriente.",
        "prompt": "Grabado o fotografía histórica coloreada de la prolongada construcción del Teatro Real de Madrid en la década de 1840 (arquitectos Antonio López Aguado y Custodio Teodoro Moreno). La monumental mole hexagonal del teatro se observa con sus muros de ladrillo macizo y sillares de granito de Colmenar a medio coronar, rodeada de gigantescos andamios de madera de varios cuerpos de altura frente al Palacio Real. Operarios izando pesadas cerchas de madera para la cubierta de la caja escénica con tornos de cuerda, carromatos de caballos descargando yeso y cal en la gran explanada aún en obras de la Plaza de Oriente, y transeúntes madrileños de época isabelina contemplando el edificio que tardó más de 30 años en culminarse.",
        "pregunta1": "¿Por qué la construcción del Teatro Real de Madrid se prolongó durante más de 30 años (1818 a 1850) y qué problemas financieros, políticos y de cimentación sobre los antiguos barrancos de Madrid tuvieron que superar?",
        "pregunta2": "¿Cómo se diseñó la acústica y la gigantesca caja escénica en la época de Isabel II antes de existir micrófonos ni amplificadores?"
    },
    {
        "num": 13,
        "id_code": "[MEM-013]",
        "titulo_corto": "La Sagrada Familia: Fachada del Nacimiento",
        "titulo_completo": "La Sagrada Familia: El Alzamiento de la Fachada del Nacimiento con Gaudí (1892-1925, Barcelona)",
        "lugar_epoca": "Barcelona (1892-1925) • Antoni Gaudí • Ensanche barcelonés primitivo",
        "concepto": "Contemplar a Antoni Gaudí en persona dirigiendo la obra sobre los campos del Ensanche: las primeras tres torres helicoidales alzándose con grúas de vapor y modelos de yeso a pie de obra.",
        "prompt": "Fotografía histórica sepia de principios del siglo XX (hacia 1915-1920) de la construcción del Templo Expiatorio de la Sagrada Familia en Barcelona. Las primeras torres de la Fachada del Nacimiento se observan a mitad de elevación, con sus perfiles parabólicos y pináculos rodeados de rústicos andamios de madera entrelazados y una grúa de vapor sobre rieles provisionales. Alrededor del templo no hay ciudad densa, sino los campos abiertos, huertas y caminos de tierra del primitivo Ensanche barcelonés. En primer plano, el cobertizo-taller de yesos y maquetas donde se aprecia la figura inconfundible de Antoni Gaudí de espaldas, con abrigo oscuro y sombrero, revisando planos con los maestros de obras entre bloques de piedra de Montjuïc esculpidos con motivos botánicos.",
        "pregunta1": "¿Qué método experimental de maquetas invertidas con saquitos de perdigones y cuerdas usaba Gaudí para calcular las curvas catenarias de la Sagrada Familia sin hacer cálculos matemáticos complejos?",
        "pregunta2": "¿Cómo era el entorno de campos y huertas de Barcelona alrededor de la Sagrada Familia en vida de Gaudí y cómo se transportaba la piedra desde la cantera de Montjuïc?"
    },
    {
        "num": 14,
        "id_code": "[MEM-014]",
        "titulo_corto": "El Viaducto de Segovia: El Viaducto de Hierro",
        "titulo_completo": "El Viaducto de Segovia: El Gran Viaducto de Hierro sobre el Barranco (1874, Madrid)",
        "lugar_epoca": "Madrid (1874) • Ingeniero Eugenio Barrón • Unión de Palacio y Vistillas",
        "concepto": "Superar el abismo de la calle Segovia: montaje de la celosía de hierro remachado de Eugenio Barrón a más de 20 metros de altura, con las casas bajas y lavanderas al pie de los pilares.",
        "prompt": "Fotografía histórica de época (hacia 1873-1874) de la construcción del primer Viaducto de Segovia (el Viaducto de Hierro de Eugenio Barrón) en Madrid. Se observa la gran estructura de celosía metálica de hierro forjado a medio montar, suspendida en el aire sobre los esbeltos pilares de hierro que salvan la profunda hondonada de la calle Segovia. Operarios sobre pasarelas voladas de madera sin arneses atornillando y remachando pernos a más de 23 metros de altura. En el fondo del barranco, la calle de tierra con lavanderas, carros de mulas y casas bajas tradicionales con tejas curvas mirando asombradas hacia la colosal obra de ingeniería que une el Palacio Real con las Vistillas.",
        "pregunta1": "¿Qué reto orográfico milenario de Madrid resolvió el Viaducto de Segovia y qué diferencias de diseño y materiales hubo entre el viaducto metálico original de 1874 y el actual de hormigón armado de los años 30?",
        "pregunta2": "¿Cómo se realizaba el izado y montaje de las enormes cerchas metálicas sobre un barranco urbano habitado en el siglo XIX?"
    },
    {
        "num": 15,
        "id_code": "[MEM-015]",
        "titulo_corto": "Los Rascacielos de Plaza de España",
        "titulo_completo": "Los Rascacielos de Plaza de España: Edificio España y Torre de Madrid (1948-1957, Madrid)",
        "lugar_epoca": "Madrid (1948-1957) • Hermanos Julián y Joaquín Otamendi",
        "concepto": "La llegada de la escala vertical y el hormigón armado a Madrid: los colosos de los hermanos Otamendi con grúas torre, hormigoneras gigantes y camiones clásicos en la Plaza de España.",
        "prompt": "Fotografía documental histórica en blanco y negro de los años 50 mostrando la construcción del Edificio España y la Torre de Madrid en la Plaza de España de Madrid (diseñados por los hermanos Julián y Joaquín Otamendi). El gigantesco rascacielos escalonado del Edificio España se muestra a medio levantar, con decenas de plantas de forjados de hormigón armado al descubierto y grúas torre mecánicas izando materiales en la cumbre. Miles de metros de andamios tubulares y de madera en las fachadas, camiones clásicos Pegaso y hormigoneras humeantes descargando áridos en la plaza. En primer plano, el monumento a Cervantes y Don Quijote rodeado de vallas de obra y madrileños con gabardinas y sombreros observando el nacimiento del primer skyline moderno de España.",
        "pregunta1": "Explica la proeza técnica y constructiva que supuso levantar el Edificio España (117 metros) y la Torre de Madrid (142 metros) en los años 50 como los edificios más altos de Europa de hormigón armado.",
        "pregunta2": "¿Qué sistemas de bombeo de hormigón, grúas torre y ascensores de obra se emplearon y cómo transformó para siempre la perspectiva visual del final de la Gran Vía?"
    }
]

def escape_pdf_text(text):
    text = str(text)
    text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    replacements = {
        'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
        'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
        'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
        '«': '<<', '»': '>>', '•': '-', '—': '-', '–': '-',
        'º': 'o', 'ª': 'a', '¿': '\xbf', '¡': '\xa1',
        '➔': '->', '→': '->', '’': "'", '‘': "'", '“': '"', '”': '"'
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def wrap_text(text, max_chars):
    paragraphs = str(text).split('\n')
    lines = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        words = p.split(' ')
        cur = []
        cur_len = 0
        for w in words:
            if not w:
                continue
            if cur_len + len(w) + 1 <= max_chars:
                cur.append(w)
                cur_len += len(w) + 1
            else:
                if cur:
                    lines.append(' '.join(cur))
                cur = [w]
                cur_len = len(w)
        if cur:
            lines.append(' '.join(cur))
    return lines or ['']

class NativePDFWriter:
    def __init__(self, page_width=612.0, page_height=792.0): # Letter estándar
        self.w = page_width
        self.h = page_height
        self.pages = []
        self.current_stream = []

    def start_page(self):
        self.current_stream = []

    def end_page(self):
        self.pages.append("".join(self.current_stream))
        self.current_stream = []

    def set_fill_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} rg\n")

    def set_stroke_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} RG\n")

    def set_line_width(self, width):
        self.current_stream.append(f"{width:.2f} w\n")

    def rect(self, x, y, width, height, fill=True, stroke=True):
        op = "B" if (fill and stroke) else ("f" if fill else "S")
        self.current_stream.append(f"{x:.2f} {y:.2f} {width:.2f} {height:.2f} re {op}\n")

    def line(self, x1, y1, x2, y2):
        self.current_stream.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S\n")

    def draw_text(self, x, y, text, font="F1", size=10, r=0, g=0, b=0):
        self.set_fill_color(r, g, b)
        escaped = escape_pdf_text(text)
        self.current_stream.append(f"BT /{font} {size} Tf {x:.2f} {y:.2f} Td ({escaped}) Tj ET\n")

    def write_to_file(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        f1_idx, f2_idx, f3_idx = 3, 4, 5
        page_obj_indices = []
        content_obj_indices = []
        cur_obj_idx = 6

        for _ in self.pages:
            page_obj_indices.append(cur_obj_idx)
            cur_obj_idx += 1
            content_obj_indices.append(cur_obj_idx)
            cur_obj_idx += 1

        kids_str = " ".join([f"{idx} 0 R" for idx in page_obj_indices])
        pages_dict = f"<< /Type /Pages /Kids [{kids_str}] /Count {len(self.pages)} >>".encode('ascii')

        all_objs = [
            b"<< /Type /Catalog /Pages 2 0 R >>",
            pages_dict,
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>"
        ]

        for p_idx, c_idx in zip(page_obj_indices, content_obj_indices):
            p_obj = f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.w} {self.h}] /Contents {c_idx} 0 R /Resources << /Font << /F1 {f1_idx} 0 R /F2 {f2_idx} 0 R /F3 {f3_idx} 0 R >> >> >>".encode('ascii')
            p_stream = self.pages[(p_idx - 6) // 2]
            c_bytes = p_stream.encode('latin-1', errors='replace')
            c_obj = f"<< /Length {len(c_bytes)} >>\nstream\n".encode('ascii') + c_bytes + b"\nendstream"
            all_objs.append(p_obj)
            all_objs.append(c_obj)

        with open(filename, 'wb') as f:
            f.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
            xref_positions = [0]
            pos = f.tell()
            for idx, obj_bytes in enumerate(all_objs, start=1):
                xref_positions.append(pos)
                header = f"{idx} 0 obj\n".encode('ascii')
                footer = b"\nendobj\n"
                f.write(header + obj_bytes + footer)
                pos = f.tell()

            xref_start = pos
            f.write(f"xref\n0 {len(all_objs) + 1}\n".encode('ascii'))
            f.write(b"0000000000 65535 f \n")
            for p in xref_positions[1:]:
                f.write(f"{p:010d} 00000 n \n".encode('ascii'))

            trailer = f"trailer\n<< /Size {len(all_objs) + 1} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF\n".encode('ascii')
            f.write(trailer)

def create_mem_native_pdf(output_path, item):
    writer = NativePDFWriter(page_width=612.0, page_height=792.0) # Letter
    margin_x = 42.0
    content_w = writer.w - (margin_x * 2) # 528.0 pt

    writer.start_page()

    # Barra superior dorada / ámbar
    writer.set_fill_color(0.72, 0.53, 0.04) # Oro viejo / ámbar #B8860B
    writer.rect(margin_x, writer.h - 26, content_w, 4, fill=True, stroke=False)

    y = writer.h - 48
    writer.draw_text(margin_x, y, "CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGIA PARA ADULTOS MAYORES (60+)", "F2", 8.5, 0.72, 0.53, 0.04)
    y -= 14
    writer.draw_text(margin_x, y, "BLOQUE 13: CAPSULA DE LA MEMORIA [MEM] - GRANDES OBRAS HISTORICAS", "F2", 10.5, 0.1, 0.05, 0.2)
    y -= 10

    writer.set_stroke_color(0.72, 0.53, 0.04)
    writer.set_line_width(1.5)
    writer.line(margin_x, y, margin_x + content_w, y)
    y -= 18

    # Título del Ítem
    writer.draw_text(margin_x, y, f"{item['id_code']} {item['titulo_completo']}", "F2", 12.0, 0.1, 0.05, 0.2)
    y -= 14
    writer.draw_text(margin_x, y, f"Patrimonio: {item['lugar_epoca']}", "F3", 9.0, 0.45, 0.45, 0.45)
    y -= 16

    # 1. Contexto Histórico
    writer.draw_text(margin_x, y, "Objetivo Didactico y Contexto Historico:", "F2", 9.5, 0.72, 0.53, 0.04)
    y -= 12
    for line in wrap_text(item['concepto'], 92):
        writer.draw_text(margin_x, y, line, "F1", 8.8, 0.18, 0.22, 0.28)
        y -= 11.5

    y -= 6

    # 2. Paso 1: Generar la Recreación Histórica en el Ordenador (PC)
    writer.draw_text(margin_x, y, "Paso 1: Recrear la Escena de Construccion con IA en el Ordenador (PC)", "F2", 9.5, 0.72, 0.53, 0.04)
    y -= 10

    p_lines = wrap_text(f'"{item["prompt"]}"', 88)
    prompt_box_h = 24 + (len(p_lines) * 11.5)

    writer.set_fill_color(0.98, 0.96, 0.91) # Crema / pergamino claro
    writer.set_stroke_color(0.72, 0.53, 0.04)
    writer.set_line_width(1.2)
    writer.rect(margin_x, y - prompt_box_h, content_w, prompt_box_h, fill=True, stroke=True)

    ty = y - 14
    writer.draw_text(margin_x + 10, ty, "Copia este prompt exacto y pegalo en Gemini Web (gemini.google.com):", "F2", 8.2, 0.1, 0.05, 0.2)
    ty -= 13
    for pl in p_lines:
        writer.draw_text(margin_x + 10, ty, pl, "F3", 8.2, 0.1, 0.05, 0.2)
        ty -= 11.5

    y -= (prompt_box_h + 14)

    # 3. Paso 2: Reto y Preguntas de Investigacion con Gemini
    writer.draw_text(margin_x, y, "Paso 2: Preguntas de Ingenieria y Vida Cotidiana para el Dialogo con Gemini", "F2", 9.5, 0.72, 0.53, 0.04)
    y -= 10

    q1_lines = wrap_text(f"1. Ingenieria de epoca: {item['pregunta1']}", 88)
    q2_lines = wrap_text(f"2. Entorno y vida cotidiana: {item['pregunta2']}", 88)
    tips_box_h = 24 + ((len(q1_lines) + len(q2_lines)) * 12.0) + 8

    writer.set_fill_color(1.0, 1.0, 1.0)
    writer.set_stroke_color(0.72, 0.53, 0.04)
    writer.set_line_width(1.2)
    writer.rect(margin_x, y - tips_box_h, content_w, tips_box_h, fill=True, stroke=True)

    ty = y - 14
    writer.draw_text(margin_x + 10, ty, "Escribe o dicta por voz estas dos preguntas a Gemini tras ver la imagen:", "F2", 8.2, 0.72, 0.53, 0.04)
    ty -= 14
    for ql in q1_lines:
        writer.draw_text(margin_x + 10, ty, ql, "F1", 8.2, 0.15, 0.2, 0.26)
        ty -= 11.5
    ty -= 4
    for ql in q2_lines:
        writer.draw_text(margin_x + 10, ty, ql, "F1", 8.2, 0.15, 0.2, 0.26)
        ty -= 11.5

    # Pie de página
    writer.set_stroke_color(0.85, 0.88, 0.92)
    writer.set_line_width(0.6)
    writer.line(margin_x, 32, margin_x + content_w, 32)
    writer.draw_text(margin_x, 22, f"Curso de Inteligencia Artificial para Seniors • Sesion {item['num']:02d} • {item['id_code']} {item['titulo_corto']}", "F1", 7.8, 0.45, 0.48, 0.52)
    writer.draw_text(margin_x + content_w - 180, 22, "Patrimonio Historico y Tecnico de Espana", "F2", 7.8, 0.72, 0.53, 0.04)

    writer.end_page()
    writer.write_to_file(output_path)

def sanitize_filename(name):
    clean = re.sub(r'[/\\:*?"<>|]', '_', name)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:65]

def main():
    print("🚀 Iniciando actualización integral de fichas [MEM] (Sesiones 03 a 15)...")

    for item in MEM_NUEVOS_ITEMS:
        s_num = item["num"]
        s_folder = f"{s_num:02d}_Sesion"
        target_session_dir = os.path.join(SESSIONS_DIR, s_folder)

        safe_title = sanitize_filename(item["titulo_completo"])
        session_pdf_name = f"14. {item['id_code']}_{safe_title}.pdf"
        lote_pdf_name = f"{item['id_code'].replace('[', '').replace(']', '')}_{safe_title}.pdf"

        # 1. Limpiar fichas MEM antiguas en la carpeta de sesión
        if os.path.exists(target_session_dir):
            for f in os.listdir(target_session_dir):
                if "MEM-" in f and f.endswith(".pdf"):
                    old_path = os.path.join(target_session_dir, f)
                    try:
                        os.remove(old_path)
                        print(f"   🗑️ Eliminado antiguo {f} en Sesión {s_num:02d}")
                    except Exception as e:
                        print(f"   ⚠️ Error eliminando {f}: {e}")

        # 2. Generar el nuevo PDF nativo en la carpeta de sesión
        session_pdf_path = os.path.join(target_session_dir, session_pdf_name)
        create_mem_native_pdf(session_pdf_path, item)
        print(f"   ✅ Generado: {s_folder}/{session_pdf_name}")

        # 3. Guardar copia en el Lote maestro de MEM
        lote_pdf_path = os.path.join(MEM_DIR_LOTE1, lote_pdf_name)
        create_mem_native_pdf(lote_pdf_path, item)

    print("\n🎉 ¡Las 13 fichas [MEM] han sido generadas y reemplazadas con éxito!")

if __name__ == "__main__":
    main()
