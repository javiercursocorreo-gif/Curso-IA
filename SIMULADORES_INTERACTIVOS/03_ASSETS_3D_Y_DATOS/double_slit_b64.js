// ==============================================================================
// ASSET CUÁNTICO: EXPERIMENTO DE LA DOBLE RENDIJA & DUALIDAD ONDA-PARTÍCULA 3D
// Procedencia: Óptica Cuántica de Thomas Young (1801) & Hipótesis de De Broglie (1924)
// Función de Onda: Psi • Patrón de Interferencia vs Colapso por Observación (Detector)
// ==============================================================================

window.DOUBLE_SLIT_DATA = {
    title: "Experimento de la Doble Rendija & Dualidad Onda-Partícula",
    history: "Thomas Young demostró la naturaleza ondulatoria de la luz en 1801; en el siglo XX, el experimento con electrones y fotones individuales reveló la superposición cuántica.",
    quantumParadox: {
        withoutDetector: "Sin observador en las rendijas: Cada partícula atraviesa ambas rendijas simultáneamente como onda de probabilidad, produciendo un patrón de franjas de interferencia constructiva y destructiva en la pantalla detectora (d * sin(theta) = m * lambda).",
        withDetector: "Con detector en las rendijas: El acto de medición destruye la superposición cuántica (colapso de la función de onda), obligando a la partícula a decidir por cuál rendija cruzar. El patrón de interferencia desaparece y quedan únicamente dos bandas clásicas."
    },
    setup: {
        source: "Cañón de electrones / Láser monocromático (532 nm)",
        slitDistance: "d = 0.25 mm",
        screenDistance: "L = 1.20 metros"
    }
};

window.DOUBLE_SLIT_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <rect width="1000" height="600" fill="#030614"/>
  <rect x="360" y="80" width="16" height="180" fill="#64748b"/>
  <rect x="360" y="280" width="16" height="40" fill="#64748b"/>
  <rect x="360" y="340" width="16" height="180" fill="#64748b"/>
  <rect x="850" y="80" width="18" height="440" fill="#1e293b" stroke="#38bdf8"/>
  <path d="M 380,270 Q 550,220 850,150" fill="none" stroke="#22c55e" stroke-width="2" opacity="0.6"/>
  <path d="M 380,270 Q 550,300 850,300" fill="none" stroke="#22c55e" stroke-width="3" opacity="0.8"/>
  <path d="M 380,330 Q 550,300 850,300" fill="none" stroke="#22c55e" stroke-width="3" opacity="0.8"/>
  <path d="M 380,330 Q 550,380 850,450" fill="none" stroke="#22c55e" stroke-width="2" opacity="0.6"/>
  <circle cx="160" cy="300" r="14" fill="#38bdf8"/>
  <text x="500" y="55" font-family="sans-serif" font-size="22" font-weight="bold" fill="#f8fafc" text-anchor="middle">EXPERIMENTO DE LA DOBLE RENDIJA & DUALIDAD ONDA-PARTÍCULA</text>
  <text x="500" y="85" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Young (1801) / De Broglie (1924) • Interferencia Cuántica vs Colapso por Observación</text>
  <text x="500" y="560" font-family="monospace" font-size="12" fill="#22c55e" text-anchor="middle">Sin detector: Franjas de interferencia • Con detector: Dos bandas clásicas (Colapso)</text>
</svg>
`);

