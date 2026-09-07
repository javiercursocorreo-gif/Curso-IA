#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_monografico_7_mapa_gestion.py
Genera todos los materiales para el Monográfico 7:
"Mapa de la Gestión del Proyecto con IA (Arquitectura y Flujo de Trabajo)"
Optimizado para su explotación con NotebookLM (fuente + prompts),
ficha oficial en PDF (ReportLab) y DOCX, e infografía interactiva en HTML.
"""

import os
import sys
import docx
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

ROOT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
MONO7_DIR = os.path.join(ROOT_DIR, "CLASES", "7. MAPA_GESTION_PROYECTO_CON_IA")
APP_DIR = os.path.join(MONO7_DIR, "app")
os.makedirs(APP_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# 1. GENERAR FUENTE DE TEXTO Y DOCX PARA NOTEBOOKLM
# -------------------------------------------------------------------------
FUENTE_TEXTO = """# 🗺️ EL MAPA DE LA GESTIÓN DEL PROYECTO CON IA
## Cómo Diseñamos, Construimos y Publicamos este Curso Trabajando en Equipo (Profesor + IA + GitHub + Classroom)

---

### 1. INTRODUCCIÓN: LA REVOLUCIÓN DEL "EQUIPO DE DOS"
Tradicionalmente, diseñar un programa formativo completo de más de 60 clases técnicas con infografías, simuladores tridimensionales interactivos, presentaciones ilustradas, vídeos dinámicos y fichas didácticas exigía un departamento entero: diseñadores gráficos, programadores, maquetadores y coordinadores pedagógicos.

En este curso demostramos un nuevo paradigma de productividad personal: el **"Equipo de Dos"**.
1. **Tú (El Profesor):** Aportas la visión pedagógica, la experiencia de vida, la empatía con el alumnado sénior, los contenidos temáticos y las directrices éticas.
2. **Antigravity (Tu Copiloto IA en el PC):** Asume el papel de taller de desarrollo autónomo: programa simuladores en JavaScript, maqueta documentos en PDF con diseño profesional, automatiza tareas repetitivas y genera la infraestructura digital en segundos.

El resultado es un ecosistema educativo de máxima calidad profesional, 100% gratuito en costes de servidor y accesible para cualquier persona desde su navegador web.

---

### 2. LOS 6 ENGRANAJES DEL SISTEMA (EL MAPA OPERATIVO)

#### ENGRANAJE 1: EL PROFESOR (El Director Creativo y Pedagógico)
* **Dónde reside:** En el mundo real, conociendo a sus alumnos.
* **Qué hace:** 
  * Decide qué conceptos enseñar en cada sesión (ej. "¿Cómo explicar la cinemática o la IA a personas de 70 años sin asustarlas?").
  * Diseña los guiones de clase, graba los vídeos explicativos de teoría y aporta los ejemplos cotidianos.
  * Supervisa y valida cada material generado por la IA antes de que llegue a los alumnos.

#### ENGRANAJE 2: ANTIGRAVITY (El Copiloto Técnico en el PC)
* **Dónde reside:** Dentro de tu ordenador ("MI PC").
* **Qué hace:**
  * Recibe tus instrucciones en lenguaje cotidiano (sin comandos crípticos).
  * Escribe código limpio en Python, HTML5, CSS y JavaScript para construir simuladores interactivos (como el dron 3D, el brazo robótico o la biografía familiar).
  * Corrige errores en bucle cerrado, comprueba la sintaxis y maqueta las fichas didácticas oficiales en PDF.
  * Es el bibliotecario digital que mantiene en perfecto orden miles de archivos multimedia.

#### ENGRANAJE 3: LAS TRES CARPETAS LOCALES (El Archivo Maestro en tu Mac)
* **Dónde residen:** En tu almacenamiento local sincronizado con iCloud.
* **Estructura modular:**
  1. `CURSO-ROBOTICA-V2`: Contiene los 8 grandes bloques de robótica física (motores, sensores, cinemática 3D, androides y animatrónica).
  2. `CURSO-IA`: Contiene el temario troncal de Inteligencia Artificial (60 sesiones prácticas, catálogo de fractales, monográficos y talleres de Gemini).
  3. `CURSO-ROBOTICA-IA-COMUN`: El nexo de unión donde residen las presentaciones inaugurales compartidas, las guías de publicación y las metodologías estándar.

