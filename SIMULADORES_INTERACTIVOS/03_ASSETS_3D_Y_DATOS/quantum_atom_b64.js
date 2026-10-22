// ==============================================================================
// ASSET CUÁNTICO: ESTRUCTURA DEL ÁTOMO & ORBITALES CUÁNTICOS 3D
// Procedencia: Ecuación de Onda de Schrödinger & Armónicos Esféricos Cuánticos
// Números Cuánticos: n (Principal), l (Momento Angular: s, p, d, f), m (Magnético)
// ==============================================================================

window.QUANTUM_ATOM_DATA = {
    title: "Estructura del Átomo & Nubes de Probabilidad Cuántica |psi|^2",
    orbitals: [
        { id: "1s", name: "Orbital 1s (Esférico)", n: 1, l: 0, m: 0, desc: "Simetría esférica perfecta con máxima densidad de probabilidad cerca del núcleo atómico." },
        { id: "2s", name: "Orbital 2s (Con Nodo Esférico)", n: 2, l: 0, m: 0, desc: "Capa esférica con una superficie nodal interna donde la probabilidad de hallar el electrón es exactamente cero." },
        { id: "2pz", name: "Orbital 2pz (Lóbulos Bipolares)", n: 2, l: 1, m: 0, desc: "Dos lóbulos orientados a lo largo del eje Z con cambio de signo en la fase de la función de onda." },
        { id: "2px", name: "Orbital 2px", n: 2, l: 1, m: 1, desc: "Lóbulos alineados sobre el eje X perpendiculares a 2py y 2pz." },
        { id: "3d_z2", name: "Orbital 3d z² (Lóbulo & Toroide)", n: 3, l: 2, m: 0, desc: "Dos lóbulos mayores en el eje Z rodeados por un anillo o toroide ecuatorial en el plano XY." },
        { id: "3d_xy", name: "Orbital 3d xy (Trébol Cuatrilobulado)", n: 3, l: 2, m: -2, desc: "Cuatro lóbulos simétricos situados entre los ejes X e Y." }
    ],
    principles: {
        heisenberg: "Principio de Incertidumbre: delta_x * delta_p >= hbar / 2 (no existen órbitas planetarias cerradas, solo orbitales de probabilidad).",
        pauli: "Principio de Exclusión de Pauli: Dos electrones no pueden poseer los mismos 4 números cuánticos en un mismo átomo."
    }
};

window.QUANTUM_ATOM_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <defs>
    <radialGradient id="nucGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f43f5e"/>
      <stop offset="60%" stop-color="#be123c"/>
      <stop offset="100%" stop-color="#4c0519"/>
    </radialGradient>
    <radialGradient id="cloudGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#0284c7" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#020817" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1000" height="600" fill="#030712"/>
  <circle cx="500" cy="300" r="180" fill="url(#cloudGrad)"/>
  <ellipse cx="500" cy="220" rx="60" ry="80" fill="#38bdf8" opacity="0.6"/>
  <ellipse cx="500" cy="380" rx="60" ry="80" fill="#fbbf24" opacity="0.6"/>
  <circle cx="500" cy="300" r="16" fill="url(#nucGrad)"/>
  <text x="500" y="55" font-family="sans-serif" font-size="22" font-weight="bold" fill="#f8fafc" text-anchor="middle">ESTRUCTURA DEL ÁTOMO & ORBITALES CUÁNTICOS</text>
  <text x="500" y="85" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Nube de Probabilidad Cuántica |psi|^2 y Armónicos Esféricos</text>
  <text x="500" y="555" font-family="monospace" font-size="12" fill="#38bdf8" text-anchor="middle">Fase Positiva (Cian) • Fase Negativa (Ámbar) • Núcleo Central de Protones y Neutrones</text>
</svg>
`);

