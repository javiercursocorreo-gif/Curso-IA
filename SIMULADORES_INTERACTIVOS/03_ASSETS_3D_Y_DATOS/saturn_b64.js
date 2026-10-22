// ==============================================================================
// ASSET ASTRONÓMICO REAL: SATURNO, SISTEMA DE ANILLOS Y DIVISIÓN DE CASSINI 3D
// Procedencia: NASA / JPL-Caltech / Misión Cassini-Huygens
// Cartografía Espectral Oficial de Bandas Zonales y Resonancia Gravitatoria
// ==============================================================================

window.SATURN_DATA = {
    planet: "Saturno (El Señor de los Anillos)",
    classification: "Gigante Gaseoso Exterior",
    distanceFromSun: "9.58 Unidades Astronómicas (1.433 millones de km)",
    axialTilt: "26.73° respecto a su plano orbital",
    rotationPeriod: "10 horas, 33 minutos (Rotación diferencial)",
    orbitalPeriod: "29.45 años terrestres",
    atmosphere: "96.3% Hidrógeno molecular, 3.25% Helio, trazas de Metano y Amoníaco",
    rings: {
        totalSpan: "282.000 km de diámetro (Desde D hasta F)",
        thickness: "Apenas 10 a 30 metros de espesor medio",
        composition: "99% partículas de hielo de agua pura, 1% silicatos y tolinas",
        subdivisions: [
            { id: "ring_d", name: "Anillo D", radius: "66.900 - 74.500 km", desc: "El más interno y tenue, casi invisible." },
            { id: "ring_c", name: "Anillo C (Crepé)", radius: "74.650 - 92.000 km", desc: "Translúcido y oscuro, con bandas concéntricas." },
            { id: "ring_b", name: "Anillo B", radius: "92.000 - 117.580 km", desc: "El más masivo, brillante y denso de todo el sistema." },
            { id: "cassini_division", name: "División de Cassini", radius: "117.580 - 122.170 km (4.800 km ancho)", desc: "Brecha oscura barrida por resonancia orbital 2:1 con la luna Mimas." },
            { id: "ring_a", name: "Anillo A", radius: "122.170 - 136.775 km", desc: "Segundo más brillante, alberga la División de Encke (325 km)." },
            { id: "ring_f", name: "Anillo F", radius: "140.180 km", desc: "Estrecho y trenzado, confinado por las lunas pastoras Prometeo y Pandora." }
        ]
    },
    features: [
        { id: "hexagon", name: "Hexágono Polar Norte", desc: "Corriente en chorro atmosférica de 30.000 km de ancho con simetría hexagonal de 6 vértices." },
        { id: "titan", name: "Titán (Luna Mayor)", desc: "Mayor que Mercurio, con atmósfera densa de nitrógeno y lagos de metano líquido." },
        { id: "enceladus", name: "Encélado", desc: "Océano global subsuperficial con géiseres de agua salada eyectados al espacio." }
    ]
};

