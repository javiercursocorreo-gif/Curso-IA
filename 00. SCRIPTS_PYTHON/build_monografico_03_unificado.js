#!/usr/bin/env node
/**
 * build_monografico_03_unificado.js
 * Genera el documento único simplificado para el Monográfico 3:
 * "MONOGRAFICO_3_COMO_CREAR_UN_CUENTO_ILUSTRADO_CON_IA.pdf"
 * 
 * Unifica en una sola guía didáctica de 2 páginas:
 * 1. Introducción al proyecto.
 * 2. Paso 1: Crear el cuento en Gemini + Prompt.
 * 3. Paso 2: Generar el guion de 10 escenas en Gemini + Prompt.
 * 4. Paso 3: Llevarlo a NotebookLM (donde ya encontrarán el cuaderno) + Prompt de arte 3D.
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

  roundedRect(x, y, width, height, radius = 4, fill = true, stroke = true) {
    // Aproximación con rectángulo para compatibilidad limpia de stream
    this.rect(x, y, width, height, fill, stroke);
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
    console.log(`[PDF] Generado con exito: ${filename} (${this.pages.length} pags)`);
  }
}

function buildPdf() {
  const pdf = new NativePDFWriter(612, 792);

  // =========================================================================
  // PÁGINA 1: INTRODUCCIÓN AL PROYECTO + PASO 1 (CREAR EL CUENTO)
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
  pdf.setFillColor(0.22, 0.74, 0.97); // #38bdf8
  pdf.drawText(48, 744, "CURSO DE INTELIGENCIA ARTIFICIAL  -  MONOGRAFICO 3", 'F2', 8.5, 0.22, 0.74, 0.97);

  // Título Principal
  pdf.drawText(48, 725, "COMO CREAR UN CUENTO ILUSTRADO CON IA", 'F2', 15.5, 1, 1, 1);
  pdf.drawText(48, 712, "Guia integral en 3 pasos: De la idea en Gemini a la presentacion visual en NotebookLM", 'F1', 9.0, 0.85, 0.90, 0.98);

  // 2. SECCIÓN: INTRODUCCIÓN AL PROYECTO
  let curY = 690;
  pdf.setFillColor(1, 1, 1);
  pdf.setStrokeColor(0.85, 0.88, 0.92);
  pdf.setLineWidth(1);
  pdf.rect(36, 580, 540, 114, true, true);

  // Título sección Intro
  pdf.setFillColor(0.06, 0.09, 0.16);
  pdf.drawText(50, 674, "PROYECTO: TU CUENTO FAMILIAR EN 3 PASOS DIRECTOS", 'F2', 11, 0.06, 0.09, 0.16);

  const introText1 = "El objetivo de este proyecto es crear un cuento infantil ilustrado para nuestros nietos o familia sin necesidad de dibujar ni programar. Unimos la capacidad de redaccion de Google Gemini con el poder visual de NotebookLM para lograr un resultado entrañable, profesional y con personajes consistentes.";
  const wrappedIntro1 = wrapText(introText1, 94);
  let textY = 658;
  for (const line of wrappedIntro1) {
    pdf.drawText(50, textY, line, 'F1', 9.2, 0.25, 0.28, 0.35);
    textY -= 13;
  }

  // Las 3 fases explicadas
  pdf.drawText(50, 626, "Flujo unificado sin saltar entre archivos:", 'F2', 9.2, 0.55, 0.36, 0.96);
  pdf.drawText(50, 612, "1. PASO 1 (Gemini): Redactas el cuento adaptado a la edad con valores positivos.", 'F1', 9.0, 0.20, 0.23, 0.30);
  pdf.drawText(50, 599, "2. PASO 2 (Gemini): Transformas el cuento en un guion estructurado de 10 escenas.", 'F1', 9.0, 0.20, 0.23, 0.30);
  pdf.drawText(50, 586, "3. PASO 3 (NotebookLM): Llevas el guion a tu cuaderno para generar la presentacion visual en 3D.", 'F1', 9.0, 0.20, 0.23, 0.30);

  // 3. SECCIÓN: PASO 1 (CREAR EL CUENTO)
  curY = 566;
  pdf.setFillColor(0.15, 0.23, 0.36); // #2563eb / navy
  pdf.rect(36, curY - 24, 540, 24, true, false);
  pdf.drawText(50, curY - 17, "PASO 1: CREAR EL CUENTO EN GOOGLE GEMINI", 'F2', 11, 1, 1, 1);

  // Explicación de lo que hace el paso
  curY -= 40;
  pdf.setFillColor(0.06, 0.09, 0.16);
  pdf.drawText(36, curY, "Que hace este paso:", 'F2', 10, 0.06, 0.09, 0.16);
  
  curY -= 14;
  const paso1Desc = "Abre una conversacion con Google Gemini (gemini.google.com). Copia el prompt que tienes debajo y pegalo en el chat. Gemini actuara como un cuentacuentos profesional: ajustara el lenguaje a la edad del niño, transmitira valores positivos y cerrara con un final reconfortante para ayudarle a dormir.";
  const wrappedPaso1 = wrapText(paso1Desc, 98);
  for (const line of wrappedPaso1) {
    pdf.drawText(36, curY, line, 'F1', 9.2, 0.22, 0.25, 0.32);
    curY -= 13;
  }

  // Caja de Prompt Paso 1
  curY -= 6;
  const promptBoxH = 175;
  pdf.setFillColor(0.08, 0.11, 0.18); // #141c2e pizarra oscura
  pdf.setStrokeColor(0.25, 0.35, 0.50);
  pdf.setLineWidth(1);
  pdf.rect(36, curY - promptBoxH, 540, promptBoxH, true, true);

  // Etiqueta Prompt
  pdf.setFillColor(0.22, 0.74, 0.97);
  pdf.drawText(50, curY - 18, "COPIA Y PEGA ESTE PROMPT EN GOOGLE GEMINI:", 'F5', 9.0, 0.22, 0.74, 0.97);

  const prompt1Content = 
`Actua como un cuentacuentos infantil profesional.
Escribe un cuento de buenas noches de 3 o 4 parrafos sobre:
"El Viaje en Globo del Abuelo y la Gata Luna" (o el tema que tu elijas).

DATOS OBLIGATORIOS PARA LA HISTORIA:
1. EDAD DEL NINO: Este cuento es para un nino de [Indica aqui la edad, ej: 6] anos.
   Ajusta estrictamente el vocabulario, la ternura y la madurez a su nivel.
2. VALORES: Debe transmitir de forma sutil valores de curiosidad, aventura
   compartida, confianza mutua y amor a la naturaleza.
3. TONO: Usa un lenguaje visual y atrapante, con un final tranquilo y muy
   reconfortante para que le ayude a conciliar el sueno feliz.`;

  const linesPrompt1 = prompt1Content.split('\n');
  let p1Y = curY - 34;
  for (const l of linesPrompt1) {
    pdf.drawText(50, p1Y, l, 'F4', 8.5, 0.92, 0.95, 1.0);
    p1Y -= 12;
  }

  // Nota alternativa (si el alumno ya tiene su propia historia)
  curY = curY - promptBoxH - 14;
  pdf.setFillColor(1, 1, 1);
  pdf.setStrokeColor(0.85, 0.88, 0.92);
  pdf.rect(36, curY - 50, 540, 50, true, true);

  pdf.drawText(48, curY - 14, "OPCION ALTERNATIVA (Para alumnos con historia propia inventada):", 'F2', 8.5, 0.55, 0.36, 0.96);
  const notaAlt = "Si ya tienes escrito tu cuento, dile a Gemini: 'A continuacion te pego un cuento escrito por mi. Reescribelo manteniendo mi historia exacta pero usando un lenguaje magico, adaptado a un nino de [X] anos y resaltando los valores de aventura y carino.'";
  const wrappedAlt = wrapText(notaAlt, 98);
  let altY = curY - 26;
  for (const l of wrappedAlt) {
    pdf.drawText(48, altY, l, 'F1', 8.5, 0.30, 0.33, 0.40);
    altY -= 11.5;
  }

  // Pie de página 1
  pdf.setStrokeColor(0.80, 0.83, 0.88);
  pdf.setLineWidth(0.8);
  pdf.line(36, 42, 576, 42);
  pdf.drawText(36, 30, "Curso de Inteligencia Artificial - Monografico 3: Cuento Ilustrado", 'F1', 8.0, 0.50, 0.55, 0.62);
  pdf.drawText(530, 30, "Pagina 1 de 2", 'F2', 8.0, 0.50, 0.55, 0.62);

  pdf.endPage();

  // =========================================================================
  // PÁGINA 2: PASO 2 (GUION 10 PÁGINAS) + PASO 3 (NOTEBOOKLM) + CONSEJOS
  // =========================================================================
  pdf.startPage();

  // Fondo sutil de página
  pdf.setFillColor(0.985, 0.988, 0.995);
  pdf.rect(0, 0, 612, 792, true, false);

  // Cabecera compacta página 2
  pdf.setFillColor(0.06, 0.09, 0.16);
  pdf.rect(36, 736, 540, 26, true, false);
  pdf.drawText(48, 746, "MONOGRAFICO 3: CUENTO ILUSTRADO CON IA  -  PASOS 2 Y 3", 'F2', 9.5, 1, 1, 1);
  pdf.drawText(470, 746, "GUIA DIDACTICA", 'F5', 8.5, 0.22, 0.74, 0.97);

  // 1. SECCIÓN: PASO 2 (CONVERTIR EL CUENTO EN GUION DE 10 PÁGINAS)
  curY = 722;
  pdf.setFillColor(0.45, 0.22, 0.78); // Purple #7c3aed
  pdf.rect(36, curY - 22, 540, 22, true, false);
  pdf.drawText(50, curY - 16, "PASO 2: CONVERTIR EL CUENTO EN GUION DE 10 ESCENAS (En Gemini)", 'F2', 10.5, 1, 1, 1);

  curY -= 36;
  pdf.setFillColor(0.06, 0.09, 0.16);
  pdf.drawText(36, curY, "Que hace este paso:", 'F2', 9.5, 0.06, 0.09, 0.16);

  curY -= 13;
  const paso2Desc = "¡IMPORTANTE: No abras un chat nuevo! En la misma conversacion de Gemini donde tienes el cuento recien generado, pega este segundo prompt. Gemini actuara como director audiovisual y dividira la historia en un guion estructurado de 10 escenas/paginas, definiendo el plano, la vestimenta fija de los personajes y los dialogos.";
  const wrappedPaso2 = wrapText(paso2Desc, 98);
  for (const line of wrappedPaso2) {
    pdf.drawText(36, curY, line, 'F1', 8.8, 0.22, 0.25, 0.32);
    curY -= 12;
  }

  // Caja Prompt Paso 2
  curY -= 4;
  const prompt2BoxH = 158;
  pdf.setFillColor(0.08, 0.11, 0.18);
  pdf.setStrokeColor(0.40, 0.30, 0.60);
  pdf.setLineWidth(1);
  pdf.rect(36, curY - prompt2BoxH, 540, prompt2BoxH, true, true);

  pdf.setFillColor(0.75, 0.55, 0.98);
  pdf.drawText(50, curY - 16, "PEGA ESTE SEGUNDO PROMPT EN LA MISMA CONVERSACION DE GEMINI:", 'F5', 8.8, 0.75, 0.55, 0.98);

  const prompt2Content =
`Toma el cuento generado en el mensaje anterior y crea el guion de un comic
secuencial siguiendo estrictamente estas instrucciones:

1. EXTENSION: Debe tener EXACTAMENTE 10 PAGINAS (de [PAGINA 1] a [PAGINA 10]).
2. ESTRUCTURA DE CADA PAGINA:
   - [PAGINA X: TITULO DE LA ESCENA]
   - Resumen narrativo de 1 linea.
   - Escena clave y tipo de plano (General, Plano Medio o Primer Plano).
   - Descripcion visual: que ocurre y que se ve.
     IMPORTANTE: Manten identica la vestimenta, colores y rasgos fisicos
     de los personajes en todas las paginas para garantizar consistencia total.
   - Iluminacion y atmosfera ambiental.
   - Dialogo obligatorio y Pensamiento del personaje.

Transforma ahora el cuento en el guion de 10 paginas completo.`;

  const linesPrompt2 = prompt2Content.split('\n');
  let p2Y = curY - 30;
  for (const l of linesPrompt2) {
    pdf.drawText(50, p2Y, l, 'F4', 8.0, 0.92, 0.95, 1.0);
    p2Y -= 11.2;
  }

  // 2. SECCIÓN: PASO 3 (LLEVAR A NOTEBOOKLM Y GENERAR EL CUENTO VISUAL)
  curY = curY - prompt2BoxH - 16;
  pdf.setFillColor(0.05, 0.55, 0.40); // Emerald #059669
  pdf.rect(36, curY - 22, 540, 22, true, false);
  pdf.drawText(50, curY - 16, "PASO 3: LLEVAR EL GUION A NOTEBOOKLM Y CREAR LA PRESENTACION VISUAL", 'F2', 10.5, 1, 1, 1);

  curY -= 36;
  pdf.setFillColor(0.06, 0.09, 0.16);
  pdf.drawText(36, curY, "Que hace este paso (Tu puente directo a NotebookLM):", 'F2', 9.5, 0.06, 0.09, 0.16);

  curY -= 13;
  const paso3Desc = "1. Abre NotebookLM (notebooklm.google.com) con tu misma cuenta de Google.\n2. ¡Tu cuaderno ya esta listo esperandote! Entra en el cuaderno 'CUENTOS' (si creas uno nuevo, simplemente pulsa '+' y pega el texto del guion de 10 paginas como fuente).\n3. Pulsa el boton 'Presentacion' (o 'Resumen de Audio' si deseas que dos voces lo narren como un podcast) y aplica los parametros visuales que tienes debajo para generar las laminas 3D con máxima calidad.";
  const linesPaso3 = paso3Desc.split('\n');
  for (const l of linesPaso3) {
    const wrapped = wrapText(l, 98);
    for (const w of wrapped) {
      pdf.drawText(36, curY, w, 'F1', 8.8, 0.22, 0.25, 0.32);
      curY -= 12;
    }
  }

  // Caja Prompt Paso 3
  curY -= 4;
  const prompt3BoxH = 142;
  pdf.setFillColor(0.08, 0.11, 0.18);
  pdf.setStrokeColor(0.15, 0.50, 0.40);
  pdf.setLineWidth(1);
  pdf.rect(36, curY - prompt3BoxH, 540, prompt3BoxH, true, true);

  pdf.setFillColor(0.30, 0.85, 0.65);
  pdf.drawText(50, curY - 16, "PARAMETROS VISUALES Y PROMPT FINAL EN NOTEBOOKLM:", 'F5', 8.8, 0.30, 0.85, 0.65);

  const prompt3Content =
`Aplica estrictamente los siguientes parametros para generar la presentacion
visual de este comic basandote en el guion adjunto en las fuentes:

- ESTILO VISUAL: Animacion 3D entranable tipo Pixar (personajes en 3D con
  iluminacion cinematografica calida, texturas suaves y maxima expresividad).
- CONSISTENCIA TOTAL: Manten la apariencia, colores de ropa, edad y rasgos
  de todos los personajes exactamente iguales en todas las laminas.
- MAQUETACION AL 100%: Cada pagina generada debe llenar todo el lienzo visual
  sin dejar huecos en blanco.
Genera ahora la presentacion ilustrada del comic.`;

  const linesPrompt3 = prompt3Content.split('\n');
  let p3Y = curY - 30;
  for (const l of linesPrompt3) {
    pdf.drawText(50, p3Y, l, 'F4', 8.0, 0.92, 0.95, 1.0);
    p3Y -= 11.2;
  }

  // 3. CAJA DE CONSEJOS PRÁCTICOS PARA EL ALUMNO SENIOR
  curY = curY - prompt3BoxH - 12;
  pdf.setFillColor(1, 1, 1);
  pdf.setStrokeColor(0.85, 0.88, 0.92);
  pdf.rect(36, curY - 44, 540, 44, true, true);

  pdf.drawText(48, curY - 13, "CONSEJOS DE ORO PARA DISFRUTAR EL CUENTO:", 'F2', 8.5, 0.06, 0.09, 0.16);
  pdf.drawText(48, curY - 25, "- En la Tablet o iPad: Abre la presentacion en pantalla completa para ensenarsela a los nietos en el sofa.", 'F1', 8.2, 0.30, 0.33, 0.40);
  pdf.drawText(48, curY - 36, "- Audio magico: Si generas el podcast de audio en NotebookLM, ponlo de fondo mientras pasan las paginas.", 'F1', 8.2, 0.30, 0.33, 0.40);

  // Pie de página 2
  pdf.setStrokeColor(0.80, 0.83, 0.88);
  pdf.setLineWidth(0.8);
  pdf.line(36, 42, 576, 42);
  pdf.drawText(36, 30, "Curso de Inteligencia Artificial - Monografico 3: Cuento Ilustrado", 'F1', 8.0, 0.50, 0.55, 0.62);
  pdf.drawText(530, 30, "Pagina 2 de 2", 'F2', 8.0, 0.50, 0.55, 0.62);

  pdf.endPage();

  // Guardar en ambas ubicaciones (en la carpeta del monográfico 3 y en Classroom)
  pdf.writeToFile(OUTPUT_PDF_1);
  pdf.writeToFile(OUTPUT_PDF_2);
}

buildPdf();
