/**
 * LÓGICA DE LA APLICACIÓN "EL ABUELO TUTOR"
 * Módulo 1: Tutor Socrático de Matemáticas en 4 niveles
 * Módulo 2: Transformador de NotebookLM a Fichas Escolares y Tarjetas Imprimibles
 */

// ==========================================================================
// 1. GESTIÓN DE PESTAÑAS
// ==========================================================================
function switchTab(tabId) {
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));

  const activeContent = document.getElementById(tabId);
  if (activeContent) {
    activeContent.classList.add('active');
  }

  // Marcar botón activo
  const buttons = document.querySelectorAll('.tab-btn');
  if (tabId === 'tab-mates') buttons[0].classList.add('active');
  else if (tabId === 'tab-historia') buttons[1].classList.add('active');
  else if (tabId === 'tab-guia') buttons[2].classList.add('active');
}

// ==========================================================================
// 2. BASE DE CONOCIMIENTO DE MATEMÁTICAS (EJEMPLOS Y RESOLUTOR)
// ==========================================================================
const MATH_EXAMPLES = {
  ecuacion2: {
    question: "¿Cómo se resuelve una ecuación de segundo grado como x² - 5x + 6 = 0 y qué significa?",
    intuition: `Imagínate que vas a una fiesta y hay personas dándose la mano. En una ecuación normal buscamos un número escondido, pero en una de segundo grado (con una 'x' elevada al cuadrado), la incógnita se multiplica por sí misma formando un área (como las baldosas cuadradas de una habitación). Por eso, casi siempre hay DOS números mágicos diferentes que hacen que la balanza dé cero. ¡Es como una cerradura que tiene dos llaves distintas que abren la misma puerta!`,
    stepbystep: `1º Identificamos los tres números clave que acompañan a las letras:
• La 'a' es el número que acompaña a x²: aquí vale 1.
• La 'b' es el número que acompaña a x: aquí vale -5.
• La 'c' es el número suelto sin letra: aquí vale +6.

2º Aplicamos la famosa fórmula cuadrática universal:
x = [-b ± √(b² - 4ac)] / (2a)

3º Hacemos las operaciones dentro de la raíz:
• b² = (-5)² = 25.
• 4 · a · c = 4 · 1 · 6 = 24.
• Restamos: 25 - 24 = 1.
• La raíz cuadrada de 1 es 1 (porque 1 · 1 = 1).

4º Sacamos los dos caminos (el del signo más y el del signo menos):
• Camino con +: x₁ = [5 + 1] / 2 = 6 / 2 = 3.
• Camino con -: x₂ = [5 - 1] / 2 = 4 / 2 = 2.`,
    formal: `<div class="math-formula">Ecuación: x² - 5x + 6 = 0</div>
Fórmula general: x = [-b ± √(b² - 4ac)] / (2a)
Sustitución con a=1, b=-5, c=6:
x = [-(-5) ± √((-5)² - 4·1·6)] / (2·1)
x = [5 ± √(25 - 24)] / 2
x = [5 ± √1] / 2 = [5 ± 1] / 2
<b>Solución 1: x₁ = 3</b>
<b>Solución 2: x₂ = 2</b>
<i>Comprobación: 3² - 5(3) + 6 = 9 - 15 + 6 = 0 (Correcto) | 2² - 5(2) + 6 = 4 - 10 + 6 = 0 (Correcto)</i>`,
    twin: `<b>Reto Gemelo para Lucas:</b> Resuelve en tu cuaderno la siguiente ecuación usando exactamente la misma fórmula que acabas de ver:<br/>
<div class="math-formula">x² - 7x + 12 = 0</div>
<i>Pista del abuelo: La 'a' vale 1, la 'b' vale -7 y la 'c' vale 12. Las dos llaves de la cerradura son dos números enteros positivos que suman 7 y multiplicados dan 12. ¡Tú puedes!</i>`
  },

  coches: {
    question: "Un coche sale de Madrid hacia Barcelona a 100 km/h a las 10:00. Otro sale de Barcelona hacia Madrid a 90 km/h a las 11:00. Si la distancia entre Madrid y Barcelona es de 670 km, ¿a qué hora y a qué distancia se encontrarán?",
    intuition: `Imagínate que Madrid y Barcelona están unidas por una cuerda tirante de 670 km.
Durante la primera hora (de 10:00 a 11:00) el coche de Barcelona está quieto en el garaje. Solo viaja el de Madrid, que a 100 km/h recorta 100 km de cuerda.
A las 11:00 de la mañana, la cuerda que los separa mide solo 570 km. En ese momento arrancan los dos a la vez y se acercan el uno hacia el otro. Como viajan en direcciones contrarias, sus velocidades se sumarán: 100 + 90 = 190 km que devoran entre los dos cada hora que pasa. ¡Solo tenemos que ver cuántas veces cabe 190 dentro de 570!`,
    stepbystep: `1º Calculamos qué pasa durante la primera hora de ventaja (de 10:00 a 11:00):
• El coche A recorre en 1 hora: 100 km/h · 1 h = 100 km.
• Distancia restante que los separa a las 11:00: 670 - 100 = 570 km.

2º Calculamos la velocidad a la que se reduce la distancia entre ambos:
• Velocidad relativa de encuentro: 100 km/h + 90 km/h = 190 km/h.

3º Calculamos el tiempo que tardan en encontrarse a partir de las 11:00:
• Tiempo = Distancia restante / Velocidad combinada
• Tiempo = 570 km / 190 km/h = exactamente 3 horas.

4º Hora de encuentro:
• Si empezaron a viajar juntos a las 11:00 y tardan 3 horas: 11:00 + 3 horas = <b>14:00 horas (las 2 de la tarde)</b>.

5º ¿A qué distancia de Madrid se cruzan?
• El coche de Madrid ha viajado 4 horas en total (de 10:00 a 14:00): 4 h · 100 km/h = <b>400 km de Madrid</b>.`,
    formal: `<div class="math-formula">Ecuación de movimiento rectilíneo uniforme: Espacio = Velocidad · Tiempo (e = v · t)</div>
Distancia total: D = 670 km
Posición coche 1 (sale a las 10:00): x₁(t) = 100 · t
Posición coche 2 (sale a las 11:00): x₂(t) = 670 - 90 · (t - 1)
Igualamos posiciones en el punto de encuentro:
100t = 670 - 90t + 90
100t + 90t = 760
190t = 760  -->  t = 760 / 190 = <b>4 horas</b> (desde las 10:00)
<b>Hora de encuentro: 10:00 + 4h = 14:00 horas.</b>
<b>Punto de encuentro: x = 100 · 4 = 400 km desde Madrid (y a 270 km de Barcelona).</b>`,
    twin: `<b>Reto Gemelo para Lucas:</b> Dos ciclistas salen a encontrarse entre dos pueblos separados por 90 km.<br/>
El ciclista A sale a las 09:00 a 20 km/h. El ciclista B sale a las 10:00 hacia él a 15 km/h.<br/>
¿A qué hora se cruzarán en la carretera?<br/>
<i>Pista del abuelo: Mira cuántos kilómetros hace el ciclista A durante su primera hora a solas. Luego suma las velocidades de los dos para devorar los kilómetros que falten.</i>`
  },

  fracciones: {
    question: "¿Cómo se suman dos fracciones con distinto denominador, como 2/3 + 3/5?",
    intuition: `Imagínate que 2/3 son porciones de una tarta cortada en 3 pedazos grandes, y 3/5 son porciones de una tarta cortada en 5 pedazos medianos. No puedes sumarlas directamente diciendo "tengo 5 trozos", porque los trozos son de tamaños completamente distintos: ¡sería como sumar manzanas con melones!
Para poder sumarlas, tenemos que cortar las dos tartas en trozos exactamente iguales. Buscamos un número de trozos que sirva para las dos: 3 · 5 = 15 trozos. Ahora que las dos tartas tienen rebanadas de 15, ya podemos contarlas juntas.`,
    stepbystep: `1º Buscamos el Mínimo Común Múltiplo (m.c.m.) entre 3 y 5:
Como son números primos, multiplicamos: 3 · 5 = 15. Ese será el nuevo denominador común.

2º Transformamos la primera fracción (2/3):
• Dividimos 15 entre el denominador viejo: 15 / 3 = 5.
• Multiplicamos el numerador por 5: 2 · 5 = 10.
• La fracción 2/3 se convierte en 10/15.

3º Transformamos la segunda fracción (3/5):
• Dividimos 15 entre el denominador viejo: 15 / 5 = 3.
• Multiplicamos el numerador por 3: 3 · 3 = 9.
• La fracción 3/5 se convierte en 9/15.

4º Ahora que los denominadores son iguales, sumamos los numeradores:
10/15 + 9/15 = (10 + 9) / 15 = 19/15.`,
    formal: `<div class="math-formula">Operación: 2/3 + 3/5</div>
m.c.m.(3, 5) = 15
2/3 = (2 · 5) / (3 · 5) = 10/15
3/5 = (3 · 3) / (5 · 3) = 9/15
10/15 + 9/15 = (10 + 9) / 15 = <b>19/15</b> (Fracción irreducible = 1 entero y 4/15).`,
    twin: `<b>Reto Gemelo para Lucas:</b> Calcula en tu cuaderno la siguiente suma de fracciones:<br/>
<div class="math-formula">3/4 + 2/5 = ?</div>
<i>Pista del abuelo: Busca en qué número coinciden el 4 y el 5 en la tabla de multiplicar. ¡Es el 20!</i>`
  },

  porcentajes: {
    question: "Unas zapatillas de deporte valen 80 euros y tienen un descuento del 30%. ¿Cuánto dinero me descuentan y cuánto pagaré al final?",
    intuition: `La palabra 'por ciento' significa literalmente 'por cada cien'.
Si algo tiene un 30% de rebaja, significa que por cada billete de 100 euros que costara, la tienda te regala 30 euros y tú pagas 70.
Como las zapatillas no valen 100 sino 80, hay un truco mental infalible: calcula primero cuánto es el 10% (que es simplemente quitar un cero o mover la coma: el 10% de 80 son 8 euros). Si el 10% son 8 euros, ¡el 30% es simplemente el triple: 8 · 3 = 24 euros de descuento!`,
    stepbystep: `1º Calculamos la cantidad de dinero que nos rebajan (el descuento):
• Multiplicamos el precio por el porcentaje: 80 · 30 = 2400.
• Dividimos entre 100: 2400 / 100 = 24 euros de descuento.

2º Calculamos el precio final restándole ese ahorro al precio original:
• Precio final = Precio original - Descuento
• Precio final = 80 - 24 = 56 euros.

3º Método rápido alternativo (para cuando vas de compras):
Si te rebajan el 30%, significa que vas a pagar el 70% del valor:
80 · 0,70 = 56 euros directamente.`,
    formal: `<div class="math-formula">Precio original: P = 80 € | Descuento: D = 30%</div>
Descuento en euros = (80 · 30) / 100 = 2400 / 100 = <b>24 €</b>
Precio final a pagar = 80 € - 24 € = <b>56 €</b>
<i>Cálculo en factor multiplicativo: 80 · (1 - 0,30) = 80 · 0,70 = 56 €</i>`,
    twin: `<b>Reto Gemelo para Lucas:</b> Una chaqueta de montaña cuesta 60 euros y tiene una rebaja del 20%.<br/>
¿Cuánto te ahorras y cuánto dinero tienes que pagar en caja?<br/>
<i>Pista del abuelo: El 10% de 60 son 6 euros... así que el 20% será el doble.</i>`
  },

  pitagoras: {
    question: "Tenemos una pared vertical de 4 metros de altura y apoyamos una escalera de 5 metros en lo alto. ¿A qué distancia de la pared debe quedar apoyada la base de la escalera en el suelo?",
    intuition: `Imagínate una escuadra de carpintero. Los dos lados rectos que forman la esquina se llaman 'catetos' (la pared vertical y el suelo horizontal). La escalera inclinada que une los dos extremos es la 'hipotenusa'.
Pitágoras descubrió una regla mágica: si dibujas un cuadrado sobre la escalera, su superficie es exactamente igual a la suma de los cuadrados dibujados en la pared y en el suelo. Como la escalera es el lado más largo (5 metros), el suelo tiene que ser más corto que 5.`,
    stepbystep: `1º Identificamos los datos:
• La hipotenusa (escalera inclinada): a = 5 metros.
• Un cateto (altura de la pared): b = 4 metros.
• El otro cateto (distancia en el suelo): c = ?

2º Escribimos el Teorema de Pitágoras:
Hipotenusa² = Cateto₁² + Cateto₂²
5² = 4² + c²

3º Elevamos al cuadrado:
25 = 16 + c²

4º Despejamos el cateto desconocido restando:
c² = 25 - 16 = 9
c = √9 = 3 metros.`,
    formal: `<div class="math-formula">Teorema de Pitágoras: a² + b² = h²</div>
Datos: h = 5 m, b = 4 m, c = ?
c² = h² - b²
c² = 5² - 4² = 25 - 16 = 9
c = √9 = <b>3 metros</b>
<b>Respuesta: La base de la escalera debe colocarse exactamente a 3 metros de la pared.</b>`,
    twin: `<b>Reto Gemelo para Lucas:</b> En un campo de fútbol rectangular, quieres cruzar en diagonal.<br/>
Un lado mide 6 metros y el otro mide 8 metros.<br/>
¿Cuántos metros mide la diagonal recta?<br/>
<i>Pista del abuelo: 6² es 36 y 8² es 64. Súmalos y busca la raíz cuadrada de 100.</i>`
  }
};

