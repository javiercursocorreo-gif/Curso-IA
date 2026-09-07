/**
 * EDUCANIETOS IA - Tutor Inteligente para Abuelos y Nietos
 * Simplicidad total: Conecta directamente con Google Gemini y NotebookLM
 */

// ==========================================================================
// 1. GESTIÓN DE PESTAÑAS
// ==========================================================================
function switchTab(tabId) {
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));

  const activeContent = document.getElementById(tabId);
  if (activeContent) activeContent.classList.add('active');

  const buttons = document.querySelectorAll('.tab-btn');
  if (tabId === 'tab-mates') buttons[0].classList.add('active');
  else if (tabId === 'tab-historia-nlm') buttons[1].classList.add('active');
  else if (tabId === 'tab-guia') buttons[2].classList.add('active');
}

// ==========================================================================
// 2. GESTIÓN DEL SELECTOR TÁCTIL DE EDADES
// ==========================================================================
let currentAgeKey = 'eso'; // Por defecto: 12-14 años

function selectAge(ageKey) {
  currentAgeKey = ageKey;
  
  const hiddenInput = document.getElementById('selected-age-key');
  if (hiddenInput) hiddenInput.value = ageKey;

  document.querySelectorAll('.age-pill-btn').forEach(btn => {
    if (btn.getAttribute('data-age') === ageKey) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
}

// ==========================================================================
// 3. CALIBRACIÓN PSICOLÓGICA Y COGNITIVA POR EDADES
// ==========================================================================
const AGE_CONFIGS = {
  peque: {
    label: "8 a 11 años (Primaria)",
    directive: `ADAPTACIÓN PSICOLÓGICA Y COGNITIVA OBLIGATORIA (El niño/a tiene 8-11 años, Primaria):
- TONO: Muy cariñoso, lúdico, cercano y lleno de curiosidad, como una historia fascinante.
- CIENCIA Y MATEMÁTICAS: PROHIBIDO utilizar fórmulas químicas abstractas complejas, enlaces covalentes o ecuaciones algebraicas avanzadas. Si te piden una fórmula química (como el etanol o el agua), explícala como una "receta mágica de bolitas de LEGO de la naturaleza" (ejemplo: tantas bolitas de carbono, tantas de hidrógeno y tantas de oxígeno unidas dándose la mano).
- ENFOQUE: Céntrate en para qué sirve en la vida cotidiana (el bote de alcohol de curar heridas, el gel de manos, la cocina) y metáforas con juguetes o comida.
- RIGOR: Solo vocabulario muy sencillo de Primaria. Sin tecnicismos aburridos ni arcanos.`
  },
  eso: {
    label: "12 a 14 años (1º y 2º de la ESO)",
    directive: `ADAPTACIÓN PSICOLÓGICA Y COGNITIVA OBLIGATORIA (El alumno/a tiene 12-14 años, 1º y 2º de la ESO):
- TONO: Motivador, práctico y ameno de profesor de secundaria. Ni infantil ni universitario.
- CIENCIA Y MATEMÁTICAS: Introduce la notación elemental estándar de la ESO (por ejemplo, la fórmula molecular básica C₂H₆O o CH₃-CH₂-OH explicada con átomos y enlaces sencillos, o ecuaciones de 1º grado paso a paso).
- ENFOQUE: Conectar la teoría con la vida real (por ejemplo, la fermentación de la fruta, desinfectantes o energía) y el porqué de los fenómenos.
- RIGOR: Los conceptos clave y el vocabulario que le piden en sus exámenes de ciencias de 1º y 2º de la ESO.`
  },
  mayor: {
    label: "15 a 18 años (3º-4º de la ESO y Bachillerato)",
    directive: `ADAPTACIÓN PSICOLÓGICA Y COGNITIVA OBLIGATORIA (El estudiante tiene 15-18 años, 3º-4º ESO / Bachillerato):
- TONO: Académico, riguroso y formal, orientado al bachillerato y preparación para la Universidad/Selectividad/EBAU.
- CIENCIA Y MATEMÁTICAS: Máximo rigor conceptual. Fórmulas semidesarrolladas y desarrolladas, grupos funcionales (ej. función alcohol -OH), enlaces, polaridad, nomenclatura IUPAC oficial, unidades precisas del Sistema Internacional (SI) y deducciones analíticas formales.
- ENFOQUE: Profundidad en el mecanismo físico, químico o matemático, desarrollo paso a paso impecable y justificación teórica completa.
- RIGOR: El estándar oficial que exige un examen de Bachillerato para aspirar a la máxima nota (un 10).`
  }
};

// ==========================================================================
// 4. GENERADOR DEL PROMPT PEDAGÓGICO MAESTRO PARA GEMINI
// ==========================================================================
function generatePedagogicalPrompt(question, nietoName, ageKey) {
  const ageConfig = AGE_CONFIGS[ageKey] || AGE_CONFIGS['eso'];

  return `Actúa como un profesor emérito de ciencias, física, química y matemáticas y a la vez como un abuelo paciente, sabio y cariñoso.
Mi nieto/a ${nietoName} (${ageConfig.label}) necesita entender la siguiente duda o ejercicio:

«${question}»

${ageConfig.directive}

Por favor, no me des una respuesta fría de libro ni un texto interminable. Necesito una FICHA EXPLICATIVA PEDAGÓGICA, amena, clara y RELATIVAMENTE CORTA (directa al grano para no cansar al estudiante), estructurada exactamente en 5 partes:

1. 🌟 COMPRENSIÓN INTUITIVA (Analogía cotidiana): Una comparación visual con la vida real adaptada estrictamente a sus ${ageConfig.label} para que entienda el concepto sin miedo antes de ver números o fórmulas.
2. 🧠 EL PASO A PASO RAZONADO (Sin rodeos): Explica la lógica de por qué ocurre cada paso sin dar saltos mágicos, ajustado a su nivel de comprensión.
3. 🎨 IMAGEN ILUSTRADA O GRÁFICA DIDÁCTICA BONITA: Genera una imagen visual ilustrada a todo color (utiliza tu generador de imágenes integrado para crear una ilustración bonita, limpia y atractiva de esta escena, concepto o gráfica). PROHIBIDO terminantemente dibujar cuadros feos en texto plano (Plaintext/ASCII) con guiones o barras en blanco y negro: debe ser una imagen visual real, colorida y de alta calidad para que mi nieto la vea con los ojos.
4. 📝 EL NIVEL PARA SU EXAMEN (${ageConfig.label}): Las fórmulas oficiales, vocabulario y desarrollo limpio adaptado a su edad para que lo borde en el colegio.
5. 🎯 EL RETO GEMELO: Un problema gemelo con datos cambiados para que ${nietoName} lo resuelva a solas a lápiz en su cuaderno.

(Nota: Redáctalo de forma limpia y legible para que podamos imprimirlo o guardarlo en PDF directamente desde aquí).`;
}

// ==========================================================================
// 5. ACCIÓN PRINCIPAL: 1 CLIC A GOOGLE GEMINI
// ==========================================================================
function launchGeminiWeb() {
  const qInput = document.getElementById('math-question');
  const qText = qInput ? qInput.value.trim() : "";
  const nietoInput = document.getElementById('nieto-name');
  const nietoName = (nietoInput && nietoInput.value.trim()) || "mi nieto";

  const hiddenAge = document.getElementById('selected-age-key');
  const ageKey = (hiddenAge && hiddenAge.value) || currentAgeKey || 'eso';

  if (!qText) {
    alert("Por favor, escribe primero la duda o problema que quieres explicarle a tu nieto.");
    if (qInput) qInput.focus();
    return;
  }

  const prompt = generatePedagogicalPrompt(qText, nietoName, ageKey);

  // 1. Copiar al portapapeles de forma garantizada
  try {
    const tempEl = document.createElement("textarea");
    tempEl.value = prompt;
    tempEl.style.position = "fixed";
    tempEl.style.left = "-9999px";
    document.body.appendChild(tempEl);
    tempEl.select();
    document.execCommand("copy");
    document.body.removeChild(tempEl);
  } catch (err) {}

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(prompt).catch(() => {});
  }

  // 2. ABRIR GEMINI SÍNCRONAMENTE (garantiza que Safari y Chrome en Mac NUNCA bloqueen la pestaña)
  window.open("https://gemini.google.com", "_blank");

  // 3. Mostrar aviso breve en pantalla
  const hint = document.getElementById('gemini-hint');
  if (hint) hint.style.display = 'block';
}
