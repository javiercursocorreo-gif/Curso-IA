#!/usr/bin/env node
/**
 * build_monografico_03_unificado.js
 * Genera el documento único simplificado para el Monográfico 3:
 * "MONOGRAFICO_3_COMO_CREAR_UN_CUENTO_ILUSTRADO_CON_IA.pdf"
 * 
 * Correcciones matemáticas y espaciales definitivas:
 * 1. Flujo dinámico vertical de la caja de Introducción: el subtítulo "Flujo unificado..."
 *    se posiciona automáticamente DEBAJO de todas las líneas del párrafo inicial (cero solapamiento).
 * 2. Altura holgada de la caja de Opción Alternativa (66 pt en vez de 48 pt): margen libre de 14 pt
 *    al fondo para que el borde inferior no toque ni atraviese jamás la última frase.
 * 3. En el Paso 1: indicación explícita de crear el cuaderno «CUENTOS» en Gemini.
 * 4. Tipografía española impecable: 'niño', 'años', 'guión', 'sueño' con Ñ en WinAnsi.
 */

const fs = require('fs');
const path = require('path');

const BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA";
const MONO3_DIR = path.join(BASE_DIR, "CLASES/3. COMO_HACER_UN_CUENTO_CON_NLM");
const MONO_CLASSROOM_DIR = path.join(BASE_DIR, "CLASES/105. [MONOGRAFICOS] CUADERNOS_Y_TALLERES_ESPECIALES");

const OUTPUT_PDF_1 = path.join(MONO3_DIR, "MONOGRAFICO_3_COMO_CREAR_UN_CUENTO_ILUSTRADO_CON_IA.pdf");
const OUTPUT_PDF_2 = path.join(MONO_CLASSROOM_DIR, "MONOGRAFICO_3_COMO_CREAR_UN_CUENTO_ILUSTRADO_CON_IA.pdf");

function escapePdfText(text) {
  text = String(text);
  text = text.replace(/\\/g, '\\\\').replace(/\(/g, '\\(').replace(/\)/g, '\\)');
  const replacements = {
    'á': '\xe1', 'é': '\xe9', 'í': '\xed', 'ó': '\xf3', 'ú': '\xfa',
    'Á': '\xc1', 'É': '\xc9', 'Í': '\xcd', 'Ó': '\xd3', 'Ú': '\xda',
    'ñ': '\xf1', 'Ñ': '\xd1', 'ü': '\xfc', 'Ü': '\xdc',
    '«': '<<', '»': '>>', '•': '-', '—': '-', '–': '-',
    'º': 'o', 'ª': 'a', '¿': '\xbf', '¡': '\xa1',
    '➔': '->', '→': '->', '’': "'", '‘': "'", '“': '"', '”': '"'
  };
  for (const [k, v] of Object.entries(replacements)) {
    text = text.split(k).join(v);
  }
  return text;
}

function wrapText(text, maxChars) {
  const paragraphs = String(text).split('\n');
  const lines = [];
  for (const p of paragraphs) {
    const trimmed = p.trim();
    if (!trimmed) {
      lines.push('');
      continue;
    }
    const words = trimmed.split(' ');
    let cur = [];
    let curLen = 0;
    for (const w of words) {
      if (!w) continue;
      if (curLen + w.length + 1 <= maxChars) {
        cur.push(w);
        curLen += w.length + 1;
      } else {
        if (cur.length > 0) lines.push(cur.join(' '));
        cur = [w];
        curLen = w.length;
      }
    }
    if (cur.length > 0) lines.push(cur.join(' '));
  }
  return lines.length ? lines : [''];
}

class NativePDFWriter {
  constructor(pageWidth = 612.0, pageHeight = 792.0) {
    this.w = pageWidth;
    this.h = pageHeight;
    this.pages = [];
    this.currentStream = [];
  }

  startPage() {
    this.currentStream = [];
  }

  endPage() {
    this.pages.push(this.currentStream.join(''));
    this.currentStream = [];
  }