function loadMathExample(key) {
  const ex = MATH_EXAMPLES[key];
  if (!ex) return;
  document.getElementById('math-question').value = ex.question;
  solveMathProblem(ex);
}

function solveMathProblem(preloadData = null) {
  const qText = document.getElementById('math-question').value.trim();
  const nietoName = document.getElementById('nieto-name').value.trim() || "mi nieto";
  if (!qText) {
    alert("Por favor, escribe primero una duda o problema de matemáticas.");
    return;
  }

  let data = preloadData;

  // Si no es un ejemplo precargado exacto, analizamos el texto libre
  if (!data) {
    const qLower = qText.toLowerCase();
    if (qLower.includes("segundo grado") || qLower.includes("x²") || qLower.includes("x^2") || qLower.includes("cuadrática")) {
      data = MATH_EXAMPLES.ecuacion2;
    } else if (qLower.includes("coche") || qLower.includes("tren") || qLower.includes("velocidad") || qLower.includes("encuentr")) {
      data = MATH_EXAMPLES.coches;
    } else if (qLower.includes("fraccion") || qLower.includes("denominador")) {
      data = MATH_EXAMPLES.fracciones;
    } else if (qLower.includes("porcentaj") || qLower.includes("rebaja") || qLower.includes("descuento") || qLower.includes("%")) {
      data = MATH_EXAMPLES.porcentajes;
    } else if (qLower.includes("pitagoras") || qLower.includes("escalera") || qLower.includes("triangul")) {
      data = MATH_EXAMPLES.pitagoras;
    } else {
      // Explicador genérico estructurado en 4 capas para cualquier entrada libre
      data = {
        question: qText,
        intuition: `Para entender bien este concepto («${qText}»), lo primero que debemos decirle a ${nietoName} es que no tenga miedo a los signos ni a los enunciados largos. En la vida diaria, las matemáticas no son números fríos sino una forma de contar historias ordenadas: repartir caramelos con amigos, medir el tiempo de una película o calcular si nos llega la paga semanal.`,
        stepbystep: `1º Leemos el enunciado despacio subrayando los datos que conocemos con lápiz azul, y lo que nos preguntan con lápiz rojo.<br/>
2º Planteamos la relación lógica: ¿aumenta o disminuye? ¿estamos sumando partes o repartiendo un total?<br/>
3º Realizamos las operaciones aritméticas de una en una, comprobando en cada línea que el resultado tiene sentido físico (por ejemplo: si calculamos la edad de un niño, no puede darnos 250 años ni un número negativo).`,
        formal: `<div class="math-formula">Planteamiento formal para entregar al profesor de ${nietoName}:</div>
• Datos identificados en el enunciado.<br/>
• Fórmula o ecuación correspondiente al tema curricular.<br/>
• Despeje ordenado paso por paso sin saltarse términos.<br/>
• <b>Resultado final recuadrado y con sus unidades correspondientes (metros, euros, horas, etc.).</b>`,
        twin: `<b>Reto Gemelo para ${nietoName}:</b><br/>
Prueba a resolver este mismo ejercicio pero cambiando las cantidades por el doble para asegurarte de que has dominado el método y no solo de memoria los números.`
      };
    }
  }

  // Pintar en pantalla
  document.getElementById('math-result-title').textContent = `📖 Ficha Pedagógica: ${qText.substring(0, 65)}...`;
  document.getElementById('res-math-intuition').innerHTML = data.intuition.replace(/Lucas/g, nietoName);
  document.getElementById('res-math-stepbystep').innerHTML = data.stepbystep.replace(/Lucas/g, nietoName).replace(/\n/g, '<br/>');
  document.getElementById('res-math-formal').innerHTML = data.formal;
  document.getElementById('res-math-twin').innerHTML = data.twin.replace(/Lucas/g, nietoName);

  document.getElementById('math-result').classList.add('visible');
  document.getElementById('btn-print-math').style.display = 'inline-flex';

  // Scroll suave al resultado
  document.getElementById('math-result').scrollIntoView({ behavior: 'smooth' });
}

