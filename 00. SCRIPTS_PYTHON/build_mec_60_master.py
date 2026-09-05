# -*- coding: utf-8 -*-
"""
Generador Maestro del Bloque 14: [MEC] CÓMO FUNCIONAN LAS COSAS (Ingeniería y Mecánica en Vídeo 3D) (60 Ítems)
Propósito: Enseñar el funcionamiento interno de 60 mecanismos e inventos mecánicos fascinantes,
generando un vídeo de 10 segundos en Google Gemini con animación 3D en corte transversal (cutaway)
a cámara lenta, con piezas metálicas realistas y fluidos en movimiento.
"""

def get_mecanica_items():
    items = []

    mecanismos = [
        # BLOQUE 1: MOTORES Y AUTOMOCIÓN (01 a 10)
        ("El Cilindro del Motor de 4 Tiempos",
         "El corazón de la automoción: cómo cuatro fases (Admisión, Compresión, Explosión y Escape) transforman el combustible en movimiento continuo.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal (cutaway) de ingeniería mostrando el funcionamiento mecánico de un cilindro de motor de 4 tiempos. Se ve el pistón subiendo y bajando dentro del bloque de cilindro de metal pulido, las válvulas de admisión y escape abriéndose y cerrándose rítmicamente mediante el árbol de levas, y la bujía emitiendo una chispa luminosa que detona el combustible con una llamarada controlada empujando la biela y haciendo girar el cigüeñal. Movimiento mecánico fluido a cámara lenta, iluminación técnica limpia y texturas de acero y aceite de motor realistas.",
         "💡 Reto en el aula: Fíjate en cómo la válvula de admisión solo se abre cuando el pistón baja para aspirar la mezcla, y la de escape cuando sube para expulsar el humo. Pregunta a Gemini: '¿A cuántas revoluciones por minuto gira el motor de un coche normal cuando circula a 120 km/h en autopista?'."),

        ("El Embrague de Fricción de Automóvil",
         "La pieza que conecta y desconecta suavemente la potencia del motor a las ruedas para cambiar de marcha sin romper los engranajes.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal de ingeniería mostrando el funcionamiento del embrague de un coche. Se ve el volante de inercia giratorio conectado al motor, el disco de embrague con forro de fricción y el plato de presión con diafragma de resorte. Se aprecia cómo el disco se desacopla suavemente al pisar el pedal deteniendo la transmisión, y vuelve a acoplarse con firmeza transmitiendo el giro de forma continua. Iluminación técnica de taller y piezas de acero templado en movimiento.",
         "💡 Reto en el aula: Observa cómo los muelles pequeños dentro del disco absorben el tirón para que no des cabezazos al arrancar. Pregunta a Gemini: '¿Por qué se quema el embrague si dejamos el pie apoyado en el pedal a medio pisar mientras conducimos?'."),

        ("El Diferencial de las Ruedas Traseras",
         "El milagro de los engranajes planetarios que permite a un vehículo girar en una curva haciendo que la rueda exterior ruede más rápido que la interior.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal de ingeniería mostrando el mecanismo de un diferencial de coche en una curva. Se observa el piñón de ataque haciendo girar la corona dentada principal, y los cuatro piñones cónicos planetarios y satélites interiores rotando sobre sus propios ejes. Muestra claramente cómo la rueda exterior gira con mayor velocidad que la rueda interior sin derrapar ni perder tracción sobre el asfalto. Movimiento de engranajes metálicos lubricados con aceite dorado brillante.",
         "💡 Reto en el aula: Si las dos ruedas traseras estuvieran unidas por una barra fija de hierro, en cada curva una de las dos tendría que derrapar obligatoriamente. Pregunta a Gemini: '¿Quién inventó el diferencial y cómo solucionaba este problema en los carros de caballos antiguos?'."),

        ("Frenos de Disco Ventilados y Pinza Hidráulica",
         "Cómo la presión hidráulica transforma la velocidad de toneladas de peso en calor disipado en segundos.",
         "Crea un vídeo de 10 segundos: Animación 3D en primer plano de ingeniería de un freno de disco de automóvil. El disco de acero perforado y ventilado gira a gran velocidad. Se ve la pinza de freno (cáliper) roja en corte, donde los pistones empujados por líquido de frenos aprietan con enorme fuerza las pastillas contra el disco. Se aprecian las ranuras de ventilación internas expulsando aire caliente mientras el disco se ilumina ligeramente al rojo tenue por la fricción hasta detener la rotación. Iluminación cinematográfica de precisión.",
         "💡 Reto en el aula: Observa los canales huecos dentro del disco: funcionan como un ventilador centrífugo que enfría el metal. Pregunta a Gemini: '¿Por qué los coches modernos llevan frenos de disco delante y muchos llevaban tambor detrás?'."),

        ("Caja de Cambios Manual y Sincronizadores",
         "El laberinto de piñones helicoidales que adapta la fuerza del motor según subamos una cuesta empinada o crucemos una llanura.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal de una caja de cambios manual de coche. En el eje primario e intermedio giran piñones helicoidales bañados en aceite. Se observa la horquilla metálica desplazando el manguito sincronizador de bronce cónico, que iguala la velocidad de giro por fricción antes de que los dientes engranen suavemente y sin rascado al meter una marcha superior. Movimiento mecánico preciso a cámara lenta con iluminación técnica de estudio.",
         "💡 Reto en el aula: Fíjate en los anillos dorados de bronce (sincronizadores): son los que impiden que los engranajes rasquen al cambiar. Pregunta a Gemini: '¿Qué significaba hacer doble embrague en los camiones antiguos que no tenían sincronizadores?'."),

        ("El Turbocompresor de Gases de Escape",
         "Aprovechar la energía residual del escape para insuflar aire comprimido a presión en los cilindros y disparar la potencia.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal de un turbocompresor de motor. En el lado derecho, los gases de escape calientes en tono naranja rojizo hacen girar la turbina de escape a altísima velocidad. El eje central de titanio transmite el giro a la rueda compresora del lado izquierdo, que aspira aire exterior azul frío y lo comprime enviándolo hacia el intercooler. Iluminación técnica con contraste térmico entre gases calientes y aire fresco comprimido.",
         "💡 Reto en el aula: El turbo gira hasta a 200.000 revoluciones por minuto sobre una película milimétrica de aceite a presión. Pregunta a Gemini: '¿Por qué en los coches turboalimentados se recomienda esperar un minuto al ralentí antes de apagar el motor tras un viaje largo?'."),

        ("La Dirección de Cremallera y Piñón",
         "El sistema más directo y seguro que convierte el giro circular del volante en el movimiento lineal de las ruedas.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal del mecanismo de dirección de cremallera de un automóvil. El piñón estriado accionado por la columna del volante gira engranado sobre la barra dentada horizontal (cremallera). Se ve cómo la cremallera se desplaza suavemente a izquierda y derecha empujando las rótulas y bielas de dirección que orientan las manguetas de las ruedas. Iluminación de taller limpia con grasa mecánica lubricando los dientes.",
         "💡 Reto en el aula: Comprueba cómo un movimiento circular (volante) se transforma de inmediato en un movimiento recto (cremallera). Pregunta a Gemini: '¿Cómo funciona la asistencia hidráulica o eléctrica que hace que el volante gire con un solo dedo?'."),

        ("Amortiguador Hidráulico Telescópico",
         "Cómo el aceite forzado a través de válvulas microscópicas evita que el coche bote como un muelle incontrolado.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte longitudinal de un amortiguador hidráulico de coche. El vástago de acero cromado y el pistón se comprimen y extienden dentro del cilindro lleno de fluido hidráulico azul. Se aprecian las diminutas láminas de válvula abriéndose con resistencia calibrada, permitiendo que el aceite pase con dificultad entre las cámaras superior e inferior, amortiguando de forma suave y controlada las oscilaciones del resorte. Iluminación técnica de ingeniería.",
         "💡 Reto en el aula: El muelle soporta el peso del coche, pero el amortiguador es quien frena el rebote. Pregunta a Gemini: '¿Qué prueba casera se puede hacer apoyándose sobre el capó del coche para saber si los amortiguadores están gastados?'."),

        ("El Motor Rotativo Wankel",
         "Un motor sin pistones, bielas ni válvulas: un rotor triangular girando excéntricamente que hace los cuatro tiempos a la vez.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal del motor rotativo Wankel. Dentro de una cámara de combustión con forma de ocho ovalada (epitrocoide), un rotor triangular con engranaje central gira de forma excéntrica. Se observan las tres cámaras creadas por los vértices del rotor: una aspirando aire y combustible, otra comprimiendo y encendiendo con dos bujías, y la tercera expulsando los gases quemados, todo en un ciclo rotativo continuo y sin vibraciones. Piezas de metal bruñido y combustión visible.",
         "💡 Reto en el aula: Cada vuelta del rotor completa tres ciclos de combustión con solo tres piezas móviles principales. Pregunta a Gemini: '¿Qué míticos deportivos como el Mazda RX-7 usaron este motor y cuál era su gran ventaja y su talón de Aquiles?'."),

        ("El Distribuidor y la Bobina de Encendido",
         "El reloj eléctrico que disparaba 20.000 voltios a cada bujía en el instante exacto en los coches clásicos.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal de un distribuidor de encendido clásico (Delco). Un eje dentado hace girar el rotor central de baquelita. Se observa el platino abriéndose y cerrándose con una pequeña leva, enviando pulsos a la bobina cilíndrica que eleva el voltaje. El dedo del rotor va barriendo los cuatro bornes de cobre de la tapa, haciendo saltar un arco eléctrico azul brillante que viaja por los cables hacia las bujías. Movimiento rítmico a cámara lenta con chispas de alta tensión.",
         "💡 Reto en el aula: Si el platino se abría una décima de segundo antes o después, el motor 'picaba biela' o no arrancaba. Pregunta a Gemini: '¿Cómo se ponía a punto el encendido en un Seat 600 o Renault 4 usando una simple bombilla de 12 voltios?'."),

        # BLOQUE 2: MECÁNICA DOMÉSTICA Y COTIDIANA (11 a 20)
        ("La Cerradura de Bombín y Llave de Serreta",
         "El invento de Linus Yale que protege nuestros hogares mediante pitones alineados a la milésima de milímetro.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal de una cerradura de cilindro de bombín de puerta. Se ven los cinco pares de pitones y contra-pitones de latón empujados hacia abajo por pequeños resortes helicoidales bloqueando el giro. Al deslizarse la llave de serreta con sus dientes tallados, cada pitón se eleva a la altura exacta, alineando la línea de corte con la superficie del cilindro giratorio, permitiendo que la llave gire con suavidad y desplace el cerrojo de acero. Iluminación macro dorada sobre metal pulido.",
         "💡 Reto en el aula: Fíjate en cómo una sola muesca de la llave que falle por medio milímetro impide que el cilindro gire. Pregunta a Gemini: '¿Cómo funciona la técnica del ganzuado o el bumping que intentan aprovechar los cerrajeros y ladrones?'."),

        ("La Máquina de Coser y la Puntada de Cierre",
         "El lazo invisible: cómo dos hilos independientes se entrelazan a través de la tela miles de veces por minuto.",
         "Crea un vídeo de 10 segundos: Animación 3D en primerísimo plano macro y corte mecánico del cabezal y base de una máquina de coser. La aguja desciende perforando la tela blanca llevando un hilo superior rojo. Al iniciar el ascenso, forma un pequeño bucle; en ese instante exacto, la lanzadera rotatoria con garfio inferior de acero pasa rozando, atrapa el bucle de hilo rojo y lo hace girar alrededor de la canilla de hilo azul, creando un nudo perfecto que queda escondido en el centro de la tela. Movimiento a cámara lenta de extrema precisión.",
         "💡 Reto en el aula: Isaac Singer no inventó la máquina de coser, sino la lanzadera rotatoria que no rompía el hilo. Pregunta a Gemini: '¿Por qué la aguja de coser a máquina tiene el ojo en la punta y no en el extremo como las agujas de coser a mano?'."),

        ("El Bolígrafo de Clic Retráctil",
         "La ingeniosa leva rotatoria de plástico que inventó Christian Fauria para sacar y guardar la punta con un dedo.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transparente del mecanismo pulsador de un bolígrafo de clic. Se ve el pulsador exterior empujando una leva dentada de plástico blanco contra un muelle de acero helicoidal. La leva rota un cuarto de vuelta guiada por ranuras diagonales en el cuerpo del bolígrafo, quedando trabada en un escalón profundo que mantiene la mina de tinta asomada fuera. Al volver a pulsar, la leva gira otro cuarto de vuelta y el muelle la expulsa retrayendo la punta. Movimiento nítido y satisfactorio.",
         "💡 Reto en el aula: Desmontar un boli de clic es la primera lección de mecánica de cualquier niño. Pregunta a Gemini: '¿Cómo consigue la pequeña bolita de carburo de tungsteno de la punta rodar y dosificar la tinta viscosa sin que gotee en el papel?'."),

        ("La Cremallera Metálica de la Ropa",
         "Cientos de pequeños ganchos que se abrazan como dedos entrelazados guiados por una cuña triangular.",
         "Crea un vídeo de 10 segundos: Animación 3D en super macro del funcionamiento de una cremallera metálica de chaqueta. Se ven los dientes de latón dorado alineados en dos cintas de tela negra. El cursor metálico en corte avanza suavemente: su cuña interior en forma de Y junta las dos filas en el ángulo exacto para que el saliente esférico de cada diente encaje con un clic en el hueco hueco del diente opuesto. Movimiento a cámara lenta mostrando la solidez del engrane que no se abre bajo tensión.",
         "💡 Reto en el aula: La cremallera moderna fue perfeccionada para las botas de los pilotos en la Primera Guerra Mundial. Pregunta a Gemini: '¿Por qué si se desalinea un solo diente en la parte inferior la cremallera se abre por detrás y cómo se repara?'."),

        ("La Cisterna del Inodoro con Boya y Sifón",
         "El mecanismo hidrostático de Thomas Crapper que llena y vacía el tanque sin usar ni un solo circuito eléctrico.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transparente de una cisterna de agua de inodoro. Al pulsar el botón, una palanca eleva la campana de goma inferior permitiendo una descarga torrencial de agua por gravedad. Al vaciarse, la boya flotante desciende abriendo la válvula de entrada; el agua fresca entra por un tubo lateral llenando el depósito mientras la boya sube flotando despacio hasta que su brazo de palanca cierra herméticamente el paso de agua al nivel exacto. Iluminación limpia con agua cristalina y burbujas.",
         "💡 Reto en el aula: Todo el sistema funciona únicamente por flotabilidad y gravedad desde hace más de 150 años. Pregunta a Gemini: '¿Cómo funciona el tubo de rebosadero central que impide que el baño se inunde si la boya se estropea?'."),

        ("El Tostador de Pan Automático con Bimetal",
         "La física térmica: dos metales pegados que se dilatan a diferente velocidad para soltar el resorte cuando el pan está dorado.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal del mecanismo de una tostadora de pan clásica. Se ve la rebanada de pan bajando impulsada por una palanca que comprime un fuerte resorte inferior y conecta los filamentos de nicrom incandescentes al rojo vivo. Al calentarse, una pequeña lámina bimetálica compuesta de latón y acero se curva lentamente hacia un lado debido a la diferente dilatación térmica, hasta tropezar con un gatillo que libera el pestillo: el muelle se dispara y expulsa las tostadas doradas hacia arriba. Movimiento mecánico rítmico.",
         "💡 Reto en el aula: El bimetal no necesita pilas ni chips para medir el tiempo: se dobla con el calor real del pan. Pregunta a Gemini: '¿En qué otros aparatos del hogar se usa una lámina bimetálica para cortar la corriente por seguridad?'."),

        ("El Candado de Combinación con Ruedas de Discos",
         "Un enigma mecánico donde tres muescas ocultas deben mirar al mismo punto para abrir el grillete de acero.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal de un candado de combinación de tres discos numéricos. Se observan las tres ruedas exteriores con números girando. En su interior, cada disco tiene un núcleo con una muesca profunda ranurada. Al introducir el código correcto (ej. 7-4-2), las tres muescas interiores se alinean en línea recta formando un canal perfecto donde cae la barra de bloqueo, permitiendo que un resorte expulse hacia arriba el grillete curvo de acero templado. Iluminación técnica sobre latón y acero.",
         "💡 Reto en el aula: Si tiras del grillete hacia arriba mientras giras las ruedas, puedes sentir una pequeña resistencia cuando la muesca encaja. Pregunta a Gemini: '¿Por qué los candados de combinación de las cajas fuertes usan discos con dientes en lugar de ruedas simples?'."),

        ("Grifo Monomando de Discos Cerámicos",
         "Dos obleas de cerámica pulidas a nivel atómico que se deslizan sin gastarse ni gotear durante décadas.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transparente del cartucho de un grifo monomando de cocina. La palanca exterior mueve un eje de latón conectado a dos discos superpuestos de cerámica blanca ultra lisa con orificios triangulares. Al mover la palanca a un lado, el disco superior se desliza abriendo el canal de agua caliente roja y cerrando el de agua fría azul; al levantarla, los orificios coinciden aumentando el caudal de salida. Cero juntas de goma desgastables, flujo de agua fluido y sellado hermético milimétrico.",
         "💡 Reto en el aula: Los antiguos grifos de zapata de goma goteaban cada dos por tres; los discos cerámicos son tan lisos que las moléculas de agua no pueden colarse entre ellos. Pregunta a Gemini: '¿De qué material cerámico están hechos y por qué resisten el ataque de la cal?'."),

        ("El Encendedor de Chispa de Pedernal (Zippo / Clipper)",
         "El principio prehistórico del pedernal mecanizado en un bolsillo: una rueda de acero rayando cerio-hierro.",
         "Crea un vídeo de 10 segundos: Animación 3D en super macro del cabezal de un mechero de rueda. Un muelle empuja desde abajo una barrita cilíndrica de ferrocerio (piedra de mechero) contra una rueda de acero templado con estrías diagonales afiladas. El pulgar hace girar la rueda con fuerza; las estrías arrancan virutas microscópicas de metal que se auto-inflaman por fricción en el aire formando una lluvia de chispas incandescentes a 2.000 °C que encienden el vapor de gas o la mecha empapada en gasolina. Iluminación de chispa en la oscuridad.",
         "💡 Reto en el aula: La 'piedra' del mechero no es piedra natural, sino una aleación artificial llamada 'mischmetal' inventada en 1903. Pregunta a Gemini: '¿Por qué las chispas arden en el aire antes incluso de tocar la mecha?'."),

        ("La Grapadora de Oficina con Yunquecillo Plegador",
         "Una hoja de acero que empuja una grapa cortante mientras una base curva las dos patillas hacia dentro para coser folios.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte lateral de una grapadora de mesa presionando un fajo de papeles. Un martillo plano de acero impulsado por el brazo superior empuja la primera grapa del cargador hacia abajo, atravesando limpiamente las hojas de papel. Al salir por la parte inferior, las dos puntas afiladas de la grapa chocan contra las dos hendiduras curvadas del yunque metálico de la base, que obligan a las puntas a doblarse hacia adentro formando un lazo plano perfecto que prensa los folios. Cámara lenta con sonido visual mecánico.",
         "💡 Reto en el aula: ¿Te has fijado en que la placa metálica de la base se puede girar para grapar 'hacia afuera' (grapado temporal fácil de quitar)? Pregunta a Gemini: '¿Quién inventó la primera grapadora para el rey Luis XIV de Francia?'."),

        # BLOQUE 3: RELOJERÍA, PRECISIÓN Y ACÚSTICA (21 a 30)
        ("El Escape de Áncora de un Reloj Mecánico",
         "La joya de la relojería suiza: cómo un áncora de rubíes dosifica la fuerza del muelle en impulsos de una fracción de segundo.",
         "Crea un vídeo de 10 segundos: Animación 3D en primerísimo plano macro del escape de áncora de un reloj de pulsera mecánico. La rueda de escape dorada con dientes puntiagudos intenta girar impulsada por el barrilete. El áncora de acero pulido con dos paletas de rubí rojo sintético bascula rítmicamente a izquierda y derecha impulsada por el volante espiral que oscila hacia adelante y hacia atrás. Cada vez que el rubí libera un diente, la rueda avanza un paso exacto generando el sonido del 'tic-tac'. Engranajes de latón, rubíes traslúcidos y resorte espiral latiendo.",
         "💡 Reto en el aula: Los rubíes no son adornos de lujo: son cojinetes sintéticos con bajísima fricción que impiden que el metal se gaste. Pregunta a Gemini: '¿Por qué los relojes automáticos se cargan solos simplemente con el movimiento natural de la muñeca al caminar?'."),

        ("El Péndulo y la Pesa de un Reloj de Pared",
         "El descubrimiento de Galileo: el tiempo que tarda un péndulo en oscilar solo depende de su longitud, no de su peso.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte del mecanismo interior de un reloj de pared antiguo tipo carillón o cuco. Una pesada pesa de latón cuelga de una cadena descendiendo lentamente por gravedad y haciendo girar los engranajes. Arriba, una rueda de escape de dientes curvos empuja ligeramente una horquilla unida a la varilla de un largo péndulo con lenteja dorada que oscila majestuosamente de un lado a otro cada segundo exacto, manteniendo el ritmo constante del tiempo. Atmósfera cálida de madera de roble y bronce pulido.",
         "💡 Reto en el aula: Si un reloj de péndulo se atrasa, basta con apretar la tuerca inferior para subir la lenteja y acortar el péndulo. Pregunta a Gemini: '¿Cómo descubrió Galileo Galilei el isocronismo del péndulo observando una lámpara balancearse en la catedral de Pisa?'."),

        ("El Mecanismo de Tecla de un Piano de Cola",
         "La increíble palanca de escape doble de Sébastien Érard: golpear la cuerda con fuerza y apartarse al instante para dejarla vibrar.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal del mecanismo de una tecla de piano de cola. El dedo presiona la tecla de madera con marfil; el balancín eleva la palanca de repetición, que dispara un macillo con cabeza de fieltro blanco hacia arriba golpeando con vigor las tres cuerdas de acero tenso. Justo antes del impacto, el escape desacopla el macillo para que rebote hacia atrás y no apague el sonido, mientras el apagador superior se levanta para permitir que la cuerda vibre libremente generando la nota musical. Madera pulida, fieltro y cuerdas resonantes.",
         "💡 Reto en el aula: Si el macillo se quedara pegado a la cuerda al apretar la tecla, el sonido moriría al instante con un golpe sordo. Pregunta a Gemini: '¿Por qué se llama 'Pianoforte' y qué diferencia tenía con el clavecín antiguo?'."),

        ("La Aguja del Tocadiscos en el Surco de Vinilo",
         "Surcar las olas microscópicas de la música: una punta de diamante leyendo sonido grabado en plástico.",
         "Crea un vídeo de 10 segundos: Animación 3D en ultra microscopía electrónica del surco de un disco de vinilo girando a 33 rpm. Se aprecia el valle serpenteante del surco con diminutas ondulaciones en sus paredes laterales (canal izquierdo y derecho). Una aguja de diamante cónica pulida viaja encajada en el centro, vibrando frenéticamente a miles de hercios con cada relieve. En el interior de la cápsula fonocaptora, diminutos imanes unidos al vástago de la aguja oscilan entre bobinas de cobre generando la micro-corriente eléctrica de la música. Iluminación dorada macro.",
         "💡 Reto en el aula: En un disco estéreo, la pared izquierda del surco lleva el sonido del oído izquierdo y la derecha el del oído derecho. Pregunta a Gemini: '¿Cuántos metros o kilómetros de surco continuo tiene grabado un disco de vinilo de larga duración (LP)?'."),

        ("El Cilindro de Púas de una Caja de Música",
         "El antepasado de la memoria digital: un cilindro giratorio con clavijas metálicas que puntean un peine de notas.",
         "Crea un vídeo de 10 segundos: Animación 3D en macro del mecanismo de una caja de música clásica suiza. Un muelle de cuerda enrollado dentro de un tambor hace girar con lentitud un cilindro de latón dorado salpicado de cientos de diminutas púas de acero. Al rotar, cada púa engancha y suelta la punta de una lengüeta de acero templado afinada de un peine metálico con forma de teclado, haciéndola vibrar con una nota cristalina resonante. La música se reproduce en una secuencia perfecta y armónica bajo una luz tenue sobre madera.",
         "💡 Reto en el aula: Las lengüetas más largas y gruesas dan notas graves; las cortas dan notas agudas como las campanas. Pregunta a Gemini: '¿Cómo se programaban estos cilindros a mano en el siglo XIX antes de existir las computadoras?'."),

        ("El Diafragma de Láminas de una Cámara de Fotos",
         "La pupila mecánica de la fotografía: hojas de acero curvadas que cierran un círculo perfecto para regular la luz.",
         "Crea un vídeo de 10 segundos: Animación 3D en primerísimo plano macro y corte de ingeniería mostrando el funcionamiento mecánico del diafragma de un objetivo fotográfico. Se ven las láminas metálicas de acero pulido superpuestas abriéndose y cerrándose con precisión milimétrica a cámara lenta, formando un orificio circular perfecto que regula el paso de un haz de luz suave. Iluminación técnica de estudio, movimiento mecánico fluido y piezas mecánicas realistas en funcionamiento.",
         "💡 Reto en el aula: Fíjate en cómo un diafragma muy abierto (f/1.8) deja el fondo borroso y uno cerrado (f/16) enfoca desde la punta de tu nariz hasta el horizonte. Pregunta a Gemini: '¿Por qué los números de diafragma van al revés: cuanto más pequeño el número más grande es el agujero?'."),

        ("El Obturador de Cortinilla de Cámara Réflex",
         "Congelar una milésima de segundo: dos láminas de titanio corriendo como persianas a la velocidad del rayo.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte del interior del cuerpo de una cámara réflex analógica. Frente a la película de 35 mm, el espejo basculante se levanta en un relámpago hacia arriba. De inmediato, la primera cortinilla metálica de titanio se desplaza a altísima velocidad abriendo la ventana a la luz, seguida inmediatamente por la segunda cortinilla que viaja detrás cerrándola, creando una rendija luminosa móvil que expone el sensor en 1/2000 de segundo antes de que el espejo vuelva a bajar. Cámara superlenta con destello de luz.",
         "💡 Reto en el aula: A altas velocidades de disparo (1/4000 de segundo), la ventana nunca llega a estar abierta del todo: es solo una rendija delgada que barre la foto. Pregunta a Gemini: '¿Qué es la velocidad de sincronización del flash y por qué si disparas más rápido media foto sale negra?'."),

        ("El Compás Náutico con Suspensión Cardán",
         "La brújula que nunca se inclina: aros concéntricos que aíslan el rumbo del balanceo de las olas en alta mar.",
         "Crea un vídeo de 10 segundos: Animación 3D del funcionamiento de una bitácora y compás náutico de barco con suspensión Cardán en plena tormenta. La nave exterior de madera y bronce se inclina fuertemente hacia babor y estribor con las olas del mar. En su interior, tres anillos metálicos concéntricos pivotan libremente sobre ejes perpendiculares a 90 grados, manteniendo el plato esférico de la brújula con su rosa de los vientos perfectamente horizontal y flotando inmóvil en líquido amortiguador, apuntando imperturbable hacia el Norte magnético.",
         "💡 Reto en el aula: El sistema Cardán fue inventado por Gerolamo Cardano en el siglo XVI y hoy se usa en los estabilizadores de los teléfonos móviles (gimbals). Pregunta a Gemini: '¿Para qué sirven las dos grandes bolas de hierro macizo (esferas de Kelvin) colocadas a los lados del compás náutico?'."),

        ("El Micrómetro / Palmer de Precisión",
         "El tornillo maestro: cómo girar una rosca calibrada permite medir el grosor de un cabello humano en centésimas de milímetro.",
         "Crea un vídeo de 10 segundos: Animación 3D en macro de un micrómetro de precisión de taller mecánico midiendo una lámina metálica delgada. Se observa el tambor graduado girando suavemente con la carraca trasera; en su interior, un tornillo con rosca micrométrica avanza con paso exacto de 0,5 mm por vuelta. El husillo móvil se aproxima al yunque fijo hasta hacer contacto suave; las líneas de la escala graduada del cilindro y del tambor coinciden milimétricamente mostrando la lectura en micrómetros con iluminación técnica sobre cromo satinado.",
         "💡 Reto en el aula: Un tornillo común transforma vueltas en avance: con una rosca finísima, una vuelta entera solo avanza medio milímetro. Pregunta a Gemini: '¿Por qué la carraca del extremo salta con un clic cuando ya ha apretado lo justo para no deformar la pieza?'."),

        ("El Giroscopio de Navegación Aérea",
         "La inercia rotatoria: una rueda girando en el vacío que se niega a cambiar de orientación aunque el avión dé una vuelta de campana.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte del horizonte artificial giroscópico del panel de instrumentos de un avión. Un rotor metálico macizo gira a 24.000 revoluciones por minuto dentro de una jaula de cardanes equilibrados. Se observa cómo el avión maniobra, ladeando el fuselaje y subiendo el morro hacia las nubes, mientras el eje del giroscopio permanece rígidamente vertical e inmutable en el espacio, haciendo que la esfera con la línea del horizonte pinte con exactitud la inclinación real del vuelo. Iluminación tenue de cabina nocturna.",
         "💡 Reto en el aula: Las bicicletas no se caen cuando están en marcha precisamente por el efecto giroscópico de las ruedas al girar. Pregunta a Gemini: '¿Cómo usan los telescopios espaciales como el Hubble los giroscopios para apuntar a una estrella lejana sin usar motores de cohete?'."),

        # BLOQUE 4: FERROCARRIL Y GRANDES MÁQUINAS HISTÓRICAS (31 a 40)
        ("La Locomotora de Vapor (Biela, Pistón y Ruedas)",
         "La reina del siglo XIX: la presión del vapor empujando el émbolo para arrastrar miles de toneladas sobre raíles de hierro.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal del tren motriz de una locomotora de vapor clásica. El vapor a alta presión entra por la válvula corredera empujando el gran pistón horizontal dentro del cilindro. El vástago empuja la cruceta y la biela motriz principal acoplada a la muñequilla de la rueda motriz de acero gigante de dos metros. Las bielas de acoplamiento transmiten el giro sincronizado a las ruedas restantes mientras el mecanismo Walschaerts regula la marcha entre nubes de vapor blanco y chispas de carbón.",
         "💡 Reto en el aula: Fíjate en los contrapesos semicirculares de plomo en las ruedas gigantes: equilibran el peso descomunal de las bielas para que el tren no vibre. Pregunta a Gemini: '¿Cómo funcionaba el inversor de marcha que permitía al maquinista dar marcha atrás con solo mover una palanca?'."),

        ("El Freno de Aire Comprimido Westinghouse",
         "La seguridad invertida: si el tren se parte o se corta una manguera, el aire escapa y los frenos se clavan solos al instante.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte esquemático del sistema de freno neumático Westinghouse de un tren. Se ve la tubería general de aire a presión que recorre todos los vagones. Muestra cómo la válvula triple de cada vagón detecta una bajada de presión al frenar el maquinista, permitiendo que el aire almacenado en el depósito auxiliar entre de golpe en el cilindro de freno, empujando con tremenda fuerza las zapatas de fundición contra las ruedas de acero entre chispas de frenado. Mecánica ferroviaria pesada.",
         "💡 Reto en el aula: George Westinghouse revolucionó el mundo porque su freno es 'a prueba de fallos': la presión mantiene los frenos abiertos; si el tren se rompe, se frena solo. Pregunta a Gemini: '¿Cómo se frenaban los trenes antes de este invento con hombres corriendo por los techos de los vagones?'."),

        ("El Cambio de Agujas Ferroviario",
         "Guiar un tren a 100 km/h sin tocar el volante: cómo dos lengüetas de acero desvían las pestañas de las ruedas.",
         "Crea un vídeo de 10 segundos: Animación 3D en vista cenital y primer plano rasante del cambio de agujas de una vía de tren. Se aprecian los dos espadines afilados de acero deslizándose lateralmente sobre las placas de asiento movidos por una barra de tracción motorizada. Al pasar un tren, las pestañas interiores de las ruedas de acero son guiadas con suavidad por el espadín pegado hacia la vía desviada, cruzando el corazón del cruzamiento (ranura en cruz) con un traqueteo metálico rítmico y seguro. Iluminación realista sobre raíles relucientes y balasto de piedra.",
         "💡 Reto en el aula: Las ruedas de tren no son cilíndricas: son cónicas y tienen una pestaña interior que es la que se apoya en el raíl. Pregunta a Gemini: '¿Por qué en invierno se colocan calentadores de gas o resistencias eléctricas en las agujas de las vías de tren?'."),

        ("El Regulador Centrífugo de James Watt",
         "El primer 'robot' analógico de la historia: dos bolas de hierro que vuelan al girar para frenar la máquina si corre demasiado.",
         "Crea un vídeo de 10 segundos: Animación 3D del regulador de bolas centrífugo de una máquina de vapor de James Watt. Un eje vertical gira conectado al motor; dos brazos articulados con pesadas bolas macizas de bronce giran a gran velocidad. Al aumentar la velocidad, la fuerza centrífuga hace que las bolas se eleven y se separen hacia afuera, levantando un manguito deslizante que tira de una palanca cerrando parcialmente la válvula de mariposa del vapor, reduciendo la velocidad de forma automática y autorregulada. Movimiento armónico elegante.",
         "💡 Reto en el aula: Este mecanismo inventado en 1788 es el origen de la cibernética y el control automático moderno. Pregunta a Gemini: '¿De dónde viene la expresión popular en inglés 'to go balls out' (ir a toda máquina) relacionada con este invento?'."),

        ("La Prensa de Imprenta de Tornillo de Gutenberg",
         "El tornillo de husillo de madera que multiplicó el conocimiento humano prensando letras de plomo sobre papel de trapo.",
         "Crea un vídeo de 10 segundos: Animación 3D del funcionamiento de una imprenta de madera del siglo XV de Johannes Gutenberg. El operario pasa las balas de piel con tinta negra sobre los tipos móviles de plomo colocados en la galera. Se abate el tímpano con la hoja de papel de lino húmedo y se desliza bajo la platina. El impresor tira con fuerza de la palanca de madera haciendo girar el grueso tornillo de husillo central, que desciende verticalmente aplicando una presión uniforme y milimétrica sobre la hoja. Al retirar la palanca, se alza la hoja con el texto impreso nítido y perfecto.",
         "💡 Reto en el aula: Gutenberg no solo inventó la prensa, sino la aleación de plomo, estaño y antimonio que no se deformaba al enfriarse. Pregunta a Gemini: '¿Cuántos años se tardaba en copiar una Biblia a mano antes de que Gutenberg imprimiera 180 copias en tres años?'."),

        ("El Telar Mecánico y las Tarjetas Perforadas de Jacquard",
         "El abuelo del ordenador: tarjetas de cartón con agujeros que deciden qué hilos subir para tejer un dibujo complejo.",
         "Crea un vídeo de 10 segundos: Animación 3D del mecanismo de selección de un telar Jacquard del siglo XIX. Una cadena continua de tarjetas de cartón perforadas avanza girando sobre un prisma cuadrado. Un bloque de agujas palpadoras choca contra la tarjeta: las agujas que encuentran un agujero avanzan y levantan los ganchos que alzan los hilos correspondientes de la urdimbre de seda; las que chocan contra el cartón ciego se quedan abajo. La lanzadera cruza a toda velocidad entre la abertura tejiendo un patrón floral multicolor. Movimiento mecánico rítmico fascinante.",
         "💡 Reto en el aula: Ada Lovelace y Charles Babbage se inspiraron en las tarjetas perforadas de este telar para diseñar el primer programa informático. Pregunta a Gemini: '¿Por qué los tejedores franceses protestaron destruyendo telares en la revuelta de los 'Canuts'?'."),

        ("El Molino de Viento Harinero (Engranaje de Linterna)",
         "Girar la fuerza del cielo: cómo las aspas de lona transmiten su giro a 90 grados para mover una muela de piedra de dos toneladas.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte del interior de un molino de viento manchego tradicional. Las cuatro aspas con aspas de tela giran empujadas por el viento exterior, haciendo rotar el grueso eje horizontal de madera de encina. Una enorme rueda dentada de madera con dientes de carpe engrana sobre una rueda de linterna cilíndrica vertical (catalina), transformando el giro horizontal en vertical a mayor velocidad para hacer girar la muela de piedra superior sobre la piedra solera, moliendo los granos de trigo dorado en harina blanca fina que cae por la tolva.",
         "💡 Reto en el aula: Las piedras de moler nunca se tocan entre sí: flotan sobre una capa de granos de trigo; si se tocaran, soltarían chispas y el molino ardería por el polvo de harina. Pregunta a Gemini: '¿Cómo orientaban los molineros el techo entero del molino para encarar el viento?'."),

        ("La Noria de Sangre o de Agua Tradicional",
         "La ingeniería hidráulica andalusí: una cadena sin fin de vasijas de barro que sacan el agua de las entrañas de la tierra.",
         "Crea un vídeo de 10 segundos: Animación 3D del funcionamiento mecánico de una noria tradicional de agua. Un engranaje de madera de dos coronas de husillo transforma el giro horizontal del tiro en giro vertical. La gran rueda vertical gira lentamente sobre el pozo con dos cuerdas de esparto paralelas que sostienen decenas de arcaduces (cangilones de barro cocido). Cada vasija se sumerge en el agua subterránea, sube llena por el lateral y al llegar a la cúspide vuelca su contenido en una arqueta de piedra que alimenta la acequia de riego. Agua fresca fluyendo con reflejos de sol.",
         "💡 Reto en el aula: Las norias permitieron a nuestros antepasados cultivar huertos fértiles en mitad de tierras secas durante siglos. Pregunta a Gemini: '¿Qué diferencia hay entre una noria fluvial movida por la corriente de un río y una noria de tiro movida por un animal?'."),

        ("El Ascensor con Freno Paracaídas de Elisha Otis",
         "El invento que permitió crear los rascacielos: un resorte que clava cuñas en los raíles si el cable se corta.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte del pozo de un ascensor en el momento de una rotura de cable. Se ve la cabina suspendida con personas dentro; de repente, el cable de tracción superior se corta. Al perder tensión, un potente resorte de ballesta en el techo de la cabina se distiende de golpe, empujando dos brazos laterales que clavan cuñas dentadas de acero endurecido directamente contra las guías verticales de hierro del hueco, deteniendo la cabina en seco en pocos centímetros de forma totalmente automática y segura. Chispas metálicas y parada instantánea.",
         "💡 Reto en el aula: En 1854, Elisha Otis se subió a una plataforma elevada en Nueva York y ordenó cortar la cuerda con un hacha ante el público para demostrar que era imposible caerse. Pregunta a Gemini: '¿Cuántos cables independientes de acero sostienen un ascensor moderno hoy en día?'."),

        ("La Cruz de Malta o Mecanismo de Ginebra",
         "La ilusión del cine: convertir el giro continuo del motor en 24 paradas secas por segundo para proyectar cada fotograma.",
         "Crea un vídeo de 10 segundos: Animación 3D en macro del mecanismo de Cruz de Malta de un proyector de cine de 35 mm. Un disco motriz gira de forma continua con un pasador saliente. Al dar una vuelta, el pasador entra en una de las cuatro ranuras de una rueda con forma de cruz de Malta, haciéndola girar exactamente 90 grados en una fracción de segundo, y luego la rueda se bloquea inmóvil mientras el pasador completa el giro exterior. Muestra cómo la película avanza un fotograma a la vez y se detiene quieta frente a la lámpara de luz. Movimiento intermitente perfecto.",
         "💡 Reto en el aula: Si la película se moviera continuamente sin parar frente a la lente, en la pantalla solo veríamos un borrón ilegible. Pregunta a Gemini: '¿Por qué el ojo humano percibe 24 fotos fijas por segundo como un movimiento continuo y real (persistencia retiniana)?'."),

        # BLOQUE 5: AVIACIÓN Y NÁUTICA (41 a 50)
        ("Motor Turbofán de Reacción (Avión Comercial)",
         "Tragar aire, comprimirlo y quemarlo: las turbinas de titanio que empujan un Boeing o un Airbus a 900 km/h.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal del motor turbofán de un avión de pasajeros moderno. Las aspas gigantescas de titanio del ventilador frontal giran tragando toneladas de aire. Muestra el flujo dividido: el aire central entra a los compresores de alta presión girando en etapas decrecientes, entra a la cámara de combustión donde se mezcla con queroseno formando una llamarada continua a 1.500 °C, y escapa haciendo girar las turbinas traseras que mueven el eje, mientras el aire exterior frío pasa por el bypass generando el 80% del empuje silencioso. Movimiento de fluidos aerodinámicos.",
         "💡 Reto en el aula: La mayor parte del aire que empuja el avión no pasa por el fuego del motor, sino que va por fuera impulsado por la hélice gigante delantera. Pregunta a Gemini: '¿Por qué los motores modernos tienen ese perfil dentado (chevrones) en la salida trasera para reducir el ruido en los aeropuertos?'."),

        ("Perfil Alar y Mecanismo de Flaps en Despegue",
         "El principio de Bernoulli y la sustentación: cómo una lámina curvada crea una fuerza invisible que levanta 300 toneladas en el aire.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal del ala de un avión comercial maniobrando en la pista de despegue. Se observa el perfil aerodinámico de aluminio en corte con líneas de flujo de aire azul dividiéndose: el aire superior viaja más rápido creando una zona de baja presión que 'succiona' el ala hacia arriba. Mediante cilindros hidráulicos y tornillos sin fin, los flaps y slats de borde de ataque se extienden y bajan curvando el ala y aumentando su superficie para generar una sustentación gigantesca a baja velocidad. Movimiento aerodinámico impecable.",
         "💡 Reto en el aula: Un avión vuela porque el aire de arriba va más deprisa que el de abajo, succionando el ala hacia el cielo. Pregunta a Gemini: '¿Qué son los 'winglets' (las aletas verticales que llevan los aviones en la punta de las alas) y cuánto combustible ahorran?'."),

        ("Tren de Aterrizaje Retráctil y Amortiguador Oleoneumático",
         "Plegar las patas como un pájaro: cilindros hidráulicos que doblan las ruedas gigantes dentro de la panza del fuselaje.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte del tren de aterrizaje principal de un avión despegando. En cuanto las ruedas despegan del suelo, los potentes gatos hidráulicos retraen el pesado soporte de acero y titanio, plegando los bogies con ruedas gemelas hacia arriba dentro del pozo del fuselaje, mientras las compuertas aerodinámicas se cierran herméticamente dejando el vientre del avión totalmente liso. Detalle del amortiguador de gas nitrógeno y aceite absorbiendo el impacto previo de la pista. Movimiento mecánico majestuoso.",
         "💡 Reto en el aula: El amortiguador del tren no lleva muelles de metal: usa gas nitrógeno comprimido y aceite, capaz de aguantar el impacto de un aterrizaje brusco a 250 km/h. Pregunta a Gemini: '¿Cómo se asegura el tren de aterrizaje para que sea imposible que se pliegue por error mientras el avión está en tierra?'."),

        ("El Rotor de Cola de un Helicóptero",
         "La tercera ley de Newton en el aire: si la hélice grande gira a la derecha, el helicóptero quiere girar a la izquierda.",
         "Crea un vídeo de 10 segundos: Animación 3D del rotor de cola de un helicóptero en vuelo. Se ve el rotor principal superior girando; para contrarrestar el par de torsión que haría girar el fuselaje sin control, un eje de transmisión de alta velocidad recorre el botalón de cola hasta una caja de engranajes a 90 grados que hace girar la pequeña hélice vertical de cola. Se muestra cómo el piloto mueve los pedales variando el ángulo de las palas mediante un plato oscilante, empujando más o menos aire lateral para orientar el morro del helicóptero con precisión en el aire.",
         "💡 Reto en el aula: Sin el pequeño rotor de cola, un helicóptero empezaría a dar vueltas como una peonza descontrolada en cuanto despegara. Pregunta a Gemini: '¿Cómo vuelan los helicópteros como el Chinook que tienen dos hélices gigantes pero no llevan rotor de cola?'."),

        ("Tanques de Lastre de un Submarino",
         "El principio de Arquímedes en las profundidades: inundar con agua de mar para hundirse o soplar aire para flotar.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal del casco doble de un submarino navegando en el océano. Para sumergirse, las válvulas superiores de venteo se abren liberando el aire, permitiendo que el agua marina entre torrencialmente por las aberturas inferiores llenando los tanques de lastre laterales y haciendo que el submarino pese más y se sumerja con elegancia. A continuación, para emerger, bancos de botellas de aire comprimido a 200 bares expulsan el agua de mar hacia abajo vaciando los tanques, devolviendo la flotabilidad positiva que eleva la nave a la superficie entre espuma marina.",
         "💡 Reto en el aula: Un submarino bajo el agua ajusta su peso exactamente igual al del agua que desaloja para quedarse inmóvil flotando a la profundidad que desee. Pregunta a Gemini: '¿Qué son los planos de inmersión y cómo funcionan como alas bajo el agua?'."),

        ("La Hélice Marina de Paso Variable",
         "Marcha atrás sin tocar el motor: girar las palas de bronce como abanicos para frenar un barco de 100.000 toneladas.",
         "Crea un vídeo de 10 segundos: Animación 3D submarina en corte del buje de la hélice de un gran buque. Las cuatro palas gigantescas de bronce-aluminio están ancladas en un núcleo central hermético. Un pistón servohidráulico interno se desplaza longitudinalmente dentro del eje, rotando las palas sobre su propio eje vertical: de empuje hacia adelante (inclinación positiva) pasan suavemente a posición neutra y luego a inclinación inversa, empujando el agua hacia proa para frenar y dar marcha atrás al buque mientras el motor diésel sigue girando siempre en el mismo sentido y a velocidad constante.",
         "💡 Reto en el aula: Los motores marinos gigantescos son tan descomunales que invertir su giro costaría minutos; con la hélice de paso variable la respuesta es inmediata. Pregunta a Gemini: '¿Qué es la cavitación marina y por qué las burbujas que crea la hélice pueden taladrar el metal más duro?'."),

        ("Las Esclusas del Canal de Panamá",
         "Un ascensor de agua para gigantes de los mares: subir un carguero a 26 metros de altura usando solo la gravedad.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte y vista aérea seccional de un juego de esclusas del Canal de Panamá. Un inmenso barco portacontenedores entra en la cámara cerrada por dos compuertas rodantes gigantescas de acero. Se abren las compuertas de alcantarilla inferiores: millones de litros de agua dulce del lago Gatún entran por gravedad desde abajo sin bombas eléctricas, elevando el nivel del agua y alzando el navío suavemente varios metros hasta igualar la altura de la siguiente cámara, abriéndose la compuerta para permitir su paso hacia el Océano Pacífico. Flujo de agua colosal y maniobra milimétrica.",
         "💡 Reto en el aula: En todo el Canal de Panamá no se usa ni una sola bomba de agua para llenar las esclusas: toda el agua baja sola por gravedad desde las montañas. Pregunta a Gemini: '¿Cuánto tiempo tarda un barco en cruzar del Atlántico al Pacífico y cuánta agua se vierte al mar en cada paso?'."),

        ("El Cabrestante y Barbotén del Ancla de un Barco",
         "Domar 30 toneladas de cadena forjada: cómo una rueda dentada acanalada frena y cobra el ancla de fondeo en el abismo marino.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte del molinete de anclas en la proa de un buque mercante. En la cubierta, el motor hidráulico hace girar con fuerza un barbotén de fundición de acero con hendiduras que abrazan exactamente los eslabones gigantes de la cadena con contrete. Se ve la cadena de acero de 100 mm rodando eslabón a eslabón, pasando por el escobén hacia el agua profunda, mientras el marinero aprieta la rueda del freno de cinta con ferodo para regular la velocidad de fondeo bajo el rocío del mar. Potencia mecánica pesada sobre metal desgastado.",
         "💡 Reto en el aula: Los eslabones llevan una barra central llamada 'contrete' para que no se aplasten bajo la tensión y no se enrollen entre sí. Pregunta a Gemini: '¿Qué es lo que realmente sujeta el barco al fondear: el ancla clavada o el peso descomunal de la cadena tendida en el fondo del mar?'."),

        ("El Tubo Pitot y la Sonda de Velocidad Aérea",
         "El lápiz del viento: cómo comparar el aire que entra a presión con el aire estático le dice al piloto si va a caer en pérdida.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal del tubo Pitot instalado en el morro de un avión comercial volando entre nubes. Se observa el orificio frontal por donde entra el aire de impacto del viento dinámico, y los orificios laterales por donde se mide la presión estática del ambiente. En el interior de la sonda calefactada por resistencias eléctricas contra el hielo, dos conductos de aire llegan a una membrana metálica de presión diferencial que se deforma con precisión, enviando la señal analógica convertida en nudos de velocidad aérea al ordenador de vuelo. Iluminación técnica de instrumentación.",
         "💡 Reto en el aula: Si el tubo Pitot se congela o se tapa por una avispa, el velocímetro del avión marca cero aunque vuele a 800 km/h. Pregunta a Gemini: '¿Qué papel jugó la congelación de los tubos Pitot en el trágico accidente del vuelo Air France 447 sobre el Atlántico?'."),

        ("El Paracaídas y su Muelle Extractor",
         "La cadena de salvamento aéreo: un pequeño paracaídas piloto impulsado por un muelle que tira de la campana principal.",
         "Crea un vídeo de 10 segundos: Animación 3D a cámara lenta de la apertura de un paracaídas de rescate en la espalda de un saltador en caída libre. Al tirar de la anilla, las solapas de la mochila se abren liberando un resorte metálico helicoidal que expulsa con fuerza hacia el viento exterior un pequeño paracaídas piloto (flamenca). En una fracción de segundo, el piloto se infla con el viento relativo y tira con fuerza de la cuerda de despliegue, extrayendo la bolsa con las cuerdas de suspensión ordenadas y abriendo la gran campana de nailon de colores en un despliegue suave y perfecto que frena la caída.",
         "💡 Reto en el aula: Las cuerdas del paracaídas están empaquetadas en zig-zag sujetas con pequeñas gomas elásticas para que se abran una a una sin enredarse. Pregunta a Gemini: '¿Cómo funciona el dispositivo de apertura barométrica automática (AAD) que abre el paracaídas solo si el saltador se desmaya?'."),

        # BLOQUE 6: HERRAMIENTAS, CONSTRUCCIÓN E HIDRÁULICA (51 a 60)
        ("El Gato Hidráulico de Botella",
         "La magia de Blaise Pascal: bombear con la fuerza de una mano para elevar un camión de cinco toneladas.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal de un gato hidráulico de taller levantando un vehículo. Se ve la palanca manual bombeando un pistón muy delgado de pequeño diámetro; con cada embolada, aspira aceite del depósito exterior y lo empuja a través de una válvula de retención de bola de acero hacia la base de un cilindro principal diez veces más ancho. Al tener mayor superficie, la presión del aceite se multiplica por diez, haciendo que el vástago macizo central de acero ascienda milímetro a milímetro levantando el chasis sin esfuerzo. Iluminación de taller limpia con fluido hidráulico transparente.",
         "💡 Reto en el aula: La presión es la misma en todo el fluido: si empujas un centímetro cuadrado con 10 kg, un pistón de 100 centímetros cuadrados empuja 1.000 kg. Pregunta a Gemini: '¿Cómo se abre la válvula de purga manual para que el aceite regrese al depósito y el coche baje despacio?'."),

        ("El Brazo Articulado de una Excavadora Hidráulica",
         "Músculos de acero y aceite a 300 bares: cilindros hidráulicos de doble efecto excavando roca sólida.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte y vista lateral del brazo articulado de una excavadora pesada en una obra. Se muestran los tres grandes cilindros hidráulicos telescópicos cromados accionando la pluma, el balancín y el cucharón de dientes de acero. En el interior del cilindro se observa el aceite a alta presión entrando por una lumbrera empujando el pistón con juntas de poliuretano, mientras el aceite del otro lado retorna al tanque, extendiendo el vástago con una fuerza colosal que clava los dientes en la tierra y levanta una tonelada de roca con movimientos milimétricos controlados por joysticks.",
         "💡 Reto en el aula: Una excavadora no tiene cables ni cadenas: todo su movimiento depende exclusivamente de tubos de goma reforzada con acero y aceite a presión. Pregunta a Gemini: '¿Qué pasa si se rompe un latiguillo hidráulico y qué válvulas paracaídas llevan para que la pala no caiga a plomo?'."),

        ("El Taladro Percutor con Ruedas de Trinquete",
         "Girar y golpear a la vez: dos discos con dientes de sierra saltando uno sobre otro a 40.000 impactos por minuto para agujerear hormigón.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transparente del cabezal de un taladro percutor doméstico perforando un bloque de hormigón. El motor eléctrico hace girar el eje porta-brocas a 3.000 rpm; al seleccionar el modo percutor, dos discos de acero cementado enfrentados con dientes de sierra inclinados entran en contacto. Al apretar contra la pared, los dientes van cabalgando y saltando unos sobre otros, provocando que la broca de widia gire y retroceda y avance milimétricamente miles de veces por minuto, pulverizando la piedra con micro-impactos continuos. Iluminación técnica con chispas de polvo mineral.",
         "💡 Reto en el aula: Un taladro normal solo gira y quema la broca contra el ladrillo; el percutor añade martillazos continuos que fracturan el material. Pregunta a Gemini: '¿Qué diferencia hay entre un taladro percutor mecánico casero y un martillo perforador neumático profesional (SDS)?'."),

        ("La Llave de Carraca con Trinquete Reversible",
         "Apretar sin soltar la tuerca: una rueda dentada y una uñeta que permiten girar con fuerza en un sentido y resbalar libremente al volver.",
         "Crea un vídeo de 10 segundos: Animación 3D en primerísimo plano macro y corte mecánico de la cabeza de una llave de carraca de vaso apretando un tornillo de motor. Se ve la rueda dentada interior de acero al cromo-vanadio con 72 dientes diminutos. Una uñeta basculante empujada por un muelle de alambre se clava en los dientes transmitiendo todo el par de apriete cuando la mano empuja; al retroceder el mango, los dientes inclinados hacen resbalar la uñeta hacia arriba produciendo un suave chasquido metálico ('clic-clic-clic') sin mover el tornillo. Se observa la palanca inversora cambiando el sentido de apriete.",
         "💡 Reto en el aula: Cuantos más dientes tiene la corona (ej. 72 dientes), menos ángulo necesitas mover la llave (solo 5 grados) para apretar en sitios estrechos. Pregunta a Gemini: '¿Por qué nunca se debe golpear una llave de carraca con un martillo para aflojar un tornillo atascado?'."),

        ("El Polipasto de Múltiples Poleas (Aparejo Factorial)",
         "Multiplicar la fuerza con cuerdas: cómo cuatro poleas dividen el peso por cuatro permitiendo levantar un motor con dos dedos.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte del funcionamiento de un aparejo de poleas compuesto en un taller mecánico levantando un motor pesado de 400 kg. Se ven dos poleas fijas en el techo y dos poleas móviles ancladas al gancho del motor. Una cuerda de cáñamo recorre en zig-zag todas las ruedas giratorias de bronce sobre rodamientos de bolas. Se observa cómo la mano de un operario tira del cabo aplicando solo 100 kg de fuerza; la tensión se reparte por igual entre los cuatro ramales de cuerda que sostienen la carga, elevando el motor con suavidad y equilibrio.",
         "💡 Reto en el aula: La energía se conserva: haces la cuarta parte de fuerza, pero tienes que tirar de cuatro veces más metros de cuerda. Pregunta a Gemini: '¿Cómo usaban Arquímedes y los antiguos marineros griegos los polipastos para botar al mar barcos gigantescos ellos solos?'."),

        ("Motosierra con Embrague Centrífugo de Zapatas",
         "Seguridad total al ralentí: los contrapesos que solo tocan la campana y mueven la cadena cuando aceleras el motor.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal del embrague centrífugo de una motosierra de gasolina. Al ralentí, el cigüeñal gira despacio; dos zapatas curvas metálicas unidas por resortes de tracción permanecen recogidas hacia adentro, dejando la campana exterior y el piñón de la cadena totalmente parados e inmóviles por seguridad. Cuando el operario aprieta el gatillo del acelerador y el motor sube de revoluciones, la fuerza centrífuga supera la resistencia de los muelles, arrojando las zapatas hacia afuera contra el tambor de acero, acoplándose por fricción y haciendo girar la cadena dentada a toda velocidad entre serrín volante.",
         "💡 Reto en el aula: Si la cadena se atasca en un tronco, el embrague patina para que el motor no se cale ni rompa la máquina. Pregunta a Gemini: '¿Qué otros vehículos sin marchas como los ciclomotores Vespino o los karts usan embrague centrífugo?'."),

        ("La Prensa Hidráulica Industrial (El Cilindro Aplastador)",
         "El monstruo silencioso: una bomba de pistones axiales que genera 500 toneladas para estampar la aleta de un coche en chapa de acero.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte de una colosal prensa hidráulica de estampación de automóviles. Se observa el depósito superior y el émbolo macizo de acero forjado de un metro de diámetro. Las electroválvulas abren paso al fluido hidráulico a 350 bares de presión; el cilindro desciende con lentitud inexorable y silenciosa sobre una chapa plana de acero colocada sobre una matriz inferior, deformando y moldeando el metal frío en una sola pulsación perfecta para crear el capó curvado de un automóvil sin una sola arruga. Presión colosal y precisión milimétrica.",
         "💡 Reto en el aula: El aceite no se puede comprimir: si empujas un litro por un tubo estrecho, ese litro entero empuja al otro lado con la fuerza de un titán. Pregunta a Gemini: '¿Quién fue Joseph Bramah y cómo patentó la primera prensa hidráulica en 1795 revolucionando la industria moderna?'."),

        ("Válvula Antirretorno de Clapeta y Bola",
         "La aduana del agua: una puerta de una sola dirección que deja pasar el líquido hacia adelante pero se sella con el retroceso.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transparente de una válvula antirretorno de fontanería instalada en una tubería de agua. Cuando la bomba impulsa el agua limpia hacia la derecha, la corriente empuja con suavidad una clapeta basculante de bronce con junta de goma, abriendo el paso sin resistencia. En cuanto la bomba se detiene y el agua intenta retroceder por gravedad hacia la izquierda, la propia presión del reflujo empuja la clapeta de golpe contra su asiento biselado sellando herméticamente el conducto en un milisegundo e impidiendo que la tubería se vacíe. Agua cristalina fluyendo con dinamismo.",
         "💡 Reto en el aula: Sin esta válvula en el pozo, cada vez que encendieras el grifo la bomba tendría que volver a cebarse y aspirar aire durante minutos. Pregunta a Gemini: '¿Sabías que nuestras propias venas tienen millones de válvulas antirretorno idénticas a esta para que la sangre no caiga a los pies?'."),

        ("Sierra de Calar con Mecanismo de Yugo Escocés",
         "Transformar el círculo en línea recta pura: cómo una manivela deslizante convierte giros de motor en vaivén sin desvíos laterales.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transparente del mecanismo interior de una sierra de calar de carpintería. El piñón del motor eléctrico hace girar una rueda excéntrica con un rodamiento saliente (manivela). Este rodamiento viaja encajado deslizándose horizontalmente dentro de la ranura transversal de un soporte de acero en forma de cruz (yugo escocés). A medida que la rueda gira, el yugo transforma el giro circular en un movimiento vertical rectilíneo puro arriba y abajo del porta-hojas, haciendo que la fina sierra de dientes afilados corte una tabla de madera de pino a gran velocidad. Mecánica de corte limpia.",
         "💡 Reto en el aula: A diferencia de una biela normal que empuja la hoja de lado a lado torciendo el corte, el yugo escocés sube y baja en línea recta matemática absoluta. Pregunta a Gemini: '¿Por qué algunas sierras de calar tienen 'movimiento pendular' que empuja la hoja hacia adelante solo cuando sube?'."),

        ("El Soplete de Oxiacetileno de Corte y Soldadura",
         "Química y mecánica de gases: mezclar oxígeno y gas inflamable en una boquilla concéntrica para fundir hierro a 3.200 °C.",
         "Crea un vídeo de 10 segundos: Animación 3D en corte transversal de la empuñadura y boquilla de un soplete de soldadura autógena de oxiacetileno. Se ven las dos mangueras (roja para acetileno y azul para oxígeno) entrando a la cámara de mezcla con válvulas de aguja de latón finamente reguladas. Los gases se combinan y viajan por la boquilla concéntrica de cobre; al salir, se observa el dardo de llama azul turquesa brillante alcanzando 3.200 grados centígrados, y cómo al apretar la palanca central se inyecta un chorro de oxígeno puro a presión por el centro que oxida y desintegra una viga de acero fundiéndola en una cascada de chispas incandescentes doradas.",
         "💡 Reto en el aula: El soplete no solo derrite el metal con calor: el chorro de oxígeno puro literalmente 'quema' el hierro convirtiéndolo en óxido líquido que sale despedido. Pregunta a Gemini: '¿Por qué se usan gafas oscuras especiales para soldar con soplete y qué peligro tiene mirar la llama sin protección?'."),
    ]

    for idx, (title, concept, prompt, tips) in enumerate(mecanismos, 1):
        items.append({
            'num_int': idx,
            'id_code': f"[MEC-{idx:03d}]",
            'block_dir': '14. [MEC] BLOQUE_14_COMO_FUNCIONAN_LAS_COSAS',
            'block_name': 'BLOQUE 14: CÓMO FUNCIONAN LAS COSAS (Ingeniería y Mecánica en Vídeo 3D)',
            'title': title,
            'concept': concept,
            'prompt': prompt,
            'tips': tips
        })

    return items

if __name__ == "__main__":
    items = get_mecanica_items()
    print(f"✅ Cargados {len(items)} mecanismos mecánicos en [MEC]")
    print("Ejemplo 1:", items[0]['title'])
    print("Ejemplo 26:", items[25]['title'])
    print("Ejemplo 60:", items[59]['title'])
