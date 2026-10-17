// intervals.js - Colección ampliada de piezas y entrenamientos del gimnasio visual
window.EXERCISES = [
    {
        id: "ex_ode_to_joy",
        title: "Himno de la Alegría (L. v. Beethoven) - Melodía Completa",
        composer: "Ludwig van Beethoven",
        timeSignature: [4, 4],
        keySignature: "C",
        defaultBpm: 95,
        measures: [
            // Compás 1
            {
                number: 1,
                rightHand: {
                    vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                    notes: [
                        { pitch: 64, name: "MI", finger: "3", duration: 1.0, isAnchor: true },
                        { pitch: 64, name: "MI", duration: 1.0, isSecondary: true },
                        { pitch: 65, name: "FA", finger: "4", duration: 1.0, isSecondary: true },
                        { pitch: 67, name: "SOL", finger: "5", duration: 1.0, isSecondary: true }
                    ]
                },
                leftHand: {
                    bass: { pitch: 48, name: "DO", finger: "5", duration: 2.0, isAnchor: true },
                    chordBlock: {
                        color: "rgba(249, 115, 22, 0.35)",
                        borderColor: "#ea580c",
                        fingers: "1-3-5",
                        anchorNote: "DO",
                        beats: [
                            { duration: 2.0, pitches: [48, 52, 55] },
                            { duration: 2.0, pitches: [48, 52, 55] }
                        ]
                    }
                }
            },
            // Compás 2
            {
                number: 2,
                rightHand: {
                    vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                    notes: [
                        { pitch: 67, name: "SOL", finger: "5", duration: 1.0, isAnchor: true },
                        { pitch: 65, name: "FA", finger: "4", duration: 1.0, isSecondary: true },
                        { pitch: 64, name: "MI", finger: "3", duration: 1.0, isSecondary: true },
                        { pitch: 62, name: "RE", finger: "2", duration: 1.0, isSecondary: true }
                    ]
                },
                leftHand: {
                    bass: { pitch: 43, name: "SOL", finger: "5", duration: 2.0, isAnchor: true },
                    chordBlock: {
                        color: "rgba(249, 115, 22, 0.35)",
                        borderColor: "#ea580c",
                        fingers: "1-3-5",
                        anchorNote: "SOL",
                        beats: [
                            { duration: 2.0, pitches: [47, 50, 55] },
                            { duration: 2.0, pitches: [47, 50, 55] }
                        ]
                    }
                }
            },
            // Compás 3
            {
                number: 3,
                rightHand: {
                    vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                    notes: [
                        { pitch: 60, name: "DO", finger: "1", duration: 1.0, isAnchor: true },
                        { pitch: 60, name: "DO", duration: 1.0, isSecondary: true },
                        { pitch: 62, name: "RE", finger: "2", duration: 1.0, isSecondary: true },
                        { pitch: 64, name: "MI", finger: "3", duration: 1.0, isSecondary: true }
                    ]
                },
                leftHand: {
                    bass: { pitch: 48, name: "DO", finger: "5", duration: 2.0, isAnchor: true },
                    chordBlock: {
                        color: "rgba(249, 115, 22, 0.35)",
                        borderColor: "#ea580c",
                        fingers: "1-3-5",
                        anchorNote: "DO",
                        beats: [
                            { duration: 2.0, pitches: [48, 52, 55] },
                            { duration: 2.0, pitches: [48, 52, 55] }
                        ]
                    }
                }
            },
            // Compás 4
            {
                number: 4,
                rightHand: {
                    vector: { color: "rgba(168, 85, 247, 0.35)", borderColor: "#9333ea" },
                    notes: [
                        { pitch: 64, name: "MI", finger: "3", duration: 1.5, isAnchor: true },
                        { pitch: 62, name: "RE", finger: "2", duration: 0.5, isSecondary: true },
                        { pitch: 62, name: "RE", duration: 2.0, isSecondary: true }
                    ]
                },
                leftHand: {
                    bass: { pitch: 43, name: "SOL", finger: "5", duration: 2.0, isAnchor: true },
                    chordBlock: {
                        color: "rgba(249, 115, 22, 0.35)",
                        borderColor: "#ea580c",
                        fingers: "1-3-5",
                        anchorNote: "SOL",
                        beats: [
                            { duration: 2.0, pitches: [47, 50, 55] },
                            { duration: 2.0, pitches: [47, 50, 55] }
                        ]
                    }
                }
            }
        ]
    }
];