// ==========================================================================
// 3. BASE DE CONOCIMIENTO DE HISTORIA Y CIENCIAS (PUENTE NOTEBOOKLM)
// ==========================================================================
const HISTORY_EXAMPLES = {
  reyes: {
    tema: "Unidad 4: Los Reyes Católicos y la Unión Dinástica de Castilla y Aragón",
    resumen: "El reinado de los Reyes Católicos (Isabel I de Castilla y Fernando II de Aragón) sentó las bases de la monarquía hispánica moderna. Su matrimonio en 1469 unió dinásticamente los dos reinos más importantes de la península, aunque cada territorio mantuvo sus propias leyes, fueros y monedas. Durante su reinado se completó la Reconquista con la toma de Granada en 1492, se financió la expedición de Cristóbal Colón que culminó con el Descubrimiento de América y se impulsó la uniformidad religiosa a través del Tribunal de la Santa Inquisición y la expulsión de los judíos.",
    preguntas: `¿En qué año contrajeron matrimonio Isabel de Castilla y Fernando de Aragón?
Respuesta: En el año 1469, uniendo dinásticamente a las coronas de Castilla y Aragón.

¿Significó la unión de los Reyes Católicos que Castilla y Aragón se convirtieran en un solo país con las mismas leyes?
Respuesta: No, se trató de una unión dinástica. Cada reino conservó sus propias leyes, aduanas, monedas e instituciones de gobierno independientes.

¿Qué tres acontecimientos históricos trascendentales ocurrieron en el año 1492?
Respuesta: 1. La rendición de Boabdil y conquista del Reino Nazarí de Granada (2 de enero), 2. La expulsión de los judíos de la península, y 3. El Descubrimiento de América por Cristóbal Colón (12 de octubre).

¿Cómo financiaron los Reyes Católicos el primer viaje de Cristóbal Colón hacia las Indias?
Respuesta: Principalmente mediante fondos de la Corona de Castilla y el préstamo gestionado por banqueros y comerciantes como Luis de Santángel, además de la ayuda de los monjes del Monasterio de La Rábida.

¿Qué tribunal eclesiástico reforzaron los reyes en 1478 para perseguir a los falsos conversos y asegurar la ortodoxia católica?
Respuesta: El Tribunal del Santo Oficio de la Inquisición Española.`,
    crono: `1469: Matrimonio secreto de Isabel I de Castilla y Fernando II de Aragón en Valladolid.
1474: Isabel es proclamada reina de Castilla tras la muerte de Enrique IV.
1479: Fernando hereda el trono de Aragón: arranca la Unión Dinástica.
1492 (Enero): Conquista de Granada y fin de la presencia islámica en la península.
1492 (Marzo): Decreto de expulsión de los judíos de los reinos hispánicos.
1492 (Octubre): Cristóbal Colón avista tierra americana (Isla de Guanahaní).
1494: Firma del Tratado de Tordesillas con Portugal para repartir las zonas de navegación del Atlántico.`
  },

  revolucion: {
    tema: "La Revolución Francesa de 1789: El Fin del Antiguo Régimen",
    resumen: "La Revolución Francesa fue el proceso social y político que transformó Europa al derrocar la monarquía absolutista de Luis XVI y proclamar los principios universales de Libertad, Igualdad y Fraternidad. Impulsada por la burguesía y el pueblo llano asfixiados por los impuestos y el hambre, desembocó en la toma de la Bastilla, la Declaración de los Derechos del Hombre y del Ciudadano y la instauración de la Primera República.",
    preguntas: `¿Qué prisión y símbolo del absolutismo fue asaltada por el pueblo de París el 14 de julio de 1789?
Respuesta: La fortaleza de la Bastilla.

¿Cuáles fueron los tres estamentos de la sociedad francesa antes de la revolución?
Respuesta: El clero (Primer Estado), la nobleza (Segundo Estado) y el pueblo llano o Tercer Estado (burgueses, artesanos y campesinos).

¿Qué célebre documento redactó la Asamblea Nacional en agosto de 1789 proclamando que todos los hombres nacen libres e iguales?
Respuesta: La Declaración de los Derechos del Hombre y del Ciudadano.

¿Qué monarcas fueron ejecutados en la guillotina durante el periodo de la Convención Nacional?
Respuesta: El rey Luis XVI y su esposa la reina María Antonieta.`,
    crono: `1789 (Mayo): Convocatoria de los Estados Generales en Versalles.
1789 (14 Julio): Toma popular de la fortaleza de la Bastilla en París.
1789 (Agosto): Abolición del feudalismo y Declaración de Derechos del Hombre.
1791: Proclamación de la primera Constitución francesa.
1793: Ejecución de Luis XVI y comienzo de la etapa del Terror con Robespierre.
1799: Golpe de Estado de Napoleón Bonaparte (18 de Brumario).`
  },

  cuerpo: {
    tema: "Biología Escolar: El Sistema Circulatorio y el Corazón Humano",
    resumen: "El sistema circulatorio es la red de transporte del cuerpo humano encargada de distribuir oxígeno y nutrientes a todas las células y recoger los desechos como el dióxido de carbono. Está compuesto por el corazón (una bomba muscular de cuatro cavidades), los vasos sanguíneos (arterias, venas y capilares) y la sangre (plasma, glóbulos rojos, glóbulos blancos y plaquetas).",
    preguntas: `¿Cuáles son las cuatro cavidades del corazón humano?
Respuesta: Dos aurículas superiores (derecha e izquierda) y dos ventrículos inferiores (derecho e izquierdo).

¿Cuál es la diferencia principal entre una arteria y una vena?
Respuesta: Las arterias transportan sangre rica en oxígeno que sale del corazón hacia el cuerpo, mientras que las venas devuelven la sangre cargada de dióxido de carbono desde el cuerpo hacia el corazón.

¿Qué componente de la sangre transporta el oxígeno gracias a la hemoglobina?
Respuesta: Los glóbulos rojos o eritrocitos.

¿Qué células sanguíneas intervienen para taponar una herida y coagular la sangre?
Respuesta: Las plaquetas o trombocitos.`,
    crono: `Diástole: El corazón se relaja y las aurículas se llenan de sangre.
Sístole auricular: Las aurículas se contraen y empujan la sangre a los ventrículos.
Sístole ventricular: Los ventrículos se contraen con fuerza y expulsan la sangre a la arteria aorta y pulmonar.`
  }
};