#### ENGRANAJE 4: GITHUB Y GITHUB PAGES (La Gran Biblioteca en la Nube)
* **Dónde reside:** En internet (servidores seguros de GitHub / Microsoft).
* **Por qué es una decisión magistral:**
  * **0 € de coste:** Aloja gratuitamente todos los vídeos, documentos, fichas y aplicaciones interactivas.
  * **0 MB gastados en Google Drive:** Evita agotar el espacio de almacenamiento de tu cuenta personal de Google.
  * **Enlaces públicos permanentes:** Cada archivo subido recibe una dirección web propia (URL directa).
  * **Actualización instantánea:** Si un día corriges una errata en un PDF y lo vuelves a subir a GitHub, se actualiza automáticamente para todos los alumnos sin tener que reenviar enlaces.

#### ENGRANAJE 5: EL PUENTE AUTOMÁTICO (Paneles CSV + Google Sheets + Apps Script)
* **Dónde reside:** Entre tu PC y Google Drive.
* **El mecanismo:**
  1. Antigravity ejecuta un script robot (`generate_multiple_csvs.py`) que escanea tus carpetas y crea una tabla CSV con los títulos limpios, descripciones y URLs exactas de GitHub.
  2. Tú importas ese CSV en tu hoja de cálculo maestra de Google Sheets (**0.PANEL_CLASSROOM**).
  3. Pegas el número de identificación de tu clase (ID de curso).
  4. Ejecutas el botón de **Apps Script** (`publicarTodoConTemas`): en menos de 10 segundos, 60 materiales quedan creados, etiquetados por temas y colocados en modo **BORRADOR** en tu aula virtual.

#### ENGRANAJE 6: GOOGLE CLASSROOM Y LOS ALUMNOS SÉNIOR
* **Dónde reside:** En los ordenadores, tabletas y teléfonos de los alumnos.
* **La experiencia del usuario final:**
  * Los alumnos entran en su entorno escolar habitual y seguro de Google Classroom.
  * Ven las clases organizadas limpiamente por semanas o bloques temáticos.
  * Al hacer clic en "Ver Material", el PDF o el simulador se abre al instante en su pantalla, servido a máxima velocidad desde GitHub.
  * **Cero instalaciones:** No tienen que descargar programas raros, descomprimir archivos ZIP ni lidiar con contraseñas complejas.

---

### 3. CUADRO COMPARATIVO: MÉTODO TRADICIONAL VS. MÉTODO GESTIONADO CON IA

| Característica | Método Tradicional (Sin IA) | Método del Curso (Con Antigravity y GitHub) |
| :--- | :--- | :--- |
| **Tiempo de preparación** | Semanas de maquetación y formateo manual. | Horas: tú pones el criterio, la IA hace el ensamblaje técnico. |
| **Coste de servidores** | Cuentas de pago en almacenamiento en la nube o hosting. | **0 €:** GitHub Pages aloja todo sin coste. |
| **Espacio en Google Drive** | Saturación rápida con vídeos y presentaciones pesadas. | **0 MB ocupados en Drive:** Todo se sirve mediante enlaces externos. |
| **Publicación en Classroom** | Crear 60 materiales a mano uno por uno (cientos de clics). | **1 solo clic:** Subida masiva automatizada con Apps Script en 10 seg. |
| **Mantenimiento y cambios** | Modificar un PDF obligaba a borrar y resubir la tarea. | **Inmediato:** Se reemplaza el archivo en GitHub y el enlace sigue intacto. |

---

### 4. CONCLUSIÓN PEDAGÓGICA: LA TECNOLOGÍA AMABLE
Este mapa demuestra a los alumnos una lección fundamental: la Inteligencia Artificial no viene a sustituir la creatividad ni el afecto del profesor; es un exoesqueleto técnico que multiplica su capacidad de enseñar, liberándole de la burocracia digital para que pueda concentrarse en lo más valioso: acompañar, escuchar y orientar a sus alumnos en el aula.
"""

PROMPT_NOTEBOOKLM_TEXTO = """# 🎯 PROMPT MAESTRO PARA GENERAR LA PRESENTACIÓN Y MATERIALES EN NOTEBOOKLM
# Monográfico 7: Mapa de la Gestión del Proyecto con IA

Instrucciones para el profesor:
1. Abre tu cuaderno en NotebookLM (notebooklm.google.com).
2. Añade como fuente el archivo: "0.FUENTE_PARA_NOTEBOOKLM_MAPA_GESTION_PROYECTO_IA.docx" (o .txt).
3. En el cuadro de diálogo inferior, copia y pega cualquiera de los siguientes prompts según lo que desees obtener:

---

