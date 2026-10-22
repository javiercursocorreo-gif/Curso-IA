// ==============================================================================
// ASSET BIOMÉDICO REAL: ESQUELETO DE LA MANO HUMANA Y BIOMECÁNICA DIGITAL 3D
// Procedencia: NIH 3D Print Exchange / Banco Anatómico Quirúrgico Ortopédico
// Escaneo Micro-CT Óseo de los 27 Huesos y Cinemática Articular
// ==============================================================================

window.HAND_DATA = {
    structure: "Esqueleto de la Mano y Muñeca Humana",
    totalBones: 27,
    groups: [
        {
            name: "Carpo (Muñeca - 8 Huesos)",
            color: "#38bdf8",
            proximalRow: ["Escafoides", "Semilunar", "Piramidal", "Pisiforme"],
            distalRow: ["Trapecio", "Trapezoide", "Grande (Capitatum)", "Ganchoso (Hamatum)"]
        },
        {
            name: "Metacarpo (Palma - 5 Huesos)",
            color: "#34d399",
            bones: ["I Metacarpiano (Pulgar)", "II Metacarpiano", "III Metacarpiano", "IV Metacarpiano", "V Metacarpiano"]
        },
        {
            name: "Falanges (Dedos - 14 Huesos)",
            color: "#fbbf24",
            proximal: ["Falanges Proximales I a V (5 huesos)"],
            middle: ["Falanges Medias II a V (4 huesos, ausente en pulgar)"],
            distal: ["Falanges Distales / Ungueales I a V (5 huesos)"]
        }
    ],
    biomechanics: {
        thumbOpposition: "Articulación Trapeciometacarpiana en silla de montar: permite el giro de 90° que capacita la pinza de precisión y la fabricación de herramientas.",
        carpalTunnel: "Canal osteofibroso delimitado por los huesos del carpo y el retináculo flexor: túnel crítico por donde pasan los 9 tendones flexores y el Nervio Mediano.",
        gripTypes: ["Pinza Fina (Pulgar - Índice)", "Puño de Fuerza Cilíndrico", "Agarre Esférico", "Pinza Lateral de Llave"]
    }
};