function loadHistoryExample(key) {
  const ex = HISTORY_EXAMPLES[key];
  if (!ex) return;
  document.getElementById('historia-tema').value = ex.tema;
  document.getElementById('historia-resumen').value = ex.resumen;
  document.getElementById('historia-preguntas').value = ex.preguntas;
  document.getElementById('historia-crono').value = ex.crono;
  generateSchoolKit();
}

function parseQuestionsAndAnswers(rawText) {
  const items = [];
  const lines = rawText.split('\n');
  let currentQ = "";
  let currentA = "";

  for (let line of lines) {
    const trimmed = line.trim();
    if (!trimmed) continue;

    if (trimmed.startsWith("¿") || trimmed.toLowerCase().startsWith("pregunta") || trimmed.match(/^\d+[\.\)]/)) {
      if (currentQ && currentA) {
        items.push({ q: currentQ, a: currentA });
        currentQ = "";
        currentA = "";
      }
      currentQ = trimmed.replace(/^pregunta\s*\d*[:\.]?\s*/i, '').replace(/^\d+[\.\)]\s*/, '');
    } else if (trimmed.toLowerCase().startsWith("respuesta:") || trimmed.toLowerCase().startsWith("r:")) {
      currentA = trimmed.replace(/^respuesta:\s*/i, '').replace(/^r:\s*/i, '');
    } else {
      if (currentA) {
        currentA += " " + trimmed;
      } else if (currentQ) {
        currentA = trimmed;
      }
    }
  }

  if (currentQ && currentA) {
    items.push({ q: currentQ, a: currentA });
  }

  // Si no pudo parsear por formato estándar, creamos preguntas automáticas por párrafos
  if (items.length === 0 && rawText.length > 20) {
    const chunks = rawText.split('\n\n');
    chunks.forEach((ch, idx) => {
      if (ch.trim()) {
        items.push({
          q: `Pregunta clave ${idx + 1}: Explica los aspectos esenciales del punto destacado`,
          a: ch.trim()
        });
      }
    });
  }

  return items;
}