### OPCIÓN A: PARA GENERAR LA PRESENTACIÓN DE DIAPOSITIVAS (SLIDES)
Copia y pega este prompt:
"Actúa como un director de diseño educativo de prestigio. Basándote exhaustivamente en la fuente sobre el Mapa de Gestión del Proyecto con IA, diseña una presentación magistral de 8 a 10 diapositivas titulada 'EL MAPA DE LA GESTIÓN DEL PROYECTO CON IA'.
El objetivo es que los alumnos comprendan de forma asombrosa, sencilla y visual cómo se organiza y publica este curso entre el Profesor, Antigravity, GitHub y Google Classroom.

Para cada diapositiva proporciona:
1. TÍTULO DE LA DIAPOSITIVA (claro y en mayúsculas).
2. CONCEPTO CENTRAL (en 1 sola frase potente).
3. PUNTOS CLAVE (3 o 4 viñetas breves y didácticas).
4. ANALOGÍA VISUAL COTIDIANA (ej. comparar GitHub con una biblioteca pública, o Antigravity con un ayudante de taller).
5. MENSAJE CLAVE PARA RECORDAR.

Mantén un tono cálido, divulgativo, inspirador y adaptado a personas mayores de 65 años."

---

### OPCIÓN B: PARA GENERAR EL AUDIO OVERVIEW (PODCAST / DEEP DIVE EN ESPAÑOL)
Copia y pega este prompt:
"Genera una conversación radiofónica dinámica y entusiasta entre dos expertos educativos comentando la fuente. Deben analizar con admiración cómo un profesor senior ha creado un flujo de trabajo pionero que combina la IA local (Antigravity), el almacenamiento gratuito en la nube (GitHub) y la distribución en Google Classroom, logrando un proyecto educativo de enorme envergadura con cero costes de servidor y cero complicaciones para los alumnos. Haz que la conversación sea cercana, divertida y llena de ejemplos fáciles de entender."

---

