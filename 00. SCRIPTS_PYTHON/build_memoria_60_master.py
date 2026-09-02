# -*- coding: utf-8 -*-
"""
Generador Maestro del Bloque 13: [MEM] CÁPSULA DE LA MEMORIA: MI PUEBLO Y MI INFANCIA (60 Ítems)
Propósito: Conectar a los abuelos con sus nietos mediante la recreación visual y narrativa de su infancia,
su pueblo natal, precios de su época, inventos cotidianos y chascarrillos entrañables.
REGLA ESTRICTA: 0% alusiones a la Guerra Civil o política. Enfoque 100% costumbrista, familiar y positivo.
"""

def get_memoria_items():
    memoria_list = []

    temas = [
        # 1. LA CALLE Y LOS JUEGOS DE INFANCIA (01-10)
        ("La Plaza del Pueblo y los Juegos de Calle: La Peonza y las Canicas",
         "Recrear la plaza del pueblo en la infancia y recordar cómo se jugaba al aire libre sin pantallas.",
         "Recrea una fotografía histórica de alta calidad en color sepia suave o blanco y negro cálido de la plaza mayor de [MI_PUEBLO] en el año [MI_AÑO_O_DÉCADA]. Muestra una calle de adoquines y tierra sin coches modernos, con niños con pantalones cortos y boina jugando agachados a las canicas de barro y bailando la peonza de madera con cuerda. Al fondo, casas tradicionales encaladas con rejas de forja y la torre de la iglesia. Atmósfera entrañable, nostálgica y llena de vida, sin textos en inglés.",
         "💬 Para contarle a tus nietos: Enséñales esta imagen y pregúntales: '¿Sabéis cómo hacíamos girar una peonza con una cuerda de cáñamo?'. Pídele a Gemini a continuación: 'Dime 3 cosas cotidianas que ocurrieron en España en el año [MI_AÑO_DE_NACIMIENTO], cuánto costaba una barra de pan en pesetas y qué invento llegó a los hogares españoles esa década. Sin temas de guerra ni política'."),

        ("El Lavadero Comunal y el Sonido del Agua de la Fuente",
         "Recordar el punto neurálgico del pueblo donde se lavaba a mano con jabón casero de sosa y aceite.",
         "Fotografía histórica de época en tonos sepia cálidos mostrando el lavadero público cubierto de piedra en [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. Mujeres del pueblo lavando sábanas blancas y ropa en las pilas de piedra inclinadas con pastillas de jabón casero, con cestas de mimbre en el suelo y charlando animadamente bajo el tejado de vigas de madera. Luz de mañana entrando entre las columnas de piedra, nítido y costumbrista.",
         "💬 Para contarle a tus nietos: Explícales cómo se hacía el jabón con restos de aceite y sosa cáustica sin gastar dinero. Pídele a Gemini: 'Escribe un relato corto de dos párrafos en tono de abuelo contando a su nieto cómo era el día de colada en el pueblo y las canciones que se cantaban junto al pilón'."),

        ("La Escuela Rural: Pupitres de Madera Dobles y el Tintero",
         "Mostrar a los nietos cómo eran las aulas de la época con pizarra de tiza, mapas de tela y tintero de porcelana.",
         "Fotografía nostálgica de época de un aula de escuela de pueblo español en [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. Pupitres dobles de madera barnizada con su agujero para el tintero blanco de cerámica, una gran pizarra negra en la pared con cuentas escritas con tiza, una estufa de hierro fundido en una esquina y un mapa físico de España de tela enrollable. Niños sentados escuchando con atención, atmósfera luminosa y respetuosa.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era escribir con plumilla metálica mojada en tinta y lo que pasaba si caía un borrón en el cuaderno. Pídele a Gemini: '¿Qué asignaturas y libros de texto clásicos (como la Enciclopedia Álvarez) estudiaban los niños en España en los años [MI_AÑO_O_DÉCADA]?'."),

        ("La Tienda de Ultramarinos: Sacos de Legumbres y Balanza de Pesas",
         "Revivir los ultramarinos de barrio donde todo se vendía a granel en cucuruchos de papel de estraza.",
         "Fotografía de época del interior de una tienda de ultramarinos y coloniales de pueblo en [MI_PUEBLO] en [MI_AÑO_O_DÉCADA]. Mostrador largo de madera con una gran balanza de dos platos de latón dorado con pesas cilíndricas, sacos de arpillera abiertos en el suelo rebosantes de garbanzos, lentejas y alubias, latas de membrillo apiladas y frascos de cristal con caramelos. El tendero con bata gris y lápiz en la oreja despachando con simpatía.",
         "💬 Para contarle a tus nietos: Enséñales que antes no había bolsas de plástico y todo iba en cartuchos de papel de estraza. Pregúntale a Gemini: '¿Cuánto costaba un cuarto de kilo de café o un litro de aceite en pesetas en España en los años 50 o 60?'."),

        ("El Primer Televisor del Pueblo en el Bar o Centro Parroquial",
         "Recordar el acontecimiento comunitario de reunirse todos los vecinos para ver la televisión en blanco y negro.",
         "Escena costumbrista histórica en blanco y negro en el bar o centro social de [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. Una pequeña televisión de válvulas en blanco y negro colocada en una peana alta de madera en la pared, con decenas de vecinos mayores y niños sentados en sillas de anea o de pie fascinados mirando la pantalla iluminada, con un porrón de vino y vasos sobre la mesa. Emoción y asombro comunitario.",
         "💬 Para contarle a tus nietos: Pregúntales si se imaginan un mundo con un solo canal de tele que empezaba por la tarde y donde toda la calle iba al mismo salón a verla. Pídele a Gemini: '¿Qué programas míticos de Televisión Española veían las familias españolas en los años 60?'."),

        ("Juegos Tradicionales: La Rayuela, las Chapas de Refresco y la Comba",
         "Transmitir a los nietos las reglas de los juegos que no necesitaban pilas ni electricidad.",
         "Fotografía histórica de unos niños sonrientes en una calle empedrada de [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. En el suelo de tierra hay dibujada con yeso blanco una rayuela numerada del 1 al 10 y un circuito de carreras de chapas aplastadas con fotos de ciclistas pegadas dentro. Dos niñas al lado saltan a la comba con alegría bajo la luz dorada de la tarde. Imagen limpia y llena de energía infantil sana.",
         "💬 Para contarle a tus nietos: Enséñales cómo se rellenaban las chapas de refresco con cera o plastilina y se ponían fotos de Bahamontes o Poblet. Pídele a Gemini: 'Escríbeme las reglas sencillas y divertidas del juego de las chapas para enseñárselo a jugar a mi nieto este fin de semana'."),

        ("La Siega y la Trilla en la Era: El Trillo y los Caballos",
         "Explicar el trabajo colectivo del campo en verano y el olor a paja dorada bajo el sol.",
         "Fotografía histórica panorámica en tonos cálidos de la era de [MI_PUEBLO] en pleno verano durante los años [MI_AÑO_O_DÉCADA]. Un campesino de pie sobre un trillo tradicional de madera con piedras de pedernal incrustadas, tirado por dos mulas o bueyes en círculo sobre el montón dorado de trigo. Familias con sombreros de paja aventando con horcas de madera la paja al viento para separar el grano. Realismo rural entrañable.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era subirse de niño al trillo para hacer peso mientras daban vueltas y el sabor del agua fresca del botijo tras una tarde de calor. Pídele a Gemini: '¿Cómo funcionaba la trilla tradicional en los pueblos de España antes de que llegaran las cosechadoras modernas?'."),

        ("El Seat 600 y las Primeras Vacaciones Familiares",
         "Revivir las míticas salidas a la playa o al pueblo con el coche familiar cargado hasta los topes.",
         "Fotografía vintage en color de los años 60 o 70 de un flamante Seat 600 blanco o verde claro aparcado a la entrada de [MI_PUEBLO]. En la baca del techo lleva una enorme pila de maletas de cartón atadas con cuerdas, y una familia sonriente de tres generaciones junto a él merendando tortilla de patatas en una mesa plegable de camping a la orilla de una carretera comarcal con chopos. Nostalgia y alegría vacacional.",
         "💬 Para contarle a tus nietos: Pregúntales cuántos cabían en un 600 sin aire acondicionado y sin GPS cantando canciones en el camino. Pídele a Gemini: '¿Qué significó la llegada del Seat 600 para las familias españolas en los años 60 y cuánto costaba comprar uno?'."),

        ("La Radio de Válvulas y las Radionovelas de la Tarde",
         "Recordar cómo se reunía la familia alrededor del receptor de madera para escuchar historias.",
         "Escena íntima de hogar español en los años [MI_AÑO_O_DÉCADA]. Sobre una mesita con tapete de ganchillo blanco luce una radio grande de madera barnizada con dial luminoso de cristal verde y ojo mágico, con dos perillas doradas. Una abuela haciendo calceta y un abuelo leyendo el periódico escuchan con atención la emisión mientras una suave luz entra por la ventana. Ambiente hogareño cálido y sereno.",
         "💬 Para contarle a tus nietos: Explícales que antes de las series de Netflix o las películas en el móvil, la gente se imaginaba las historias con la voz de actores de radio. Pídele a Gemini: '¿Cuáles fueron las radionovelas y los seriales radiofónicos más famosos de la Cadena SER en los años 50 y 60?'."),

        ("La Panadería del Pueblo y el Pan de Horno de Leña",
         "Evocar el olor inolvidable del pan recién cocido con harina de trigo candeal y leña de encina.",
         "Fotografía histórica del interior del horno de pan tradicional de [MI_PUEBLO] en [MI_AÑO_O_DÉCADA]. La boca de piedra del horno de leña con rescoldos rojos al fondo, el panadero con pala larga de madera sacando hogazas redondas doradas y crujientes con harina blanca en la corteza, y estanterías de tablas de madera repletas de panes y tortas de aceite recién hechas. Vaho caliente y atmósfera rústica auténtica.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era ir a por el pan de buena mañana y pellizcar el cuscurro caliente de camino a casa. Pídele a Gemini: '¿Cómo se elaboraba el pan de pueblo tradicional con masa madre y horno de leña en España?'."),

        # 2. OFICIOS, COSTUMBRES Y SONIDOS DEL PUEBLO (11-20)
        ("El Afilador con su Chiflo y su Bicicleta de Rueda de Piedra",
         "Recordar la melodía inconfundible de la flauta de pan del afilador que resonaba por todas las calles.",
         "Fotografía de calle histórica de un afilador ambulante en [MI_PUEBLO] en [MI_AÑO_O_DÉCADA]. El afilador vestido con chaleco de pana accionando el pedal de su bicicleta modificada con esmeril de piedra circular, sacando chispas brillantes mientras afila un cuchillo de cocina. Varios vecinos esperando con tijeras en la mano y niños alrededor asombrados con la escala de notas de su chiflo de madera.",
         "💬 Para contarle a tus nietos: Pregúntales si saben cómo sonaba la melodía del afilador. Pídele a Gemini: '¿Cuál era el origen de los afiladores tradicionales gallegos que recorrían toda España y qué instrumentos usaban?'."),

        ("El Lechero y las Cántaras de Aluminio de Puerta en Puerta",
         "Rememorar el reparto matinal de leche fresca recién ordeñada que luego había que hervir en la cocina.",
         "Escena histórica de primera hora de la mañana en una calle empedrada de [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. El lechero repartidor con boina y carro de madera con dos grandes cántaras metálicas de aluminio brillante con asa, sirviendo leche fresca con un cazo dosificador de medio litro en la lechera esmaltada blanca y azul que sostiene una vecina sonriente en el zaguán de su casa.",
         "💬 Para contarle a tus nietos: Explícales por qué había que hervir la leche tres veces en el cazo para que subiera la nata y lo rica que estaba esa nata con un poco de azúcar. Pídele a Gemini: '¿Cómo era el oficio tradicional del lechero antes del envasado en tetrabrik?'."),

        ("Las Fiestas Patronales: El Baile de la Plaza y la Orquesta",
         "Revivir la emoción anual del pregón, las bombillas de colores y el pasodoble con orquesta.",
         "Fotografía festiva de noche de verbena en la plaza de [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. Guirnaldas de bombillas de colores encendidas cruzando el cielo estrellado, un entarimado de madera con una orquesta tocando trompetas y acordeones, y parejas de jóvenes y mayores bailando pasodobles y coplas con sus mejores trajes de fiesta. Clima alegre, romántico y festivo.",
         "💬 Para contarle a tus nietos: Enséñales qué canciones sonaban en el baile del pueblo en tus tiempos. Pídele a Gemini: '¿Cuáles fueron los mayores éxitos musicales del verano en España en el año [MI_AÑO_DE_NACIMIENTO]?'."),

        ("El Botijo de Barro Blanco a la Sombra de la Higuera",
         "Explicar a los nietos el invento ecológico perfecto que enfriaba el agua sin gastar electricidad.",
         "Primer plano con luz estival de un clásico botijo español de barro blanco o terracota clara con su pitorro fino y su boca ancha, sudando gotas microscópicas de frescor sobre una mesa de madera a la sombra de una higuera en un patio de [MI_PUEBLO]. Al lado, un racimo de uvas y un paño blanco. Atmósfera de descanso veraniego y serenidad campestre.",
         "💬 Para contarle a tus nietos: Cuéntales cómo funciona el enfriamiento por evaporación del botijo: el barro 'suda' para que el agua de dentro esté helada sin enchufe. Pídele a Gemini: 'Explica de forma divertida para un niño de 8 años la física de cómo enfría el agua un botijo de barro'."),

        ("La Merienda de la Infancia: Pan con Chocolate o Pan con Aceite y Azúcar",
         "Homenajear el sabor de las meriendas humildes y deliciosas que esperábamos al salir del colegio.",
         "Fotografía cenital cálida sobre un paño de cocina de cuadros rojos y blancos, mostrando una rebanada gruesa de pan de pueblo con corteza crujiente untada generosamente con aceite de oliva virgen y espolvoreada con azúcar moreno, y al lado otra rebanada con dos onzas gruesas de chocolate negro de tableta. Sencillez, nostalgia y sabor auténtico.",
         "💬 Para contarle a tus nietos: Pregúntales cuál era la merienda estrella antes de la bollería industrial. Pídele a Gemini: 'Escribe una lista nostálgica y simpática de las 5 meriendas tradicionales españolas más populares de los años 50 y 60'."),

        ("La Bicicleta de Paseo (BH o GAC) y los Caminos de Tierra",
         "Recordar el tesoro que suponía tener una bicicleta con dinamo en la rueda para ir al río o a la era.",
         "Fotografía vintage de una bicicleta clásica española de hierro negro (marca BH o GAC) con sillín de muelles de cuero marrón, bomba de inflar en el cuadro, timbre cromado y pequeño foco delantero conectado a una dinamo sobre la rueda delantera, apoyada contra una tapia de piedra en [MI_PUEBLO]. Fondo de campos verdes de trigo en primavera.",
         "💬 Para contarle a tus nietos: Explícales cómo se encendía la luz pedaleando gracias a la dinamo y cómo se arreglaban los pinchazos con un parche, pegamento y una palangana de agua. Pídele a Gemini: '¿Cómo eran las míticas bicicletas BH fabricadas en España y qué significaban para un joven de la época?'."),

        ("El Quiosco de Pipas, Regaliz de Palo y Tebeos",
         "Revivir el puesto callejero donde comprábamos chicles de peseta, regaliz negro y los tebeos de Bruguera.",
         "Fotografía histórica de un quiosco callejero verde de chapa en [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. Mostrador repleto de tarros de cristal con chufas, pipas de girasol tostadas, regaliz de palo de raíz, y colgados de pinzas de madera ejemplares de tebeos clásicos como Mortadelo y Filemón, Zipi y Zape, TBO y Capitán Trueno. Niños mirando ilusionados con monedas en la mano.",
         "💬 Para contarle a tus nietos: Cuéntales qué personajes de cómic leías tú de pequeño y lo que costaba un tebeo. Pídele a Gemini: '¿Cuáles fueron los tebeos y personajes de historietas más leídos en los años [MI_AÑO_O_DÉCADA] en España?'."),

        ("El Fotógrafo Ambulante con Cámara de Fuelle y Decorado",
         "Recordar el rito familiar de posar muy quietos para la foto oficial de las fiestas o de comunión.",
         "Escena histórica de época en una esquina de la plaza de [MI_PUEBLO] en [MI_AÑO_O_DÉCADA]. Un fotógrafo con boina bajo la tela negra de una gran cámara fotográfica de madera sobre trípode con fuelle plegable, retratando a una familia engalanada sentada en un banco con telón de fondo pintado con un paisaje romántico. Luz natural de tarde, seriedad y dignidad en los rostros.",
         "💬 Para contarle a tus nietos: Explícales por qué en las fotos antiguas nadie sonreía con la boca abierta y había que estar 5 segundos sin pestañear. Pídele a Gemini: '¿Cómo funcionaban los fotógrafos minuteros que revelaban las fotos en la propia plaza dentro del cajón de la cámara?'."),

        ("La Máquina de Coser Singer a Pedal en el Salón",
         "Evocar el sonido rítmico del pedal de hierro y las tardes de costura y arreglos de ropa en casa.",
         "Fotografía nostálgica en plano medio de una clásica máquina de coser de hierro fundido negro con filigranas doradas sobre su mueble de nogal barnizado, con la rueda de transmisión de cuero y el pedal enrejado de hierro en el suelo. Un retal de tela estampada con alfileres en el acerico y una tijera de sastre sobre la mesa. Luz dorada de ventana doméstica.",
         "💬 Para contarle a tus nietos: Cuéntales cómo la abuela aprovechaba las camisas viejas para hacer trapos o ensanchar pantalones cuando crecíais. Pídele a Gemini: '¿Qué papel tuvieron las máquinas de coser a pedal en la economía familiar de los hogares españoles del siglo XX?'."),

        ("El Tren de Vapor o Ferrobús llegando a la Estación",
         "Rememorar el silbato, el vapor y la emoción de las despedidas y bienvenidas en la estación de tren.",
         "Fotografía histórica de época en la pequeña estación de ferrocarril de pueblo en [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. Una locomotora de vapor o un ferrobús plateado de la época entrando despacio en el andén soltando una nube de vapor blanco, con maletas de piel sobre carretillas de madera y viajeros con abrigos saludando desde las ventanillas bajadas con correa de cuero. Nostalgia y viaje ferroviario.",
         "💬 Para contarle a tus nietos: Cuéntales cómo eran los billetes de tren de cartón duro que el revisor picaba con una tenaza metálica. Pídele a Gemini: '¿Cómo era viajar en los trenes de vapor y ferrobuses en España en los años 50 y 60?'."),

        # 3. EL INVIERNO, EL HOGAR Y LA VIDA FAMILIAR (21-30)
        ("La Mesa Camilla con Brasero de Picón y Enaguas",
         "Recordar el centro de reunión familiar en invierno donde se hacían los deberes y se jugaba a las cartas.",
         "Fotografía de interior cálida y hogareña en una casa de [MI_PUEBLO] en una tarde fría de invierno de los años [MI_AÑO_O_DÉCADA]. Una mesa redonda camilla vestida con pesadas faldillas o enaguas de paño marrón hasta el suelo, con una baraja española y una tetera humeante encima, y varias personas sentadas con las piernas metidas bajo las faldillas calentándose con el brasero. Luz tenue de lámpara de tulipa.",
         "💬 Para contarle a tus nietos: Explícales qué era la badila para remover el picón del brasero y cómo se evitaba el dolor de cabeza ventilando la habitación. Pídele a Gemini: 'Escribe un relato entrañable sobre las tardes de invierno alrededor de la mesa camilla en un pueblo español'."),

        ("La Nevera de Hielo y el Reparto de Barras Heladas",
         "Mostrar cómo se conservaban los alimentos antes de que todas las casas tuvieran frigorífico eléctrico.",
         "Fotografía de época de un mueble nevera doméstico de madera barnizada con herrajes de latón y puerta gruesa aislada abierta, mostrando en su compartimento superior una gran barra transparente de hielo natural goteando sobre una bandeja de zinc, enfriando jarras de agua, mantequilla y leche. Al lado, tenazas de hierro para agarrar el bloque de hielo.",
         "💬 Para contarle a tus nietos: Pregúntales cómo creen que se mantenía fresca la comida cuando no había enchufes para la nevera. Pídele a Gemini: '¿Cómo funcionaban las fábricas de hielo y las neveras de madera en los hogares españoles de mediados del siglo XX?'."),

        ("El Sereno con su Chuzo, Farol y Manojo de Llaves",
         "Recordar la figura nocturna que abría los portales y daba la hora y el tiempo en las calles.",
         "Escena nocturna atmosférica en una calle empedrada de [MI_PUEBLO] o ciudad en los años [MI_AÑO_O_DÉCADA], iluminada por farolas de gas tenues. Un sereno con guardapolvo gris oscuro, gorra de plato, bastón con punta de hierro (chuzo) y farolillo de aceite en la mano, comprobando la cerradura de un gran portal de madera con su pesado manojo de llaves maestras en el cinto.",
         "💬 Para contarle a tus nietos: Cuéntales cómo se llamaba al sereno dando tres palmadas fuertes en la calle y gritando '¡Sereno!'. Pídele a Gemini: '¿Cuál era el trabajo de los serenos en las noches de España y cuándo desapareció este oficio tradicional?'."),

        ("El Cartero con su Cartera de Cuero y las Cartas Manuscritas",
         "Valorar la emoción de recibir noticias lejanas escritas con pluma y sello postal tras días de espera.",
         "Fotografía histórica de un cartero rural con uniforme azul marino de Correos y cartera grande de cuero marrón cruzada al pecho, entregando un sobre de papel con matasellos y sello de correos a una vecina sonriente en la puerta de su casa de pueblo en [MI_PUEBLO]. Detrás, su bicicleta de reparto apoyada en la acera.",
         "💬 Para contarle a tus nietos: Explícales qué era el papel de carta fino de avión o las tarjetas postales que se enviaban en vacaciones. Pídele a Gemini: '¿Cuánto tardaba en llegar una carta por correo postal en España en los años 60 y cuánto costaba el sello de Correos?'."),

        ("El Cine de Verano en la Pared del Frontón o Plaza",
         "Revivir las noches calurosas de julio y agosto viendo películas bajo las estrellas llevando la silla de casa.",
         "Fotografía nocturna en blanco y negro o color cálido en una plaza de [MI_PUEBLO] en verano en [MI_AÑO_O_DÉCADA]. Una gran pared blanca encalada sirve de pantalla donde se proyecta una película clásica de aventuras, con decenas de vecinos de todas las edades sentados en sillas de tijera o anea traídas desde casa comiendo pipas bajo la brisa nocturna. Haz de luz del proyector visible en el cielo.",
         "💬 Para contarle a tus nietos: Pregúntales si se imaginan ver una película al aire libre donde cada uno tenía que llevar su propia silla de la cocina. Pídele a Gemini: '¿Qué películas españolas y extranjeras triunfaban en los cines de pueblo en los años [MI_AÑO_O_DÉCADA]?'."),

        ("El Día de Reyes: Juguetes de Hojalata y la Ilusión Sencilla",
         "Mostrar que con un juguete sencillo de cuerda o una pelota se era inmensamente feliz.",
         "Fotografía vintage entrañable en la mañana del 6 de enero en un salón modesto de [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. Dos niños con zapatillas de paño sentados en el suelo mirando ilusionados sus regalos: un camión de bomberos de hojalata pintada con llave de cuerda, una muñeca de cartón piedra con vestido de flores y una bolsita de tela con peladillas y nueces.",
         "💬 Para contarle a tus nietos: Enséñales que la ilusión de Reyes no dependía de tener 20 regalos caros sino de la magia de estrenar un juguete de cuerda. Pídele a Gemini: '¿Cuáles eran los juguetes españoles de Reyes más famosos fabricados en Ibi (Alicante) en los años 50 y 60?'."),

        ("Los Cromos de Fútbol y Naturaleza en Álbumes de Papel",
         "Recordar el rito de comprar sobres con pesetas sueltas e intercambiar los 'repes' en el recreo.",
         "Fotografía en primer plano de dos manos infantiles pegando con cola o saliva un cromo de papel litografiado de un futbolista legendario en un álbum oficial de la Liga Española de los años [MI_AÑO_O_DÉCADA]. Sobre la mesa, un montón de cromos desordenados marcados a lápiz por detrás para cambiar.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era cantar en el patio '¡Sile, nole!' para cambiar cromos con los amigos. Pídele a Gemini: '¿Quiénes eran los futbolistas y deportistas más admirados por los niños españoles en el año [MI_AÑO_DE_NACIMIENTO]?'."),

        ("El Mercado Semanal de los Jueves: Tenderetes y Regateo",
         "Evocar el colorido y la algarabía del mercadillo con telas, zapatos, ganado menor y cacharros.",
         "Vista panorámica bulliciosa del mercado callejero semanal en la plaza o calle mayor de [MI_PUEBLO] en [MI_AÑO_O_DÉCADA]. Toldos de lona a rayas protegiendo puestos de telas y pañuelos, loza de barro vidriado de alfarero, zapatos de cuero y alpargatas, y vecinos vestidos de domingo mirando los géneros mientras los vendedores pregonan a viva voz.",
         "💬 Para contarle a tus nietos: Cuéntales cómo se comerciaba y se regateaba con simpatía en los tenderetes ambulantes. Pídele a Gemini: '¿Cómo eran los mercados de ganado y ferias comarcales en las provincias españolas a mediados del siglo XX?'."),

        ("La Llegada del Hombre a la Luna (1969) en la Televisión",
         "Compartir el recuerdo imborrable de la noche en que el mundo entero contuvo la respiración mirando al cielo.",
         "Fotografía histórica de julio de 1969 en el salón de una casa española en [MI_PUEBLO]. Una familia reunida de madrugada alrededor del televisor en blanco y negro, con la emblemática imagen borrosa de Neil Armstrong bajando la escalerilla del módulo lunar proyectada en el tubo de rayos catódicos. Rostros de incredulidad y emoción histórica.",
         "💬 Para contarle a tus nietos: Cuéntales qué estabas haciendo tú exactamente esa noche de julio de 1969 y la voz de Jesús Hermida retransmitiendo el alunizaje. Pídele a Gemini: '¿Cómo vivió la sociedad española la retransmisión televisiva de la llegada a la Luna en julio de 1969?'."),

        ("El Tocadiscos Portátil ('Pick-up') y los Guateques Juveniles",
         "Revivir los primeros bailes en casa con discos pequeños de vinilo de 45 revoluciones con solapa de cartón.",
         "Escena juvenil festiva de un guateque en un salón de los años 60 o 70. En una mesa baja luce un tocadiscos portátil maleta de vinilo rojo y crema abierto girando un single pequeño de 45 rpm, con fundas de discos del Dúo Dinámico, Los Bravos o Raphael alrededor. Jóvenes con pantalones de campana y peinados de época charlando con vasos de refresco en la mano.",
         "💬 Para contarle a tus nietos: Enséñales qué era un guateque en casa con tortilla y discos prestados. Pídele a Gemini: '¿Qué música ye-yé y qué grupos pop españoles se bailaban en los guateques de los años 60 en España?'."),

        # 4. TRADICIONES, CAMPO Y MEMORIA COLECTIVA (31-40)
        ("La Recolección de la Aceituna o la Vendimia en Familia",
         "Recordar el trabajo compartido en el campo donde varias generaciones recogían el fruto juntas.",
         "Fotografía histórica en un olivar o viñedo luminoso cerca de [MI_PUEBLO] en [MI_AÑO_O_DÉCADA]. Mantones de arpillera extendidos bajo los olivos centenarios, agricultores vareando las ramas con varas de castaño y mujeres y jóvenes arrodillados recogiendo aceitunas en espuertas de esparto. Al fondo, un carro con bidones y mulas descansando a la sombra.",
         "💬 Para contarle a tus nietos: Cuéntales cómo se comía en cuadrilla en el suelo del campo y el sabor del aceite recién prensado en la almazara del pueblo. Pídele a Gemini: '¿Cómo era la campaña de vendimia o aceituna tradicional en España antes de la mecanización?'."),

        ("El Pastor con su Rebaño Cruzando la Cañada Real",
         "Evocar el sonido de las esquilas y el paso pausado de las ovejas por las vías pecuarias históricas.",
         "Fotografía de época de un pastor castellano o andaluz con pelliza de lana, garrota de fresno y morral de cuero al hombro, caminando junto a su perro carea guiando un gran rebaño de ovejas merinas por una cañada de tierra con encinas a las afueras de [MI_PUEBLO] al amanecer. Polvareda dorada a contraluz y sonido sugerido de cencerros.",
         "💬 Para contarle a tus nietos: Explícales qué son las cañadas reales y la trashumancia que cruzaba España de norte a sur. Pídele a Gemini: '¿Qué importancia histórica tuvieron las vías pecuarias y la Mesta en las comarcas de España?'."),

        ("La Cocina de Carbón o Leña y los Pucheros de Barro",
         "Rememorar el sabor inigualable de los guisos a fuego lento en la cocina económica de hierro fundido.",
         "Fotografía de época del interior de una cocina rústica en [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. Una robusta cocina de leña de hierro fundido negro con aros concéntricos pulidos en la plancha superior, con dos ollas de barro cocido humeando suavemente, cucharas de madera en el escurridor de cerámica de la pared y un haz de leña de sarmientos en el rincón.",
         "💬 Para contarle a tus nietos: Cuéntales cómo se regulaba el calor del fuego quitando o poniendo los aros concéntricos de hierro de la plancha. Pídele a Gemini: '¿Qué recetas de cocido y puchero tradicionales se hacían en las cocinas económicas de los pueblos españoles?'."),

        ("El Día de Matanza Tradicional y los Embutidos en la Despensa",
         "Explicar la fiesta de invierno que aseguraba el sustento cárnico de la familia para todo el año.",
         "Fotografía histórica costumbrista en el corral o patio empedrado de una casa de [MI_PUEBLO] en [MI_AÑO_O_DÉCADA]. Varias mujeres alrededor de una gran artesa de madera picando magro y especias para chorizos con pimentón rojo vivo, con ristras de morcillas y chorizos curándose colgadas de varas de madera en el techo del zaguán. Ambiente festivo familiar de invierno.",
         "💬 Para contarle a tus nietos: Explícales que del cerdo se aprovechaba absolutamente todo hasta el último bocado. Pídele a Gemini: '¿Por qué la matanza tradicional era una fiesta comunitaria de ayuda mutua entre vecinos en los pueblos de España?'."),

        ("Los Domingos de Paseo por la Alameda o Calle Mayor",
         "Recordar la elegancia de vestirse con la ropa de domingo para pasear y saludar a los conocidos.",
         "Fotografía histórica de un domingo soleado de primavera en el paseo arbolado o alameda principal de [MI_PUEBLO] en [MI_AÑO_O_DÉCADA]. Familias y parejas de jóvenes paseando despacio con sus mejores abrigos y sombreros, señores con boina saludando con la mano, puestos de castañas asadas o barquillos en la esquina y niños con globos de colores.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era la costumbre del paseo de domingo para ver y dejarse ver antes de que existieran las redes sociales. Pídele a Gemini: '¿Cómo era el rito social del paseo dominical en los pueblos y ciudades de España a mediados del siglo XX?'."),

        ("La Máquina de Escribir Portátil Olivetti y el Papel de Calco",
         "Mostrar a los nietos cómo se hacían copias dobles de un documento antes de que existieran las impresoras.",
         "Fotografía macro nostálgica de una clásica máquina de escribir portátil verde oliva (Olivetti Lettera) sobre una mesa de despacho, mostrando el rodillo con una hoja blanca y detrás una hoja azul brillante de papel de calco (papel carbón) para sacar copia doble. Teclas circulares mecánicas y cinta bicolor negra y roja.",
         "💬 Para contarle a tus nietos: Cuéntales qué pasaba si te equivocabas de letra al final de una página entera y tenías que borrar con típex o empezar de nuevo. Pídele a Gemini: '¿Cómo funcionaba la mítica máquina Olivetti Lettera 32 y qué supuso para escritores y estudiantes en España?'."),

        ("La Cabina Telefónica Pública y las Monedas de Cinco Duros",
         "Rememorar la aventura de meter monedas por la ranura para hablar con los parientes lejanos.",
         "Fotografía de época de una clásica cabina telefónica de cristal y aluminio en una plaza española en los años 70 u 80. En el interior se aprecia el icónico teléfono gris o verde de disco giratorio con ranura superior de monedas, y una persona esperando con una moneda de 25 pesetas (cinco duros) con agujero en la mano mientras caen los pitidos de aviso de saldo.",
         "💬 Para contarle a tus nietos: Pregúntales cómo harían para llamar a su madre en la calle si no existieran los móviles. Pídele a Gemini: '¿Cómo funcionaban las cabinas de teléfono públicas de España y cuándo se instaló la primera cabina?'."),

        ("El Zapatero Remendón con su Lezna y su Banqueta Baja",
         "Recordar cómo se reparaban las suelas de cuero y se ponían tapas de goma para no gastar zapatos.",
         "Fotografía de época del pequeño taller de un zapatero artesano en [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. El maestro zapatero sentado en su banqueta baja de madera con mandil de cuero, sujetando un zapato en una horma metálica de tres brazos mientras clava tachuelas con un martillo corto. Estanterías repletas de pieles curtidas, leznas, hilos encerados y botes de cola.",
         "💬 Para contarle a tus nietos: Explícales que antes los zapatos duraban diez años porque se cambiaban las suelas una y otra vez. Pídele a Gemini: '¿Cómo era el oficio de zapatero remendón y qué herramientas tradicionales utilizaba?'."),

        ("Los Refranes del Abuelo y la Sabiduría del Tiempo",
         "Transmitir a los nietos los dichos populares que predecían la lluvia, el frío y las cosechas.",
         "Ilustración clásica estilo aguafuerte o grabado botánico cálido, representando un cielo campestre con nubes algodonosas doradas sobre los campos de [MI_PUEBLO], con golondrinas volando bajo cerca del trigo y un caracol sobre una hoja húmeda. Tipografía en pergamino que evoca sabiduría rural.",
         "💬 Para contarle a tus nietos: Enséñales tres refranes de tu tierra que sigan teniendo vigencia hoy. Pídele a Gemini: 'Dime 5 refranes tradicionales españoles sobre el clima y el campo (como 'Cielo aborregado, a los tres días mojado') y explícame la base científica que tenían'."),

        ("El Regalo de Cumpleaños Hecho a Mano con Cariño",
         "Recordar que el mejor regalo de la infancia era un jersey tejido por la madre o un juguete tallado de madera.",
         "Fotografía íntima de una mesa de madera rústica donde descansa un jersey infantil de lana virgen de color mostaza tejido a dos agujas con ochos, envuelto con un cordel de cáñamo y una ramita de lavanda seca, junto a una figura de caballo tallada a navaja en madera de pino. Calidez, dedicación y afecto artesano.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era recibir un regalo que alguien había pasado semanas haciendo con sus propias manos para ti. Pídele a Gemini: 'Escribe una reflexión emotiva sobre el valor del tiempo y las cosas hechas a mano en la época de nuestros abuelos'."),

        # 5. OBJETOS, CANCIONES Y SABORES OLVIDADOS (41-50)
        ("El Botiquín Tradicional: Agua Oxigenada, Mercromina y Manzanilla",
         "Evocar los remedios caseros que nos curaban las raspaduras de las rodillas tras caernos en la calle.",
         "Fotografía de primer plano de un estante de botiquín casero de madera en los años [MI_AÑO_O_DÉCADA], mostrando un bote de cristal de agua oxigenada con tapón de corcho, el icónico frasco de Mercromina roja con su aplicador de cristal, una caja metálica de tiritas de tela rosa y un frasco con flores secas de manzanilla silvestre.",
         "💬 Para contarle a tus nietos: Cuéntales por qué todos los niños llevaban las rodillas y los codos pintados de rojo brillante de Mercromina todo el verano. Pídele a Gemini: '¿Cuáles eran los remedios caseros y de farmacia más populares en los hogares españoles de los años 50 y 60?'."),

        ("El Pincel de la Cal y el Blanqueo de las Casas en Primavera",
         "Recordar la tradición de pintar de blanco puro las fachadas y patios antes de que llegara el calor.",
         "Escena luminosa en una callejuela de [MI_PUEBLO] en primavera en [MI_AÑO_O_DÉCADA]. Un vecino subido a una escalera de madera aplicando con una brocha gorda cal viva blanca desleída en un cubo de zinc sobre la fachada de piedra, dejando la pared deslumbrante de blancura bajo un cielo azul intenso, con macetas de geranios rojos esperando ser colgadas.",
         "💬 Para contarle a tus nietos: Explícales por qué se encalaban las casas de blanco: para desinfectar con la cal y para rebotar el calor del sol en verano. Pídele a Gemini: '¿Por qué la cal apagada era el material estrella de la arquitectura mediterránea y rural española?'."),

        ("El Vaso de Leche con Galletas María y el Cola Cao",
         "Homenajear el desayuno de toda una vida y el bote metálico con litografías que se guardaba para hilos.",
         "Fotografía cenital vintage de un desayuno de la época: un vaso grueso de cristal con leche caliente con los característicos grumos flotantes de cacao en polvo, un plato con galletas María doradas con su dibujo grabado alrededor y al fondo la icónica lata cilíndrica metálica decorada de Cola Cao. Nostalgia pura y recuerdos de infancia.",
         "💬 Para contarle a tus nietos: Cuéntales cómo se deshacían las galletas María en la leche hasta formar una papilla deliciosa. Pídele a Gemini: '¿Cuándo nació el Cola Cao en España y cómo eran las primeras latas de hojalata que usaban las abuelas como costurero?'."),

        ("Los Patinetes Caseros con Rodamientos de Bolas y Tablas",
         "Mostrar cómo nos fabricábamos nuestros propios bólidos con maderas de desecho y cojinetes de camión.",
         "Fotografía de época de un niño sonriente en [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA] junto a un patinete o carricoche artesanal hecho a mano con dos tablas de madera clavadas en ángulo recto, un manillar con dos empuñaduras y tres rodamientos de bolas de acero pulido como ruedas. Fondo de calle en cuesta de adoquines.",
         "💬 Para contarle a tus nietos: Pregúntales si saben el ruido ensordecedor y divertido que hacían los rodamientos de hierro sobre el asfalto o la acera. Pídele a Gemini: '¿Cómo construían los niños de los años 60 sus propios patinetes y carretones de rodamientos?'."),

        ("Las Canciones Populares del Corro y la Comba",
         "Rescatar del olvido las melodías que cantaban las niñas y niños cogidos de la mano en el patio.",
         "Ilustración vintage luminosa de un grupo de niñas con vestidos de flores y calcetines cortos cogidas de la mano formando un corro circular en la plaza de [MI_PUEBLO], girando sonrientes bajo los árboles en una tarde dorada de primavera. Flores silvestres en el suelo y atmósfera de alegría pura.",
         "💬 Para contarle a tus nietos: Cántales dos estrofas de 'El patio de mi casa' o 'Al corro de la patata' y mira si se la saben en el colegio. Pídele a Gemini: 'Escríbeme la letra completa y el origen histórico de 3 canciones tradicionales de corro infantiles en España'."),

        ("El Primer Viaje a la Capital en el Autobús de Línea",
         "Recordar la impresión de ver por primera vez los edificios altos, los semáforos y los escaparates grandes.",
         "Fotografía histórica de un autobús comarcal antiguo de morro redondo (tipo Pegaso o Chausson) azul o verde, llegando a la gran estación o plaza de la capital provincial en los años [MI_AÑO_O_DÉCADA]. Pasajeros bajando abrigados mirando asombrados los rótulos luminosos de neón y los tranvías que cruzan la avenida.",
         "💬 Para contarle a tus nietos: Cuéntales qué sentiste la primera vez que viste un edificio de 10 plantas o una escalera mecánica. Pídele a Gemini: '¿Cómo eran los autobuses de línea de los años 50 y 60 en las carreteras de España?'."),

        ("Las Visitas al Huerto del Abuelo y el Sabor del Tomate Real",
         "Transmitir a los nietos el olor a mata de tomate verde y el sabor de una fruta recién cogida del árbol.",
         "Fotografía en plano medio de un abuelo campesino con boina y azada en la mano junto a su nieto en un huerto fértil en [MI_PUEBLO], entregándole un gran tomate rojo carnoso recién arrancado de la tomatera que todavía conserva el pedúnculo verde. Riego por surcos de tierra húmeda y sol estival brillante.",
         "💬 Para contarle a tus nietos: Explícales la diferencia abismal entre un tomate de plástico del súper y un tomate criado con agua de acequia y estiércol madurado al sol. Pídele a Gemini: '¿Cuáles son las variedades de tomates y verduras tradicionales de la huerta española que se están recuperando hoy?'."),

        ("La Zapatilla de Paño y la Alpargata de Cáñamo",
         "Recordar el calzado cómodo de estar en casa y de trabajar que hacían los artesanos del pueblo.",
         "Bodegón vintage con dos pares de calzado tradicional sobre suelo de baldosas de barro cocido: unas alpargatas de lona blanca con suela trenzada de cáñamo atadas con cintas negras, y unas zapatillas de paño caliente a cuadros con forro de borreguito interior.",
         "💬 Para contarle a tus nietos: Enséñales cómo la alpargata de esparto ha pasado de ser el calzado más humilde a estar en las pasarelas de moda de todo el mundo. Pídele a Gemini: '¿Cuál es la historia artesana de la alpargata en España y cómo se fabrica su suela trenzada?'."),

        ("Las Primeras Monedas: La Peseta, el Duro y el Billete de Mil",
         "Explicar a los nietos la moneda con la que creciste antes de que llegara el euro.",
         "Fotografía macro en alta resolución sobre una mesa de madera de varias monedas históricas españolas de los años [MI_AÑO_O_DÉCADA]: la moneda rubia de una peseta con el escudo, la moneda grande de 5 pesetas (el duro), la moneda de 25 pesetas con el agujero en el centro y un billete verde de 1.000 pesetas.",
         "💬 Para contarle a tus nietos: Pregúntales si saben cuántos céntimos de euro eran un 'duro' y lo que podías comprar de chuches con una peseta rubia. Pídele a Gemini: 'Hazme una tabla divertida de equivalencias: ¿qué podías comprar con 1 peseta, con 5 pesetas y con 100 pesetas en los años [MI_AÑO_O_DÉCADA]?'."),

        ("El Huerto de Plantas Medicinales de la Abuela: Poleo, Ruda y Romero",
         "Homenajear el saber de las abuelas que conocían para qué servía cada hierba recogida en el monte.",
         "Fotografía botánica cálida en un rincón de piedra de un patio de [MI_PUEBLO], con manojos de plantas aromáticas secándose boca abajo atadas con cuerda: romero, tomillo silvestre, poleo menta y manzanilla, junto a un mortero de piedra y tarros de cristal con tisanas.",
         "💬 Para contarle a tus nietos: Enséñales a frotar una hoja de romero entre los dedos para oler el campo y cuéntales qué infusión te preparaba tu madre cuando te dolía la tripa. Pídele a Gemini: '¿Cuáles eran las 5 plantas silvestres medicinales más usadas tradicionalmente en la medicina popular de los pueblos españoles?'."),

        # 6. EL LEGADO VIVO Y EL FUTURO DE LA FAMILIA (51-60)
        ("El Orgullo de las Raíces: El Nombre de las Calles y Parajes",
         "Enseñar a los nietos el mapa sentimental del pueblo: la cuesta de las piedras, el molino viejo y la dehesa.",
         "Mapa antiguo ilustrado con acuarela y tinta que recrea el término municipal de [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA], señalando con dibujos entrañables el río, el puente romano o de piedra, el molino harinero, la fuente de los caños, el cerro del castillo y los caminos de las viñas.",
         "💬 Para contarle a tus nietos: Cuéntales por qué cada rincón del pueblo tiene un mote o nombre popular que no sale en Google Maps. Pídele a Gemini: 'Escribe una dedicatoria emotiva de un abuelo para su nieto transmitiéndole el amor por la tierra donde nació y creció su familia'."),

        ("Las Noches de Estrellas en la Era y los Cuentos del Abuelo",
         "Rememorar cuando las noches de verano no tenían contaminación lumínica y la Vía Láctea brillaba sobre el pueblo.",
         "Fotografía histórica nostálgica de una noche despejada en la era de [MI_PUEBLO]. Un cielo inmenso cuajado de millones de estrellas y la Vía Láctea luminosa, y abajo a contraluz un abuelo señalando con el dedo al cielo a su nieto sentado a su lado sobre un fardo de paja. Silencio, asombro cósmico y complicidad familiar.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era acostarse de espaldas en la paja en verano a ver caer las lágrimas de San Lorenzo (perseidas). Pídele a Gemini: '¿Cómo se veían las estrellas en los pueblos de España antes de la llegada de la iluminación eléctrica moderna?'."),

        ("El Molino de Aceite o Harinero del Río",
         "Mostrar cómo la fuerza del agua o los bueyes movía las grandes muelas de piedra para moler el grano.",
         "Fotografía de época del interior de un antiguo molino harinero de río en [MI_PUEBLO] en [MI_AÑO_O_DÉCADA]. Dos enormes piedras circulares de granito rozándose entre sí, con harina blanca flotando en el ambiente y depositándose en la artesa de madera, con el molinero cubierto de polvillo blanco revisando la tolva con una sonrisa.",
         "💬 Para contarle a tus nietos: Explícales cómo el río movía la rueda que hacía girar la piedra para convertir el trigo en harina para el pan. Pídele a Gemini: '¿Cómo funcionaban los molinos fluviales hidráulicos en la España rural del siglo XX?'."),

        ("La Fuente de los Cuatro Caños y el Cántaro en el Cuello",
         "Recordar la habilidad de llevar el cántaro de barro apoyado en la cadera o en la cabeza con un rodete.",
         "Fotografía histórica de la fuente monumental de piedra de cuatro caños en [MI_PUEBLO] en [MI_AÑO_O_DÉCADA]. Cuatro chorros continuos de agua cristalina cayendo al pilón, con varias mozas y muchachos llenando cántaros de barro blanco y colocándose el rodete de tela en la cabeza para equilibrar el cántaro sin que se cayera de camino a casa.",
         "💬 Para contarle a tus nietos: Pregúntales si serían capaces de andar 100 metros con 10 kilos de agua en la cabeza sin tocar el cántaro con las manos. Pídele a Gemini: '¿Qué habilidad y equilibrio tenían las mujeres españolas para acarrear el agua en cántaros antes del agua corriente en las casas?'."),

        ("El Día de Matrícula en la Universidad o el Primer Empleo",
         "Compartir con los nietos el valor del esfuerzo y la emoción del primer sueldo entregado en casa.",
         "Fotografía histórica de un joven orgulloso con traje modesto o mono de trabajo limpio de los años 60 o 70 en [MI_PUEBLO] o en la ciudad, sosteniendo con dignidad su primer sobre marrón de nómina o su carnet de estudiante o aprendiz. Fondo de taller industrial limpio o aula universitaria clásica.",
         "💬 Para contarle a tus nietos: Cuéntales qué hiciste tú con tu primer sueldo o con tus primeros ahorros y a quién se lo entregaste. Pídele a Gemini: '¿Cómo eran las condiciones laborales y el valor del primer empleo para los jóvenes en España en los años [MI_AÑO_O_DÉCADA]?'."),

        ("Los Juegos de Invierno con Nieve en el Pueblo",
         "Recordar cuando las nevadas cubrían los tejados y se bajaban las cuestas con sacos de plástico.",
         "Fotografía de época de [MI_PUEBLO] completamente cubierto por una gran nevada blanca en invierno en los años [MI_AÑO_O_DÉCADA]. Calles silenciosas con muñecos de nieve con nariz de zanahoria y ojos de carbón, niños tirándose bolas de nieve sonrientes con pasamontañas de lana y perros saltando en la nieve virgen.",
         "💬 Para contarle a tus nietos: Cuéntales cómo os tirabais por las cuestas heladas montados en un saco lleno de paja a toda velocidad. Pídele a Gemini: '¿Cuáles fueron las nevadas históricas más copiosas recordadas en España en las décadas de los 50 y 60?'."),

        ("El Primer Disco que Compré con mis Ahorros",
         "Revivir la magia de poner la aguja sobre el surco del vinilo y escuchar la canción que te cambió la vida.",
         "Primer plano con luz cálida de un tocadiscos doméstico de los años 60 o 70, con la aguja apoyándose sobre el primer surco de un disco de vinilo negro brillante, y al lado la portada de cartón con el grupo musical favorito de tu juventud en España. Atmósfera íntima y musical.",
         "💬 Para contarle a tus nietos: Diles cuál fue la primera canción o artista que te entusiasmó de joven y ponédsela juntos en el móvil en YouTube. Pídele a Gemini: 'Dime los 5 cantantes y grupos musicales más populares de España en el año en que yo cumplí 15 años'."),

        ("La Celebración de las Bodas de Antaño: El Convite en el Patio",
         "Recordar cómo se celebraban las bodas con chocolate con churros, jamón, baile y alegría sincera.",
         "Fotografía de época de una boda popular en [MI_PUEBLO] en los años [MI_AÑO_O_DÉCADA]. Los novios vestidos con elegancia clásica cortando una tarta en el patio de una casa encalada decorada con macetas y lazos blancos, rodeados de todos los vecinos, familiares y niños del pueblo brindando con copas de anís y sidra. Felicidad auténtica y cercana.",
         "💬 Para contarle a tus nietos: Cuéntales cómo era la fiesta de boda de antes donde todo el pueblo cocinaba y participaba en la celebración. Pídele a Gemini: '¿Cómo eran los banquetes y celebraciones de bodas populares en los pueblos españoles a mediados del siglo XX?'."),

        ("El Tesoro del Refranero Popular de Mi Provincia",
         "Recopilar los modismos, palabras únicas y chascarrillos que solo se dicen en tu comarca.",
         "Ilustración clásica con aire de grabado que muestra una pequeña biblioteca rústica con un libro antiguo abierto de páginas amarillentas donde se leen palabras tradicionales, refranes y modismos populares de la provincia de [MI_PUEBLO], con una vela encendida y unas gafas de montura de carey descansando encima.",
         "💬 Para contarle a tus nietos: Enséñales 3 palabras típicas de tu pueblo que ellos no usan y pregúntales qué creen que significan. Pídele a Gemini: 'Hazme una lista de 5 palabras autóctonas y modismos tradicionales entrañables de la provincia de [MI_PUEBLO] con su significado'."),

        ("La Carta al Futuro: El Legado de un Abuelo para sus Nietos",
         "Dejar un mensaje imborrable de amor, experiencia y raíces que los nietos guardarán toda la vida.",
         "Fotografía cálida y emotiva en primer plano de las manos arrugadas y sabias de un abuelo o abuela sosteniendo con cariño las manos jóvenes de su nieto sobre una carta manuscrita doblada en papel pergamino, con un reloj de bolsillo antiguo de plata sobre la mesa. Luz dorada de atardecer, ternura infinita y amor familiar.",
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

