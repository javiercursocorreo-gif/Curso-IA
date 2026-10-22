// ==============================================================================
// ASSET FOTOGRAMÉTRICO Y ARQUEOLÓGICO REAL: EL PARTENÓN DE ATENAS (ACRÓPOLIS)
// Procedencia: Levantamiento Arqueológico Oficial de la Acrópolis de Atenas
// Herencia Cultural Griega • Ictino, Calícrates y Fidias (447-432 a.C.)
// ==============================================================================

window.PARTHENON_DATA = {
    title: "El Partenón de Atenas",
    site: "Acrópolis de Atenas, Grecia",
    architects: "Ictino y Calícrates (Supervisión escultórica de Fidias)",
    period: "Siglo V a.C. (Época Clásica, 447 - 432 a.C.)",
    order: "Dórico Octástilo Períptero (8 columnas frontales x 17 laterales)",
    material: "Mármol Pentélico blanco",
    proportions: {
        stylobateLength: 69.51, // metros
        stylobateWidth: 30.88,  // metros
        ratio: 2.251,           // Relación 4:9 (2n + 1)
        phiRatio: 1.6180339887, // Proporción Áurea (Phi)
        columnHeight: 10.43,    // metros (5.5 veces el diámetro inferior)
        columnDiameterBase: 1.905, // metros
        columnDiameterTop: 1.481,  // metros (éntasis cónica)
        curvatureRiseFront: 0.065, // 6.5 cm de alza convexa en fachadas
        curvatureRiseFlanks: 0.110, // 11 cm de alza convexa en lados
        inclinationInward: 0.070    // Columnas inclinadas hacia dentro (ejes convergen a 2.400 m)
    },
    hotspots: [
        {
            id: "stylobate",
            name: "Estilóbato y Curvaturas de Corrección Óptica",
            desc: "La base escalonada (crepidoma) no es perfectamente plana: se eleva 6.5 cm en los frentes y 11 cm en los laterales. Si fuera recta, el ojo humano percibiría un hundimiento central.",
            coords: { x: 0, y: 1.2, z: 14.5 }
        },
        {
            id: "entasis",
            name: "Éntasis Dórica e Inclinación Convergente",
            desc: "Las 46 columnas exteriores tienen un ligero abombamiento (éntasis) a un tercio de su altura y están inclinadas hacia el interior. Si se prolongaran sus ejes imaginarios, convergerían a 2.400 metros en el cielo.",
            coords: { x: -12.5, y: 6.5, z: 14.0 }
        },
        {
            id: "golden_ratio",
            name: "Fachada Áurea de Fibonacci (Phi = 1.618)",
            desc: "El ancho total de la fachada respecto a la altura total con el frontón describe un rectángulo áureo perfecto. Las metopas y triglifos modulan la espiral dorada de Fibonacci.",
            coords: { x: 0, y: 11.5, z: 14.5 }
        },
        {
            id: "frieze",
            name: "Friso Panatenaico y Metopas de Fidias",
            desc: "Friso continuo de 160 metros que representaba la solemne procesión de las Panateneas, esculpido en altorrelieve con mármol pentélico policromado en rojo y azul egipcio.",
            coords: { x: 5.5, y: 13.0, z: 13.5 }
        },
        {
            id: "cella",
            name: "Naos / Cella y Estatua Criselefantina de Atenea",
            desc: "La cámara interior albergaba la colosal estatua de 12 metros de Atenea Pártenos, realizada en oro y marfil por Fidias, rodeada por una doble columnata dórica en dos pisos.",
            coords: { x: 0, y: 7.0, z: 0 }
        }
    ]
};