### OPCIÓN C: PARA GENERAR UNA GUÍA RESUMIDA EN INFOGRAFÍA DE TEXTO
Copia y pega este prompt:
"Elabora una guía de referencia rápida en 5 pasos que resuma el viaje de un material escolar: desde que nace como idea en la mente del profesor, pasa por el teclado de Antigravity, se aloja en GitHub, se indexa en Google Sheets y termina en la pantalla del alumno en Classroom. Incluye una sección final con 'Los 3 Grandes Beneficios' (Cero coste, Cero espacio en Drive, Cero fricción)."
"""

# -------------------------------------------------------------------------
# 2. GENERAR ARCHIVO .DOCX CON PYTHON-DOCX
# -------------------------------------------------------------------------
def create_docx():
    docx_path = os.path.join(MONO7_DIR, "0.FUENTE_PARA_NOTEBOOKLM_MAPA_GESTION_PROYECTO_IA.docx")
    doc = docx.Document()
    
    # Configurar márgenes
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
        
    p_title = doc.add_paragraph()
    run_title = p_title.add_run("EL MAPA DE LA GESTIÓN DEL PROYECTO CON IA")
    run_title.font.name = "Arial"
    run_title.font.size = Pt(20)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(10, 37, 64) # #0A2540
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p_sub = doc.add_paragraph()
    run_sub = p_sub.add_run("Cómo Diseñamos, Construimos y Publicamos este Curso Trabajando en Equipo\n(Profesor + Antigravity + GitHub + Classroom + Alumnos)")
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(11)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(230, 92, 0) # #E65C00
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_paragraph()
    
    lines = FUENTE_TEXTO.split("\n")
    for line in lines:
        line_s = line.strip()
        if not line_s or line_s.startswith("#") or line_s.startswith("---"):
            continue
            
        if line_s.startswith("### "):
            h = doc.add_paragraph()
            r = h.add_run(line_s.replace("### ", ""))
            r.font.name = "Arial"
            r.font.size = Pt(14)
            r.font.bold = True
            r.font.color.rgb = RGBColor(10, 37, 64)
            h.paragraph_format.space_before = Pt(12)
            h.paragraph_format.space_after = Pt(4)
        elif line_s.startswith("#### "):
            h = doc.add_paragraph()
            r = h.add_run(line_s.replace("#### ", ""))
            r.font.name = "Arial"
            r.font.size = Pt(12)
            r.font.bold = True
            r.font.color.rgb = RGBColor(230, 92, 0)
            h.paragraph_format.space_before = Pt(8)
            h.paragraph_format.space_after = Pt(3)
        elif line_s.startswith("* ") or line_s.startswith("- "):
            p = doc.add_paragraph(style='List Bullet')
            text_item = line_s[2:]
            # Bold handling basic
            parts = text_item.split("**")
            for i, part in enumerate(parts):
                r = p.add_run(part)
                r.font.name = "Arial"
                r.font.size = Pt(10)
                if i % 2 == 1:
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(15, 23, 42)
                else:
                    r.font.color.rgb = RGBColor(51, 65, 85)
        else:
            p = doc.add_paragraph()
            parts = line_s.split("**")
            for i, part in enumerate(parts):
                r = p.add_run(part)
                r.font.name = "Arial"
                r.font.size = Pt(10.5)
                if i % 2 == 1:
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(15, 23, 42)
                else:
                    r.font.color.rgb = RGBColor(51, 65, 85)
            p.paragraph_format.space_after = Pt(6)
            
    doc.save(docx_path)
    print(f"✅ Documento Word generado: {docx_path}")

# -------------------------------------------------------------------------
# 3. GENERAR FICHA DIDÁCTICA EN PDF (REPORTLAB)
# -------------------------------------------------------------------------
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_decorations(self, page_count):
        self.saveState()
        # Top banner
        self.setFillColor(colors.HexColor("#0A2540"))
        self.rect(0, letter[1] - 32, letter[0], 32, stroke=0, fill=1)
        
        self.setFillColor(colors.white)
        self.setFont("Helvetica-Bold", 9)
        self.drawString(35, letter[1] - 20, "CURSO DE INTELIGENCIA ARTIFICIAL — MONOGRÁFICO 7")
        
        # Bottom rule & footer
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(35, 38, letter[0] - 35, 38)
        
        self.setFillColor(colors.HexColor("#64748B"))
        self.setFont("Helvetica", 8.5)
        self.drawString(35, 24, "Ficha Didáctica: El Mapa de la Gestión del Proyecto con IA")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(letter[0] - 35, 24, page_str)
        self.restoreState()

def create_pdf():
    pdf_path = os.path.join(MONO7_DIR, "FICHA_MONOGRAFICO_MAPA_GESTION_PROYECTO_IA.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=48
    )
    
    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#0A2540"),
        alignment=TA_CENTER,
        spaceAfter=4
    )
    
    style_subtitle = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#E65C00"),
        alignment=TA_CENTER,
        spaceAfter=14
    )
    
    style_h2 = ParagraphStyle(
        'Heading2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#0A2540"),
        spaceBefore=12,
        spaceAfter=6
    )
    
    style_body = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#334155"),
        alignment=TA_JUSTIFY,
        spaceAfter=8
    )
    
    style_bullet = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=4
    )
    
    elements = []
    
    elements.append(Paragraph("EL MAPA DE LA GESTIÓN DEL PROYECTO CON IA", style_title))
    elements.append(Paragraph("Arquitectura de Trabajo en Equipo: Profesor + Antigravity + GitHub + Classroom", style_subtitle))
    
    # Caja introductoria
    intro_html = (
        "<b>EL NUEVO MODELO DE TRABAJO:</b> En este monográfico descubrimos cómo se concibió, organizó y publicó "
        "todo este curso de Robótica e Inteligencia Artificial. No mediante grandes departamentos, sino mediante un "
        "<b>Equipo de Dos</b>: Tú (con tu criterio didáctico y experiencia docente) y <b>Antigravity</b> (tu copiloto en el PC), "
        "aprovechando la nube gratuita de GitHub y la sencillez de Google Classroom para los alumnos."
    )
    intro_table = Table([[Paragraph(intro_html, style_body)]], colWidths=[letter[0] - 72])
    intro_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    elements.append(intro_table)
    elements.append(Spacer(1, 10))
    
    elements.append(Paragraph("Los 6 Componentes Clave de la Arquitectura", style_h2))
    
    componentes = [
        ("1. EL PROFESOR (TÚ)", "#0284C7", "Director pedagógico. Decide qué temas enseñar, redacta contenidos, graba vídeos de teoría y adapta las clases a personas sénior."),
        ("2. ANTIGRAVITY EN EL PC", "#0A2540", "Copiloto técnico en local. Escribe código de simuladores, maqueta fichas PDF en ReportLab, genera CSVs y sincroniza con GitHub."),
        ("3. CARPETAS LOCALES", "#E65C00", "Estructura modular en tu Mac: <code>CURSO-ROBOTICA-V2</code>, <code>CURSO-IA</code> y <code>CURSO-ROBOTICA-IA-COMUN</code> sincronizadas en iCloud."),
        ("4. GITHUB / GITHUB PAGES", "#16A34A", "Almacén público en la nube. Aloja gratis los vídeos y PDFs, asigna URLs públicas permanentes y evita consumir tu espacio de Google Drive."),
        ("5. PANELES CSV Y EXCEL", "#7C3AED", "El puente automatizado. Los scripts de Antigravity generan las tablas que importas en Google Sheets. Con 1 clic en Apps Script se crea todo en Classroom."),
        ("6. ALUMNOS EN CLASSROOM", "#D97706", "Los alumnos ven todo ordenado por temas y sesiones. Al hacer clic en cualquier material, se abre al instante desde GitHub sin instalaciones.")
    ]
    
    t_rows = []
    for num_tit, color_hex, desc in componentes:
        p_col1 = Paragraph(f"<font color='{color_hex}'><b>{num_tit}</b></font>", ParagraphStyle('C1', fontName='Helvetica-Bold', fontSize=9.5, leading=12))
        p_col2 = Paragraph(desc, style_bullet)
        t_rows.append([p_col1, p_col2])
        
    comp_table = Table(t_rows, colWidths=[170, letter[0] - 72 - 170])
    comp_table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F1F5F9")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(comp_table)
    elements.append(Spacer(1, 10))
    
    elements.append(Paragraph("Los 3 Grandes Beneficios del Sistema", style_h2))
    
    ventajas = [
        ("💰 0 € de Coste de Infraestructura", "Todo el almacenamiento de vídeos, PDFs y aplicaciones interactivas está alojado gratis en GitHub Pages sin pagar suscripciones de servidores."),
        ("☁️ 0 MB Consumidos en Google Drive", "Google Classroom solo guarda los enlaces web hacia GitHub. Tu cuenta de Drive personal permanece con el 100% de su espacio libre."),
        ("⚡ 1 Clic para Publicar 60 Lecciones", "Gracias a Google Apps Script, no hay que crear tareas a mano una por una. Toda la clase queda montada en segundos en modo borrador.")
    ]
    
    v_rows = []
    for tit, desc in ventajas:
        v_rows.append([Paragraph(f"<b>{tit}</b>", ParagraphStyle('VT', fontName='Helvetica-Bold', fontSize=9.5, textColor=colors.HexColor("#0A2540")))])
        v_rows.append([Paragraph(desc, style_bullet)])
        
    v_table = Table(v_rows, colWidths=[letter[0] - 72])
    v_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    elements.append(v_table)
    
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"✅ Ficha Didáctica PDF generada: {pdf_path}")

# -------------------------------------------------------------------------
# 4. GENERAR INFOGRAFÍA WEB INTERACTIVA (APP/INDEX.HTML)
# -------------------------------------------------------------------------
def create_interactive_app():
    html_path = os.path.join(APP_DIR, "index.html")
    
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mapa de Gestión del Proyecto con IA — Arquitectura Educativa</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #0A1128;
      --card-bg: rgba(255, 255, 255, 0.05);
      --card-border: rgba(255, 255, 255, 0.12);
      --accent-blue: #0084FF;
      --accent-cyan: #00F2FE;
      --accent-orange: #FF6B35;
      --accent-green: #00E676;
      --accent-purple: #9D4EDD;
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: radial-gradient(circle at 50% 20%, #111D4A, var(--bg-dark) 80%);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }
    header {
      padding: 30px 20px 15px;
      text-align: center;
      background: rgba(10, 17, 40, 0.7);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--card-border);
    }
    .badge {
      display: inline-block;
      padding: 6px 14px;
      background: rgba(255, 107, 53, 0.15);
      border: 1px solid var(--accent-orange);
      color: var(--accent-orange);
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 1px;
      margin-bottom: 10px;
      text-transform: uppercase;
    }
    h1 {
      font-family: 'Outfit', sans-serif;
      font-size: 2.2rem;
      font-weight: 800;
      background: linear-gradient(135deg, #FFFFFF, var(--accent-cyan));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }
    p.subtitle {
      color: var(--text-muted);
      font-size: 1.05rem;
      max-width: 750px;
      margin: 0 auto;
    }
    .main-container {
      flex: 1;
      max-width: 1250px;
      margin: 0 auto;
      padding: 30px 20px;
      display: flex;
      flex-direction: column;
      gap: 30px;
    }
    .flow-wrapper {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--card-border);
      border-radius: 24px;
      padding: 30px 20px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.5);
      position: relative;
    }
    .zones-grid {
      display: grid;
      grid-template-columns: 1.2fr 0.9fr 0.9fr;
      gap: 25px;
    }
    @media (max-width: 992px) {
      .zones-grid { grid-template-columns: 1fr; }
    }
    .zone-box {
      background: var(--card-bg);
      border: 1px dashed var(--card-border);
      border-radius: 18px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    .zone-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1rem;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 8px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--card-border);
    }
    .node-card {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      padding: 16px;
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
    }
    .node-card:hover {
      transform: translateY(-3px);
      border-color: var(--accent-cyan);
      box-shadow: 0 10px 25px rgba(0, 242, 254, 0.2);
    }
    .node-card.active {
      border-color: var(--accent-orange);
      box-shadow: 0 0 25px rgba(255, 107, 53, 0.3);
      background: rgba(30, 41, 59, 0.95);
    }
    .node-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 8px;
    }
    .node-icon {
      font-size: 1.8rem;
      background: rgba(255, 255, 255, 0.08);
      width: 44px;
      height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 10px;
    }
    .node-title-text {
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: #FFF;
    }
    .node-role {
      font-size: 0.8rem;
      color: var(--accent-cyan);
      font-weight: 600;
    }
    .node-desc {
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.45;
    }
    .details-panel {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--accent-cyan);
      border-radius: 18px;
      padding: 25px;
      display: none;
      animation: fadeIn 0.4s ease;
    }
    .details-panel.visible { display: block; }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .details-panel h3 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.5rem;
      color: var(--accent-cyan);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .details-panel p {
      color: #CBD5E1;
      font-size: 1rem;
      line-height: 1.6;
      margin-bottom: 15px;
    }
    .pill-list {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }
    .pill {
      background: rgba(0, 132, 255, 0.15);
      border: 1px solid var(--accent-blue);
      color: #93C5FD;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 600;
    }
    .benefits-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }
    @media (max-width: 768px) {
      .benefits-grid { grid-template-columns: 1fr; }
    }
    .benefit-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      text-align: center;
    }
    .benefit-card h4 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      color: #FFF;
      margin-bottom: 8px;
    }
    .benefit-card p {
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.4;
    }
    footer {
      text-align: center;
      padding: 20px;
      color: var(--text-muted);
      font-size: 0.85rem;
      border-top: 1px solid var(--card-border);
    }
    .btn-action {
      background: linear-gradient(135deg, var(--accent-orange), #FF8E53);
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 10px;
      font-weight: 700;
      cursor: pointer;
      font-family: 'Plus Jakarta Sans', sans-serif;
      transition: opacity 0.2s;
      margin-top: 10px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .btn-action:hover { opacity: 0.9; }
  </style>
</head>
<body>

  <header>
    <div class="badge">Monográfico 7 · Arquitectura del Curso</div>
    <h1>El Mapa de la Gestión del Proyecto con IA</h1>
    <p class="subtitle">Descubre cómo creamos, organizamos y distribuimos todo este ecosistema educativo trabajando en equipo: Profesor + Copiloto IA + Nube Gratuita de GitHub + Google Classroom.</p>
  </header>

  <main class="main-container">
    
    <div class="flow-wrapper">
      <div class="zones-grid">
        
        <!-- ZONA 1: MI PC -->
        <div class="zone-box">
          <div class="zone-title" style="color: var(--accent-cyan);">
            💻 Zona 1: MI ORDENADOR (Local)
          </div>
          
          <div class="node-card" onclick="showDetails('profesor')">
            <div class="node-header">
              <div class="node-icon">🧑🏻‍🏫</div>
              <div>
                <div class="node-title-text">El Profesor (Tú)</div>
                <div class="node-role">Director Pedagógico</div>
              </div>
            </div>
            <div class="node-desc">Aporta las ideas, los temas, el cariño didáctico y graba los vídeos de teoría.</div>
          </div>

          <div class="node-card active" onclick="showDetails('antigravity')">
            <div class="node-header">
              <div class="node-icon">🤖</div>
              <div>
                <div class="node-title-text">Antigravity</div>
                <div class="node-role">Copiloto Técnico IA</div>
              </div>
            </div>
            <div class="node-desc">Programa simuladores, maqueta PDFs, genera CSVs y sincroniza con GitHub.</div>
          </div>

          <div class="node-card" onclick="showDetails('carpetas')">
            <div class="node-header">
              <div class="node-icon">📁</div>
              <div>
                <div class="node-title-text">3 Carpetas Maestras</div>
                <div class="node-role">Estructura Modular</div>
              </div>
            </div>
            <div class="node-desc">Robótica V2 + Curso IA + Carpeta Común organizadas limpiamente en tu Mac.</div>
          </div>

          <div class="node-card" onclick="showDetails('csvs')">
            <div class="node-header">
              <div class="node-icon">📄</div>
              <div>
                <div class="node-title-text">Paneles CSV / Excel</div>
                <div class="node-role">Puente de URLs</div>
              </div>
            </div>
            <div class="node-desc">Tablas de enlaces con URLs públicas y Apps Script para inyección a Classroom.</div>
          </div>
        </div>

        <!-- ZONA 2: LA NUBE -->
        <div class="zone-box">
          <div class="zone-title" style="color: var(--accent-green);">
            ☁️ Zona 2: EN LA NUBE (Internet)
          </div>

          <div class="node-card" onclick="showDetails('github')">
            <div class="node-header">
              <div class="node-icon">🌐</div>
              <div>
                <div class="node-title-text">GitHub Pages</div>
                <div class="node-role">Alojamiento Gratuito</div>
              </div>
            </div>
            <div class="node-desc">Guarda gratis todos los vídeos y PDFs sin gastar un solo mega de tu Google Drive.</div>
          </div>

          <div class="node-card" onclick="showDetails('classroom')">
            <div class="node-header">
              <div class="node-icon">🏫</div>
              <div>
                <div class="node-title-text">Google Classroom</div>
                <div class="node-role">El Aula Virtual</div>
              </div>
            </div>
            <div class="node-desc">Organiza las clases en temas limpios y muestra las tareas en modo borrador.</div>
          </div>
        </div>

        <!-- ZONA 3: DESTINO -->
        <div class="zone-box">
          <div class="zone-title" style="color: var(--accent-orange);">
            👥 Zona 3: LOS ALUMNOS
          </div>

          <div class="node-card" onclick="showDetails('alumnos')">
            <div class="node-header">
              <div class="node-icon">🎓</div>
              <div>
                <div class="node-title-text">Alumnos Sénior</div>
                <div class="node-role">Experiencia Cero Fricción</div>
              </div>
            </div>
            <div class="node-desc">Abren Classroom desde PC o móvil y acceden al material con un solo clic instantáneo.</div>
          </div>
        </div>

      </div>
    </div>

    <!-- PANEL DE DETALLES INTERACTIVO -->
    <div id="detailsPanel" class="details-panel visible">
      <h3 id="panelTitle">🤖 Antigravity: Tu Copiloto Técnico en el PC</h3>
      <p id="panelDesc">Antigravity reside en tu ordenador y asume todas las tareas de programación pesada, maquetación de fichas en PDF con ReportLab, generación de tablas CSV de enlaces y sincronización con GitHub. Tú solo tienes que darle instrucciones en lenguaje cotidiano.</p>
      <div class="pill-list" id="panelPills">
        <span class="pill">Automatización en Python</span>
        <span class="pill">Cero código para el profesor</span>
        <span class="pill">Maquetación profesional</span>
      </div>
    </div>

    <!-- BENEFICIOS -->
    <div class="benefits-grid">
      <div class="benefit-card">
        <div style="font-size: 2rem; margin-bottom: 8px;">💰</div>
        <h4>0 € en Servidores</h4>
        <p>GitHub Pages aloja todo el contenido público del curso (vídeos, simuladores y PDFs) sin cuotas mensuales.</p>
      </div>
      <div class="benefit-card">
        <div style="font-size: 2rem; margin-bottom: 8px;">☁️</div>
        <h4>0 MB en Google Drive</h4>
        <p>Classroom solo enlaza los archivos alojados en GitHub. Tu cuota de Google permanece 100% limpia.</p>
      </div>
      <div class="benefit-card">
        <div style="font-size: 2rem; margin-bottom: 8px;">⚡</div>
        <h4>Publicación en 10 Segundos</h4>
        <p>Gracias a Google Apps Script, 60 lecciones se inyectan en Classroom agrupadas por temas con un solo clic.</p>
      </div>
    </div>

  </main>

  <footer>
    Curso de Inteligencia Artificial para Mayores · Ecosistema Pedagógico de Trabajo en Equipo
  </footer>

  <script>
    const data = {
      profesor: {
        title: "🧑🏻‍🏫 El Profesor (Tú): El Director Pedagógico",
        desc: "Eres el corazón del curso. Conoces a los alumnos, decides la progresión didáctica, grabas los vídeos explicativos y garantizas que la tecnología se explique siempre con cariño, cercanía y sin tecnicismos.",
        pills: ["Visión Didáctica", "Contenidos de Aula", "Empatía Sénior", "Supervisión Ética"]
      },
      antigravity: {
        title: "🤖 Antigravity: Tu Copiloto Técnico en el PC",
        desc: "Es tu taller de desarrollo autónomo. Programa simuladores 3D interactivos, maqueta fichas didácticas oficiales en PDF, genera los índices CSV para Google Classroom y resuelve cualquier traba técnica al instante.",
        pills: ["Automatización Python", "Cero código para el profesor", "Maquetación ReportLab", "Sincronización Git"]
      },
      carpetas: {
        title: "📁 Las 3 Carpetas Maestras en tu Mac",
        desc: "El proyecto se organiza en 3 carpetas modulares: CURSO-ROBOTICA-V2 (8 bloques de robótica), CURSO-IA (60 sesiones prácticas y monográficos) y CURSO-ROBOTICA-IA-COMUN (guías y presentaciones inaugurales compartidas).",
        pills: ["Modularidad", "Sincronización iCloud", "Reutilización de Contenidos"]
      },
      csvs: {
        title: "📄 Paneles CSV y Google Sheets con Apps Script",
        desc: "Los scripts escanean automáticamente tus carpetas y generan archivos CSV con las URLs públicas exactas de GitHub. Al importar el CSV en Google Sheets, un script de Apps Script crea todos los materiales en Classroom en 10 segundos.",
        pills: ["generate_multiple_csvs.py", "Google Apps Script", "Modo Borrador Seguro", "Subida Masiva"]
      },
      github: {
        title: "🌐 GitHub y GitHub Pages: La Gran Nube Gratuita",
        desc: "GitHub aloja todo el material pesado (vídeos MP4, fichas PDF y aplicaciones web interactivas). Gracias a GitHub Pages, cada archivo tiene su propia URL pública permanente sin gastar almacenamiento en tu Google Drive.",
        pills: ["Almacenamiento Ilimitado", "0 € de Coste", "URLs Públicas Rápidas", "Actualización Transparente"]
      },
      classroom: {
        title: "🏫 Google Classroom: El Aula Virtual Ordenada",
        desc: "Es el espacio donde los alumnos acceden al curso. Cada tema agrupa sus materiales didácticos en modo borrador para que el profesor los publique poco a poco a lo largo de las semanas.",
        pills: ["Entorno Seguro", "Organización por Temas", "Fácil Seguimiento"]
      },
      alumnos: {
        title: "🎓 Los Alumnos Sénior: Cero Fricción",
        desc: "El alumno entra en Google Classroom desde su ordenador o teléfono, pulsa sobre la ficha o el vídeo y se reproduce al instante. No necesitan instalar programas raros ni lidiar con contraseñas complejas.",
        pills: ["Acceso con 1 Clic", "Cero Instalaciones", "Legibilidad Óptima", "Sin Estrés"]
      }
    };

    function showDetails(key) {
      document.querySelectorAll('.node-card').forEach(c => c.classList.remove('active'));
      event.currentTarget.classList.add('active');
      
      const item = data[key];
      if (!item) return;
      
      document.getElementById('panelTitle').innerText = item.title;
      document.getElementById('panelDesc').innerText = item.desc;
      
      const pillsContainer = document.getElementById('panelPills');
      pillsContainer.innerHTML = item.pills.map(p => `<span class="pill">${p}</span>`).join('');
    }
  </script>
</body>
</html>
"""
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ Infografía Web Interactiva generada: {html_path}")

