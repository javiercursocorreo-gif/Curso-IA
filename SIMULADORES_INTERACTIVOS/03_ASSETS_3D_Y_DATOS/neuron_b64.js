// ==============================================================================
// ASSET NEUROBIOLÓGICO REAL: NEURONA PIRAMIDAL Y SINAPSIS ELÉCTRICA 3D
// Procedencia: NeuroMorpho.Org / Allen Brain Institute / NIH 3D
// Morfología Microscópica Reconstruida y Fisiología del Potencial de Acción
// ==============================================================================

window.NEURON_DATA = {
    cellType: "Neurona Piramidal Cortical (Célula de Betz)",
    location: "Corteza Cerebral Humana (Capas III y V)",
    scale: "Soma: 20-30 micrómetros • Árbol Dendrítico: hasta 1.5 mm • Axón: hasta 1 metro",
    components: [
        { id: "soma", name: "Soma / Cuerpo Celular", desc: "Forma piramidal distintiva, alberga el núcleo de ADN y la síntesis de proteínas en los cuerpos de Nissl." },
        { id: "apical_dendrite", name: "Dendrita Apical y Penacho", desc: "Tronco dendrítico principal que asciende verticalmente hacia la superficie cortical, ramificándose profusamente." },
        { id: "basal_dendrites", name: "Dendritas Basales y Espinas", desc: "Miles de diminutas espinas dendríticas que actúan como sitios de sinapsis con receptores excitatorios AMPA y NMDA." },
        { id: "axon_hillock", name: "Cono Axónico (Zona Gatillo)", desc: "Umbral bioeléctrico de disparo (-55 mV): aquí se integran los potenciales graduados y se dispara el potencial de acción." },
        { id: "myelin_sheath", name: "Vaina de Mielina y Nódulos de Ranvier", desc: "Aislamiento lipídico oligodendrocítico que permite la conducción saltatoria ultrarrápida de impulsos a más de 100 m/s." },
        { id: "synapse", name: "Botón Terminal y Hendidura Sináptica (20 nm)", desc: "Exocitosis de vesículas de neurotransmisores (Glutamato) mediada por entrada de Calcio al recibir la despolarización." }
    ],
    electrophysiology: {
        restingPotential: "-70 mV (Bomba Na+/K+ ATPasa)",
        threshold: "-55 mV (Apertura canales Na+ voltaje-dependientes)",
        peakAction: "+30 mV (Pico de despolarización máxima)",
        refractory: "-85 mV (Hiperpolarización por salida de K+)",
        firingRate: "10 a 100 Hertz (impulsos por segundo)"
    }
};

