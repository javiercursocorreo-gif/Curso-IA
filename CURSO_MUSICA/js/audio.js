// audio.js - Motor de sonido de piano robusto para Web Audio API
class PianoAudioEngine {
    constructor() {
        this.ctx = null;
        this.masterGain = null;
        this.isMuted = false;
        this.initialized = false;
    }

    init() {
        if (this.initialized && this.ctx) {
            if (this.ctx.state === 'suspended') {
                this.ctx.resume();
            }
            return;
        }

        const AudioContext = window.AudioContext || window.webkitAudioContext;
        this.ctx = new AudioContext();
        this.masterGain = this.ctx.createGain();
        this.masterGain.gain.setValueAtTime(0.8, this.ctx.currentTime);
        this.masterGain.connect(this.ctx.destination);
        this.initialized = true;

        if (this.ctx.state === 'suspended') {
            this.ctx.resume();
        }
    }

    midiToFreq(midiNote) {
        return 440 * Math.pow(2, (midiNote - 69) / 12);
    }

    playNote(midiNote, duration = 1.0, velocity = 0.8) {
        // Asegurar que el contexto de audio esté vivo
        if (!this.initialized || !this.ctx) {
            this.init();
        }

        if (this.ctx.state === 'suspended') {
            this.ctx.resume();
        }

        const now = this.ctx.currentTime;
        const freq = this.midiToFreq(midiNote);

        // Ganancia principal de la nota con envolvente suave
        const noteGain = this.ctx.createGain();
        const baseVol = Math.max(0.2, Math.min(1.0, velocity)) * 0.5;

        noteGain.gain.setValueAtTime(0.0001, now);
        noteGain.gain.linearRampToValueAtTime(baseVol, now + 0.005);
        noteGain.gain.exponentialRampToValueAtTime(baseVol * 0.4, now + 0.12);
        noteGain.gain.exponentialRampToValueAtTime(0.0001, now + Math.max(duration, 0.4));

        // Armónicos fundamentales del piano acústico
        const harmonics = [
            { mult: 1, gain: 0.8, decay: 1.0 },
            { mult: 2, gain: 0.4, decay: 0.7 },
            { mult: 3, gain: 0.2, decay: 0.5 },
            { mult: 4, gain: 0.1, decay: 0.3 }
        ];

        harmonics.forEach(h => {
            const osc = this.ctx.createOscillator();
            const hGain = this.ctx.createGain();

            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq * h.mult, now);

            hGain.gain.setValueAtTime(h.gain, now);
            hGain.gain.exponentialRampToValueAtTime(0.0001, now + duration * h.decay);

            osc.connect(hGain);
            hGain.connect(noteGain);

            osc.start(now);
            osc.stop(now + duration + 0.1);
        });

        noteGain.connect(this.masterGain);
    }

    playClick(isAccented = false) {
        if (!this.initialized || !this.ctx) this.init();
        if (this.ctx.state === 'suspended') this.ctx.resume();

        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = 'sine';
        osc.frequency.setValueAtTime(isAccented ? 1200 : 800, now);

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + 0.05);
    }
}

window.pianoAudio = new PianoAudioEngine();

// Desbloquear AudioContext en el primer clic del usuario en la página
window.addEventListener('click', () => {
    if (window.pianoAudio) window.pianoAudio.init();
}, { once: false });