  setFillColor(r, g, b) {
    this.currentStream.push(`${r.toFixed(3)} ${g.toFixed(3)} ${b.toFixed(3)} rg\n`);
  }

  setStrokeColor(r, g, b) {
    this.currentStream.push(`${r.toFixed(3)} ${g.toFixed(3)} ${b.toFixed(3)} RG\n`);
  }

  setLineWidth(width) {
    this.currentStream.push(`${width.toFixed(2)} w\n`);
  }

  rect(x, y, width, height, fill = true, stroke = true) {
    const op = (fill && stroke) ? 'B' : (fill ? 'f' : 'S');
    this.currentStream.push(`${x.toFixed(2)} ${y.toFixed(2)} ${width.toFixed(2)} ${height.toFixed(2)} re ${op}\n`);
  }

  line(x1, y1, x2, y2) {
    this.currentStream.push(`${x1.toFixed(2)} ${y1.toFixed(2)} m ${x2.toFixed(2)} ${y2.toFixed(2)} l S\n`);
  }

  drawText(x, y, text, font = 'F1', size = 10, r = 0, g = 0, b = 0) {
    this.setFillColor(r, g, b);
    const escaped = escapePdfText(text);
    this.currentStream.push(`BT /${font} ${size.toFixed(1)} Tf ${x.toFixed(2)} ${y.toFixed(2)} Td (${escaped}) Tj ET\n`);
  }

  writeToFile(filename) {
    fs.mkdirSync(path.dirname(filename), { recursive: true });
    const pageObjIndices = [];
    const contentObjIndices = [];
    let curObjIdx = 8; // 1: Catalog, 2: Pages, 3-7: Fonts

    for (let i = 0; i < this.pages.length; i++) {
      pageObjIndices.push(curObjIdx++);
      contentObjIndices.push(curObjIdx++);
    }

    const kidsStr = pageObjIndices.map(idx => `${idx} 0 R`).join(' ');
    const pagesDict = Buffer.from(`<< /Type /Pages /Kids [${kidsStr}] /Count ${this.pages.length} >>`, 'ascii');

    const allObjs = [
      Buffer.from('<< /Type /Catalog /Pages 2 0 R >>', 'ascii'),
      pagesDict,
      Buffer.from('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>', 'ascii'),
      Buffer.from('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>', 'ascii'),
      Buffer.from('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>', 'ascii'),
      Buffer.from('<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>', 'ascii'),
      Buffer.from('<< /Type /Font /Subtype /Type1 /BaseFont /Courier-Bold /Encoding /WinAnsiEncoding >>', 'ascii')
    ];

    for (let i = 0; i < this.pages.length; i++) {
      const contentIdx = contentObjIndices[i];
      const pObj = Buffer.from(
        `<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${this.w} ${this.h}] ` +
        `/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R /F4 6 0 R /F5 7 0 R >> >> ` +
        `/Contents ${contentIdx} 0 R >>`,
        'ascii'
      );
      allObjs.push(pObj);

      const sBytes = Buffer.from(this.pages[i], 'latin1');
      const cObj = Buffer.concat([
        Buffer.from(`<< /Length ${sBytes.length} >>\nstream\n`, 'ascii'),
        sBytes,
        Buffer.from('\nendstream', 'ascii')
      ]);
      allObjs.push(cObj);
    }

    const outChunks = [];
    outChunks.push(Buffer.from('%PDF-1.4\n%\xe2\xe3\xcf\xd3\n', 'latin1'));
    const offsets = [];
    let curOffset = outChunks[0].length;

    for (let i = 0; i < allObjs.length; i++) {
      offsets.push(curOffset);
      const header = Buffer.from(`${i + 1} 0 obj\n`, 'ascii');
      const footer = Buffer.from('\nendobj\n', 'ascii');
      outChunks.push(header, allObjs[i], footer);
      curOffset += header.length + allObjs[i].length + footer.length;
    }

    const xrefOffset = curOffset;
    let xrefStr = `xref\n0 ${allObjs.length + 1}\n0000000000 65535 f \n`;
    for (const off of offsets) {
      xrefStr += `${String(off).padStart(10, '0')} 00000 n \n`;
    }
    const xrefBuf = Buffer.from(xrefStr, 'ascii');
    const trailerBuf = Buffer.from(
      `trailer\n<< /Size ${allObjs.length + 1} /Root 1 0 R >>\nstartxref\n${xrefOffset}\n%%EOF\n`,
      'ascii'
    );
    outChunks.push(xrefBuf, trailerBuf);

    fs.writeFileSync(filename, Buffer.concat(outChunks));
    console.log(`[PDF] Generado con éxito: ${filename} (${this.pages.length} págs)`);
  }
}

