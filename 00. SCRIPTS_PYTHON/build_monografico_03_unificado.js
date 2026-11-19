#!/usr/bin/env node
/**
 * build_monografico_03_unificado.js
 * Genera el documento único simplificado para el Monográfico 3:
 * "MONOGRAFICO_3_COMO_CREAR_UN_CUENTO_ILUSTRADO_CON_IA.pdf"
 * 
 * Incorpora el truco maestro de "Personalizar Audio (Customize)" para que el podcast
 * de NotebookLM narre el cuento con voces y ternura infantil en vez de analizarlo.
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
    let curObjIdx = 8;

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
  pdf.setFillColor(0.06, 0.09, 0.16);
  pdf.rect(36, 706, 540, 56, true, false);

  // Borde inferior cabecera magenta/cyan
  pdf.setFillColor(0.55, 0.36, 0.96);
  pdf.rect(36, 704, 540, 2, true, false);

  // Badge píldora
  pdf.drawText(48, 744, "CURSO DE INTELIGENCIA ARTIFICIAL  •  MONOGRÁFICO 3", 'F2', 8.5, 0.22, 0.74, 0.97);

  // Título Principal
  pdf.drawText(48, 725, "CÓMO CREAR UN CÓMIC ILUSTRADO CON IA", 'F2', 15.0, 1, 1, 1);
  pdf.drawText(48, 712, "Guía integral en 4 pasos: Del argumento al cómic y audio narrado en Google Gemini", 'F1', 9.0, 0.85, 0.90, 0.98);

  // 2. SECCIÓN: INTRODUCCIÓN AL PROYECTO
  const box1Top = 692;
  const box1W = 540;
  const box1H = 120;
  const box1Bottom = box1Top - box1H;

  pdf.setFillColor(1, 1, 1);
  pdf.setStrokeColor(0.85, 0.88, 0.92);
  pdf.setLineWidth(1);
  pdf.rect(36, box1Bottom, box1W, box1H, true, true);

  let curY = box1Top - 15;
  pdf.drawText(50, curY, "PROYECTO: TU CÓMIC FAMILIAR EN 4 PASOS DIRECTOS", 'F2', 10.0, 0.06, 0.09, 0.16);
  curY -= 13;

  const introText1 = "Creamos un auténtico cómic infantil ilustrado para nuestros nietos o familia sin necesidad de dibujar. Diseñamos el guion en viñetas y diálogos, y generamos las láminas de cómic y el audio narrado con voces interpretadas en Google Gemini.";
  const wrappedIntro1 = wrapText(introText1, 95);
  for (const line of wrappedIntro1) {
    pdf.drawText(50, curY, line, 'F1', 8.5, 0.25, 0.28, 0.35);
    curY -= 11.0;
  }

  curY -= 2;
  const stepsList = [
    "• Paso 1 (Google Gemini): Diseñas el argumento y personajes adaptados a la edad del niño.",
    "• Paso 2 (Google Gemini): Conviertes la historia en guion de cómic de 6 páginas con 3 viñetas y diálogos.",
    "• Paso 3 (Google Gemini): Creas la presentación de cómic en cuadrículas con bocadillos estilo 3D.",
    "• Paso 4 (Google Gemini): Generas el audio en modo radioteatro arrancando con «Érase una vez...»."
  ];
  for (const step of stepsList) {
    pdf.drawText(50, curY, step, 'F1', 8.2, 0.20, 0.23, 0.30);
    curY -= 10.5;
  }

  // 3. SECCIÓN: PASO 1 (CREAR EL CUADERNO Y EL ARGUMENTO)
  let paso1Top = box1Bottom - 10;
  pdf.setFillColor(0.15, 0.23, 0.36);
  pdf.rect(36, paso1Top - 20, 540, 20, true, false);
  pdf.drawText(50, paso1Top - 15, "PASO 1: CREAR EL CUADERNO «CUENTOS» Y EL ARGUMENTO EN GOOGLE GEMINI", 'F2', 9.5, 1, 1, 1);

  curY = paso1Top - 32;
  const paso1Desc = "1. Abre Google Gemini y crea un nuevo chat o cuaderno llamado «CUENTOS».\n" +
                    "2. Pega este prompt: Gemini redactará el argumento con valores y personajes según la edad del niño.";
  const linesPaso1Desc = paso1Desc.split('\n');
  for (const line of linesPaso1Desc) {
    pdf.drawText(36, curY, line, 'F1', 8.4, 0.22, 0.25, 0.32);
    curY -= 11.0;
  }

  // Caja de Prompt Paso 1
  curY -= 3;
  const promptBoxH = 136;
  const promptBoxBottom = curY - promptBoxH;
  pdf.setFillColor(0.08, 0.11, 0.18);
  pdf.setStrokeColor(0.25, 0.35, 0.50);
  pdf.setLineWidth(1);
  pdf.rect(36, promptBoxBottom, 540, promptBoxH, true, true);

  pdf.drawText(50, curY - 14, "COPIA Y PEGA ESTE PROMPT EN TU CUADERNO «CUENTOS» DE GEMINI:", 'F5', 8.5, 0.22, 0.74, 0.97);

  const prompt1Content = 
`Actúa como un guionista de cómics infantiles profesional.
Escribe el argumento y personajes para un cómic de aventuras familiares sobre:
"El Viaje en Globo del Abuelo y la Gata Luna" (o el tema que elijas).

DATOS OBLIGATORIOS PARA LA HISTORIA:
1. EDAD DEL NIÑO: Este cómic es para un niño de [indica edad, ej: 6] años.
   Ajusta estrictamente el vocabulario, la ternura y la madurez a su nivel.
2. VALORES: Debe transmitir curiosidad, aventura, confianza mutua y cariño.
3. TONO: Muy visual, ágil, con diálogos expresivos y final reconfortante y feliz.`;

  const linesPrompt1 = prompt1Content.split('\n');
  let p1Y = curY - 27;
  for (const l of linesPrompt1) {
    pdf.drawText(50, p1Y, l, 'F4', 7.8, 0.92, 0.95, 1.0);
    p1Y -= 9.5;
  }

  // 4. NUEVA SECCIÓN DIDÁCTICA: NOVEDADES EN GOOGLE GEMINI (CREAR NOTA, WEB Y FAST RESEARCH)
  const nlmTop = promptBoxBottom - 10;
  pdf.setFillColor(0.02, 0.44, 0.55);
  pdf.rect(36, nlmTop - 20, 540, 20, true, false);
  pdf.drawText(50, nlmTop - 15, "GOOGLE GEMINI: CÓMO AÑADIR TUS FUENTES («CREAR NOTA», «WEB» Y «FAST RESEARCH»)", 'F2', 9.5, 1, 1, 1);

  const nlmBoxH = 118;
  const nlmBoxBottom = nlmTop - 20 - nlmBoxH;
  pdf.setFillColor(1, 1, 1);
  pdf.setStrokeColor(0.75, 0.85, 0.92);
  pdf.setLineWidth(1);
  pdf.rect(36, nlmBoxBottom, 540, nlmBoxH, true, true);

  let nlmY = nlmTop - 34;

  // 1. Crear nota
  pdf.drawText(48, nlmY, "1. BOTÓN «+ CREAR NOTA» (Add Note):", 'F2', 8.8, 0.05, 0.40, 0.50);
  nlmY -= 11.0;
  const tNota = "Permite escribir o pegar texto directamente en Google Gemini sin subir ningún archivo desde el ordenador. Sirve para guardar el guion del cómic, tus propias ideas o notas de trabajo. Es una fuente viva e interna editable.";
  for (const l of wrapText(tNota, 98)) {
    pdf.drawText(48, nlmY, l, 'F1', 8.0, 0.25, 0.28, 0.35);
    nlmY -= 10.0;
  }

  // 2. Desplegable Web
  nlmY -= 2;
  pdf.drawText(48, nlmY, "2. DESPLEGABLE «WEB» (Enlaces URL y Vídeos de YouTube):", 'F2', 8.8, 0.05, 0.40, 0.50);
  nlmY -= 11.0;
  const tWeb = "Permite pegar cualquier enlace de una página web, blog o vídeo de YouTube. Google Gemini descarga el texto o transcribe el audio del vídeo automáticamente y lo convierte en fuente de consulta en segundos.";
  for (const l of wrapText(tWeb, 98)) {
    pdf.drawText(48, nlmY, l, 'F1', 8.0, 0.25, 0.28, 0.35);
    nlmY -= 10.0;
  }

  // 3. Desplegable Fast Research
  nlmY -= 2;
  pdf.drawText(48, nlmY, "3. DESPLEGABLE «FAST RESEARCH» (Investigación Rápida con IA):", 'F2', 8.8, 0.05, 0.40, 0.50);
  nlmY -= 11.0;
  const tFast = "Escribes un tema o pregunta clave (ej. «curiosidades sobre globos aerostáticos») y la IA rastrea la web, selecciona fuentes fiables y las añade al cuaderno automáticamente sin que tengas que buscar tú en Google.";
  for (const l of wrapText(tFast, 98)) {
    pdf.drawText(48, nlmY, l, 'F1', 8.0, 0.25, 0.28, 0.35);
    nlmY -= 10.0;
  }

  // 5. CAJA DE OPCIÓN ALTERNATIVA (HISTORIA PROPIA)
  const altTop = nlmBoxBottom - 8;
  const altBoxH = 46;
  const altBottom = altTop - altBoxH;

  pdf.setFillColor(0.97, 0.98, 1.0);
  pdf.setStrokeColor(0.85, 0.88, 0.95);
  pdf.rect(36, altBottom, 540, altBoxH, true, true);

  pdf.drawText(48, altTop - 13, "OPCIÓN ALTERNATIVA (Si ya tienes una historia propia escrita):", 'F2', 8.2, 0.45, 0.25, 0.85);
  
  const notaAlt = "Usa el botón «+ Crear nota» en Google Gemini y pega tu historia directa, o pídele: «Te pego mi historia: adáptala a cómic para un niño de [X] años manteniendo el argumento y resaltando diálogos entre personajes.»";
  const wrappedAlt = wrapText(notaAlt, 99);
  
  let altTextY = altTop - 24;
  for (const l of wrappedAlt) {
    pdf.drawText(48, altTextY, l, 'F1', 7.8, 0.30, 0.33, 0.40);
    altTextY -= 9.5;
  }

  // Pie de página 1
  pdf.setStrokeColor(0.80, 0.83, 0.88);
  pdf.setLineWidth(0.8);
  pdf.line(36, 42, 576, 42);
  pdf.drawText(36, 30, "Curso de Inteligencia Artificial • Monográfico 3: Cómic Ilustrado", 'F1', 8.0, 0.50, 0.55, 0.62);
  pdf.drawText(530, 30, "Página 1 de 2", 'F2', 8.0, 0.50, 0.55, 0.62);

  pdf.endPage();

  // =========================================================================
  // PÁGINA 2: PASO 2 (GUIÓN EN VIÑETAS) + PASO 3 (PRESENTACIÓN CÓMIC REAL)
  // =========================================================================
  pdf.startPage();

  // Fondo sutil de página
  pdf.setFillColor(0.985, 0.988, 0.995);
  pdf.rect(0, 0, 612, 792, true, false);

  // Cabecera compacta página 2
  pdf.setFillColor(0.06, 0.09, 0.16);
  pdf.rect(36, 736, 540, 26, true, false);
  pdf.drawText(48, 746, "MONOGRÁFICO 3: CÓMIC ILUSTRADO CON IA  •  PASOS 2, 3 Y 4", 'F2', 9.5, 1, 1, 1);
  pdf.drawText(470, 746, "GUÍA DIDÁCTICA", 'F5', 8.5, 0.22, 0.74, 0.97);

  // 1. SECCIÓN: PASO 2 (GUIÓN DE CÓMIC CON VIÑETAS Y DIÁLOGOS)
  curY = 726;
  pdf.setFillColor(0.45, 0.22, 0.78);
  pdf.rect(36, curY - 20, 540, 20, true, false);
  pdf.drawText(50, curY - 15, "PASO 2: CONVERTIR EL CUENTO EN GUION DE CÓMIC CON VIÑETAS (En Gemini)", 'F2', 9.8, 1, 1, 1);

  curY -= 32;
  const paso2Desc = "En la misma conversación de Gemini dentro de «CUENTOS», pega este segundo prompt para transformar la historia en un guion de 6 páginas con 3 viñetas secuenciales y diálogos directos:";
  const wrappedPaso2 = wrapText(paso2Desc, 96);
  for (const line of wrappedPaso2) {
    pdf.drawText(36, curY, line, 'F1', 8.8, 0.22, 0.25, 0.32);
    curY -= 11.5;
  }

  // Caja Prompt Paso 2
  curY -= 4;
  const prompt2BoxH = 152;
  pdf.setFillColor(0.08, 0.11, 0.18);
  pdf.setStrokeColor(0.40, 0.30, 0.60);
  pdf.setLineWidth(1);
  pdf.rect(36, curY - prompt2BoxH, 540, prompt2BoxH, true, true);

  pdf.drawText(50, curY - 14, "PEGA ESTE SEGUNDO PROMPT EN LA MISMA CONVERSACIÓN DE GEMINI:", 'F5', 8.5, 0.75, 0.55, 0.98);

  const prompt2Content =
`Toma la historia anterior y crea el GUION DE UN CÓMIC REAL de 6 PÁGINAS.
Cada página debe tener 3 VIÑETAS secuenciales con acción y DIÁLOGOS DIRECTOS:

Para cada una de las 6 páginas ([PÁGINA 1] a [PÁGINA 6]), desglosa:
- [PÁGINA X: TÍTULO DE LA PÁGINA]
  * VIÑETA 1: Escena visual (acción, decorado) + BOCADILLOS DE DIÁLOGO:
    - Abuelo: "..." (su frase en bocadillo).
    - Luna: "..." (su maullido o pensamiento expresivo).
  * VIÑETA 2: Escena visual (giro o avance) + DIÁLOGOS DE PERSONAJES.
  * VIÑETA 3: Escena visual (cierre de página) + DIÁLOGOS DE PERSONAJES.

REGLA: Personajes idénticos (Abuelo suéter verde, Gata Luna blanca) y cero teoría.
Genera ahora el guion completo de cómic en viñetas con diálogos.`;

  const linesPrompt2 = prompt2Content.split('\n');
  let p2Y = curY - 26;
  for (const l of linesPrompt2) {
    pdf.drawText(50, p2Y, l, 'F4', 7.8, 0.92, 0.95, 1.0);
    p2Y -= 9.5;
  }

  // 2. SECCIÓN: PASO 3 (PRESENTACIÓN DE CÓMIC MULTI-VIÑETA EN GOOGLE GEMINI)
  curY = curY - prompt2BoxH - 12;
  pdf.setFillColor(0.05, 0.55, 0.40);
  pdf.rect(36, curY - 20, 540, 20, true, false);
  pdf.drawText(50, curY - 15, "PASO 3: GENERAR LA PRESENTACIÓN DE CÓMIC MULTI-VIÑETA (En Google Gemini)", 'F2', 9.8, 1, 1, 1);

  curY -= 32;
  const paso3Desc = "En Google Gemini abre tu cuaderno «CUENTOS», pulsa «Presentación» y pega este prompt: obligará a crear las 6 páginas de cómic en cuadrículas de 3 viñetas con bocadillos (sin resúmenes):";
  const linesPaso3 = wrapText(paso3Desc, 96);
  for (const l of linesPaso3) {
    pdf.drawText(36, curY, l, 'F1', 8.8, 0.22, 0.25, 0.32);
    curY -= 11.5;
  }

  // Caja Prompt Paso 3 (Formato Cómic Multi-Viñeta)
  curY -= 4;
  const prompt3BoxH = 142;
  pdf.setFillColor(0.08, 0.11, 0.18);
  pdf.setStrokeColor(0.15, 0.50, 0.40);
  pdf.setLineWidth(1);
  pdf.rect(36, curY - prompt3BoxH, 540, prompt3BoxH, true, true);

  pdf.drawText(50, curY - 14, "PROMPT FINAL PARA LA PRESENTACIÓN EN GOOGLE GEMINI (COPIAR Y PEGAR):", 'F5', 8.5, 0.30, 0.85, 0.65);

  const prompt3Content =
`Crea una presentación que sea un CÓMIC ILUSTRADO de 6 diapositivas (1 por página).
Cada diapositiva debe ser una PÁGINA DE CÓMIC dividida en 3 VIÑETAS (panels):

REGLAS OBLIGATORIAS DE CÓMIC REAL:
1. FORMATO MULTI-VIÑETA: Cada diapositiva muestra una cuadrícula de 3 viñetas.
2. BOCADILLOS DE DIÁLOGO: En cada viñeta, incluye los bocadillos con los diálogos
   directos entre los personajes (ej. Abuelo: "...", Luna: "..."). NO texto al pie.
3. ESTILO VISUAL: Ilustración dinámica tipo cómic moderno en 3D Pixar, color cálido,
   expresiones vivas y vestimenta idéntica del abuelo y la gata en todas las viñetas.
4. PROHIBICIÓN: Cero diapositivas de análisis, ni gráficos ni teoría corporativa.

Genera ahora el cómic completo de 6 páginas con viñetas y bocadillos.`;

  const linesPrompt3 = prompt3Content.split('\n');
  let p3Y = curY - 26;
  for (const l of linesPrompt3) {
    pdf.drawText(50, p3Y, l, 'F4', 7.8, 0.92, 0.95, 1.0);
    p3Y -= 9.5;
  }

  // 3. SECCIÓN: PASO 4 (AUDIO NARRADO DIRECTO SIN INTRODUCCIONES)
  curY = curY - prompt3BoxH - 12;
  pdf.setFillColor(0.85, 0.45, 0.08);
  pdf.rect(36, curY - 20, 540, 20, true, false);
  pdf.drawText(50, curY - 15, "PASO 4: GENERAR EL AUDIO EN MODO RADIOTEATRO (En Google Gemini)", 'F2', 9.8, 1, 1, 1);

  curY -= 32;
  const paso4Desc = "Junto a «Generar Audio», pulsa Personalizar (icono de lápiz ✏️) y pega este prompt: anula el modo podcast/presentación y fuerza a las dos voces a actuar como personajes del cuento:";
  const linesPaso4 = wrapText(paso4Desc, 96);
  for (const l of linesPaso4) {
    pdf.drawText(36, curY, l, 'F1', 8.8, 0.22, 0.25, 0.32);
    curY -= 11.5;
  }

  // Caja Prompt Paso 4 (Audio Prompt)
  curY -= 4;
  const prompt4BoxH = 112;
  pdf.setFillColor(0.08, 0.11, 0.18);
  pdf.setStrokeColor(0.85, 0.50, 0.15);
  pdf.setLineWidth(1);
  pdf.rect(36, curY - prompt4BoxH, 540, prompt4BoxH, true, true);

  pdf.drawText(50, curY - 14, "PROMPT PARA EL BOTÓN PERSONALIZAR (LÁPIZ ✏️) DE AUDIO EN GOOGLE GEMINI:", 'F5', 8.5, 0.98, 0.70, 0.25);

  const prompt4Content =
`MODO RADIOTEATRO / AUDIOLIBRO INFANTIL EN VIVO (CERO FORMATO PODCAST).

PROHIBICIONES ESTRICTAS:
1. Queda terminantemente prohibido hablar como presentadores de podcast o locutores.
2. No saludéis, no deis la bienvenida ni expliquéis de qué trata este documento.
3. Cero resúmenes, cero análisis corporativo y cero opiniones de adultos.

ASIGNACIÓN DE ROLES DRAMÁTICOS:
- Locutora femenina: Eres la NARRADORA (voz dulce) y haces la voz traviesa de la Gata Luna.
- Locutor masculino: Eres el ABUELO (voz cariñosa, sabia y entusiasta).

ARRANQUE DIRECTO: La locutora DEBE arrancar diciendo inmediatamente: "Érase una vez...".
Actuad e interpretad la historia directamente viñeta a viñeta con ternura.`;

  const linesPrompt4 = prompt4Content.split('\n');
  let p4Y = curY - 26;
  for (const l of linesPrompt4) {
    pdf.drawText(50, p4Y, l, 'F4', 7.5, 0.92, 0.95, 1.0);
    p4Y -= 9.0;
  }

  // Pie de página 2
  pdf.setStrokeColor(0.80, 0.83, 0.88);
  pdf.setLineWidth(0.8);
  pdf.line(36, 42, 576, 42);
  pdf.drawText(36, 30, "Curso de Inteligencia Artificial • Monográfico 3: Cómic Ilustrado", 'F1', 8.0, 0.50, 0.55, 0.62);
  pdf.drawText(530, 30, "Página 2 de 2", 'F2', 8.0, 0.50, 0.55, 0.62);

  pdf.endPage();

  pdf.writeToFile(OUTPUT_PDF_1);
  pdf.writeToFile(OUTPUT_PDF_2);
}

buildPdf();
