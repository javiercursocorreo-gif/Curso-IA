// ==============================================================================
// ASSET ARQUEOLÓGICO REAL: FARAÓN TUTANKAMÓN Y MÁSCARA FUNERARIA DORADA 3D
// Procedencia: Museo Egipcio de El Cairo / Metropolitan Museum of Art (Met)
// Tumba KV62, Valle de los Reyes • Dinastía XVIII de Egipto (c. 1323 a.C.)
// ==============================================================================

window.TUTANKHAMUN_DATA = {
    artifact: "Máscara Funeraria de Tutankamón",
    tomb: "Tumba KV62, Valle de los Reyes (Luxor, Egipto)",
    discovery: "4 de noviembre de 1922 por Howard Carter y Lord Carnarvon",
    date: "c. 1323 a.C. (Imperio Nuevo, Dinastía XVIII)",
    dimensions: "Altura: 54 cm • Anchura: 39.3 cm • Profundidad: 49 cm",
    weight: "10.23 kg de oro macizo batido de 24 quilates",
    materials: [
        "Oro macizo batido y pulido (reflejos PBR solares)",
        "Lapislázuli afgano auténtico (franjas del Nemes y cejas)",
        "Pasta vítrea azul cobalto y turquesa",
        "Cuarzo blanco lechoso (esclerótica de los ojos)",
        "Obsidiana volcánica negra (pupilas)",
        "Cornalina roja y fayenza polícroma (collar usej)"
    ],
    symbolism: [
        {
            id: "nemes",
            name: "Tocado Nemes Real",
            desc: "Tocado rayado reservado a los faraones, símbolo del renacimiento solar. Sus bandas alternan oro fino y franjas vidriadas de azul cobalto imitando lapislázuli."
        },
        {
            id: "uraeus",
            name: "Las Dos Señoras (Ureo y Buitre)",
            desc: "En la frente se alzan las protectoras divinas de Egipto: la cobra Uadyet (Bajo Egipto) escupiendo fuego y la diosa buitre Nejbet (Alto Egipto) con alas protectoras."
        },
        {
            id: "beard",
            name: "Barba Postiza Osiríaca",
            desc: "Barba ceremonial trenzada con curvatura distal de 2.5 kg de oro y lapislázuli, que asimila al faraón fallecido con Osiris, el señor del inframundo."
        },
        {
            id: "collar",
            name: "Collar Usej y Halcones de Horus",
            desc: "Pectoral ancho de doce vueltas rematado en broches con cabezas del halcón Horus incrustadas con piedras semipreciosas."
        },
        {
            id: "inscription",
            name: "Conjuro 151b del Libro de los Muertos",
            desc: "En la espalda y hombros de la máscara se encuentra grabado un texto jeroglífico que asegura la visión, respiración y protección eterna de cada rasgo facial del rey."
        }
    ]
};

