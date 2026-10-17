// renderer.js - Motor SVG con soporte para partitura estándar (Grand Staff) y Lead Sheet (Melodía + Cifrado Sajón)
class ScoreRenderer {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.mode = 'pianovista'; // 'pianovista', 'skeleton', 'traditional'
        this.systemWidth = 1100;
        this.measuresPerSystem = 4;
        this.initPitchMap();
    }

    setMode(mode) {
        this.mode = mode;
        if (this.currentSong) this.render(this.currentSong);
    }

    initPitchMap() {
        const gClefBasePitch = 71; // Si4
        this.gClefBaseY = 90;
        const fClefBasePitch = 50; // Re3
        this.fClefBaseY = 230;

        this.pitchToY = (pitch, clef = 'treble') => {
            const diatonicOffsets = [0, 0, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6];
            const getDiatonicStep = (p) => {
                const oct = Math.floor(p / 12);
                const rem = p % 12;
                return oct * 7 + diatonicOffsets[rem];
            };

            if (clef === 'treble') {
                const baseStep = getDiatonicStep(gClefBasePitch);
                const step = getDiatonicStep(pitch);
                return this.gClefBaseY - (step - baseStep) * 9.5;
            } else {
                const baseStep = getDiatonicStep(fClefBasePitch);
                const step = getDiatonicStep(pitch);
                return this.fClefBaseY - (step - baseStep) * 9.5;
            }
        };
    }

    render(song) {
        this.currentSong = song;
        if (!this.container) return;

        const isLeadSheet = song.isLeadSheet === true;
        this.systemHeight = isLeadSheet ? 200 : 320;
        const measures = song.measures;
        const totalSystems = Math.ceil(measures.length / this.measuresPerSystem);
        const totalHeight = totalSystems * this.systemHeight + 40;

        let svgHtml = `
        <svg id="score-svg" viewBox="0 0 ${this.systemWidth} ${totalHeight}" class="w-full select-none" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <filter id="soft-glow" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="3" result="blur" />
                    <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
            </defs>
        `;

        for (let sysIdx = 0; sysIdx < totalSystems; sysIdx++) {
            const sysY = sysIdx * this.systemHeight + 20;
            const systemMeasures = measures.slice(sysIdx * this.measuresPerSystem, (sysIdx + 1) * this.measuresPerSystem);

            svgHtml += `<g id="system-${sysIdx}" transform="translate(0, ${sysY})">`;
            svgHtml += this.renderStaves(this.systemWidth, sysIdx === 0, isLeadSheet);

            const measureWidth = (this.systemWidth - 120) / systemMeasures.length;

            systemMeasures.forEach((m, mIdx) => {
                const startX = 110 + mIdx * measureWidth;
                svgHtml += this.renderMeasure(m, startX, measureWidth, isLeadSheet);
            });

            svgHtml += `</g>`;
        }

        svgHtml += `<g id="live-played-layer"></g>`;

        svgHtml += `
            <line id="playback-cursor" x1="110" y1="20" x2="110" y2="300" 
                  stroke="#ef4444" stroke-width="3" stroke-linecap="round" 
                  class="transition-all duration-100 opacity-0 pointer-events-none" />
        `;

        svgHtml += `</svg>`;
        this.container.innerHTML = svgHtml;
    }

    renderStaves(width, isFirstSystem, isLeadSheet) {
        const hideLines = this.mode === 'skeleton';
        const lineOpacity = hideLines ? '0.0' : '1.0';
        const staffColor = '#1e293b';

        let html = `<g class="staves" style="opacity: ${lineOpacity}; transition: opacity 0.3s ease;">`;

        if (!isLeadSheet) {
            html += `
                <path d="M 50 48 Q 35 155 50 165 Q 35 175 50 282" fill="none" stroke="${staffColor}" stroke-width="3" stroke-linecap="round"/>
                <line x1="60" y1="52" x2="60" y2="268" stroke="${staffColor}" stroke-width="2"/>
            `;
        } else {
            html += `<line x1="60" y1="52" x2="60" y2="128" stroke="${staffColor}" stroke-width="2.5"/>`;
        }

        // 5 líneas Clave de Sol
        for (let i = 0; i < 5; i++) {
            const y = 52 + i * 19;
            html += `<line x1="60" y1="${y}" x2="${width - 20}" y2="${y}" stroke="${staffColor}" stroke-width="1.2"/>`;
        }

        // Si no es Lead Sheet, dibujar pentagrama Clave de Fa
        if (!isLeadSheet) {
            for (let i = 0; i < 5; i++) {
                const y = 192 + i * 19;
                html += `<line x1="60" y1="${y}" x2="${width - 20}" y2="${y}" stroke="${staffColor}" stroke-width="1.2"/>`;
            }
        }

        html += `</g>`;

        // Símbolo de Clave de Sol
        html += `
            <g class="clefs">
                <text x="68" y="115" font-family="serif" font-size="56" font-weight="bold" fill="#1e293b">𝄞</text>
            </g>
        `;

        if (!isLeadSheet) {
            html += `<text x="68" y="240" font-family="serif" font-size="46" font-weight="bold" fill="#1e293b">𝄢</text>`;
        }

        // Compás
        if (this.mode !== 'skeleton' && isFirstSystem) {
            const timeSig = (this.currentSong && this.currentSong.timeSignature) ? this.currentSong.timeSignature : [4, 4];
            html += `
                <g class="time-signature font-bold text-slate-800" font-family="sans-serif">
                    <text x="96" y="82" font-size="24" font-weight="900" fill="#0f172a">${timeSig[0]}</text>
                    <text x="96" y="120" font-size="24" font-weight="900" fill="#0f172a">${timeSig[1]}</text>
                </g>
            `;
        }

        return html;
    }

    renderMeasure(m, startX, width, isLeadSheet) {
        let html = `<g id="measure-${m.number}" class="measure-group">`;
        const barX = startX + width;
        const barBottom = isLeadSheet ? 128 : 280;

        html += `<line x1="${barX}" y1="45" x2="${barX}" y2="${barBottom}" stroke="#64748b" stroke-width="1.5" />`;
        html += `<text x="${startX + 6}" y="40" font-size="11" font-weight="bold" fill="#64748b">${m.number}</text>`;

        // CIFRADO SAJÓN (Americano) Grande y Elegante sobre el compás
        if (m.chord) {
            html += `
                <g class="lead-sheet-chord cursor-pointer" onclick="pianoAudio.playNote(48); pianoAudio.playNote(52); pianoAudio.playNote(55);">
                    <rect x="${startX + 14}" y="12" width="48" height="26" rx="6" fill="#1e293b" />
                    <text x="${startX + 38}" y="30" text-anchor="middle" font-size="16" font-weight="900" fill="#38bdf8" font-family="sans-serif">${m.chord}</text>
                </g>
            `;
        }

        // Melodía (Mano derecha)
        html += this.renderRightHand(m.rightHand, startX, width);

        // Acompañamiento si existe
        if (!isLeadSheet && m.leftHand) {
            html += this.renderLeftHand(m.leftHand, startX, width);
        }

        html += `</g>`;
        return html;
    }

    renderLeftHand(lh, startX, width) {
        if (!lh) return '';
        let html = `<g class="left-hand-group">`;

        const bassX = startX + width * 0.16;
        const bassY = this.pitchToY(lh.bass.pitch, 'bass');

        const chord1X = startX + width * 0.50;
        const chord2X = startX + width * 0.78;

        const chordYs = lh.chordBlock.beats[0].pitches.map(p => this.pitchToY(p, 'bass'));
        const minY = Math.min(...chordYs);
        const maxY = Math.max(...chordYs);
        const chordTop = minY - 8;
        const chordHeight = (maxY - minY) + 16;

        if (this.mode === 'pianovista' || this.mode === 'skeleton') {
            const midX = (bassX + chord1X) / 2;
            const controlY = Math.max(bassY, chordTop + chordHeight) + 16;
            html += `
                <path d="M ${bassX + 10} ${bassY} Q ${midX} ${controlY} ${chord1X - 10} ${maxY}" 
                      fill="none" stroke="#3b82f6" stroke-width="2.2" stroke-dasharray="4,4" opacity="0.9"/>
            `;

            const boneW = (chord2X - chord1X) + 26;
            const boneLeft = chord1X - 13;
            
            html += `
                <g class="chord-dumbbell-block cursor-pointer transition-all duration-150"
                   data-pitches="${lh.chordBlock.beats[0].pitches.join(',')}"
                   onclick="pianoAudio.playNote(${lh.chordBlock.beats[0].pitches[0]}); pianoAudio.playNote(${lh.chordBlock.beats[0].pitches[1]}); pianoAudio.playNote(${lh.chordBlock.beats[0].pitches[2]});">
                    <rect x="${boneLeft}" y="${chordTop}" width="${boneW}" height="${chordHeight}" rx="12" 
                          fill="${lh.chordBlock.color}" stroke="${lh.chordBlock.borderColor}" stroke-width="2"/>
                    <rect x="${chord1X + 10}" y="${chordTop + 4}" width="${chord2X - chord1X - 20}" height="${chordHeight - 8}" 
                          fill="${lh.chordBlock.color}" rx="5"/>
                </g>
            `;
        }

        // Bajo
        if (this.mode === 'pianovista' || this.mode === 'skeleton') {
            html += `
                <g class="anchor-node cursor-pointer score-target" data-pitch="${lh.bass.pitch}" onclick="pianoAudio.playNote(${lh.bass.pitch})">
                    <circle cx="${bassX}" cy="${bassY}" r="13" fill="#0f172a" stroke="#ec4899" stroke-width="3.5" class="target-node"/>
                    <text x="${bassX}" y="${bassY + 4}" text-anchor="middle" font-size="10" font-weight="900" fill="#ffffff">${lh.bass.name}</text>
                    <text x="${bassX}" y="${bassY + 26}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">${lh.bass.finger || '5'}</text>
                </g>
            `;
        } else {
            html += `
                <g class="score-target" data-pitch="${lh.bass.pitch}">
                    <circle cx="${bassX}" cy="${bassY}" r="6" fill="#0f172a" class="target-node" />
                    <line x1="${bassX + 6}" y1="${bassY}" x2="${bassX + 6}" y2="${bassY - 30}" stroke="#0f172a" stroke-width="1.8"/>
                </g>
            `;
        }

        if (bassY > 268) {
            html += `<line x1="${bassX - 12}" y1="287" x2="${bassX + 12}" y2="287" stroke="#0f172a" stroke-width="1.5"/>`;
        }

        // Acordes
        [chord1X, chord2X].forEach((cx, beatIdx) => {
            if (!lh.chordBlock.beats[beatIdx]) return;
            lh.chordBlock.beats[beatIdx].pitches.forEach((pitch) => {
                const cy = this.pitchToY(pitch, 'bass');

                if (this.mode === 'skeleton') {
                    html += `
                        <g class="score-target" data-pitch="${pitch}">
                            <circle cx="${cx}" cy="${cy}" r="5.5" fill="#ffffff" stroke="#e11d48" stroke-width="2.5" class="target-node" />
                        </g>
                    `;
                } else if (this.mode === 'pianovista') {
                    html += `
                        <g class="score-target" data-pitch="${pitch}">
                            <circle cx="${cx}" cy="${cy}" r="6" fill="#ffffff" stroke="#ea580c" stroke-width="2.2" class="target-node" />
                        </g>
                    `;
                } else {
                    html += `
                        <g class="score-target" data-pitch="${pitch}">
                            <circle cx="${cx}" cy="${cy}" r="6" fill="#0f172a" class="target-node" />
                        </g>
                    `;
                }
            });

            html += `<line x1="${cx + 6}" y1="${minY}" x2="${cx + 6}" y2="${minY - 24}" stroke="#0f172a" stroke-width="1.6"/>`;
        });

        html += `</g>`;
        return html;
    }

    renderRightHand(rh, startX, width) {
        if (!rh || !rh.notes || rh.notes.length === 0) return '';
        let html = `<g class="right-hand-group">`;

        const notePoints = [];
        const stepX = width / (rh.notes.length + 0.6);

        rh.notes.forEach((n, i) => {
            const nx = startX + 26 + i * stepX;
            const ny = this.pitchToY(n.pitch, 'treble');
            notePoints.push({ x: nx, y: ny, note: n });
        });

        if ((this.mode === 'pianovista' || this.mode === 'skeleton') && notePoints.length > 1) {
            const padding = 15;
            let topPath = `M ${notePoints[0].x - padding} ${notePoints[0].y}`;
            let bottomPath = '';

            for (let i = 0; i < notePoints.length; i++) {
                const pt = notePoints[i];
                topPath += ` L ${pt.x} ${pt.y - padding}`;
            }
            topPath += ` L ${notePoints[notePoints.length - 1].x + padding} ${notePoints[notePoints.length - 1].y}`;

            for (let i = notePoints.length - 1; i >= 0; i--) {
                const pt = notePoints[i];
                bottomPath += ` L ${pt.x} ${pt.y + padding}`;
            }

            const capsulePath = `${topPath} ${bottomPath} Z`;

            html += `
                <path d="${capsulePath}" fill="${rh.vector.color}" stroke="${rh.vector.borderColor}" 
                      stroke-width="2" rx="12" filter="url(#soft-glow)" opacity="0.9" />
            `;
        }

        notePoints.forEach((pt) => {
            const n = pt.note;

            if (pt.y <= 38) {
                html += `<line x1="${pt.x - 12}" y1="38" x2="${pt.x + 12}" y2="38" stroke="#0f172a" stroke-width="1.5"/>`;
            }
            if (pt.y >= 128) {
                html += `<line x1="${pt.x - 12}" y1="128" x2="${pt.x + 12}" y2="128" stroke="#0f172a" stroke-width="1.5"/>`;
            }

            if (n.isAnchor && (this.mode === 'pianovista' || this.mode === 'skeleton')) {
                html += `
                    <g class="anchor-melody cursor-pointer score-target" data-pitch="${n.pitch}" onclick="pianoAudio.playNote(${n.pitch})">
                        <circle cx="${pt.x}" cy="${pt.y}" r="12" fill="#0f172a" stroke="#ec4899" stroke-width="3" class="target-node"/>
                        <text x="${pt.x}" y="${pt.y + 4}" text-anchor="middle" font-size="8.5" font-weight="900" fill="#ffffff">${n.name}</text>
                        <text x="${pt.x}" y="${pt.y - 16}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">${n.finger || '1'}</text>
                    </g>
                `;
            } else if (this.mode === 'skeleton') {
                html += `
                    <g class="score-target" data-pitch="${n.pitch}">
                        <circle cx="${pt.x}" cy="${pt.y}" r="5" fill="#ffffff" stroke="#2563eb" stroke-width="2.5" 
                                class="cursor-pointer target-node" onclick="pianoAudio.playNote(${n.pitch})" />
                    </g>
                `;
                if (n.finger) {
                    html += `<text x="${pt.x}" y="${pt.y - 13}" text-anchor="middle" font-size="10" font-weight="bold" fill="#0f172a">${n.finger}</text>`;
                }
            } else {
                const isHollow = n.duration >= 2.0;
                const stemUp = pt.y > 90;
                const stemX = stemUp ? pt.x + 6 : pt.x - 6;
                const stemY2 = stemUp ? pt.y - 28 : pt.y + 28;

                html += `
                    <g class="score-target" data-pitch="${n.pitch}">
                        <ellipse cx="${pt.x}" cy="${pt.y}" rx="6" ry="4.8" fill="${isHollow ? '#ffffff' : '#0f172a'}" 
                                 stroke="#0f172a" stroke-width="${isHollow ? '2' : '0'}" 
                                 transform="rotate(-20, ${pt.x}, ${pt.y})" class="cursor-pointer target-node" onclick="pianoAudio.playNote(${n.pitch})"/>
                        <line x1="${stemX}" y1="${pt.y}" x2="${stemX}" y2="${stemY2}" stroke="#0f172a" stroke-width="1.6"/>
                    </g>
                `;

                if (n.finger) {
                    html += `<text x="${pt.x}" y="${stemUp ? stemY2 - 5 : pt.y - 11}" text-anchor="middle" font-size="10" font-weight="bold" fill="#0f172a">${n.finger}</text>`;
                }
            }
        });

        html += `</g>`;
        return html;
    }

    triggerNoteFeedback(pitch, isDown = true, noteName = '') {
        const liveLayer = document.getElementById('live-played-layer');
        
        const targets = document.querySelectorAll(`.score-target[data-pitch="${pitch}"] .target-node`);
        targets.forEach(el => {
            if (isDown) {
                el.style.transition = 'all 0.1s ease';
                el.style.fill = '#10b981';
                el.style.stroke = '#047857';
                el.style.strokeWidth = '5px';
            } else {
                el.style.fill = '';
                el.style.stroke = '';
                el.style.strokeWidth = '';
            }
        });

        if (liveLayer && isDown) {
            const clef = pitch >= 60 ? 'treble' : 'bass';
            const yPos = this.pitchToY(pitch, clef) + 20;
            
            const ghostNote = document.createElementNS('http://www.w3.org/2000/svg', 'g');
            ghostNote.setAttribute('id', `live-pitch-${pitch}`);
            ghostNote.innerHTML = `
                <circle cx="80" cy="${yPos}" r="12" fill="#10b981" stroke="#ffffff" stroke-width="3" opacity="0.95" />
                <text x="80" y="${yPos + 4}" text-anchor="middle" font-size="9" font-weight="bold" fill="#ffffff">${noteName || ''}</text>
                <circle cx="80" cy="${yPos}" r="22" fill="none" stroke="#10b981" stroke-width="2" class="animate-ping" opacity="0.75"/>
            `;
            liveLayer.appendChild(ghostNote);
        } else if (liveLayer && !isDown) {
            const existing = document.getElementById(`live-pitch-${pitch}`);
            if (existing) {
                existing.style.opacity = '0';
                setTimeout(() => { if (existing.parentNode) existing.parentNode.removeChild(existing); }, 200);
            }
        }
    }

    updateCursor(measureIdx, beatFraction) {
        const cursor = document.getElementById('playback-cursor');
        if (!cursor || !this.currentSong) return;

        const systemIdx = Math.floor(measureIdx / this.measuresPerSystem);
        const measureInSystem = measureIdx % this.measuresPerSystem;
        const measureWidth = (this.systemWidth - 120) / this.measuresPerSystem;
        const currentX = 110 + measureInSystem * measureWidth + beatFraction * measureWidth;

        const sysY = systemIdx * this.systemHeight + 20;

        cursor.setAttribute('x1', currentX);
        cursor.setAttribute('x2', currentX);
        cursor.setAttribute('y1', sysY + 20);
        cursor.setAttribute('y2', sysY + (this.currentSong.isLeadSheet ? 140 : 280));
        cursor.style.opacity = '1';
    }

    hideCursor() {
        const cursor = document.getElementById('playback-cursor');
        if (cursor) cursor.style.opacity = '0';
    }
}

window.scoreRenderer = new ScoreRenderer('score-container');
