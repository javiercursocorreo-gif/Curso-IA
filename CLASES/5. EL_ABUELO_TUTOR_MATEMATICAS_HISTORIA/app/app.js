/**
 * LÓGICA DE LA APLICACIÓN "EDUCANIETOS IA"
 * Módulo 1: Tutor de Matemáticas Razonadas en 4 niveles pedagógicos e impresión en cuadrícula
 * Módulo 2: Guía metodológica para la Sesión en Pantalla con Google NotebookLM
 * Módulo 3: Decálogo Pedagógico del Abuelo Tutor
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
  else if (tabId === 'tab-historia-nlm') buttons[1].classList.add('active');
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
    twin: `<b>Reto Gemelo para Lucas:</b> Resuelve en tu cuaderno o en la cuadrícula inferior la siguiente ecuación usando exactamente la misma fórmula que acabas de ver:<br/>
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

let currentMathData = null;

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

  // Si no es un ejemplo precargado exacto, analizamos el texto libre introducido por el abuelo
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
      // Explicador estructurado en 4 capas pedagógicas universales
      data = {
        question: qText,
        intuition: `Para entender bien este concepto («${qText}»), lo primero que debemos decirle a ${nietoName} es que no tenga miedo a los signos ni a los enunciados largos. En la vida diaria, las matemáticas no son números fríos sino una forma de contar historias ordenadas: repartir caramelos con amigos, medir el tiempo de una película o calcular si nos llega la paga semanal.`,
        stepbystep: `1º Leemos el enunciado despacio subrayando los datos que conocemos con lápiz azul, y lo que nos piden averiguar con lápiz rojo.<br/>
2º Planteamos la relación lógica: ¿la cantidad aumenta o disminuye? ¿estamos sumando partes o repartiendo un total?<br/>
3º Realizamos las operaciones de una en una, comprobando en cada línea que el resultado tiene sentido en el mundo real (por ejemplo: si calculamos la edad de una persona, no puede darnos 250 años ni un número negativo).`,
        formal: `<div class="math-formula">Planteamiento formal para el cuaderno escolar de ${nietoName}:</div>
• Datos identificados claramente en el margen izquierdo.<br/>
• Fórmula o ecuación correspondiente al tema del libro de texto.<br/>
• Despeje ordenado renglón por renglón sin saltarse pasos intermedios.<br/>
• <b>Resultado final recuadrado con sus unidades correspondientes (metros, euros, horas, etc.).</b>`,
        twin: `<b>Reto Gemelo para ${nietoName}:</b><br/>
Prueba a resolver este mismo ejercicio en la cuadrícula inferior, pero cambiando los valores por el doble para asegurarte de que dominas el procedimiento y no solo el resultado de memoria.`
      };
    }
  }

  currentMathData = {
    ...data,
    questionText: qText,
    nietoName: nietoName
  };

  // Pintar en pantalla
  document.getElementById('math-result-title').textContent = `📖 Ficha Pedagógica: ${qText.substring(0, 60)}...`;
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
// 3. IMPRESIÓN DE LA FICHA DE MATEMÁTICAS CON CUADRÍCULA
// ==========================================================================
function printMathWorksheet() {
  if (!currentMathData) return;

  const pDoc = document.getElementById('printable-document');
  const now = new Date();
  const fechaStr = now.toLocaleDateString('es-ES', { day: '2-digit', month: 'long', year: 'numeric' });
  const nieto = currentMathData.nietoName || "Alumno";

  pDoc.innerHTML = `
    <div class="print-header">
      <div>
        <h1>📐 Cuaderno de Matemáticas Razonadas</h1>
        <div style="font-size: 11pt; color: #333; margin-top: 4px;">Tutor: Educanietos IA</div>
      </div>
      <div class="print-meta">
        <div><strong>Alumno/a:</strong> ${nieto}</div>
        <div><strong>Fecha:</strong> ${fechaStr}</div>
      </div>
    </div>

    <div class="print-box">
      <h2>📌 El Problema a Resolver:</h2>
      <p style="font-size: 11pt; font-weight: bold; margin-top: 4px;">${currentMathData.questionText}</p>
    </div>

    <div class="print-box">
      <h2>🌟 1. La Idea Intuitiva (Para comprenderlo sin miedo):</h2>
      <p style="font-size: 10.5pt; line-height: 1.45;">${currentMathData.intuition.replace(/Lucas/g, nieto)}</p>
    </div>

    <div class="print-box">
      <h2>🧠 2. El Paso a Paso Razonado:</h2>
      <div style="font-size: 10pt; line-height: 1.45;">${currentMathData.stepbystep.replace(/Lucas/g, nieto).replace(/\n/g, '<br/>')}</div>
    </div>

    <div class="print-box">
      <h2>📝 3. Solución Formal para el Examen:</h2>
      <div style="font-size: 10pt; line-height: 1.45;">${currentMathData.formal}</div>
    </div>

    <div class="page-break"></div>

    <div class="print-header">
      <div>
        <h1>🎯 Reto Gemelo: ¡Demuestra lo que sabes!</h1>
        <div style="font-size: 10pt; color: #333;">Espacio de trabajo a lápiz para ${nieto}</div>
      </div>
      <div class="print-meta">
        <div><strong>Calificación:</strong> [ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ]</div>
      </div>
    </div>

    <div class="print-box">
      <h2>Enunciado del Reto:</h2>
      <p style="font-size: 11pt; line-height: 1.45;">${currentMathData.twin.replace(/Lucas/g, nieto)}</p>
    </div>

    <div style="margin-top: 14px;">
      <h3 style="font-size: 11pt; margin-bottom: 6px;">✏️ Resuelve aquí paso a paso (Usa lápiz y regla):</h3>
      <div class="print-grid"></div>
    </div>

    <div style="margin-top: 20px; border-top: 1px solid #999; padding-top: 8px; font-size: 9pt; color: #555; text-align: center;">
      Educanietos IA • Metodología de Razonamiento Socrático para el Éxito Escolar
    </div>
  `;

  window.print();
}
