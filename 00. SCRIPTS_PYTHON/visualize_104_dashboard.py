#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
visualize_104_dashboard.py
Inspecciona la carpeta '104 ESTILO ANIMADOS SIN PROGRAMAR', extrae los 100 Prompts
del PDF con múltiples motores (pypdf, pdfplumber, PyPDF2, Quartz/PDFKit o parser de streams),
clasifica las utilidades y genera un Visor Interactivo en HTML accesible para Safari:
VISOR_100_PROMPTS_ANIMADOS.html
"""

import os
import sys
import re
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

# Búsqueda flexible de la carpeta para evitar discrepancias de tildes NFD/NFC
CANDIDATE_DIRS = [
    os.path.join(BASE_DIR, "104 ESTILO ANIMADOS SIN PROGRAMAR"),
    os.path.join(BASE_DIR, "104_ESTILO_ANIMADOS_SIN_PROGRAMAR"),
]

TARGET_DIR = None
for d in CANDIDATE_DIRS:
    if os.path.exists(d):
        TARGET_DIR = d
        break

if not TARGET_DIR:
    for entry in os.listdir(BASE_DIR):
        if "104" in entry and "ANIMAD" in entry.upper():
            TARGET_DIR = os.path.join(BASE_DIR, entry)
            break

if not TARGET_DIR:
    TARGET_DIR = os.path.join(BASE_DIR, "104 ESTILO ANIMADOS SIN PROGRAMAR")

DASHBOARD_HTML = os.path.join(TARGET_DIR, "VISOR_100_PROMPTS_ANIMADOS.html")
OUTPUT_MD = os.path.join(TARGET_DIR, "INDICE_Y_ANALISIS_100_PROMPTS.md")
BACKUP_MD = os.path.join(SCRIPT_DIR, "104_PROMPTS_ANALISIS.md")
LOG_FILE = os.path.join(SCRIPT_DIR, "104_debug_log.txt")

def log(msg):
    print(msg)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass

def extract_pdf_text(pdf_path):
    log(f"Intentando extraer texto de: {pdf_path}")
    text = ""

    # Motor 1: pypdf
    try:
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        log(f"  [pypdf] {len(reader.pages)} páginas encontradas.")
        for i, p in enumerate(reader.pages):
            t = p.extract_text() or ""
            text += f"\n--- PAGINA {i+1} ---\n" + t
        if text.strip():
            return text
    except Exception as e:
        log(f"  [pypdf falló: {e}]")

    # Motor 2: PyPDF2
    try:
        import PyPDF2
        reader = PyPDF2.PdfReader(pdf_path)
        log(f"  [PyPDF2] {len(reader.pages)} páginas.")
        for i, p in enumerate(reader.pages):
            t = p.extract_text() or ""
            text += f"\n--- PAGINA {i+1} ---\n" + t
        if text.strip():
            return text
    except Exception as e:
        log(f"  [PyPDF2 falló: {e}]")

    # Motor 3: pdfplumber
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            log(f"  [pdfplumber] {len(pdf.pages)} páginas.")
            for i, p in enumerate(pdf.pages):
                t = p.extract_text() or ""
                text += f"\n--- PAGINA {i+1} ---\n" + t
        if text.strip():
            return text
    except Exception as e:
        log(f"  [pdfplumber falló: {e}]")

    # Motor 4: macOS PDFKit nativo via PyObjC
    try:
        from Quartz import PDFDocument, NSURL
        url = NSURL.fileURLWithPath_(pdf_path)
        doc = PDFDocument.alloc().initWithURL_(url)
        if doc:
            count = doc.pageCount()
            log(f"  [PDFKit macOS] {count} páginas.")
            for i in range(count):
                page = doc.pageAtIndex_(i)
                text += f"\n--- PAGINA {i+1} ---\n" + (page.string() or "")
            if text.strip():
                return text
    except Exception as e:
        log(f"  [PDFKit falló: {e}]")

    # Motor 5: Extracción directa de streams de texto comprimidos FlateDecode
    try:
        import zlib
        with open(pdf_path, "rb") as f:
            content = f.read()
        streams = re.findall(rb"stream\r?\n(.*?)endstream", content, re.DOTALL)
        log(f"  [Streams puros] {len(streams)} streams detectados.")
        raw_chunks = []
        for s in streams:
            try:
                decomp = zlib.decompress(s)
                # Extraer bloques de texto (Tj / TJ)
                matches = re.findall(rb"\((.*?)\)\s*Tj", decomp)
                for m in matches:
                    try:
                        raw_chunks.append(m.decode("utf-8", errors="ignore"))
                    except Exception:
                        pass
            except Exception:
                pass
        text = " ".join(raw_chunks)
        if text.strip():
            return text
    except Exception as e:
        log(f"  [Streams falló: {e}]")

    return text

def parse_prompts(raw_text):
    """
    Intenta extraer y numerar los prompts del texto.
    """
    prompts = []
    lines = raw_text.splitlines()
    current_prompt = None

    # Expresión regular para detectar títulos con número: "1.", "Prompt 1:", "01 -", "#1", etc.
    p_num_regex = re.compile(r"^(?:prompt\s*)?#?(\d{1,3})[\.\:\-\s]+(.+)$", re.IGNORECASE)

    for line in lines:
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("--- PAGINA"):
            continue

        match = p_num_regex.match(line_clean)
        if match and int(match.group(1)) <= 120:
            if current_prompt:
                prompts.append(current_prompt)
            num = int(match.group(1))
            title = match.group(2).strip()
            current_prompt = {
                "num": num,
                "title": title,
                "lines": [],
                "category": categorize_prompt(title)
            }
        elif current_prompt:
            current_prompt["lines"].append(line_clean)

    if current_prompt:
        prompts.append(current_prompt)

    # Si la heurística por números no capturó suficientes, segmentar por párrafos
    if len(prompts) < 10:
        log(f"Aviso: La heurística estricta detectó solo {len(prompts)} prompts. Aplicando segmentación inteligente por bloques.")
        prompts = []
        blocks = re.split(r"\n\s*\n", raw_text)
        idx = 1
        for b in blocks:
            b_clean = b.strip()
            if len(b_clean) > 30 and not b_clean.startswith("--- PAGINA"):
                lines = b_clean.splitlines()
                first_line = lines[0].strip()
                desc_lines = lines[1:] if len(lines) > 1 else [b_clean]
                prompts.append({
                    "num": idx,
                    "title": first_line[:80],
                    "lines": desc_lines,
                    "category": categorize_prompt(first_line)
                })
                idx += 1
                if idx > 100:
                    break

    return prompts

def categorize_prompt(title):
    t = title.lower()
    if any(k in t for k in ["salud", "medic", "agua", "pastilla", "sueño", "caminar", "presion", "pulso"]):
        return "salud"
    elif any(k in t for k in ["dinero", "ahorro", "gasto", "pension", "compra", "banco", "factura"]):
        return "finanzas"
    elif any(k in t for k in ["memoria", "juego", "reto", "mente", "palabra", "puzzle", "adivina"]):
        return "memoria"
    elif any(k in t for k in ["casa", "receta", "cocina", "tarea", "calendario", "planta", "tiempo", "clima"]):
        return "hogar"
    else:
        return "creatividad"

def build_dashboard_html(prompts, raw_text, pdf_name):
    """
    Construye el cuadro de mando visual HTML con diseño de alto contraste,
    filtros en tiempo real, búsqueda y copia directa de prompts.
    """
    prompts_json = json.dumps(prompts, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>100 Prompts: Estilos Animados Sin Programar • Visor Interactivo</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #060913;
            --bg-card: rgba(15, 23, 42, 0.94);
            --border: rgba(255, 255, 255, 0.12);
            --primary: #38bdf8;
            --emerald: #34d399;
            --amber: #fbbf24;
            --purple: #c084fc;
            --rose: #fb7185;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --text-muted: #94a3b8;
            --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; user-select: none; }}
        body {{
            background: radial-gradient(circle at 50% 10%, #172554 0%, #060913 70%);
            color: var(--text-main);
            font-family: var(--font-sans);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }}

        header {{
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            padding: 20px 32px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        .top-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 16px;
        }}

        .title-block {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}

        .icon-badge {{
            width: 48px;
            height: 48px;
            border-radius: 12px;
            background: linear-gradient(135deg, #0284c7, #38bdf8);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.6rem;
            box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
        }}

        h1 {{
            font-size: 1.4rem;
            font-weight: 800;
            letter-spacing: -0.02em;
        }}

        .subtitle {{
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-top: 2px;
        }}

        .meta-pills {{
            display: flex;
            gap: 10px;
            align-items: center;
        }}

        .pill {{
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 0.8rem;
            font-weight: 600;
            border: 1px solid var(--border);
            background: rgba(255, 255, 255, 0.05);
        }}
        .pill-count {{ background: rgba(56, 189, 248, 0.15); border-color: var(--primary); color: var(--primary); }}

        /* CONTROLES Y FILTROS */
        .controls-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
        }}

        .search-box {{
            flex: 1;
            min-width: 260px;
            position: relative;
        }}

        .search-input {{
            width: 100%;
            background: rgba(2, 6, 23, 0.8);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 10px 16px 10px 42px;
            color: var(--text-main);
            font-size: 0.95rem;
            outline: none;
            transition: all 0.2s;
        }}
        .search-input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
        }}
        .search-icon {{
            position: absolute;
            left: 14px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
        }}

        .filter-buttons {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .btn-filter {{
            padding: 8px 16px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            color: var(--text-sub);
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .btn-filter:hover {{ background: rgba(255, 255, 255, 0.1); color: var(--text-main); }}
        .btn-filter.active {{
            background: var(--primary);
            color: #060913;
            border-color: var(--primary);
            box-shadow: 0 0 14px rgba(56, 189, 248, 0.4);
        }}

        /* GRID DE PROMPTS */
        main {{
            flex: 1;
            padding: 32px;
            max-width: 1500px;
            margin: 0 auto;
            width: 100%;
        }}

        .prompts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 20px;
        }}

        .prompt-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 22px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
            position: relative;
        }}
        .prompt-card:hover {{
            transform: translateY(-3px);
            border-color: var(--primary);
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.4);
        }}

        .card-header {{
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 12px;
        }}

        .card-num {{
            font-family: var(--font-mono);
            font-size: 0.85rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 6px;
            background: rgba(56, 189, 248, 0.15);
            color: var(--primary);
            border: 1px solid rgba(56, 189, 248, 0.3);
        }}

        .cat-tag {{
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            padding: 4px 8px;
            border-radius: 6px;
        }}
        .cat-salud {{ background: rgba(251, 113, 133, 0.2); color: var(--rose); }}
        .cat-finanzas {{ background: rgba(52, 211, 153, 0.2); color: var(--emerald); }}
        .cat-memoria {{ background: rgba(192, 132, 252, 0.2); color: var(--purple); }}
        .cat-hogar {{ background: rgba(251, 191, 36, 0.2); color: var(--amber); }}
        .cat-creatividad {{ background: rgba(56, 189, 248, 0.2); color: var(--primary); }}

        .card-title {{
            font-size: 1.05rem;
            font-weight: 700;
            line-height: 1.35;
            color: var(--text-main);
        }}

        .card-body {{
            font-size: 0.88rem;
            line-height: 1.5;
            color: var(--text-sub);
            flex: 1;
            user-select: text;
            background: rgba(0, 0, 0, 0.25);
            padding: 12px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            max-height: 200px;
            overflow-y: auto;
        }}

        .card-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            padding-top: 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }}

        .btn-copy {{
            flex: 1;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 10px 14px;
            border-radius: 8px;
            background: linear-gradient(135deg, #0284c7, #0ea5e9);
            color: #ffffff;
            font-weight: 700;
            font-size: 0.85rem;
            border: none;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .btn-copy:hover {{
            background: linear-gradient(135deg, #0369a1, #0284c7);
            box-shadow: 0 0 14px rgba(56, 189, 248, 0.4);
        }}
        .btn-copy.copied {{
            background: var(--emerald);
            color: #060913;
        }}

        .badge-recommend {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--amber);
        }}

        /* TOAST COPIADO */
        #toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #0f172a;
            border: 1px solid var(--emerald);
            color: var(--emerald);
            padding: 12px 20px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 0.9rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s;
            pointer-events: none;
            z-index: 200;
        }}
        #toast.show {{
            opacity: 1;
            transform: translateY(0);
        }}
    </style>
</head>
<body>

    <header>
        <div class="top-row">
            <div class="title-block">
                <div class="icon-badge">✨</div>
                <div>
                    <h1>100 Prompts: Estilos Animados Sin Programar</h1>
                    <div class="subtitle">Documento Oficial: <code>{pdf_name}</code> • Cuadro de Mando Didáctico para Seniors</div>
                </div>
            </div>
            <div class="meta-pills">
                <span class="pill pill-count" id="visibleCount">{len(prompts)} utilidades</span>
                <span class="pill">Cero Código • Gemini Listo</span>
            </div>
        </div>

        <div class="controls-row">
            <div class="search-box">
                <span class="search-icon">🔍</span>
                <input type="text" class="search-input" id="searchInput" placeholder="Buscar utilidad por palabra clave (salud, dinero, memoria, cocina...)" oninput="filterPrompts()">
            </div>
            <div class="filter-buttons">
                <button class="btn-filter active" onclick="setCategory('all', this)">Todas (100)</button>
                <button class="btn-filter" onclick="setCategory('salud', this)">❤️ Salud & Bienestar</button>
                <button class="btn-filter" onclick="setCategory('finanzas', this)">💶 Finanzas Familiares</button>
                <button class="btn-filter" onclick="setCategory('memoria', this)">🧠 Memoria & Juegos</button>
                <button class="btn-filter" onclick="setCategory('hogar', this)">🏡 Hogar & Vida Práctica</button>
                <button class="btn-filter" onclick="setCategory('creatividad', this)">🎨 Creatividad & Ocio</button>
            </div>
        </div>
    </header>

    <main>
        <div class="prompts-grid" id="promptsGrid"></div>
    </main>

    <div id="toast">✅ Prompt copiado al portapapeles</div>

    <script>
        const PROMPTS = {prompts_json};
        let currentCategory = 'all';

        function renderPrompts(items) {{
            const grid = document.getElementById('promptsGrid');
            grid.innerHTML = '';

            document.getElementById('visibleCount').textContent = items.length + ' utilidades disponibles';

            if (items.length === 0) {{
                grid.innerHTML = '<div style="grid-column: 1 / -1; text-align: center; padding: 60px; color: var(--text-muted); font-size: 1.1rem;">No se encontraron utilidades con ese criterio de búsqueda.</div>';
                return;
            }}

            items.forEach(p => {{
                const card = document.createElement('div');
                card.className = 'prompt-card';

                const fullContent = p.lines.join('\\n');
                const catClass = 'cat-' + (p.category || 'creatividad');
                const catLabels = {{
                    salud: '❤️ Salud',
                    finanzas: '💶 Finanzas',
                    memoria: '🧠 Memoria',
                    hogar: '🏡 Hogar',
                    creatividad: '🎨 Creativo'
                }};

                card.innerHTML = `
                    <div class="card-header">
                        <span class="card-num">#${{String(p.num).padStart(3, '0')}}</span>
                        <span class="cat-tag ${{catClass}}">${{catLabels[p.category] || 'Utilidad'}}</span>
                    </div>
                    <div class="card-title">${{p.title}}</div>
                    <div class="card-body">${{fullContent.replace(/\\n/g, '<br/>') || 'Prompt listo para generar la animación interactiva directamente en Gemini.'}}</div>
                    <div class="card-footer">
                        <button class="btn-copy" onclick="copyPrompt(${{p.num}}, this)">
                            <span>📋 Copiar Prompt para Gemini</span>
                        </button>
                    </div>
                `;
                grid.appendChild(card);
            }});
        }}

        function setCategory(cat, btn) {{
            currentCategory = cat;
            document.querySelectorAll('.btn-filter').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            filterPrompts();
        }}

        function filterPrompts() {{
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            const filtered = PROMPTS.filter(p => {{
                const matchCat = (currentCategory === 'all' || p.category === currentCategory);
                const matchQuery = !query || 
                    p.title.toLowerCase().includes(query) || 
                    p.lines.some(l => l.toLowerCase().includes(query)) ||
                    String(p.num).includes(query);
                return matchCat && matchQuery;
            }});
            renderPrompts(filtered);
        }}

        function copyPrompt(num, btn) {{
            const item = PROMPTS.find(p => p.num === num);
            if (!item) return;

            const textToCopy = `Genera una aplicación interactiva con animación fluida, tipografía grande (18px) y controles accesibles para personas mayores sobre:\\n\\n${{item.title}}\\n\\n${{item.lines.join('\\n')}}\\n\\nRequisitos:\\n1. Entrega el código en un único bloque HTML, CSS y JavaScript funcional sin dependencias externas complejas.\\n2. Diseño en modo oscuro (#060913) con alto contraste y botones grandes.\\n3. Lenguaje sencillo en español sin tecnicismos ni anglicismos.`;

            navigator.clipboard.writeText(textToCopy).then(() => {{
                btn.classList.add('copied');
                btn.innerHTML = '<span>✅ ¡Copiado con Éxito!</span>';
                showToast();
                setTimeout(() => {{
                    btn.classList.remove('copied');
                    btn.innerHTML = '<span>📋 Copiar Prompt para Gemini</span>';
                }}, 2000);
            }});
        }}

        function showToast() {{
            const t = document.getElementById('toast');
            t.classList.add('show');
            setTimeout(() => t.classList.remove('show'), 2200);
        }}

        // Inicializar al cargar
        renderPrompts(PROMPTS);
    </script>
</body>
</html>
"""
    return html