function generateSchoolKit() {
  const tema = document.getElementById('historia-tema').value.trim() || "Cuaderno de Repaso de Historia";
  const resumen = document.getElementById('historia-resumen').value.trim();
  const preguntasRaw = document.getElementById('historia-preguntas').value.trim();
  const cronoRaw = document.getElementById('historia-crono').value.trim();

  if (!preguntasRaw && !resumen) {
    alert("Por favor, pega al menos el Resumen o las Preguntas generadas por NotebookLM.");
    return;
  }

  const qaItems = parseQuestionsAndAnswers(preguntasRaw);

  // 1. Título y Resumen
  document.getElementById('prev-title').textContent = tema;
  document.getElementById('prev-resumen').textContent = resumen || "Repasa los conceptos clave aprendidos en clase.";

  // 2. Cuestionario con líneas punteadas para escribir a lápiz
  const qContainer = document.getElementById('prev-preguntas');
  qContainer.innerHTML = '';
  qaItems.forEach((item, idx) => {
    const qDiv = document.createElement('div');
    qDiv.style.marginBottom = '14px';
    qDiv.innerHTML = `
      <div style="font-weight: 700; color: #1e293b; margin-bottom: 6px;">
        ${idx + 1}. ${item.q}
      </div>
      <div class="handwriting-lines">
        <div class="blank-line"></div>
        <div class="blank-line"></div>
      </div>
    `;
    qContainer.appendChild(qDiv);
  });

  // 3. Tarjetas de Memoria Recortables (Flashcards)
  const fcContainer = document.getElementById('prev-flashcards');
  fcContainer.innerHTML = '';
  qaItems.forEach((item, idx) => {
    const card = document.createElement('div');
    card.className = 'flashcard';
    card.innerHTML = `
      <div>
        <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 4px;">✂️ Tarjeta de estudio #${idx + 1}</div>
        <div class="flashcard-q">${item.q}</div>
      </div>
      <div>
        <div style="font-size: 0.75rem; color: #047857; margin-bottom: 2px;">💡 Respuesta para comprobar:</div>
        <div class="flashcard-a">${item.a}</div>
      </div>
    `;
    fcContainer.appendChild(card);
  });

  // 4. Cronología
  const cronoBox = document.getElementById('prev-crono-box');
  const cronoContainer = document.getElementById('prev-crono');
  if (cronoRaw) {
    cronoBox.style.display = 'block';
    cronoContainer.innerHTML = '';
    const cLines = cronoRaw.split('\n');
    const ul = document.createElement('ul');
    ul.style.paddingLeft = '20px';
    cLines.forEach(cl => {
      if (cl.trim()) {
        const li = document.createElement('li');
        li.style.marginBottom = '4px';
        li.style.fontSize = '0.95rem';
        li.style.color = '#334155';
        li.textContent = cl.trim();
        ul.appendChild(li);
      }
    });
    cronoContainer.appendChild(ul);
  } else {
    cronoBox.style.display = 'none';
  }

  // 5. Hoja de Soluciones Oficial
  const solContainer = document.getElementById('prev-soluciones');
  solContainer.innerHTML = '';
  const ol = document.createElement('ol');
  ol.style.paddingLeft = '20px';
  qaItems.forEach(item => {
    const li = document.createElement('li');
    li.style.marginBottom = '6px';
    li.innerHTML = `<b>${item.q}</b><br/>👉 <i>${item.a}</i>`;
    ol.appendChild(li);
  });
  solContainer.appendChild(ol);

  document.getElementById('historia-result').classList.add('visible');
  document.getElementById('btn-print-historia').style.display = 'inline-flex';

  document.getElementById('historia-result').scrollIntoView({ behavior: 'smooth' });
}

