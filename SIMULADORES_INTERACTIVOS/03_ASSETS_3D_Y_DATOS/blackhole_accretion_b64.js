// ==============================================================================
// ASSET ASTROFÍSICO: AGUJERO NEGRO SUPERMASIVO, DISCO DE ACRECIÓN & LENTE 3D
// Procedencia: Métricas de Schwarzschild y Kerr • Event Horizon Telescope (EHT M87* / Sgr A*)
// Radio de Schwarzschild: rs = 2GM/c^2 • Esfera de Fotones: 1.5 rs • ISCO: 3.0 rs
// ==============================================================================

window.BLACKHOLE_DATA = {
    title: "Agujero Negro Supermasivo Sagitario A* & Lente Gravitatoria",
    target: "Sagitario A* (Centro de la Vía Láctea)",
    mass: "4.3 millones de masas solares (8.5 × 10^36 kg)",
    schwarzschildRadius: "12.7 millones de kilómetros (~0.08 UA)",
    photonSphereRadius: "19.0 millones de kilómetros (1.5 rs)",
    iscoRadius: "38.1 millones de kilómetros (3.0 rs - Órbita Circular Estable Más Interna)",
    accretionDisk: {
        gasTemperature: "10^7 Kelvin (Plasma brillante emisor de rayos X y luz visible)",
        dopplerBeaming: "El hemisferio del disco que rota hacia el observador es más azul y brillante por amplificación relativista.",
        gravitationalLensing: "La inmensa curvatura del espacio-tiempo deforma la parte trasera del disco, proyectándola por encima y por debajo del horizonte."
    }
};

window.BLACKHOLE_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <defs>
    <radialGradient id="bhHalo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.9"/>
      <stop offset="40%" stop-color="#ea580c" stop-opacity="0.6"/>
      <stop offset="70%" stop-color="#7c2d12" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1000" height="600" fill="#020308"/>
  <ellipse cx="500" cy="300" rx="420" ry="80" fill="url(#bhHalo)"/>
  <ellipse cx="500" cy="300" rx="260" ry="220" fill="none" stroke="#ea580c" stroke-width="26" opacity="0.45"/>
  <circle cx="500" cy="300" r="100" fill="#000000" stroke="#f59e0b" stroke-width="3"/>
  <circle cx="500" cy="300" r="130" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,6" opacity="0.6"/>
  <text x="500" y="55" font-family="sans-serif" font-size="22" font-weight="bold" fill="#f8fafc" text-anchor="middle">AGUJERO NEGRO SUPERMASIVO SAGITARIO A*</text>
  <text x="500" y="85" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Horizonte de Sucesos, Disco de Acreción Deformado por Lente Gravitatoria y Beaming Relativista</text>
  <text x="500" y="555" font-family="monospace" font-size="12" fill="#38bdf8" text-anchor="middle">Radio de Schwarzschild rs = 2GM/c^2 • Esfera de Fotones (1.5 rs) • ISCO (3 rs)</text>
</svg>
`);

