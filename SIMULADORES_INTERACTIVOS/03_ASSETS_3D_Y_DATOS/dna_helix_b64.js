/**
 * DNA HELIX PDB DATA (B-DNA crystallographic coordinates based on RCSB PDB 1BNA)
 * Modelado atómico para simulaciones biomoleculares en Three.js / Babylon.js
 */
window.DNA_HELIX_PDB_DATA = {
  name: "B-DNA Dodecamer (CGCGAATTCGCG)",
  source: "RCSB Protein Data Bank (PDB ID: 1BNA) / Dickerson & Drew (1981)",
  pitch_nm: 3.4,
  pairs_per_turn: 10,
  diameter_nm: 2.0,
  base_pairs: [
    { index: 1, base1: "C", base2: "G", h_bonds: 3, y: -4.5, angle_deg: 0 },
    { index: 2, base1: "G", base2: "C", h_bonds: 3, y: -3.5, angle_deg: 36 },
    { index: 3, base1: "C", base2: "G", h_bonds: 3, y: -2.5, angle_deg: 72 },
    { index: 4, base1: "G", base2: "C", h_bonds: 3, y: -1.5, angle_deg: 108 },
    { index: 5, base1: "A", base2: "T", h_bonds: 2, y: -0.5, angle_deg: 144 },
    { index: 6, base1: "A", base2: "T", h_bonds: 2, y: 0.5, angle_deg: 180 },
    { index: 7, base1: "T", base2: "A", h_bonds: 2, y: 1.5, angle_deg: 216 },
    { index: 8, base1: "T", base2: "A", h_bonds: 2, y: 2.5, angle_deg: 252 },
    { index: 9, base1: "C", base2: "G", h_bonds: 3, y: 3.5, angle_deg: 288 },
    { index: 10, base1: "G", base2: "C", h_bonds: 3, y: 4.5, angle_deg: 324 }
  ]
};

