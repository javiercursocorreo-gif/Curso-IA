// app.js - Orquestador principal de la aplicación
document.addEventListener('DOMContentLoaded', () => {
    // 1. Estado de la aplicación
    const state = {
        isPlaying: false,
        bpm: 88,
        currentMeasure: 0,
        playbackInterval: null,
        currentSong: window.TO_ALL_THE_GIRLS || window.CHOPIN_VALSE
    };

    // Inicializar con la partitura del PDF (To All The Girls I've Loved Before)
    window.scoreRenderer.render(state.currentSong);

    // 2. Referencias DOM
    const btnPlay = document.getElementById('btn-play');
    const btnStop = document.getElementById('btn-stop');
    const bpmSlider = document.getElementById('bpm-slider');
    const bpmVal = document.getElementById('bpm-val');
    const midiStatus = document.getElementById('midi-status');
    const songSelect = document.getElementById('song-select');

    // Botones de capas visuales PianoVista
    const btnModePianovista = document.getElementById('mode-pianovista');
    const btnModeSkeleton = document.getElementById('mode-skeleton');
    const btnModeTraditional = document.getElementById('mode-traditional');

    function updateModeButtons(activeMode) {
        [btnModePianovista, btnModeSkeleton, btnModeTraditional].forEach(btn => {
            if (btn) btn.classList.remove('active');
        });
        if (activeMode === 'pianovista') btnModePianovista.classList.add('active');
        if (activeMode === 'skeleton') btnModeSkeleton.classList.add('active');
        if (activeMode === 'traditional') btnModeTraditional.classList.add('active');
    }

    if (btnModePianovista) {
        btnModePianovista.addEventListener('click', () => {
            window.scoreRenderer.setMode('pianovista');
            updateModeButtons('pianovista');
        });
    }

    if (btnModeSkeleton) {
        btnModeSkeleton.addEventListener('click', () => {
            window.scoreRenderer.setMode('skeleton');
            updateModeButtons('skeleton');
        });
    }

    if (btnModeTraditional) {
        btnModeTraditional.addEventListener('click', () => {
            window.scoreRenderer.setMode('traditional');
            updateModeButtons('traditional');
        });
    }

    // Selector de piezas
    if (songSelect) {
        songSelect.value = "to_all_the_girls";
        songSelect.addEventListener('change', (e) => {
            stopPlayback();
            if (e.target.value === 'to_all_the_girls') {
                state.currentSong = window.TO_ALL_THE_GIRLS;
            } else if (e.target.value === 'chopin') {
                state.currentSong = window.CHOPIN_VALSE;
            } else if (e.target.value === 'intervals') {
                state.currentSong = window.EXERCISES[0];
            }
            state.bpm = state.currentSong.defaultBpm || 84;
            if (bpmSlider) bpmSlider.value = state.bpm;
            if (bpmVal) bpmVal.innerText = state.bpm;
            window.scoreRenderer.render(state.currentSong);
        });
    }

    // BPM Slider
    if (bpmSlider && bpmVal) {
        bpmSlider.addEventListener('input', (e) => {
            state.bpm = parseInt(e.target.value);
            bpmVal.innerText = state.bpm;
            if (state.isPlaying) {
                restartPlaybackInterval();
            }
        });
    }

    // 3. Lógica de Reproducción con Melodía Nota por Nota Real
    function startPlayback() {
        if (window.pianoAudio) window.pianoAudio.init();
        if (state.isPlaying) return;
        state.isPlaying = true;
        btnPlay.innerHTML = `
            <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 24 24"><path d="M6 4h4v16H6zm8 0h4v16h-4z"/></svg> Pausar
        `;
        btnPlay.classList.replace('bg-emerald-600', 'bg-amber-600');
        btnPlay.classList.replace('hover:bg-emerald-500', 'hover:bg-amber-500');

        restartPlaybackInterval();
    }

    function stopPlayback() {
        state.isPlaying = false;
        clearInterval(state.playbackInterval);
        state.currentMeasure = 0;
        window.scoreRenderer.hideCursor();

        btnPlay.innerHTML = `
            <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg> Escuchar
        `;
        btnPlay.classList.replace('bg-amber-600', 'bg-emerald-600');
        btnPlay.classList.replace('hover:bg-amber-500', 'hover:bg-emerald-500');
    }

    function restartPlaybackInterval() {
        clearInterval(state.playbackInterval);
        const beatsPerMeasure = state.currentSong.timeSignature[0];
        const beatDurationMs = (60 / state.bpm) * 1000;
        const totalMeasures = state.currentSong.measures.length;
        let currentStep = 0;
        const stepsPerMeasure = 16; // 16 pasos por compás (resolución de semicorchea)

        state.playbackInterval = setInterval(() => {
            const measureIdx = Math.floor(currentStep / stepsPerMeasure) % totalMeasures;
            const fraction = (currentStep % stepsPerMeasure) / stepsPerMeasure;

            // Metrónomo en cada tiempo (4 por compás)
            if (currentStep % (stepsPerMeasure / beatsPerMeasure) === 0) {
                const beatNum = Math.floor((currentStep % stepsPerMeasure) / (stepsPerMeasure / beatsPerMeasure));
                const measureData = state.currentSong.measures[measureIdx];

                if (beatNum === 0) {
                    window.pianoAudio.playClick(true);
                    // Tocar acorde del cifrado sajón
                    if (measureData.leftHand && measureData.leftHand.chordBlock) {
                        const pitches = measureData.leftHand.chordBlock.beats[0].pitches;
                        pitches.forEach(p => window.pianoAudio.playNote(p, 2.2, 0.4));
                    }
                } else {
                    window.pianoAudio.playClick(false);
                }
            }

            // Reproducir notas de la melodía según su tiempo exacto
            const measureData = state.currentSong.measures[measureIdx];
            if (measureData && measureData.rightHand && measureData.rightHand.notes) {
                let noteAccum = 0;
                measureData.rightHand.notes.forEach(note => {
                    const noteStep = Math.round(noteAccum * (stepsPerMeasure / beatsPerMeasure));
                    const currentMeasureStep = currentStep % stepsPerMeasure;
                    if (currentMeasureStep === noteStep) {
                        window.pianoAudio.playNote(note.pitch, note.duration * (60 / state.bpm), 0.85);
                        highlightKey(note.pitch, true);
                        window.scoreRenderer.triggerNoteFeedback(note.pitch, true, note.name || '');
                        setTimeout(() => {
                            highlightKey(note.pitch, false);
                            window.scoreRenderer.triggerNoteFeedback(note.pitch, false);
                        }, 250);
                    }
                    noteAccum += note.duration;
                });
            }

            window.scoreRenderer.updateCursor(measureIdx, fraction);
            currentStep++;
        }, beatDurationMs / (stepsPerMeasure / beatsPerMeasure));
    }

    if (btnPlay) {
        btnPlay.addEventListener('click', () => {
            if (state.isPlaying) stopPlayback();
            else startPlayback();
        });
    }

    if (btnStop) {
        btnStop.addEventListener('click', stopPlayback);
    }

    // 4. Teclado en pantalla
    buildRealisticKeyboard();

    function pitchToNoteName(pitch) {
        const noteNames = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"];
        return noteNames[pitch % 12];
    }

    function buildRealisticKeyboard() {
        const kbContainer = document.getElementById('piano-keys');
        if (!kbContainer) return;
        kbContainer.innerHTML = '';

        const whiteNotes = [
            { note: 48, label: 'Do3', hasSharp: true, sharpNote: 49 },
            { note: 50, label: 'Re3', hasSharp: true, sharpNote: 51 },
            { note: 52, label: 'Mi3', hasSharp: false },
            { note: 53, label: 'Fa3', hasSharp: true, sharpNote: 54 },
            { note: 55, label: 'Sol3', hasSharp: true, sharpNote: 56 },
            { note: 57, label: 'La3', hasSharp: true, sharpNote: 58 },
            { note: 59, label: 'Si3', hasSharp: false },
            { note: 60, label: 'Do4', hasSharp: true, sharpNote: 61 },
            { note: 62, label: 'Re4', hasSharp: true, sharpNote: 63 },
            { note: 64, label: 'Mi4', hasSharp: false },
            { note: 65, label: 'Fa4', hasSharp: true, sharpNote: 66 },
            { note: 67, label: 'Sol4', hasSharp: true, sharpNote: 68 },
            { note: 69, label: 'La4', hasSharp: true, sharpNote: 70 },
            { note: 71, label: 'Si4', hasSharp: false },
            { note: 72, label: 'Do5', hasSharp: true, sharpNote: 73 },
            { note: 74, label: 'Re5', hasSharp: true, sharpNote: 75 },
            { note: 76, label: 'Mi5', hasSharp: false },
            { note: 77, label: 'Fa5', hasSharp: true, sharpNote: 78 },
            { note: 79, label: 'Sol5', hasSharp: true, sharpNote: 80 },
            { note: 81, label: 'La5', hasSharp: true, sharpNote: 82 },
            { note: 83, label: 'Si5', hasSharp: false },
            { note: 84, label: 'Do6', hasSharp: false }
        ];

        const whiteKeyWidth = 44;
        const paddingLeft = 16;

        whiteNotes.forEach((wn) => {
            const whiteKey = document.createElement('div');
            whiteKey.className = 'key-white';
            whiteKey.dataset.pitch = wn.note;
            whiteKey.innerHTML = `<span>${wn.label}</span>`;
            whiteKey.addEventListener('mousedown', () => {
                window.pianoAudio.playNote(wn.note, 1.0);
                highlightKey(wn.note, true);
                window.scoreRenderer.triggerNoteFeedback(wn.note, true, wn.label);
            });
            whiteKey.addEventListener('mouseup', () => {
                highlightKey(wn.note, false);
                window.scoreRenderer.triggerNoteFeedback(wn.note, false);
            });
            whiteKey.addEventListener('mouseleave', () => {
                highlightKey(wn.note, false);
                window.scoreRenderer.triggerNoteFeedback(wn.note, false);
            });
            kbContainer.appendChild(whiteKey);
        });

        whiteNotes.forEach((wn, idx) => {
            if (wn.hasSharp) {
                const blackKey = document.createElement('div');
                blackKey.className = 'key-black';
                blackKey.dataset.pitch = wn.sharpNote;

                const crackPosition = paddingLeft + ((idx + 1) * whiteKeyWidth);
                const blackKeyLeft = crackPosition - 13;

                blackKey.style.left = `${blackKeyLeft}px`;

                blackKey.addEventListener('mousedown', (e) => {
                    e.stopPropagation();
                    window.pianoAudio.playNote(wn.sharpNote, 1.0);
                    highlightKey(wn.sharpNote, true);
                    window.scoreRenderer.triggerNoteFeedback(wn.sharpNote, true, pitchToNoteName(wn.sharpNote));
                });
                blackKey.addEventListener('mouseup', () => {
                    highlightKey(wn.sharpNote, false);
                    window.scoreRenderer.triggerNoteFeedback(wn.sharpNote, false);
                });
                blackKey.addEventListener('mouseleave', () => {
                    highlightKey(wn.sharpNote, false);
                    window.scoreRenderer.triggerNoteFeedback(wn.sharpNote, false);
                });
                kbContainer.appendChild(blackKey);
            }
        });
    }

    function highlightKey(pitch, active) {
        const keyEl = document.querySelector(`[data-pitch="${pitch}"]`);
        if (keyEl) {
            if (active) keyEl.classList.add('active');
            else keyEl.classList.remove('active');
        }
    }

    // 5. Conexión Web MIDI
    function updateMidiBadge(statusText, isConnected, isClickable = false) {
        if (!midiStatus) return;
        midiStatus.innerText = statusText;
        if (isConnected) {
            midiStatus.className = "text-xs font-semibold px-3 py-1.5 rounded-lg bg-emerald-950 text-emerald-300 border border-emerald-700 shadow-sm flex items-center gap-1.5 cursor-default";
            midiStatus.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-400"></span> ${statusText}`;
        } else {
            midiStatus.className = "text-xs font-medium px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 border border-slate-700 hover:border-slate-500 transition cursor-pointer flex items-center gap-1.5 shadow-sm";
            midiStatus.innerHTML = `<span class="w-2 h-2 rounded-full bg-amber-400"></span> ${statusText}`;
        }
    }

    if (midiStatus) {
        midiStatus.addEventListener('click', async () => {
            await window.midiManager.requestAccess();
        });
    }

    window.midiManager.init(
        (statusText, isConnected, isClickable) => {
            updateMidiBadge(statusText, isConnected, isClickable);
        },
        (note, velocity) => {
            window.pianoAudio.playNote(note, 1.2, Math.max(0.6, velocity));
            highlightKey(note, true);
            window.scoreRenderer.triggerNoteFeedback(note, true, pitchToNoteName(note));
        },
        (note) => {
            highlightKey(note, false);
            window.scoreRenderer.triggerNoteFeedback(note, false);
        }
    );
});
