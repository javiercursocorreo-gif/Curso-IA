# -*- coding: utf-8 -*-
"""
Generador Maestro del Bloque 13: [MEM] CÁPSULA DE LA MEMORIA: MI INFANCIA, MI BARRIO Y MI PUEBLO (60 Ítems)
Propósito: Conectar a los abuelos con sus nietos mediante la recreación visual y narrativa de su infancia,
adaptado tanto para quienes crecieron en un PUEBLO RURAL como para quienes crecieron en MADRID o en un BARRIO URBANO.
Variables adaptables: [MI_LUGAR_PUEBLO_O_BARRIO] y [MI_AÑO_O_DÉCADA].
REGLA ESTRICTA: 0% alusiones a la Guerra Civil o política. Enfoque 100% costumbrista, familiar y positivo.
"""

def get_memoria_items():
    memoria_list = []

    temas = [
        # 1. LA CALLE Y LOS JUEGOS DE INFANCIA (01-10)
        ("La Plaza o el Barrio de Mi Infancia: Juegos de Calle (Peonza y Canicas)",
         "Recrear la plaza del pueblo o la calle de barrio (ej. Madrid/Chamberí/Lavapiés) y recordar cómo se jugaba al aire libre.",
         "Recrea una fotografía histórica en color sepia cálido o blanco y negro de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Si es un barrio urbano o Madrid, muestra una calle adoquinada con tranvías clásicos, farolas de hierro y balcones con toldos a rayas. Si es un pueblo, muestra la plaza mayor de tierra o piedra y casas tradicionales. En primer plano, niños con pantalones cortos y boina jugando agachados a las canicas y bailando la peonza de madera con cuerda. Atmósfera entrañable, nostálgica y llena de vida, sin coches modernos ni textos en inglés.",
         "💬 Para contarle a tus nietos: Enséñales esta imagen y pregúntales: '¿Sabéis cómo hacíamos bailar una peonza en la acera con una cuerda de cáñamo?'. Pídele a Gemini a continuación: 'Dime 3 cosas curiosas y cotidianas que ocurrieron en España en el año [MI_AÑO_DE_NACIMIENTO], cuánto costaba un café o un billete de metro/autobús en pesetas, y qué invento llegó a los hogares esa década. Sin temas de guerra ni política'."),

        ("El Lavadero Comunal o las Corralas de Vecinos: El Olor a Jabón Casero",
         "Recordar el punto de encuentro donde se lavaba a mano con jabón casero de sosa o en los patios de vecinos.",
         "Fotografía histórica de época en tonos sepia mostrando el lavadero público o el patio de una corrala tradicional de vecinos en [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Mujeres lavando sábanas y ropa blanca con pastillas de jabón casero, tendiendo la ropa al sol en cuerdas cruzadas entre balcones de forja o pilares de madera, charlando amigablemente bajo la luz de la mañana. Atmósfera comunitaria y auténtica.",
         "💬 Para contarle a tus nietos: Explícales cómo se hacía el jabón con restos de aceite usado y sosa cáustica y el olor a limpio de las sábanas tendidas al sol. Pídele a Gemini: 'Escribe un relato corto de dos párrafos en tono de abuelo contando a su nieto cómo era la vida comunitaria y la ayuda entre vecinas en los años [MI_AÑO_O_DÉCADA]'."),

        ("La Escuela de Barrio o Rural: Pupitres de Madera Dobles y el Tintero",
         "Mostrar a los nietos cómo eran las aulas de la época con pizarra de tiza, mapas de tela y tintero de porcelana.",
         "Fotografía nostálgica de época de un aula escolar en [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Pupitres dobles de madera barnizada con su agujero para el tintero blanco de cerámica, una gran pizarra negra con cuentas escritas con tiza, una estufa de hierro en un rincón y un mapa físico de España de tela enrollable en la pared. Niños y niñas con batas escolares escuchando con atención, atmósfera luminosa y entrañable.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era escribir con plumilla metálica mojada en tinta china y el miedo a que cayera un borrón en el cuaderno. Pídele a Gemini: '¿Qué asignaturas, cuadernos y enciclopedias clásicas (como la Enciclopedia Álvarez) estudiaban los niños en España en los años [MI_AÑO_O_DÉCADA]?'."),

        ("La Tienda de Ultramarinos o la Vaquería de Barrio: Balanza de Pesas y Granel",
         "Revivir los ultramarinos y tiendas de coloniales donde todo se vendía a granel en cartuchos de papel de estraza.",
         "Fotografía de época del interior de una tienda de ultramarinos o vaquería tradicional en [MI_LUGAR_PUEBLO_O_BARRIO] en [MI_AÑO_O_DÉCADA]. Mostrador largo de madera con una gran balanza de dos platos dorados con pesas de latón, sacos de arpillera abiertos en el suelo con legumbres, latas grandes de membrillo y botellas de vidrio alineadas. El tendero con guardapolvo gris despachando con simpatía a una clienta con bolsa de malla de tela.",
         "💬 Para contarle a tus nietos: Enséñales que antes no existían las bolsas de plástico y todo iba en cartuchos cónicos de papel de estraza. Pregúntale a Gemini: '¿Cuánto costaba un cuarto de kilo de café o un litro de leche en pesetas en España en los años 50 y 60?'."),

        ("El Primer Televisor del Barrio o del Bar Social",
         "Recordar el acontecimiento de reunirse los vecinos en el bar o centro social para ver la tele en blanco y negro.",
         "Escena costumbrista histórica en un bar o salón vecinal de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Una pequeña televisión de válvulas en blanco y negro en una peana alta de madera en la pared, con decenas de vecinos mayores y niños fascinados mirando la pantalla iluminada, con sifones de agua de soda, vasos de chato de vino y porrones sobre las mesas. Rostros de asombro y alegría compartida.",
         "💬 Para contarle a tus nietos: Pregúntales si se imaginan un mundo con un solo canal de televisión que empezaba a emitir por la tarde y donde toda la calle iba al mismo bar a verla juntos. Pídele a Gemini: '¿Qué programas míticos de TVE y qué anuncios clásicos veían las familias españolas en los años 60?'."),

        ("Juegos Tradicionales: La Rayuela, las Chapas de Refresco y la Comba",
         "Transmitir a los nietos las reglas de los juegos que no necesitaban pilas ni pantallas.",
         "Fotografía histórica de niños sonrientes en una calle o plaza de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. En el suelo hay dibujada con yeso blanco una rayuela numerada y un circuito de carreras de chapas aplastadas con fotos de ciclistas pegadas dentro. Al lado, dos niñas saltan a la comba cogidas del ritmo bajo la luz dorada del atardecer. Energía infantil limpia y alegre.",
         "💬 Para contarle a tus nietos: Enséñales cómo se rellenaban las chapas de refresco con plastilina o cera de vela para que corrieran más en el suelo. Pídele a Gemini: 'Escríbeme las reglas sencillas y divertidas del juego de las chapas para enseñárselo a jugar a mi nieto este fin de semana'."),

        ("El Campo y los Parques Históricos: De las Eras a la Casa de Campo o el Retiro",
         "Recordar las tardes de domingo al aire libre, ya fuera en los campos del pueblo o paseando por el parque.",
         "Fotografía histórica panorámica en tonos cálidos en [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Si es un pueblo, muestra campesinos en la era con trillo y sombreros de paja bajo el sol estival. Si es Madrid o ciudad, muestra familias paseando junto a los estanques del Parque del Retiro o la Casa de Campo, niños con barquitos de madera y familias merendando a la sombra de los castaños. Luz estival limpia y atmósfera entrañable.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era pasar una tarde entera al aire libre merendando bajo los árboles sin mirar ningún reloj ni móvil. Pídele a Gemini: '¿Cómo eran los domingos de excursión familiar y merienda en los parques y campos de España a mediados del siglo XX?'."),

        ("El Seat 600 y los Tranvías: Los Primeros Viajes en Familia",
         "Revivir la emoción del mítico 'pelotilla' cargado hasta el techo o de subir al tranvía de madera.",
         "Fotografía vintage en color de los años 60 de una calle o carretera de [MI_LUGAR_PUEBLO_O_BARRIO]. Un flamante Seat 600 blanco o verde claro con una baca en el techo repleta de maletas de cartón atadas con cuerdas, cruzándose con un clásico tranvía urbano con trole superior, con una familia sonriente saludando desde el interior. Nostalgia y alegría de los primeros viajes familiares.",
         "💬 Para contarle a tus nietos: Pregúntales cuántos cabían en un 600 sin aire acondicionado cantando canciones por la carretera. Pídele a Gemini: '¿Qué supuso la llegada del Seat 600 para la movilidad de las familias trabajadoras españolas en los años 60 y cuánto costaba comprar uno?'."),

        ("La Radio de Válvulas y las Radionovelas de la Tarde",
         "Recordar cómo se reunía la familia alrededor del receptor de madera para escuchar historias.",
         "Escena íntima de hogar español en [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Sobre una mesita con tapete de ganchillo blanco luce una radio grande de madera barnizada con dial luminoso de cristal verde y ojo mágico. Una abuela haciendo calceta y un abuelo leyendo la prensa escuchan la emisión mientras una suave luz entra por el balcón. Ambiente hogareño cálido y sereno.",
         "💬 Para contarle a tus nietos: Explícales que antes de las series de televisión modernas, la gente se emocionaba con las voces y efectos de sonido de los seriales de radio. Pídele a Gemini: '¿Cuáles fueron los seriales radiofónicos y radionovelas más célebres de la radio española en los años 50 y 60?'."),

        ("La Panadería de Barrio y el Pan de Horno de Leña",
         "Evocar el olor inolvidable del pan recién cocido con masa madre en los hornos tradicionales.",
         "Fotografía histórica del interior de un obrador de pan tradicional en [MI_LUGAR_PUEBLO_O_BARRIO] en [MI_AÑO_O_DÉCADA]. La boca de piedra del horno de leña con rescoldos encendidos al fondo, el panadero con pala larga de madera sacando hogazas redondas doradas y barras crujientes con harina en la corteza, y estanterías de madera repletas de panes recién hechos. Vaho caliente y aroma rústico auténtico.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era ir a por el pan de buena mañana y pellizcar el cuscurro caliente de camino a casa. Pídele a Gemini: '¿Cómo se elaboraba el pan tradicional de masa madre y horno de leña en los barrios y pueblos de España?'."),

        # 2. OFICIOS, COSTUMBRES Y SONIDOS DE LA ÉPOCA (11-20)
        ("El Afilador con su Chiflo por las Calles de la Ciudad o del Pueblo",
         "Recordar la melodía inconfundible de la flauta de pan que resonaba anunciando el afilado de cuchillos y tijeras.",
         "Fotografía de calle histórica de un afilador ambulante en [MI_LUGAR_PUEBLO_O_BARRIO] en [MI_AÑO_O_DÉCADA]. El afilador con chaleco de pana pedaleando su rueda de esmeril con chispas brillantes al aire mientras afila un cuchillo, con vecinas esperando con tijeras de costura en la mano y niños fascinados escuchando la melodía de notas agudas de su chiflo de madera.",
         "💬 Para contarle a tus nietos: Pregúntales si saben cómo sonaba la melodía del afilador que subía y bajaba de tono. Pídele a Gemini: '¿Cuál era el origen de los afiladores tradicionales que recorrían toda España y qué instrumentos usaban?'."),

        ("El Lechero y las Vaquerías Urbanas de Puerta en Puerta",
         "Rememorar el reparto matinal de leche fresca en lecheras de aluminio o la visita a la vaquería del barrio.",
         "Escena histórica de primera hora de la mañana en una calle de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. El repartidor con carro y grandes cántaras metálicas de aluminio sirviendo leche fresca con un cazo dosificador en la lechera esmaltada blanca con ribete azul que sostiene una vecina sonriente en la puerta de su casa o portal. Detrás, fachada tradicional con rótulos pintados a mano.",
         "💬 Para contarle a tus nietos: Explícales por qué había que hervir la leche en el cazo para que subiera la nata y lo rica que estaba esa nata fresca con un poco de azúcar. Pídele a Gemini: '¿Cómo funcionaban las vaquerías urbanas en ciudades como Madrid y cómo era el reparto de leche de puerta en puerta?'."),

        ("Las Verbenas Castizas y Fiestas Patronales: El Baile y la Orquesta",
         "Revivir la emoción del mantón de Manila, los farolillos de papel, las bombillas de colores y el pasodoble.",
         "Fotografía festiva de noche de verbena en [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Guirnaldas de bombillas de colores encendidas cruzando la plaza o calle, un entarimado con una orquesta tocando saxofones y acordeones, y parejas de jóvenes y mayores bailando pasodobles y chotis con mantones bordados y trajes elegantes. Clima alegre, romántico y festivo.",
         "💬 Para contarle a tus nietos: Enséñales qué canciones sonaban en el baile en tus tiempos y cómo se bailaba pegado. Pídele a Gemini: '¿Cuáles fueron los mayores éxitos musicales del verano y las coplas más populares en España en el año [MI_AÑO_DE_NACIMIENTO]?'."),

        ("El Botijo de Barro Blanco y el Botijo de Balcón para Enfriar el Agua",
         "Explicar a los nietos el invento ecológico perfecto que enfriaba el agua sin gastar electricidad.",
         "Primer plano con luz estival de un clásico botijo español de barro blanco o terracota clara con su pitorro fino y su boca ancha, sudando gotas microscópicas de frescor sobre una repisa o mesa a la sombra en un patio o balcón de [MI_LUGAR_PUEBLO_O_BARRIO]. Al lado, un vaso de cristal y un paño blanco. Atmósfera de descanso veraniego y serenidad doméstica.",
         "💬 Para contarle a tus nietos: Cuéntales cómo funciona el enfriamiento por evaporación del botijo: el barro 'suda' para que el agua de dentro esté helada sin enchufe. Pídele a Gemini: 'Explica de forma divertida para un niño de 8 años la física de cómo enfría el agua un botijo de barro'."),

        ("La Merienda de la Infancia: Pan con Chocolate o Pan con Aceite y Azúcar",
         "Homenajear el sabor de las meriendas humildes y deliciosas que esperábamos al salir del colegio.",
         "Fotografía cenital cálida sobre un paño de cuadros rojos y blancos, mostrando una rebanada gruesa de pan con corteza crujiente untada generosamente con aceite de oliva virgen y espolvoreada con azúcar, y al lado otra rebanada con dos onzas gruesas de chocolate negro de tableta. Sencillez, nostalgia y sabor auténtico de infancia.",
         "💬 Para contarle a tus nietos: Pregúntales cuál era la merienda estrella antes de la bollería industrial. Pídele a Gemini: 'Escribe una lista nostálgica y simpática de las 5 meriendas tradicionales españolas más populares de los años 50 y 60'."),

        ("La Bicicleta Clásica de Hierro (BH o GAC) y los Paseos de Tarde",
         "Recordar el tesoro que suponía tener una bicicleta con dinamo en la rueda para salir con los amigos.",
         "Fotografía vintage de una bicicleta clásica española de hierro negro (marca BH o GAC) con sillín de muelles de cuero marrón, bomba de inflar en el cuadro, timbre cromado y pequeño faro delantero conectado a una dinamo sobre la rueda, apoyada contra una tapia en [MI_LUGAR_PUEBLO_O_BARRIO]. Luz dorada de primavera.",
         "💬 Para contarle a tus nietos: Explícales cómo se encendía la luz pedaleando gracias a la dinamo y cómo se arreglaban los pinchazos con un parche, pegamento y una palangana de agua. Pídele a Gemini: '¿Cómo eran las míticas bicicletas BH y GAC fabricadas en España y qué significaban para un joven de la época?'."),

        ("El Quiosco de Prensa, Pipas, Regaliz de Palo y Tebeos",
         "Revivir el quiosco de la esquina donde comprábamos chicles de peseta, regaliz negro y tebeos de Bruguera.",
         "Fotografía histórica de un quiosco callejero verde de chapa en una esquina de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Mostrador repleto de tarros de cristal con chufas, pipas de girasol tostadas, regaliz de palo, y colgados de pinzas de madera ejemplares de tebeos clásicos como Mortadelo y Filemón, Zipi y Zape, TBO y Capitán Trueno. Niños mirando ilusionados con monedas en la mano.",
         "💬 Para contarle a tus nietos: Cuéntales qué personajes de cómic leías tú de pequeño y lo que costaba un tebeo en pesetas. Pídele a Gemini: '¿Cuáles fueron los tebeos y personajes de historietas más leídos en los años [MI_AÑO_O_DÉCADA] en España?'."),

        ("El Fotógrafo Ambulante con Cámara de Fuelle y Decorado",
         "Recordar el rito familiar de posar muy quietos para la foto oficial de las fiestas o de comunión.",
         "Escena histórica de época en una plaza o parque de [MI_LUGAR_PUEBLO_O_BARRIO] en [MI_AÑO_O_DÉCADA]. Un fotógrafo con boina bajo la tela negra de una gran cámara fotográfica de madera sobre trípode con fuelle plegable, retratando a una familia engalanada sentada en un banco con telón pintado de fondo. Luz natural de tarde, seriedad y dignidad en los rostros.",
         "💬 Para contarle a tus nietos: Explícales por qué en las fotos antiguas nadie sonreía con la boca abierta y había que estar 5 segundos sin pestañear. Pídele a Gemini: '¿Cómo funcionaban los fotógrafos minuteros que revelaban las fotos en la propia calle dentro del cajón de la cámara?'."),

        ("La Máquina de Coser Singer a Pedal en el Salón",
         "Evocar el sonido rítmico del pedal de hierro y las tardes de costura y arreglos de ropa en casa.",
         "Fotografía nostálgica en plano medio de una clásica máquina de coser de hierro fundido negro con filigranas doradas sobre su mueble de nogal barnizado, con la rueda de transmisión de cuero y el pedal enrejado de hierro en el suelo. Un retal de tela estampada con alfileres en el acerico y una tijera de sastre sobre la mesa. Luz dorada de ventana doméstica en [MI_LUGAR_PUEBLO_O_BARRIO].",
         "💬 Para contarle a tus nietos: Cuéntales cómo la abuela aprovechaba las camisas viejas para hacer trapos o ensanchar pantalones cuando crecíais. Pídele a Gemini: '¿Qué papel tuvieron las máquinas de coser a pedal en la economía familiar de los hogares españoles del siglo XX?'."),

        ("La Estación de Tren, el Metro o el Ferrobús de la Época",
         "Rememorar el silbato, el billete de cartón duro y la emoción de los viajes y despedidas.",
         "Fotografía histórica de época en la estación de tren o andén de metro de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Un tren clásico o vagón antiguo de madera llegando despacio al andén con maletas de piel y viajeros con abrigos saludando desde las ventanillas bajadas con correa de cuero. Atmósfera de viaje clásico y nostalgia ferroviaria.",
         "💬 Para contarle a tus nietos: Cuéntales cómo eran los billetes de cartón duro que el revisor picaba con una tenaza metálica. Pídele a Gemini: '¿Cómo era viajar en los trenes de vapor, tranvías y primeros metros en España en los años 50 y 60?'."),

        # 3. EL INVIERNO, EL HOGAR Y LA VIDA FAMILIAR (21-30)
        ("La Mesa Camilla con Brasero y Faldillas en Invierno",
         "Recordar el centro de reunión familiar en invierno donde se hacían los deberes y se jugaba al parchís o las cartas.",
         "Fotografía de interior cálida y hogareña en una casa de [MI_LUGAR_PUEBLO_O_BARRIO] en una tarde fría de invierno de los años [MI_AÑO_O_DÉCADA]. Una mesa redonda camilla vestida con pesadas faldillas de paño marrón hasta el suelo, con una baraja española y una tetera humeante encima, y varias personas sentadas con las piernas metidas bajo las faldillas calentándose. Luz tenue de lámpara de tulipa.",
         "💬 Para contarle a tus nietos: Explícales qué era la badila para remover el picón del brasero y cómo se ventilaba la habitación para evitar el dolor de cabeza. Pídele a Gemini: 'Escribe un relato entrañable sobre las tardes de invierno alrededor de la mesa camilla en un hogar español'."),

        ("La Nevera de Hielo y la Compra de Barras Heladas",
         "Mostrar cómo se conservaban los alimentos antes de que todas las casas tuvieran frigorífico eléctrico.",
         "Fotografía de época de un mueble nevera doméstico de madera barnizada con herrajes de latón y puerta gruesa aislada abierta, mostrando en su compartimento superior una gran barra transparente de hielo natural goteando sobre una bandeja de zinc, enfriando jarras de agua, mantequilla y leche en una cocina de [MI_LUGAR_PUEBLO_O_BARRIO]. Al lado, tenazas de hierro para agarrar el bloque de hielo.",
         "💬 Para contarle a tus nietos: Pregúntales cómo creen que se mantenía fresca la comida cuando no había enchufes para la nevera. Pídele a Gemini: '¿Cómo funcionaban las fábricas de hielo y las neveras de madera en los hogares españoles de mediados del siglo XX?'."),

        ("El Sereno Nocturno con su Chuzo, Farol y Manojo de Llaves",
         "Recordar la figura nocturna que abría los portales y daba la hora y el tiempo por las calles de Madrid o de pueblo.",
         "Escena nocturna atmosférica en una calle de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA], iluminada por farolas de luz cálida. Un sereno con guardapolvo gris oscuro, gorra de plato, bastón con punta de hierro (chuzo) y farolillo de aceite en la mano, abriendo la cerradura de un gran portal de madera con su pesado manojo de llaves maestras en el cinto.",
         "💬 Para contarle a tus nietos: Cuéntales cómo se llamaba al sereno dando tres palmadas fuertes en la calle desierta y gritando '¡Sereno!'. Pídele a Gemini: '¿Cuál era el trabajo de los serenos en las noches de Madrid y de las ciudades españolas y cuándo desapareció este oficio tradicional?'."),

        ("El Cartero con su Cartera de Cuero y las Cartas Manuscritas",
         "Valorar la emoción de recibir noticias lejanas escritas con pluma y sello postal tras días de espera.",
         "Fotografía histórica de un cartero con uniforme azul de Correos y cartera grande de cuero marrón cruzada al pecho, entregando un sobre de papel con matasellos y sello de correos a una vecina sonriente en la puerta de su casa o portal en [MI_LUGAR_PUEBLO_O_BARRIO]. Detrás, su bicicleta de reparto apoyada en la acera.",
         "💬 Para contarle a tus nietos: Explícales qué era el papel de carta fino de avión o las tarjetas postales que se enviaban en vacaciones. Pídele a Gemini: '¿Cuánto tardaba en llegar una carta por correo postal en España en los años 60 y cuánto costaba el sello de Correos?'."),

        ("El Cine de Barrio o de Verano en la Pared Encalada",
         "Revivir las sesiones continuas con bolsa de pipas viendo películas de aventuras o de risa.",
         "Fotografía nocturna en [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Una fachada de cine clásico con marquesina luminosa o una pared blanca al aire libre donde se proyecta una película clásica, con decenas de vecinos y niños sentados en butacas de madera o sillas de tijera comiendo pipas y refrescos bajo el haz de luz del proyector.",
         "💬 Para contarle a tus nietos: Pregúntales si se imaginan ir al cine de sesión continua donde podías quedarte a ver la película dos veces seguidas con la misma entrada. Pídele a Gemini: '¿Qué películas españolas y extranjeras triunfaban en los cines de barrio en los años [MI_AÑO_O_DÉCADA]?'."),

        ("El Día de Reyes: Juguetes de Hojalata y la Ilusión Sencilla",
         "Mostrar que con un juguete de cuerda o una muñeca se era inmensamente feliz.",
         "Fotografía vintage entrañable en la mañana del 6 de enero en un salón modesto de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Dos niños con zapatillas de paño sentados en el suelo mirando ilusionados sus regalos: un camión de bomberos de hojalata pintada con llave de cuerda, una muñeca de cartón piedra con vestido de flores y una bolsita de tela con peladillas y nueces.",
         "💬 Para contarle a tus nietos: Enséñales que la ilusión de Reyes no dependía de tener 20 regalos caros sino de la magia de estrenar un juguete de cuerda. Pídele a Gemini: '¿Cuáles eran los juguetes españoles de Reyes más famosos fabricados en Ibi (Alicante) en los años 50 y 60?'."),

        ("Los Cromos de Fútbol y Naturaleza en Álbumes de Papel",
         "Recordar el rito de comprar sobres con perras gordas o pesetas e intercambiar los 'repes' en la acera.",
         "Fotografía en primer plano de dos manos infantiles pegando con cola o saliva un cromo de papel litografiado de un futbolista de leyenda en un álbum oficial de la Liga Española de los años [MI_AÑO_O_DÉCADA]. Sobre la mesa, un montón de cromos desordenados marcados a lápiz por detrás para cambiar.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era cantar en la calle o en el patio '¡Sile, nole!' para cambiar cromos con los amigos. Pídele a Gemini: '¿Quiénes eran los futbolistas y deportistas más admirados por los niños españoles en el año [MI_AÑO_DE_NACIMIENTO]?'."),

        ("El Mercado Tradicional de Abastos: Tenderetes y Bullicio",
         "Evocar el colorido y la algarabía del mercado de abastos con pescaderías, carnicerías y puestos de frutas.",
         "Vista bulliciosa del mercado de abastos o mercado callejero de [MI_LUGAR_PUEBLO_O_BARRIO] en [MI_AÑO_O_DÉCADA]. Toldos y puestos de madera con balanzas colgantes, pescaderos pregonando la merluza fresca del día sobre hielo picado, montañas de naranjas y verduras de temporada, y vecinas con cestas de mimbre haciendo la compra de la semana.",
         "💬 Para contarle a tus nietos: Cuéntales cómo se conocía todo el mundo en el mercado y cómo los tenderos regalaban una fruta o perejil con la compra. Pídele a Gemini: '¿Cómo eran los mercados tradicionales de abastos en España a mediados del siglo XX?'."),

        ("La Llegada del Hombre a la Luna (1969) en la Televisión",
         "Compartir el recuerdo imborrable de la noche en que el mundo entero contuvo la respiración mirando al cielo.",
         "Fotografía histórica de julio de 1969 en el salón de una casa en [MI_LUGAR_PUEBLO_O_BARRIO]. Una familia reunida de madrugada alrededor del televisor en blanco y negro, con la emblemática imagen borrosa de Neil Armstrong bajando la escalerilla del módulo lunar proyectada en el tubo de rayos catódicos. Rostros de incredulidad y emoción histórica.",
         "💬 Para contarle a tus nietos: Cuéntales qué estabas haciendo tú exactamente esa noche de julio de 1969 y la voz de Jesús Hermida retransmitiendo el alunizaje. Pídele a Gemini: '¿Cómo vivió la sociedad española la retransmisión televisiva de la llegada a la Luna en julio de 1969?'."),

        ("El Tocadiscos Portátil ('Pick-up') y los Guateques Juveniles",
         "Revivir los primeros bailes en casa con discos pequeños de vinilo de 45 revoluciones con solapa de cartón.",
         "Escena juvenil festiva de un guateque en un salón de [MI_LUGAR_PUEBLO_O_BARRIO] en los años 60 o 70. En una mesa baja luce un tocadiscos portátil maleta de vinilo rojo y crema abierto girando un single pequeño de 45 rpm, con fundas de discos del Dúo Dinámico, Los Bravos o Raphael alrededor. Jóvenes con pantalones de campana charlando con vasos de refresco en la mano.",
         "💬 Para contarle a tus nietos: Enséñales qué era un guateque en casa con tortilla de patatas y discos prestados. Pídele a Gemini: '¿Qué música ye-yé y qué grupos pop españoles se bailaban en los guateques de los años 60 en España?'."),

        # 4. TRADICIONES, OFICIOS Y MEMORIA COMPARTIDA (31-40)
        ("Las Excursiones Familiares o el Día de Campo",
         "Recordar el viaje de fin de semana con la fiambrera de tortilla y el termo de café.",
         "Fotografía histórica en un merendero o pinar cercano a [MI_LUGAR_PUEBLO_O_BARRIO] en [MI_AÑO_O_DÉCADA]. Manteles extendidos sobre mesas de madera rústica, fiambreras metálicas de varios pisos abiertas con filetes empanados y tortilla de patatas, termos de café con leche y una baraja de cartas para jugar al tute o mus tras comer. Ambiente familiar feliz y relajado.",
         "💬 Para contarle a tus nietos: Cuéntales qué comida se llevaba en la fiambrera cuando no había hamburgueserías ni comida rápida. Pídele a Gemini: '¿Cómo eran los domingos de excursión campestre con fiambrera y bota de vino en la España de los años 60?'."),

        ("Los Oficios Tradicionales de la Calle: El Basurero de Carro y el Vendedor de Hielo",
         "Evocar las profesiones que recorrían las calles antes de los camiones modernos y electrodomésticos.",
         "Fotografía de época de una calle de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Un operario de limpieza con carro y escoba de ramas de brezo barriendo adoquines, mientras cruza un repartidor con carretilla de barras de hielo protegidas con sacos de arpillera. Fachadas con rótulos de cerámica vidriada.",
         "💬 Para contarle a tus nietos: Explícales cómo se recogía la basura en cubos de zinc antes de los contenedores de colores de reciclaje. Pídele a Gemini: '¿Cuáles eran los oficios callejeros más característicos que desaparecieron con la modernización de las ciudades españolas?'."),

        ("La Cocina de Carbón o de Gas Butano: El Sonido de la Bombona Naranja",
         "Rememorar la llegada de la primera bombona naranja de butano a la cocina de casa.",
         "Fotografía de época del interior de una cocina luminosa en [MI_LUGAR_PUEBLO_O_BARRIO] en los años 60. En una esquina luce una flamante bombona metálica naranja de gas butano con su alcachofa y manguera negra conectada a una cocina de esmalte blanco, con dos pucheros humeando sobre los quemadores y azulejos blancos en la pared.",
         "💬 Para contarle a tus nietos: Cuéntales cómo el repartidor de butano subía las bombonas a hombros por las escaleras avisando golpeándolas con una llave inglesa. Pídele a Gemini: '¿Cómo revolucionó el gas butano la vida de los hogares y las cocinas españolas en los años 60?'."),

        ("Las Recetas Tradicionales de la Abuela: El Guiso que Llenaba la Casa de Olor",
         "Recordar el plato estrella de la casa: cocido, potaje, lentejas o estofado a fuego lento.",
         "Bodegón gastronómico vintage en la cocina de [MI_LUGAR_PUEBLO_O_BARRIO] en [MI_AÑO_O_DÉCADA]. Una olla grande de barro o esmaltada con cocido o estofado humeante recién servido en platos hondos con cuchara de alpaca, hogaza de pan al lado y jarra de loza. Iluminación lateral cálida y apetitosa.",
         "💬 Para contarle a tus nietos: Explícales cuál era el plato especial que tu madre o abuela preparaba los domingos y que nunca has vuelto a probar igual. Pídele a Gemini: 'Escribe la receta tradicional paso a paso del plato típico de la comarca de [MI_LUGAR_PUEBLO_O_BARRIO] explicada con cariño de abuela'."),

        ("Los Domingos de Paseo Elegante por la Gran Vía, la Alameda o la Plaza",
         "Recordar la elegancia de ponerse la ropa de domingo para pasear y saludar a los conocidos.",
         "Fotografía histórica de un domingo soleado de primavera en la avenida o paseo principal de [MI_LUGAR_PUEBLO_O_BARRIO] en [MI_AÑO_O_DÉCADA]. Familias y parejas paseando despacio con abrigos impecables y sombreros, señores con traje saludando con cortesía, puestos de barquillos con ruleta giratoria en la esquina y niños vestidos de punta en blanco.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era la costumbre del paseo dominical para ver y ser visto antes de que existieran las redes sociales. Pídele a Gemini: '¿Cómo era el rito social del paseo de los domingos en España a mediados del siglo XX?'."),

        ("La Máquina de Escribir Portátil Olivetti y el Papel de Calco",
         "Mostrar a los nietos cómo se hacían copias dobles de un documento antes de que existieran las impresoras.",
         "Fotografía macro nostálgica de una clásica máquina de escribir portátil verde oliva (Olivetti Lettera) sobre una mesa, mostrando el rodillo con una hoja blanca y detrás una hoja azul brillante de papel de calco (papel carbón) para sacar copia doble. Teclas circulares mecánicas y cinta bicolor.",
         "💬 Para contarle a tus nietos: Cuéntales qué pasaba si te equivocabas de letra al final de una página entera y tenías que borrar con típex o empezar de nuevo. Pídele a Gemini: '¿Cómo funcionaba la mítica máquina Olivetti Lettera 32 y qué supuso para escritores y estudiantes en España?'."),

        ("La Cabina Telefónica Pública y las Monedas de Cinco Duros",
         "Rememorar la aventura de meter monedas por la ranura para hablar con los parientes lejanos.",
         "Fotografía de época de una clásica cabina telefónica de cristal y aluminio en una calle española en los años 70 u 80. En el interior se aprecia el icónico teléfono de disco giratorio con ranura superior de monedas, y una persona esperando con una moneda de 25 pesetas (cinco duros) con agujero en la mano mientras caen los pitidos de aviso de saldo.",
         "💬 Para contarle a tus nietos: Pregúntales cómo harían para llamar a su madre en la calle si no existieran los teléfonos móviles. Pídele a Gemini: '¿Cómo funcionaban las cabinas de teléfono públicas de España y cuándo se instaló la primera cabina?'."),

        ("El Zapatero Remendón con su Lezna y su Banqueta Baja",
         "Recordar cómo se reparaban las suelas de cuero y se ponían tapas de goma para no gastar zapatos.",
         "Fotografía de época del pequeño taller de un zapatero artesano en [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. El maestro zapatero sentado en su banqueta baja de madera con mandil de cuero, sujetando un zapato en una horma metálica de tres brazos mientras clava tachuelas con un martillo corto. Estanterías con pieles, leznas y botes de cola.",
         "💬 Para contarle a tus nietos: Explícales que antes los zapatos duraban diez años porque se cambiaban las suelas una y otra vez. Pídele a Gemini: '¿Cómo era el oficio de zapatero remendón y qué herramientas tradicionales utilizaba?'."),

        ("Los Refranes y Dichos Populares de Mi Tierra",
         "Transmitir a los nietos la sabiduría popular sobre el tiempo, el trabajo y las personas.",
         "Ilustración clásica con aire de grabado botánico cálido, representando un cielo con nubes algodonosas sobre los tejados y chimeneas de [MI_LUGAR_PUEBLO_O_BARRIO], con golondrinas volando bajo y un caracol sobre una hoja húmeda. Tipografía en pergamino que evoca sabiduría popular.",
         "💬 Para contarle a tus nietos: Enséñales tres refranes de tu tierra que sigan teniendo vigencia hoy. Pídele a Gemini: 'Dime 5 refranes tradicionales españoles sobre el clima y la vida cotidiana (como 'En abril, aguas mil') y explícame la base científica o sociológica que tenían'."),

        ("El Regalo de Cumpleaños Hecho a Mano con Cariño",
         "Recordar que el mejor regalo de la infancia era un jersey tejido por la madre o un juguete de madera.",
         "Fotografía íntima de una mesa rústica donde descansa un jersey infantil de lana virgen tejido a dos agujas con ochos, envuelto con un cordel de cáñamo y una ramita aromática, junto a una figura de juguete tallada a navaja. Calidez, dedicación y afecto artesano en [MI_LUGAR_PUEBLO_O_BARRIO].",
         "💬 Para contarle a tus nietos: Cuéntales cómo era recibir un regalo que alguien había pasado semanas haciendo con sus propias manos para ti. Pídele a Gemini: 'Escribe una reflexión emotiva sobre el valor del tiempo y las cosas hechas a mano en la época de nuestros abuelos'."),

        # 5. OBJETOS, CANCIONES Y SABORES OLVIDADOS (41-50)
        ("El Botiquín Tradicional: Agua Oxigenada, Mercromina y Manzanilla",
         "Evocar los remedios caseros que nos curaban las raspaduras de las rodillas tras caernos en la calle.",
         "Fotografía de primer plano de un estante de botiquín casero de madera en los años [MI_AÑO_O_DÉCADA], mostrando un bote de cristal de agua oxigenada con tapón de corcho, el icónico frasco de Mercromina roja con su aplicador de cristal, una caja metálica de tiritas de tela rosa y un frasco con flores secas de manzanilla silvestre.",
         "💬 Para contarle a tus nietos: Cuéntales por qué todos los niños llevaban las rodillas y los codos pintados de rojo brillante de Mercromina todo el verano. Pídele a Gemini: '¿Cuáles eran los remedios caseros y de farmacia más populares en los hogares españoles de los años 50 y 60?'."),

        ("El Arreglo y Blanqueo de las Casas en Primavera",
         "Recordar la tradición de pintar y poner a punto balcones y fachadas antes de que llegara el calor.",
         "Escena luminosa en una calle de [MI_LUGAR_PUEBLO_O_BARRIO] en primavera en [MI_AÑO_O_DÉCADA]. Un vecino aplicando cal o pintura blanca sobre la fachada, dejando la pared deslumbrante de blancura bajo un cielo azul intenso, con macetas de geranios rojos y gitanillas listas para ser colgadas de los balcones de forja.",
         "💬 Para contarle a tus nietos: Explícales por qué se pintaban las casas de blanco puro: para rebotar el calor del sol en verano y desinfectar. Pídele a Gemini: '¿Por qué el blanco de cal era el sello de identidad arquitectónico de las casas españolas en verano?'."),

        ("El Vaso de Leche con Galletas María y el Cola Cao",
         "Homenajear el desayuno de toda una vida y el bote metálico con litografías que se guardaba para hilos.",
         "Fotografía cenital vintage de un desayuno de la época: un vaso grueso de cristal con leche caliente con los característicos grumos flotantes de cacao en polvo, un plato con galletas María doradas con su dibujo grabado alrededor y al fondo la icónica lata cilíndrica metálica decorada de Cola Cao. Nostalgia pura y recuerdos de infancia.",
         "💬 Para contarle a tus nietos: Cuéntales cómo se deshacían las galletas María en la leche hasta formar una papilla deliciosa. Pídele a Gemini: '¿Cuándo nació el Cola Cao en España y cómo eran las primeras latas de hojalata que usaban las abuelas como costurero?'."),

        ("Los Patinetes Caseros con Rodamientos de Bolas y Tablas",
         "Mostrar cómo nos fabricábamos nuestros propios bólidos con maderas de desecho y cojinetes de camión.",
         "Fotografía de época de un niño sonriente en una calle en cuesta de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA] junto a un carricoche artesanal hecho a mano con dos tablas de madera clavadas, un manillar con dos empuñaduras y tres rodamientos de bolas de acero pulido como ruedas. Fondo urbano o rural de época.",
         "💬 Para contarle a tus nietos: Pregúntales si saben el ruido ensordecedor y divertido que hacían los rodamientos de hierro sobre el asfalto o la acera. Pídele a Gemini: '¿Cómo construían los niños de los años 60 sus propios patinetes y carretones de rodamientos?'."),

        ("Las Canciones Populares del Corro y la Comba",
         "Rescatar del olvido las melodías que cantaban las niñas y niños cogidos de la mano en la calle.",
         "Ilustración vintage luminosa de un grupo de niñas con vestidos de flores y calcetines cortos cogidas de la mano formando un corro circular en una plaza de [MI_LUGAR_PUEBLO_O_BARRIO], girando sonrientes bajo los árboles en una tarde dorada de primavera. Flores silvestres y atmósfera de alegría pura.",
         "💬 Para contarle a tus nietos: Cántales dos estrofas de 'El patio de mi casa' o 'Al corro de la patata' y mira si se la saben en el colegio. Pídele a Gemini: 'Escríbeme la letra completa y el origen histórico de 3 canciones tradicionales de corro infantiles en España'."),

        ("El Primer Viaje en Autobús de Línea o en Metro",
         "Recordar la impresión de ver por primera vez las avenidas bulliciosas, los semáforos y los escaparates grandes.",
         "Fotografía histórica de un autobús comarcal o tranvía urbano antiguo de morro redondo en [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Pasajeros bajando abrigados mirando asombrados los rótulos luminosos de neón y el ajetreo de la gran ciudad.",
         "💬 Para contarle a tus nietos: Cuéntales qué sentiste la primera vez que viste un edificio de 10 plantas o una escalera mecánica. Pídele a Gemini: '¿Cómo eran los autobuses y tranvías de los años 50 y 60 en las calles de España?'."),

        ("El Huerto Familiar o las Plantas de la Terraza y Balcón",
         "Transmitir a los nietos el olor a mata de tomate verde o el cuidado diario de los geranios y albahaca.",
         "Fotografía en plano medio de un abuelo con azada o regadera de zinc junto a su nieto en una huerta fértil o en una terraza soleada llena de macetas en [MI_LUGAR_PUEBLO_O_BARRIO], entregándole un gran tomate rojo carnoso o cuidando un esqueje. Riego fresco y sol brillante.",
         "💬 Para contarle a tus nietos: Explícales la diferencia abismal entre un tomate criado al sol y uno industrial de supermercado. Pídele a Gemini: '¿Cuáles son las variedades tradicionales de verduras y flores más cultivadas en los huertos y balcones españoles?'."),

        ("La Zapatilla de Paño y la Alpargata Tradicional",
         "Recordar el calzado cómodo de estar en casa y de trabajar que hacían los artesanos zapateros.",
         "Bodegón vintage con dos pares de calzado tradicional sobre suelo de baldosas de barro o terrazo: unas alpargatas de lona con suela trenzada de cáñamo atadas con cintas negras, y unas zapatillas de paño caliente a cuadros con forro de borreguito interior.",
         "💬 Para contarle a tus nietos: Enséñales cómo la alpargata humilde de cáñamo ha pasado a estar en las tiendas de moda de todo el mundo. Pídele a Gemini: '¿Cuál es la historia artesana de la alpargata en España y cómo se fabrica su suela trenzada?'."),

        ("Las Primeras Monedas: La Peseta Rubia, el Duro y el Billete de Mil",
         "Explicar a los nietos la moneda con la que creciste antes de que llegara el euro.",
         "Fotografía macro en alta resolución sobre una mesa de madera de varias monedas históricas españolas de los años [MI_AÑO_O_DÉCADA]: la moneda rubia de una peseta con el escudo, la moneda grande de 5 pesetas (el duro), la moneda de 25 pesetas con el agujero en el centro y un billete verde de 1.000 pesetas.",
         "💬 Para contarle a tus nietos: Pregúntales si saben cuántos céntimos de euro eran un 'duro' y lo que podías comprar de chuches con una peseta rubia. Pídele a Gemini: 'Hazme una tabla divertida de equivalencias: ¿qué podías comprar con 1 peseta, con 5 pesetas y con 100 pesetas en los años [MI_AÑO_O_DÉCADA]?'."),

        ("Las Infusiones y Tisanas Caseras: Manzanilla, Tila y Poleo",
         "Homenajear el saber de las madres y abuelas que sabían qué infusión preparar para cada malestar.",
         "Fotografía botánica cálida en un rincón de cocina de [MI_LUGAR_PUEBLO_O_BARRIO], con manojos de plantas secándose boca abajo: tila, poleo menta y manzanilla en flor, junto a una taza de porcelana humeante y tarros de cristal con tisanas.",
         "💬 Para contarle a tus nietos: Enséñales a reconocer el olor de la manzanilla o de la tila y cuéntales qué te daban en casa cuando te dolía la tripa. Pídele a Gemini: '¿Cuáles eran las 5 infusiones medicinales caseras más usadas tradicionalmente en los hogares españoles?'."),

        # 6. EL LEGADO VIVO Y EL FUTURO DE LA FAMILIA (51-60)
        ("El Mapa Sentimental de Mi Infancia: Calles, Plazas y Esquinas Míticas",
         "Enseñar a los nietos los rincones que marcaron tu vida: la cuesta del colegio, el cine viejo y la plazoleta.",
         "Mapa antiguo ilustrado con acuarela y tinta que recrea el callejero o término municipal de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA], señalando con dibujos entrañables la escuela, la iglesia o parroquia, el parque, la fuente, los ultramarinos y las casas de los amigos de infancia.",
         "💬 Para contarle a tus nietos: Cuéntales por qué cada esquina tenía una historia que no sale en Google Maps. Pídele a Gemini: 'Escribe una dedicatoria emotiva de un abuelo para su nieto transmitiéndole el amor por las calles y raíces donde creció su familia'."),

        ("Las Noches de Verano al Fresco y las Historias Familiares",
         "Rememorar la tertulia en la puerta de casa o en la terraza sacando las sillas para tomar el fresco por la noche.",
         "Fotografía histórica nostálgica de una noche de verano en [MI_LUGAR_PUEBLO_O_BARRIO]. Vecinos y familiares sentados en sillas de anea o tijera en la acera o portal charlando amigablemente bajo la brisa nocturna, mientras los niños juegan cerca bajo las farolas. Cielo estrellado y serenidad vecinal.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era la costumbre de 'tomar el fresco' en la calle charlando con los vecinos hasta la medianoche en verano. Pídele a Gemini: '¿Por qué la costumbre de tomar el fresco en la calle era el gran pegamento social de los barrios y pueblos españoles?'."),

        ("El Primer Empleo y el Orgullo del Esfuerzo",
         "Compartir con los nietos el valor del trabajo honrado y la emoción del primer sobre de nómina.",
         "Fotografía histórica de un joven o muchacha en [MI_LUGAR_PUEBLO_O_BARRIO] en los años 60 o 70, con ropa modesta y mirada orgullosa sosteniendo su primer sobre marrón de nómina o su carnet de aprendiz o estudiante. Fondo de taller, oficina clásica o comercio de la época.",
         "💬 Para contarle a tus nietos: Cuéntales qué hiciste tú con tu primer sueldo y qué regalo le compraste a tu madre con tus primeros ahorros. Pídele a Gemini: '¿Cómo eran las condiciones y el valor del primer empleo para los jóvenes en España en los años [MI_AÑO_O_DÉCADA]?'."),

        ("Las Fuentes Públicas y el Rito del Agua Fresca",
         "Recordar cuando no había botellas de plástico y se bebía directamente del caño de hierro o piedra.",
         "Fotografía histórica de una fuente monumental o caño de hierro público en [MI_LUGAR_PUEBLO_O_BARRIO] en [MI_AÑO_O_DÉCADA]. Niños bebiendo agua fresca apoyando la palma en el caño para dirigir el chorro, con vecinos llenando jarras o cántaros bajo la sombra de los plátanos de paseo.",
         "💬 Para contarle a tus nietos: Pregúntales si saben cómo se bebía en una fuente pública tapando medio caño con el dedo para que el chorro saliera hacia arriba. Pídele a Gemini: '¿Cómo eran las fuentes públicas históricas de ciudades como Madrid y los pueblos de España?'."),

        ("El Valor del Esfuerzo y los Estudios en Familia",
         "Recordar el sacrificio familiar para que los hijos y nietos pudieran estudiar y tener una vida mejor.",
         "Fotografía de época de un joven estudiando por la noche bajo la luz de un flexo de metal sobre una mesa con libros gruesos y libretas manuscritas, con su madre o padre trayéndole un vaso de leche caliente con cariño en [MI_LUGAR_PUEBLO_O_BARRIO]. Atmósfera de esfuerzo y amor familiar.",
         "💬 Para contarle a tus nietos: Cuéntales el orgullo que sintieron tus padres cuando terminaste tus estudios o conseguiste tu profesión. Pídele a Gemini: '¿Cómo fue la gran transformación educativa y social de la juventud española en los años 60 y 70?'."),

        ("Las Grandes Nevadas de Invierno: Muñecos de Nieve en la Calle",
         "Recordar cuando las nevadas cubrían los tejados y se bajaban las cuestas con plásticos o trineos caseros.",
         "Fotografía de época de [MI_LUGAR_PUEBLO_O_BARRIO] completamente cubierto por un gran manto blanco de nieve en invierno en los años [MI_AÑO_O_DÉCADA]. Calles silenciosas con muñecos de nieve con bufandas de lana y ojos de carbón, niños tirándose bolas de nieve sonrientes y abrigos de pana.",
         "💬 Para contarle a tus nietos: Cuéntales cómo os tirabais por las cuestas nevadas montados en un trozo de plástico o saco a toda velocidad. Pídele a Gemini: '¿Cuáles fueron las nevadas históricas más recordadas en Madrid y en España a mediados del siglo XX?'."),

        ("La Música que Marcó Mi Juventud: De la Copla al Pop Español",
         "Revivir la magia de la radio y los primeros tocadiscos con los artistas que te hacían soñar.",
         "Bodegón con luz cálida de un tocadiscos de los años 60 o 70, con la aguja apoyándose en el surco de un vinilo y fundas de discos clásicos españoles de la época sobre una mesa de madera en [MI_LUGAR_PUEBLO_O_BARRIO]. Atmósfera musical entrañable.",
         "💬 Para contarle a tus nietos: Diles cuál fue tu cantante o grupo favorito de juventud y poned juntos esa canción en el móvil en YouTube para que vean lo bien que se cantaba. Pídele a Gemini: 'Dime los 5 cantantes y canciones más escuchadas en España en el año en que yo cumplí 15 años'."),

        ("Las Celebraciones Familiares: El Banquete y la Alegría Sencilla",
         "Recordar cómo se celebraban las bodas y bautizos con churros, embutido, baile y abrazos sinceros.",
         "Fotografía de época de una celebración familiar en un patio o salón de [MI_LUGAR_PUEBLO_O_BARRIO] en los años [MI_AÑO_O_DÉCADA]. Familias reunidas alrededor de mesas largas con platos de jamón, queso, aceitunas y jarras de sangría o sidra, brindando con alegría y niños corriendo alrededor. Felicidad auténtica y cercana.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era una fiesta familiar donde no había lujos pero sobraba el cariño y las risas. Pídele a Gemini: '¿Cómo eran los banquetes y fiestas familiares en los barrios y pueblos españoles a mediados del siglo XX?'."),

        ("El Tesoro del Habla Popular: Modismos y Giros de Mi Tierra",
         "Recopilar las palabras castizas, modismos y dichos que solo se decían en tu ciudad o comarca.",
         "Ilustración clásica estilo grabado rústico mostrando un libro antiguo abierto donde se aprecian palabras castizas, giros populares y chascarrillos tradicionales de [MI_LUGAR_PUEBLO_O_BARRIO], con unas gafas de montura redonda descansando sobre las páginas amarillentas.",
         "💬 Para contarle a tus nietos: Enséñales 3 palabras castizas o expresiones de tu época que ellos no usan y pregúntales qué creen que significan. Pídele a Gemini: 'Hazme una lista de 5 expresiones castizas y modismos entrañables de [MI_LUGAR_PUEBLO_O_BARRIO] con su significado y origen'."),

        ("La Carta al Futuro: El Legado de un Abuelo para sus Nietos",
         "Dejar un mensaje imborrable de amor, experiencia y raíces que los nietos guardarán toda la vida.",
         "Fotografía cálida y emotiva en primer plano de las manos sabias de un abuelo o abuela sosteniendo con ternura las manos jóvenes de su nieto sobre una carta manuscrita, con un reloj clásico de bolsillo sobre la mesa. Luz dorada de atardecer, complicidad infinita y amor familiar.",
         "💬 Para contarle a tus nietos: Este es el broche de oro de tu curso. Pídele a Gemini: 'Ayúdame a redactar una carta conmovedora y llena de sabiduría de un abuelo para su nieto, recordándole de dónde viene su familia, los valores que le han guiado en la vida y el amor incondicional que siempre le tendrá'." )
    ]

    for idx, (title, concept, prompt_pc, prompt_tips) in enumerate(temas, 1):
        memoria_list.append({
            "block_dir": "13. [MEM] BLOQUE_13_CAPSULA_DE_LA_MEMORIA",
            "block_name": "BLOQUE 13: CÁPSULA DE LA MEMORIA [MEM]",
            "id_code": f"[MEM-{idx:03d}]",
            "title": title,
            "concept": concept,
            "prompt": prompt_pc,
            "tips": prompt_tips
        })

    return memoria_list

if __name__ == "__main__":
    items = get_memoria_items()
    print(f"Total ítems MEMORIA generados: {len(items)}")
    print(f"Muestra ítem 1: {items[0]['title']}")
    print(f"Tips ítem 1: {items[0]['tips']}")
