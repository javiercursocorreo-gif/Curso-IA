// ==============================================================================
// ASSET FÍSICO: RELATIVIDAD ESPECIAL, CONO DE LUZ & DILATACIÓN LORENTZ 3D
// Procedencia: Albert Einstein (1905) & Espacio-Tiempo de Minkowski (1908)
// Factor de Lorentz: gamma = 1 / sqrt(1 - v^2/c^2) • Velocidad Luz c = 299.792 km/s
// ==============================================================================

window.RELATIVITY_DATA = {
    title: "Relatividad Especial & Deformación Espacio-Temporal de Lorentz",
    speedOfLight: "c = 299.792.458 m/s",
    lorentzCases: [
        { v_frac: 0.00, gamma: 1.000, timeDilation: "1.00 s nave = 1.00 s Tierra", contraction: "100% longitud original", desc: "Física clásica de Newton: el tiempo y el espacio son absolutos." },
        { v_frac: 0.50, gamma: 1.155, timeDilation: "1.00 s nave = 1.15 s Tierra (+15%)", contraction: "86.6% de la longitud", desc: "Efectos relativistas incipientes pero medibles en satélites GPS." },
        { v_frac: 0.866, gamma: 2.000, timeDilation: "1.00 s nave = 2.00 s Tierra (Doble)", contraction: "50% de la longitud", desc: "El reloj en la Tierra corre exactamente al doble de velocidad." },
        { v_frac: 0.990, gamma: 7.089, timeDilation: "1.00 s nave = 7.09 s Tierra", contraction: "14.1% de la longitud", desc: "El espacio se aplasta radicalmente en la dirección del movimiento." },
        { v_frac: 0.999, gamma: 22.366, timeDilation: "1.00 s nave = 22.37 s Tierra", contraction: "4.47% de la longitud", desc: "Dilatación extrema: 1 año a bordo equivale a más de 22 años en la Tierra." }
    ],
    minkowskiCone: {
        future: "Cono de Luz Futuro (Eventos que podemos influir a velocidad <= c)",
        past: "Cono de Luz Pasado (Eventos que pueden habernos alcanzado a velocidad <= c)",
        elsewhere: "Espacio Inaccesible Causalmente (Separación tipo espacio: requiere v > c, prohibido)"
    }
};

window.RELATIVITY_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <defs>
    <linearGradient id="coneGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#818cf8" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0.8"/>
    </linearGradient>
  </defs>
  <rect width="1000" height="600" fill="#040714"/>
  <polygon points="500,300 250,80 750,80" fill="url(#coneGrad)" opacity="0.4"/>
  <polygon points="500,300 250,520 750,520" fill="url(#coneGrad)" opacity="0.4"/>
  <line x1="150" y1="300" x2="850" y2="300" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="500" y1="40" x2="500" y2="560" stroke="#f8fafc" stroke-width="2"/>
  <text x="500" y="35" font-family="sans-serif" font-size="13" fill="#f8fafc" text-anchor="middle">TIEMPO (ct)</text>
  <text x="860" y="305" font-family="sans-serif" font-size="13" fill="#94a3b8">ESPACIO (x)</text>
  <text x="500" y="160" font-family="sans-serif" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">FUTURO CAUSAL</text>
  <text x="500" y="440" font-family="sans-serif" font-size="18" font-weight="bold" fill="#c084fc" text-anchor="middle">PASADO CAUSAL</text>
  <circle cx="500" cy="300" r="6" fill="#fbbf24"/>
  <text x="515" y="315" font-family="sans-serif" font-size="12" fill="#fbbf24">Presente (Aquí y Ahora)</text>
</svg>
`);

