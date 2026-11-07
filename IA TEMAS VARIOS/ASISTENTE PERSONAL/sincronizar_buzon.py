#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sincronizar_buzon.py
Lee las ideas dictadas desde el iPhone en 'BUZON_IDEAS.txt' dentro de iCloud Shortcuts,
las clasifica inteligentemente por TEMAS (Robótica, IA, Salud, Música, Personal),
y las inserta directamente en 'BUZON_IDEAS_VOZ.md'.
"""

import os
import sys
import datetime
import re

try:
    from generar_pdf_reporte import generar_pdf
except ImportError:
    generar_pdf = None

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
BUZON_MD = os.path.join(WORKSPACE_DIR, "BUZON_IDEAS_VOZ.md")
LOCAL_COPY = os.path.join(WORKSPACE_DIR, "BUZON_IDEAS_RECIBIDAS.txt")
ROOT_DIR = os.path.abspath(os.path.join(WORKSPACE_DIR, "..", ".."))
MIRROR_MD = os.path.join(ROOT_DIR, "CURSO-IA", "IA TEMAS VARIOS", "ASISTENTE PERSONAL", "BUZON_IDEAS_VOZ.md")

ICLOUD_SHORTCUTS_DIR = os.path.expanduser("~/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents")
SHORTCUTS_TXT = os.path.join(ICLOUD_SHORTCUTS_DIR, "BUZON_IDEAS.txt")

SECCIONES_MAP = {
    "robotica": "## 🤖 1. ROBÓTICA (`CURSO-ROBOTICA-V2`)",
    "ia": "## 🧠 2. INTELIGENCIA ARTIFICIAL (`CURSO-IA`)",
    "salud": "## 🩺 3. SALUD Y BIOMECÁNICA (`IA TEMAS VARIOS`)",
    "musica": "## 🎹 4. MÚSICA Y WEB MIDI (`CURSO_MUSICA`)",
    "personal": "## 🛠️ 5. HOGAR Y PROYECTOS PERSONALES"
}

def corregir_fonetica(texto):
    """Corrige erratas fonéticas habituales de Siri."""
    t = texto.strip()
    reemplazos = {
        "de ella": "de IA",
        "la ella": "la IA",
        "una ella": "una IA",
        "inteligencia artificial": "IA",
        "motor huar": "motor Warp",
        "motor bar": "motor Warp",
        "star trek": "Star Trek",
        "inter estelar": "Interstellar",
        "licores": "picores"
    }
    for k, v in reemplazos.items():
        if k in t.lower():
            t = re.sub(re.escape(k), v, t, flags=re.IGNORECASE)
    return t

def detectar_tema_contextual(texto, default=None):
    """Deduce el tema por palabras clave inteligentes."""
    t_lower = texto.lower()
    
    # Robótica
    if any(w in t_lower for w in ["robot", "star trek", "warp", "nave", "espacial", "lego", "arduino", "mro", "iss", "interstellar", "spacex"]):
        return "robotica"
        
    # Salud y Biomecánica
    elif any(w in t_lower for w in [
        "alerg", "espalda", "modic", "médic", "pastill", "medicament", "colesterol", 
        "rodilla", "infiltraci", "ecograf", "anal[ií]tic", "análisis", "sangre", "cita", 
        "consulta", "resonancia", "radiograf", "cl[ií]nic", "hospital", "receta", 
        "traumat[oó]log", "alerg[oó]log", "digestivo", "bempedoico", "nexletol", "atorvastatina"
    ]):
        return "salud"
        
    # Inteligencia Artificial
    elif any(w in t_lower for w in [
        "ia", "gemini", "monogr[aá]fico", "notebooklm", "chatgpt", "claude", "prompt", 
        "inteligencia", "c[oó]digo", "probador", "simulador"
    ]):
        return "ia"
        
    # Música y Web MIDI
    elif any(w in t_lower for w in ["korg", "midi", "canci[oó]n", "partitura", "piano", "teclado", "m[uú]sica", "ek-50", "atril", "volumen"]):
        return "musica"
        
    # Hogar y Proyectos Personales
    elif any(w in t_lower for w in [
        "caldera", "casa", "comprar", "banco", "coche", "residencia", "casablanca", 
        "fianza", "contrato", "alquiler", "factura", "luz", "agua", "gas", "seguro"
    ]):
        return "personal"
        
    return default if default else "ia"

def desglosar_items(lineas):
    """
    Desglosa una lista de líneas en ítems individuales (tema, texto_item).
    Permite:
    1. Dictado con saltos de línea ("nueva línea" o "punto y aparte" en Siri).
    2. Enumeraciones verbales: "primero...", "segundo...", "tercero..."
    3. Puntos numerados: "punto 1...", "punto 2...", "1...", "2..."
    4. Mantiene el tema para todos los puntos si se especificó al inicio.
    """
    items_finales = []
    tema_actual = "ia"

    for linea in lineas:
        l = linea.strip()
        if not l:
            continue

        l_norm = corregir_fonetica(l)

        # Detectar si esta línea declara un tema explícito
        m = re.match(r'^(?:tema\s+)?(rob[oó]tica|ia|salud|m[uú]sica|personal|hogar)[\s:,\.-]+(.*)$', l_norm, re.IGNORECASE)
        subetiqueta = ""
        if m:
            tema_palabra = m.group(1).lower()
            if "rob" in tema_palabra: tema_actual = "robotica"
            elif "ia" in tema_palabra: tema_actual = "ia"
            elif "salud" in tema_palabra: tema_actual = "salud"
            elif "mús" in tema_palabra or "mus" in tema_palabra: tema_actual = "musica"
            elif "person" in tema_palabra or "hogar" in tema_palabra: tema_actual = "personal"
            resto = m.group(2).strip()
        else:
            # Comprobar si dice 'Tema <Nombre Personalizado>' (ej: Tema Residencia Casablanca...)
            m_custom = re.match(r'^tema\s+([^:.\n]+?)[:.\n]\s*(.*)$', l_norm, re.IGNORECASE)
            if m_custom:
                nombre_tema = m_custom.group(1).strip()
                tema_actual = detectar_tema_contextual(nombre_tema, default="personal")
                subetiqueta = f"**[{nombre_tema.title()}]**: "
                resto = m_custom.group(2).strip()
            else:
                resto = l_norm

        if not resto:
            continue

        # Separadores estrictos (requieren punto, salto de línea, punto y coma o inicio para no partir fechas ni cantidades)
        patron_separadores = r'(?:^|[\.\n;]\s*|\s*,\s*)(?:primero|segundo|tercero|cuarto|quinto|sexto|s[eé]ptimo|octavo|noveno|d[eé]cimo|punto\s+\d+|paso\s+\d+|\b\d+(?!\.\d)[\.\)\-]?|\b(?:uno|dos|tres|cuatro|cinco)\b)[\s:,\.-]+'
        partes = re.split(patron_separadores, resto, flags=re.IGNORECASE)
        partes_limpias = []
        for p in partes:
            p_limp = p.strip(" ,;.-")
            if p_limp and p_limp.lower() not in ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"]:
                # Limpiar número huérfano final si el usuario paró tras decir el número
                p_limp = re.sub(r'[\.\s,;\-]+(?:uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|\b\d+\b)\s*$', '', p_limp, flags=re.IGNORECASE).strip()
                if p_limp:
                    partes_limpias.append(p_limp)

        if len(partes_limpias) > 1:
            for p in partes_limpias:
                texto_item = f"{subetiqueta}{p}" if subetiqueta and not p.startswith("**[") else p
                items_finales.append((tema_actual, texto_item))
        else:
            if not m and not m_custom:
                tema_linea = detectar_tema_contextual(resto, default=tema_actual)
            else:
                tema_linea = tema_actual
            texto_item = f"{subetiqueta}{resto}" if subetiqueta and not resto.startswith("**[") else resto
            items_finales.append((tema_linea, texto_item))

    return items_finales

def renumerar_tareas(contenido):
    """Garantiza que todas las tareas activas tengan una numeración correlativa continua [#01], [#02]..."""
    partes = contenido.split("## ✅ TAREAS COMPLETADAS Y ARCHIVADAS")
    activo = partes[0]
    historico = "## ✅ TAREAS COMPLETADAS Y ARCHIVADAS" + partes[1] if len(partes) > 1 else ""

    contador = 1
    lineas_nuevas = []
    for l in activo.splitlines():
        if l.strip().startswith("- [ ]"):
            l_limpia = re.sub(r"^-\s*\[\s*\]\s*(\*\*\[#\d+\]\*\*\s*|\[#\d+\]\s*)?", "", l.strip())
            lineas_nuevas.append(f"- [ ] **[#{contador:02d}]** {l_limpia}")
            contador += 1
        else:
            lineas_nuevas.append(l)

    return "\n".join(lineas_nuevas).rstrip() + ("\n\n" + historico.strip() if historico else "\n")

def sincronizar(silencioso=False):
    if not silencioso:
        print("=" * 60)
        print("=== SINCRONIZACIÓN DE IDEAS DE VOZ (iPHONE ➔ ANTIGRAVITY) ===")
        print("=" * 60)
    
    if not os.path.exists(SHORTCUTS_TXT) or os.path.getsize(SHORTCUTS_TXT) == 0:
        if not silencioso:
            print("ℹ️ No hay notas nuevas dictadas pendientes en el iPhone.")
            mostrar_resumen_activo()
        return

    try:
        with open(SHORTCUTS_TXT, "r", encoding="utf-8", errors="ignore") as f:
            lineas = [l.strip() for l in f.readlines() if l.strip()]
    except Exception as e:
        if not silencioso:
            print(f"⚠️ Error al leer el archivo de iCloud: {e}")
        return

    if not lineas:
        if not silencioso:
            print("ℹ️ No hay notas nuevas dictadas pendientes en el iPhone.")
            mostrar_resumen_activo()
        return

    items = desglosar_items(lineas)
    if not items:
        if not silencioso:
            print("ℹ️ No se detectaron tareas válidas para integrar.")
        return

    if not silencioso:
        print(f"📥 Se han extraído {len(items)} tarea(s) individual(es):")
    ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    if not os.path.exists(BUZON_MD):
        print(f"⚠️ No se encontró {BUZON_MD}")
        return

    with open(BUZON_MD, "r", encoding="utf-8") as f:
        contenido = f.read()

    for tema, item_texto in items:
        # Evitar duplicados exactos si ya existen en el archivo
        item_normalizado = item_texto.strip().lower()
        if item_normalizado in contenido.lower():
            if not silencioso:
                print(f"   ⏩ Ya existe (omitido duplicado): «{item_texto}»")
            continue

        if not silencioso:
            print(f"   • [{tema.upper()}] ➔ «{item_texto}»")
        nueva_linea = f"- [ ] **[{ahora} - Dictado iPhone]**: {item_texto}\n"
        
        header_seccion = SECCIONES_MAP.get(tema, SECCIONES_MAP["ia"])
        if header_seccion in contenido:
            partes = contenido.split(header_seccion)
            contenido = partes[0] + header_seccion + "\n" + nueva_linea + partes[1]
        else:
            contenido += f"\n{nueva_linea}"

    # Renumerar todas las tareas correlativamente (#01, #02, ...)
    contenido = renumerar_tareas(contenido)

    with open(BUZON_MD, "w", encoding="utf-8") as f:
        f.write(contenido)

    if os.path.dirname(MIRROR_MD) and os.path.exists(os.path.dirname(MIRROR_MD)):
        with open(MIRROR_MD, "w", encoding="utf-8") as f:
            f.write(contenido)

    # Actualizar PDF estático automáticamente
    if generar_pdf:
        try:
            generar_pdf()
        except Exception as e:
            if not silencioso:
                print(f"⚠️ Error al actualizar PDF: {e}")

    # Copia local de histórico
    with open(LOCAL_COPY, "a", encoding="utf-8") as f:
        for l in lineas:
            f.write(f"[{ahora}] {l}\n")

    # Limpiar archivo de entrada en iCloud
    with open(SHORTCUTS_TXT, "w", encoding="utf-8") as f:
        f.write("")

    print(f"✅ Ideas clasificadas e integradas correctamente en {BUZON_MD}")
    print("🧹 Entrada de iCloud lista para el siguiente dictado.")

    mostrar_resumen_activo(contenido)

def mostrar_resumen_activo(contenido=None):
    if generar_pdf:
        try:
            generar_pdf()
        except Exception:
            pass

    if not contenido:
        if os.path.exists(BUZON_MD):
            with open(BUZON_MD, "r", encoding="utf-8") as f:
                contenido = f.read()
        else:
            return

    print("\n" + "=" * 60)
    print("📋 RESUMEN CONSOLIDADO DE TAREAS PENDIENTES POR TEMA")
    print("=" * 60)
    for linea in contenido.splitlines():
        if linea.startswith("## ") and not "COMPLETADAS" in linea:
            print(f"\n{linea}")
        elif linea.strip().startswith("- [ ]"):
            print(f"  {linea.strip()}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    silencioso = "--daemon" in sys.argv or "--silencioso" in sys.argv
    sincronizar(silencioso=silencioso)