window.SATURN_CASSINI_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <defs>
    <radialGradient id="saturnGlobe" cx="42%" cy="38%" r="60%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="30%" stop-color="#fde047"/>
      <stop offset="60%" stop-color="#eab308"/>
      <stop offset="85%" stop-color="#a16207"/>
      <stop offset="100%" stop-color="#451a03"/>
    </radialGradient>
    <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706" stop-opacity="0.2"/>
      <stop offset="25%" stop-color="#fde047" stop-opacity="0.85"/>
      <stop offset="55%" stop-color="#fef08a" stop-opacity="0.95"/>
      <stop offset="65%" stop-color="#050814" stop-opacity="0.95"/> <!-- Cassini Div -->
      <stop offset="72%" stop-color="#eab308" stop-opacity="0.75"/>
      <stop offset="90%" stop-color="#ca8a04" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#78350f" stop-opacity="0.1"/>
    </linearGradient>
  </defs>
  
  <rect width="1200" height="800" fill="#02040a"/>
  <!-- Campo Estelar de Fondo -->
  <circle cx="120" cy="80" r="1.5" fill="#ffffff" opacity="0.8"/>
  <circle cx="340" cy="190" r="1.2" fill="#ffffff" opacity="0.6"/>
  <circle cx="890" cy="110" r="1.8" fill="#ffffff" opacity="0.9"/>
  <circle cx="1050" cy="240" r="1.3" fill="#ffffff" opacity="0.7"/>
  <circle cx="210" cy="670" r="1.6" fill="#ffffff" opacity="0.85"/>
  <circle cx="980" cy="710" r="1.4" fill="#ffffff" opacity="0.75"/>

  <!-- Resplandor Atmosférico -->
  <circle cx="600" cy="400" r="180" fill="#fde047" opacity="0.1" filter="blur(40px)"/>

  <!-- PARTE TRASERA DE LOS ANILLOS (Pasa por detrás del globo) -->
  <ellipse cx="600" cy="400" rx="460" ry="110" fill="none" stroke="url(#ringGrad)" stroke-width="120" transform="rotate(-26.73, 600, 400)" opacity="0.95"/>

  <!-- GLOBO PLANETARIO DE SATURNO (Achatado en polos: 60.268 km eq vs 54.364 km pol) -->
  <ellipse cx="600" cy="400" rx="172" ry="155" fill="url(#saturnGlobe)" transform="rotate(-26.73, 600, 400)"/>

  <!-- Bandas Atmosféricas Zonales -->
  <path d="M 438,360 Q 600,340 762,360" stroke="#ca8a04" stroke-width="8" fill="none" opacity="0.35" transform="rotate(-26.73, 600, 400)"/>
  <path d="M 445,390 Q 600,370 755,390" stroke="#fde047" stroke-width="14" fill="none" opacity="0.4" transform="rotate(-26.73, 600, 400)"/>
  <path d="M 455,430 Q 600,410 745,430" stroke="#a16207" stroke-width="10" fill="none" opacity="0.45" transform="rotate(-26.73, 600, 400)"/>

  <!-- Hexágono Polar Norte -->
  <polygon points="585,255 615,255 630,270 615,285 585,285 570,270" stroke="#fef08a" stroke-width="2.5" fill="#854d0e" opacity="0.75" transform="rotate(-26.73, 600, 400)"/>

  <!-- Sombra del globo proyectada sobre el anillo trasero -->
  <!-- PARTE DELANTERA DE LOS ANILLOS (Cubre el hemisferio sur) -->
  <clipPath id="frontRingsClip">
    <rect x="0" y="380" width="1200" height="420"/>
  </clipPath>
  <ellipse cx="600" cy="400" rx="460" ry="110" fill="none" stroke="url(#ringGrad)" stroke-width="120" transform="rotate(-26.73, 600, 400)" clip-path="url(#frontRingsClip)"/>

  <!-- DIVISIÓN DE CASSINI (4.800 km brecha vacía) -->
  <ellipse cx="600" cy="400" rx="422" ry="101" fill="none" stroke="#02040a" stroke-width="12" transform="rotate(-26.73, 600, 400)"/>

  <!-- LUNAS ORBITALES -->
  <!-- Titán -->
  <circle cx="1100" cy="310" r="10" fill="#f59e0b"/>
  <text x="1100" y="335" fill="#fde047" font-family="'Inter', sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Titán</text>

  <!-- Encélado -->
  <circle cx="280" cy="480" r="4.5" fill="#e0f2fe"/>
  <text x="280" y="505" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Encélado</text>

  <!-- TÍTULO Y LEYENDA TÉCNICA -->
  <text x="600" y="745" fill="#fde047" font-family="'Cinzel', serif" font-size="22" font-weight="bold" text-anchor="middle">SATURNO, SISTEMA DE ANILLOS & DIVISIÓN DE CASSINI</text>
  <text x="600" y="772" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="13" text-anchor="middle">NASA Cassini-Huygens • Inclinación Axial 26.73° • Anillos A, B, C y Brecha de Cassini de 4.800 km</text>
</svg>
`);

