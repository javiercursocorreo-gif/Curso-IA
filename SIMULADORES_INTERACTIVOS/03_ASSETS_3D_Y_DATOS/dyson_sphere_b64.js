// ==============================================================================
// ASSET ASTROFÍSICO: ESFERA DE DYSON Y MEGAESTRUCTURAS KARDASHEV 3D
// Procedencia: Astrofísica Teórica, Freeman Dyson (1960) & Escala de Kardashev (1964)
// Luminosidad Solar: 3.828 × 10^26 Watts • Radio Orbital: 1 Unidad Astronómica
// ==============================================================================

window.DYSON_DATA = {
    title: "Esfera de Dyson & Enjambre Colector Kardashev Tipo II",
    star: {
        name: "Estrella Tipo G2V (Sol Central)",
        luminosity: "3.828 × 10^26 Watts",
        mass: "1.989 × 10^30 kg",
        surfaceTemp: "5778 Kelvin",
        radius: "696.340 km"
    },
    kardashevScale: [
        { type: "Tipo I", power: "10^16 Watts", desc: "Aprovecha toda la energía solar y térmica que incide sobre su planeta natal (la Tierra actual ronda ~0.73)." },
        { type: "Tipo II", power: "3.8 × 10^26 Watts", desc: "Captura el 100% de la energía emitida por su estrella central mediante un enjambre de Dyson." },
        { type: "Tipo III", power: "10^36 Watts", desc: "Controla la energía total de una galaxia completa (cientos de miles de millones de estrellas)." }
    ],
    swarmConfig: {
        orbitalRadius: "1.00 UA (149.597.870 km)",
        collectorUnits: "120.000 satélites en anillos keplerianos contrarrotantes",
        mirrorMaterial: "Película de grafeno y reflectores dieléctricos ultraligeros",
        wasteHeatEmission: "Radiación infrarroja residual emitida a 300 K (firma teórica buscada por telescopios SETI)"
    }
};

window.DYSON_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <defs>
    <radialGradient id="starGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#fef08a"/>
      <stop offset="60%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </radialGradient>
    <radialGradient id="haloGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="#f59e0b" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1000" height="600" fill="#04060d"/>
  <circle cx="500" cy="300" r="180" fill="url(#haloGrad)"/>
  <ellipse cx="500" cy="300" rx="380" ry="110" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,8" opacity="0.6"/>
  <ellipse cx="500" cy="300" rx="360" ry="150" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="6,6" opacity="0.5"/>
  <ellipse cx="500" cy="300" rx="320" ry="200" fill="none" stroke="#34d399" stroke-width="1.5" stroke-dasharray="3,7" opacity="0.4"/>
  <circle cx="500" cy="300" r="54" fill="url(#starGrad)"/>
  <text x="500" y="50" font-family="sans-serif" font-size="22" font-weight="bold" fill="#f8fafc" text-anchor="middle">ESFERA DE DYSON & ENJAMBRE KARDASHEV TIPO II</text>
  <text x="500" y="80" font-family="sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Captura de 3.828 × 10^26 Watts mediante colectores solares a 1 UA</text>
  <text x="500" y="560" font-family="monospace" font-size="12" fill="#38bdf8" text-anchor="middle">Firma de Detección SETI: Exceso de radiación infrarroja térmica a 300 K</text>
</svg>
`);

