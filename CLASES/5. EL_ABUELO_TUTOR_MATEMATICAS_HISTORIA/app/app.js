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
// 2. GENERADOR DEL PROMPT PEDAGÓGICO MAESTRO PARA GEMINI
// ==========================================================================
function generatePedagogicalPrompt(question, nietoName, levelText) {
  return `Actúa como un profesor emérito de ciencias, física, química y matemáticas y a la vez como un abuelo paciente, sabio y cariñoso.
Mi nieto/a ${nietoName} (nivel escolar: ${levelText}) necesita entender la siguiente duda o ejercicio:

«${question}»

Por favor, no me des una respuesta fría de libro ni un texto interminable y aburrido. Necesito una FICHA EXPLICATIVA PEDAGÓGICA, amena, clara y RELATIVAMENTE CORTA (directa al grano para no cansar al niño), estructurada exactamente en 5 partes:

1. 🌟 COMPRENSIÓN INTUITIVA (Analogía cotidiana): Una comparación visual con la vida real (la cocina, el deporte, juguetes o la naturaleza) o anécdota histórica para que entienda el concepto sin miedo antes de ver números.
2. 🧠 EL PASO A PASO RAZONADO (Sin rodeos): Explica la lógica de por qué se hace cada paso sin dar saltos mágicos.
3. 📊 ESQUEMA GRÁFICO O ILUSTRACIÓN: Un diagrama visual claro (puedes usar un esquema en texto/ASCII bien formateado, flechas o una descripción visual paso a paso) para que mi nieto pueda dibujarlo fácilmente con regla y colores en su cuaderno escolar.
4. 📝 RIGOR PARA EL EXAMEN: Las fórmulas oficiales con sus unidades del Sistema Internacional (SI) y el desarrollo limpio para sacar la máxima nota en el colegio.
5. 🎯 EL RETO GEMELO: Un problema gemelo con datos cambiados para que ${nietoName} lo resuelva a solas a lápiz en su cuaderno.

(Nota: Redáctalo de forma limpia y legible para que podamos imprimirlo o guardarlo en PDF directamente desde aquí).`;
}

// ==========================================================================
// 3. ACCIÓN PRINCIPAL: 1 CLIC A GOOGLE GEMINI
// ==========================================================================
function launchGeminiWeb() {
  const qInput = document.getElementById('math-question');
  const qText = qInput ? qInput.value.trim() : "";
  const nietoInput = document.getElementById('nieto-name');
  const nietoName = (nietoInput && nietoInput.value.trim()) || "mi nieto";
  const levelSelect = document.getElementById('math-level');
  const levelText = levelSelect ? levelSelect.options[levelSelect.selectedIndex].text : "Escolar";

  if (!qText) {
    alert("Por favor, escribe primero la duda o problema que quieres explicarle a tu nieto.");
    if (qInput) qInput.focus();
    return;
  }

  const prompt = generatePedagogicalPrompt(qText, nietoName, levelText);

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
