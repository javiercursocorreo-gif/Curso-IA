// ==============================================================================
// ASSET FÍSICO-TEÓRICO: LAS 11 DIMENSIONES DEL UNIVERSO & CALABI-YAU 3D
// Procedencia: Teoría M (Edward Witten, 1995) & Geometría de Supercuerdas (CERN)
// 3 Dimensiones Espaciales + 1 Temporal + 6 Compactificadas Calabi-Yau + 1 Membrana
// ==============================================================================

window.DIMENSIONS_DATA = {
    title: "Las 11 Dimensiones del Universo & Variedad de Calabi-Yau",
    dimensions: [
        { dim: "1D", name: "Línea / Longitud", desc: "Movimiento estrictamente unidimensional hacia adelante y atrás." },
        { dim: "2D", name: "Plano / Área", desc: "Superficie bidimensional: longitud y anchura (círculos, polígonos)." },
        { dim: "3D", name: "Volumen Espacial", desc: "Nuestro mundo macroscópico observable: ancho, alto y profundidad tridimensional." },
        { dim: "4D", name: "Tiempo (Espacio-Tiempo)", desc: "La flecha de la entropía einsteiniana donde transcurre la causalidad física." },
        { dim: "5D a 10D", name: "Variedad de Calabi-Yau (6D Compactificadas)", desc: "Espacio geométrico complejo enrollado a escala de Planck (10^-35 m) donde vibran las supercuerdas fundamentales." },
        { dim: "11D", name: "Dimensión de Membrana (Teoría M)", desc: "La undécima dimensión que unifica las 5 teorías de supercuerdas en la Teoría M mediante branas multidimensionales." }
    ],
    calabiYauParams: {
        eulerCharacteristic: "-6 (3 generaciones de familias de fermiones en el Modelo Estándar)",
        holonomy: "SU(3) (Preserva N=1 supersimetría en 4D)",
        stringModes: "Modo cerrado (Gravitón sin masa) y modo abierto (Fotones, gluones, bosones débiles)"
    }
};

window.DIMENSIONS_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <defs>
    <radialGradient id="cyGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#818cf8"/>
      <stop offset="40%" stop-color="#4f46e5"/>
      <stop offset="80%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#050714"/>
    </radialGradient>
  </defs>
  <rect width="1000" height="600" fill="#040612"/>
  <circle cx="500" cy="300" r="220" fill="url(#cyGrad)" opacity="0.4"/>
  <path d="M 350,300 C 400,200 600,200 650,300 C 600,400 400,400 350,300 Z" fill="none" stroke="#38bdf8" stroke-width="2.5" opacity="0.8"/>
  <path d="M 500,150 C 420,250 420,350 500,450 C 580,350 580,250 500,150 Z" fill="none" stroke="#c084fc" stroke-width="2.5" opacity="0.7"/>
  <text x="500" y="55" font-family="sans-serif" font-size="22" font-weight="bold" fill="#f8fafc" text-anchor="middle">LAS 11 DIMENSIONES DEL UNIVERSO & TEORÍA M</text>
  <text x="500" y="85" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Proyección Tridimensional de la Variedad de Calabi-Yau en la Escala de Planck</text>
  <text x="500" y="550" font-family="monospace" font-size="12" fill="#38bdf8" text-anchor="middle">Holonomía SU(3) • 6 Dimensiones Compactificadas • Modos Vibracionales de Cuerdas</text>
</svg>
`);

