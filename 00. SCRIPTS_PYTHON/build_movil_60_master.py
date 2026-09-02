# -*- coding: utf-8 -*-
"""
Generador Maestro del Bloque 12: [MOVIL] EL SALVAVIDAS COTIDIANO (60 Ítems)
Dinámica interactiva:
1. En el PC: Generar con Gemini una imagen hiperrealista de una situación cotidiana compleja.
2. Con el Móvil: El alumno enfoca la pantalla del PC con la cámara de Gemini y formula la pregunta de salvavidas por voz.
"""

def get_movil_items():
    movil_list = []

    retos = [
        # 1. ELECTRODOMÉSTICOS Y COCINA (01-10)
        ("Símbolos de Lavado Textil: Jersey delicado de lana",
         "Aprender a interpretar etiquetas de ropa fotografiando los símbolos crípticos de lavado para no arruinar prendas.",
         "Fotografía en primer plano macro de la etiqueta interior de un jersey de lana beige, con 5 símbolos de cuidado textil impresos en negro: barreño de agua a 30 grados, tina tachada, plancha con un punto, círculo tachado y cuadrado con círculo tachado. Fondo textil realista, iluminación de estudio limpia, sin textos en inglés.",
         "Enfoca con la cámara de Gemini en tu móvil la pantalla del PC y pregúntale por voz: 'Gemini, mira esta etiqueta. ¿Puedo meter este jersey en la lavadora o se me va a encoger? ¿Puedo usar secadora?'."),

        ("Panel de Lavadora Moderna: Selector de programas y centrifugado",
         "Descifrar el panel de mandos con dial giratorio y botones de una lavadora moderna para elegir el programa correcto.",
         "Primer plano frontal nítido del panel de control de una lavadora moderna blanca, mostrando la rueda selectora con programas en español: Algodón, Sintéticos, Delicados, Lana, Rápido 15 min, y pantalla digital que marca 1200 rpm y 40 grados. Acabado metálico realista, números legibles, sin textos en inglés.",
         "Apunta con la cámara de tu móvil al panel y di: 'Gemini, tengo que lavar una colcha fina que no quiero que se estropee, ¿qué programa y cuántas revoluciones me recomiendas poner según esta rueda?'."),

        ("Vitrocerámica Táctil: Código de bloqueo infantil 'L'",
         "Resolver el bloqueo accidental de la placa de inducción o vitrocerámica cuando aparece el símbolo 'L' o llave.",
         "Plano cenital en primer plano de los mandos táctiles de una placa vitrocerámica negra de cristal brillante, con los 4 fuegos apagados y en el display digital central una letra 'L' roja brillante encendida junto al icono de un candado. Iluminación realista de cocina, superficie limpia, sin textos en inglés.",
         "Abre la app de Gemini en el móvil, enfoca la pantalla y pregunta: 'Gemini, se me ha quedado la vitrocerámica bloqueada con esta letra L roja y no calienta, ¿cómo la desbloqueo con los dedos?'."),

        ("Microondas Digital: Descongelar por peso o tiempo",
         "Aprender a usar los botones de descongelación adecuada en el microondas sin cocinar los bordes de la comida.",
         "Panel frontal de control de un microondas de acero inoxidable pulido, con botones táctiles en español: Descongelar por peso (g), Descongelar por tiempo, Potencia, Inicio rápido +30s, y pantalla verde marcando '00:00'. Botones con iconos claros y números grandes y legibles.",
         "Fotografía la pantalla con el móvil y dile a Gemini: 'Quiero descongelar medio kilo de filetes de ternera, ¿qué botón tengo que apretar y cuánto tiempo le pongo para que no se me cocinen?'."),

        ("Lavavajillas: Aviso de falta de sal o abrillantador",
         "Identificar los pilotos rojos con forma de 'S' entrelazada o 'sol de chispas' en el lavavajillas.",
         "Fotografía detallada del borde superior de la puerta de un lavavajillas de acero inox, con dos pilotos luminosos rojos encendidos: uno con forma de dos flechas onduladas en 'S' (sal) y otro con forma de sol radiante de copos (abrillantador). Letras en español, nítido y realista.",
         "Apunta al lavavajillas con el móvil y pregunta: 'Gemini, se me han encendido estas dos luces rojas en el lavavajillas, ¿qué significan y qué producto tengo que rellenar?'."),

        ("Mando de Aire Acondicionado: Modo bomba de calor vs frío",
         "Distinguir el icono de sol (calefacción) del copo de nieve (frío) o la gota (deshumidificador) en mandos de clima.",
         "Primer plano de la pantalla LCD de un mando a distancia de aire acondicionado blanco, mostrando varios iconos pequeños: un sol, un copo de nieve, una gota de agua y un ventilador, con una temperatura marcada de 24°C y flechas de subir/bajar. Pantalla iluminada nítida y legible.",
         "Hazle una foto a la pantalla con el móvil y pregúntale: 'Gemini, hace frío en casa y quiero poner la calefacción, ¿qué icono de los que se ven en este mando es el de dar calor y a cuántos grados lo pongo?'."),

        ("Caldera de Gas: Presión a 0.5 bar y luz roja",
         "Interpretar la aguja del manómetro de la caldera para saber cuándo le falta agua al circuito de calefacción.",
         "Fotografía realista de la parte inferior de una caldera de gas mural blanca, mostrando un manómetro circular de aguja situado en la zona roja baja marcando 0.5 bar, junto a un testigo luminoso rojo de advertencia y una llave de paso negra debajo. Indicadores nítidos y claros.",
         "Enfoca con el móvil y di por voz: 'Gemini, mira este reloj de la caldera, la aguja está en el 0.5 y tiene luz roja, ¿qué le pasa a la calefacción y qué llave tengo que girar para meterle agua?'."),

        ("Cuadro Eléctrico: Diferencial general saltado",
         "Saber qué palanca ha saltado en el cuadro de luces de casa cuando se va la electricidad y cómo rearmarla.",
         "Fotografía de un cuadro de fusibles e interruptores magnetotérmicos doméstico blanco abierto, con varios interruptores negros subidos en posición 'ON' y el interruptor diferencial principal más ancho con botón de test con la palanca hacia abajo en posición 'OFF'. Etiquetas rotuladas en español: General, Enchufes, Alumbrado.",
         "Apunta con tu móvil al cuadro y pregunta a Gemini: 'Se me ha ido la luz en toda la casa, mira la foto, ¿cuál es la palanca que ha saltado y qué tengo que hacer para que vuelva la corriente con seguridad?'."),

        ("Robot Aspirador: Luz amarilla y aviso de cepillo atascado",
         "Descifrar los códigos lumínicos del robot de limpieza para retirar pelos o hilos del rodillo central.",
         "Vista superior en primer plano de un robot aspirador circular negro mate en su base de carga, con un anillo de luz led pulsando en color naranja y un icono con forma de cepillo giratorio iluminado en rojo. Superficie nítida, acabado moderno y limpio.",
         "Saca el móvil, apunta al robot y di: 'Gemini, el robot aspirador se ha parado con esta luz naranja parpadeante, ¿por qué no limpia y qué pieza tengo que soltar para revisarlo?'."),

        ("Cafetera Exprés: Testigo de descalcificación encendido",
         "Reconocer el piloto de cal en cafeteras de cápsulas o automáticas y saber cómo hacer la limpieza.",
         "Panel frontal de una cafetera automática doméstica con los botones de café corto y café largo apagados, y un botón inferior con el icono de tres gotas de agua y una espiral encendido en color naranja fijo. Acabado cromado elegante y nítido.",
         "Enfoca con el móvil y pregunta por voz: 'Gemini, mira este botón naranja con gotas en mi cafetera, ¿qué me está pidiendo que haga y cómo le quito la cal?'."),

        # 2. FACTURAS, BANCOS Y DOCUMENTOS (11-18)
        ("Factura de la Luz: Término de potencia vs consumo de energía",
         "Entender el recibo eléctrico distinguiendo lo que pagamos fijo por potencia de los kilovatios realmente consumidos.",
         "Primer plano de un fragmento de una factura eléctrica en papel en español, con un cuadro destacado que muestra: 'Potencia contratada: 4.6 kW - Importe: 18.50 €' y debajo 'Energía consumida: 140 kWh - Importe: 22.30 €' con el total a pagar y gráfico de barras mensual. Texto nítido y legible.",
         "Fotografía la factura con el móvil y dile a Gemini: 'Gemini, explícame en cristiano esta factura: ¿cuánto estoy pagando de fijo aunque no encienda una bombilla y qué significa la potencia contratada?'."),

        ("Factura del Gas: Lectura estimada vs lectura real",
         "Detectar si la compañía de gas nos está cobrando de más por una estimación o por el consumo del contador.",
         "Fragmento de factura de gas natural en español con tabla comparativa de lecturas: 'Lectura anterior (Real): 12.340 m³' y 'Lectura actual (Estimada): 12.510 m³', con una advertencia en recuadro que indica consumo facturado por estimación. Tipografía impresa nítida.",
         "Pregunta a Gemini con el móvil: 'Gemini, mira estas dos lecturas de mi factura de gas, ¿me están cobrando lo que he gastado de verdad o se lo han inventado por estimación?'."),

        ("Factura de Teléfono: Cargo adicional por SMS premium o suscripción",
         "Identificar cargos sorpresa en la factura del móvil por servicios de tarificación especial no solicitados.",
         "Detalle de factura telefónica móvil impresa en papel, mostrando la cuota mensual de 20 € y un apartado de 'Otros servicios / Pagos a terceros: 8.99 € (Suscripción Juegos Online / SMS Premium)'. Total a pagar destacado con círculo rojo.",
         "Apunta al papel y di: 'Gemini, me han cobrado casi 9 euros de más en el móvil por algo de pagos a terceros que yo no he pedido, ¿qué es esto y qué tengo que decirle a la compañía para que lo cancelen ya?'."),

        ("Ticket de Compra: Cobro duplicado en la caja del supermercado",
         "Aprender a revisar un ticket largo de supermercado con la cámara del móvil para detectar errores de cobro.",
         "Primer plano de un ticket de papel térmico de supermercado español con lista de artículos: Leche desnatada 1.05 €, Plátanos de Canarias 2.40 €, Aceite de oliva 8.50 €, Aceite de oliva 8.50 € (dos líneas idénticas consecutivas marcadas con flecha), Pan de barra 0.65 €. Tipografía térmica nítida.",
         "Enfoca el ticket con el móvil y dile a Gemini: 'Gemini, revisa este ticket del súper, ¿me han cobrado dos veces el aceite de oliva sin darme cuenta?'."),

        ("Carta del Banco: Modificación de comisiones de mantenimiento",
         "Traducir la jerga bancaria para saber si nos van a cobrar por la libreta de ahorros o tarjeta.",
         "Fragmento de una carta bancaria formal en papel membretado en español, con un párrafo redactado en lenguaje legal: 'Le comunicamos que a partir del 1 de octubre la comisión de administración y mantenimiento de su cuenta corriente será de 60 € semestrales salvo que mantenga domiciliada su pensión y tres recibos...'.",
         "Hazle una foto a la carta con el móvil y pregúntale: 'Gemini, tradúceme esta carta del banco a lenguaje de la calle: ¿cuánto me van a cobrar de comisión y qué tengo que hacer para que no me quiten ni un euro?'."),

        ("Multa de Estacionamiento: Plazo y descuento del 50% por pronto pago",
         "Revisar una notificación de tráfico para localizar el importe con descuento y la fecha límite de abono.",
         "Notificación municipal de denuncia de estacionamiento regulado (zona azul) en papel oficial, con número de expediente, matrícula, importe de 'Sanción: 90,00 €' y en negrita 'Importe reducido con el 50% de descuento: 45,00 € abonando en los primeros 20 días naturales'.",
         "Apunta con el móvil y pregunta: 'Gemini, mira esta multa que me han puesto, ¿cuál es el importe reducido que tengo que pagar si lo hago rápido y cuántos días tengo antes de perder el descuento?'."),

        ("Impreso de Tasas Municipales: Código de barras y modelo 046",
         "Localizar los datos necesarios para pagar una tasa de vado, basuras o certificado en el cajero del banco.",
         "Documento de autoliquidación de tasa municipal modelo 046 en papel, mostrando el campo 'Identificación del sujeto pasivo', 'Concepto: Expedición de documento', un código de barras ancho en la base con los números de Emisora, Sufijo y Referencia, y el importe de 12.40 €.",
         "Enfoca el papel con el móvil y di: 'Gemini, tengo que pagar este papel en el cajero del banco y no sé qué números meter, ¿dónde está el código de barras y la referencia que me pide la máquina?'."),

        ("Certificado de Pensión e IRPF: Retención y pensión neta",
         "Comprender el certificado anual de revalorización de la pensión y las retenciones de Hacienda.",
         "Fragmento de documento oficial de la Seguridad Social con la revalorización de la pensión: 'Pensión mensual íntegra: 1.250,00 €', 'Porcentaje de retención IRPF: 8.5% (-106.25 €)', 'Líquido a percibir: 1.143,75 €'. Tabulación clara y sellos oficiales simulados.",
         "Pregunta a Gemini con el móvil: 'Gemini, mira esta carta de mi pensión, ¿cuánto es lo que gano en bruto y cuánto me retiene Hacienda cada mes antes de ingresarme el dinero en el banco?'."),

        # 3. SALUD, FARMACIA Y BIENESTAR (19-26)
        ("Prospecto de Colirio: Caducidad tras apertura y dosificación",
         "Buscar rápidamente en un prospecto de letra minúscula cuántos días dura el bote abierto y cómo aplicarlo.",
         "Fotografía en plano macro del prospecto en papel plegado de un frasco de gotas oculares (colirio), destacando en un recuadro: 'Posología: Instilar 1 gota en cada ojo cada 12 horas. Caducidad: Desechar el frasco transcurridos 28 días tras su primera apertura'. Letra muy pequeña pero nítida.",
         "Enfoca el prospecto con el móvil y pregúntale por voz: 'Gemini, la letra es enana y no la veo bien: ¿cuántas gotas me tengo que echar al día y cuántas semanas dura el bote una vez abierto?'."),

        ("Caja de Medicamento: Pictograma de conducción de vehículos",
         "Identificar el triángulo rojo de advertencia con un coche dentro en las cajas de medicamentos para dormir o calmar el dolor.",
         "Fotografía de la cara frontal de una caja de pastillas tranquilizantes o analgésicos, mostrando el nombre del fármaco y en la esquina inferior un pictograma triangular blanco con borde rojo y el dibujo negro de un coche en su interior junto al texto 'Medicamento que puede reducir la capacidad de conducir'.",
         "Apunta a la caja con tu móvil y di: 'Gemini, mira este triángulo con un coche en la caja de estas pastillas, ¿puedo coger el coche si me tomo una o me da somnolencia?'."),

        ("Envase de Jarabe: Fecha de caducidad estampada en relieve",
         "Leer fechas de lote y caducidad grabadas sin tinta en el plástico o tapa de un envase de farmacia.",
         "Fotografía en primer plano con luz lateral del cuello y tapón blanco de un frasco de jarabe, donde se aprecia grabado en relieve sobre el plástico sin tinta: 'LOTE 24B01 - CAD 05/2027'. Iluminación rasante que resalta el texto tridimensional.",
         "Enfoca con el móvil y di a Gemini: 'Gemini, no distingo bien los números grabados en este bote de jarabe, ¿me dices qué fecha de caducidad tiene puesta?'."),

        ("Tensiómetro Digital: Código de error 'Err 2' (brazalete flojo)",
         "Saber por qué el aparato de tomar la tensión pita y da error en la pantalla antes de asustarse.",
         "Pantalla LCD grande de un tensiómetro digital de brazo sobre una mesa, mostrando en dígitos grandes 'Err 2' y el icono parpadeante de un brazalete con una flecha. Botón de inicio azul al lado, iluminación limpia.",
         "Apunta con el móvil a la pantalla del tensiómetro y pregunta: 'Gemini, el tensiómetro me pita y me saca este Err 2 en la pantalla, ¿por qué no me mide la tensión y cómo me pongo bien el manguito?'."),

        ("Tira Reactiva de Glucemia o Salud: Escala de colores en el bote",
         "Comparar el color de una tira reactiva contra la tabla de referencia del bote con la cámara del móvil.",
         "Fotografía de un bote cilíndrico de tiras reactivas de orina o glucosa mostrando su cuadrícula de colores graduados (amarillo a morado), sosteniendo junto al bote una tira impregnada con dos almohadillas de color visible. Comparativa visual clara.",
         "Apunta a la tira y al bote con el móvil y dile a Gemini: 'Gemini, mira el color de esta tira reactiva al lado del bote, ¿a qué valor de la escala se parece más el color que ha salido?'."),

        ("Pomada con Cortisona: Advertencia de exposición al sol",
         "Descubrir si una crema para la piel puede producir manchas si nos da el sol en verano.",
         "Tubo de pomada dérmica sobre fondo neutro, mostrando en el reverso el texto de precauciones: 'Contiene hidrocortisona. Evitar la exposición directa a la luz solar o rayos UVA en la zona tratada durante el tratamiento para prevenir reacciones de fotosensibilidad'.",
         "Fotografía el tubo con el móvil y pregunta: 'Gemini, me he puesto esta crema en el brazo, ¿puedo salir a pasear al sol o me van a salir manchas en la piel?'."),

        ("Pastillero Semanal: Identificación de pastillas por forma y color",
         "Confirmar si una pastilla que se ha caído del pastillero es la del colesterol o la de la tensión.",
         "Fotografía en primer plano macro de un pastillero de plástico con casilleros abiertos, y sobre la mesa dos pastillas diferentes: una redonda pequeña blanca con una ranura al medio y otra alargada ovalada azul claro. Nitidez máxima.",
         "Enfoca las pastillas con el móvil y pregúntale: 'Gemini, se me han mezclado estas dos pastillas: una blanca redonda y otra azul ovalada. Tomo Enalapril y Simvastatina, ¿cuál suele ser cuál según su forma habitual?'."),

        ("Receta Electrónica: Fecha límite de dispensación en farmacia",
         "Localizar en la hoja de medicación del centro de salud hasta qué día se puede retirar la caja en la farmacia.",
         "Hoja de tratamiento médico crónico del servicio público de salud en papel, con lista de 3 medicamentos, su posología y en la columna derecha destacada: 'Disponible en farmacia hasta: 24/11/2026' con código de barras y datos del facultativo.",
         "Apunta a la hoja con el móvil y di: 'Gemini, mira esta receta del médico, ¿cuál es el último día que tengo para ir a la farmacia antes de que se me caduque el volante?'."),

        # 4. TRANSPORTE, VIAJES Y COCHE (27-34)
        ("Salpicadero del Coche: Testigo naranja de presión de neumáticos",
         "Reconocer el símbolo de la herradura con signo de exclamación para saber que una rueda está baja de aire.",
         "Fotografía del cuadro de instrumentos encendido de un automóvil tras el volante, mostrando velocímetro y en el centro un testigo luminoso naranja brillante con forma de sección de neumático con una exclamación dentro (!). Vista nítida y realista del tablero.",
         "Hazle una foto al tablero con tu móvil y pregúntale por voz: 'Gemini, se me ha encendido esta luz naranja con forma de herradura y exclamación en el coche, ¿qué significa y puedo seguir conduciendo hasta la gasolinera?'."),

        ("Salpicadero del Coche: Testigo de bombilla fundida o líquido limpiaparabrisas",
         "Identificar averías menores que no impiden la marcha pero que conviene solucionar.",
         "Panel digital del coche mostrando dos iconos iluminados: un surtidor de agua salpicando un parabrisas en color ámbar y un pequeño icono de una bombilla con rayos alrededor. Tacómetro e indicadores secundarios apagados.",
         "Enfoca con el móvil y pregunta: 'Gemini, mira estos dos testigos amarillos en el coche, ¿cuál es el que me avisa de rellenar el agua del limpiaparabrisas?'."),

        ("Billete de Tren de Renfe: Coche, plaza y hora límite de embarque",
         "Encontrar al instante en un billete impreso o en PDF el número de vagón (coche) y asiento para no perderse en el andén.",
         "Billete de tren de alta velocidad en papel o pantalla con diseño clásico: origen Madrid-Puerta de Atocha, destino Sevilla-Santa Justa, código QR grande, 'Coche: 07', 'Plaza: 12B (Ventana)', 'Cierre de acceso al andén: 2 minutos antes de la salida'.",
         "Apunta al billete con el móvil y dile a Gemini: 'Gemini, voy con prisa por la estación: ¿en qué coche y en qué asiento me tengo que sentar según este billete?'."),

        ("Tarjeta de Embarque de Avión: Puerta y grupo de embarque",
         "Localizar la puerta de embarque (Gate), la hora de embarque (Boarding time) y el asiento en un billete de avión.",
         "Primer plano de una tarjeta de embarque aérea con campos destacados: 'Flight: IB3840', 'Gate: B24', 'Boarding: 10:15', 'Seat: 14C (Pasillo)', 'Group: 3'. Tipografía estándar de aerolínea limpia y contrastada.",
         "Enfoca con el móvil y di por voz: 'Gemini, mira mi billete de avión: ¿a qué puerta de embarque tengo que ir y a qué hora abren la puerta para entrar?'."),

        ("Parquímetro de Zona Azul: Horarios de pago y tarifa gratuita",
         "Interpretar la pegatina del parquímetro de la calle para saber si a esa hora es gratis aparcar o hay que poner ticket.",
         "Fotografía frontal de la placa informativa de metal de un parquímetro callejero, indicando: 'Horario regulado: Lunes a Viernes de 9:00 a 14:00 y de 16:00 a 20:00. Sábados de 9:00 a 14:00. Domingos y festivos: Gratuito'.",
         "Apunta a la placa con el móvil y pregunta: 'Gemini, son las cinco de la tarde de un sábado, según este cartel del parquímetro ¿tengo que pagar ticket o es gratis aparcar a esta hora?'."),

        ("Máquina de Billetes de Metro: Elegir bono de 10 viajes",
         "Saber qué opción tocar en la pantalla táctil de la estación de metro para comprar billetes económicos.",
         "Pantalla táctil de máquina expendedora de billetes de transporte público urbano, mostrando 4 casillas grandes en español: 'Billete Sencillo 1 Viaje', 'Metrobús 10 Viajes', 'Abono Turístico' y 'Recargar Tarjeta Multi'. Botones grandes con diseño gráfico oficial.",
         "Enfoca la pantalla con el móvil y di: 'Gemini, voy a estar 4 días en la ciudad y me voy a mover en metro, ¿cuál de estos cuatro botones de la pantalla me conviene pulsar para no gastar de más?'."),

        ("Señal de Tráfico de Estacionamiento: Excepción por carga y descarga",
         "Descifrar placas complementarias debajo de la señal de prohibido aparcar para no llevarse una multa.",
         "Fotografía de una señal redonda de prohibido estacionar (borde rojo y fondo azul con franja diagonal roja), y debajo una placa rectangular blanca que dice: 'Excepto carga y descarga laborables de 8:00 a 14:00 h. Máximo 30 minutos'. Fondo urbano de calle.",
         "Apunta a la señal con el móvil y pregunta: 'Gemini, es martes a las tres de la tarde, ¿puedo aparcar aquí el coche para ir a comer o me lo va a retirar la grúa?'."),

        ("Panel de Salidas de Estación: Localizar andén o vía",
         "Leer rápidamente la pantalla gigante de salidas de trenes o autobuses para encontrar el andén.",
         "Pantalla electrónica de estación de trenes tipo LED con fondo negro y letras amarillas/naranjas, mostrando lista de salidas con columnas: 'Hora', 'Tren', 'Destino', 'Vía/Andén' y 'Estado: Embarque'. Fila de Valencia Joaquín Sorolla con vía 4 parpadeando.",
         "Apunta al panel con el móvil y pregúntale: 'Gemini, voy en el tren hacia Valencia de las 18:30, ¿en qué vía o andén tengo que esperar según esta pantalla?'."),

        # 5. DISPOSITIVOS DIGITALES Y CABLES (35-42)
        ("Router Wifi: Nombre de red (SSID) y contraseña de fábrica",
         "Localizar en la pegatina trasera del router cuál es la contraseña larga que hay que dictarle a los invitados.",
         "Fotografía en plano detalle de la etiqueta blanca pegada detrás de un router de fibra negro, con varios campos rotulados: 'Modelo', 'MAC', 'Nombre de red (SSID): MiFibra_4G_8A', 'Clave Wifi / Password: K9m2X7pL4wQ1' con código QR al lado. Letras y números nítidos.",
         "Enfoca la pegatina del router con el móvil y di: 'Gemini, han venido mis nietos a casa y quieren conectarse al wifi, ¿cuál de todas estas líneas es la contraseña que tienen que poner en sus móviles?'."),

        ("Mando de Televisión Inteligente: Botón 'Source / Input' para ver la tele",
         "Solucionar la típica pantalla negra de 'Sin señal' encontrando el botón correcto del mando a distancia.",
         "Fotografía en primer plano de un mando a distancia de televisión moderna negro con botones de goma, destacando en la parte superior el botón de encendido rojo, y justo al lado un botón con un icono de un rectángulo con una flecha entrando (Source / Entrada HDMI).",
         "Apunta con el móvil al mando y pregunta: 'Gemini, en la tele se me ha puesto la pantalla en azul diciendo sin señal de entrada, ¿qué botón de este mando tengo que apretar para volver a ver los canales normales?'."),

        ("Regleta con Protector: Botón Reset saltado",
         "Descubrir por qué no funciona ningún aparato enchufado a una regleta múltiple.",
         "Fotografía de una regleta blanca de enchufes sobre el suelo, con 5 tomas de corriente y en el extremo un botón basculante rojo con luz apagada y un pequeño pulsador negro cilíndrico salido rotulado con la palabra 'RESET 10A'.",
         "Enfoca la regleta con el móvil y di por voz: 'Gemini, se me han apagado de golpe la lámpara y la radio que tengo en esta regleta, ¿qué le pasa a este botón negro que pone Reset?'."),

        ("Identificación de Cables: USB-C vs USB clásico vs HDMI",
         "Aprender a diferenciar los cables del móvil y de la tele por la forma de su clavija.",
         "Fotografía sobre una mesa blanca con 3 cables desenrollados mostrando sus conectores metálicos de frente: uno rectangular clásico USB-A, uno ovalado reversible USB-C pequeño y uno plano biselado ancho HDMI para televisor. Formas perfectamente diferenciadas.",
         "Apunta con el móvil a los cables y pregunta: 'Gemini, tengo aquí estos tres cables sueltos, ¿cuál de ellos es el que sirve para cargar mi móvil moderno que se conecta por los dos lados?'."),

        ("Pantalla del PC: Mensaje de 'No hay conexión a internet'",
         "Saber si el problema de internet es del ordenador o si se ha desenchufado el cable de red.",
         "Captura de pantalla realista de navegador web mostrando la ilustración de un dinosaurio pixelado o un cable desconectado con el mensaje: 'No hay conexión a Internet. Comprueba los cables de red, el módem y el router. ERR_INTERNET_DISCONNECTED'.",
         "Hazle una foto a la pantalla del PC con tu móvil y pregúntale: 'Gemini, me sale este mensaje en el ordenador y no me abre el correo, ¿qué tres cosas sencillas tengo que mirar en el router antes de llamar al técnico?'."),

        ("Cajero Automático: Mensaje sobre comisión por retirada",
         "Comprender la pantalla del cajero antes de aceptar sacar dinero para saber cuánto nos van a cobrar de comisión.",
         "Pantalla de cajero bancario exterior con texto en español: 'Su entidad bancaria no pertenece a esta red. La entidad propietaria del cajero le cobrará una comisión de 2,90 € por esta operación. ¿Desea continuar? Botones táctiles: [Continuar] [Cancelar]'.",
         "Enfoca la pantalla del cajero con el móvil y di: 'Gemini, mira lo que me dice el cajero: ¿me van a cobrar comisión si saco dinero aquí y cuánto me van a cobrar?'."),

        ("Dispositivo de Teleasistencia: Luces verde y roja del medallón",
         "Verificar si el colgante o pulsera de ayuda a domicilio tiene batería y cobertura con la central.",
         "Fotografía en primer plano de un colgante de botón de teleasistencia blanco con cordón rojo, mostrando un botón central con cruz roja y un pequeño piloto led verde encendido fijo y otro piloto de batería apagado sobre la base cargadora.",
         "Apunta al botón con el móvil y pregunta: 'Gemini, mira el medallón de teleasistencia, tiene esta lucecita verde fija, ¿eso significa que está funcionando bien y que tiene batería?'."),

        ("Auriculares Inalámbricos: Luz parpadeante de emparejamiento Bluetooth",
         "Saber cuándo los auriculares están listos para conectarse al móvil.",
         "Estuche blanco abierto de auriculares inalámbricos tipo botón, con uno de los auriculares dentro mostrando un diminuto led azul parpadeando rápidamente de forma rítmica. Acabado brillante limpio.",
         "Enfoca con el móvil y pregunta: 'Gemini, el auricular tiene esta luz azul que parpadea muy rápido, ¿eso quiere decir que está buscando mi móvil o que se ha quedado sin batería?'."),

        # 6. HOGAR, PLANTAS Y BRICOLAJE (43-50)
        ("Planta de Interior: Hojas amarillentas con puntas secas",
         "Usar la cámara del móvil como botánico personal para saber si a una maceta le sobra o le falta agua.",
         "Fotografía en primer plano de las hojas de una planta de interior (poto o espatifilo) en maceta, mostrando dos hojas inferiores que se han vuelto completamente amarillas y las puntas marrones y quebradizas. Tierra en maceta visible.",
         "Saca el móvil, enfoca la planta y di: 'Gemini, mira cómo se me están poniendo las hojas de esta maceta, ¿por qué se ponen amarillas y qué tengo que hacer con el riego para salvarla?'."),

        ("Radiador de Calefacción: Válvula termostática del 1 al 5",
         "Saber qué número poner en la rueda del radiador de cada habitación para no gastar calefacción de más.",
         "Primer plano de la llave de paso termostática metálica blanca de un radiador de agua de pared, con números grabados del * (antihielo) al 5, con la muesca de referencia colocada en el número 3. Acabado nítido.",
         "Enfoca con el móvil y pregunta: 'Gemini, tengo esta rueda con números del 1 al 5 en el radiador del dormitorio, ¿en qué número lo pongo para dormir a gusto sin que suba la factura del gas?'."),

        ("Contador de Agua: Números negros vs números rojos",
         "Distinguir los metros cúbicos que factura el ayuntamiento de los litros de consumo para comprobar fugas.",
         "Fotografía cenital de la esfera de cristal de un contador de agua doméstico, mostrando cuatro rodillos numéricos negros que marcan '0342' (metros cúbicos) y dos rodillos rojos que marcan '85' (decilitros), con una rueda dentada diminuta en movimiento.",
         "Apunta al contador con el móvil y pregúntale: 'Gemini, tengo que dar la lectura del agua al ayuntamiento, ¿qué números tengo que apuntar: los negros, los rojos o todos?'."),

        ("Llave de Paso General del Agua: Abierta vs cerrada",
         "Saber en un segundo si una llave de corte está cortando el agua o dejándola pasar antes de una reparación.",
         "Fotografía de una tubería de cobre vista con una llave de paso de palanca roja, orientada de forma totalmente perpendicular (en ángulo de 90 grados respecto al sentido del tubo). Tubería y accesorios limpios.",
         "Enfoca con el móvil y pregunta por voz: 'Gemini, mira esta palanca roja de la tubería, ¿así atravesada el agua está cortada o está abierta?'."),

        ("Grifo con Manchas de Cal: Grifería cromada opaca",
         "Identificar acumulación de cal en el aireador o grifo para limpiarlo con productos ecológicos caseros.",
         "Primer plano macro del caño y aireador de un grifo de lavabo cromado, mostrando costras blancas y rugosas de cal incrustada en la rejilla de salida del agua que desvían los chorros. Iluminación lateral que resalta la cal.",
         "Hazle una foto con el móvil y dile a Gemini: 'Gemini, mira cómo tengo la boca de este grifo llena de cal blanca que no sale el agua recta, ¿cómo lo limpio en 10 minutos con vinagre sin rayar el metal?'."),

        ("Sustrato de Jardinería: Proporción N-P-K en abono",
         "Entender para qué sirve cada tipo de abono según las tres letras mágicas de los fertilizantes.",
         "Detalle de la parte trasera de un saco de fertilizante orgánico para plantas, mostrando en un recuadro destacado: 'Composición NPK 7-3-5: Nitrógeno total (N) 7%, Fósforo (P₂O₅) 3%, Potasio (K₂O) 5% enriquecido con magnesio'.",
         "Enfoca el saco con el móvil y pregunta: 'Gemini, mira estos tres números NPK 7-3-5 de este abono, ¿esto le viene bien a mis geranios con flor o es para dar hojas verdes?'."),

        ("Filtro de Campana Extractora: Malla metálica saturada",
         "Reconocer cuándo el filtro de la cocina necesita limpieza urgente en el lavavajillas.",
         "Fotografía en plano detalle de la rejilla metálica de aluminio perforado de una campana extractora de cocina, con los poros de la malla amarillentos y cubiertos de película de grasa brillante pegajosa. Textura metálica muy nítida.",
         "Apunta al filtro con el móvil y pregúntale: 'Gemini, mira cómo está el filtro de mi campana de la cocina, ¿lo puedo meter al lavavajillas o con qué producto casero se le va esta grasa pegajosa?'."),

        ("Termostato Inalámbrico: Modo automático vs manual de confort",
         "Aprender a manejar la rueda del termostato del salón para mantener la casa a 21 grados estables.",
         "Fotografía frontal de un termostato digital de pared blanco circular, mostrando en su pantalla dígitos grandes de temperatura actual: '19.5 °C', temperatura deseada en pequeño '21.0 °C' y el icono de una llama de fuego encendida en la esquina.",
         "Enfoca con el móvil y pregunta por voz: 'Gemini, mira la pantalla del termostato: ¿está la caldera encendida ahora mismo y a cuántos grados se va a apagar?'."),

        # 7. ALIMENTACIÓN, COMPRAS Y NUTRICIÓN (51-56)
        ("Etiqueta Nutricional: Azúcares añadidos en alimentos procesados",
         "Aprender a buscar la línea de 'de los cuales azúcares' para no comprar productos con azúcar oculto.",
         "Fotografía macro nítida de la tabla de información nutricional impresa en una caja de cereales o galletas, mostrando: 'Hidratos de carbono: 68 g', y justo debajo con sangría: 'de los cuales azúcares: 28 g'. Valores resaltados con tipografía clara.",
         "Apunta a la tabla con tu móvil y pregúntale a Gemini: 'Gemini, soy mayor y tengo que cuidar el azúcar: mira esta tabla nutricional, ¿cuántas cucharadas de azúcar tiene este paquete por cada 100 gramos?'."),

        ("Fecha de Caducidad vs Consumo Preferente: Paquete de legumbres o yogur",
         "Saber si un alimento se puede comer con total seguridad aunque hayan pasado unos días de la fecha.",
         "Fotografía de la tapa de un alimento envasado donde se lee claramente impreso en tinta negra: 'Consumir preferentemente antes del: 15/09/2026' junto al lote de fabricación. Fondo limpio sobre mesa de cocina.",
         "Enfoca con el móvil y pregunta: 'Gemini, este paquete dice consumir preferentemente antes de la fecha que se ve, ¿si se me pasa unos días me lo puedo comer o es peligroso para la salud?'."),

        ("Lista de Ingredientes: Detección de alérgenos y aditivos E-xxx",
         "Descubrir si un producto que parece inocuo lleva gluten, lactosa o potenciadores de sabor como glutamato.",
         "Detalle en macro de la lista de ingredientes de una salsa envasada, mostrando texto en negrita: 'Ingredientes: Agua, tomate, almidón modificado de maíz, gluten de trigo, potenciador del sabor (E-621) y conservante (E-202)'.",
         "Apunta con el móvil y dile a Gemini: 'Gemini, mi nieto es celíaco y no puede tomar nada con gluten: mira esta lista de ingredientes, ¿hay algo aquí que le pueda sentar mal?'."),

        ("Etiquetas de Jamón Ibérico: Precinto de color (Negro, Rojo, Verde, Blanco)",
         "Saber qué calidad de jamón nos están vendiendo según el color de la brida de plástico de la pata.",
         "Fotografía en primer plano de la caña de una pata de jamón curado, con una brida o precinto de plástico de color verde precintada alrededor del hueso con el logotipo oficial de norma de calidad del ibérico.",
         "Enfoca el precinto con tu móvil y pregunta: 'Gemini, mira esta etiqueta verde que lleva el jamón en la pata, ¿qué pureza de raza ibérica y qué tipo de alimentación tiene este animal según la ley?'."),

        ("Etiqueta Adhesiva de Fruta: Código PLU de 4 o 5 dígitos",
         "Descubrir qué significa el numerito pegado a las manzanas o plátanos sobre si son ecológicos o convencionales.",
         "Primer plano macro de una manzana roja brillante sobre la que hay pegada una pequeña etiqueta ovalada que muestra el código numérico '94011' con el nombre de la variedad y origen. Iluminación limpia.",
         "Apunta a la manzana con el móvil y pregúntale: 'Gemini, mira esta pegatina con el número 94011 en la manzana: ¿qué significa que empiece por el número 9, es fruta ecológica cultivada sin pesticidas?'."),

        ("Pescado Fresco de Pescadería: Ojo brillante y agallas rojas",
         "Aprender a comprobar la frescura de una pieza de pescado en la pescadería o en la cocina.",
         "Fotografía en plano detalle de la cabeza de una lubina o dorada fresca sobre hielo picado, mostrando su ojo transparente y abombado con pupila negra brillante, y el opérculo ligeramente levantado mostrando agallas de color rojo sangre vivo.",
         "Hazle una foto al pescado con el móvil y di por voz: 'Gemini, mira el ojo y las agallas de este pescado que acabo de comprar, ¿tiene aspecto de estar muy fresco o lleva ya varios días en la tienda?'."),

        # 8. BRICOLAJE Y HERRAMIENTAS (57-60)
        ("Brocas de Taladro: Madera vs Pared vs Metal",
         "Elegir la broca correcta en la caja de herramientas para no romperla al hacer un agujero en la pared.",
         "Fotografía sobre mesa de trabajo de 3 brocas de taladro colocadas en paralelo: una con punta de centrado afilada (madera), una con pastilla ancha de carburo en la punta (pared/hormigón) y una con punta helicoidal cónica (metal).",
         "Apunta con el móvil a las tres brocas y pregunta a Gemini: 'Gemini, quiero colgar un cuadro en una pared de ladrillo con el taladro: ¿cuál de estas tres brocas es la de pared que tengo que poner?'."),

        ("Tacos y Tornillos: Emparejar el grosor adecuado",
         "Asegurarse de que el tornillo no quede flojo dentro del taco de plástico antes de taladrar.",
         "Primer plano de un taco de plástico gris de 6 mm de diámetro colocado junto a dos tornillos: uno demasiado fino que baila dentro y otro de rosca adecuada de 4.5 mm de grosor con cabeza avellanada de estrella.",
         "Enfoca con el móvil y di por voz: 'Gemini, mira este taco gris y estos tornillos: ¿cuál de los dos tornillos es del tamaño exacto para que quede bien firme en este taco?'."),

        ("Cinta de Teflón en Fontanería: Sentido de giro del hilo",
         "Aprender a poner la cinta blanca de teflón en un grifo para que no gotee ni se desenrolle al apretar.",
         "Fotografía en detalle de las roscas macho de latón de un grifo de jardín, con varias vueltas de cinta de teflón blanco fino envueltas en el sentido de las agujas del reloj alrededor de la rosca metálica.",
         "Apunta con el móvil y pregunta: 'Gemini, voy a cambiar el grifo del patio: mira cómo he puesto el teflón blanco en la rosca, ¿está enrollado en el sentido correcto para que no se arrugue al enroscar?'."),

        ("Maletín de Herramientas Básico: Llave inglesa vs llave fija",
         "Reconocer las herramientas imprescindibles del hogar para apretar una tuerca que se mueve.",
         "Fotografía cenital ordenada de un maletín abierto con herramientas de mano básicas: una llave inglesa ajustable con rueda de ajuste, un juego de llaves fijas cromadas, un alicate universal con mango de goma y dos destornilladores.",
         "Enfoca el maletín con tu móvil y pregúntale a Gemini: 'Gemini, se me mueve la tuerca del asiento del inodoro, ¿cuál de las herramientas de esta caja es la que puedo ajustar a cualquier medida de tuerca para apretarla?'."),
    ]

    for idx, (title, concept, prompt_pc, prompt_movil) in enumerate(retos, 1):
        movil_list.append({
            "block_dir": "12. [MOVIL] BLOQUE_12_EL_SALVAVIDAS_DEL_MOVIL",
            "block_name": "BLOQUE 12: EL SALVAVIDAS DEL MÓVIL [MOVIL]",
            "id_code": f"[MOVIL-{idx:03d}]",
            "title": title,
            "concept": concept,
            "prompt": prompt_pc,
            "tips": prompt_movil
        })

    return movil_list

if __name__ == "__main__":
    items = get_movil_items()
    print(f"Total ítems MOVIL generados: {len(items)}")
    print(f"Muestra ítem 1: {items[0]['title']}")
    print(f"Tips ítem 1: {items[0]['tips']}")