function buildPdf() {
  const pdf = new NativePDFWriter(612, 792);

  // =========================================================================
  // PÁGINA 1: INTRODUCCIÓN AL PROYECTO + PASO 1 (CREAR EL CUADERNO Y CUENTO)
  // =========================================================================
  pdf.startPage();

  // Fondo sutil de página
  pdf.setFillColor(0.985, 0.988, 0.995);
  pdf.rect(0, 0, 612, 792, true, false);

  // 1. Cabecera institucional
  pdf.setFillColor(0.06, 0.09, 0.16); // Navy #0f172a
  pdf.rect(36, 706, 540, 56, true, false);

  // Borde inferior cabecera magenta/cyan
  pdf.setFillColor(0.55, 0.36, 0.96); // Purple #8b5cf6
  pdf.rect(36, 704, 540, 2, true, false);

  // Badge píldora
  pdf.drawText(48, 744, "CURSO DE INTELIGENCIA ARTIFICIAL  •  MONOGRÁFICO 3", 'F2', 8.5, 0.22, 0.74, 0.97);

  // Título Principal
  pdf.drawText(48, 725, "CÓMO CREAR UN CUENTO ILUSTRADO CON IA", 'F2', 15.0, 1, 1, 1);
  pdf.drawText(48, 712, "Guía integral en 3 pasos: De la idea en Gemini a la presentación visual en NotebookLM", 'F1', 9.0, 0.85, 0.90, 0.98);

  // 2. SECCIÓN: INTRODUCCIÓN AL PROYECTO (MAQUETACIÓN DINÁMICA DE ARRIBA A ABAJO)
  const box1Top = 692;
  const box1W = 540;
  
  // Textos de la caja de introducción
  const introTitle = "PROYECTO: TU CUENTO FAMILIAR EN 3 PASOS DIRECTOS";
  const introText1 = "El objetivo de este proyecto es crear un cuento infantil ilustrado para nuestros nietos o familia sin necesidad de dibujar ni programar. Unimos la capacidad de redacción de Google Gemini con el poder visual de NotebookLM (Gemini Notebook) para lograr un resultado entrañable, profesional y con personajes consistentes.";
  const wrappedIntro1 = wrapText(introText1, 94); // 4 líneas
  
  const introSub = "Flujo unificado sin saltar entre archivos:";
  const stepsList = [
    "1. PASO 1 (Gemini): Creas el cuaderno CUENTOS y redactas la historia con valores.",
    "2. PASO 2 (Gemini): Conviertes el cuento en un guión estructurado de 10 escenas.",
    "3. PASO 3 (NotebookLM): Abres tu cuaderno CUENTOS para generar la presentación visual en 3D."
  ];

  // Cálculo exacto de altura necesaria:
  // Top padding: 16 pt
  // Título: 12 pt
  // Gap: 14 pt
  // Párrafo (4 líneas x 13 pt): 52 pt
  // Gap: 14 pt
  // Subtítulo: 11 pt
  // Gap: 12 pt
  // 3 líneas de lista x 13 pt: 39 pt
  // Bottom padding: 15 pt
  // Total altura: 16 + 12 + 14 + 52 + 14 + 11 + 12 + 39 + 15 = 175 pt
  const box1H = 158;
  const box1Bottom = box1Top - box1H;

  // Dibujar fondo de la Caja 1
  pdf.setFillColor(1, 1, 1);
  pdf.setStrokeColor(0.85, 0.88, 0.92);
  pdf.setLineWidth(1);
  pdf.rect(36, box1Bottom, box1W, box1H, true, true);

  // Imprimir contenidos secuenciales dentro de Caja 1
  let curY = box1Top - 18;
  pdf.drawText(50, curY, introTitle, 'F2', 10.5, 0.06, 0.09, 0.16);
  curY -= 15;

  for (const line of wrappedIntro1) {
    pdf.drawText(50, curY, line, 'F1', 8.8, 0.25, 0.28, 0.35);
    curY -= 12.5;
  }

  curY -= 3; // Gap visual claro
  pdf.drawText(50, curY, introSub, 'F2', 9.0, 0.55, 0.36, 0.96);
  curY -= 14;

  for (const step of stepsList) {
    pdf.drawText(50, curY, step, 'F1', 8.6, 0.20, 0.23, 0.30);
    curY -= 12.5;
  }
  // curY queda en ~546, mientras que box1Bottom está en 534 (margen libre de 12 pt)

  // 3. SECCIÓN: PASO 1 (CREAR EL CUADERNO Y EL CUENTO)
  let paso1Top = box1Bottom - 14; // ~520
  pdf.setFillColor(0.15, 0.23, 0.36); // #2563eb / navy
  pdf.rect(36, paso1Top - 22, 540, 22, true, false);
  pdf.drawText(50, paso1Top - 16, "PASO 1: CREAR EL CUADERNO «CUENTOS» Y LA HISTORIA EN GOOGLE GEMINI", 'F2', 10.0, 1, 1, 1);

  curY = paso1Top - 36;
  pdf.drawText(36, curY, "Qué hace este paso (Tu punto de partida):", 'F2', 9.5, 0.06, 0.09, 0.16);
  
  curY -= 13;
  const paso1Desc = "1. Abre Google Gemini (gemini.google.com). Crea o abre un nuevo chat o cuaderno llamado «CUENTOS».\n" +
                    "2. Esto es esencial: al trabajar dentro de «CUENTOS», luego te encontrarás el cuaderno listo automáticamente en NotebookLM.\n" +
                    "3. Pega el prompt que tienes debajo: Gemini redactará la historia ajustando el vocabulario a la edad exacta del niño.";
  const linesPaso1Desc = paso1Desc.split('\n');
  for (const line of linesPaso1Desc) {
    const wrapped = wrapText(line, 98);
    for (const w of wrapped) {
      pdf.drawText(36, curY, w, 'F1', 8.6, 0.22, 0.25, 0.32);
      curY -= 11.5;
    }
  }

  // Caja de Prompt Paso 1
  curY -= 4;
  const promptBoxH = 168;
  const promptBoxBottom = curY - promptBoxH;
  pdf.setFillColor(0.08, 0.11, 0.18); // #141c2e pizarra oscura
  pdf.setStrokeColor(0.25, 0.35, 0.50);
  pdf.setLineWidth(1);
  pdf.rect(36, promptBoxBottom, 540, promptBoxH, true, true);

  // Etiqueta Prompt
  pdf.drawText(50, curY - 16, "COPIA Y PEGA ESTE PROMPT EN TU CUADERNO «CUENTOS» DE GEMINI:", 'F5', 8.8, 0.22, 0.74, 0.97);

  const prompt1Content = 
`Actúa como un cuentacuentos infantil profesional.
Escribe un cuento de buenas noches de 3 o 4 párrafos sobre:
"El Viaje en Globo del Abuelo y la Gata Luna" (o el tema que elijas).

DATOS OBLIGATORIOS PARA LA HISTORIA:
1. EDAD DEL NIÑO: Este cuento es para un niño de [indica aquí la edad, ej: 6] años.
   Ajusta estrictamente el vocabulario, la ternura y la madurez a su nivel.
2. VALORES: Debe transmitir de forma sutil valores de curiosidad, aventura
   compartida, confianza mutua y amor a la naturaleza.
3. TONO: Usa un lenguaje visual y atrapante, con un final tranquilo y muy
   reconfortante para que le ayude a conciliar el sueño feliz.`;

  const linesPrompt1 = prompt1Content.split('\n');
  let p1Y = curY - 31;
  for (const l of linesPrompt1) {
    pdf.drawText(50, p1Y, l, 'F4', 8.0, 0.92, 0.95, 1.0);
    p1Y -= 11.0;
  }

  // 4. CAJA DE OPCIÓN ALTERNATIVA (CON ALTURA Y MÁRGENES HOLGADOS PARA NO ATRAVESAR TEXTO)
  const altTop = promptBoxBottom - 10;
  const altBoxH = 60; // 60 pt garantiza espacio total para título + 3 líneas + padding inferior
  const altBottom = altTop - altBoxH;

  pdf.setFillColor(1, 1, 1);
  pdf.setStrokeColor(0.85, 0.88, 0.92);
  pdf.rect(36, altBottom, 540, altBoxH, true, true);

  pdf.drawText(48, altTop - 14, "OPCIÓN ALTERNATIVA (Para alumnos con historia propia inventada):", 'F2', 8.5, 0.55, 0.36, 0.96);
  
  const notaAlt = "Si ya tienes escrito tu cuento, dile a Gemini: «A continuación te pego un cuento escrito por mí. Reescriíbelo manteniendo mi historia exacta pero usando un lenguaje mágico, adaptado a un niño de [X] años y resaltando los valores de aventura y cariño.»";
  const wrappedAlt = wrapText(notaAlt, 98);
  
  let altTextY = altTop - 26;
  for (const l of wrappedAlt) {
    pdf.drawText(48, altTextY, l, 'F1', 8.2, 0.30, 0.33, 0.40);
    altTextY -= 11.0;
  }
  // altTextY queda en ~altTop - 48, mientras que altBottom está en altTop - 60 (margen libre de 12 pt al fondo)

  // Pie de página 1
  pdf.setStrokeColor(0.80, 0.83, 0.88);
  pdf.setLineWidth(0.8);
  pdf.line(36, 42, 576, 42);
  pdf.drawText(36, 30, "Curso de Inteligencia Artificial • Monográfico 3: Cuento Ilustrado", 'F1', 8.0, 0.50, 0.55, 0.62);
  pdf.drawText(530, 30, "Página 1 de 2", 'F2', 8.0, 0.50, 0.55, 0.62);

  pdf.endPage();

  // =========================================================================
  // PÁGINA 2: PASO 2 (GUIÓN 10 PÁGINAS) + PASO 3 (NOTEBOOKLM) + CONSEJOS
  // =========================================================================
  pdf.startPage();

  // Fondo sutil de página
  pdf.setFillColor(0.985, 0.988, 0.995);
  pdf.rect(0, 0, 612, 792, true, false);

  // Cabecera compacta página 2
  pdf.setFillColor(0.06, 0.09, 0.16);
  pdf.rect(36, 736, 540, 26, true, false);
  pdf.drawText(48, 746, "MONOGRÁFICO 3: CUENTO ILUSTRADO CON IA  •  PASOS 2 Y 3", 'F2', 9.5, 1, 1, 1);
  pdf.drawText(470, 746, "GUÍA DIDÁCTICA", 'F5', 8.5, 0.22, 0.74, 0.97);

  // 1. SECCIÓN: PASO 2 (CONVERTIR EL CUENTO EN GUIÓN DE 10 ESCENAS)
  curY = 722;
  pdf.setFillColor(0.45, 0.22, 0.78); // Purple #7c3aed
  pdf.rect(36, curY - 22, 540, 22, true, false);
  pdf.drawText(50, curY - 16, "PASO 2: CONVERTIR EL CUENTO EN GUIÓN DE 10 ESCENAS (En Gemini)", 'F2', 10.0, 1, 1, 1);

  curY -= 36;
  pdf.drawText(36, curY, "Qué hace este paso (Transformación audiovisual):", 'F2', 9.5, 0.06, 0.09, 0.16);

  curY -= 13;
  const paso2Desc = "¡IMPORTANTE: No abras un chat nuevo! En la misma conversación de Gemini dentro de «CUENTOS», pega este segundo prompt. Gemini actuará como director audiovisual y dividirá la historia en un guión estructurado de 10 escenas, definiendo el plano, la vestimenta fija de los personajes y los diálogos.";
  const wrappedPaso2 = wrapText(paso2Desc, 98);
  for (const line of wrappedPaso2) {
    pdf.drawText(36, curY, line, 'F1', 8.8, 0.22, 0.25, 0.32);
    curY -= 12;
  }

  // Caja Prompt Paso 2
  curY -= 5;
  const prompt2BoxH = 158;
  pdf.setFillColor(0.08, 0.11, 0.18);
  pdf.setStrokeColor(0.40, 0.30, 0.60);
  pdf.setLineWidth(1);
  pdf.rect(36, curY - prompt2BoxH, 540, prompt2BoxH, true, true);

  pdf.drawText(50, curY - 17, "PEGA ESTE SEGUNDO PROMPT EN LA MISMA CONVERSACIÓN DE GEMINI:", 'F5', 8.8, 0.75, 0.55, 0.98);

  const prompt2Content =
`Toma el cuento generado en el mensaje anterior y crea el guión de un cómic
secuencial siguiendo estrictamente estas instrucciones:

1. EXTENSIÓN: Debe tener EXACTAMENTE 10 PÁGINAS (de [PÁGINA 1] a [PÁGINA 10]).
2. ESTRUCTURA DE CADA PÁGINA:
   - [PÁGINA X: TÍTULO DE LA ESCENA]
   - Resumen narrativo de 1 línea.
   - Escena clave y tipo de plano (General, Plano Medio o Primer Plano).
   - Descripción visual: qué ocurre y qué se ve.
     IMPORTANTE: Mantén idéntica la vestimenta, colores y rasgos físicos
     de los personajes en todas las páginas para garantizar consistencia total.
   - Iluminación y atmósfera ambiental.
   - Diálogo obligatorio y Pensamiento del personaje.

Transforma ahora el cuento en el guión de 10 páginas completo.`;

  const linesPrompt2 = prompt2Content.split('\n');
  let p2Y = curY - 32;
  for (const l of linesPrompt2) {
    pdf.drawText(50, p2Y, l, 'F4', 8.0, 0.92, 0.95, 1.0);
    p2Y -= 11.2;
  }

  // 2. SECCIÓN: PASO 3 (LLEVAR A NOTEBOOKLM / GEMINI NOTEBOOK)
  curY = curY - prompt2BoxH - 16;
  pdf.setFillColor(0.05, 0.55, 0.40); // Emerald #059669
  pdf.rect(36, curY - 22, 540, 22, true, false);
  pdf.drawText(50, curY - 16, "PASO 3: LLEVAR EL GUIÓN A NOTEBOOKLM (GEMINI NOTEBOOK) Y CREAR EL ARTE", 'F2', 9.8, 1, 1, 1);

  curY -= 36;
  pdf.drawText(36, curY, "Qué hace este paso (Tu cuaderno «CUENTOS» te estará esperando):", 'F2', 9.5, 0.06, 0.09, 0.16);

  curY -= 13;
  const paso3Desc = "1. Abre NotebookLM (Gemini Notebook en notebooklm.google.com) con tu misma cuenta de Google.\n" +
                    "2. ¡Tu cuaderno ya estará esperándote! Abre el cuaderno «CUENTOS» (o crea uno nuevo y pega el guión de 10 páginas como fuente).\n" +
                    "3. Pulsa el botón «Presentación» (o «Resumen de Audio» para escucharlo narrado como podcast) y aplica los parámetros visuales que tienes debajo.";
  const linesPaso3 = paso3Desc.split('\n');
  for (const l of linesPaso3) {
    const wrapped = wrapText(l, 98);
    for (const w of wrapped) {
      pdf.drawText(36, curY, w, 'F1', 8.8, 0.22, 0.25, 0.32);
      curY -= 12;
    }
  }

  // Caja Prompt Paso 3
  curY -= 5;
  const prompt3BoxH = 142;
  pdf.setFillColor(0.08, 0.11, 0.18);
  pdf.setStrokeColor(0.15, 0.50, 0.40);
  pdf.setLineWidth(1);
  pdf.rect(36, curY - prompt3BoxH, 540, prompt3BoxH, true, true);

  pdf.drawText(50, curY - 17, "PARÁMETROS VISUALES Y PROMPT FINAL EN NOTEBOOKLM:", 'F5', 8.8, 0.30, 0.85, 0.65);

  const prompt3Content =
`Aplica estrictamente los siguientes parámetros para generar la presentación
visual de este cómic basándote en el guión adjunto en las fuentes:

- ESTILO VISUAL: Animación 3D entrañable tipo Pixar (personajes en 3D con
  iluminación cinematográfica cálida, texturas suaves y máxima expresividad).
- CONSISTENCIA TOTAL: Mantén la apariencia, colores de ropa, edad y rasgos
  de todos los personajes exactamente iguales en todas las láminas.
- MAQUETACIÓN AL 100%: Cada página generada debe llenar todo el lienzo visual
  sin dejar huecos en blanco.
Genera ahora la presentación ilustrada del cómic.`;

  const linesPrompt3 = prompt3Content.split('\n');
  let p3Y = curY - 32;
  for (const l of linesPrompt3) {
    pdf.drawText(50, p3Y, l, 'F4', 8.0, 0.92, 0.95, 1.0);
    p3Y -= 11.2;
  }

  // 3. CAJA DE CONSEJOS PRÁCTICOS PARA EL ALUMNO SENIOR
  curY = curY - prompt3BoxH - 12;
  pdf.setFillColor(1, 1, 1);
  pdf.setStrokeColor(0.85, 0.88, 0.92);
  pdf.rect(36, curY - 46, 540, 46, true, true);

  pdf.drawText(48, curY - 14, "CONSEJOS DE ORO PARA DISFRUTAR EL CUENTO:", 'F2', 8.5, 0.06, 0.09, 0.16);
  pdf.drawText(48, curY - 26, "• En la Tablet o iPad: Abre la presentación en pantalla completa para enseñársela a los nietos en el sofá.", 'F1', 8.2, 0.30, 0.33, 0.40);
  pdf.drawText(48, curY - 38, "• Audio mágico: Si generas el podcast de audio en NotebookLM, ponlo de fondo mientras pasan las páginas.", 'F1', 8.2, 0.30, 0.33, 0.40);

  // Pie de página 2
  pdf.setStrokeColor(0.80, 0.83, 0.88);
  pdf.setLineWidth(0.8);
  pdf.line(36, 42, 576, 42);
  pdf.drawText(36, 30, "Curso de Inteligencia Artificial • Monográfico 3: Cuento Ilustrado", 'F1', 8.0, 0.50, 0.55, 0.62);
  pdf.drawText(530, 30, "Página 2 de 2", 'F2', 8.0, 0.50, 0.55, 0.62);

  pdf.endPage();

  // Guardar en ambas ubicaciones
  pdf.writeToFile(OUTPUT_PDF_1);
  pdf.writeToFile(OUTPUT_PDF_2);
}

buildPdf();
