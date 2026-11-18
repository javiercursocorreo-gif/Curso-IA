#!/usr/bin/env node
/**
 * build_sesion_07_info_maps.js
 * Genera la Ficha Didáctica Oficial INFO-007:
 * 1. INFO-007_Google_Maps_y_Rutas_Interactivas_con_IA.pdf
 * Calibración tipográfica y espacial con tipografía WinAnsi, tildes y eñes impecables.
 */

const fs = require('fs');
const path = require('path');

const BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA";
const S07_DIR = path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/07_Sesion");
const B15_DIR = path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/15. [INFO] BLOQUE_15_INFOGRAFIAS_Y_NOVEDADES_IA/Lote_01_al_20");

const S07_PDF = path.join(S07_DIR, "1. INFO-007_Google_Maps_y_Rutas_Interactivas_con_IA.pdf");
const B15_PDF = path.join(B15_DIR, "INFO-007_Google_Maps_y_Rutas_Interactivas_con_IA.pdf");

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
    if (!trimmed) continue;
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
    let curObjIdx = 6;

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
      Buffer.from('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>', 'ascii')
    ];

    for (let i = 0; i < this.pages.length; i++) {
      const contentIdx = contentObjIndices[i];
      const pObj = Buffer.from(
        `<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${this.w} ${this.h}] ` +
        `/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> ` +
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
  }
}

