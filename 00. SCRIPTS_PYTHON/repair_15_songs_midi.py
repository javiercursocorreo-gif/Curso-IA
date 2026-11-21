#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
repair_15_songs_midi.py
"""

import os
import re

DIR_MUSICA = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CURSO_MUSICA"

RED_SONGS = [
    "CANCION_36_O_SOLE_MIO.html",
    "CANCION_37_PARLAMI_DAMORE_MARIU.html",
    "CANCION_05_CON_TE_PARTIRO.html",
    "CANCION_04_CUANDO_CALIENTA_EL_SOL.html",
    "CANCION_09_AMOR_AMOR_AMOR.html",
    "CANCION_19_PERFIDIA.html",
    "CANCION_21_AMAPOLA.html",
    "CANCION_25_CANT_HELP_FALLING_IN_LOVE.html",
    "CANCION_26_UNCHAINED_MELODY.html",
    "CANCION_01_TO_ALL_THE_GIRLS.html",
    "CANCION_02_HALLELUJAH.html",
    "CANCION_34_WHAT_A_WONDERFUL_WORLD.html",
    "CANCION_16_MY_HEART_WILL_GO_ON.html",
    "CANCION_29_BORN_FREE.html",
    "CANCION_38_YOULL_BE_IN_MY_HEART.html"
]

CANONICAL_KBD_SETS = {
    '001': {'lsb': 0, 'pc': 0, 'name': '001 Grand Piano'},
    '005': {'lsb': 0, 'pc': 4, 'name': '005 E.GrandPiano'},
    '006': {'lsb': 0, 'pc': 5, 'name': '006 Piano&Pad'},
    '009': {'lsb': 0, 'pc': 8, 'name': '009 Funky Clavi'},
    '011': {'lsb': 1, 'pc': 0, 'name': '011 Stage E.P.'},
    '015': {'lsb': 1, 'pc': 6, 'name': '015 Span.Guitar'},
    '018': {'lsb': 1, 'pc': 9, 'name': '018 Clean Guitar'},
    '029': {'lsb': 2, 'pc': 8, 'name': '029 Harmonica'},
    '034': {'lsb': 3, 'pc': 3, 'name': '034 Hot BX3'},
    '037': {'lsb': 3, 'pc': 12, 'name': '037 Full Organ'},
    '038': {'lsb': 3, 'pc': 13, 'name': '038 Jazz Organ'},
    '048': {'lsb': 4, 'pc': 7, 'name': '048 Solo Violin'},
    '051': {'lsb': 5, 'pc': 0, 'name': '051 Aco.Guitar'},
    '053': {'lsb': 5, 'pc': 2, 'name': '053 Jazz Guitar'},
    '056': {'lsb': 5, 'pc': 5, 'name': '056 Dist.Guitar'},
    '061': {'lsb': 6, 'pc': 0, 'name': '061 The Strings'},
    '062': {'lsb': 6, 'pc': 1, 'name': '062 Bow Strings'},
    '066': {'lsb': 6, 'pc': 5, 'name': '066 Oct.Strings'},
    '071': {'lsb': 7, 'pc': 0, 'name': '071 Oooh&Aahs'},
    '086': {'lsb': 8, 'pc': 5, 'name': '086 Trp. & Trb.1'},
    '091': {'lsb': 9, 'pc': 0, 'name': '091 Grd.Accordion'},
    '095': {'lsb': 9, 'pc': 4, 'name': '095 Horns&Ens.'},
    '101': {'lsb': 10, 'pc': 0, 'name': '101 Tenor Sax'},
    '107': {'lsb': 10, 'pc': 6, 'name': '107 Flute'},
    '109': {'lsb': 10, 'pc': 8, 'name': '109 ClarinetEns'},
    '113': {'lsb': 11, 'pc': 2, 'name': '113 ThreeFlutes'},
    '114': {'lsb': 11, 'pc': 5, 'name': '114 Whistels'},
    '118': {'lsb': 11, 'pc': 9, 'name': '118 Wind Sect.'}
}

CANONICAL_ESTILOS = {
    '12': {'msb': 32, 'lsb': 0, 'pc': 11, 'name': '012 Standard Pop'},
    '012': {'msb': 32, 'lsb': 0, 'pc': 11, 'name': '012 Standard Pop'},
    '41': {'msb': 32, 'lsb': 2, 'pc': 8, 'name': '041 Love Ballad'},
    '041': {'msb': 32, 'lsb': 2, 'pc': 8, 'name': '041 Love Ballad'},
    '42': {'msb': 32, 'lsb': 2, 'pc': 9, 'name': '042 Slow Ballad'},
    '042': {'msb': 32, 'lsb': 2, 'pc': 9, 'name': '042 Slow Ballad'},
    '43': {'msb': 32, 'lsb': 2, 'pc': 10, 'name': '043 Modern Ballad'},
    '043': {'msb': 32, 'lsb': 2, 'pc': 10, 'name': '043 Modern Ballad'},
    '51': {'msb': 32, 'lsb': 3, 'pc': 2, 'name': '051 6/8 Slow Pop'},
    '051': {'msb': 32, 'lsb': 3, 'pc': 2, 'name': '051 6/8 Slow Pop'},
    '52': {'msb': 32, 'lsb': 3, 'pc': 3, 'name': '052 6/8 Ballad'},
    '052': {'msb': 32, 'lsb': 3, 'pc': 3, 'name': '052 6/8 Ballad'},
    '54': {'msb': 32, 'lsb': 3, 'pc': 5, 'name': '054 Slow Waltz1'},
    '054': {'msb': 32, 'lsb': 3, 'pc': 5, 'name': '054 Slow Waltz1'},
    '93': {'msb': 32, 'lsb': 5, 'pc': 12, 'name': '093 Pop Shuffle'},
    '093': {'msb': 32, 'lsb': 5, 'pc': 12, 'name': '093 Pop Shuffle'},
    '106': {'msb': 32, 'lsb': 6, 'pc': 9, 'name': '106 MotownShufl'},
    '111': {'msb': 32, 'lsb': 6, 'pc': 14, 'name': '111 Motown'},
    '118': {'msb': 32, 'lsb': 7, 'pc': 5, 'name': '118 60s Pop'},
    '154': {'msb': 32, 'lsb': 9, 'pc': 9, 'name': '154 Movie Ballad'},
    '171': {'msb': 32, 'lsb': 10, 'pc': 10, 'name': '171 Bolero Latino'},
    '172': {'msb': 32, 'lsb': 10, 'pc': 11, 'name': '172 Latin Rock'},
    '174': {'msb': 32, 'lsb': 10, 'pc': 13, 'name': '174 Beguine 1'},
    '175': {'msb': 32, 'lsb': 10, 'pc': 14, 'name': '175 Beguine 2'},
    '247': {'msb': 32, 'lsb': 15, 'pc': 6, 'name': '247 ViennaWaltz'}
}

def clean_script_code(code):
    # Eliminar cualquier bloque previo del motor inyectado
    code = re.sub(r'// =========================================================================\s*// MOTOR CANÓNICO WEB MIDI KORG EK-50[\s\S]*', '', code)

    # Eliminar bloques huérfanos o sintaxis rota
    code = re.sub(r'document\.addEventListener\(\s*[\'"]pointerdown[\'"][\s\S]*?\}\s*,\s*\{\s*passive:\s*true\s*\}\s*\);?', '', code)
    code = re.sub(r'if\s*\(btn\)\s*dispararDestelloBoton\(btn\);?\s*\}?\s*,\s*\{\s*passive:\s*true\s*\}\s*\);?', '', code)
    code = re.sub(r'\}\s*,\s*\{\s*passive:\s*true\s*\}\s*\);?', '', code)

    # Eliminar definiciones previas
    code = re.sub(r'async\s+function\s+activarEstilo[\s\S]*?\n    \}', '', code)
    code = re.sub(r'function\s+activarEstilo[\s\S]*?\n    \}', '', code)
    code = re.sub(r'async\s+function\s+cargarKeyboardSet[\s\S]*?\n    \}', '', code)
    code = re.sub(r'function\s+cargarKeyboardSet[\s\S]*?\n    \}', '', code)
    code = re.sub(r'async\s+function\s+desbloquearKorgEK50[\s\S]*?\n    \}', '', code)
    code = re.sub(r'function\s+desbloquearKorgEK50[\s\S]*?\n    \}', '', code)
    code = re.sub(r'function\s+dispararDestelloBoton[\s\S]*?\n    \}', '', code)
    code = re.sub(r'function\s+cerrarPartituraPantallaCompleta[\s\S]*?\n    \}', '', code)
    code = re.sub(r'const\s+CANONICAL_KBD_MAP[\s\S]*?;\n', '', code)
    code = re.sub(r'const\s+CANONICAL_STYLE_MAP[\s\S]*?;\n', '', code)

    destello_clean = '''function dispararDestelloBoton(el) {
        if (!el) return;
        el.style.transform = 'scale(0.95)';
        setTimeout(() => { el.style.transform = 'scale(1)'; }, 150);
    }'''

    midi_engine_block = '''
    // =========================================================================
    // MOTOR CANÓNICO WEB MIDI KORG EK-50 (BLINDADO CON RETARDOS DE 40ms)
    // =========================================================================
    ''' + destello_clean + '''

    var CANONICAL_KBD_MAP = ''' + str(CANONICAL_KBD_SETS).replace("'", '"') + ''';
    var CANONICAL_STYLE_MAP = ''' + str(CANONICAL_ESTILOS).replace("'", '"') + ''';

    async function enviarMidiGlobal(bytes) {
        if (!midiOutput && (!midiAccessInstance || obtenerSalidasDisponibles().length === 0)) {
            await conectarMIDI();
        }
        if (midiOutput) {
            try { midiOutput.send(bytes); return true; } catch(e) {}
        }
        const outputs = obtenerSalidasDisponibles();
        let enviado = false;
        outputs.forEach(port => {
            try { port.send(bytes); enviado = true; } catch(e) {}
        });
        return enviado;
    }

    async function activarEstilo(codigo, btn = null) {
        if (btn) dispararDestelloBoton(btn);
        habilitarNoSleep();
        actualizarEstilosActivosUI(codigo);

        if (!midiOutput && (!midiAccessInstance || obtenerSalidasDisponibles().length === 0)) {
            await conectarMIDI();
        }

        try {
            const num = parseInt(codigo, 10);
            let msb = 32;
            let lsb = !isNaN(num) && num > 0 ? Math.floor((num - 1) / 16) : 0;
            let pc = !isNaN(num) && num > 0 ? (num - 1) % 16 : 0;
            let stName = `Estilo ${codigo}`;

            const codStr = String(codigo);
            if (CANONICAL_STYLE_MAP[codStr]) {
                msb = CANONICAL_STYLE_MAP[codStr].msb;
                lsb = CANONICAL_STYLE_MAP[codStr].lsb;
                pc = CANONICAL_STYLE_MAP[codStr].pc;
                stName = CANONICAL_STYLE_MAP[codStr].name;
            }

            // 1. Detener acompañamiento previo limpiamente para no colgar el DSP
            await enviarMidiGlobal([0xFC]);
            await new Promise(r => setTimeout(r, 40));

            // 2. Transmisión limpia en Canal 16 (0xBF = CC, 0xCF = PC)
            await enviarMidiGlobal([0xBF, 0x00, msb]);
            await enviarMidiGlobal([0xBF, 0x20, lsb]);
            await enviarMidiGlobal([0xCF, pc]);
            await new Promise(r => setTimeout(r, 40));

            const log = document.getElementById('log-midi');
            if (log) log.innerHTML = `🥁 <b>${stName}</b> activado en Korg EK-50.`;
        } catch(e) {
            console.error('Error al activar estilo:', e);
        }
    }

    async function cargarKeyboardSet(codigo, btn = null) {
        if (btn) dispararDestelloBoton(btn);
        habilitarNoSleep();
        actualizarSonidoUI(codigo);

        if (!midiOutput && (!midiAccessInstance || obtenerSalidasDisponibles().length === 0)) {
            await conectarMIDI();
        }

        try {
            const numStr = String(codigo).padStart(3, '0');
            let bankLsb = 0;
            let pc = 0;
            let sndName = `Sonido ${codigo}`;

            if (CANONICAL_KBD_MAP[numStr]) {
                bankLsb = CANONICAL_KBD_MAP[numStr].lsb;
                pc = CANONICAL_KBD_MAP[numStr].pc;
                sndName = CANONICAL_KBD_MAP[numStr].name;
            } else if (codigo === 'sts_strings') {
                bankLsb = 6; pc = 0; sndName = '061 The Strings';
            } else {
                const num = parseInt(codigo, 10);
                if (!isNaN(num) && num > 0) {
                    bankLsb = Math.floor((num - 1) / 16);
                    pc = (num - 1) % 16;
                }
            }

            // 1. Upper 1 (Canal 1 - índice 0): Banco Maestro MSB 33
            await enviarMidiGlobal([0xB0, 0x00, 33]);
            await enviarMidiGlobal([0xB0, 0x20, bankLsb]);
            await enviarMidiGlobal([0xC0, pc]);
            await new Promise(r => setTimeout(r, 40));

            // 2. Global LCD (Canal 16 - índice 15): Banco Maestro MSB 33
            await enviarMidiGlobal([0xBF, 0x00, 33]);
            await enviarMidiGlobal([0xBF, 0x20, bankLsb]);
            await enviarMidiGlobal([0xCF, pc]);
            await new Promise(r => setTimeout(r, 40));

            // 3. Calibración acústica de directo
            [0, 1, 2, 3].forEach(ch => {
                enviarMidiGlobal([0xB0 | ch, 0x07, 122]);
                enviarMidiGlobal([0xB0 | ch, 0x0B, 127]);
                enviarMidiGlobal([0xB0 | ch, 0x5B, 42]);
            });

            const log = document.getElementById('log-midi');
            if (log) log.innerHTML = `🎹 Keyboard Set <b>${sndName}</b> activado en Korg EK-50.`;
        } catch(e) {
            console.error('Error al cargar sonido:', e);
        }
    }

    async function desbloquearKorgEK50(btn = null) {
        if (btn) dispararDestelloBoton(btn);
        if (!midiOutput && (!midiAccessInstance || obtenerSalidasDisponibles().length === 0)) {
            await conectarMIDI();
        }

        try {
            // Panic en todos los 16 canales
            for (let ch = 0; ch < 16; ch++) {
                enviarMidiGlobal([0xB0 | ch, 120, 0]); // All Sound Off
                enviarMidiGlobal([0xB0 | ch, 123, 0]); // All Notes Off
                enviarMidiGlobal([0xB0 | ch, 121, 0]); // Reset Controllers
                enviarMidiGlobal([0xB0 | ch, 7, 127]);  // Vol 127
                enviarMidiGlobal([0xB0 | ch, 11, 127]); // Expr 127
            }
            await new Promise(r => setTimeout(r, 50));
            const log = document.getElementById('log-midi');
            if (log) log.innerHTML = `⚡ <b>Korg EK-50 restablecido con éxito</b> (Panic enviado y controladores reiniciados).`;
        } catch(e) {
            console.error('Error al resetear Korg EK-50:', e);
        }
    }

    function cerrarPartituraPantallaCompleta(btn = null) {
        if (btn) dispararDestelloBoton(btn);
        const modal = document.getElementById('modal-partitura-fullscreen') || document.getElementById('modal-cifraclub');
        if (modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    }
'''
    return code + '\n' + midi_engine_block

def repair_song_html(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Limpieza de CSS que interfiere con eventos táctiles en iOS
    html = re.sub(r'@keyframes\s+destelloPulsacion\s*\{[\s\S]*?\}\s*\}', '', html)
    html = re.sub(r'\.btn-flash-active\s*\{[\s\S]*?\}', '', html)
    
    # 2. Limpieza de doble punto y coma ';;'
    html = html.replace(';;', ';')

    # 3. Asegurar que el botón de cerrar en el modal tenga onclick="cerrarPartituraPantallaCompleta(this)"
    html = re.sub(
        r'<button\s+id=["\']btn-close-score-modal["\']([^>]*)>',
        r'<button id="btn-close-score-modal" onclick="cerrarPartituraPantallaCompleta(this)"\1>',
        html
    )
    html = re.sub(
        r'<button\s+id=["\']hud-btn-cerrar["\']([^>]*)>',
        r'<button id="hud-btn-cerrar" onclick="cerrarPartituraPantallaCompleta(this)"\1>',
        html
    )

    # 4. Modificar el bloque principal de script
    last_script_match = list(re.finditer(r'<script[\s\S]*?</script>', html))
    if last_script_match:
        target = last_script_match[-1]
        raw_script = target.group(0)
        prefix = raw_script[:raw_script.find('>') + 1]
        suffix = '</script>'
        inner_code = raw_script[raw_script.find('>') + 1:-len(suffix)]
        
        cleaned = clean_script_code(inner_code)
        new_script = prefix + '\n' + cleaned + '\n' + suffix
        html = html[:target.start()] + new_script + html[target.end():]

    # 5. Smart Dimming Overlay a 45 min
    html = re.sub(r'setTimeout\(\(\)\s*=>\s*\{[\s\S]*?\},?\s*(?:180000|120000|60000)\)', 'setTimeout(() => { if (ov) { ov.style.display="flex"; void ov.offsetWidth; ov.style.opacity="1"; ov.style.pointerEvents="auto"; } }, 2700000)', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Reparado con éxito: {filename}")

def main():
    print("=================================================================")
    print("=== REPARACIÓN DE BOTONES FLOTANTES Y WEB MIDI EN 15 CANCIONES ===")
    print("=================================================================")
    for song in RED_SONGS:
        p = os.path.join(DIR_MUSICA, song)
        if os.path.exists(p):
            repair_song_html(p)
        else:
            print(f"⚠️ Canción no encontrada: {p}")

    p_rep = os.path.join(DIR_MUSICA, "REPERTORIO_KORG_EK50.html")
    p_idx = os.path.join(DIR_MUSICA, "index.html")
    if os.path.exists(p_rep):
        with open(p_rep, 'r', encoding='utf-8') as f:
            rep_content = f.read()
        with open(p_idx, 'w', encoding='utf-8') as f:
            f.write(rep_content)
        print("✅ index.html sincronizado al 100% con REPERTORIO_KORG_EK50.html")

if __name__ == '__main__':
    main()
