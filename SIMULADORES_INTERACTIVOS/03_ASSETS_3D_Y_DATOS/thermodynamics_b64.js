// ==============================================================================
// ASSET FÍSICO: TERMODINÁMICA MOLECULAR: DEL CERO ABSOLUTO A LA FUSIÓN SOLAR 3D
// Procedencia: NIST Physical Reference Data & Ecuación de Estado de Boltzmann
// Rangos: 0 Kelvin (-273.15 °C) a 15.000.000 Kelvin (Fusión Nuclear Solar)
// ==============================================================================

window.THERMO_DATA = {
    title: "Termodinámica Molecular & Cinética Atómica",
    benchmarks: [
        { tempK: 0, tempC: -273.15, name: "Cero Absoluto (0 K)", desc: "Inmovilidad cinética total. Los átomos cesan toda vibración térmica salvo la mínima energía de punto cero cuántico.", state: "Condensado Bose-Einstein", speedMs: 0 },
        { tempK: 2.73, tempC: -270.42, name: "Fondo Cósmico de Microondas (CMB)", desc: "La temperatura residual del Big Bang que baña todo el espacio intergaláctico profundo.", state: "Gas Criogénico Extremo", speedMs: 130 },
        { tempK: 77.36, tempC: -195.79, name: "Nitrógeno Líquido", desc: "Criogenia industrial y preservación biológica; movimiento browniano muy atenuado.", state: "Líquido Criogénico", speedMs: 380 },
        { tempK: 273.15, tempC: 0.0, name: "Punto de Congelación del Agua", desc: "Formación de la red cristalina hexagonal de puentes de hidrógeno en hielo.", state: "Sólido Cristalino", speedMs: 440 },
        { tempK: 294.15, tempC: 21.0, name: "Confort Térmico del Hogar (21 °C)", desc: "La temperatura óptima recomendada para el descanso y salud cardiovascular en personas mayores.", state: "Gas Atmosférico", speedMs: 460 },
        { tempK: 373.15, tempC: 100.0, name: "Ebullición del Agua", desc: "Ruptura masiva de enlaces moleculares pasando a fase de vapor con gran energía cinética.", state: "Vapor de Agua", speedMs: 520 },
        { tempK: 5778, tempC: 5505, name: "Superficie Solar (Fotosfera)", desc: "Incandescencia estelar amarilla emitiendo el espectro visible según la Ley de Planck.", state: "Gas Ionizado Incandescente", speedMs: 2050 },
        { tempK: 15000000, tempC: 14999727, name: "Núcleo Solar (Fusión Nuclear Protón-Protón)", desc: "Plasma superdenso donde la velocidad térmica supera la barrera de repulsión electrostática de Coulomb.", state: "Plasma de Fusión Termonuclear", speedMs: 600000 }
    ],
    formula: "Ek = (3/2) * kB * T  |  v_rms = sqrt(3 * kB * T / m)"
};

window.THERMO_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <defs>
    <linearGradient id="tempBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="20%" stop-color="#34d399"/>
      <stop offset="45%" stop-color="#fbbf24"/>
      <stop offset="70%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
  </defs>
  <rect width="1000" height="600" fill="#040814"/>
  <text x="500" y="55" font-family="sans-serif" font-size="22" font-weight="bold" fill="#f8fafc" text-anchor="middle">TERMODINÁMICA MOLECULAR & CINÉTICA DE BOLTZMANN</text>
  <text x="500" y="85" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Energía Cinética Atómica: Del Cero Absoluto (0 K) a la Fusión Solar (15.000.000 K)</text>
  <rect x="80" y="480" width="840" height="18" rx="9" fill="url(#tempBar)"/>
  <text x="80" y="525" font-family="monospace" font-size="12" fill="#38bdf8">0 K (-273.15 °C)</text>
  <text x="500" y="525" font-family="monospace" font-size="12" fill="#fbbf24" text-anchor="middle">294 K (21 °C Hogar)</text>
  <text x="920" y="525" font-family="monospace" font-size="12" fill="#c084fc" text-anchor="end">15 MK (Plasma Solar)</text>
</svg>
`);

