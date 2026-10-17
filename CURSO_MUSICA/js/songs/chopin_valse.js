// chopin_valse.js - Vals en La menor B.150 de Frédéric Chopin (Tema principal completo: 16 compases)
window.CHOPIN_VALSE = {
    id: "chopin_valse_am",
    title: "Vals en La menor (B. 150) - Tema Completo",
    composer: "Frédéric Chopin",
    timeSignature: [3, 4],
    keySignature: "Am",
    defaultBpm: 90,
    measures: [
        // Compás 1
        {
            number: 1,
            rightHand: {
                vector: { color: "rgba(100, 160, 255, 0.35)", borderColor: "#3b82f6" },
                notes: [
                    { pitch: 69, name: "LA", finger: "2", duration: 0.5, isAnchor: true },
                    { pitch: 71, name: "SI", duration: 0.5, isSecondary: true },
                    { pitch: 72, name: "DO", finger: "4", duration: 1.0, isSecondary: true },
                    { pitch: 69, name: "LA", finger: "1", duration: 1.0, isSecondary: true }
                ]
            },
            leftHand: {
                bass: { pitch: 45, name: "LA", finger: "5", duration: 1.0, isAnchor: true },
                chordBlock: {
                    color: "rgba(255, 140, 80, 0.35)",
                    borderColor: "#f97316",
                    fingers: "1-2-4",
                    anchorNote: "LA",
                    beats: [
                        { duration: 1.0, pitches: [52, 57, 60] },
                        { duration: 1.0, pitches: [52, 57, 60] }
                    ]
                }
            }
        },
        // Compás 2
        {
            number: 2,
            rightHand: {
                vector: { color: "rgba(100, 160, 255, 0.35)", borderColor: "#3b82f6" },
                notes: [
                    { pitch: 74, name: "RE", finger: "4", duration: 1.5, isAnchor: true },
                    { pitch: 72, name: "DO", duration: 0.5, isSecondary: true },
                    { pitch: 71, name: "SI", duration: 1.0, isSecondary: true }
                ]
            },
            leftHand: {
                bass: { pitch: 50, name: "RE", finger: "5", duration: 1.0, isAnchor: true },
                chordBlock: {
                    color: "rgba(255, 140, 80, 0.35)",
                    borderColor: "#f97316",
                    fingers: "1-2-4",
                    anchorNote: "LA",
                    beats: [
                        { duration: 1.0, pitches: [53, 57, 62] },
                        { duration: 1.0, pitches: [53, 57, 62] }
                    ]
                }
            }
        },
        // Compás 3
        {
            number: 3,
            rightHand: {
                vector: { color: "rgba(100, 160, 255, 0.35)", borderColor: "#3b82f6" },
                notes: [
                    { pitch: 71, name: "SI", finger: "1", duration: 0.5, isAnchor: true },
                    { pitch: 72, name: "DO", duration: 0.5, isSecondary: true },
                    { pitch: 74, name: "RE", duration: 0.5, isSecondary: true },
                    { pitch: 76, name: "MI", duration: 0.5, isSecondary: true },
                    { pitch: 81, name: "LA", finger: "5", duration: 1.0, isAnchor: true }
                ]
            },
            leftHand: {
                bass: { pitch: 43, name: "SOL", finger: "5", duration: 1.0, isAnchor: true },
                chordBlock: {
                    color: "rgba(255, 140, 80, 0.35)",
                    borderColor: "#f97316",
                    fingers: "1-3-5",
                    anchorNote: "SOL",
                    beats: [
                        { duration: 1.0, pitches: [50, 55, 59] },
                        { duration: 1.0, pitches: [50, 55, 59] }
                    ]
                }
            }
        },
        // Compás 4
        {
            number: 4,
            rightHand: {
                vector: { color: "rgba(168, 85, 247, 0.35)", borderColor: "#a855f7" },
                notes: [
                    { pitch: 76, name: "MI", finger: "1-4-3", duration: 1.0, isAnchor: true, ornament: "tr" },
                    { pitch: 76, name: "MI", duration: 0.5, isSecondary: true },
                    { pitch: 75, name: "RE#", finger: "2", duration: 0.5, isSecondary: true, accidental: "#" },
                    { pitch: 76, name: "MI", finger: "3", duration: 1.0, isSecondary: true }
                ]
            },
            leftHand: {
                bass: { pitch: 48, name: "DO", finger: "5", duration: 1.0, isAnchor: true },
                chordBlock: {
                    color: "rgba(255, 140, 80, 0.35)",
                    borderColor: "#f97316",
                    fingers: "1-2-4",
                    anchorNote: "SOL",
                    beats: [
                        { duration: 1.0, pitches: [52, 55, 60] },
                        { duration: 1.0, pitches: [52, 55, 60] }
                    ]
                }
            }
        },
        // Compás 5
        {
            number: 5,
            rightHand: {
                vector: { color: "rgba(100, 160, 255, 0.35)", borderColor: "#3b82f6" },
                notes: [
                    { pitch: 69, name: "LA", finger: "1", duration: 0.5, isAnchor: true },
                    { pitch: 71, name: "SI", duration: 0.5, isSecondary: true },
                    { pitch: 72, name: "DO", finger: "3", duration: 1.0, isSecondary: true },
                    { pitch: 74, name: "RE", finger: "4", duration: 1.0, isSecondary: true }
                ]
            },
            leftHand: {
                bass: { pitch: 45, name: "LA", finger: "5", duration: 1.0, isAnchor: true },
                chordBlock: {
                    color: "rgba(255, 140, 80, 0.35)",
                    borderColor: "#f97316",
                    fingers: "1-2-4",
                    anchorNote: "LA",
                    beats: [
                        { duration: 1.0, pitches: [52, 57, 60] },
                        { duration: 1.0, pitches: [52, 57, 60] }
                    ]
                }
            }
        },
        // Compás 6
        {
            number: 6,
            rightHand: {
                vector: { color: "rgba(100, 160, 255, 0.35)", borderColor: "#3b82f6" },
                notes: [
                    { pitch: 76, name: "MI", finger: "5", duration: 1.5, isAnchor: true },
                    { pitch: 74, name: "RE", duration: 0.5, isSecondary: true },
                    { pitch: 72, name: "DO", duration: 1.0, isSecondary: true }
                ]
            },
            leftHand: {
                bass: { pitch: 50, name: "RE", finger: "5", duration: 1.0, isAnchor: true },
                chordBlock: {
                    color: "rgba(255, 140, 80, 0.35)",
                    borderColor: "#f97316",
                    fingers: "1-2-4",
                    anchorNote: "LA",
                    beats: [
                        { duration: 1.0, pitches: [53, 57, 62] },
                        { duration: 1.0, pitches: [53, 57, 62] }
                    ]
                }
            }
        },
        // Compás 7
        {
            number: 7,
            rightHand: {
                vector: { color: "rgba(100, 160, 255, 0.35)", borderColor: "#3b82f6" },
                notes: [
                    { pitch: 71, name: "SI", finger: "2", duration: 1.0, isAnchor: true },
                    { pitch: 72, name: "DO", duration: 1.0, isSecondary: true },
                    { pitch: 68, name: "SOL#", finger: "1", duration: 1.0, isSecondary: true, accidental: "#" }
                ]
            },
            leftHand: {
                bass: { pitch: 40, name: "MI", finger: "5", duration: 1.0, isAnchor: true },
                chordBlock: {
                    color: "rgba(255, 140, 80, 0.35)",
                    borderColor: "#f97316",
                    fingers: "1-2-4",
                    anchorNote: "MI",
                    beats: [
                        { duration: 1.0, pitches: [50, 56, 59] }, // Re3, Sol#3, Si3 (E7)
                        { duration: 1.0, pitches: [50, 56, 59] }
                    ]
                }
            }
        },
        // Compás 8
        {
            number: 8,
            rightHand: {
                vector: { color: "rgba(16, 185, 129, 0.35)", borderColor: "#10b981" },
                notes: [
                    { pitch: 69, name: "LA", finger: "2", duration: 3.0, isAnchor: true }
                ]
            },
            leftHand: {
                bass: { pitch: 45, name: "LA", finger: "5", duration: 1.0, isAnchor: true },
                chordBlock: {
                    color: "rgba(255, 140, 80, 0.35)",
                    borderColor: "#f97316",
                    fingers: "1-2-4",
                    anchorNote: "LA",
                    beats: [
                        { duration: 1.0, pitches: [52, 57, 60] },
                        { duration: 1.0, pitches: [52, 57, 60] }
                    ]
                }
            }
        }
    ]
};