function buildInfo007Pdf() {
  const pdf = new NativePDFWriter();
  pdf.startPage();

  // 1. Marco exterior y fondo suave
  pdf.setFillColor(0.985, 0.992, 1.0);
  pdf.setStrokeColor(0.12, 0.40, 0.80);
  pdf.setLineWidth(1.5);
  pdf.rect(20, 20, 572, 752, true, true);

  // 2. Cabecera institucional
  pdf.setFillColor(0.06, 0.16, 0.35);
  pdf.rect(24, 716, 564, 52, true, false);
  pdf.drawText(36, 750, 'SESIÓN 07 • FICHA DIDÁCTICA DE INNOVACIÓN [INFO-007]', 'F2', 8.5, 0.4, 0.8, 1.0);
  pdf.drawText(36, 730, 'Google Maps con IA: De un Plano Pasivo a tu Copiloto de Viajes', 'F2', 13.0, 1.0, 1.0, 1.0);

  // =========================================================================
  // BLOQUE 1: LA GRAN NOVEDAD Y LA DIFERENCIA DIDÁCTICA (y = 535 a 705)
  // =========================================================================
  pdf.setFillColor(0.94, 0.97, 1.0);
  pdf.setStrokeColor(0.18, 0.48, 0.82);
  pdf.setLineWidth(1.0);
  pdf.rect(30, 535, 552, 170, true, true);

  pdf.drawText(42, 690, '1. LA GRAN NOVEDAD: GOOGLE ABRE LA CARTOGRAFÍA REAL A LA INTELIGENCIA ARTIFICIAL', 'F2', 9.0, 0.08, 0.25, 0.55);

  const t1 = "Google ha integrado la inmensa base de datos de Google Maps (más de 300 millones de lugares, comercios, horarios reales y opiniones verificadas) directamente dentro de sus modelos de inteligencia artificial (Gemini). Ahora la IA ya no 'alucina' inventándose calles ni itinerarios ficticios: dispone de telemetría cartográfica y espacial en tiempo real.";
  const linesT1 = wrapText(t1, 114);
  let y1 = 676;
  for (const l of linesT1) {
    pdf.drawText(42, y1, l, 'F1', 7.7, 0.15, 0.20, 0.25);
    y1 -= 11.0;
  }

  // Recuadro interior: Reto Pedagógico (alto 96, y = 543 a 639)
  pdf.setFillColor(1.0, 0.965, 0.90);
  pdf.setStrokeColor(0.85, 0.50, 0.10);
  pdf.setLineWidth(0.8);
  pdf.rect(38, 543, 536, 96, true, true);

  pdf.drawText(46, 626, 'LA LECCIÓN CLAVE DEL AULA: "DIBUJO ESQUEMÁTICO" VS "DATO CARTOGRÁFICO REAL"', 'F2', 8.0, 0.75, 0.30, 0.05);

  const b1 = "• Si solo pides un 'mapa en pantalla', Gemini Canvas suele pintar un dibujo vectorial esquemático (como un plano turístico infantil con iconos de catedral o río). Es vistoso, pero no es Google Maps: no permite ampliar calles ni ver comercios reales.";
  const b2 = "• Para que la IA sea un verdadero copiloto de viaje, debemos exigir la conexión cartográfica real mediante dos métodos probados que veremos a continuación: la tarjeta oficial de Google Maps o un visor interactivo de calles con satélite y zoom.";
  
  let yB = 612;
  for (const l of wrapText(b1, 112)) {
    pdf.drawText(46, yB, l, 'F1', 7.3, 0.20, 0.15, 0.05);
    yB -= 10.0;
  }
  yB -= 3;
  for (const l of wrapText(b2, 112)) {
    pdf.drawText(46, yB, l, 'F1', 7.3, 0.20, 0.15, 0.05);
    yB -= 10.0;
  }

  // =========================================================================
  // BLOQUE 2: EJERCICIO PRÁCTICO 1 (CHAT DIRECTO CON TARJETA DE GOOGLE MAPS) (y = 345 a 523)
  // =========================================================================
  pdf.setFillColor(0.96, 0.985, 1.0);
  pdf.setStrokeColor(0.15, 0.45, 0.80);
  pdf.setLineWidth(1.0);
  pdf.rect(30, 345, 552, 178, true, true);

  pdf.drawText(42, 508, '2. EJERCICIO PRÁCTICO 1: LA RUTA OFICIAL EN EL CHAT DIRECTO DE GEMINI', 'F2', 9.0, 0.08, 0.25, 0.55);

  const e1Desc = "En el chat habitual de Gemini (sin entrar en Canvas), activamos la extensión oficial de Maps para que nos entregue la ruta real con tiempos a pie y el botón para abrir la navegación asistida por voz en nuestro teléfono móvil:";
  let yE1 = 494;
  for (const l of wrapText(e1Desc, 114)) {
    pdf.drawText(42, yE1, l, 'F1', 7.6, 0.15, 0.20, 0.25);
    yE1 -= 10.5;
  }

  // Caja de prompt oscuro estilo código (y = 380 a 468, alto 88)
  pdf.setFillColor(0.05, 0.09, 0.18);
  pdf.setStrokeColor(0.20, 0.40, 0.70);
  pdf.setLineWidth(0.8);
  pdf.rect(38, 380, 536, 88, true, true);

  pdf.drawText(46, 454, 'PROMPT EXACTO PARA COPIAR EN EL CHAT DE GEMINI:', 'F2', 7.5, 0.35, 0.75, 1.0);
  const p1 = "@Google Maps Diseña una ruta a pie de 1 hora por Segovia entre el Acueducto, la Plaza Mayor y el Alcázar, evitando cuestas empinadas y con paradas llanas de descanso. Muestra la ruta oficial sobre el mapa de Google Maps con distancias reales, tiempos a pie y enlaces para abrir la navegación guiada en el móvil.";
  let yP1 = 438;
  for (const l of wrapText(p1, 108)) {
    pdf.drawText(46, yP1, l, 'F1', 7.4, 0.95, 0.95, 0.95);
    yP1 -= 11.0;
  }

  // Píldora de resultado
  pdf.setFillColor(0.90, 0.96, 0.90);
  pdf.rect(38, 353, 536, 20, true, false);
  pdf.drawText(44, 359, 'QUÉ OBTENDRÁS: La tarjeta oficial interactiva de Google Maps con fotos reales y el botón "Abrir en Maps" en tu smartphone.', 'F2', 7.1, 0.05, 0.40, 0.15);

  // =========================================================================
  // BLOQUE 3: EJERCICIO PRÁCTICO 2 (VISOR CARTOGRÁFICO REAL EN CANVAS) (y = 145 a 333)
  // =========================================================================
  pdf.setFillColor(0.985, 0.985, 0.95);
  pdf.setStrokeColor(0.80, 0.50, 0.10);
  pdf.setLineWidth(1.0);
  pdf.rect(30, 145, 552, 188, true, true);

  pdf.drawText(42, 318, '3. EJERCICIO PRÁCTICO 2: EL VISOR CARTOGRÁFICO REAL NAVEGABLE EN CANVAS', 'F2', 9.0, 0.70, 0.30, 0.05);

  const e2Desc = "Si queremos que en pantalla nazca una aplicación interactiva donde podamos hacer zoom con el ratón, explorar calles reales y pulsar marcadores con consejos de salud (prohibiéndole expresamente que dibuje planos esquemáticos falsos):";
  let yE2 = 304;
  for (const l of wrapText(e2Desc, 114)) {
    pdf.drawText(42, yE2, l, 'F1', 7.6, 0.15, 0.20, 0.25);
    yE2 -= 10.5;
  }

  // Caja de prompt Canvas (y = 180 a 278, alto 98)
  pdf.setFillColor(0.05, 0.09, 0.18);
  pdf.setStrokeColor(0.85, 0.55, 0.15);
  pdf.setLineWidth(0.8);
  pdf.rect(38, 180, 536, 98, true, true);

  pdf.drawText(46, 264, 'PROMPT DE VISUALIZACIÓN DIRECTA PARA CANVAS / VISTA PREVIA:', 'F2', 7.5, 1.0, 0.70, 0.20);
  const p2 = "Diseña y ejecuta directamente en pantalla (en modo vista previa interactiva / Canvas) un mapa interactivo real sobre Segovia. NO dibujes gráficos vectoriales ni esquemas ficticios; utiliza un visor cartográfico real interactivo (como Leaflet / OpenStreetMap) centrado en Segovia, con controles de zoom, capa de calles reales y 4 marcadores interactivos pulsables (Acueducto, Plaza Mayor, Catedral y Alcázar) que al tocarlos muestren consejos de accesibilidad para mayores.";
  let yP2 = 248;
  for (const l of wrapText(p2, 108)) {
    pdf.drawText(46, yP2, l, 'F1', 7.4, 0.95, 0.95, 0.95);
    yP2 -= 11.0;
  }

  // Píldora de resultado
  pdf.setFillColor(0.99, 0.94, 0.88);
  pdf.rect(38, 153, 536, 20, true, false);
  pdf.drawText(44, 159, 'QUÉ OBTENDRÁS: Un visor cartográfico real con botones de zoom (+/-), calles auténticas y fichas desplegables de salud.', 'F2', 7.1, 0.60, 0.25, 0.05);

  // =========================================================================
  // PIE DE PÁGINA INSTITUCIONAL (y = 100 a 130)
  // =========================================================================
  pdf.setStrokeColor(0.8, 0.85, 0.9);
  pdf.line(30, 132, 582, 132);
  pdf.drawText(36, 116, 'CURSO DE INTELIGENCIA ARTIFICIAL PARA MAYORES (60+) • SESIÓN 07 • MAPAS INTERACTIVOS CON IA [INFO-007]', 'F2', 7.4, 0.15, 0.35, 0.55);
  pdf.drawText(36, 102, 'Herramientas Oficiales: Gemini (gemini.google.com) & Google Maps • Metodología: Cero Código y Visualización Directa', 'F3', 7.0, 0.45, 0.45, 0.55);

  pdf.endPage();

  pdf.writeToFile(S07_PDF);
  console.log(`✅ Ficha INFO-007 generada en Sesión 07: ${S07_PDF}`);

  pdf.writeToFile(B15_PDF);
  console.log(`✅ Ficha INFO-007 generada en Bloque 15: ${B15_PDF}`);
}

buildInfo007Pdf();