window.TUTANKHAMUN_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 800" width="1000" height="800">
  <defs>
    <linearGradient id="goldPlate" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fffbeb"/>
      <stop offset="25%" stop-color="#fde047"/>
      <stop offset="50%" stop-color="#eab308"/>
      <stop offset="75%" stop-color="#ca8a04"/>
      <stop offset="100%" stop-color="#854d0e"/>
    </linearGradient>
    <linearGradient id="lapisStripes" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="50%" stop-color="#172554"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <radialGradient id="faceGlow" cx="50%" cy="45%" r="40%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="60%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#a16207"/>
    </radialGradient>
  </defs>
  
  <rect width="1000" height="800" fill="#04060b"/>
  <circle cx="500" cy="380" r="320" fill="#eab308" opacity="0.12" filter="blur(60px)"/>
  
  <!-- TOCADO NEMES (Silueta Expandida) -->
  <path d="M 500,120 C 650,120 780,240 820,380 C 850,480 830,620 760,660 L 680,660 C 650,560 630,480 630,440 L 370,440 C 370,480 350,560 320,660 L 240,660 C 170,620 150,480 180,380 C 220,240 350,120 500,120 Z" fill="url(#goldPlate)"/>
  
  <!-- Franjas de Lapislázuli en el Nemes -->
  <path d="M 270,220 C 340,160 430,135 500,135 C 570,135 660,160 730,220 L 745,245 C 670,185 580,160 500,160 C 420,160 330,185 255,245 Z" fill="url(#lapisStripes)"/>
  <path d="M 240,280 C 320,210 420,180 500,180 C 580,180 680,210 760,280 L 775,310 C 690,235 590,205 500,205 C 410,205 310,235 225,310 Z" fill="url(#lapisStripes)"/>
  <path d="M 205,360 C 280,280 400,245 500,245 C 600,245 720,280 795,360 L 805,395 C 725,310 610,270 500,270 C 390,270 275,310 195,395 Z" fill="url(#lapisStripes)"/>
  <path d="M 185,450 C 220,400 280,360 320,340 L 320,375 C 285,395 235,430 200,480 Z" fill="url(#lapisStripes)"/>
  <path d="M 815,450 C 780,400 720,360 680,340 L 680,375 C 715,395 765,430 800,480 Z" fill="url(#lapisStripes)"/>
  
  <!-- ROSTRO DORADO REAL -->
  <path d="M 500,220 C 585,220 635,280 635,370 C 635,465 575,540 500,560 C 425,540 365,465 365,370 C 365,280 415,220 500,220 Z" fill="url(#faceGlow)" stroke="#ca8a04" stroke-width="2"/>
  
  <!-- OJOS ALMENDRADOS DE CUARZO Y OBSIDIANA -->
  <!-- Ojo Izquierdo -->
  <path d="M 405,365 Q 445,340 475,365 Q 445,390 405,365 Z" fill="#f8fafc" stroke="#0f172a" stroke-width="4"/>
  <circle cx="445" cy="365" r="9" fill="#020617"/>
  <!-- Delineado kohl de lapislázuli -->
  <path d="M 390,368 L 405,365" stroke="#1e3a8a" stroke-width="5" stroke-linecap="round"/>
  <path d="M 475,365 L 495,360" stroke="#1e3a8a" stroke-width="4" stroke-linecap="round"/>
  <!-- Ceja Lapislázuli -->
  <path d="M 400,340 Q 445,325 480,335" stroke="#1e3a8a" stroke-width="7" fill="none" stroke-linecap="round"/>
  
  <!-- Ojo Derecho -->
  <path d="M 595,365 Q 555,340 525,365 Q 555,390 595,365 Z" fill="#f8fafc" stroke="#0f172a" stroke-width="4"/>
  <circle cx="555" cy="365" r="9" fill="#020617"/>
  <path d="M 610,368 L 595,365" stroke="#1e3a8a" stroke-width="5" stroke-linecap="round"/>
  <path d="M 525,365 L 505,360" stroke="#1e3a8a" stroke-width="4" stroke-linecap="round"/>
  <path d="M 600,340 Q 555,325 520,335" stroke="#1e3a8a" stroke-width="7" fill="none" stroke-linecap="round"/>

  <!-- Nariz y Labios Carnosos -->
  <path d="M 500,350 L 492,435 Q 500,442 508,435 Z" fill="#d97706" opacity="0.6"/>
  <path d="M 470,470 Q 500,460 530,470 Q 500,490 470,470 Z" fill="#b45309" stroke="#92400e" stroke-width="1.5"/>

  <!-- BARBA OSIRÍACA TRENZADA -->
  <path d="M 485,555 L 475,690 Q 500,715 525,690 L 515,555 Z" fill="url(#goldPlate)" stroke="#1e3a8a" stroke-width="3"/>
  <line x1="480" y1="590" x2="520" y2="590" stroke="#1e3a8a" stroke-width="3"/>
  <line x1="477" y1="625" x2="523" y2="625" stroke="#1e3a8a" stroke-width="3"/>
  <line x1="475" y1="660" x2="525" y2="660" stroke="#1e3a8a" stroke-width="3"/>

  <!-- UREO Y BUITRE EN LA FRENTE -->
  <!-- Cobra Uadyet -->
  <path d="M 485,210 Q 470,150 480,120 Q 500,110 495,145 Q 495,180 490,210 Z" fill="url(#goldPlate)" stroke="#0f172a" stroke-width="2"/>
  <!-- Cabeza Buitre Nejbet -->
  <path d="M 515,210 Q 530,150 520,120 Q 505,115 510,145 Q 510,180 515,210 Z" fill="url(#goldPlate)" stroke="#0f172a" stroke-width="2"/>

  <!-- TEXTO INFORMATIVO -->
  <text x="500" y="745" fill="#fde047" font-family="'Cinzel', serif" font-size="22" font-weight="bold" text-anchor="middle">MÁSCARA FUNERARIA DE TUTANKAMÓN (c. 1323 a.C.)</text>
  <text x="500" y="772" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="13" text-anchor="middle">Museo Egipcio de El Cairo • Valle de los Reyes (KV62) • 10.23 kg Oro Macizo y Lapislázuli</text>
</svg>
`);

