// ==============================================================================
// ASSET CUÁNTICO: COMPUTACIÓN CUÁNTICA, QUBITS & ESFERA DE BLOCH 3D
// Procedencia: Félix Bloch (1946) & Computación Cuántica (Nielsen & Chuang)
// Estado Qubit: |psi> = cos(theta/2)|0> + e^(i*phi)*sin(theta/2)|1>
// Puertas Cuánticas: Pauli X, Y, Z, Hadamard (H), Fase (S, T)
// ==============================================================================

window.BLOCH_DATA = {
    title: "Computación Cuántica: Qubits & Esfera de Bloch",
    stateFormula: "|psi> = cos(theta/2)|0> + e^(i*phi)*sin(theta/2)|1>",
    poles: {
        north: "|0> (Estado Base Clásico 0 - Probabilidad 100% de medir 0)",
        south: "|1> (Estado Excitado Clásico 1 - Probabilidad 100% de medir 1)",
        equatorPlus: "|+> = (|0> + |1>) / sqrt(2) (Superposición coherente equiprobable 50/50)",
        equatorMinus: "|-> = (|0> - |1>) / sqrt(2) (Superposición con desfase relativo de pi)"
    },
    quantumGates: [
        { name: "NOT Cuántica (Pauli-X)", effect: "Rotación de 180° (pi) sobre el eje X: invierte |0> a |1> y viceversa." },
        { name: "Puerta Hadamard (H)", effect: "Lleva el polo |0> al ecuador |+>: crea superposición cuántica pura." },
        { name: "Puerta de Fase (Pauli-Z)", effect: "Rotación de 180° en torno al eje Z: cambia la fase de |1> sin alterar las probabilidades." },
        { name: "Puerta S", effect: "Rotación de 90° (pi/2) en el eje Z." },
        { name: "Medición Proyectiva", effect: "Colapsa el vector |psi> instantáneamente a |0> o |1> según las probabilidades cos²(theta/2) y sin²(theta/2)." }
    ]
};

window.BLOCH_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <rect width="1000" height="600" fill="#040714"/>
  <circle cx="500" cy="300" r="180" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.4"/>
  <ellipse cx="500" cy="300" rx="180" ry="60" fill="none" stroke="#64748b" stroke-dasharray="4,6" opacity="0.6"/>
  <line x1="500" y1="90" x2="500" y2="510" stroke="#f8fafc" stroke-width="2"/>
  <line x1="300" y1="300" x2="700" y2="300" stroke="#f8fafc" stroke-width="2"/>
  <text x="500" y="80" font-family="sans-serif" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">|0&gt; (Polo Norte)</text>
  <text x="500" y="535" font-family="sans-serif" font-size="16" font-weight="bold" fill="#f43f5e" text-anchor="middle">|1&gt; (Polo Sur)</text>
  <line x1="500" y1="300" x2="610" y2="180" stroke="#fbbf24" stroke-width="4"/>
  <circle cx="610" cy="180" r="7" fill="#fbbf24"/>
  <text x="625" y="185" font-family="sans-serif" font-size="15" font-weight="bold" fill="#fbbf24">|psi&gt;</text>
  <text x="500" y="50" font-family="sans-serif" font-size="22" font-weight="bold" fill="#f8fafc" text-anchor="middle">ESFERA DE BLOCH & COMPUTACIÓN CUÁNTICA</text>
  <text x="500" y="570" font-family="monospace" font-size="12" fill="#38bdf8" text-anchor="middle">Estado |psi&gt; = cos(theta/2)|0&gt; + e^(i*phi)*sin(theta/2)|1&gt; • Superposición Cuántica y Puertas Lógicas</text>
</svg>
`);

