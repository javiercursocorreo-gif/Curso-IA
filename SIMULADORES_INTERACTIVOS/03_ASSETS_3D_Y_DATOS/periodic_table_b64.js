// ==============================================================================
// ASSET QUÍMICO: TABLA PERIÓDICA INTERACTIVA & ENLACES QUÍMICOS 3D
// Procedencia: IUPAC (Unión Internacional de Química Pura y Aplicada) & Teoría VSEPR
// 118 Elementos Químicos • Enlaces Covalentes, Iónicos y Metálicos Tridimensionales
// ==============================================================================

window.PERIODIC_DATA = {
    title: "Tabla Periódica de los Elementos & Enlaces Moleculares 3D",
    blocks: [
        { name: "Bloque s", elements: "Hidrógeno, Alcalinos y Alcalinotérreos (Grupos 1 y 2)", color: "#f87171" },
        { name: "Bloque p", elements: "No metales, Halógenos y Gases Nobles (Grupos 13 a 18)", color: "#fbbf24" },
        { name: "Bloque d", elements: "Metales de Transición (Grupos 3 a 12)", color: "#38bdf8" },
        { name: "Bloque f", elements: "Lantánidos y Actínidos (Tierras raras y radiactivos)", color: "#c084fc" }
    ],
    molecules: [
        {
            name: "Agua (H2O)", type: "Enlace Covalente Polar", geometry: "Angular (104.5°)",
            atoms: [
                { elem: "O", x: 0, y: 0.4, z: 0, color: "#ef4444", radius: 1.2 },
                { elem: "H", x: -1.2, y: -0.6, z: 0, color: "#f8fafc", radius: 0.7 },
                { elem: "H", x: 1.2, y: -0.6, z: 0, color: "#f8fafc", radius: 0.7 }
            ],
            desc: "Momento dipolar permanente que permite los puentes de hidrógeno y la vida en la Tierra."
        },
        {
            name: "Metano (CH4)", type: "Enlace Covalente Apolar", geometry: "Tetraédrica (109.5°)",
            atoms: [
                { elem: "C", x: 0, y: 0, z: 0, color: "#334155", radius: 1.3 },
                { elem: "H", x: 0, y: 1.4, z: 0, color: "#f8fafc", radius: 0.7 },
                { elem: "H", x: 1.3, y: -0.5, z: 0.6, color: "#f8fafc", radius: 0.7 },
                { elem: "H", x: -1.3, y: -0.5, z: 0.6, color: "#f8fafc", radius: 0.7 },
                { elem: "H", x: 0, y: -0.5, z: -1.4, color: "#f8fafc", radius: 0.7 }
            ],
            desc: "Gas natural fundamental; hibridación sp3 del carbono con simetría tetraédrica perfecta."
        },
        {
            name: "Cloruro de Sodio (NaCl)", type: "Enlace Iónico", geometry: "Red Cúbica Centrada en las Caras",
            atoms: [
                { elem: "Na+", x: -1.0, y: 0, z: 0, color: "#a855f7", radius: 1.0 },
                { elem: "Cl-", x: 1.0, y: 0, z: 0, color: "#22c55e", radius: 1.5 }
            ],
            desc: "Transferencia completa del electrón de valencia del sodio al cloro formando una red cristalina salina."
        }
    ]
};

window.PERIODIC_SVG_B64 = "data:image/svg+xml;base64," + btoa(`
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <rect width="1000" height="600" fill="#040817"/>
  <text x="500" y="55" font-family="sans-serif" font-size="22" font-weight="bold" fill="#f8fafc" text-anchor="middle">TABLA PERIÓDICA DE LOS ELEMENTOS & ENLACES QUÍMICOS</text>
  <text x="500" y="85" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">IUPAC • Geometría Molecular VSEPR (Agua H2O, Metano CH4 y Sal NaCl)</text>
  <rect x="120" y="490" width="180" height="24" rx="6" fill="#f87171" opacity="0.8"/>
  <text x="210" y="507" font-family="sans-serif" font-size="12" fill="#fff" font-weight="bold" text-anchor="middle">Bloque s (Alcalinos)</text>
  <rect x="320" y="490" width="180" height="24" rx="6" fill="#38bdf8" opacity="0.8"/>
  <text x="410" y="507" font-family="sans-serif" font-size="12" fill="#fff" font-weight="bold" text-anchor="middle">Bloque d (Transición)</text>
  <rect x="520" y="490" width="180" height="24" rx="6" fill="#fbbf24" opacity="0.8"/>
  <text x="610" y="507" font-family="sans-serif" font-size="12" fill="#030712" font-weight="bold" text-anchor="middle">Bloque p (No Metales)</text>
  <rect x="720" y="490" width="160" height="24" rx="6" fill="#c084fc" opacity="0.8"/>
  <text x="800" y="507" font-family="sans-serif" font-size="12" fill="#fff" font-weight="bold" text-anchor="middle">Bloque f (Tierras Raras)</text>
</svg>
`);