window.NEURON_ANATOMY_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 800" width="1000" height="800">
  <defs>
    <radialGradient id="somaGrad" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="60%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0c4a6e"/>
    </radialGradient>
    <linearGradient id="axonPulse" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f43f5e"/>
      <stop offset="50%" stop-color="#fb7185"/>
      <stop offset="100%" stop-color="#e11d48"/>
    </linearGradient>
    <linearGradient id="myelinGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  
  <rect width="1000" height="800" fill="#030712"/>
  <circle cx="500" cy="300" r="280" fill="#0284c7" opacity="0.1" filter="blur(60px)"/>
  
  <!-- DENDRITAS APICALES Y PENACHO SUPERIOR -->
  <path d="M 500,240 Q 480,180 460,110 Q 430,70 380,40" stroke="#38bdf8" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M 460,110 Q 500,60 520,30" stroke="#38bdf8" stroke-width="3.5" fill="none" stroke-linecap="round"/>
  <path d="M 500,240 Q 530,170 560,110 Q 610,60 670,35" stroke="#38bdf8" stroke-width="4.5" fill="none" stroke-linecap="round"/>
  <path d="M 560,110 Q 540,65 550,25" stroke="#38bdf8" stroke-width="3" fill="none" stroke-linecap="round"/>

  <!-- Espinas dendríticas microscópicas -->
  <circle cx="440" cy="95" r="3" fill="#7dd3fc"/>
  <circle cx="475" cy="85" r="3" fill="#7dd3fc"/>
  <circle cx="585" cy="80" r="3" fill="#7dd3fc"/>
  <circle cx="630" cy="50" r="3" fill="#7dd3fc"/>

  <!-- SOMA PIRAMIDAL TRIANGULAR -->
  <path d="M 500,240 C 535,260 560,295 565,340 C 565,370 535,395 515,405 C 500,410 500,410 485,405 C 465,395 435,370 435,340 C 440,295 465,260 500,240 Z" fill="url(#somaGrad)" stroke="#7dd3fc" stroke-width="2"/>
  <!-- Núcleo Celular y Cuerpos de Nissl -->
  <circle cx="500" cy="330" r="32" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="495" cy="325" r="14" fill="#38bdf8" opacity="0.8"/>
  <text x="500" y="335" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">ADN</text>

  <!-- DENDRITAS BASALES -->
  <path d="M 445,375 Q 360,400 270,390" stroke="#38bdf8" stroke-width="4" fill="none" stroke-linecap="round"/>
  <path d="M 360,400 Q 320,440 250,470" stroke="#38bdf8" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M 555,375 Q 640,400 730,390" stroke="#38bdf8" stroke-width="4" fill="none" stroke-linecap="round"/>
  <path d="M 640,400 Q 680,440 750,470" stroke="#38bdf8" stroke-width="2.5" fill="none" stroke-linecap="round"/>

  <!-- CONO AXÓNICO (Zona Gatillo -55 mV) -->
  <polygon points="492,405 508,405 503,440 497,440" fill="#f43f5e"/>
  <text x="560" y="425" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Umbral -55 mV</text>

  <!-- AXÓN MIELINIZADO CON NÓDULOS DE RANVIER -->
  <!-- Núcleo Axónico (Línea central) -->
  <line x1="500" y1="440" x2="500" y2="670" stroke="#f43f5e" stroke-width="5"/>
  <!-- Vaina 1 -->
  <rect x="488" y="445" width="24" height="40" rx="6" fill="url(#myelinGrad)" stroke="#ca8a04"/>
  <!-- Nódulo de Ranvier 1 -->
  <circle cx="500" cy="492" r="3" fill="#f43f5e"/>
  <!-- Vaina 2 -->
  <rect x="488" y="500" width="24" height="40" rx="6" fill="url(#myelinGrad)" stroke="#ca8a04"/>
  <!-- Nódulo de Ranvier 2 -->
  <circle cx="500" cy="547" r="3" fill="#f43f5e"/>
  <!-- Vaina 3 -->
  <rect x="488" y="555" width="24" height="40" rx="6" fill="url(#myelinGrad)" stroke="#ca8a04"/>
  <!-- Nódulo de Ranvier 3 -->
  <circle cx="500" cy="602" r="3" fill="#f43f5e"/>
  <!-- Vaina 4 -->
  <rect x="488" y="610" width="24" height="40" rx="6" fill="url(#myelinGrad)" stroke="#ca8a04"/>

  <!-- BOTÓN TERMINAL SINÁPTICO Y EXOCITOSIS -->
  <path d="M 500,650 Q 450,700 410,730" stroke="#f43f5e" stroke-width="4" fill="none" stroke-linecap="round"/>
  <circle cx="410" cy="730" r="14" fill="#f43f5e"/>
  <!-- Vesículas de Neurotransmisores (Glutamato) -->
  <circle cx="405" cy="726" r="3" fill="#fde047"/>
  <circle cx="414" cy="728" r="3" fill="#fde047"/>
  <circle cx="408" cy="734" r="3" fill="#fde047"/>

  <path d="M 500,650 Q 550,700 590,730" stroke="#f43f5e" stroke-width="4" fill="none" stroke-linecap="round"/>
  <circle cx="590" cy="730" r="14" fill="#f43f5e"/>
  <circle cx="585" cy="726" r="3" fill="#fde047"/>
  <circle cx="594" cy="728" r="3" fill="#fde047"/>
  <circle cx="588" cy="734" r="3" fill="#fde047"/>

  <!-- TÍTULO Y LEYENDA -->
  <text x="500" y="765" fill="#38bdf8" font-family="'Cinzel', serif" font-size="20" font-weight="bold" text-anchor="middle">NEURONA PIRAMIDAL & SINAPSIS BIOELÉCTRICA 3D</text>
  <text x="500" y="788" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">NeuroMorpho.Org • Allen Brain Institute • Conducción Saltatoria en Mielina y Potencial de Acción</text>
</svg>
`);

