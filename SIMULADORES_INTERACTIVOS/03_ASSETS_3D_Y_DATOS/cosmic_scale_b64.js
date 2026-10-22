// ==============================================================================
// ASSET CIENTÍFICO: ESCALA CÓSMICA 3D: DEL QUARK A LOS FILAMENTOS GALÁCTICOS
// Procedencia: Astrofísica Computacional, CERN & NASA Astrophysics Data System
// Potencias de 10: 61 Órdenes de Magnitud (10^-35 m a 10^26 m)
// ==============================================================================

window.COSMIC_SCALE_DATA = {
    title: "Escala Cósmica: 61 Órdenes de Magnitud",
    orders: [
        { exp: -35, name: "Longitud de Planck", size: "1.616 × 10^-35 m", desc: "La escala mínima teórica del espacio-tiempo. Por debajo de esta distancia, la física clásica y la relatividad pierden sentido.", realm: "Física Cuántica Fundamental" },
        { exp: -18, name: "Quarks Up & Down", size: "10^-18 m", desc: "Partículas elementales indivisibles que componen los protones y neutrones en el interior de los átomos.", realm: "Modelo Estándar de Partículas" },
        { exp: -15, name: "Protón / Núcleo Atómico", size: "1.75 × 10^-15 m", desc: "Núcleo atómico retenido por la interacción nuclear fuerte, la fuerza más intensa de la naturaleza.", realm: "Física Nuclear" },
        { exp: -10, name: "Átomo de Hidrógeno", size: "1.06 × 10^-10 m (1 Å)", desc: "El átomo más simple del cosmos: un protón y un electrón orbital. Un 99.9999999% es espacio vacío.", realm: "Química Cuántica" },
        { exp: -9, name: "Doble Hélice de ADN", size: "2 × 10^-9 m (2 nm ancho)", desc: "La molécula maestra de la herencia biológica terrestre. Cuatro bases químicas que codifican toda la vida.", realm: "Biología Molecular" },
        { exp: -7, name: "Virus Bacteriófago T4", size: "2 × 10^-7 m (200 nm)", desc: "Estructura molecular con cápside icosaédrica que parasita bacterias; puente entre la química y la biología.", realm: "Microbiología" },
        { exp: -5, name: "Glóbulo Rojo Humano", size: "7.5 × 10^-6 m (7.5 µm)", desc: "Célula sin núcleo especializada en transportar oxígeno mediante hemoglobina a cada tejido del cuerpo.", realm: "Fisiología Médica" },
        { exp: -3, name: "Grano de Arena / Hormiga", size: "10^-3 m (1 mm)", desc: "Escala táctil cotidiana visible a simple vista; punto de cruce hacia el mundo mesoscópico.", realm: "Mundo Cotidiano" },
        { exp: 0, name: "Ser Humano Adulto", size: "1.70 m", desc: "Estructura biológica compuesta por 37 billones de células conscientes de su propia existencia cósmica.", realm: "Escala Antrópica" },
        { exp: 7, name: "Planeta Tierra", size: "1.274 × 10^7 m (12.742 km)", desc: "Nuestro hogar planetario: el único mundo conocido en albergar océanos líquidos, atmósfera protectora y vida.", realm: "Geofísica Planetaria" },
        { exp: 9, name: "El Sol", size: "1.392 × 10^9 m (1.392.000 km)", desc: "Estrella de secuencia principal (tipo G2V) que concentra el 99.86% de la masa de todo nuestro Sistema Solar.", realm: "Astrofísica Estelar" },
        { exp: 13, name: "Sistema Solar Exterior", size: "1.5 × 10^13 m (~100 UA)", desc: "Dominio gravitatorio directo del Sol que abarca desde Mercurio hasta el Cinturón de Kuiper y la heliopausa.", realm: "Astronomía Planetaria" },
        { exp: 16, name: "Año Luz (Distancia a Próxima Centauri)", size: "9.46 × 10^15 m", desc: "Distancia que recorre un fotón en el vacío en un año terrestre (300.000 km/s). Nuestra estrella vecina está a 4.2 años luz.", realm: "Astrofísica Interestelar" },
        { exp: 21, name: "Vía Láctea (Nuestra Galaxia)", size: "10^21 m (100.000 años luz)", desc: "Galaxia espiral barrada que contiene entre 100.000 y 400.000 millones de estrellas girando en torno a Sagitario A*.", realm: "Cosmología Galáctica" },
        { exp: 23, name: "Cúmulo de Virgo y Grupo Local", size: "10^23 m (10 millones de años luz)", desc: "Concentración gravitatoria de galaxias que agrupa a Andrómeda, la Vía Láctea y miles de galaxias vecinas.", realm: "Cosmología Extragaláctica" },
        { exp: 26, name: "Universo Observable & Red Cósmica", size: "8.8 × 10^26 m (93.000 millones a.l.)", desc: "La mayor estructura conocida: billones de galaxias tejidas en filamentos y vacíos cósmicos desde el Big Bang.", realm: "Cosmología Fundamental" }
    ]
};

window.COSMIC_SCALE_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <defs>
    <radialGradient id="spaceGrad" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="60%" stop-color="#090a1a"/>
      <stop offset="100%" stop-color="#020308"/>
    </radialGradient>
    <linearGradient id="scaleBarGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="25%" stop-color="#34d399"/>
      <stop offset="50%" stop-color="#fbbf24"/>
      <stop offset="75%" stop-color="#f43f5e"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
  </defs>
  <rect width="1000" height="600" fill="url(#spaceGrad)"/>
  <circle cx="500" cy="300" r="240" fill="none" stroke="#38bdf8" stroke-dasharray="4,6" opacity="0.3"/>
  <circle cx="500" cy="300" r="160" fill="none" stroke="#fbbf24" stroke-dasharray="3,5" opacity="0.4"/>
  <circle cx="500" cy="300" r="80" fill="none" stroke="#f43f5e" opacity="0.6"/>
  <circle cx="500" cy="300" r="12" fill="#38bdf8"/>
  <text x="500" y="55" font-family="sans-serif" font-size="24" font-weight="bold" fill="#f8fafc" text-anchor="middle">ESCALA CÓSMICA: 61 ÓRDENES DE MAGNITUD</text>
  <text x="500" y="85" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Desde la Longitud de Planck (10^-35 m) hasta el Universo Observable (10^26 m)</text>
  <rect x="100" y="520" width="800" height="12" rx="6" fill="url(#scaleBarGrad)"/>
  <text x="100" y="555" font-family="monospace" font-size="13" fill="#38bdf8">10^-35 m (Planck)</text>
  <text x="500" y="555" font-family="monospace" font-size="13" fill="#fbbf24" text-anchor="middle">10^0 m (Humano)</text>
  <text x="900" y="555" font-family="monospace" font-size="13" fill="#c084fc" text-anchor="end">10^26 m (Cosmos)</text>
</svg>
`);

