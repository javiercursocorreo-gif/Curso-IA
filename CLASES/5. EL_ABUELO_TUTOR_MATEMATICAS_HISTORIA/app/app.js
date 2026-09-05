/**
 * LÓGICA DE LA APLICACIÓN "EDUCANIETOS IA"
 * Tutor de Matemáticas Razonadas con Gran Valor Pedagógico
 * Analogías cotidianas, explicaciones profundas, gráficas SVG y chat socrático
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

  const buttons = document.querySelectorAll('.tab-btn');
  if (tabId === 'tab-mates') buttons[0].classList.add('active');
  else if (tabId === 'tab-historia-nlm') buttons[1].classList.add('active');
  else if (tabId === 'tab-guia') buttons[2].classList.add('active');
}

// ==========================================================================
// 2. BASE DE CONOCIMIENTO PEDAGÓGICO AVANZADO CON GRÁFICAS VECTORIALES SVG
// ==========================================================================
const MATH_KNOWLEDGE_BASE = {
  // --- DERIVADAS ---
  // --- DERIVADAS Y PENDIENTE DE UNA CURVA ---
  derivada: {
    title: "La Derivada y la Pendiente de una Curva: La inclinación exacta en cada punto",
    intuition: `Dile a tu nieto: <i>«Imagínate que vas en bicicleta subiendo un puerto de montaña en los Pirineos.
Si la carretera fuera una rampa recta de garaje, la cuesta tendría siempre la misma pendiente: por ejemplo, subes 10 metros por cada 100 metros de carretera (pendiente fija del 10%).
Pero una montaña real es una curva: empieza suave con un falso llano, luego se empina con una cuesta brutal del 18% donde tienes que pedalear de pie sobre los pedales, luego corona en la cima en una carretera completamente horizontal (pendiente 0%), y finalmente se lanza cuesta abajo.
¿Cómo sabes lo empinada que está la cuesta en el punto exacto donde tienes apoyada la rueda de la bicicleta en este mismo segundo?
Apoyas una regla recta de madera (o un monopatín) sobre la rueda de la bici de forma que solo roce en ese punto sin clavarse en el suelo: esa regla es la <b>Recta Tangente</b>.
Y la inclinación de esa regla es exactamente <b>LA DERIVADA</b>.
<b>LA REGLA DE ORO: La Derivada en un punto ES la Pendiente de la curva en ese punto exacto:</b>
• Si la derivada es positiva (+): Vas cuesta arriba (la curva sube).
• Si la derivada es cero (0): Estás en la cima de la montaña (máximo) o en el fondo del valle (mínimo, terreno plano horizontal).
• Si la derivada es negativa (-): Vas cuesta abajo (la curva decrece).
Cuanto mayor sea el número de la derivada, ¡más empinada es la pared de la curva!»</i>`,
    stepbystep: `¿Cómo se pasa de dos puntos a la inclinación en un punto exacto?
1º <b>La Secante (Pendiente media entre dos puntos):</b> Si tomas dos puntos separados sobre la curva (el punto P y el punto Q), la recta que pasa por ambos es una <b>recta secante</b> (la línea naranja discontinua en la gráfica). Su pendiente mide el cambio medio entre dos momentos distantes: m_sec = [f(x + h) - f(x)] / h.
2º <b>El paso al límite (h tiende a 0):</b> Pero nosotros no queremos la pendiente media entre dos pueblos, ¡queremos la inclinación exacta en el punto P!
3º <b>El giro de la recta:</b> A medida que acercamos el punto Q hacia el punto P (haciendo que la distancia 'h' se encoja hacia cero), la recta secante naranja va girando sobre el punto P...
4º <b>La Tangente definitiva:</b> En el instante exacto en que Q se funde con P, la secante se convierte en la <b>recta tangente roja</b>, que toca a la curva en ese único punto P sin atravesarla.
5º Por eso los matemáticos definen: <b>Derivada = Pendiente de la recta tangente = lim (h → 0) [f(x + h) - f(x)] / h</b>.`,
    graphDesc: "<b>De la Secante a la Tangente (Geometría Exacta):</b> El punto P (rojo) está sobre la curva. La recta tangente roja toca la curva en P y su inclinación es la Derivada. La recta secante naranja une P con Q, y al hacer h → 0 se convierte en la tangente.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <defs>
          <pattern id="grid-der" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="1"/>
          </pattern>
          <marker id="arrow-der" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#ea580c"/>
          </marker>
        </defs>
        <rect width="580" height="250" fill="url(#grid-der)" />
        
        <!-- Ejes -->
        <line x1="50" y1="210" x2="550" y2="210" stroke="#475569" stroke-width="2"/>
        <line x1="60" y1="220" x2="60" y2="20" stroke="#475569" stroke-width="2"/>
        <text x="540" y="230" font-size="12" fill="#475569" font-weight="bold">x</text>
        <text x="70" y="30" font-size="12" fill="#475569" font-weight="bold">y = f(x)</text>
        
        <!-- Curva f(x): P0(80,200), P1(240,200), P2(440,40) -->
        <path d="M 80 200 Q 240 200 440 40" fill="none" stroke="#0b2545" stroke-width="4"/>
        
        <!-- Recta Secante (Naranja discontinua): Pasa exactamente por P(250,160) y Q(362,98) -->
        <line x1="110" y1="238" x2="440" y2="55" stroke="#f97316" stroke-width="2.5" stroke-dasharray="6,4"/>
        
        <!-- Recta Tangente (Roja sólida): Toca a la curva EXACTAMENTE en P(250,160) con pendiente -4/9 -->
        <line x1="70" y1="240" x2="430" y2="80" stroke="#dc2626" stroke-width="3.5"/>
        
        <!-- Punto P (250, 160) -->
        <circle cx="250" cy="160" r="6" fill="#dc2626" stroke="#ffffff" stroke-width="2"/>
        <text x="160" y="152" font-size="12" font-weight="bold" fill="#dc2626">P (Punto exacto)</text>
        
        <!-- Punto Q (362, 98) -->
        <circle cx="362" cy="98" r="6" fill="#f97316" stroke="#ffffff" stroke-width="2"/>
        <text x="375" y="96" font-size="12" font-weight="bold" fill="#f97316">Q (Punto x + h)</text>
        
        <!-- Flecha de convergencia de Q hacia P a lo largo de la curva -->
        <path d="M 345 108 Q 295 138 265 154" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrow-der)"/>
        <text x="290" y="124" font-size="11" font-weight="bold" fill="#ea580c">h → 0</text>
        
        <!-- Leyenda didáctica -->
        <rect x="70" y="36" width="230" height="54" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
        <line x1="80" y1="52" x2="110" y2="52" stroke="#f97316" stroke-width="2.5" stroke-dasharray="4,3"/>
        <text x="118" y="56" font-size="11" fill="#334155">Secante: Pendiente media Δy/Δx</text>
        <line x1="80" y1="74" x2="110" y2="74" stroke="#dc2626" stroke-width="3.5"/>
        <text x="118" y="78" font-size="11" font-weight="bold" fill="#dc2626">Tangente: Pendiente = Derivada f'(x)</text>
      </svg>
    `,
    formal: `<div class="math-formula">Relación Fundamental: Pendiente de la Tangente m = f'(x₀)</div>
<b>1. Definición como límite de pendientes de secantes:</b>
m_secante = [f(x₀ + h) - f(x₀)] / h  -->  m_tangente = f'(x₀) = lim (h → 0) [f(x₀ + h) - f(x₀)] / h
<br/><br/>
<b>2. Ejercicio Clásico de Examen: Ecuación de la Recta Tangente</b>
Halla la recta tangente a la curva f(x) = x² en el punto x₀ = 3:
• <b>Paso 1:</b> Derivamos para obtener la pendiente: f'(x) = 2x  -->  <b>m = f'(3) = 2(3) = 6</b>
• <b>Paso 2:</b> Hallamos el punto de la curva: y₀ = f(3) = 3² = 9  -->  Punto P(3, 9)
• <b>Paso 3:</b> Ecuación punto-pendiente: y - y₀ = m · (x - x₀)
  y - 9 = 6 · (x - 3)  -->  y - 9 = 6x - 18  -->  <b>y = 6x - 9</b>
<i>(Justificación para el profesor: «La pendiente de la recta tangente coincide exactamente con la derivada evaluada en el punto de tangencia»).</i>`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Dada la curva f(x) = x² + 2x, halla la pendiente de la recta tangente en el punto x = 1.<br/>
<i>Pista del abuelo: Deriva la función: f'(x) = 2x + 2. Ahora sustituye x por 1: f'(1) = 2(1) + 2 = 4. ¡La pendiente de la cuesta en ese punto vale 4!</i>`
  },

  // --- INTEGRALES ---
  integral: {
    title: "Cálculo Integral: El arte de sumar infinitas rodajas invisibles",
    intuition: `Imagínate que vas en coche y el velocímetro está roto, pero necesitas saber con exactitud cuántos kilómetros has recorrido en un viaje de 2 horas.
Si el coche hubiera ido siempre a 100 km/h en línea recta sin parar, es una multiplicación de niños de primaria: 100 km/h × 2 horas = 200 km. Es un rectángulo perfecto y plano (velocidad fija × tiempo).
Pero en la vida real te encuentras un atasco, frenas en un semáforo en rojo, aceleras en una cuesta... Tu velocidad cambia a cada segundo formando una gráfica llena de montañas, picos y valles. ¿Cómo calculas los kilómetros totales recorridos si la velocidad nunca fue constante?
O imagínate que quieres medir cuánta agua ha caído en una tormenta que empezó con cuatro gotas sueltas, luego descargó un chaparrón torrencial y al final fue aflojando poco a poco.
Aquí es donde Arquímedes, Newton y Leibniz inventaron la <b>Integral</b>:
<i>«Si divido el tiempo en rodajitas microscópicas (de una décima de segundo o menos), en ese instante tan diminuto el coche casi no cambió de velocidad. Es un rectangulito casi plano. Calculo los metros de ese rectangulito... ¡y luego SUMO los millones de rectangulitos de todo el viaje!»</i>.
Eso es una integral: <b>el pegamento matemático que suma infinitos trocitos microscópicos para calcular un total acumulado</b> (el área bajo una curva irregular, los litros de una piscina con formas onduladas o los kilómetros de un viaje).
¿Sabías que el símbolo de la integral <b>«∫»</b> no es una letra extraña? ¡Es simplemente una letra <b>'S'</b> alargada que inventó Leibniz para abreviar la palabra <b>SUMA</b>!`,
    stepbystep: `Veamos cómo funciona con el ejemplo físico más limpio: la piedra que cae desde un puente acelerada por la gravedad.
1º <b>La velocidad en rampa:</b> Al soltar la piedra, cada segundo que pasa la gravedad le añade 9,8 metros por segundo de velocidad (v = 9,8 · t). A los 0 segundos la velocidad es 0, al segundo 1 es 9,8 m/s, al segundo 2 es 19,6 m/s... La gráfica es una rampa que sube en diagonal formando un triángulo.
2º <b>La suma de áreas:</b> Para saber cuántos metros cae en 3 segundos, tenemos que sumar toda la superficie debajo de esa rampa triangular.
3º <b>La regla mágica de la integral:</b> Si una función es x (una rampa de una dimensión), su integral es <b>(x²)/2</b>.
4º <b>¿Por qué aparece un cuadrado (x²)?</b> ¡Porque al sumar infinitas líneas estamos creando una superficie plana (un área de 2 dimensiones)! Y si volviéramos a integrar esa área plana (x²), obtendríamos un volumen tridimensional de 3 dimensiones: <b>(x³)/3</b>.
Integrar es como apilar hojas de papel finísimas, una sobre otra, hasta construir un libro gordo.`,
    graphDesc: "<b>La Integral como suma de rodajas acumuladas:</b> El área azul irregular bajo la curva f(x) se calcula sumando millones de tiras o rectángulos verticales finísimos de ancho Δx (Sumas de Riemann).",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <defs>
          <pattern id="grid-int" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="1"/>
          </pattern>
        </defs>
        <rect width="580" height="250" fill="url(#grid-int)" />
        
        <!-- Ejes -->
        <line x1="50" y1="210" x2="550" y2="210" stroke="#475569" stroke-width="2"/>
        <line x1="60" y1="220" x2="60" y2="20" stroke="#475569" stroke-width="2"/>
        <text x="540" y="230" font-size="12" fill="#475569" font-weight="bold">x</text>
        <text x="70" y="30" font-size="12" fill="#475569" font-weight="bold">y = f(x)</text>
        
        <!-- Rectángulos de Riemann (rodajitas verticales) -->
        <rect x="140" y="150" width="40" height="60" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5" opacity="0.8"/>
        <rect x="180" y="115" width="40" height="95" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5" opacity="0.8"/>
        <rect x="220" y="90" width="40" height="120" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5" opacity="0.8"/>
        <rect x="260" y="75" width="40" height="135" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5" opacity="0.8"/>
        <rect x="300" y="70" width="40" height="140" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5" opacity="0.8"/>
        <rect x="340" y="80" width="40" height="130" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5" opacity="0.8"/>
        <rect x="380" y="105" width="40" height="105" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5" opacity="0.8"/>
        <rect x="420" y="140" width="40" height="70" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5" opacity="0.8"/>
        
        <!-- Curva f(x) -->
        <path d="M 80 190 C 180 50, 320 50, 500 200" fill="none" stroke="#0369a1" stroke-width="3.5"/>
        
        <!-- Puntos a y b -->
        <line x1="140" y1="210" x2="140" y2="220" stroke="#0f172a" stroke-width="2"/>
        <text x="136" y="235" font-size="13" font-weight="bold" fill="#0f172a">a</text>
        <line x1="460" y1="210" x2="460" y2="220" stroke="#0f172a" stroke-width="2"/>
        <text x="456" y="235" font-size="13" font-weight="bold" fill="#0f172a">b</text>
        
        <!-- Etiquetas explicativas -->
        <text x="240" y="150" font-size="14" font-weight="bold" fill="#0369a1">Área = ∫ₐᵇ f(x) dx</text>
        <text x="270" y="202" font-size="11" fill="#0f172a">Δx (tira)</text>
        
        <!-- Cartel explicativo -->
        <rect x="340" y="25" width="220" height="44" rx="8" fill="#f0f9ff" stroke="#7dd3fc" stroke-width="1.2"/>
        <text x="350" y="42" font-size="11" font-weight="bold" fill="#0369a1">💡 S de SUMA (∫)</text>
        <text x="350" y="58" font-size="10" fill="#334155">Al sumar infinitas tiras, el área es exacta.</text>
      </svg>
    `,
    formal: `<div class="math-formula">Operador Integral: ∫ f(x) dx</div>
<b>1. Integral Indefinida (La Primitiva):</b>
Regla de las potencias: ∫ xⁿ dx = [xⁿ⁺¹ / (n + 1)] + C  (para n ≠ -1)
Ejemplo: ∫ (2x) dx = 2 · (x² / 2) + C = <b>x² + C</b>
<i>(Nota para el alumno: Se suma siempre la constante '+ C' porque cualquier número suelto tiene derivada igual a cero).</i><br/><br/>
<b>2. Integral Definida y Regla de Barrow (Cálculo del área exacta entre dos puntos a y b):</b>
∫ₐᵇ f(x) dx = [F(x)]ₐᵇ = F(b) - F(a)
Ejemplo: Calcular el área bajo la recta f(x) = 2x entre x = 0 y x = 3:
F(x) = x²
Área = F(3) - F(0) = (3)² - (0)² = 9 - 0 = <b>9 unidades cuadradas</b>.`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Un grifo averiado empieza cerrado y cada hora que pasa se abre un poco más, echando agua a un ritmo de f(t) = 4t litros por hora.<br/>
¿Cuántos litros exactos de agua se acumularán en el cubo después de 2 horas?<br/>
<i>Pista del abuelo: Halla la primitiva de 4t (que es 2t²) y calcula cuánto vale a las 2 horas: 2 · (2)² = 2 · 4 = 8 litros. ¡Mucho menos que si hubiera estado abierto a tope desde el principio!</i>`
  },

  // --- LOGARITMOS ---
  logaritmo: {
    title: "Logaritmos: La llave maestra para abrir candados de potencias gigantescas",
    intuition: `Imagínate que las potencias son una máquina de multiplicar que fabrica monstruos gigantescos:
Si pones un 10 y lo elevas al cubo (10³), te sale 1.000. Si lo elevas a la 6 (10⁶), te sale un millón.
En una potencia normal tú conoces la base (10) y el exponente (3) y buscas el número grande.
El <b>Logaritmo</b> es exactamente el viaje de vuelta, como un detective que tiene la caja fuerte cerrada y pregunta:
<i>«¿A qué número tuve que elevar el 10 para conseguir 1.000?»</i> -> Respuesta: al 3. Por eso: log₁₀(1000) = 3.
¿Para qué sirve esto a un científico, un arquitecto o un médico?
Sirve para <b>domesticar números gigantescos que no caben en una regla</b>:
• <b>Los terremotos (Escala Richter):</b> Un terremoto de magnitud 7 no es un punto más fuerte que uno de magnitud 6: ¡es 10 VECES más demoledor! Y uno de 8 es 100 veces más fuerte. Si no usáramos logaritmos, en la gráfica tendríamos que dibujar una línea de kilómetros para comparar un temblor con el de Japón.
• <b>El sonido (Decibelios):</b> El oído humano escucha desde el roce de una hoja hasta el motor de un avión a reacción (que tiene un billón de veces más energía sonora). El logaritmo permite comprimir ese billón en una escala del 0 al 140.`,
    stepbystep: `1º La regla de oro del logaritmo es transformar operaciones difíciles en operaciones fáciles:
• Convierte las multiplicaciones en sumas: log(A · B) = log(A) + log(B).
• Convierte las divisiones en restas: log(A / B) = log(A) - log(B).
• Convierte las potencias en multiplicaciones sencillas: log(Aⁿ) = n · log(A). (¡El exponente baja al suelo como por un tobogán!).
2º Cuando en el colegio veas «log» sin ningún número abajo, significa que la base es 10 (logaritmo decimal).
3º Cuando veas «ln», es el logaritmo natural o neperiano, cuya base es el famoso número 'e' (2,7182...).`,
    graphDesc: "<b>La Escala Logarítmica:</b> Convierte saltos gigantescos de multiplicación (×10, ×100, ×1.000) en pasos iguales de una regla (1, 2, 3). Permite representar en un folio tanto un susurro como el despegue de un cohete.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <rect width="580" height="250" fill="#f8fafc"/>
        
        <!-- Ejes -->
        <line x1="60" y1="200" x2="540" y2="200" stroke="#334155" stroke-width="2.5"/>
        <line x1="70" y1="210" x2="70" y2="30" stroke="#334155" stroke-width="2"/>
        <text x="500" y="225" font-size="12" font-weight="bold" fill="#334155">Valor real x</text>
        <text x="80" y="45" font-size="12" font-weight="bold" fill="#0284c7">y = log₁₀(x)</text>

        <!-- Curva Logarítmica y = log10(x) -->
        <path d="M 80 200 C 130 140, 260 100, 520 70" fill="none" stroke="#0284c7" stroke-width="3.5"/>

        <!-- Puntos clave: x=1 -> y=0 -->
        <circle cx="80" cy="200" r="5.5" fill="#dc2626"/>
        <text x="75" y="218" font-size="11" font-weight="bold" fill="#dc2626">x = 1 (10⁰)</text>
        <text x="75" y="190" font-size="11" fill="#475569">y = 0</text>

        <!-- x=10 -> y=1 -->
        <circle cx="180" cy="140" r="5.5" fill="#2563eb"/>
        <line x1="180" y1="200" x2="180" y2="140" stroke="#94a3b8" stroke-dasharray="3,3"/>
        <text x="160" y="218" font-size="11" font-weight="bold" fill="#2563eb">x = 10 (10¹)</text>
        <text x="140" y="140" font-size="11" font-weight="bold" fill="#2563eb">y = 1</text>

        <!-- x=100 -> y=2 -->
        <circle cx="330" cy="100" r="5.5" fill="#059669"/>
        <line x1="330" y1="200" x2="330" y2="100" stroke="#94a3b8" stroke-dasharray="3,3"/>
        <text x="310" y="218" font-size="11" font-weight="bold" fill="#059669">x = 100 (10²)</text>
        <text x="290" y="100" font-size="11" font-weight="bold" fill="#059669">y = 2</text>

        <!-- x=1000 -> y=3 -->
        <circle cx="500" cy="73" r="5.5" fill="#d97706"/>
        <line x1="500" y1="200" x2="500" y2="73" stroke="#94a3b8" stroke-dasharray="3,3"/>
        <text x="470" y="218" font-size="11" font-weight="bold" fill="#d97706">x = 1.000 (10³)</text>
        <text x="455" y="75" font-size="11" font-weight="bold" fill="#d97706">y = 3</text>

        <!-- Cartel explicativo -->
        <rect x="220" y="25" width="220" height="46" rx="8" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.2"/>
        <text x="230" y="43" font-size="11.5" font-weight="bold" fill="#1e40af">💡 Domar Números Monstruosos</text>
        <text x="230" y="58" font-size="10.5" fill="#334155">Multiplicar por 10 es solo sumar +1 en 'y'.</text>
      </svg>
    `,
    formal: `<div class="math-formula">Definición: log_b(a) = c  ⟺  bᶜ = a   (con b > 0, b ≠ 1, a > 0)</div>
<b>Ejemplos típicos de examen:</b>
• log₂(8) = 3  (porque 2³ = 8)
• log₁₀(100.000) = 5  (porque 10⁵ = 100.000, cuenta los 5 ceros)
• log₃(81) = 4  (porque 3 · 3 · 3 · 3 = 81)
<b>Ecuación logarítmica clásica:</b> 2ˣ = 50  --> Tomamos logaritmos: x · log(2) = log(50) --> x = log(50) / log(2) ≈ 5,64.`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Calcula de cabeza el valor de los siguientes tres logaritmos usando la pregunta mágica del abuelo:<br/>
1) log₂(64) = ?  (¿Cuántas veces multiplicas el 2 por sí mismo para llegar a 64?)<br/>
2) log₁₀(1.000.000) = ?<br/>
3) log₅(25) = ?<br/>
<i>Respuestas: 1) 6 (porque 2⁶ = 64). 2) 6 (tiene 6 ceros). 3) 2 (porque 5² = 25).</i>`
  },

  // --- ECUACIONES DE SEGUNDO GRADO ---
  ecuacion2: {
    title: "Ecuaciones de 2º Grado: La cerradura con dos llaves y las baldosas cuadradas",
    intuition: `Imagínate que estás en una habitación y quieres embaldosar el suelo con losetas cuadradas.
En una ecuación normal de primer grado (como 2x = 8) buscamos una sola longitud de cuerda (x = 4).
Pero en una de segundo grado, la incógnita 'x' está multiplicada por sí misma (x²), lo que forma una superficie, un cuadrado plano.
Por eso en las ecuaciones de segundo grado <b>casi siempre existen DOS soluciones reales diferentes</b> que hacen que la balanza dé cero. ¡Es exactamente igual que una cerradura de seguridad que tiene dos llaves distintas y cualquiera de las dos abre la puerta!
Por ejemplo, si x² = 9, la x puede valer +3 (porque 3 × 3 = 9), pero también puede valer -3 (porque un número negativo multiplicado por otro negativo vuelve a dar positivo: (-3) × (-3) = +9).`,
    stepbystep: `1º Ordenamos siempre la ecuación para que quede igualada a cero: a·x² + b·x + c = 0.
2º Reconocemos a los tres guardianes:
• 'a' es el número pegado a la x² (las baldosas cuadradas).
• 'b' es el número pegado a la x simple (las tiras de borde).
• 'c' es el número suelto sin letras (las esquinas).
3º Aplicamos la célebre fórmula cuadrática general. El signo «±» (más o menos) es el cruce de caminos que nos llevará a las dos llaves de la cerradura.`,
    graphDesc: "<b>La Parábola cortando el suelo:</b> Las dos soluciones de la ecuación x² - 5x + 6 = 0 son exactamente los dos puntos rojos (x₁=2 y x₂=3) donde la curva corta el eje horizontal del suelo.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <defs>
          <pattern id="grid-eq" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="1"/>
          </pattern>
        </defs>
        <rect width="580" height="250" fill="url(#grid-eq)" />
        
        <!-- Ejes -->
        <line x1="50" y1="170" x2="530" y2="170" stroke="#334155" stroke-width="2.5"/>
        <line x1="120" y1="230" x2="120" y2="20" stroke="#334155" stroke-width="2"/>
        <text x="500" y="162" font-size="12" fill="#334155" font-weight="bold">Eje X (Suelo y=0)</text>
        <text x="130" y="32" font-size="12" fill="#334155" font-weight="bold">Eje Y</text>
        
        <!-- Parábola y = x^2 - 5x + 6 -->
        <path d="M 160 40 Q 280 310 400 40" fill="none" stroke="#2563eb" stroke-width="3.5"/>
        
        <!-- Cortes x1 = 2 y x2 = 3 -->
        <circle cx="230" cy="170" r="6.5" fill="#dc2626" stroke="#ffffff" stroke-width="2"/>
        <text x="205" y="196" font-size="13" font-weight="bold" fill="#dc2626">x₁ = 2</text>
        
        <circle cx="330" cy="170" r="6.5" fill="#dc2626" stroke="#ffffff" stroke-width="2"/>
        <text x="325" y="196" font-size="13" font-weight="bold" fill="#dc2626">x₂ = 3</text>
        
        <!-- Vértice -->
        <circle cx="280" cy="205" r="4.5" fill="#047857"/>
        <text x="250" y="225" font-size="11" fill="#047857" font-weight="bold">Vértice (Mínimo)</text>
        
        <!-- Cartel explicativo -->
        <rect x="290" y="20" width="260" height="46" rx="8" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>
        <text x="300" y="38" font-size="11.5" font-weight="bold" fill="#1e40af">🎯 Dos soluciones = Dos cortes en el suelo</text>
        <text x="300" y="54" font-size="10" fill="#334155">En x=2 y x=3 el resultado es exactamente cero.</text>
      </svg>
    `,
    formal: `<div class="math-formula">x = [-b ± √(b² - 4ac)] / (2a)</div>
Ejemplo: x² - 5x + 6 = 0  (a=1, b=-5, c=6)
x = [-(-5) ± √((-5)² - 4·1·6)] / (2·1)
x = [5 ± √(25 - 24)] / 2 = [5 ± √1] / 2 = [5 ± 1] / 2
• Camino (+): x₁ = (5 + 1) / 2 = 6 / 2 = <b>3</b>
• Camino (-): x₂ = (5 - 1) / 2 = 4 / 2 = <b>2</b>
<i>Comprobación: 3² - 5(3) + 6 = 9 - 15 + 6 = 0 | 2² - 5(2) + 6 = 4 - 10 + 6 = 0</i>`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Resuelve a lápiz en la cuadrícula la ecuación: x² - 7x + 12 = 0.<br/>
<i>Pista del abuelo: Busca dos números que sumados den 7 y multiplicados den 12. ¡Son el 3 y el 4!</i>`
  },

  // --- COCHES Y MOVIMIENTO ---
  coches: {
    title: "Problemas de Encuentro y Velocidad: La cuerda elástica que se encoge",
    intuition: `Imagínate que Madrid y Barcelona están unidas por una cuerda gigante y tirante de 670 kilómetros.
Un coche sale de Madrid a las 10:00 viajando a 100 km/h. El otro coche sale de Barcelona a las 11:00 viajando a 90 km/h.
Durante la primera hora entera (de 10 a 11), el coche de Barcelona sigue aparcado en el garaje. Solo viaja el de Madrid, que recorta 100 km de cuerda.
A las 11:00 en punto, la cuerda que los separa mide solo 570 kilómetros.
En ese instante arranca el de Barcelona. Como los dos coches van el uno hacia el otro, ¡sus velocidades se suman! Cada hora devoran juntos 100 + 90 = 190 km de carretera.
Ahora el problema se reduce a ver cuántas veces cabe 190 dentro de 570: ¡exactamente 3 horas!`,
    stepbystep: `1º Ventaja inicial (de 10:00 a 11:00): 1 hora × 100 km/h = 100 km recorridos. Distancia restante: 670 - 100 = 570 km.
2º Velocidad combinada de aproximación: 100 + 90 = 190 km/h.
3º Tiempo hasta el choque/cruce: Tiempo = 570 / 190 = 3 horas.
4º Hora del cruce: 11:00 + 3 horas = <b>14:00 horas (las dos de la tarde)</b>.
5º Lugar del cruce: El coche de Madrid condujo 4 horas en total (4 × 100 = 400 km de Madrid).`,
    graphDesc: "<b>Gráfica de Posición vs. Tiempo:</b> La línea azul representa el coche de Madrid y la roja el de Barcelona. Se cruzan exactamente en el punto de encuentro a las 14:00 h a 400 km de Madrid.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <defs>
          <pattern id="grid-c" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="1"/>
          </pattern>
        </defs>
        <rect width="580" height="250" fill="url(#grid-c)" />
        
        <!-- Ejes -->
        <line x1="80" y1="200" x2="540" y2="200" stroke="#334155" stroke-width="2"/>
        <line x1="90" y1="210" x2="90" y2="20" stroke="#334155" stroke-width="2"/>
        
        <!-- Marcas de tiempo en X -->
        <text x="80" y="218" font-size="11" fill="#475569">10:00</text>
        <text x="160" y="218" font-size="11" fill="#475569">11:00</text>
        <text x="240" y="218" font-size="11" fill="#475569">12:00</text>
        <text x="320" y="218" font-size="11" fill="#475569">13:00</text>
        <text x="400" y="218" font-size="11" font-weight="bold" fill="#047857">14:00</text>
        <text x="480" y="218" font-size="11" fill="#475569">15:00</text>
        
        <!-- Marcas en Y -->
        <text x="15" y="205" font-size="10" fill="#475569">0 km (Mad)</text>
        <text x="10" y="98" font-size="10" font-weight="bold" fill="#047857">400 km</text>
        <text x="15" y="38" font-size="10" fill="#475569">670 km (Bcn)</text>
        
        <!-- Líneas guía de cruce -->
        <line x1="90" y1="95" x2="400" y2="95" stroke="#cbd5e1" stroke-dasharray="4,4"/>
        <line x1="400" y1="95" x2="400" y2="200" stroke="#cbd5e1" stroke-dasharray="4,4"/>
        
        <!-- Coche Madrid (Azul) -->
        <line x1="90" y1="200" x2="400" y2="95" stroke="#2563eb" stroke-width="3.5"/>
        <text x="180" y="160" font-size="11" font-weight="bold" fill="#2563eb">Madrid (100 km/h)</text>
        
        <!-- Coche Barcelona (Rojo) -->
        <line x1="90" y1="35" x2="170" y2="35" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="4,4"/>
        <text x="95" y="28" font-size="9" fill="#991b1b">En garaje</text>
        <line x1="170" y1="35" x2="400" y2="95" stroke="#dc2626" stroke-width="3.5"/>
        <text x="250" y="58" font-size="11" font-weight="bold" fill="#dc2626">Barcelona (90 km/h)</text>
        
        <!-- Punto estrella de encuentro -->
        <circle cx="400" cy="95" r="7" fill="#f59e0b" stroke="#ffffff" stroke-width="2.5"/>
        <text x="350" y="80" font-size="12" font-weight="bold" fill="#b45309">⭐ ¡Cruce a las 14:00!</text>
      </svg>
    `,
    formal: `<div class="math-formula">Ecuación de Movimiento: e = v · t</div>
Posición Coche Madrid: x₁(t) = 100 · t
Posición Coche Barcelona: x₂(t) = 670 - 90 · (t - 1)
Punto de encuentro x₁ = x₂:
100t = 670 - 90t + 90  -->  190t = 760  -->  <b>t = 4 horas desde las 10:00</b>.
Hora: 10:00 + 4h = <b>14:00 h</b>. Distancia: x = 100 · 4 = <b>400 km de Madrid</b>.`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Dos ciclistas salen a encontrarse entre dos pueblos separados por 90 km. El ciclista A sale a las 09:00 a 20 km/h. El ciclista B sale a las 10:00 hacia él a 15 km/h. ¿A qué hora se cruzarán?<br/>
<i>Pista del abuelo: El ciclista A hace 20 km en su primera hora. Quedan 70 km que se comen entre los dos a 35 km/h (2 horas). ¡Se cruzan a las 12:00!</i>`
  },

  // --- TRIGONOMETRÍA ---
  trigonometria: {
    title: "Trigonometría: Medir la altura de una torre sin subirte a ella",
    intuition: `Imagínate que estás frente a un pino gigante o la torre de una iglesia y quieres saber cuánto mide, pero no tienes una escalera kilométrica para subirte a poner una cinta métrica.
Los antiguos griegos y los marineros descubrieron una genialidad:
Si miras la sombra que proyecta la torre en el suelo (que sí la puedes medir caminando con pasos) y mides el ángulo con el que los rayos del sol bajan hacia el suelo... ¡la geometría del triángulo hace el trabajo sucio por ti!
Todos los triángulos rectángulos del mundo que tienen los mismos ángulos guardan exactamente las mismas proporciones entre sus lados, da igual que el triángulo sea del tamaño de una moneda o del tamaño de una montaña.
Las palabras raras (Seno, Coseno y Tangente) son simplemente nombres que les pusieron a esas proporciones fijas:
• <b>Tangente:</b> Compara la altura vertical dividida entre la sombra horizontal del suelo. Si el sol está a 45º, la altura es exactamente igual a la sombra.`,
    stepbystep: `1º Identificamos los tres lados respecto al ángulo que miramos:
• <b>Hipotenusa:</b> El lado más largo (la rampa inclinada por donde baja el rayo de sol).
• <b>Cateto Opuesto:</b> El lado que está enfrente del ángulo (la altura vertical del edificio).
• <b>Cateto Contiguo:</b> El lado pegado al suelo que sujeta el ángulo (la sombra).
2º Regla mnemotécnica infalible (SOH-CAH-TOA):
• Seno = Opuesto / Hipotenusa
• Coseno = Contiguo / Hipotenusa
• Tangente = Opuesto / Contiguo`,
    graphDesc: "<b>El Triángulo del Árbol y la Sombra:</b> Conociendo solo la sombra en el suelo (12 m) y el ángulo solar (30º), la tangente calcula la altura vertical de 6.92 m sin subirte al árbol.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <!-- Suelo -->
        <line x1="50" y1="200" x2="530" y2="200" stroke="#64748b" stroke-width="2"/>
        
        <!-- Sombra en el suelo -->
        <line x1="120" y1="200" x2="420" y2="200" stroke="#0284c7" stroke-width="5"/>
        <text x="230" y="222" font-size="12" font-weight="bold" fill="#0369a1">Sombra = 12 metros</text>
        
        <!-- Altura vertical -->
        <line x1="420" y1="200" x2="420" y2="65" stroke="#16a34a" stroke-width="5"/>
        <text x="430" y="140" font-size="12" font-weight="bold" fill="#15803d">Altura = 6.92 m</text>
        <circle cx="420" cy="60" r="28" fill="#22c55e" opacity="0.85"/>
        
        <!-- Rayo solar (Hipotenusa) -->
        <line x1="120" y1="200" x2="420" y2="65" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6,4"/>
        <circle cx="100" cy="45" r="20" fill="#fbbf24"/>
        
        <!-- Ángulo -->
        <path d="M 170 200 A 50 50 0 0 0 162 180" fill="none" stroke="#dc2626" stroke-width="2.5"/>
        <text x="178" y="192" font-size="12" font-weight="bold" fill="#dc2626">30º</text>
        
        <rect x="220" y="20" width="220" height="38" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
        <text x="230" y="44" font-size="12" font-weight="bold" fill="#1e293b">tg(30º) = Altura / Sombra</text>
      </svg>
    `,
    formal: `<div class="math-formula">tg(α) = Cateto Opuesto / Cateto Contiguo  -->  Altura = Sombra · tg(α)</div>
Ejemplo escolar: La sombra de un árbol mide 12 metros y el ángulo de elevación solar es de 30º:
tg(30º) = Altura / 12  -->  Altura = 12 · tg(30º) = 12 · 0,577 = <b>6,92 metros</b>.`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Estás en la playa y clavas una sombrilla vertical. La sombra en la arena mide 2 metros y el sol incide con un ángulo de 45º. ¿Cuánto mide la sombrilla?<br/>
<i>Pista del abuelo: Como tg(45º) = 1, la altura es exactamente igual a la sombra: ¡2 metros!</i>`
  },

  // --- TEOREMA DE PITÁGORAS ---
  pitagoras: {
    title: "Teorema de Pitágoras: La escuadra del albañil y la pared vertical",
    intuition: `Imagínate una pared vertical recta de 4 metros y el suelo horizontal de tu casa. La esquina entre la pared y el suelo forma un ángulo recto perfecto de 90 grados.
Si apoyas una escalera de 5 metros de largo desde el suelo hasta lo alto de la pared, has formado un triángulo rectángulo.
Los dos lados que forman la esquina se llaman <b>catetos</b> (la pared y el suelo). La escalera inclinada es la <b>hipotenusa</b>.
Pitágoras descubrió una regla geométrica preciosa: si dibujas baldosas cuadradas sobre la pared (4 × 4 = 16 baldosas) y sobre el suelo (3 × 3 = 9 baldosas), y las sumas: 16 + 9 = 25 baldosas... ¡esa suma es EXACTAMENTE igual al cuadrado de baldosas dibujado sobre la escalera inclinada (5 × 5 = 25)!`,
    stepbystep: `1º Identificamos los datos: Hipotenusa (escalera) = 5 m. Cateto vertical (pared) = 4 m. Cateto horizontal (suelo) = c.
2º La fórmula: Hipotenusa² = Cateto₁² + Cateto₂²
3º Sustituimos: 5² = 4² + c²  -->  25 = 16 + c²
4º Despejamos el suelo restando: c² = 25 - 16 = 9
5º Sacamos la raíz cuadrada: c = √9 = 3 metros de distancia.`,
    graphDesc: "<b>Demostración Geométrica de Pitágoras:</b> El cuadrado naranja (3²=9) más el cuadrado verde (4²=16) suman exactamente las 25 baldosas del cuadrado azul de la hipotenusa (5²=25).",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <!-- Triángulo Rectángulo central -->
        <polygon points="190,150 190,80 280,150" fill="#f8fafc" stroke="#0f172a" stroke-width="3"/>
        
        <!-- Cuadrado Cateto Vertical 3x3 -->
        <rect x="120" y="80" width="70" height="70" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
        <text x="138" y="122" font-size="14" font-weight="bold" fill="#c2410c">3² = 9</text>
        
        <!-- Cuadrado Cateto Horizontal 4x4 -->
        <rect x="190" y="150" width="90" height="90" fill="#bbf7d0" stroke="#16a34a" stroke-width="2"/>
        <text x="222" y="202" font-size="15" font-weight="bold" fill="#15803d">4² = 16</text>
        
        <!-- Cuadrado Hipotenusa 5x5 (Rotado) -->
        <g transform="translate(190,80) rotate(37.87)">
          <rect x="0" y="-114" width="114" height="114" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/>
          <text x="35" y="-50" font-size="16" font-weight="bold" fill="#1d4ed8">5² = 25</text>
        </g>
        
        <!-- Cartel -->
        <rect x="350" y="30" width="200" height="58" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="365" y="52" font-size="14" font-weight="bold" fill="#1d4ed8">a² + b² = h²</text>
        <text x="365" y="72" font-size="12" fill="#334155">9 + 16 = 25 baldosas</text>
      </svg>
    `,
    formal: `<div class="math-formula">a² + b² = h²  -->  c = √(h² - b²)</div>
Datos: h = 5 m, b = 4 m
c² = 5² - 4² = 25 - 16 = 9  -->  c = √9 = <b>3 metros</b>.`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Quieres cruzar en diagonal un campo rectangular que mide 6 metros de ancho por 8 metros de largo. ¿Cuántos metros mide esa diagonal recta?<br/>
<i>Pista del abuelo: 6²=36 y 8²=64. Suma 36+64=100. La raíz cuadrada de 100 son exactamente 10 metros.</i>`
  },

  // --- NÚMEROS NEGATIVOS ---
  negativo: {
    title: "Números Negativos y la Regla de los Signos: Por qué 'Menos por Menos es Más'",
    intuition: `La mayor duda que tienen todos los niños en la ESO es: <i>«¿Por qué si multiplico dos números negativos el resultado se vuelve positivo?»</i>. En el colegio se lo hacen aprender como un loro: «menos por menos, más». Pero tiene una lógica visual preciosa:
1º <b>El ascensor y el sótano:</b> Los números positivos son pisos hacia el cielo (+1, +2, +3). Los negativos son los sótanos subterráneos (-1, -2, -3 aparcamiento).
2º <b>Las deudas del banco:</b> Tener +50€ es dinero en tu bolsillo. Tener -50€ es deberle 50€ al banco.
3º <b>La película de cine rebobinada al revés:</b>
Imagínate que ves una película donde un villano entra en una casa y roba un reloj: el villano es un personaje negativo (-).
Ahora imagina que le das al mando a distancia y pones la película en marcha atrás, rebobinando (ir marcha atrás es una acción negativa -).
¿Qué ves en la pantalla al rebobinar? ¡Ves al villano devolviendo el reloj a la mesa y marchándose de la casa! Algo bueno y positivo (+) está ocurriendo en la escena.
En la vida real: si a ti te <b>QUITAN (-)</b> una <b>DEUDA (-)</b>... ¡te están dando dinero (+)!`,
    stepbystep: `• Positivo × Positivo = Positivo (Un amigo que te da caramelos: todo bien).
• Positivo × Negativo = Negativo (Un amigo que te quita caramelos: pierdes).
• Negativo × Positivo = Negativo (Un enemigo que te da una multa: pierdes).
• Negativo × Negativo = Positivo (Un enemigo al que le quitas su arma: ganas tú).`,
    graphDesc: "<b>La Recta Numérica y la Regla de los Signos:</b> El cero es el espejo central. Restar un número negativo (- -) significa anular una marcha atrás y avanzar hacia el lado positivo (+).",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <defs>
          <marker id="arr-num-r" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#10b981"/>
          </marker>
        </defs>
        <rect width="580" height="250" fill="#f8fafc"/>
        
        <!-- Línea Central de la Recta Numérica -->
        <line x1="40" y1="140" x2="540" y2="140" stroke="#334155" stroke-width="3"/>
        <polygon points="545,140 535,135 535,145" fill="#334155"/>
        <polygon points="35,140 45,135 45,145" fill="#334155"/>

        <!-- Marcas: -4 a +4 (Centro en x=290) -->
        <line x1="90" y1="130" x2="90" y2="150" stroke="#ef4444" stroke-width="2"/>
        <text x="82" y="170" font-size="12" font-weight="bold" fill="#ef4444">-4</text>
        <line x1="140" y1="130" x2="140" y2="150" stroke="#ef4444" stroke-width="2"/>
        <text x="132" y="170" font-size="12" font-weight="bold" fill="#ef4444">-3</text>
        <line x1="190" y1="130" x2="190" y2="150" stroke="#ef4444" stroke-width="2"/>
        <text x="182" y="170" font-size="12" font-weight="bold" fill="#ef4444">-2</text>
        <line x1="240" y1="130" x2="240" y2="150" stroke="#ef4444" stroke-width="2"/>
        <text x="232" y="170" font-size="12" font-weight="bold" fill="#ef4444">-1</text>

        <!-- Cero (Origen) -->
        <line x1="290" y1="125" x2="290" y2="155" stroke="#0f172a" stroke-width="3.5"/>
        <circle cx="290" cy="140" r="6" fill="#0f172a"/>
        <text x="285" y="173" font-size="14" font-weight="bold" fill="#0f172a">0</text>

        <!-- Positivos -->
        <line x1="340" y1="130" x2="340" y2="150" stroke="#10b981" stroke-width="2"/>
        <text x="332" y="170" font-size="12" font-weight="bold" fill="#10b981">+1</text>
        <line x1="390" y1="130" x2="390" y2="150" stroke="#10b981" stroke-width="2"/>
        <text x="382" y="170" font-size="12" font-weight="bold" fill="#10b981">+2</text>
        <line x1="440" y1="130" x2="440" y2="150" stroke="#10b981" stroke-width="2"/>
        <text x="432" y="170" font-size="12" font-weight="bold" fill="#10b981">+3</text>
        <line x1="490" y1="130" x2="490" y2="150" stroke="#10b981" stroke-width="2"/>
        <text x="482" y="170" font-size="12" font-weight="bold" fill="#10b981">+4</text>

        <!-- Salto de (-) x (-) = (+) -->
        <path d="M 140 120 Q 215 50 290 120" fill="none" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="4,2"/>
        <path d="M 290 120 Q 390 40 440 120" fill="none" stroke="#10b981" stroke-width="3" marker-end="url(#arr-num-r)"/>
        <text x="270" y="55" font-size="12" font-weight="bold" fill="#10b981">Quitar una deuda: - (-3) = +3 ➔ Avanzas a la derecha (+)</text>

        <!-- Carteles -->
        <rect x="50" y="25" width="170" height="46" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="60" y="43" font-size="11.5" font-weight="bold" fill="#b91c1c">❄️ Deuda / Bajo cero (-)</text>
        <text x="60" y="58" font-size="10.5" fill="#475569">Moverse a la izquierda</text>
      </svg>
    `,
    formal: `<div class="math-formula">Regla de los signos: (+)·(+)=(+) | (+)·(-)=(-) | (-)·(+)=(-) | (-)·(-)=(+)</div>
Ejemplos de examen:
• (-3) · (+4) = -12
• (-5) · (-6) = <b>+30</b>
• Operación combinada: 10 - (-8) = 10 + 8 = 18  (restar un negativo equivale a sumar).`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Calcula el resultado de la siguiente operación paso a paso: (-2) · (-4) - (-5) + (-6) = ?<br/>
<i>Pista del abuelo: Primero multiplica (-2)·(-4)=+8. Luego -(-5) se convierte en +5. Finalmente suma 8 + 5 - 6 = 7.</i>`
  },

  // --- SISTEMAS DE ECUACIONES ---
  sistema: {
    title: "Sistemas de Ecuaciones: El tablero de detectives con dos pistas cruzadas",
    intuition: `Imagínate que vas a la frutería con tu nieto.
El lunes compras 2 kilos de manzanas y 1 kilo de peras y el frutero te cobra 5 euros.
Con esa sola pista no puedes saber cuánto cuesta el kilo de manzanas: podrían costar 2€ las manzanas y 1€ las peras, o 1€ las manzanas y 3€ las peras... Hay infinitas combinaciones posibles.
Pero el martes vuelves y compras 1 kilo de manzanas y 3 kilos de peras y te cobra 10 euros.
¡Ahora tienes dos pistas del mismo misterio! Al cruzarlas en el tablero de investigación, solo existe un único precio en todo el universo para las manzanas y para las peras que cuadre con las dos compras a la vez.`,
    stepbystep: `El método de Sustitución (el más intuitivo):
1º Despejamos una fruta en la primera pista: si 2M + 1P = 5, entonces 1 kilo de peras vale (5 - 2M).
2º Nos vamos a la segunda pista y donde ponía 'P' ponemos su disfraz (5 - 2M).
3º Ahora la segunda ecuación ya solo tiene manzanas: calculamos el precio de la manzana.
4º Con el precio de la manzana en la mano, descubrimos al segundo el precio de la pera.`,
    graphDesc: "<b>Intersección de Rectas (Solución Gráfica):</b> Cada ecuación es una línea recta en el mapa cartesiano. El punto donde ambas se cortan (x=1, y=3) es la única solución que satisface ambas pistas a la vez.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <rect width="580" height="250" fill="#f8fafc"/>
        
        <!-- Ejes -->
        <line x1="60" y1="210" x2="520" y2="210" stroke="#334155" stroke-width="2"/>
        <line x1="120" y1="225" x2="120" y2="25" stroke="#334155" stroke-width="2"/>
        <text x="490" y="200" font-size="12" font-weight="bold" fill="#334155">X (Manzanas)</text>
        <text x="130" y="40" font-size="12" font-weight="bold" fill="#334155">Y (Peras)</text>

        <!-- Recta 1: 2x + y = 5 (Azul) -->
        <line x1="100" y1="35" x2="330" y2="218" stroke="#2563eb" stroke-width="3.5"/>
        <text x="320" y="235" font-size="11" font-weight="bold" fill="#2563eb">Recta 1: 2x + y = 5</text>

        <!-- Recta 2: x + 3y = 10 (Roja) -->
        <line x1="80" y1="80" x2="480" y2="180" stroke="#dc2626" stroke-width="3.5"/>
        <text x="440" y="170" font-size="11" font-weight="bold" fill="#dc2626">Recta 2: x + 3y = 10</text>

        <!-- Líneas guía al punto de cruce (1, 3) -->
        <line x1="120" y1="110" x2="200" y2="110" stroke="#94a3b8" stroke-dasharray="3,3"/>
        <line x1="200" y1="110" x2="200" y2="210" stroke="#94a3b8" stroke-dasharray="3,3"/>
        <text x="95" y="114" font-size="11" font-weight="bold" fill="#047857">y = 3</text>
        <text x="195" y="226" font-size="11" font-weight="bold" fill="#047857">x = 1</text>

        <!-- Punto solución (1, 3) -->
        <circle cx="200" cy="110" r="7.5" fill="#f59e0b" stroke="#ffffff" stroke-width="2.5"/>
        <text x="215" y="105" font-size="13" font-weight="bold" fill="#b45309">⭐ Solución Única: (1, 3)</text>
        <text x="215" y="122" font-size="11" fill="#334155">1 € Manzanas / 3 € Peras</text>
      </svg>
    `,
    formal: `<div class="math-formula">Sistema: { 2x + y = 5 (1) | x + 3y = 10 (2) }</div>
Despejamos y en (1): y = 5 - 2x
Sustituimos en (2): x + 3(5 - 2x) = 10  -->  x + 15 - 6x = 10
-5x = 10 - 15  -->  -5x = -5  -->  <b>x = 1 € (Manzanas)</b>
Sustituimos para hallar y: y = 5 - 2(1) = <b>3 € (Peras)</b>.`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Resuelve por sustitución: { x + y = 9 ; x - y = 3 }.<br/>
<i>Pista del abuelo: Despeja x = 9 - y. Los dos números que sumados dan 9 y restados dan 3 son x = 6 e y = 3.</i>`
  },

  // --- FRACCIONES ---
  fracciones: {
    title: "Suma de Fracciones: El dilema de cortar las tartas en trozos iguales",
    intuition: `Imagínate que tienes una tarta de manzana cortada en 3 pedazos enormes (cada trozo es 1/3) y al lado tienes una tarta de chocolate cortada en 5 pedazos medianos (cada trozo es 1/5).
Si tu nieto coge 2 trozos de manzana y 3 de chocolate y dice: <i>«¡Abuelo, tengo 5 trozos de tarta!»</i>, tiene razón en número de piezas, pero es una trampa: ¡los trozos son de tamaños completamente distintos! Sería como sumar monedas de 2 euros con monedas de 10 céntimos diciendo que tienes dos monedas.
Para poder sumarlas de verdad, tenemos que cortar las dos tartas en porciones que sean exactamente del mismo tamaño.
Buscamos un número que sirva para las dos familias: 3 × 5 = 15 trozos.
Ahora que las dos tartas tienen rebanadas de 1/15, ya podemos sumarlas limpiamente.`,
    stepbystep: `1º Buscamos el Mínimo Común Múltiplo (m.c.m.) entre los denominadores (3 y 5) = 15.
2º Convertimos la primera fracción (2/3): dividimos 15 / 3 = 5, y multiplicamos arriba: 2 × 5 = 10. Queda 10/15.
3º Convertimos la segunda fracción (3/5): dividimos 15 / 5 = 3, y multiplicamos arriba: 3 × 3 = 9. Queda 9/15.
4º Ahora que tienen el mismo tamaño, sumamos los trozos: 10/15 + 9/15 = 19/15.`,
    graphDesc: "<b>Visualización de la Suma de Fracciones:</b> Al principio los trozos tienen tamaños incompatibles (tercios y quintos). Al cortarlos en trozos comunes de 1/15, sumamos 10 trozos + 9 trozos = 19/15.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <rect width="580" height="250" fill="#f8fafc"/>
        
        <!-- Barra Fracción 1: 2/3 (Largo 180) -->
        <text x="50" y="40" font-size="12" font-weight="bold" fill="#2563eb">Fracción 1: 2/3 (10/15)</text>
        <rect x="50" y="48" width="180" height="32" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
        <rect x="50" y="48" width="120" height="32" rx="4" fill="#3b82f6"/>
        <line x1="110" y1="48" x2="110" y2="80" stroke="#ffffff" stroke-width="2"/>
        <line x1="170" y1="48" x2="170" y2="80" stroke="#ffffff" stroke-width="2"/>
        <text x="75" y="70" font-size="11" font-weight="bold" fill="#ffffff">1/3</text>
        <text x="135" y="70" font-size="11" font-weight="bold" fill="#ffffff">1/3</text>
        <text x="195" y="70" font-size="10" fill="#64748b">1/3</text>

        <!-- Barra Fracción 2: 3/5 (Largo 180) -->
        <text x="310" y="40" font-size="12" font-weight="bold" fill="#ea580c">Fracción 2: 3/5 (9/15)</text>
        <rect x="310" y="48" width="180" height="32" rx="4" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
        <rect x="310" y="48" width="108" height="32" rx="4" fill="#f97316"/>
        <line x1="346" y1="48" x2="346" y2="80" stroke="#ffffff" stroke-width="1.5"/>
        <line x1="382" y1="48" x2="382" y2="80" stroke="#ffffff" stroke-width="1.5"/>
        <line x1="418" y1="48" x2="418" y2="80" stroke="#ffffff" stroke-width="1.5"/>
        <line x1="454" y1="48" x2="454" y2="80" stroke="#ffffff" stroke-width="1.5"/>
        <text x="345" y="70" font-size="11" font-weight="bold" fill="#ffffff">3/5 pintados</text>

        <!-- Signo más (+) -->
        <text x="260" y="70" font-size="22" font-weight="bold" fill="#0f172a">+</text>

        <!-- Barra Resultado Común: 19/15 -->
        <text x="50" y="130" font-size="12" font-weight="bold" fill="#047857">Tarta subdividida en partes comunes (m.c.m = 15):</text>
        <rect x="50" y="145" width="300" height="36" rx="4" fill="#10b981" stroke="#047857" stroke-width="2"/>
        <text x="160" y="168" font-size="12" font-weight="bold" fill="#ffffff">15/15 (1 Tarta Entera)</text>

        <rect x="365" y="145" width="80" height="36" rx="4" fill="#10b981" stroke="#047857" stroke-width="2"/>
        <rect x="445" y="145" width="60" height="36" rx="4" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>
        <text x="380" y="168" font-size="12" font-weight="bold" fill="#ffffff">4/15</text>

        <!-- Resultado final -->
        <text x="160" y="215" font-size="13" font-weight="bold" fill="#047857">Total = 10/15 + 9/15 = 19/15 (1 entero y 4/15)</text>
      </svg>
    `,
    formal: `<div class="math-formula">Operación: 2/3 + 3/5  -->  m.c.m.(3, 5) = 15</div>
2/3 = (2·5)/(3·5) = 10/15
3/5 = (3·3)/(5·3) = 9/15
10/15 + 9/15 = (10 + 9) / 15 = <b>19/15</b> (Fracción irreducible = 1 entero y 4/15).`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Calcula en tu cuaderno la siguiente suma de fracciones: 3/4 + 2/5 = ?<br/>
<i>Pista del abuelo: El denominador común entre 4 y 5 es 20. El resultado final es 23/20.</i>`
  },

  // --- PORCENTAJES ---
  porcentajes: {
    title: "Porcentajes y Rebajas: El truco mental infalible del 10%",
    intuition: `La palabra 'Por Ciento' significa literalmente 'Por Cada Cien'.
Si en una tienda ves un cartel de <i>«30% de descuento»</i>, significa que por cada billete de 100 euros que costara la prenda, la tienda te regala 30 euros y tú pagas 70.
Pero casi nada cuesta 100 euros clavados. Imagínate que unas zapatillas valen 80 euros.
Hay un truco mental de los abuelos que nunca falla y que no necesita calculadora:
<b>Calcula siempre primero el 10%</b> (que es simplemente quitar un cero o mover la coma a la izquierda).
El 10% de 80 euros son <b>8 euros</b>.
Si el 10% son 8 euros...
• ¡El 20% es el doble: 8 × 2 = 16 euros de rebaja!
• ¡El 30% es el triple: 8 × 3 = 24 euros de rebaja!
• ¡El 5% es la mitad de 8: 4 euros!`,
    stepbystep: `1º Descuento en euros: 80 × 30 / 100 = 24 euros de ahorro.
2º Precio final a pagar: 80 - 24 = 56 euros.
3º El método exprés del comercio (Factor multiplicador): Si te descuentan el 30%, tú pagas el 70% restante: 80 × 0,70 = 56 euros en un solo paso.`,
    graphDesc: "<b>El Truco Mental del 10%:</b> Toda la barra mide 80 € (100%). Cada pastilla del 10% vale 8 €. Para un 30% de rebaja, quitamos 3 pastillas (24 € de descuento) y quedan 7 pastillas para pagar (56 € en caja).",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <rect width="580" height="250" fill="#f8fafc"/>
        
        <!-- Título -->
        <text x="50" y="42" font-size="12" font-weight="bold" fill="#0f172a">Barra de Precio: 80 € (100% Original)</text>

        <!-- 3 pastillas descontadas (Rojo) -->
        <rect x="50" y="55" width="132" height="48" fill="#fca5a5" stroke="#dc2626" stroke-width="2"/>
        <line x1="94" y1="55" x2="94" y2="103" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,3"/>
        <line x1="138" y1="55" x2="138" y2="103" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,3"/>
        <text x="65" y="83" font-size="11" font-weight="bold" fill="#991b1b">-30% Descuento</text>
        <text x="95" y="98" font-size="10" fill="#991b1b">24 €</text>

        <!-- 7 pastillas a pagar (Verde) -->
        <rect x="182" y="55" width="308" height="48" fill="#86efac" stroke="#16a34a" stroke-width="2"/>
        <line x1="226" y1="55" x2="226" y2="103" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3,3"/>
        <line x1="270" y1="55" x2="270" y2="103" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3,3"/>
        <line x1="314" y1="55" x2="314" y2="103" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3,3"/>
        <line x1="358" y1="55" x2="358" y2="103" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3,3"/>
        <line x1="402" y1="55" x2="402" y2="103" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3,3"/>
        <line x1="446" y1="55" x2="446" y2="103" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3,3"/>
        <text x="250" y="83" font-size="12" font-weight="bold" fill="#14532d">70% Precio Final que pagas en caja</text>
        <text x="330" y="98" font-size="11" font-weight="bold" fill="#14532d">56 €</text>

        <!-- Clave del 10% -->
        <rect x="50" y="130" width="440" height="60" rx="8" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.2"/>
        <text x="65" y="152" font-size="11.5" font-weight="bold" fill="#1e40af">⚡ El Secreto del 10% (Quitar un cero):</text>
        <text x="65" y="170" font-size="10.5" fill="#334155">• 10% de 80 € = 8 € (1 pastilla)</text>
        <text x="65" y="185" font-size="10.5" fill="#334155">• 30% = 3 × 8 € = 24 € de ahorro  ➔  Pagas: 80 - 24 = <b>56 €</b></text>
      </svg>
    `,
    formal: `<div class="math-formula">Precio Final = Precio Original · (1 - %/100)</div>
Precio original: 80 € | Descuento: 30%
Descuento = (80 · 30) / 100 = <b>24 €</b>
Precio final = 80 - 24 = <b>56 €</b>`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Una chaqueta de montaña cuesta 60 euros y tiene un descuento del 20%. ¿Cuánto dinero te descuentan y cuánto pagas en caja?<br/>
<i>Pista del abuelo: El 10% de 60 son 6 euros... así que el 20% son 12 euros. Pagas 48 euros.</i>`
  },

  // --- TEOREMA / PRINCIPIO DE ARQUÍMEDES Y FLOTABILIDAD ---
  arquimedes: {
    title: "Principio de Arquímedes: El empuje de los fluidos, la corona de oro y el grito de ¡Eureka!",
    intuition: `Dile a tu nieto: <i>«¿Alguna vez has intentado hundir una pelota de playa hinchada o un balón debajo del agua en la piscina?
Tienes que empujar con todas tus fuerzas con las dos manos porque sientes una mano invisible gigante que te la devuelve disparada hacia arriba.
O cuando juegas en el agua a coger a tu hermano o a tu abuelo en brazos: ¡fuera del agua no puedes ni levantarlo, pero dentro del agua parece que no pesa nada!
Esa fuerza hacia arriba que hace el agua se llama <b>EMPUJE</b>.
¿Y sabes cómo se descubrió? Hace más de 2.200 años en Siracusa (Grecia).
El rey Hierón II le dio una barra de oro puro a un joyero para que le hiciera una corona para los dioses. Pero el rey desconfiaba: sospechaba que el joyero se había quedado con parte del oro y había rellenado la corona con plata barata. El rey le dijo al sabio Arquímedes: <i>'Descubre si me ha engañado, pero sin romper ni fundir la corona'</i>.
Arquímedes se estaba devanando los sesos. Un día, se metió en una bañera que estaba llena de agua hasta el borde y vio cómo el agua se desbordaba por el suelo al meterse su cuerpo.
En una fracción de segundo lo comprendió todo: <b>el volumen de agua que se desborda es exactamente igual al volumen del cuerpo que se sumerge</b>.
Como el oro es mucho más denso y pesado que la plata, una corona de oro puro ocupa muy poco espacio; pero si tenía plata de relleno, la corona sería más gorda para el mismo peso y desalojaría mucha más agua.
Arquímedes se puso tan eufórico que salió de la bañera y corrió desnudo por las calles gritando: <b>«¡EUREKA! ¡EUREKA!»</b> (que en griego significa <i>'¡Lo he encontrado!'</i>).
¿Y por qué un tornillito de hierro de 10 gramos se hunde como una piedra, pero un barco petrolero de 100.000 toneladas de acero flota en el océano?
Porque el barco tiene un casco gigante hueco lleno de aire: desaloja miles de toneladas de agua, y el empuje de toda esa agua desalojada hacia arriba es mucho mayor que el peso del acero del barco.»</i>`,
    stepbystep: `1º <b>Las dos fuerzas enfrentadas en cualquier cuerpo bajo el agua:</b>
• <b>El Peso (P = m · g):</b> La gravedad de la Tierra tira del objeto hacia abajo (hacia el fondo).
• <b>El Empuje de Arquímedes (E):</b> El fluido empuja el objeto hacia arriba con una fuerza exactamente igual al peso del agua desalojada: E = ρ_líquido · V_sumergido · g.
2º <b>Las tres situaciones de flotabilidad:</b>
• <b>Si el Peso es mayor que el Empuje (P > E):</b> El cuerpo es más denso que el agua (ρ_cuerpo > ρ_agua) y <b>se hunde</b> hasta el fondo (como una moneda de euro o una piedra).
• <b>Si el Peso es igual al Empuje sumergido (P = E):</b> El cuerpo se queda en <b>equilibrio entre dos aguas</b>, suspendido a media profundidad (como un pez con su vejiga natatoria o un submarino).
• <b>Si el Empuje supera al Peso (E > P):</b> El cuerpo <b>sube a la superficie y flota</b> (como un corcho o un iceberg), sacando parte de su cuerpo fuera del agua hasta que el empuje de la parte sumergida iguala su peso total.
3º <b>El Peso Aparente:</b> En el agua todo pesa menos porque el empuje nos ayuda:
P_aparente = P_real - Empuje.`,
    graphDesc: "<b>Esquema del Principio de Arquímedes y ¡Eureka!:</b> El objeto sumergido desaloja un volumen de agua idéntico hacia el vaso medidor. El líquido reacciona con una fuerza vertical de Empuje (E, flecha verde hacia arriba) que se opone al Peso gravitatorio (P, flecha roja hacia abajo).",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <defs>
          <linearGradient id="waterGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#0284c7" stop-opacity="0.75"/>
          </linearGradient>
          <marker id="arrow-up" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 10 L 5 0 L 10 10 z" fill="#10b981"/>
          </marker>
          <marker id="arrow-down" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 0 L 5 10 z" fill="#ef4444"/>
          </marker>
        </defs>

        <!-- Fondo sutil de laboratorio -->
        <rect width="580" height="250" fill="#f8fafc"/>
        <line x1="30" y1="225" x2="550" y2="225" stroke="#64748b" stroke-width="2.5"/>

        <!-- Recipiente Principal con caño de desborde -->
        <path d="M 80 60 L 80 220 L 250 220 L 250 100 L 300 130 L 300 138 L 250 115 L 250 220" fill="none" stroke="#334155" stroke-width="3"/>
        
        <!-- Agua en el recipiente principal -->
        <path d="M 83 100 L 247 100 L 247 217 L 83 217 Z" fill="url(#waterGrad)"/>
        
        <!-- Chorro de agua que desborda -->
        <path d="M 248 102 Q 275 115 295 136 Q 315 160 325 190" fill="none" stroke="#0284c7" stroke-width="3.5" stroke-dasharray="4,2"/>

        <!-- Vaso medidor lateral (Agua desalojada) -->
        <path d="M 310 160 L 310 220 L 370 220 L 370 160" fill="none" stroke="#334155" stroke-width="2.5"/>
        <rect x="312" y="185" width="56" height="33" fill="url(#waterGrad)"/>
        <line x1="320" y1="195" x2="330" y2="195" stroke="#0284c7" stroke-width="1.5"/>
        <line x1="320" y1="205" x2="330" y2="205" stroke="#0284c7" stroke-width="1.5"/>
        <text x="315" y="152" font-size="11" font-weight="bold" fill="#0284c7">Agua desalojada</text>
        <text x="320" y="238" font-size="10" fill="#475569">V_desalojado</text>

        <!-- Bloque sumergido en el agua -->
        <rect x="135" y="125" width="60" height="60" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="2"/>
        <text x="145" y="158" font-size="11" font-weight="bold" fill="#ffffff">Cuerpo (V)</text>

        <!-- Vector Peso (P = m·g) hacia abajo -->
        <line x1="165" y1="155" x2="165" y2="215" stroke="#ef4444" stroke-width="3" marker-end="url(#arrow-down)"/>
        <text x="172" y="210" font-size="11" font-weight="bold" fill="#dc2626">Peso (P = m·g)</text>

        <!-- Vector Empuje (E) hacia arriba -->
        <line x1="165" y1="155" x2="165" y2="80" stroke="#10b981" stroke-width="3.5" marker-end="url(#arrow-up)"/>
        <text x="172" y="78" font-size="11" font-weight="bold" fill="#059669">Empuje (E = ρ·V·g)</text>

        <!-- Cartel explicativo de Arquímedes -->
        <rect x="390" y="45" width="175" height="110" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
        <text x="402" y="68" font-size="12" font-weight="bold" fill="#0369a1">👑 ¡EUREKA!</text>
        <text x="402" y="88" font-size="10.5" fill="#334155">• V_sumergido = V_agua</text>
        <text x="402" y="106" font-size="10.5" fill="#059669"><b>• Empuje E = ρ_f · V · g</b></text>
        <text x="402" y="124" font-size="10.5" fill="#dc2626"><b>• P_aparente = P - E</b></text>
        <text x="402" y="142" font-size="10" fill="#64748b">Si E > P ➔ ¡Flota!</text>
      </svg>
    `,
    formal: `<div class="math-formula">Ecuación Fundamental del Empuje: E = ρ_f · V_s · g</div>
<b>Donde:</b>
• E = Empuje hidrostático en Newtons (N)
• ρ_f = Densidad del fluido (Agua dulce = 1.000 kg/m³, Agua de mar ≈ 1.030 kg/m³)
• V_s = Volumen de la parte sumergida en metros cúbicos (m³)
• g = Aceleración de la gravedad (9,8 m/s²)
<br/><br/>
<b>Problema Clásico de Examen (Física y Química 3º/4º ESO y Bachillerato):</b>
Un cuerpo metálico tiene un volumen de 0,002 m³ (2 litros) y una masa de 5 kg. Se sumerge completamente en agua dulce.
1º <b>Peso real fuera del agua:</b>
P = m · g = 5 kg · 9,8 m/s² = <b>49 N</b>.
2º <b>Empuje del agua:</b>
E = ρ_agua · V_sumergido · g = 1000 kg/m³ · 0,002 m³ · 9,8 m/s² = <b>19,6 N</b>.
3º <b>Peso aparente dentro del agua:</b>
P_aparente = P_real - E = 49 N - 19,6 N = <b>29,4 N</b> (dentro del agua parece que pesa solo 3 kg).
4º <b>¿Se hunde o flota?</b>
Como el Peso (49 N) es mayor que el Empuje (19,6 N), la fuerza neta es hacia abajo: <b>el cuerpo se hunde hasta el fondo</b>.`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Una talla de madera decorativa tiene un volumen de 0,005 m³ y una masa de 3 kg. La tiramos a una piscina de agua dulce (densidad = 1.000 kg/m³, g = 9,8 m/s²).<br/>
a) ¿Cuánto vale su peso real?<br/>
b) ¿Cuánto valdría el empuje máximo si estuviera totalmente bajo el agua?<br/>
c) ¿Se hundirá hasta el fondo o flotará en la superficie?<br/>
<i>Pista del abuelo: Peso = 3 · 9,8 = 29,4 N. Empuje máximo sumergido = 1000 · 0,005 · 9,8 = 49 N. Como el Empuje (49 N) es mucho mayor que el Peso (29,4 N), ¡la madera sube como un tapón de corcho y flota plácidamente!</i>`
  },

  // --- PRINCIPIO DE PASCAL Y PRENSA HIDRÁULICA ---
  pascal: {
    title: "Principio de Pascal y Prensa Hidráulica: Levantar un camión con la fuerza de un dedo",
    intuition: `Dile a tu nieto: <i>«Imagínate un tubo de pasta de dientes o una jeringuilla con agua.
Si aprietas con tu dedo en la base del tubo, ¿se queda la fuerza donde pusiste el dedo? ¡Para nada! La presión viaja a toda velocidad por el líquido y sale disparada por el tapón.
El científico francés Blaise Pascal descubrió una propiedad asombrosa: <b>los líquidos no se pueden aplastar</b> (son incompresibles).
Si empujas el agua en un tubo estrecho, esa presión se transmite con la mismísima fuerza por centímetro cuadrado a todos los rincones del recipiente.
¿Y qué pasa si al otro lado del tubo pones una plataforma 50 veces más ancha?
Que cada centímetro cuadrado de esa plataforma recibe la misma presión... ¡así que tu fuerza se multiplica por 50!
Con la fuerza de un solo dedo en un pedal de freno, eres capaz de frenar en seco un coche de dos toneladas lanzado a 120 km/h por la autopista. ¡La hidráulica es el músculo invisible de la civilización!»</i>`,
    stepbystep: `1º <b>La Presión es la misma en todas partes:</b> P₁ = P₂.
2º Como Presión = Fuerza / Superficie (P = F / S), tenemos:
<b>F₁ / S₁ = F₂ / S₂</b>.
3º <b>El Multiplicador de Fuerza:</b>
Si la superficie grande (S₂) es 100 veces mayor que la pequeña (S₁), la fuerza de salida (F₂) será 100 veces mayor que la que hiciste con tu mano: F₂ = F₁ · (S₂ / S₁).
4º <b>La ley de la conservación:</b> La física nunca regala nada gratis: ganas fuerza a cambio de tener que empujar el émbolo pequeño una distancia mucho más larga.`,
    graphDesc: "<b>Prensa Hidráulica de Pascal:</b> Al aplicar una fuerza pequeña F₁ sobre el émbolo estrecho S₁, la presión hidráulica se transmite íntegra y genera una fuerza gigante F₂ sobre el émbolo ancho S₂, levantando el coche.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <defs>
          <linearGradient id="oilGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#38bdf8"/>
            <stop offset="100%" stop-color="#0284c7"/>
          </linearGradient>
          <marker id="arrow-down-p" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 0 L 5 10 z" fill="#ef4444"/>
          </marker>
          <marker id="arrow-up-p" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 10 L 5 0 L 10 10 z" fill="#10b981"/>
          </marker>
        </defs>
        <rect width="580" height="250" fill="#f8fafc"/>
        
        <!-- Tubo en U comunicado -->
        <path d="M 80 90 L 80 210 L 460 210 L 460 120 L 320 120 L 320 180 L 140 180 L 140 90" fill="none" stroke="#334155" stroke-width="4"/>
        
        <!-- Líquido hidráulico azul -->
        <path d="M 82 120 L 138 120 L 138 182 L 322 182 L 322 122 L 458 122 L 458 208 L 82 208 Z" fill="url(#oilGrad)"/>
        
        <!-- Émbolo Pequeño S1 -->
        <rect x="82" y="110" width="56" height="15" fill="#475569" stroke="#1e293b" stroke-width="1.5"/>
        <line x1="110" y1="40" x2="110" y2="105" stroke="#ef4444" stroke-width="3" marker-end="url(#arrow-down-p)"/>
        <text x="118" y="55" font-size="12" font-weight="bold" fill="#ef4444">F₁ (Fuerza pequeña)</text>
        <text x="95" y="142" font-size="11" font-weight="bold" fill="#ffffff">S₁</text>
        
        <!-- Émbolo Grande S2 -->
        <rect x="322" y="112" width="136" height="16" fill="#475569" stroke="#1e293b" stroke-width="1.5"/>
        <line x1="390" y1="108" x2="390" y2="40" stroke="#10b981" stroke-width="4" marker-end="url(#arrow-up-p)"/>
        <text x="405" y="55" font-size="12" font-weight="bold" fill="#059669">F₂ (Fuerza multiplicada)</text>
        <text x="380" y="145" font-size="11" font-weight="bold" fill="#ffffff">S₂ (Área grande)</text>

        <!-- Silueta del Coche encima del émbolo grande -->
        <rect x="340" y="70" width="100" height="28" rx="6" fill="#dc2626"/>
        <polygon points="355,70 370,52 410,52 425,70" fill="#b91c1c"/>
        <circle cx="360" cy="98" r="8" fill="#1e293b"/>
        <circle cx="420" cy="98" r="8" fill="#1e293b"/>
        <text x="365" y="86" font-size="10" font-weight="bold" fill="#ffffff">🚗 1.600 kg</text>
        
        <!-- Ecuación de Pascal -->
        <rect x="155" y="25" width="150" height="42" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
        <text x="170" y="42" font-size="12" font-weight="bold" fill="#0f172a">P₁ = P₂</text>
        <text x="170" y="58" font-size="11" fill="#0369a1">F₁ / S₁ = F₂ / S₂</text>
      </svg>
    `,
    formal: `<div class="math-formula">Ecuación de la Prensa Hidráulica: F₁ / S₁ = F₂ / S₂  ⟹  F₂ = F₁ · (S₂ / S₁)</div>
<b>Ejercicio Resuelto de Examen:</b>
En un taller mecánico disponen de un elevador hidráulico con un pistón pequeño de sección S₁ = 20 cm² y un pistón grande de sección S₂ = 800 cm².
Queremos elevar un coche cuya masa es de 1.600 kg.
1º <b>Peso del coche a levantar (F₂):</b>
F₂ = m · g = 1600 kg · 9,8 m/s² = <b>15.680 N</b>.
2º <b>Relación de superficies (multiplicador):</b>
S₂ / S₁ = 800 cm² / 20 cm² = <b>40 veces mayor</b>.
3º <b>Fuerza necesaria en el émbolo pequeño (F₁):</b>
F₁ = F₂ · (S₁ / S₂) = 15.680 N / 40 = <b>392 N</b> (equivalente a levantar apenas 40 kg).
<i>¡Con la fuerza de un niño hemos levantado un todoterreno entero!</i>`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
En una prensa hidráulica de laboratorio, el émbolo pequeño mide 5 cm² y el grande 250 cm². Si aplicamos una fuerza de 100 N sobre el pequeño, ¿cuánta fuerza se genera en el émbolo grande?<br/>
<i>Pista del abuelo: Como la superficie grande es 50 veces mayor (250 / 5 = 50), la fuerza se multiplica por 50: 100 × 50 = 5.000 N.</i>`
  },

  // --- LEYES DE NEWTON Y DINÁMICA ---
  newton: {
    title: "Las Leyes de Newton y Dinámica: Los tres mandamientos del movimiento universal",
    intuition: `Dile a tu nieto: <i>«Isaac Newton descubrió en 1687 cómo se mueve todo en el universo, desde una canica hasta los planetas:
1. <b>1ª Ley (La Inercia o 'la ley del vago'):</b> Todo cuerpo quieto quiere seguir quieto, y todo cuerpo en movimiento rectilíneo quiere seguir en movimiento para siempre, a no ser que una fuerza lo obligue a frenar. Por eso cuando el metro o el autobús da un frenazo, sales despedido hacia adelante: ¡tu cuerpo quiere seguir viajando a 50 km/h!
2. <b>2ª Ley (F = m · a):</b> La fuerza es igual a la masa multiplicada por la aceleración. Si empujas un carrito del supermercado vacío, acelera como un bólido con un empujón suave; pero si está lleno de sacos de patatas (mucha masa), tienes que dejarte la piel empujando para que coja la misma aceleración.
3. <b>3ª Ley (Acción y Reacción):</b> Si tú empujas a una pared, la pared te empuja exactamente a ti con la misma fuerza en sentido contrario. ¿Por qué despega un cohete al espacio? Porque expulsa gases ardiendo hacia el suelo con furia (acción), y esos gases empujan al cohete hacia las estrellas (reacción). O cuando saltas de una canoa a la orilla: tú vas adelante pero la barca sale disparada hacia atrás en el agua.»</i>`,
    stepbystep: `1º <b>El Diagrama de Cuerpo Libre (DCL):</b> En cualquier problema de física, aislamos el objeto y dibujamos todas las flechas de fuerza que actúan sobre él:
• <b>Peso (P = m·g):</b> Siempre vertical hacia abajo (hacia el centro de la Tierra).
• <b>Normal (N):</b> La fuerza perpendicular que hace el suelo para sostener el objeto y que no se hunda.
• <b>Fuerza aplicada (F):</b> El tirón o empuje del motor o la persona.
• <b>Fuerza de rozamiento (Fr = μ · N):</b> La fricción rugosa del suelo que siempre se opone al avance.
2º <b>Ecuación fundamental de la Dinámica:</b> Sumatorio de Fuerzas = m · a
Fuerza neta (F - Fr) = masa · aceleración.`,
    graphDesc: "<b>Diagrama de Fuerzas de Newton (DCL):</b> Las 4 fuerzas que gobiernan el movimiento sobre un plano: el Peso (P) equilibrado por la Normal (N), y la Fuerza motriz (F) venciendo al rozamiento (Fr) para acelerar la masa m.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <defs>
          <marker id="arr-newt-r" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb"/>
          </marker>
          <marker id="arr-newt-l" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 10 0 L 0 5 L 10 10 z" fill="#ea580c"/>
          </marker>
          <marker id="arr-newt-u" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 10 L 5 0 L 10 10 z" fill="#10b981"/>
          </marker>
          <marker id="arr-newt-d" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 0 L 5 10 z" fill="#ef4444"/>
          </marker>
        </defs>
        <rect width="580" height="250" fill="#f8fafc"/>
        
        <!-- Suelo con rugosidad -->
        <line x1="40" y1="180" x2="540" y2="180" stroke="#334155" stroke-width="3"/>
        <path d="M 50 185 L 45 195 M 80 185 L 75 195 M 110 185 L 105 195 M 140 185 L 135 195 M 170 185 L 165 195 M 200 185 L 195 195 M 230 185 L 225 195 M 260 185 L 255 195 M 290 185 L 285 195 M 320 185 L 315 195 M 350 185 L 345 195 M 380 185 L 375 195 M 410 185 L 405 195 M 440 185 L 435 195 M 470 185 L 465 195 M 500 185 L 495 195" stroke="#94a3b8" stroke-width="1.5"/>

        <!-- Bloque de masa m -->
        <rect x="230" y="110" width="90" height="70" rx="4" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
        <text x="260" y="150" font-size="14" font-weight="bold" fill="#0f172a">m = 10 kg</text>

        <!-- Vector Normal (N) hacia arriba -->
        <line x1="275" y1="110" x2="275" y2="35" stroke="#10b981" stroke-width="3" marker-end="url(#arr-newt-u)"/>
        <text x="285" y="45" font-size="11" font-weight="bold" fill="#059669">Normal (N)</text>

        <!-- Vector Peso (P = mg) hacia abajo -->
        <line x1="275" y1="180" x2="275" y2="245" stroke="#ef4444" stroke-width="3" marker-end="url(#arr-newt-d)"/>
        <text x="285" y="235" font-size="11" font-weight="bold" fill="#dc2626">Peso (P = m·g)</text>

        <!-- Vector Fuerza (F) hacia la derecha -->
        <line x1="320" y1="145" x2="430" y2="145" stroke="#2563eb" stroke-width="3.5" marker-end="url(#arr-newt-r)"/>
        <text x="350" y="135" font-size="12" font-weight="bold" fill="#2563eb">F (Tracción = 50 N)</text>

        <!-- Vector Rozamiento (Fr) hacia la izquierda -->
        <line x1="230" y1="178" x2="140" y2="178" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arr-newt-l)"/>
        <text x="145" y="170" font-size="11" font-weight="bold" fill="#ea580c">Fr = μ·N</text>

        <!-- Flecha de aceleración resultante -->
        <line x1="330" y1="95" x2="400" y2="95" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,2" marker-end="url(#arr-newt-r)"/>
        <text x="345" y="90" font-size="11" font-weight="bold" fill="#0284c7">a (aceleración)</text>

        <!-- Cartel 2ª Ley -->
        <rect x="50" y="30" width="165" height="50" rx="8" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.2"/>
        <text x="60" y="50" font-size="12" font-weight="bold" fill="#1e40af">🎯 2ª Ley de Newton</text>
        <text x="60" y="68" font-size="11" fill="#334155">Σ F = m · a  ➔  F - Fr = m·a</text>
      </svg>
    `,
    formal: `<div class="math-formula">Ecuación Fundamental: Σ F = m · a</div>
<b>Ejercicio de Examen:</b>
Sobre un bloque de 10 kg apoyado en un suelo horizontal se aplica una fuerza de F = 50 N hacia la derecha. El coeficiente de rozamiento entre el suelo y el bloque es μ = 0,2 (g = 9,8 m/s²).
1º <b>Eje Vertical (Equilibrio Y):</b> N - P = 0  ⟹  N = P = m · g = 10 · 9,8 = <b>98 N</b>.
2º <b>Fuerza de Rozamiento:</b> Fr = μ · N = 0,2 · 98 = <b>19,6 N</b>.
3º <b>Eje Horizontal (Movimiento X):</b>
Fuerza neta = F - Fr = 50 N - 19,6 N = <b>30,4 N</b>.
4º <b>Aceleración del bloque:</b>
a = Fuerza neta / masa = 30,4 N / 10 kg = <b>3,04 m/s²</b>.`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Empujamos un cajón de 5 kg con una fuerza de 30 N sobre un suelo cuyo rozamiento genera una resistencia de Fr = 10 N. ¿Con qué aceleración se moverá el cajón?<br/>
<i>Pista del abuelo: Fuerza neta = 30 - 10 = 20 N. Ahora divide entre la masa (5 kg): a = 20 / 5 = 4 m/s².</i>`
  },

  // --- CONSERVACIÓN DE LA ENERGÍA MECÁNICA ---
  energia: {
    title: "Conservación de la Energía Mecánica: La física invisible de la montaña rusa",
    intuition: `Dile a tu nieto: <i>«La energía es la moneda de cambio del universo: <b>ni se crea de la nada ni se destruye, solo cambia de disfraz</b>.
Imagínate una vagoneta en lo alto de una montaña rusa gigantesca de 20 metros de altura.
Cuando está parada en la cumbre antes de caer, tiene guardada una cantidad enorme de <b>Energía Potencial</b> (la energía que tiene un cuerpo solo por estar muy alto).
De repente se tira al vacío. A medida que va cayendo y perdiendo altura, esa altura no desaparece: ¡se canjea por una velocidad vertiginosa! Se transforma en <b>Energía Cinética</b> (la energía del movimiento rápido).
En el punto más bajo de la pista, donde la altura es cero, la energía potencial se ha gastado entera, pero la energía cinética es máxima: ¡la vagoneta va a toda pastilla!
Y con ese impulso, vuelve a trepar la siguiente cuesta, cambiando velocidad por altura otra vez.
La suma de las dos (Energía Mecánica = Cinética + Potencial) es un número constante y sagrado que no cambia nunca si no hay rozamiento.»</i>`,
    stepbystep: `1º <b>Energía Potencial Gravitatoria:</b> Ep = m · g · h (depende de la altura h).
2º <b>Energía Cinética:</b> Ec = ½ · m · v² (depende de la velocidad v).
3º <b>Principio de Conservación de la Energía Mecánica:</b>
Em = Ec + Ep = constante
<b>Em (en lo alto de la cima) = Em (en el suelo)</b>
m · g · h = ½ · m · v²
4º ¡Fíjate que la masa 'm' se cancela en ambos lados! Una vagoneta llena de gente y una vagoneta vacía alcanzan exactamente la misma velocidad abajo si caen desde la misma altura: <b>v = √(2 · g · h)</b>.`,
    graphDesc: "<b>Conservación de la Energía en la Montaña Rusa:</b> En el punto A (cumbre), toda la energía es Potencial (Ep max, Ec=0). En el punto B (valle), toda la energía se ha convertido en Cinética (Ec max, Ep=0). La Energía Mecánica total se mantiene constante.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <rect width="580" height="250" fill="#f8fafc"/>
        
        <!-- Pista de Montaña Rusa -->
        <path d="M 50 50 Q 200 240 380 210 T 540 90" fill="none" stroke="#475569" stroke-width="4"/>
        
        <!-- Soportes de la pista -->
        <line x1="70" y1="60" x2="70" y2="220" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3,3"/>
        <line x1="260" y1="210" x2="260" y2="220" stroke="#94a3b8" stroke-width="2"/>
        <line x1="520" y1="80" x2="520" y2="220" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3,3"/>
        <line x1="40" y1="220" x2="540" y2="220" stroke="#334155" stroke-width="2.5"/>

        <!-- Vagoneta en Cima A -->
        <circle cx="70" cy="55" r="9" fill="#dc2626"/>
        <text x="50" y="38" font-size="12" font-weight="bold" fill="#dc2626">Punto A (Cima: h=20m)</text>
        <text x="85" y="60" font-size="10" fill="#dc2626">• Ep = Máxima | Ec = 0 (v=0)</text>

        <!-- Vagoneta en Valle B -->
        <circle cx="260" cy="205" r="9" fill="#2563eb"/>
        <text x="210" y="240" font-size="12" font-weight="bold" fill="#2563eb">Punto B (Valle: h=0)</text>
        <text x="280" y="200" font-size="10" fill="#2563eb">• Ec = Máxima (v_max) | Ep = 0</text>

        <!-- Cartel de Conservación -->
        <rect x="360" y="25" width="200" height="65" rx="8" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>
        <text x="372" y="45" font-size="12" font-weight="bold" fill="#1e40af">⚡ Em = Ep + Ec = Cte</text>
        <text x="372" y="62" font-size="10.5" fill="#334155">m·g·h = ½·m·v²</text>
        <text x="372" y="78" font-size="11" font-weight="bold" fill="#047857">v = √(2 · g · h)</text>
      </svg>
    `,
    formal: `<div class="math-formula">Conservación de la Energía: Em_A = Em_B  ⟹  Ep_A + Ec_A = Ep_B + Ec_B</div>
<b>Ejercicio de Examen:</b>
Una vagoneta de 200 kg parte del reposo (v_A = 0) desde una altura h = 20 metros en una montaña rusa. Despreciando el rozamiento (g = 9,8 m/s²), calcula la velocidad con la que llega al suelo (h_B = 0).
1º <b>Energía en el punto A:</b>
Ep_A = m · g · h = 200 · 9,8 · 20 = <b>39.200 Julios (J)</b>.
Ec_A = 0 (parte del reposo).
2º <b>Energía en el punto B:</b>
Ep_B = 0 (en el suelo).
Ec_B = ½ · m · v² = ½ · 200 · v² = 100 · v².
3º <b>Igualamos las energías:</b>
39.200 = 100 · v²  ⟹  v² = 392  ⟹  <b>v = √392 ≈ 19,8 m/s (unos 71 km/h)</b>.`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Un esquiador de 60 kg se lanza desde una colina de 5 metros de altura partiendo del reposo. ¿Con qué velocidad llegará a la base de la colina? (g = 9,8 m/s²).<br/>
<i>Pista del abuelo: Usa la fórmula directa v = √(2 · g · h) = √(2 · 9,8 · 5) = √98 ≈ 9,9 m/s (unos 36 km/h). ¡Ni siquiera necesitaste usar los 60 kg de su peso!</i>`
  },

  // --- TEOREMA DE TALES Y SEMEJANZA ---
  tales: {
    title: "Teorema de Tales y Semejanza: Medir pirámides y rascacielos con un simple bastón",
    intuition: `Dile a tu nieto: <i>«Hace 2.600 años, el sabio griego Tales de Mileto visitó Egipto. Los sacerdotes del faraón le retaron: <i>'Nadie es capaz de medir la altura de la Gran Pirámide de Keops porque es imposible trepar con una cuerda hasta su punta'</i>.
Tales sonrió, clavó su bastón de madera en la arena del desierto de forma vertical y se sentó pacientemente a esperar bajo el sol.
¿Qué estaba esperando? Esperó al momento exacto del mediodía en que la sombra que el bastón proyectaba en el suelo medía exactamente lo mismo que el bastón.
En ese instante exacto, gritó: <i>'¡Medid ahora la sombra de la pirámide!'</i>. ¡La longitud de la sombra de la pirámide era idéntica a su altura!
Tales descubrió el principio de los <b>triángulos semejantes</b>: cuando dos figuras tienen exactamente los mismos ángulos (porque los rayos del sol bajan con la misma inclinación paralela), las proporciones entre sus lados son gemelas.
Si un árbol es 10 veces más alto que tu bastón, su sombra en el suelo medirá exactamente 10 veces más que la sombra de tu bastón.»</i>`,
    stepbystep: `1º <b>Triángulos en Posición de Tales:</b>
Si dos rectas secantes son cortadas por rectas paralelas (los rayos del sol), los segmentos que determinan son proporcionales:
<b>Altura_edificio / Altura_bastón = Sombra_edificio / Sombra_bastón</b>
2º <b>Fórmula para despejar la incógnita:</b>
H = h · (S / s)
(La altura desconocida H se obtiene multiplicando la altura conocida de la vara 'h' por la razón entre las dos sombras S y s).`,
    graphDesc: "<b>Geometría de Tales:</b> Los rayos de sol paralelos forman dos triángulos semejantes rectángulos. La proporción entre la altura del objeto y su sombra es constante: H / S = h / s.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <defs>
          <linearGradient id="sunGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fef08a"/>
            <stop offset="100%" stop-color="#facc15"/>
          </linearGradient>
        </defs>
        <rect width="580" height="250" fill="#f8fafc"/>
        
        <!-- Suelo arenoso -->
        <line x1="30" y1="210" x2="550" y2="210" stroke="#78350f" stroke-width="2.5"/>

        <!-- Sol en lo alto -->
        <circle cx="80" cy="40" r="22" fill="url(#sunGrad)" stroke="#eab308" stroke-width="2"/>
        <text x="110" y="45" font-size="12" font-weight="bold" fill="#ca8a04">☀️ Rayos solares paralelos</text>

        <!-- Pirámide / Edificio grande (H) -->
        <polygon points="120,210 220,70 320,210" fill="#fde68a" stroke="#d97706" stroke-width="2.5"/>
        <line x1="220" y1="70" x2="220" y2="210" stroke="#b45309" stroke-width="2" stroke-dasharray="4,3"/>
        <text x="225" y="145" font-size="13" font-weight="bold" fill="#b45309">Altura H (?)</text>
        
        <!-- Sombra del Edificio (S) -->
        <line x1="220" y1="210" x2="390" y2="210" stroke="#d97706" stroke-width="4"/>
        <text x="270" y="226" font-size="11" font-weight="bold" fill="#92400e">Sombra S = 24 m</text>

        <!-- Rayo solar que roza la pirámide -->
        <line x1="220" y1="70" x2="390" y2="210" stroke="#eab308" stroke-width="2" stroke-dasharray="5,3"/>

        <!-- Bastón de Tales (h) -->
        <line x1="450" y1="160" x2="450" y2="210" stroke="#0f172a" stroke-width="3.5"/>
        <text x="455" y="185" font-size="11" font-weight="bold" fill="#0f172a">Vara h = 1.5 m</text>

        <!-- Sombra del bastón (s) -->
        <line x1="450" y1="210" x2="495" y2="210" stroke="#0284c7" stroke-width="4"/>
        <text x="455" y="226" font-size="11" font-weight="bold" fill="#0369a1">s = 2 m</text>
        <line x1="450" y1="160" x2="495" y2="210" stroke="#eab308" stroke-width="2" stroke-dasharray="5,3"/>

        <!-- Cartel de proporción de Tales -->
        <rect x="340" y="30" width="220" height="52" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
        <text x="352" y="50" font-size="12" font-weight="bold" fill="#0284c7">📐 H / S = h / s</text>
        <text x="352" y="70" font-size="11" fill="#334155">H = h · (S / s) = 1.5 · (24/2) = 18 m</text>
      </svg>
    `,
    formal: `<div class="math-formula">Teorema de Tales: H / S = h / s  ⟹  H = h · (S / s)</div>
<b>Problema Clásico de Examen:</b>
Queremos calcular la altura de la torre de una iglesia. En el mismo momento del día, un poste vertical de 2 metros proyecta una sombra de 1,5 metros en el suelo, mientras que la sombra de la torre mide 36 metros.
1º <b>Planteamiento de semejanza:</b>
H / 36 = 2 / 1,5
2º <b>Despejamos la altura H:</b>
H = (2 · 36) / 1,5 = 72 / 1,5 = <b>48 metros</b> de altura.`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
Un árbol proyecta una sombra de 12 metros en el parque. Justo a su lado, Lucas (que mide 1,5 metros de alto) proyecta una sombra de 2 metros. ¿Cuánto mide el árbol?<br/>
<i>Pista del abuelo: La sombra del árbol es 6 veces más larga que la de Lucas (12 / 2 = 6). Por tanto, el árbol mide 6 veces la altura de Lucas: 1,5 × 6 = 9 metros.</i>`
  },

  // --- PRINCIPIO DE BERNOULLI Y AERODINÁMICA ---
  bernoulli: {
    title: "Principio de Bernoulli: ¿Por qué vuelan los aviones gigantes de 400 toneladas?",
    intuition: `Dile a tu nieto: <i>«¿Cómo es posible que un avión Boeing 747, que pesa 400.000 kilos de metal macizo con cientos de pasajeros y maletas, se mantenga flotando en el aire sin caerse?
Haz este experimento en casa con una tira de papel: sostén un extremo del papel pegado a tu labio inferior y sopla fuerte por encima de él. ¿Qué hace el papel? ¡Sube hacia arriba desafiando la gravedad!
El físico suizo Daniel Bernoulli descubrió en 1738 la razón: <b>cuando el aire viaja más rápido, ejerce menos presión</b>.
Las alas de los aviones no son planas: tienen una forma especial de joroba (perfil alar), muy curvadas por arriba y completamente planas por abajo.
Cuando el avión corre por la pista, el aire que pasa por encima del ala se ve obligado a viajar más rápido para sortear la curva que el aire de abajo.
Al ir más rápido, la presión arriba baja drásticamente: se forma una zona de 'vacío' o succión que aspira el ala hacia el cielo. Esa fuerza se llama <b>Sustentación</b>. ¡El aire 'chupa' el avión hacia las nubes!»</i>`,
    stepbystep: `1º <b>Forma asimétrica del ala (Perfil alar):</b> El camino superior es más largo que el inferior.
2º <b>Diferencia de velocidades:</b> Velocidad superior (v₁) > Velocidad inferior (v₂).
3º <b>Efecto Bernoulli:</b> A mayor velocidad, menor presión: Presión superior (P₁) < Presión inferior (P₂).
4º <b>Fuerza neta de Sustentación (L):</b>
La mayor presión de abajo empuja el ala hacia arriba con una fuerza de toneladas: Sustentación L = (P₂ - P₁) · Superficie_ala.`,
    graphDesc: "<b>Perfil Alar y Principio de Bernoulli:</b> El aire viaja a mayor velocidad por la superficie curvada superior (Baja Presión P₁), generando una fuerza de succión hacia arriba (Sustentación) que vence al peso del avión.",
    getSvg: () => `
      <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
        <defs>
          <marker id="arr-lift" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 10 L 5 0 L 10 10 z" fill="#0284c7"/>
          </marker>
        </defs>
        <rect width="580" height="250" fill="#f8fafc"/>
        
        <!-- Líneas de corriente de aire superiores (rápidas, comprimidas) -->
        <path d="M 50 70 Q 220 20 450 75" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6,3"/>
        <path d="M 50 85 Q 220 40 450 85" fill="none" stroke="#0284c7" stroke-width="3"/>
        
        <!-- Perfil alar del avión -->
        <path d="M 120 130 C 120 70, 300 70, 420 130 C 320 140, 160 140, 120 130 Z" fill="#94a3b8" stroke="#334155" stroke-width="3"/>
        <text x="210" y="125" font-size="13" font-weight="bold" fill="#0f172a">Ala de Avión</text>

        <!-- Líneas de corriente inferiores (lentas, rectas) -->
        <path d="M 50 155 Q 260 155 450 155" fill="none" stroke="#64748b" stroke-width="2.5"/>
        <path d="M 50 175 Q 260 175 450 175" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6,3"/>

        <!-- Textos de velocidad y presión -->
        <text x="180" y="45" font-size="12" font-weight="bold" fill="#0369a1">Alta velocidad (v₁) ➔ BAJA PRESIÓN (P₁)</text>
        <text x="180" y="200" font-size="12" font-weight="bold" fill="#334155">Baja velocidad (v₂) ➔ ALTA PRESIÓN (P₂)</text>

        <!-- Flechas de Sustentación hacia arriba -->
        <line x1="260" y1="110" x2="260" y2="40" stroke="#0284c7" stroke-width="4" marker-end="url(#arr-lift)"/>
        <text x="270" y="55" font-size="13" font-weight="bold" fill="#0284c7">Sustentación (Fuerza hacia arriba)</text>
      </svg>
    `,
    formal: `<div class="math-formula">Ecuación de Bernoulli: P + ½ · ρ · v² + ρ · g · h = constante</div>
<b>Conclusión Física:</b> Al mantenerse la altura h constante entre la cara superior e inferior del ala:
P₁ + ½ · ρ · v₁² = P₂ + ½ · ρ · v₂²
Como v₁ > v₂  ⟹  <b>P₁ < P₂</b> (Efecto de succión ascendente).`,
    twin: `<b>Reto Gemelo para Lucas:</b><br/>
¿Por qué cuando estás en la ducha y abres el grifo de agua caliente con fuerza, la cortina de plástico de la ducha se mete hacia dentro y se te pega a las piernas?<br/>
<i>Pista del abuelo: ¡Es el principio de Bernoulli! El chorro de agua arrastra el aire dentro de la ducha a gran velocidad, reduciendo la presión interna. El aire quieto de fuera tiene más presión y empuja la cortina hacia ti.</i>`
  }
};

let currentMathData = null;

// ==========================================================================
// 3. MOTOR DE RESOLUCIÓN PEDAGÓGICA CON ACTIVACIÓN DE GRÁFICA
// ==========================================================================
function solveMathProblem() {
  const qText = document.getElementById('math-question').value.trim();
  const nietoName = document.getElementById('nieto-name').value.trim() || "mi nieto";
  const levelSelect = document.getElementById('math-level');
  const levelText = levelSelect.options[levelSelect.selectedIndex].text;

  if (!qText) {
    alert("Por favor, escribe la duda, teorema o problema que quieres explicarle a tu nieto.");
    return;
  }

  const qLower = qText.toLowerCase();
  let matchedData = null;

  // Búsqueda semántica inteligente (Matemáticas, Física y Teoremas Científicos)
  if (qLower.includes("arquimedes") || qLower.includes("arquímedes") || qLower.includes("empuje") || qLower.includes("flota") || qLower.includes("eureka") || qLower.includes("desalojado") || qLower.includes("corona de oro") || qLower.includes("peso aparente")) {
    matchedData = MATH_KNOWLEDGE_BASE.arquimedes;
  } else if (qLower.includes("pascal") || qLower.includes("prensa hidraulica") || qLower.includes("prensa hidráulica") || qLower.includes("embolo") || qLower.includes("émbolo") || qLower.includes("elevador hidraulico") || qLower.includes("elevador hidráulico")) {
    matchedData = MATH_KNOWLEDGE_BASE.pascal;
  } else if (qLower.includes("newton") || qLower.includes("inercia") || qLower.includes("f = m") || qLower.includes("f=m") || qLower.includes("accion y reaccion") || qLower.includes("acción y reacción") || qLower.includes("fuerza y aceleracion") || qLower.includes("dinamica") || qLower.includes("dinámica")) {
    matchedData = MATH_KNOWLEDGE_BASE.newton;
  } else if (qLower.includes("energia") || qLower.includes("energía") || qLower.includes("cinetica") || qLower.includes("cinética") || qLower.includes("potencial") || qLower.includes("montaña rusa") || qLower.includes("mecanica") || qLower.includes("mecánica")) {
    matchedData = MATH_KNOWLEDGE_BASE.energia;
  } else if (qLower.includes("tales") || qLower.includes("thales") || qLower.includes("semejanza") || qLower.includes("triangulos semejantes") || qLower.includes("triángulos semejantes") || qLower.includes("sombra piramide") || qLower.includes("sombra del arbol")) {
    matchedData = MATH_KNOWLEDGE_BASE.tales;
  } else if (qLower.includes("bernoulli") || qLower.includes("venturi") || qLower.includes("avion") || qLower.includes("avión") || qLower.includes("alas") || qLower.includes("sustentacion") || qLower.includes("sustentación")) {
    matchedData = MATH_KNOWLEDGE_BASE.bernoulli;
  } else if (qLower.includes("derivada") || qLower.includes("diferencial") || qLower.includes("tangente") || qLower.includes("velocidad instantanea") || qLower.includes("pendiente de una curva")) {
    matchedData = MATH_KNOWLEDGE_BASE.derivada;
  } else if (qLower.includes("integral") || qLower.includes("área bajo la curva") || qLower.includes("area bajo la curva") || qLower.includes("barrow") || qLower.includes("primitiva") || qLower.includes("riemann")) {
    matchedData = MATH_KNOWLEDGE_BASE.integral;
  } else if (qLower.includes("logaritmo") || qLower.includes("richter") || qLower.includes("decibelio") || qLower.includes("neperiano")) {
    matchedData = MATH_KNOWLEDGE_BASE.logaritmo;
  } else if (qLower.includes("segundo grado") || qLower.includes("x²") || qLower.includes("x^2") || qLower.includes("cuadrática") || qLower.includes("cuadratica") || qLower.includes("parabola") || qLower.includes("parábola")) {
    matchedData = MATH_KNOWLEDGE_BASE.ecuacion2;
  } else if (qLower.includes("coche") || qLower.includes("tren") || qLower.includes("velocidad") || qLower.includes("encuentr") || qLower.includes("km/h")) {
    matchedData = MATH_KNOWLEDGE_BASE.coches;
  } else if (qLower.includes("trigonometr") || qLower.includes("seno") || qLower.includes("coseno") || qLower.includes("angulo") || qLower.includes("ángulo")) {
    matchedData = MATH_KNOWLEDGE_BASE.trigonometria;
  } else if (qLower.includes("pitagoras") || qLower.includes("pitágoras") || qLower.includes("hipotenusa") || qLower.includes("cateto") || qLower.includes("escalera")) {
    matchedData = MATH_KNOWLEDGE_BASE.pitagoras;
  } else if (qLower.includes("negativo") || qLower.includes("signos") || qLower.includes("menos por menos") || qLower.includes("entero")) {
    matchedData = MATH_KNOWLEDGE_BASE.negativo;
  } else if (qLower.includes("sistema") || qLower.includes("dos ecuaciones") || qLower.includes("incognita") || qLower.includes("incógnita")) {
    matchedData = MATH_KNOWLEDGE_BASE.sistema;
  } else if (qLower.includes("fraccion") || qLower.includes("fracción") || qLower.includes("denominador") || qLower.includes("mcm") || qLower.includes("m.c.m")) {
    matchedData = MATH_KNOWLEDGE_BASE.fracciones;
  } else if (qLower.includes("porcentaj") || qLower.includes("rebaja") || qLower.includes("descuento") || qLower.includes("%") || qLower.includes("iva")) {
    matchedData = MATH_KNOWLEDGE_BASE.porcentajes;
  }

  // Generación pedagógica enriquecida si es una consulta libre diferente
  if (!matchedData) {
    matchedData = {
      title: `Razonamiento Explicativo para ${nietoName} (Ciencias, Física y Matemáticas - ${levelText})`,
      intuition: `Para que ${nietoName} comprenda de verdad este concepto (<i>«${qText}»</i>), lo primero que debemos hacer como abuelos es despojar a la pregunta de todo tecnicismo árido y buscar su equivalente en el mundo tangible.
Las ciencias, la física y las matemáticas no nacieron en despachos universitarios con fórmulas abstractas, sino en los talleres, puertos, barcos y observatorios: para saber por qué flotaban los barcos de guerra, para levantar pesos gigantescos con poleas y prensas sin romperse la espalda, para calcular la trayectoria de una bala o un satélite, o para medir parcelas de tierra tras las crecidas de los ríos.
Cuando le expliques esto a ${nietoName}, dile: <i>«No mires las fórmulas como una amenaza de examen; imagínate que es una ley del universo que describe cómo funciona la realidad que tocas con tus manos todos los días»</i>.`,
      stepbystep: `<b>El protocolo del Abuelo Tutor para desgranar cualquier problema científico o matemático:</b><br/>
1º <b>La lectura dramatizada:</b> Leed el enunciado juntos en voz alta. Pídele que te lo cuente con sus propias palabras como si fuera un misterio o una película de intriga.<br/>
2º <b>Separar datos de preguntas:</b> Subrayad con lápiz verde los datos seguros que nos da el problema (masas, distancias, tiempos, densidades), y con lápiz rojo la incógnita exacta que nos pide averiguar.<br/>
3º <b>El dibujo en servilleta (Diagrama visual):</b> Dibujad siempre un esquema físico: las fuerzas tirando hacia arriba o abajo, los recipientes de líquido, la trayectoria o el triángulo.<br/>
4º <b>Comprobación con el sentido común:</b> Antes de dar por bueno un número, pregúntale a ${nietoName}: <i>«¿Tiene lógica este resultado en el mundo real?»</i>.`,
      formal: `<div class="math-formula">Estructura Curricular para el Cuaderno Escolar de ${nietoName}:</div>
• <b>Planteamiento Físico/Matemático:</b> Declaración explícita de incógnitas, unidades en el Sistema Internacional (SI: kg, m, s, N, J, Pa) y fórmulas del currículo escolar.<br/>
• <b>Desarrollo analítico:</b> Sustitución numérica paso a paso sin saltarse operaciones intermedias.<br/>
• <b>Solución definitiva:</b> Resultado numérico recuadrado con sus unidades correspondientes.<br/>
<i>💡 Si necesitas una explicación aún más detallada para este ejercicio específico, pulsa el botón morado de abajo para consultar directamente en Gemini.</i>`,
      twin: `<b>Reto Gemelo para ${nietoName}:</b><br/>
Prueba a resolver este mismo problema pero duplicando los valores iniciales en la cuadrícula de trabajo. Si logras llegar al resultado razonando cada paso, significará que has entendido el concepto y no solo los números de memoria.`,
      graphDesc: `<b>Esquema Conceptual de Equilibrio y Despeje:</b> En todo problema de ciencias o matemáticas, la igualdad (=) es una balanza perfecta. En el platillo izquierdo colocamos los datos que conocemos, y en el derecho equilibramos para despejar la incógnita.`,
      getSvg: () => {
        const cleanQ = qText.length > 45 ? qText.substring(0, 42) + "..." : qText;
        return `
        <svg viewBox="0 0 580 250" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif;">
          <defs>
            <marker id="arr-bal-r" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#0284c7"/>
            </marker>
          </defs>
          <rect width="580" height="250" fill="#f8fafc"/>
          
          <!-- Suelo -->
          <line x1="40" y1="220" x2="540" y2="220" stroke="#334155" stroke-width="2.5"/>

          <!-- Columna central de la balanza -->
          <polygon points="282,220 295,95 305,95 318,220" fill="#475569"/>
          <circle cx="300" cy="90" r="8" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>

          <!-- Barra horizontal de equilibrio -->
          <line x1="120" y1="90" x2="480" y2="90" stroke="#0f172a" stroke-width="4"/>

          <!-- Cuerdas y Platillo Izquierdo -->
          <line x1="120" y1="90" x2="90" y2="150" stroke="#64748b" stroke-width="2"/>
          <line x1="120" y1="90" x2="150" y2="150" stroke="#64748b" stroke-width="2"/>
          <path d="M 70 150 Q 120 170 170 150 Z" fill="#94a3b8" stroke="#475569" stroke-width="2"/>

          <!-- Cuerdas y Platillo Derecho -->
          <line x1="480" y1="90" x2="450" y2="150" stroke="#64748b" stroke-width="2"/>
          <line x1="480" y1="90" x2="510" y2="150" stroke="#64748b" stroke-width="2"/>
          <path d="M 430 150 Q 480 170 530 150 Z" fill="#94a3b8" stroke="#475569" stroke-width="2"/>

          <!-- Contenido Platillo Izquierdo (Datos conocidos) -->
          <rect x="90" y="120" width="60" height="30" rx="4" fill="#10b981"/>
          <text x="96" y="139" font-size="11" font-weight="bold" fill="#ffffff">DATOS</text>
          <text x="75" y="185" font-size="11" font-weight="bold" fill="#047857">Pistas conocidas</text>

          <!-- Flecha de relación lógica -->
          <line x1="210" y1="135" x2="390" y2="135" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="5,3" marker-end="url(#arr-bal-r)"/>
          <text x="240" y="125" font-size="11" font-weight="bold" fill="#0284c7">Ecuación / Despeje</text>

          <!-- Contenido Platillo Derecho (Incógnita a despejar) -->
          <rect x="450" y="115" width="60" height="35" rx="4" fill="#dc2626"/>
          <text x="472" y="138" font-size="16" font-weight="bold" fill="#ffffff">?</text>
          <text x="430" y="185" font-size="11" font-weight="bold" fill="#dc2626">Incógnita a resolver</text>

          <!-- Cartela superior con la consulta -->
          <rect x="110" y="22" width="360" height="42" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
          <text x="125" y="40" font-size="11.5" font-weight="bold" fill="#0284c7">⚖️ Balanza Lógica para ${nietoName}:</text>
          <text x="125" y="55" font-size="10.5" fill="#334155">«${cleanQ}»</text>
        </svg>
        `;
      }
    };
  }

  currentMathData = {
    ...matchedData,
    questionText: qText,
    nietoName: nietoName,
    levelText: levelText
  };

  // Renderizar textos
  document.getElementById('math-result-title').textContent = `📖 ${matchedData.title || 'Explicación Pedagógica'}`;
  document.getElementById('res-math-intuition').innerHTML = matchedData.intuition.replace(/Lucas/g, nietoName);
  document.getElementById('res-math-stepbystep').innerHTML = matchedData.stepbystep.replace(/Lucas/g, nietoName).replace(/\n/g, '<br/>');
  document.getElementById('res-math-formal').innerHTML = matchedData.formal;
  document.getElementById('res-math-twin').innerHTML = matchedData.twin.replace(/Lucas/g, nietoName);

  // Renderizar Gráfica SVG SIEMPRE (Garantía pedagógica total)
  const graphBox = document.getElementById('math-graph-box');
  const graphDesc = document.getElementById('math-graph-desc');
  const graphSvgContainer = document.getElementById('math-graph-svg');

  graphDesc.innerHTML = matchedData.graphDesc || "Representación gráfica visual:";
  graphSvgContainer.innerHTML = matchedData.getSvg ? matchedData.getSvg() : "";
  graphBox.style.display = 'block';

  // Limpiar el historial de conversación para la nueva duda
  const chatHist = document.getElementById('chat-history');
  if (chatHist) {
    chatHist.innerHTML = '';
    chatHist.style.display = 'none';
  }

  document.getElementById('math-result').classList.add('visible');
  document.getElementById('btn-print-math').style.display = 'inline-flex';
  document.getElementById('btn-gemini-math').style.display = 'inline-block';

  document.getElementById('math-result').scrollIntoView({ behavior: 'smooth' });
}

// ==========================================================================
// 4. DIÁLOGO SOCRÁTICO CONTINUO (PREGUNTAR DUDAS A LA IA)
// ==========================================================================
function sendSocraticQuestion() {
  const inputEl = document.getElementById('chat-user-msg');
  const userQ = inputEl.value.trim();
  if (!userQ) return;

  const chatHist = document.getElementById('chat-history');
  const nieto = (currentMathData && currentMathData.nietoName) || "tu nieto";

  // Mostrar el contenedor de mensajes
  chatHist.style.display = 'flex';

  // 1. Añadir la burbuja del usuario
  const userBubble = document.createElement('div');
  userBubble.className = 'chat-bubble bubble-user';
  userBubble.textContent = userQ;
  chatHist.appendChild(userBubble);
  inputEl.value = '';

  // 2. Generar respuesta socrática inteligente
  const qLower = userQ.toLowerCase();
  let aiReply = "";

  if (qLower.includes("arquimedes") || qLower.includes("arquímedes") || qLower.includes("empuje") || qLower.includes("barco") || qLower.includes("flota") || qLower.includes("hierro")) {
    aiReply = `¡Fíjate qué fascinante para ${nieto}! Dile esto:
<i>«¿Por qué un tornillo de hierro de 5 gramos se hunde hasta el fondo y un barco petrolero de 100.000 toneladas de hierro flota como una pluma en el mar?»</i><br/>
Porque el tornillo es macizo y ocupa muy poco espacio: solo desaloja 1 mililitro de agua, y el empuje de ese mililitro hacia arriba es ridículo.<br/>
En cambio, el barco de acero está <b>hueco por dentro lleno de aire</b>: para meterlo en el mar tiene que empujar y apartar miles de toneladas de agua salada. Y como descubrió Arquímedes, el agua devuelve el empujón hacia arriba con el peso exacto de toda esa agua apartada. ¡Esa fuerza hacia arriba supera con creces todo el peso del acero!`;
  } else if (qLower.includes("eureka") || qLower.includes("bañera") || qLower.includes("corona")) {
    aiReply = `¡La anécdota de la bañera de Arquímedes es la mejor para contarle a ${nieto} merendando!<br/>
El rey de Siracusa le dio una barra de oro a un joyero para hacer una corona para los dioses. Sospechaba que el joyero le había robado oro y metido plata barata dentro, pero no quería romper la corona para comprobarlo.<br/>
Arquímedes se estaba bañando y vio que al meter su cuerpo, el agua desbordaba por los bordes. Se dio cuenta de que la plata ocupa más volumen que el oro para el mismo peso (la plata es menos densa). Si la corona desalojaba más agua que un lingote de oro puro del mismo peso... ¡el joyero era un ladrón! Salió corriendo desnudo gritando: <b>«¡Eureka!»</b> («¡Lo encontré!»).`;
  } else if (qLower.includes("pascal") || qLower.includes("prensa") || qLower.includes("freno")) {
    aiReply = `El principio de Pascal es la base de cómo frenan los camiones y coches modernos.<br/>
El líquido de frenos no se puede comprimir ni aplastar. Cuando el conductor pisa el pedal con un pie suavemente, esa presión empuja por un tubito estrecho y llega a los frenos de las cuatro ruedas gigantes, multiplicando la fuerza por 50 para frenar en seco un vehículo de dos toneladas. ¡El agua o el aceite transmiten la fuerza íntegra!`;
  } else if (qLower.includes("newton") || qLower.includes("inercia") || qLower.includes("fuerza")) {
    aiReply = `Para que ${nieto} entienda las leyes de Newton:<br/>
1. <b>Inercia:</b> Si vas en patinete o autobús y frena de golpe, tu cuerpo sigue hacia adelante. ¡Las cosas quieren seguir como están a no ser que alguien las obligue!<br/>
2. <b>F = m · a:</b> Para acelerar un balón de fútbol necesitas una patada suave; para acelerar un balón medicinal de 5 kg necesitas una patada con toda tu fuerza. A más masa, más fuerza cuesta moverlo.<br/>
3. <b>Acción y Reacción:</b> Cuando inflas un globo y lo sueltas sin atar, el aire sale hacia abajo y el globo vuela hacia arriba disparado. ¡Toda acción produce una reacción opuesta!`;
  } else if (qLower.includes("c") || qLower.includes("constante")) {
    aiReply = `¡Qué pregunta tan inteligente para ${nieto}! Te lo explico con la <b>metáfora del ascensor</b>:
Imagínate que un ascensor sube 3 pisos (+3).
Si el ascensor arrancó en la planta baja (piso 0), terminará en el piso 3. Pero si arrancó en el piso 10, terminará en el piso 13.
En ambos casos, el movimiento fue exactamente el mismo (+3 pisos de subida).
Al derivar una función matemática, solo medimos la velocidad o el movimiento del ascensor, pero se nos 'olvida' saber desde qué piso despegó originalmente en el edificio.
Por eso en las integrales los matemáticos siempre ponen <b>«+ C»</b> (una constante desconocida), para avisar: <i>«Sabemos cuánto se movió la curva, pero no sabemos la altura exacta del suelo hasta que el problema nos dé un dato inicial extra»</i>.`;
  } else if (qLower.includes("grafic") || qLower.includes("gráfic") || qLower.includes("dibuj") || qLower.includes("curva") || qLower.includes("secante") || qLower.includes("tangente")) {
    aiReply = `¡Fíjate en la <b>sección gráfica de arriba</b>! Hemos incluido la gráfica interactiva donde puedes ver con total claridad la curva, el punto exacto, la recta secante naranja (que une dos momentos separados) y cómo al juntarse se convierte en la recta tangente roja. ¡Verlo con los ojos vale más que diez páginas de fórmulas!`;
  } else if (qLower.includes("divid") || qLower.includes("entre 2") || qLower.includes("partido 2") || qLower.includes("/2")) {
    aiReply = `¿Por qué se divide entre 2? Imagínate un folio de papel rectangular. Si mide 4 cm de alto por 6 cm de largo, su área entera es 4 × 6 = 24 cm².
Ahora coge unas tijeras y corta el folio en diagonal de esquina a esquina: te quedan dos triángulos idénticos, y cada uno tiene exactamente la mitad de superficie: (4 × 6) / 2 = 12 cm².
En cálculo y física, cuando una velocidad empieza en cero y va subiendo en rampa constante, la figura que forma debajo no es una caja cuadrada, ¡es medio rectángulo (un triángulo)! Por eso siempre aparece ese «dividido entre 2».`;
  } else if (qLower.includes("otro ejemplo") || qLower.includes("mas facil") || qLower.includes("más fácil") || qLower.includes("no lo entiende") || qLower.includes("no entiendo")) {
    aiReply = `¡Vamos con un ejemplo todavía más visual para merendar con ${nieto}!
Imagínate una hucha donde metes monedas.
Si cada día metes exactamente 2 monedas de euro, a los 10 días tienes 2 × 10 = 20 euros (aritmética simple de multiplicar).
Pero si el primer día metes 1 moneda, el segundo día 2, el tercer día 3, el cuarto día 4... el ritmo al que entra el dinero va acelerando.
Al final de la semana no multiplicas plano, sino que sumas una escalera de monedas: 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 monedas.
Las fórmulas complejas solo son el atajo de los sabios para no tener que contar monedas una a una cuando la hucha tiene millones de céntimos.`;
  } else if (qLower.includes("para que sirve") || qLower.includes("vida real") || qLower.includes("utilidad")) {
    aiReply = `Dile a ${nieto} que esto se usa todos los días en cosas que le encantan:
1. <b>En los barcos y submarinos:</b> Para no irse a pique en las tormentas y flotar con precisión de milímetros.
2. <b>En los videojuegos (como Fortnite o FIFA):</b> Para calcular la trayectoria parabólica del balón o cómo rebota un coche tras un derrape.
3. <b>En los teléfonos móviles y coches:</b> Para calibrar los frenos ABS, los sensores de aceleración y las pantallas táctiles.
4. <b>En la medicina:</b> Para calcular la dosis exacta de un antibiótico en sangre para que baje la infección sin dañar el riñón.`;
  } else if (qLower.includes("negativo") || qLower.includes("raiz") || qLower.includes("raíz")) {
    aiReply = `Dile a ${nieto}: <i>«Busca dos números idénticos que multiplicados den -16»</i>.
Si prueba con +4: 4 × 4 = +16.
Si prueba con -4: (-4) × (-4) = ¡también +16, porque menos por menos es más!
¡Es imposible que un número al cuadrado dé negativo! Por eso cuando dentro de una raíz cuadrada sale un número negativo, la balanza se rompe y en el colegio se escribe: <b>'No tiene solución real'</b>. (Para resolverlo en la universidad se inventaron los 'números imaginarios', representados con la letra 'i').`;
  } else {
    aiReply = `Comprendo perfectamente tu duda, abuelo/a. Respecto a <i>«${userQ}»</i>:
En este nivel escolar, la clave que debes transmitirle a ${nieto} es que no intente memorizar pasos mecánicamente como si fuera una receta de cocina sin sentido.
Pregúntale siempre: <i>«¿Qué representa este número o fuerza en el dibujo?»</i>. Cuando asociamos cada término a un objeto físico (un metro, un kilogramo, una fuerza de empuje o un segundo de tiempo), la confusión desaparece de inmediato.
<br/><br/><i>💡 Si quieres profundizar todavía más en este matiz concreto, pulsa arriba el botón «⚡ Si quieres profundizar más... (Consultar en Gemini)».</i>`;
  }

  // 3. Añadir burbuja de la IA
  const aiBubble = document.createElement('div');
  aiBubble.className = 'chat-bubble bubble-ai';
  aiBubble.innerHTML = `👴 <strong>El Abuelo Tutor:</strong><br/>${aiReply}`;
  chatHist.appendChild(aiBubble);

  // Auto-scroll
  chatHist.scrollTop = chatHist.scrollHeight;
}

// ==========================================================================
// 5. CONSULTA EN DIRECTO CON GEMINI (PROMPT MAESTRO SOCRÁTICO)
// ==========================================================================
function openInGemini() {
  if (!currentMathData) return;

  const nieto = currentMathData.nietoName || "mi nieto";
  const nivel = currentMathData.levelText || "Escolar";
  const pregunta = currentMathData.questionText;

  const promptTexto = `Actúa como un profesor emérito de ciencias, física y matemáticas y un abuelo paciente, sabio y cariñoso.
Mi nieto/a ${nieto} tiene ${nivel} y tiene la siguiente duda, problema o teorema:

«${pregunta}»

Por favor, no me des una respuesta fría de libro de texto ni te limites a soltar fórmulas. Necesito que me des una explicación con un inmenso valor añadido pedagógico estructurada exactamente en 5 partes:

1. 🌟 COMPRENSIÓN INTUITIVA COTIDIANA: Una analogía visual, anécdota histórica (como la bañera de Arquímedes o la manzana de Newton) o historia cotidiana sin números ni miedo, para que el niño entienda para qué sirve y qué significa antes de ver fórmulas.
2. 🧠 EL PASO A PASO RAZONADO: La explicación lógica desmenuzada paso a paso, explicando el «por qué» de cada movimiento matemático o físico sin saltos mágicos.
3. 📊 ILUSTRACIÓN O ESQUEMA GRÁFICO: Describe con claridad cómo dibujar un esquema visual (fuerzas, vectores de empuje, curvas, secantes/tangentes o áreas) para visualizarlo con los ojos.
4. 📝 PARA EL EXAMEN DEL COLEGIO: El rigor formal con las fórmulas del currículo escolar, unidades del Sistema Internacional (N, J, Pa, m/s²...) y el desarrollo completo para sacar la máxima nota.
5. 🎯 EL RETO GEMELO: Un problema gemelo con números cambiados para que ${nieto} lo resuelva a solas a lápiz en su cuaderno y demuestre que lo ha aprendido.`;

  navigator.clipboard.writeText(promptTexto).then(() => {
    alert(`✨ ¡La consulta explicativa ha sido copiada al portapapeles!\n\nAhora se abrirá Google Gemini en una nueva pestaña.\nSolo tienes que pulsar Ctrl+V (o Cmd+V en Mac) en el cuadro de texto de Gemini y pulsar Enter para ver la explicación en vivo de la IA.`);
    window.open("https://gemini.google.com", "_blank");
  }).catch(() => {
    window.open("https://gemini.google.com", "_blank");
  });
}

// ==========================================================================
// 6. IMPRESIÓN DE LA FICHA DE MATEMÁTICAS Y CIENCIAS CON GRÁFICA Y CUADRÍCULA
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
        <h1>📐 Cuaderno de Ciencias y Matemáticas Razonadas</h1>
        <div style="font-size: 11pt; color: #333; margin-top: 4px;">Tutor: Educanietos IA • Nivel: ${currentMathData.levelText}</div>
      </div>
      <div class="print-meta">
        <div><strong>Alumno/a:</strong> ${nieto}</div>
        <div><strong>Fecha:</strong> ${fechaStr}</div>
      </div>
    </div>

    <div class="print-box">
      <h2>📌 El Concepto, Teorema o Problema a Resolver:</h2>
      <p style="font-size: 11pt; font-weight: bold; margin-top: 4px;">${currentMathData.questionText}</p>
    </div>

    <div class="print-box">
      <h2>🌟 1. La Idea Intuitiva (Para comprenderlo sin miedo):</h2>
      <p style="font-size: 10pt; line-height: 1.5;">${currentMathData.intuition.replace(/Lucas/g, nieto)}</p>
    </div>

    <div class="print-box">
      <h2>🧠 2. El Paso a Paso Razonado:</h2>
      <div style="font-size: 10pt; line-height: 1.5;">${currentMathData.stepbystep.replace(/Lucas/g, nieto).replace(/\n/g, '<br/>')}</div>
    </div>

    ${currentMathData.getSvg ? `
    <div class="print-box" style="text-align: center; page-break-inside: avoid;">
      <h2>📊 Ilustración Gráfica / Esquema Conceptual:</h2>
      <div style="max-width: 480px; margin: 0 auto;">
        ${currentMathData.getSvg()}
      </div>
    </div>
    ` : ''}

    <div class="print-box">
      <h2>📝 3. Solución Formal para el Examen:</h2>
      <div style="font-size: 10pt; line-height: 1.5;">${currentMathData.formal}</div>
    </div>

    <div class="page-break"></div>

    <div class="print-header">
      <div>
        <h1>🎯 Reto Gemelo: ¡Demuestra lo que has aprendido!</h1>
        <div style="font-size: 10pt; color: #333;">Espacio de resolución a lápiz para ${nieto}</div>
      </div>
      <div class="print-meta">
        <div><strong>Calificación del Abuelo:</strong> [ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ]</div>
      </div>
    </div>

    <div class="print-box">
      <h2>Enunciado del Reto:</h2>
      <p style="font-size: 11pt; line-height: 1.5;">${currentMathData.twin.replace(/Lucas/g, nieto)}</p>
    </div>

    <div style="margin-top: 14px;">
      <h3 style="font-size: 11pt; margin-bottom: 6px;">✏️ Resuelve aquí paso a paso (Usa lápiz y regla):</h3>
      <div class="print-grid"></div>
    </div>

    <div style="margin-top: 20px; border-top: 1px solid #999; padding-top: 8px; font-size: 9pt; color: #555; text-align: center;">
      Educanietos IA • Explicaciones Claras y Razonadas para el Éxito Escolar
    </div>
  `;

  window.print();
}