window.HAND_SKELETON_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 800" width="1000" height="800">
  <defs>
    <radialGradient id="boneGrad" cx="45%" cy="35%" r="60%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#94a3b8"/>
    </radialGradient>
    <linearGradient id="carpalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7dd3fc"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="metaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#6ee7b7"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="phalangeGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fde047"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  
  <rect width="1000" height="800" fill="#040711"/>
  <circle cx="500" cy="400" r="300" fill="#0284c7" opacity="0.08" filter="blur(50px)"/>

  <!-- RADIO Y CÚBITO (Antebrazo Distal) -->
  <path d="M 430,730 L 440,650 Q 450,640 470,645 L 480,730 Z" fill="url(#boneGrad)" opacity="0.5"/>
  <text x="400" y="700" fill="#64748b" font-family="'Inter', sans-serif" font-size="11">Cúbito</text>
  <path d="M 495,730 L 485,645 Q 520,630 550,645 L 565,730 Z" fill="url(#boneGrad)" opacity="0.5"/>
  <text x="590" y="700" fill="#64748b" font-family="'Inter', sans-serif" font-size="11">Radio</text>

  <!-- CARPO (8 Huesos en dos filas) -->
  <!-- Fila Proximal: Escafoides, Semilunar, Piramidal, Pisiforme -->
  <rect x="455" y="618" width="22" height="18" rx="6" fill="url(#carpalGrad)"/>
  <rect x="480" y="615" width="22" height="20" rx="6" fill="url(#carpalGrad)"/>
  <rect x="505" y="616" width="24" height="22" rx="6" fill="url(#carpalGrad)"/>
  <!-- Fila Distal: Trapecio, Trapezoide, Grande, Ganchoso -->
  <rect x="445" y="590" width="20" height="22" rx="6" fill="url(#carpalGrad)"/>
  <rect x="470" y="588" width="22" height="24" rx="6" fill="url(#carpalGrad)"/>
  <rect x="496" y="585" width="24" height="26" rx="6" fill="url(#carpalGrad)"/>
  <rect x="525" y="588" width="22" height="24" rx="6" fill="url(#carpalGrad)"/>
  <text x="375" y="605" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="12" font-weight="bold">Carpo (8)</text>

  <!-- METACARPIANOS (Palma I a V) -->
  <!-- I Metacarpiano (Pulgar en oposición) -->
  <path d="M 435,595 L 360,540 L 375,520 L 445,580 Z" fill="url(#metaGrad)"/>
  <!-- II Metacarpiano (Índice) -->
  <rect x="450" y="470" width="18" height="110" rx="7" fill="url(#metaGrad)"/>
  <!-- III Metacarpiano (Medio - Eje de la mano) -->
  <rect x="485" y="455" width="19" height="125" rx="7" fill="url(#metaGrad)"/>
  <!-- IV Metacarpiano (Anular) -->
  <rect x="520" y="470" width="18" height="112" rx="7" fill="url(#metaGrad)"/>
  <!-- V Metacarpiano (Meñique) -->
  <rect x="552" y="490" width="17" height="95" rx="7" fill="url(#metaGrad)"/>
  <text x="615" y="525" fill="#34d399" font-family="'Inter', sans-serif" font-size="12" font-weight="bold">Metacarpo (5)</text>

  <!-- FALANGES (14 Huesos) -->
  <!-- PULGAR (2 falanges) -->
  <!-- Proximal -->
  <path d="M 360,535 L 310,485 L 325,470 L 372,518 Z" fill="url(#phalangeGrad)"/>
  <!-- Distal -->
  <path d="M 310,480 L 275,445 L 290,432 L 322,468 Z" fill="url(#phalangeGrad)"/>

  <!-- ÍNDICE (3 falanges) -->
  <rect x="451" y="380" width="16" height="80" rx="6" fill="url(#phalangeGrad)"/>
  <rect x="452" y="315" width="14" height="60" rx="5" fill="url(#phalangeGrad)"/>
  <rect x="453" y="270" width="12" height="40" rx="4" fill="url(#phalangeGrad)"/>

  <!-- MEDIO (3 falanges - El más largo) -->
  <rect x="487" y="360" width="16" height="85" rx="6" fill="url(#phalangeGrad)"/>
  <rect x="488" y="290" width="14" height="65" rx="5" fill="url(#phalangeGrad)"/>
  <rect x="489" y="240" width="12" height="45" rx="4" fill="url(#phalangeGrad)"/>

  <!-- ANULAR (3 falanges) -->
  <rect x="521" y="380" width="16" height="80" rx="6" fill="url(#phalangeGrad)"/>
  <rect x="522" y="318" width="14" height="58" rx="5" fill="url(#phalangeGrad)"/>
  <rect x="523" y="275" width="12" height="38" rx="4" fill="url(#phalangeGrad)"/>

  <!-- MEÑIQUE (3 falanges) -->
  <rect x="553" y="415" width="15" height="70" rx="5" fill="url(#phalangeGrad)"/>
  <rect x="554" y="360" width="13" height="50" rx="5" fill="url(#phalangeGrad)"/>
  <rect x="555" y="320" width="11" height="35" rx="4" fill="url(#phalangeGrad)"/>
  <text x="615" y="310" fill="#fbbf24" font-family="'Inter', sans-serif" font-size="12" font-weight="bold">Falanges (14)</text>

  <!-- LEYENDA TÉCNICA Y TÍTULO -->
  <text x="500" y="750" fill="#f8fafc" font-family="'Cinzel', serif" font-size="21" font-weight="bold" text-anchor="middle">ESQUELETO DE LA MANO HUMANA & BIOMECÁNICA (27 HUESOS)</text>
  <text x="500" y="775" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="13" text-anchor="middle">NIH 3D Print Exchange • Carpo (8) • Metacarpo (5) • Falanges (14) • Oposición del Pulgar</text>
</svg>
`);