// ==========================================================================
// 4. GENERACIÓN DE VISTA DE IMPRESIÓN / PDF NATIVO
// ==========================================================================
function printMathWorksheet() {
  const printArea = document.getElementById('printable-document');
  const nietoName = document.getElementById('nieto-name').value.trim() || "mi nieto";
  const question = document.getElementById('math-question').value.trim();

  const intuition = document.getElementById('res-math-intuition').innerHTML;
  const stepbystep = document.getElementById('res-math-stepbystep').innerHTML;
  const formal = document.getElementById('res-math-formal').innerHTML;
  const twin = document.getElementById('res-math-twin').innerHTML;

  printArea.innerHTML = `
    <div class="print-header">
      <div>
        <h1>📐 CUADERNO DE MATEMÁTICAS: TALLER DEL ABUELO TUTOR</h1>
        <p>Aprender razonando: explicaciones paso a paso y reto escolar</p>
      </div>
      <div class="print-meta">
        <strong>Alumno:</strong> ${nietoName}<br/>
        <strong>Fecha de estudio:</strong> ${new Date().toLocaleDateString('es-ES')}<br/>
        <strong>Revisado por:</strong> El Abuelo Tutor
      </div>
    </div>

    <div class="print-box">
      <h2>❓ El Problema Planteado:</h2>
      <p style="font-size: 11pt; font-weight: bold;">${question}</p>
    </div>

    <div class="print-box">
      <h2>🌟 1. Para comprenderlo (La analogía sencilla del abuelo):</h2>
      <p>${intuition}</p>
    </div>

    <div class="print-box">
      <h2>🧠 2. El paso a paso lógico (Sin saltos):</h2>
      <p>${stepbystep}</p>
    </div>

    <div class="print-box">
      <h2>📝 3. Desarrollo formal para el examen del colegio:</h2>
      <div>${formal}</div>
    </div>

    <div class="print-box" style="background-color: #fdfdfd; border: 2px solid #000000; margin-top: 15px;">
      <h2>🎯 4. Reto Escolar para ${nietoName} (Resuélvelo en el hueco de abajo):</h2>
      <p style="margin-bottom: 10px;">${twin}</p>
      <div style="border: 1px dashed #666; height: 160px; padding: 10px; background-color: #fafafa;">
        <span style="font-size: 9pt; color: #666;">Espacio para cálculos y desarrollo a lápiz de ${nietoName}:</span>
        <div class="print-line" style="margin-top: 25px;"></div>
        <div class="print-line" style="margin-top: 25px;"></div>
        <div class="print-line" style="margin-top: 25px;"></div>
        <div class="print-line" style="margin-top: 25px;"></div>
      </div>
      <div style="text-align: right; margin-top: 12px; font-size: 10pt;">
        Firma del Abuelo Tutor: ___________________________ | Nota: [   / 10 ]
      </div>
    </div>
  `;

  window.print();
}

