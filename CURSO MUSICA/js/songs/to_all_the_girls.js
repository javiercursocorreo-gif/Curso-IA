// to_all_the_girls.js - "To All The Girls I've Loved Before" (arr: Don Quattrocchi)
// Calibración exacta y perfecta dictada por el usuario:
// Compás 1: G4 - C5 - B4 - D5 - C5
// Compás 2: E5 - G4 - G4
window.TO_ALL_THE_GIRLS = {
    id: "to_all_the_girls",
    title: "To All The Girls I've Loved Before",
    composer: "Albert Hammond & Hal David (arr. Don Quattrocchi)",
    timeSignature: [4, 4],
    keySignature: "C",
    defaultBpm: 88,
    isLeadSheet: true,
    measures: [
        // ==================== SISTEMA 1 (Compases 1 - 4) ====================
        // Compás 1: To all the girls I've (C) -> G4 - C5 - B4 - D5 - C5
        {
            number: 1,
            chord: "C",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isAnchor: true },  // To (G4)
                    { pitch: 72, name: "DO", finger: "3", duration: 0.5, isSecondary: true }, // all (C5)
                    { pitch: 71, name: "SI", finger: "2", duration: 0.5, isSecondary: true }, // the (B4)
                    { pitch: 74, name: "RE", finger: "4", duration: 0.5, isSecondary: true }, // girls (D5)
                    { pitch: 72, name: "DO", finger: "3", duration: 0.5, isAnchor: true }    // I've (C5)
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [48, 52, 55] }] } }
        },
        // Compás 2: loved be - fore (C) -> E5 - G4 - G4
        {
            number: 2,
            chord: "C",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 76, name: "MI", finger: "5", duration: 1.5, isAnchor: true },   // loved (E5)
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isSecondary: true },// be- (G4)
                    { pitch: 67, name: "SOL", duration: 2.0, isSecondary: true }             // fore (G4)
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [48, 52, 55] }] } }
        },
        // Compás 3: who trave - ed in and out (Dm) -> G4 - D5 - C5 - E5 - D5
        {
            number: 3,
            chord: "Dm",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isAnchor: true },  // who (G4)
                    { pitch: 74, name: "RE", finger: "4", duration: 0.5, isSecondary: true }, // tra- (D5)
                    { pitch: 72, name: "DO", finger: "3", duration: 0.5, isSecondary: true }, // veled (C5)
                    { pitch: 76, name: "MI", finger: "5", duration: 0.5, isSecondary: true }, // in (E5)
                    { pitch: 74, name: "RE", finger: "4", duration: 0.5, isAnchor: true }    // out (D5)
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [50, 53, 57] }] } }
        },
        // Compás 4: my door (Dm) -> F5 - G4 - G4
        {
            number: 4,
            chord: "Dm",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 77, name: "FA", finger: "5", duration: 1.5, isAnchor: true },   // my (F5)
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isSecondary: true },// - (G4)
                    { pitch: 67, name: "SOL", duration: 2.0, isSecondary: true }             // door (G4)
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [50, 53, 57] }] } }
        },

        // ==================== SISTEMA 2 (Compases 5 - 8) ====================
        // Compás 5: i'm glad the came a - long (G7) -> G4 - E5 - D5 - F5 - E5 - D5
        {
            number: 5,
            chord: "G7",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isAnchor: true },  // I'm (G4)
                    { pitch: 76, name: "MI", finger: "4", duration: 0.5, isSecondary: true }, // glad (E5)
                    { pitch: 74, name: "RE", finger: "3", duration: 0.5, isSecondary: true }, // the (D5)
                    { pitch: 77, name: "FA", finger: "5", duration: 0.5, isSecondary: true }, // came (F5)
                    { pitch: 76, name: "MI", finger: "4", duration: 0.5, isSecondary: true }, // a- (E5)
                    { pitch: 74, name: "RE", finger: "3", duration: 1.5, isAnchor: true }    // long (D5)
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [47, 50, 53, 55] }] } }
        },
        // Compás 6: i de - di - cate this song (G7) -> G4 - E5 - D5 - F5 - E5 - D5
        {
            number: 6,
            chord: "G7",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isAnchor: true },  // I (G4)
                    { pitch: 76, name: "MI", finger: "4", duration: 0.5, isSecondary: true }, // de- (E5)
                    { pitch: 74, name: "RE", finger: "3", duration: 0.5, isSecondary: true }, // di- (D5)
                    { pitch: 77, name: "FA", finger: "5", duration: 0.5, isSecondary: true }, // cate (F5)
                    { pitch: 76, name: "MI", finger: "4", duration: 0.5, isSecondary: true }, // this (E5)
                    { pitch: 74, name: "RE", finger: "3", duration: 1.5, isAnchor: true }    // song (D5)
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [47, 50, 53, 55] }] } }
        },
        // Compás 7: to all the girls i've loved (C) -> E5 - D5 - C5 - B4 - D5 - C5
        {
            number: 7,
            chord: "C",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 76, name: "MI", finger: "5", duration: 0.5, isAnchor: true },   // to (E5)
                    { pitch: 74, name: "RE", finger: "4", duration: 0.5, isSecondary: true }, // all (D5)
                    { pitch: 72, name: "DO", finger: "3", duration: 0.5, isSecondary: true }, // the (C5)
                    { pitch: 71, name: "SI", finger: "2", duration: 0.5, isSecondary: true }, // girls (B4)
                    { pitch: 74, name: "RE", finger: "4", duration: 0.5, isSecondary: true }, // I've (D5)
                    { pitch: 72, name: "DO", finger: "3", duration: 1.5, isAnchor: true }    // loved (C5)
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [48, 52, 55] }] } }
        },
        // Compás 8: be - fore (C) -> G4 - G4
        {
            number: 8,
            chord: "C",
            rightHand: {
                vector: { color: "rgba(16, 185, 129, 0.35)", borderColor: "#10b981" },
                notes: [
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isAnchor: true },  // be- (G4)
                    { pitch: 67, name: "SOL", duration: 3.0, isSecondary: true }             // fore (G4)
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [48, 52, 55] }] } }
        },

        // ==================== SISTEMA 3 (Compases 9 - 12) ====================
        // Compás 9: to all the girls i once (C) -> G4 - C5 - B4 - D5 - C5
        {
            number: 9,
            chord: "C",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isAnchor: true },
                    { pitch: 72, name: "DO", finger: "3", duration: 0.5, isSecondary: true },
                    { pitch: 71, name: "SI", finger: "2", duration: 0.5, isSecondary: true },
                    { pitch: 74, name: "RE", finger: "4", duration: 0.5, isSecondary: true },
                    { pitch: 72, name: "DO", finger: "3", duration: 0.5, isAnchor: true }
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [48, 52, 55] }] } }
        },
        // Compás 10: caressed (C) -> E5 - G4 - G4
        {
            number: 10,
            chord: "C",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 76, name: "MI", finger: "5", duration: 1.5, isAnchor: true },
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isSecondary: true },
                    { pitch: 67, name: "SOL", duration: 2.0, isSecondary: true }
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [48, 52, 55] }] } }
        },
        // Compás 11: and may i say i'ved (Dm) -> G4 - D5 - C5 - E5 - D5
        {
            number: 11,
            chord: "Dm",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isAnchor: true },
                    { pitch: 74, name: "RE", finger: "4", duration: 0.5, isSecondary: true },
                    { pitch: 72, name: "DO", finger: "3", duration: 0.5, isSecondary: true },
                    { pitch: 76, name: "MI", finger: "5", duration: 0.5, isSecondary: true },
                    { pitch: 74, name: "RE", finger: "4", duration: 0.5, isAnchor: true }
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [50, 53, 57] }] } }
        },
        // Compás 12: held the best (Dm) -> F5 - G4 - G4
        {
            number: 12,
            chord: "Dm",
            rightHand: {
                vector: { color: "rgba(59, 130, 246, 0.35)", borderColor: "#2563eb" },
                notes: [
                    { pitch: 77, name: "FA", finger: "5", duration: 1.5, isAnchor: true },
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isSecondary: true },
                    { pitch: 67, name: "SOL", duration: 2.0, isSecondary: true }
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [50, 53, 57] }] } }
        },

        // ==================== SISTEMA 5: ESTRIBILLO (Compases 17 - 20) ====================
        // Compás 17: The winds of changeare al - ways (C) -> G4 - E5 - E5 - E5 - E5 - E5 - E5 - F5
        {
            number: 17,
            chord: "C",
            rightHand: {
                vector: { color: "rgba(168, 85, 247, 0.35)", borderColor: "#a855f7" },
                notes: [
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isAnchor: true },  // The (G4)
                    { pitch: 76, name: "MI", finger: "4", duration: 0.5, isSecondary: true }, // winds (E5)
                    { pitch: 76, name: "MI", duration: 0.5, isSecondary: true },             // of
                    { pitch: 76, name: "MI", duration: 0.5, isSecondary: true },             // change
                    { pitch: 76, name: "MI", duration: 0.5, isSecondary: true },             // are
                    { pitch: 76, name: "MI", duration: 0.5, isSecondary: true },             // al-
                    { pitch: 76, name: "MI", duration: 0.5, isSecondary: true },             // ways
                    { pitch: 77, name: "FA", finger: "5", duration: 0.5, isAnchor: true }    // blow- (F5)
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [48, 52, 55] }] } }
        },
        // Compás 18: blow - ing (C) -> E5 (blanca)
        {
            number: 18,
            chord: "C",
            rightHand: {
                vector: { color: "rgba(168, 85, 247, 0.35)", borderColor: "#a855f7" },
                notes: [
                    { pitch: 76, name: "MI", finger: "4", duration: 2.0, isAnchor: true }
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [48, 52, 55] }] } }
        },
        // Compás 19: and ev - vry time i try to stay (Dm) -> G4 - D5 - D5 - D5 - D5 - D5 - D5 - E5
        {
            number: 19,
            chord: "Dm",
            rightHand: {
                vector: { color: "rgba(168, 85, 247, 0.35)", borderColor: "#a855f7" },
                notes: [
                    { pitch: 67, name: "SOL", finger: "1", duration: 0.5, isAnchor: true },  // and (G4)
                    { pitch: 74, name: "RE", finger: "3", duration: 0.5, isSecondary: true }, // ev- (D5)
                    { pitch: 74, name: "RE", duration: 0.5, isSecondary: true },             // vry
                    { pitch: 74, name: "RE", duration: 0.5, isSecondary: true },             // time
                    { pitch: 74, name: "RE", duration: 0.5, isSecondary: true },             // I
                    { pitch: 74, name: "RE", duration: 0.5, isSecondary: true },             // try
                    { pitch: 74, name: "RE", duration: 0.5, isSecondary: true },             // to
                    { pitch: 76, name: "MI", finger: "4", duration: 0.5, isAnchor: true }    // stay (E5)
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [50, 53, 57] }] } }
        },
        // Compás 20: stay (Dm) -> D5 (blanca con puntillo)
        {
            number: 20,
            chord: "Dm",
            rightHand: {
                vector: { color: "rgba(168, 85, 247, 0.35)", borderColor: "#a855f7" },
                notes: [
                    { pitch: 74, name: "RE", finger: "3", duration: 3.0, isAnchor: true }
                ]
            },
            leftHand: { chordBlock: { beats: [{ pitches: [50, 53, 57] }] } }
        }
    ]
};