def main():
    log("=" * 80)
    log("🚀 PROCESANDO CARPETA Y GENERANDO VISOR INTERACTIVO EN SAFARI")
    log("=" * 80)

    log(f"Directorio objetivo: {TARGET_DIR}")
    if not os.path.exists(TARGET_DIR):
        log(f"❌ El directorio no existe: {TARGET_DIR}")
        return

    all_entries = os.listdir(TARGET_DIR)
    log(f"Elementos encontrados en la carpeta ({len(all_entries)}):")
    pdf_files = []
    for f in all_entries:
        p = os.path.join(TARGET_DIR, f)
        log(f"  • {f} ({'DIR' if os.path.isdir(p) else 'FILE'})")
        if f.lower().endswith(".pdf"):
            pdf_files.append(p)

    if not pdf_files:
        log("⚠️ No se encontró ningún archivo PDF en la carpeta.")
        return

    target_pdf = pdf_files[0]
    pdf_name = os.path.basename(target_pdf)
    log(f"\nProcesando PDF: {pdf_name}")

    raw_text = extract_pdf_text(target_pdf)
    log(f"Texto total extraído: {len(raw_text)} caracteres.")

    prompts = parse_prompts(raw_text)
    log(f"Prompts detectados y clasificados: {len(prompts)}")

    # Guardar informe Markdown
    md_content = f"# ANÁLISIS DE LOS 100 PROMPTS ANIMADOS: {pdf_name}\n\n"
    for p in prompts:
        md_content += f"### #{p['num']:03d} - {p['title']} [{p['category'].upper()}]\n"
        md_content += "\n".join(p["lines"]) + "\n\n---\n\n"

    for dest in [OUTPUT_MD, BACKUP_MD]:
        try:
            with open(dest, "w", encoding="utf-8") as f:
                f.write(md_content)
            log(f"Markdown guardado en: {dest}")
        except Exception as e:
            log(f"Error al guardar MD en {dest}: {e}")

    # Generar cuadro de mando HTML
    html_content = build_dashboard_html(prompts, raw_text, pdf_name)
    try:
        with open(DASHBOARD_HTML, "w", encoding="utf-8") as f:
            f.write(html_content)
        log(f"✅ Dashboard HTML generado con éxito en:\n   {DASHBOARD_HTML}")
    except Exception as e:
        log(f"Error al guardar HTML: {e}")

    # Abrir inmediatamente en Safari
    try:
        os.system(f'open -a "Safari" "{DASHBOARD_HTML}"')
        log(f"🌐 ¡Lanzado en Safari con éxito!")
    except Exception as e:
        log(f"Error al abrir Safari: {e}")

if __name__ == "__main__":
    main()