function printHistoryKit() {
  const printArea = document.getElementById('printable-document');
  const nietoName = document.getElementById('nieto-name').value.trim() || "mi nieto";
  const tema = document.getElementById('historia-tema').value.trim() || "Cuaderno de Repaso de Historia";
  const resumen = document.getElementById('historia-resumen').value.trim();
  const preguntasRaw = document.getElementById('historia-preguntas').value.trim();
  const cronoRaw = document.getElementById('historia-crono').value.trim();

  const qaItems = parseQuestionsAndAnswers(preguntasRaw);

  let qHtml = '';
  qaItems.forEach((it, i) => {
    qHtml += `
      <div style="margin-bottom: 16px; page-break-inside: avoid;">
        <div style="font-weight: bold; font-size: 10.5pt; margin-bottom: 4px;">
          ${i + 1}. ${it.q}
        </div>
        <div class="print-line"></div>
        <div class="print-line"></div>
      </div>
    `;
  });

  let cardsHtml = '';
  qaItems.forEach((it, i) => {
    cardsHtml += `
      <div class="print-flashcard">
        <div style="font-size: 8pt; color: #555;">✂️ Tarjeta recortable #${i + 1} (Doblar por el medio)</div>
        <div style="font-weight: bold; font-size: 10pt; margin: 4px 0 6px 0;">[PREGUNTA]: ${it.q}</div>
        <div style="border-top: 1px dotted #888; padding-top: 4px; font-size: 9.5pt; color: #222;">
          [RESPUESTA]: ${it.a}
        </div>
      </div>
    `;
  });

  let cronoHtml = '';
  if (cronoRaw) {
    cronoHtml = `
      <div class="print-box">
        <h2>⏱️ Eje Cronológico de Fechas Clave:</h2>
        <ul style="padding-left: 20px; font-size: 10pt;">
          ${cronoRaw.split('\n').filter(l => l.trim()).map(l => `<li>${l.trim()}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  let solucionesHtml = '';
  qaItems.forEach((it, i) => {
    solucionesHtml += `
      <div style="margin-bottom: 8px; font-size: 9.5pt;">
        <b>${i + 1}. ${it.q}</b><br/>
        👉 <i>Solución correcta:</i> ${it.a}
      </div>
    `;
  });

  printArea.innerHTML = `
    <!-- PÁGINA 1: EXAMEN Y REPASO ESCOLAR -->
    <div class="print-header">
      <div>
        <h1>📚 CUADERNILLO DE REPASO ESCOLAR: ${tema.toUpperCase()}</h1>
        <p>Material de estudio preparado con NotebookLM por El Abuelo Tutor</p>
      </div>
      <div class="print-meta">
        <strong>Alumno:</strong> ${nietoName}<br/>
        <strong>Fecha:</strong> ${new Date().toLocaleDateString('es-ES')}<br/>
        <strong>Puntuación:</strong> [    / 10 ]
      </div>
    </div>

    <div class="print-box">
      <h2>📖 Resumen del Tema para Leer y Repasar:</h2>
      <p style="font-size: 10pt; line-height: 1.4;">${resumen}</p>
    </div>

    ${cronoHtml}

    <div class="print-box">
      <h2>✍️ Cuestionario de Repaso (Responde con tus palabras a lápiz):</h2>
      ${qHtml}
    </div>

    <!-- SALTO DE PÁGINA PARA TARJETAS Y SOLUCIONES -->
    <div class="page-break"></div>

    <div class="print-header">
      <div>
        <h1>🗂️ JUEGO DE TARJETAS DE MEMORIA RECORTABLES (FLASHCARDS)</h1>
        <p>Recorta por la línea de puntos y juega con tu abuelo al trivial de preguntas y respuestas</p>
      </div>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
      ${cardsHtml}
    </div>

    <div class="page-break"></div>

    <div class="print-header">
      <div>
        <h1>🔑 HOJA DE SOLUCIONES OFICIAL (EXCLUSIVA PARA EL ABUELO TUTOR)</h1>
        <p>Utiliza esta hoja para corregir el examen de tu nieto y repasar juntos las dudas</p>
      </div>
    </div>

    <div class="print-box" style="background-color: #f9f9f9;">
      ${solucionesHtml}
    </div>
  `;

  window.print();
}