# -------------------------------------------------------------------------
# 5. EJECUCIÓN PRINCIPAL
# -------------------------------------------------------------------------
def main():
    print("🚀 Construyendo todos los materiales del Monográfico 7...")
    
    # 1. Archivo de texto para NotebookLM
    txt_path = os.path.join(MONO7_DIR, "0.FUENTE_PARA_NOTEBOOKLM_MAPA_GESTION_PROYECTO_IA.txt")
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(FUENTE_TEXTO)
    print(f"✅ Fuente TXT para NotebookLM: {txt_path}")
    
    # 2. Prompt guía para NotebookLM
    prompt_path = os.path.join(MONO7_DIR, "0.PROMPT_GUIA_ESTILO_NOTEBOOKLM.txt")
    with open(prompt_path, 'w', encoding='utf-8') as f:
        f.write(PROMPT_NOTEBOOKLM_TEXTO)
    print(f"✅ Prompt para NotebookLM: {prompt_path}")
    
    # 3. Documento Word (.docx) para subir a NotebookLM
    create_docx()
    
    # 4. Ficha Didáctica PDF (ReportLab)
    create_pdf()
    
    # 5. App Web Interactiva (HTML5)
    create_interactive_app()
    
    print("\n🎉 ¡Monográfico 7 completado con éxito!")

if __name__ == "__main__":
    main()
