# -*- coding: utf-8 -*-
"""
Generador de las 60 temáticas de cómic y literatura formativa para abuelos y nietos.
"""

def get_cuent_items():
    cuent_list = []
    
    # 01. Cuento infantil inaugural con doble opción (<6 años y >6 años)
    cuent_list.append({
        "block_dir": "11. [CUENT] BLOQUE_11_CUENTOS_NIETOS",
        "block_name": "BLOQUE_11_CUENTOS_NIETOS",
        "id_code": "[CUENT-001]",
        "title": "Cuentos Infantiles: El perro bombero que salvó a los gatitos",
        "concept": "Narrativa infantil ilustrada para que el abuelo comparta con su nieto una tierna historia de valentía, trabajo en equipo y protección de los animales.",
        "prompt": "Actúa como un cuentacuentos infantil profesional. Escribe un cuento ilustrado de unos 3 o 4 párrafos sobre 'El perro bombero que salvó a los gatitos'. El cuento debe transmitir de forma sutil los valores de valentía, empatía y ayuda mutua. Usa un lenguaje mágico, visual y atrapante, con un final reconfortante para dormir.",
        "tips": "Fomenta la adaptación según la edad del nieto: para menores de 6 años usa tono dulce y sensorial; para mayores de 6 añade más aventura y suspense."
    })
    
    # Lista de los 59 restantes (02 a 60)
    cuentos_restantes = [
        # BLOQUE A: VIDAS FASCINANTES, GENIOS E INVENTORES (10)
        ("[CUENT-002]", "Grandes Genios: Nikola Tesla y el misterio de la luz invisible",
         "Culturización narrativa sobre la curiosidad científica, el afán de investigar y cómo la electricidad transformó el mundo.",
         "Actúa como un cuentacuentos y narrador pedagógico para niños. Escribe la historia en viñetas de 'Nikola Tesla y el misterio de la luz invisible'. Cuenta cómo de niño observaba las chispas de su gato y soñó con llevar luz a cada rincón de la Tierra. Tono inspirador, lleno de asombro y valores de perseverancia y curiosidad."),
        
        ("[CUENT-003]", "Grandes Genios: Marie Curie y las piedras que brillaban en la noche",
         "Relato sobre el amor al estudio, la superación de dificultades y el descubrimiento de la ciencia en familia.",
         "Actúa como un narrador de literatura infantil y juvenil. Escribe la historia de 'Marie Curie y las piedras que brillaban en la noche'. Muestra su fascinación por los minerales misteriosos en su humilde laboratorio y su generosidad compartiendo sus hallazgos con la humanidad. Tono cálido, lleno de magia científica y valores de generosidad."),

        ("[CUENT-004]", "Grandes Genios: Leonardo da Vinci y el sueño de volar como las aves",
         "Introducción a la creatividad multidisciplinar: pintar, inventar y observar la naturaleza con ojos atentos.",
         "Actúa como un cuentacuentos profesional. Escribe la aventura de 'Leonardo da Vinci y el sueño de volar como las aves'. Relata cómo el joven Leonardo llenaba sus cuadernos de bocetos observando libélulas y alas de pájaros para diseñar sus ingeniosas máquinas voladoras. Tono de aventura renacentista y amor por el aprendizaje."),

        ("[CUENT-005]", "Grandes Genios: Ada Lovelace y la máquina que tejía números",
         "La historia de la primera programadora del mundo contada como un cuento de hadas tecnológico para nietos.",
         "Actúa como un cuentacuentos infantil y juvenil. Escribe el relato de 'Ada Lovelace y la máquina que tejía números'. Explica cómo una niña con enorme imaginación unió las matemáticas con la poesía para anticipar los cerebros de los ordenadores modernos. Tono ameno, brillante y motivador."),

        ("[CUENT-006]", "Grandes Genios: Alexander Fleming y el guardián microscópico",
         "Una lección de cómo la observación paciente y la casualidad pueden salvar millones de vidas.",
         "Actúa como un narrador escolar entrañable. Escribe la historia de 'Alexander Fleming y el guardián microscópico'. Narra cómo un médico curioso descubrió en una placa de laboratorio que un pequeño hongo protegía contra las bacterias, dando origen a la medicina moderna. Tono de intriga detectivesca científica."),

        ("[CUENT-007]", "Grandes Genios: Amelia Earhart y la brújula de las nubes",
         "El coraje de perseguir los sueños y cruzar los cielos derribando barreras.",
         "Actúa como un cuentacuentos de aventuras. Escribe la historia de 'Amelia Earhart y la brújula de las nubes'. Relata su pasión por pilotar avionetas rojas entre tormentas y arcoíris sobre el inmenso océano. Tono épico, emocionante y lleno de confianza en uno mismo."),

        ("[CUENT-008]", "Grandes Genios: Galileo Galilei y los secretos de la Luna",
         "La pasión por buscar la verdad observando las estrellas contra viento y marea.",
         "Actúa como un narrador formativo para niños. Escribe la historia de 'Galileo Galilei y los secretos de la Luna'. Describe la noche mágica en que miró por su tubo de lentes y descubrió montañas en la Luna y compañeros danzando alrededor de Júpiter. Tono poético y de reverencia por el cosmos."),

        ("[CUENT-009]", "Grandes Genios: Los Hermanos Wright y la cometa que aprendió a volar",
         "El trabajo artesanal, el ensayo-error y la determinación de dos hermanos empeñados en surcar el aire.",
         "Actúa como un cuentacuentos de superación. Escribe la historia de 'Los Hermanos Wright y la cometa que aprendió a volar'. Cuenta cómo dos reparadores de bicicletas construyeron alas de madera y tela en las dunas de viento hasta lograr despegar. Tono emocionante y de colaboración fraternal."),

        ("[CUENT-010]", "Grandes Genios: Arquímedes y la corona del rey",
         "El ingenio puro frente a la fuerza bruta: cómo un baño relajante resolvió un enigma de oro.",
         "Actúa como un narrador divertido y formativo. Escribe la aventura de 'Arquímedes y la corona del rey'. Cuenta con humor y claridad cómo el sabio descubrió en la bañera cómo medir el volumen del agua y salió corriendo al grito de ¡Eureka!. Tono alegre y de ingenio."),

        ("[CUENT-011]", "Grandes Genios: Johannes Gutenberg y el bosque de letras de plomo",
         "La revolución de los libros y cómo el conocimiento pasó a estar al alcance de todos los niños del mundo.",
         "Actúa como un cuentacuentos histórico. Escribe 'Johannes Gutenberg y el bosque de letras de plomo'. Relata cómo un artesano unió prensas de uvas con pequeños tipos metálicos para que las historias viajaran por todo el planeta. Tono entrañable y de amor por los libros."),

        # BLOQUE B: GRANDES HAZAÑAS HISTÓRICAS Y EXPLORACIONES (10)
        ("[CUENT-012]", "Hazañas Históricas: El viaje del Apolo 11 y la huella en el polvo lunar",
         "La mayor aventura tecnológica de la humanidad contada desde la emoción de cruzar el abismo espacial.",
         "Actúa como un narrador audiovisual para niños. Escribe la gesta de 'El viaje del Apolo 11 y la huella en el polvo lunar'. Describe el despegue del cohete gigante Saturno V y el instante en que el módulo posó sus patas doradas en el Mar de la Tranquilidad. Tono épico, emocionante y de fraternidad universal."),

        ("[CUENT-013]", "Hazañas Históricas: Shackleton y la tripulación valiente del hielo",
         "La epopeya del Endurance en la Antártida: el verdadero liderazgo no es vencer, sino traer a todos a salvo a casa.",
         "Actúa como un cuentacuentos de expediciones. Escribe la aventura de 'Shackleton y la tripulación valiente del hielo'. Muestra cómo un grupo de marineros cuidaron de sus trineos y perros en los témpanos antárticos hasta ser rescatados gracias a la lealtad de su capitán. Tono heroico y de compañerismo inquebrantable."),

        ("[CUENT-014]", "Hazañas Históricas: Magallanes y Elcano: El abrazo alrededor del mundo",
         "La primera vuelta al globo terráqueo navegando por mares jamás cartografiados.",
         "Actúa como un cuentacuentos marítimo. Escribe la historia de 'Magallanes y Elcano: El abrazo alrededor del mundo'. Describe el cruce del estrecho desconocido entre fuegos lejanos y el regreso de la nao Victoria demostrando que la Tierra es una hermosa esfera redonda. Tono de aventura clásica marina."),

        ("[CUENT-015]", "Hazañas Históricas: La construcción de la Torre de Hierro de París",
         "Cómo el ingeniero Eiffel desafió el vértigo y las críticas para alzar la torre más alta del mundo.",
         "Actúa como un narrador infantil y juvenil. Escribe 'La construcción de la Torre de Hierro de París'. Muestra el baile de remaches al rojo vivo y vigas de celosía que crecían hacia las nubes para la Exposición Universal. Tono visual, constructivo y de orgullo del trabajo bien hecho."),

        ("[CUENT-016]", "Hazañas Históricas: Howard Carter y los tesoros dorados de Tutankamón",
         "La arqueología como la mayor búsqueda del tesoro: linternas, jeroglíficos y el Valle de los Reyes.",
         "Actúa como un narrador de misterio infantil. Escribe 'Howard Carter y los tesoros dorados de Tutankamón'. Cuenta los años de búsqueda en las arenas de Egipto hasta que una pequeña mirilla reveló sarcófagos y carros de oro intactos tras milenios. Tono de intriga, respeto histórico y maravilla."),

        ("[CUENT-017]", "Hazañas Históricas: Marco Polo y las campanas de las caravanas de seda",
         "Cruzar desiertos, montañas y estepas para hermanar culturas lejanas.",
         "Actúa como un cuentacuentos tradicional. Escribe 'Marco Polo y las campanas de las caravanas de seda'. Narra el largo viaje desde Venecia hasta los fastuosos palacios de Catay, descubriendo especias, papel moneda y cometas voladoras. Tono exótico, amable y de tolerancia cultural."),

        ("[CUENT-018]", "Hazañas Históricas: La pequeña María y los bisontes mágicos de Altamira",
         "La niña de ocho años que alzó la mirada en la cueva de Cantabria y descubrió la primera gran pintura de la humanidad.",
         "Actúa como un cuentacuentos entrañable. Escribe 'La pequeña María y los bisontes mágicos de Altamira'. Cuenta cómo una niña jugando con una vela descubrió los lomos rojizos de los bisontes pintados en el techo de piedra por cazadores prehistóricos. Tono de asombro y orgullo de nuestras raíces."),

        ("[CUENT-019]", "Hazañas Históricas: El tren de vapor cruzando la cordillera salvaje",
         "La odisea de abrir túneles y viaductos de piedra para unir pueblos aislados por la nieve.",
         "Actúa como un narrador clásico de aventuras. Escribe 'El tren de vapor cruzando la cordillera salvaje'. Relata la valentía de los maquinistas y fogoneros alimentando la caldera de carbón para cruzar desfiladeros imposibles y llevar cartas y medicinas. Tono épico y ferroviario."),

        ("[CUENT-020]", "Hazañas Históricas: El rescate del batiscafo en las fosas del océano",
         "Explorar el fondo más hondo del mar donde no llega ni un rayo de sol.",
         "Actúa como un cuentacuentos de exploración submarina. Escribe 'El rescate del batiscafo en las fosas del océano'. Cuenta la inmersión en una esfera de acero con grandes focos descubriendo peces luminosos y criaturas abisales asombrosas. Tono de misterio acuático y respeto por el mar."),

        ("[CUENT-021]", "Hazañas Históricas: El gran reloj astronómico de la plaza medieval",
         "La maestría de los maestros artesanos construyendo engranajes que siguen el curso de los astros y las estaciones.",
         "Actúa como un cuentacuentos tradicional. Escribe 'El gran reloj astronómico de la plaza medieval'. Narra cómo un sabio relojero diseñó un mecanismo de bronce con figuras danzantes que enseñaba a todo el pueblo el ciclo del sol y la luna. Tono mágico y de sabiduría artesana."),

        # BLOQUE C: CLÁSICOS DEL TEBEO POPULAR Y AVENTURAS CABALLERESCAS (10)
        ("[CUENT-022]", "Clásicos del Cómic: El Caballero del Antifaz y el castillo de la niebla",
         "Homenaje al cómic de aventuras medievales: valor, defensa de los débiles y lealtad inquebrantable.",
         "Actúa como un guionista de cómic clásico español para niños. Escribe la aventura de 'El Caballero del Antifaz y el castillo de la niebla'. Narra cómo el noble jinete enmascarado cabalga de noche para liberar a los aldeanos de un bandido que les arrebató sus cosechas. Tono de acción caballeresca noble, sin violencia gráfica, ensalzando la justicia."),

        ("[CUENT-023]", "Clásicos del Cómic: El Capitán Valiente y el torneo de la paz",
         "El espíritu del cómic heroico tradicional: resolver conflictos con nobleza e ingenio en lugar de armas.",
         "Actúa como un narrador de tebeo clásico. Escribe 'El Capitán Valiente y el torneo de la paz'. Cuenta cómo un veterano capitán y sus jóvenes escuderos superan las pruebas del rey usando destreza, agilidad y corazón para evitar una guerra vecina. Tono dinámico, divertido y caballeresco."),

        ("[CUENT-024]", "Clásicos del Cómic: El Corsario de la Nao Blanca y el galeón perdido",
         "Aventuras marítimas en aguas transparentes buscando islas con mapas trazados a mano.",
         "Actúa como un cuentacuentos de aventuras marinas. Escribe 'El Corsario de la Nao Blanca y el galeón perdido'. Describe timones crujiendo, velas al viento y la búsqueda de un antiguo cargamento de libros y mapas robados por corsarios codiciosos. Tono vivaz y de brisa marinera."),

        ("[CUENT-025]", "Clásicos del Cómic: El misterio de la locomotora fantasma",
         "Intriga sobre raíles al estilo del tebeo de misterio europeo: detectives infantiles resolviendo enigmas.",
         "Actúa como un narrador de novela gráfica juvenil. Escribe 'El misterio de la locomotora fantasma'. Narra cómo un joven ayudante de estación y su perro descubren que los silbidos misteriosos en el túnel abandonado eran provocados por el viento en una vieja chimenea. Tono detectivesco y alegre."),

        ("[CUENT-026]", "Clásicos del Cómic: Los exploradores del cráter de los dinosaurios",
         "Expediciones con mapas de piel, cantimploras y gigantes del pasado en valles remotos.",
         "Actúa como un cuentacuentos de aventuras pulp familiares. Escribe 'Los exploradores del cráter de los dinosaurios'. Cuenta el hallazgo de un valle protegido entre cascadas donde manadas de herbívoros gigantes conviven pacíficamente. Tono de maravilla natural y respeto por la fauna."),

        ("[CUENT-027]", "Clásicos del Cómic: El guardián de la muralla y el halcón mensajero",
         "La complicidad entre el vigía de la torre y su fiel ave en las cumbres montañosas.",
         "Actúa como un narrador de leyendas de frontera. Escribe 'El guardián de la muralla y el halcón mensajero'. Relata cómo un halcón adiestrado avisa a tiempo de una gran tormenta de nieve para que los pastores recojan a sus rebaños. Tono emotivo de lealtad animal."),

        ("[CUENT-028]", "Clásicos del Cómic: Los tres aprendices de la imprenta secreta",
         "Jóvenes audaces defendiendo la libertad de repartir periódicos y noticias justas.",
         "Actúa como un cuentacuentos histórico de aventuras urbanas. Escribe 'Los tres aprendices de la imprenta secreta'. Muestra a tres muchachos repartidores burlando a guardias despistados en callejones adoquinados para entregar el periódico de la verdad. Tono ágil, cómico y valiente."),

        ("[CUENT-029]", "Clásicos del Cómic: El enigma de la esfinge de alabastro",
         "Aventuras de arqueólogos y exploradores descifrando acertijos de piedra sin caer en trampas.",
         "Actúa como un narrador de tebeo clásico de aventuras. Escribe 'El enigma de la esfinge de alabastro'. Cuenta cómo dos compañeros de expedición usan un espejo y la luz del sol para activar el mecanismo que abre la biblioteca secreta de un templo milenario. Tono de ingenio y arqueología."),

        ("[CUENT-030]", "Clásicos del Cómic: El joven Quijote y el molino de las sorpresas",
         "Reinvención formativa para niños del mito cervantino: la imaginación como el escudo más poderoso.",
         "Actúa como un cuentacuentos cervantino adaptado para nietos. Escribe 'El joven Quijote y el molino de las sorpresas'. Narra con humor tierno cómo el hidalgo caballero y su escudero descubren que el molino gigante es un amigo de madera que ayuda a moler harina para todo el pueblo. Tono poético y entrañable."),

        ("[CUENT-031]", "Clásicos del Cómic: El detective de la boina y el gato de la discordia",
         "Intriga de barrio tradicional español con humor sano, vecindad y pistas curiosas.",
         "Actúa como un narrador costumbrista y cómico de tebeo. Escribe 'El detective de la boina y el gato de la discordia'. Cuenta cómo un abuelo sagaz resuelve por qué el gato del carnicero siempre desaparecía a las cinco de la tarde para visitar a una abuela solitaria. Tono tierno, simpático y de vecindad."),

        # BLOQUE D: MITOS, LEYENDAS Y HÉROES UNIVERSALES (10)
        ("[CUENT-032]", "Mitos y Héroes: Robin del Bosque Verde y la flecha de la diana de oro",
         "El arquero legendario que defendía a los campesinos frente a las injusticias de los poderosos.",
         "Actúa como un cuentacuentos legendario para niños. Escribe la historia de 'Robin del Bosque Verde y la flecha de la diana de oro'. Narra el torneo de tiro con arco en que Robin, disfrazado de anciano mendigo, parte en dos la flecha del rival para regalar el premio a los pobres del pueblo. Tono de justicia, humor y puntería."),

        ("[CUENT-033]", "Mitos y Héroes: El joven Arturo y la espada en el yunque de piedra",
         "La nobleza de corazón por encima del linaje: sólo quien es puro y justo puede empuñar la espada.",
         "Actúa como un narrador de leyendas artúricas para niños. Escribe 'El joven Arturo y la espada en el yunque de piedra'. Describe la plaza de la catedral en invierno, los caballeros presumidos que fracasan y el muchacho humilde que saca la espada sin esfuerzo para ayudar a su hermano. Tono solemne y emotivo."),

        ("[CUENT-034]", "Mitos y Héroes: Teseo, Ariadna y el laberinto de la sombra",
         "Cómo la inteligencia y un hilo de lana vencieron al miedo en el laberinto más temido del mundo.",
         "Actúa como un cuentacuentos mitológico formativo. Escribe 'Teseo, Ariadna y el laberinto de la sombra'. Cuenta cómo el héroe no usó la violencia desmedida sino la astucia y el ovillo dorado para salir de los pasadizos de piedra y pactar la paz en Creta. Tono de misterio mitológico e ingenio."),

        ("[CUENT-035]", "Mitos y Héroes: Guillermo Tell y la manzana en los picos nevados",
         "El amor de un padre por su hijo y la defensa de la libertad en las montañas de Suiza.",
         "Actúa como un narrador dramático y noble para niños. Escribe 'Guillermo Tell y la manzana en los picos nevados'. Narra el tenso momento en que el cazador debe acertar con su ballesta a una manzana sobre la cabeza de su hijo confiado y cómo su serenidad vence al tirano. Tono de valentía y vínculo paterno-filial."),

        ("[CUENT-036]", "Mitos y Héroes: El flautista viajero y la melodía del bosque",
         "La importancia sagrada de cumplir la palabra dada y tratar con respeto a los forasteros.",
         "Actúa como un cuentacuentos clásico. Escribe 'El flautista viajero y la melodía del bosque'. Versión adaptada donde la música mágica rescata al pueblo de una plaga pero enseña a los concejales a no ser tacaños ni engañar a quien les ayudó. Tono moral, lírico y de justicia poética."),

        ("[CUENT-037]", "Mitos y Héroes: El caballero Jorge y el dragón de las aguas claras",
         "Una leyenda de coraje donde el entendimiento pacífico y la protección de la naturaleza vencen al fuego.",
         "Actúa como un cuentacuentos infantil. Escribe 'El caballero Jorge y el dragón de las aguas claras'. Narra cómo el noble jinete dialoga con el dragón sediento para limpiar el manantial del pueblo en lugar de luchar, sellando una alianza de amistad eterna. Tono noble y pacífico."),

        ("[CUENT-038]", "Mitos y Héroes: La valiente Mulan y el estandarte de la nieve",
         "El sacrificio de una hija para proteger a su anciano padre enfermo y defender a su pueblo.",
         "Actúa como un narrador épico infantil. Escribe 'La valiente Mulan y el estandarte de la nieve'. Cuenta cómo la joven demuestra que la astucia en la estrategia y la lealtad familiar valen más que la fuerza física de cien guerreros. Tono de honor, amor filial y coraje."),

        ("[CUENT-039]", "Mitos y Héroes: El guardián de barro de la vieja Praga",
         "La leyenda del gigante protector moldeado con tierra del río Moldava para cuidar a los desvalidos.",
         "Actúa como un cuentacuentos centroeuropeo para niños. Escribe 'El guardián de barro de la vieja Praga'. Relata cómo un sabio grabó en la frente de un coloso la palabra Verdad para que velara por el barrio judío en las noches frías de invierno. Tono solemne, protector y lleno de encanto medieval."),

        ("[CUENT-040]", "Mitos y Héroes: El martillo del trueno y el gigante juguetón",
         "Leyendas nórdicas de relámpagos, cielos de aurora boreal y desafíos de ingenio.",
         "Actúa como un narrador de mitos nórdicos infantiles. Escribe 'El martillo del trueno y el gigante juguetón'. Cuenta cómo el dios del trueno recupera su martillo mágico no peleando, sino ganando un concurso de adivinanzas contra el gigante de escarcha. Tono simpático, épico y de ingenio."),

        ("[CUENT-041]", "Mitos y Héroes: Ulises y el misterio del canto de las olas",
         "La curiosidad por escuchar lo desconocido resistiendo la tentación gracias al consejo sabio.",
         "Actúa como un cuentacuentos homérico para niños. Escribe 'Ulises y el misterio del canto de las olas'. Narra cómo el navegante se ató al mástil de madera de su barco con cera en los oídos de sus remeros para disfrutar de la música de las sirenas sin peligro. Tono poético y de aventura marina."),

        # BLOQUE E: CIENCIA FICCIÓN CLÁSICA, AUTÓMATAS Y STEAMPUNK (10)
        ("[CUENT-042]", "Ciencia Ficción Clásica: Veinte mil leguas en el submarino Nautilus",
         "La visión de Julio Verne: barcos de metal que bucean como cetáceos en el fondo de los océanos.",
         "Actúa como un cuentacuentos verniano para niños. Escribe 'Veinte mil leguas en el submarino Nautilus'. Describe el gran ventanal circular del salón del Capitán Nemo iluminando bosques de coral gigante, pulpos fosforescentes y ruinas de ciudades sumergidas. Tono de asombro científico y maravilla submarina."),

        ("[CUENT-043]", "Ciencia Ficción Clásica: Viaje al interior de la Tierra de Julio Verne",
         "Descender por cráteres apagados hacia un mundo subterráneo de setas gigantes y playas ocultas.",
         "Actúa como un narrador de aventuras clásicas. Escribe 'Viaje al interior de la Tierra de Julio Verne'. Relata la bajada de un profesor y su sobrino guiados por un pergamino antiguo hasta un mar interior donde navegan en balsa bajo techos de cristal iluminados por gases eléctricos. Tono de intriga científica y expedición."),

        ("[CUENT-044]", "Ciencia Ficción Clásica: La nave esférica rumbo a la Luna",
         "El cañón gigante que disparó una cápsula habitable hacia la órbita de nuestro satélite.",
         "Actúa como un cuentacuentos de ciencia ficción pionera. Escribe 'La nave esférica rumbo a la Luna'. Muestra a los pioneros con telescopios flotando en gravedad cero dentro de su cápsula acolchada con perros y plantas. Tono alegre, visionario y lleno de optimismo tecnológico."),

        ("[CUENT-045]", "Ciencia Ficción Clásica: La máquina del tiempo y el reloj del futuro",
         "Homenaje a H.G. Wells: palancas de marfil y cristal que giran para ver el mañana.",
         "Actúa como un narrador de fantasía científica infantil. Escribe 'La máquina del tiempo y el reloj del futuro'. Describe el taller del inventor y cómo el dial retrocede y avanza mostrando civilizaciones de jardines luminosos y flores gigantes. Tono poético y de reflexión sobre cuidar el planeta."),

        ("[CUENT-046]", "Ciencia Ficción Clásica: El autómata de latón que jugaba al ajedrez",
         "La fascinación decimonónica por los robots mecánicos de engranajes y muelles de relojería.",
         "Actúa como un cuentacuentos steampunk para niños. Escribe 'El autómata de latón que jugaba al ajedrez'. Cuenta la historia de una figura mecánica con turbante y ruedas dentadas que vencía a reyes jugando partidas pero que en realidad guardaba en su pecho una pequeña caja de música. Tono misterioso y elegante."),

        ("[CUENT-047]", "Ciencia Ficción Clásica: La ciudad de los zepelines y puentes de bronce",
         "Estética steampunk: ciudades verticales entre nubes propulsadas por vapor y poleas silenciosas.",
         "Actúa como un narrador visual de fantasía retro-futurista. Escribe 'La ciudad de los zepelines y puentes de bronce'. Narra el viaje de un abuelo maquinista y su nieto a bordo de un dirigible plateado que atraca en las agujas de una metrópolis que funciona con energía solar y agua caliente. Tono visual espectacular."),

        ("[CUENT-048]", "Ciencia Ficción Clásica: El centinela del faro en el fin del universo",
         "Un faro espacial que emite haces de luz cuántica para guiar a las sondas exploradoras.",
         "Actúa como un cuentacuentos poético de ciencia ficción. Escribe 'El centinela del faro en el fin del universo'. Muestra a un anciano astrónomo en una estación rocosa limpiando las lentes de plasma que evitan que las naves choquen con lluvias de meteoritos. Tono sereno, hermoso y reconfortante para dormir."),

        ("[CUENT-049]", "Ciencia Ficción Clásica: Los robots mensajeros de la ciudad de cobre",
         "Compañeros robóticos autónomos (con nombres originales y simpáticos) ayudando a los humanos.",
         "Actúa como un narrador infantil de ciencia ficción amable. Escribe 'Los robots mensajeros de la ciudad de cobre'. Relata cómo dos droides mecánicos llamados Chispas y Rueditas rescatan un mapa estelar extraviado en el mercado galáctico para ayudar a despegar a una nave médica. Tono divertido y de amistad tecnológica."),

        ("[CUENT-050]", "Ciencia Ficción Clásica: El tren que atravesaba los anillos de Saturno",
         "Un convoy ferroviario transparente que viaja suspendido sobre partículas de hielo cósmico.",
         "Actúa como un cuentacuentos galáctico para niños. Escribe 'El tren que atravesaba los anillos de Saturno'. Describe las vistas desde las ventanas panorámicas con fragmentos de hielo brillando como diamantes bajo la luz de las lunas del gigante gaseoso. Tono poético y deslumbrante."),

        ("[CUENT-051]", "Ciencia Ficción Clásica: El jardín botánico dentro de la nave cúpula",
         "Proteger la flora y los árboles de la Tierra viajando en una inmensa biosfera transparente por el espacio.",
         "Actúa como un cuentacuentos ecológico de ciencia ficción. Escribe 'El jardín botánico dentro de la nave cúpula'. Muestra cómo abuelo y nieta riegan robles, naranjos y mariposas mientras su nave cruza nebulosas de colores hacia un nuevo hogar. Tono de paz, ecología y amor a la naturaleza."),

        # BLOQUE F: OBRAS MAESTRAS DE LA LITERATURA CLÁSICA ADAPTADAS (9)
        ("[CUENT-052]", "Literatura Clásica: El Principito y el secreto del zorro sabio",
         "El valor de lo invisible a los ojos: la amistad, el cuidado de la rosa y la ternura esencial.",
         "Actúa como un narrador lírico infantil. Escribe la historia de 'El Principito y el secreto del zorro sabio'. Recrea el encuentro en las dunas doradas del desierto donde el zorro enseña que domesticar significa crear lazos y que uno se hace responsable de lo que ama para siempre. Tono poético, filosófico y reconfortante."),

        ("[CUENT-053]", "Literatura Clásica: El viaje de Gulliver a la isla de los diminutos",
         "La perspectiva y la tolerancia: el gigante amable que ayudó a un reino en miniatura.",
         "Actúa como un cuentacuentos de literatura universal. Escribe 'El viaje de Gulliver a la isla de los diminutos'. Cuenta cómo el náufrago despierta atado por miles de hilos de seda por personitas de seis pulgadas y cómo se gana su confianza apagando incendios con su sombrero y defendiéndoles con ternura. Tono divertido y de convivencia pacífica."),

        ("[CUENT-054]", "Literatura Clásica: El Mago de Oz y el camino de baldosas amarillas",
         "Descubrir que lo que buscamos (corazón, cerebro y coraje) ya habita dentro de nosotros.",
         "Actúa como un narrador clásico para niños. Escribe 'El Mago de Oz y el camino de baldosas amarillas'. Narra la travesía de Dorothy junto al Espantapájaros, el Hombre de Hojalata y el León Cobarde superando obstáculos en equipo hasta descubrir que la magia está en volver a casa. Tono colorido, musical y de autoestima."),

        ("[CUENT-055]", "Literatura Clásica: Pinocho y el grillo de la buena conciencia",
         "El viaje de un muñeco de madera hacia la empatía, el esfuerzo escolar y el amor a su creador.",
         "Actúa como un cuentacuentos moral y entrañable. Escribe 'Pinocho y el grillo de la buena conciencia'. Cuenta cómo el muñeco aprende a no dejarse engañar por zorros y gatos callejeros y rescata a su padre Gepetto del vientre del gran pez ballena para ganarse un corazón de niño de verdad. Tono tierno y de superación."),

        ("[CUENT-056]", "Literatura Clásica: La isla del tesoro y el mapa del viejo marinero",
         "La iniciación a la aventura, el mar embravecido y el respeto a la palabra de honor.",
         "Actúa como un narrador de aventuras literarias clásicas. Escribe 'La isla del tesoro y el mapa del viejo marinero'. Cuenta cómo el joven Jim Hawkins halla un pergamino con una cruz roja en un baúl de posada y zarpa en La Española entre gaviotas y canciones marineras. Tono vibrante, de aventura sana y sin violencia."),

        ("[CUENT-057]", "Literatura Clásica: Alicia en el jardín de las maravillas parlantes",
         "La imaginación sin límites, juegos de lógica y acertijos divertidos para la mente infantil.",
         "Actúa como un cuentacuentos de fantasía literaria. Escribe 'Alicia en el jardín de las maravillas parlantes'. Narra la merienda de té del Sombrerero Loco y las flores que cantan acertijos matemáticos y juegos de palabras divertidos. Tono chispeante, ingenioso y alegre."),

        ("[CUENT-058]", "Literatura Clásica: El bosque de Mowgli y las enseñanzas del oso Baloo",
         "La ley de la selva entendida como respeto al río, armonía entre especies y agradecimiento a la manada.",
         "Actúa como un cuentacuentos de Kipling para niños. Escribe 'El bosque de Mowgli y las enseñanzas del oso Baloo'. Describe cómo el oso bonachón y la pantera negra enseñan al cachorro humano a buscar miel, nadar sin asustar a los peces y ser agradecido con la naturaleza. Tono rítmico, sabio y natural."),

        ("[CUENT-059]", "Literatura Clásica: Heidi y el aire puro de las cumbres alpinas",
         "La bondad que transforma a las personas: el abuelo huraño que vuelve a sonreír con la pureza de su nieta.",
         "Actúa como un narrador entrañable y emotivo. Escribe 'Heidi y el aire puro de las cumbres alpinas'. Cuenta la vida en la cabaña de madera entre abetos susurrantes, cabras montesas y flores de edelweiss, mostrando cómo el amor de la niña ilumina la vida del abuelo solitario. Tono cálido, familiar y de amor a la montaña."),

        ("[CUENT-060]", "Literatura Clásica: Don Quijote y el gran banquete de la amistad en la ínsula",
         "El broche de oro literario: Sancho Panza como gobernador sabio y bondadoso demostrando que la justicia con corazón es el mayor logro de la humanidad.",
         "Actúa como un maestro de la literatura y cuentacuentos para nietos. Escribe 'Don Quijote y el gran banquete de la amistad en la ínsula'. Narra cómo Sancho Panza resuelve pleitos con sentido común y cómo él y don Quijote celebran bajo las encinas de la Mancha que el mayor tesoro del mundo es la libertad y un buen amigo. Tono sublime, tierno, cómico y de clausura magistral.")
    ]
    
    for item in cuentos_restantes:
        cuent_list.append({
            "block_dir": "11. [CUENT] BLOQUE_11_CUENTOS_NIETOS",
            "block_name": "BLOQUE_11_CUENTOS_NIETOS",
            "id_code": item[0],
            "title": item[1],
            "concept": item[2],
            "prompt": item[3],
            "tips": "Invita a los alumnos a adaptar el vocabulario y tono si el nieto es menor de 6 años o mayor de 6 años, e insertar nombres de sus propios nietos o lugares familiares."
        })
        
    return cuent_list
