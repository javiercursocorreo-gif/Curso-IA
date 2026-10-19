// midi.js - Soporte Web MIDI API con botón de reconexión manual y diagnóstico
class MidiManager {
    constructor() {
        this.midiAccess = null;
        this.activeInputs = [];
        this.onNoteOn = null;
        this.onNoteOff = null;
        this.statusCallback = null;
        this.supported = false;
    }

    async init(statusCallback, onNoteOn, onNoteOff) {
        this.statusCallback = statusCallback;
        this.onNoteOn = onNoteOn;
        this.onNoteOff = onNoteOff;

        await this.requestAccess();
    }

    async requestAccess() {
        if (!navigator.requestMIDIAccess) {
            if (this.statusCallback) {
                this.statusCallback("Tu navegador no soporta Web MIDI. Usa Chrome o Edge.", false);
            }
            return false;
        }

        try {
            if (this.statusCallback) this.statusCallback("Buscando teclados MIDI...", false);
            
            this.midiAccess = await navigator.requestMIDIAccess({ sysex: false });
            this.supported = true;
            this.setupInputs();

            // Detectar conexión/desconexión física en caliente (hotplug)
            this.midiAccess.onstatechange = (e) => {
                console.log("Cambio de estado MIDI:", e.port.name, e.port.state);
                this.setupInputs();
            };

            return true;
        } catch (err) {
            console.error("Error solicitando acceso MIDI:", err);
            if (this.statusCallback) {
                this.statusCallback("Haz clic aquí para conceder permiso MIDI", false, true);
            }
            return false;
        }
    }

    setupInputs() {
        if (!this.midiAccess) return;
        this.activeInputs = [];
        const inputs = this.midiAccess.inputs.values();

        for (let input of inputs) {
            if (input.state === "connected") {
                this.activeInputs.push(input.name);
                input.onmidimessage = (msg) => this.handleMidiMessage(msg);
            }
        }
        this.updateStatus();
    }

    updateStatus() {
        if (!this.statusCallback) return;
        if (this.activeInputs.length > 0) {
            this.statusCallback(`Conectado: ${this.activeInputs.join(', ')}`, true);
        } else {
            this.statusCallback("MIDI: Sin teclado detectado. Pulsa para reescanear.", false, true);
        }
    }

    handleMidiMessage(event) {
        const [status, note, velocity] = event.data;
        const command = status >> 4;

        if (command === 9 && velocity > 0) {
            // Note On
            if (this.onNoteOn) this.onNoteOn(note, velocity / 127);
        } else if (command === 8 || (command === 9 && velocity === 0)) {
            // Note Off
            if (this.onNoteOff) this.onNoteOff(note);
        }
    }
}

window.midiManager = new MidiManager();
