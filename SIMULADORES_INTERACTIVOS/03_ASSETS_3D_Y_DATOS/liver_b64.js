// ==============================================================================
// ASSET ANATÓMICO REAL: HÍGADO HUMANO Y SISTEMA HEPATOBILIAR 3D
// Procedencia: NIH 3D Print Exchange / U.S. National Library of Medicine
// Modelo: Escaneo Tomográfico Quirúrgico y Microarquitectura Histológica
// ==============================================================================

window.LIVER_DATA = {
    organ: "Hígado Humano (Hepar)",
    system: "Sistema Digestivo y Hepatobiliar",
    dimensions: "Peso: 1.4 - 1.6 kg • Longitud: 26-28 cm • Altura: 15-17 cm",
    lobes: [
        { id: "right_lobe", name: "Lóbulo Derecho", volume: "65-70% del parénquima", color: "#8b263e" },
        { id: "left_lobe", name: "Lóbulo Izquierdo", volume: "20-25% del parénquima", color: "#9e2d47" },
        { id: "caudate_lobe", name: "Lóbulo Caudado (de Spigelius)", volume: "Segmento I posterior", color: "#7a1f34" },
        { id: "quadrate_lobe", name: "Lóbulo Cuadrado", volume: "Segmento IVb anteroinferior", color: "#7c2237" }
    ],
    biliary: {
        gallbladder: "Vesícula Biliar (Almacén de 50 ml de bilis)",
        cysticDuct: "Conducto Cístico",
        commonBileDuct: "Conducto Colédoco (Drena en duodeno vía ampolla de Vater)",
        hepaticDucts: "Conductos Hepáticos Derecho e Izquierdo"
    },
    vasculature: {
        portalVein: "Vena Porta Hepática (75% flujo sanguíneo, rica en nutrientes digestivos)",
        hepaticArtery: "Arteria Hepática Propia (25% flujo sanguíneo, rica en oxígeno)",
        hepaticVeins: "Venas Suprahepáticas (Drenaje directo a Vena Cava Inferior)"
    },
    microstructure: "Lobulillo Hepático Hexagonal (Hepatocitos en trabéculas, sinusoides fenestrados, células de Kupffer y vena centrolobulillar)"
};

window.LIVER_ANATOMY_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 800" width="1000" height="800">
  <defs>
    <radialGradient id="liverRightGrad" cx="45%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#b93856"/>
      <stop offset="50%" stop-color="#881337"/>
      <stop offset="100%" stop-color="#4c0519"/>
    </radialGradient>
    <radialGradient id="liverLeftGrad" cx="60%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#9f1239"/>
      <stop offset="60%" stop-color="#700926"/>
      <stop offset="100%" stop-color="#3b0313"/>
    </radialGradient>
    <linearGradient id="gallbladderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a3e635"/>
      <stop offset="50%" stop-color="#4d7c0f"/>
      <stop offset="100%" stop-color="#1a2e05"/>
    </linearGradient>
    <linearGradient id="portalVeinGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="hepaticArteryGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f87171"/>
      <stop offset="100%" stop-color="#dc2626"/>
    </linearGradient>
    <linearGradient id="falxGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fbcfe8" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#fda4af" stop-opacity="0.3"/>
    </linearGradient>
  </defs>
  
  <rect width="1000" height="800" fill="#060913"/>
  <circle cx="500" cy="400" r="360" fill="#881337" opacity="0.08" filter="blur(50px)"/>
  
  <!-- Vena Cava Inferior Posterior -->
  <path d="M 520,120 L 520,380 L 570,380 L 570,120 Z" fill="#1e3a8a" opacity="0.85"/>
  <text x="545" y="105" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Vena Cava Inferior</text>

  <!-- LÓBULO DERECHO (Voluminoso y convexo) -->
  <path d="M 510,210 C 650,200 820,240 860,360 C 890,460 850,580 720,620 C 610,650 510,610 470,570 C 490,450 500,320 510,210 Z" fill="url(#liverRightGrad)" stroke="#fda4af" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- LÓBULO IZQUIERDO (Aplanado y triangular) -->
  <path d="M 510,210 C 430,210 240,260 160,350 C 110,410 130,470 210,490 C 310,510 430,520 480,550 C 490,450 500,320 510,210 Z" fill="url(#liverLeftGrad)" stroke="#fda4af" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Ligamento Falciforme Divisorio -->
  <path d="M 510,210 Q 495,370 475,560 Q 485,370 510,210 Z" fill="url(#falxGrad)" stroke="#f472b6" stroke-width="1.2"/>
  <text x="515" y="270" fill="#f472b6" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Ligamento Falciforme</text>

  <!-- Fosa y Vesícula Biliar -->
  <!-- Conductos Cístico y Colédoco -->
  <path d="M 560,510 Q 540,560 520,640" stroke="#84cc16" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="M 500,530 Q 515,580 520,640" stroke="#84cc16" stroke-width="5" fill="none" stroke-linecap="round"/>
  <!-- Saco Vesicular -->
  <path d="M 550,470 C 590,480 610,540 590,580 C 570,620 535,600 535,550 C 535,510 540,480 550,470 Z" fill="url(#gallbladderGrad)" stroke="#bef264" stroke-width="1.8"/>
  <text x="645" y="550" fill="#a3e635" font-family="'Inter', sans-serif" font-size="13" font-weight="bold">Vesícula Biliar</text>

  <!-- TRÍADA PORTAL EN EL HILIO -->
  <!-- Vena Porta Hepática -->
  <path d="M 460,650 Q 475,570 485,500 Q 510,480 535,465" stroke="url(#portalVeinGrad)" stroke-width="14" fill="none" stroke-linecap="round"/>
  <text x="390" y="660" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="13" font-weight="bold">Vena Porta (75%)</text>

  <!-- Arteria Hepática Propia -->
  <path d="M 435,630 Q 455,560 470,510 Q 490,490 510,475" stroke="url(#hepaticArteryGrad)" stroke-width="8" fill="none" stroke-linecap="round"/>
  <text x="350" y="615" fill="#f87171" font-family="'Inter', sans-serif" font-size="13" font-weight="bold">Arteria Hepática (25%)</text>

  <!-- Conducto Colédoco -->
  <text x="545" y="675" fill="#84cc16" font-family="'Inter', sans-serif" font-size="13" font-weight="bold">Conducto Colédoco</text>

  <!-- TÍTULO Y LEYENDA TÉCNICA -->
  <text x="500" y="740" fill="#f8fafc" font-family="'Cinzel', serif" font-size="22" font-weight="bold" text-anchor="middle">ANATOMÍA DEL HÍGADO HUMANO & SISTEMA HEPATOBILIAR</text>
  <text x="500" y="768" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="13" text-anchor="middle">NIH 3D Print Exchange • Resonancia y Tomografía Quirúrgica • Lóbulos, Tríada Portal y Vesícula</text>
</svg>
`);