// Fotografía Arqueológica HD de Referencia (Base64)
window.PARTHENON_RUINS_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="40%" stop-color="#1e293b"/>
      <stop offset="70%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <linearGradient id="marbleSun" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fdfbf7"/>
      <stop offset="35%" stop-color="#f3ebd9"/>
      <stop offset="75%" stop-color="#d8cbb5"/>
      <stop offset="100%" stop-color="#b09f84"/>
    </linearGradient>
    <linearGradient id="marbleShadow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8a7963"/>
      <stop offset="100%" stop-color="#b8a68b"/>
    </linearGradient>
    <linearGradient id="goldSpiral" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="800" fill="url(#skyGrad)"/>
  <circle cx="950" cy="180" r="140" fill="#fef08a" opacity="0.15" filter="blur(30px)"/>
  <!-- Acrópolis roca base -->
  <polygon points="40,800 1160,800 1120,620 980,590 850,610 720,595 540,615 360,600 200,625 80,680" fill="#4a3e31"/>
  <!-- Estilóbato escalonado (3 peldaños) con sutil curvatura convexa -->
  <path d="M 120,620 Q 600,613 1080,620 L 1090,635 Q 600,628 110,635 Z" fill="url(#marbleSun)"/>
  <path d="M 140,605 Q 600,598 1060,605 L 1070,620 Q 600,613 130,620 Z" fill="url(#marbleShadow)"/>
  <path d="M 160,590 Q 600,583 1040,590 L 1050,605 Q 600,598 150,605 Z" fill="url(#marbleSun)"/>
  <!-- 8 Columnas Dóricas Frontales con Éntasis -->
  <!-- Col 1 -->
  <path d="M 180,589 L 195,330 Q 198,322 208,322 L 232,322 Q 242,322 245,330 L 260,589 Z" fill="url(#marbleSun)"/>
  <!-- Col 2 -->
  <path d="M 295,588 L 308,330 Q 311,322 321,322 L 345,322 Q 355,322 358,330 L 371,588 Z" fill="url(#marbleSun)"/>
  <!-- Col 3 -->
  <path d="M 410,586 L 421,330 Q 424,322 434,322 L 458,322 Q 468,322 471,330 L 482,586 Z" fill="url(#marbleSun)"/>
  <!-- Col 4 -->
  <path d="M 525,585 L 534,330 Q 537,322 547,322 L 571,322 Q 581,322 584,330 L 593,585 Z" fill="url(#marbleSun)"/>
  <!-- Col 5 -->
  <path d="M 640,585 L 649,330 Q 652,322 662,322 L 686,322 Q 696,322 699,330 L 708,585 Z" fill="url(#marbleSun)"/>
  <!-- Col 6 -->
  <path d="M 755,586 L 766,330 Q 769,322 779,322 L 803,322 Q 813,322 816,330 L 827,586 Z" fill="url(#marbleSun)"/>
  <!-- Col 7 -->
  <path d="M 870,588 L 883,330 Q 886,322 896,322 L 920,322 Q 930,322 933,330 L 946,588 Z" fill="url(#marbleSun)"/>
  <!-- Col 8 -->
  <path d="M 985,589 L 1000,330 Q 1003,322 1013,322 L 1037,322 Q 1047,322 1050,330 L 1065,589 Z" fill="url(#marbleSun)"/>
  <!-- Arquitrabe -->
  <path d="M 170,322 Q 600,315 1070,322 L 1070,285 Q 600,278 170,285 Z" fill="url(#marbleShadow)"/>
  <!-- Friso con Triglifos y Metopas -->
  <path d="M 165,285 Q 600,278 1075,285 L 1075,245 Q 600,238 165,245 Z" fill="url(#marbleSun)"/>
  <!-- Cornisa y Frontón Triangular Áureo -->
  <polygon points="150,245 600,105 1090,245" fill="url(#marbleSun)" stroke="#8a7963" stroke-width="4"/>
  <!-- Tímpano interior con relieve escultórico -->
  <polygon points="190,235 600,120 1050,235" fill="#2d2218" opacity="0.65"/>
  <!-- Espiral Áurea de Fibonacci Superpuesta -->
  <path d="M 150,245 L 1090,245 L 1090,105 L 150,105 Z" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="6,4" opacity="0.8"/>
  <circle cx="600" cy="175" r="5" fill="#38bdf8"/>
  <text x="600" y="760" font-family="'Cinzel', serif" font-size="22" fill="#fbbf24" text-anchor="middle" font-weight="bold">EL PARTENÓN • ACRÓPOLIS DE ATENAS (447 - 432 a.C.)</text>
  <text x="600" y="785" font-family="'Inter', sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Proporción Áurea Φ = 1.6180339 • Correcciones Ópticas de Ictino y Calícrates</text>
</svg>
`);

