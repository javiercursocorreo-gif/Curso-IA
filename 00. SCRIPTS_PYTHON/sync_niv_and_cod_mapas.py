#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_niv_and_cod_mapas.py
Actualiza automáticamente las tarjetas de [NIV] y [COD] en MAPA_SESION_XX.html
y MAPA_CLASE_SESION_XX.html para todas las sesiones (01 a 20+), insertando
los botones interactivos hacia las Micro-Apps de Seniors (+65) y los Simuladores 3D.
"""

import os
import re
import urllib.parse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
SESSIONS_DIR = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

NIV_CONFIG = {
    1: {
        "file": "SIMULADOR_TRANQUILIDAD_JUBILACION.html",
        "title": "Los 5 Escalones de la Tranquilidad en la Jubilación",
        "btn": "🛡️ Abrir Calculadora Tranquilidad Jubilación (+65) ↗"
    },
    2: {
        "file": "SIMULADOR_RADAR_ESTAFAS_SENIORS.html",
        "title": "Radar de Detección de Fraudes y Estafas para Mayores",
        "btn": "🛡️ Abrir Radar Antifraude para Seniors (+65) ↗"
    },
    3: {
        "file": "SIMULADOR_RADAR_GEOPOLITICA_SENIORS.html",
        "title": "Los 5 Niveles del Poder Geopolítico y la Economía del Hogar",
        "btn": "🌍 Abrir Radar Geopolítica y Cesta de la Compra (+65) ↗"
    },
    4: {
        "file": "SIMULADOR_APORTE_VALOR_EMPRESA_SENIORS.html",
        "title": "Los 6 Niveles de Aporte de Valor y Sabiduría Senior",
        "btn": "💎 Abrir Simulador Sabiduría y Valor Senior (+65) ↗"
    },
    5: {
        "file": "SIMULADOR_EVOLUCION_DINERO_SENIORS.html",
        "title": "Los 5 Niveles de la Evolución del Dinero: Del Trueque a Bizum",
        "btn": "🪙 Abrir Simulador Evolución del Dinero (+65) ↗"
    },
    6: {
        "file": "SIMULADOR_PODER_ADQUISITIVO_COSTE_VIDA_SENIORS.html",
        "title": "Calculadora de Poder Adquisitivo y Cesta de la Compra Real",
        "btn": "🛒 Abrir Calculadora Poder Adquisitivo (+65) ↗"
    },
    7: {
        "file": "SIMULADOR_AUTOMATIZACION_TRABAJO_IA_SENIORS.html",
        "title": "Los 5 Niveles de Automatización e IA en el Hogar de los Mayores",
        "btn": "🤖 Abrir Simulador Asistencia e IA en el Hogar (+65) ↗"
    },
    8: {
        "file": "SIMULADOR_RADAR_PERSUASION_PUBLICIDAD_SENIORS.html",
        "title": "Radar Antimanipulación: Los 6 Niveles de Persuasión y Venta Agresiva",
        "btn": "📢 Abrir Radar Antimanipulación y Ventas (+65) ↗"
    },
    9: {
        "file": "SIMULADOR_SEGURIDAD_PREVENCION_SENIORS.html",
        "title": "Semáforo de Seguridad Ciudadana y Prevención en el Hogar",
        "btn": "🚨 Abrir Semáforo Seguridad Ciudadana (+65) ↗"
    },
    10: {
        "file": "SIMULADOR_SALUD_FINANCIERA_SENIORS.html",
        "title": "Los 6 Niveles de Alfabetización y Blindaje Patrimonial Familiar",
        "btn": "🏦 Abrir Blindaje Patrimonial y Cuentas (+65) ↗"
    },
    11: {
        "file": "SIMULADOR_INTELIGENCIA_COGNITIVA_SENIORS.html",
        "title": "Los 7 Niveles de Inteligencia Cognitiva y Sabiduría en la Madurez",
        "btn": "🧠 Abrir Diagnóstico Reserva Cognitiva (+65) ↗"
    },
    12: {
        "file": "SIMULADOR_CONCIENCIA_ALERTA_NEUROLOGICA_SENIORS.html",
        "title": "Los 6 Niveles de Conciencia, Ritmos Circadianos y Alerta Serena",
        "btn": "☀️ Abrir Simulador Ritmos y Alerta Serena (+65) ↗"
    },
    13: {
        "file": "SIMULADOR_MEMORIA_RETENCION_BIOLOGICA_SENIORS.html",
        "title": "Los 5 Niveles de Memoria Práctica y Retención Cotidiana",
        "btn": "📝 Abrir Simulador Memoria Cotidiana (+65) ↗"
    },
    14: {
        "file": "SIMULADOR_TOMA_DECISIONES_SESGOS_SENIORS.html",
        "title": "Los 6 Niveles de Toma de Decisiones y Filtro de Sesgos Mentales",
        "btn": "⚖️ Abrir Filtro de Sesgos y Decisiones (+65) ↗"
    },
    15: {
        "file": "SIMULADOR_RESILIENCIA_SALUD_MENTAL_SENIORS.html",
        "title": "Los 5 Niveles de Resiliencia Emocional y Fortaleza Interior",
        "btn": "🌱 Abrir Simulador Resiliencia y Paz Interior (+65) ↗"
    },
    16: {
        "file": "SIMULADOR_PREVENCION_ADICCIONES_HABITOS_SENIORS.html",
        "title": "Los 6 Niveles de Prevención de Adicciones, Hábitos y Fármacos",
        "btn": "💊 Abrir Semáforo Seguridad Farmacológica (+65) ↗"
    },
    17: {
        "file": "SIMULADOR_EMPATIA_INTELIGENCIA_EMOCIONAL_SENIORS.html",
        "title": "Los 5 Niveles de Empatía, Vínculo Familiar e Inteligencia Emocional",
        "btn": "🤝 Abrir Simulador Empatía Familiar (+65) ↗"
    },
    18: {
        "file": "SIMULADOR_DISCIPLINA_HABITOS_VIDA_SENIORS.html",
        "title": "Los 6 Niveles de Disciplina Serena y Hábitos de Longevidad Activa",
        "btn": "🚶‍♂️ Abrir Simulador Hábitos y Longevidad (+65) ↗"
    },
    19: {
        "file": "SIMULADOR_COMUNICACION_LENGUAJE_SENIORS.html",
        "title": "Los 5 Niveles de Comunicación y Lenguaje Claro para Mayores",
        "btn": "🗣️ Abrir Guía Comunicación Médica y Bancaria (+65) ↗"
    },
    20: {
        "file": "SIMULADOR_CREATIVIDAD_INNOVACION_SENIORS.html",
        "title": "Los 6 Niveles de Creatividad, Curiosidad e Innovación Vital",
        "btn": "🎨 Abrir Diagnóstico Creatividad y Legado (+65) ↗"
    },
    21: {
        "file": "SIMULADOR_ESCALA_UNIVERSO_SENIORS.html",
        "title": "Los 7 Escalones de la Escala del Universo",
        "btn": "🔭 Abrir Explorador Escala del Universo (+65) ↗"
    },
    22: {
        "file": "SIMULADOR_ENERGIA_KARDASHEV_HOGAR_SENIORS.html",
        "title": "Los 5 Niveles de Energía, Escala Kardashev y Consumo en el Hogar",
        "btn": "⚡ Abrir Optimizador Energía y Kardashev (+65) ↗"
    },
    23: {
        "file": "SIMULADOR_TEMPERATURA_CONFORT_HOGAR_SENIORS.html",
        "title": "Los 7 Niveles de Temperatura en el Cosmos y Confort Térmico en el Hogar",
        "btn": "🌡️ Abrir Termómetro Confort y Salud (+65) ↗"
    },
    24: {
        "file": "SIMULADOR_GRAVEDAD_EQUILIBRIO_SENIORS.html",
        "title": "Los 6 Niveles de Gravedad en el Cosmos, Equilibrio y Prevención de Caídas",
        "btn": "🪐 Abrir Báscula Cósmica y Equilibrio (+65) ↗"
    },
    25: {
        "file": "SIMULADOR_VELOCIDAD_RITMO_VIDA_SENIORS.html",
        "title": "Los 5 Niveles de Velocidad en el Universo y el Elogio de la Lentitud Serena",
        "btn": "🚶‍♂️ Abrir Simulador Velocidad y Calma (+65) ↗"
    },
    26: {
        "file": "SIMULADOR_ESPECTRO_ELECTROMAGNETICO_SALUD_SENIORS.html",
        "title": "Los 6 Niveles del Espectro Electromagnético, Luz, Ondas y Salud",
        "btn": "📻 Abrir Guía Espectro, Ondas y Salud (+65) ↗"
    },
    27: {
        "file": "SIMULADOR_TIEMPO_LEGADO_SENIORS.html",
        "title": "Los 5 Niveles del Tiempo: De los Segundos al Legado Familiar y la Edad Cósmica",
        "btn": "⏳ Abrir Calculadora de Tiempo y Legado (+65) ↗"
    },
    28: {
        "file": "SIMULADOR_PRESION_CLIMA_TENSION_SENIORS.html",
        "title": "Los 6 Niveles de Presión Físico-Química, Clima y Tensión Arterial",
        "btn": "🩺 Abrir Tensiómetro y Presión Barométrica (+65) ↗"
    },
    29: {
        "file": "SIMULADOR_ESTADOS_MATERIA_HIDRATACION_SENIORS.html",
        "title": "Los 5 Estados de la Materia, el Ciclo del Agua y la Hidratación Saludable",
        "btn": "💧 Abrir Planificador de Hidratación y Materia (+65) ↗"
    },
    30: {
        "file": "SIMULADOR_RADIOACTIVIDAD_MEDICINA_SENIORS.html",
        "title": "Los 6 Niveles de Radioactividad, Pruebas Médicas y Tranquilidad Senior",
        "btn": "☢️ Abrir Comparador de Radiación y Medicina (+65) ↗"
    },
    31: {
        "file": "SIMULADOR_PROFUNDIDAD_OCEANO_RESPIRACION_SENIORS.html",
        "title": "Los 6 Estratos del Océano, Respiración Pulmonar y Calma Mental",
        "btn": "🌊 Abrir Respiración y Calma Marina (+65) ↗"
    },
    32: {
        "file": "SIMULADOR_NUTRICION_DIGESTION_SALUDABLE_SENIORS.html",
        "title": "Los 5 Niveles de la Pirámide Nutricional y Digestión Saludable Senior",
        "btn": "🥗 Abrir Guía Nutrición y Digestión (+65) ↗"
    },
    33: {
        "file": "SIMULADOR_VITALIDAD_MUSCULAR_SARCOPENIA_SENIORS.html",
        "title": "Los 6 Niveles de Vitalidad Celular, Mitocondrias y Masa Muscular",
        "btn": "💪 Abrir Test Vitalidad y Fuerza Muscular (+65) ↗"
    },
    34: {
        "file": "SIMULADOR_ZONAS_AZULES_LONGEVIDAD_SENIORS.html",
        "title": "Los 5 Pilares de la Longevidad Activa: El Secreto de las Zonas Azules",
        "btn": "🌱 Abrir Calculadora Zonas Azules y Longevidad (+65) ↗"
    },
    35: {
        "file": "SIMULADOR_BANOS_BOSQUE_NATURALEZA_SENIORS.html",
        "title": "Los 6 Estratos del Bosque, Paseos Verdes y Baños de Bosque (Shinrin-Yoku)",
        "btn": "🌲 Abrir Guía Baños de Bosque y Salud (+65) ↗"
    },
    36: {
        "file": "SIMULADOR_TOXICIDAD_HOGAR_PREVENCION_SENIORS.html",
        "title": "El Radar de Toxicidad en el Hogar: Químicos de Limpieza, Humos y Prevención",
        "btn": "⚠️ Abrir Radar Seguridad Doméstica y Tóxicos (+65) ↗"
    },
    37: {
        "file": "SIMULADOR_TERMORREGULACION_CONFORT_SENIORS.html",
        "title": "Los 6 Niveles de Termorregulación Corporal, Abrigarse Bien y Evitar Caídas por Frío",
        "btn": "🧣 Abrir Guía Termorregulación y Confort (+65) ↗"
    },
    38: {
        "file": "SIMULADOR_ERGONOMIA_COLUMNA_ARTICULACIONES_SENIORS.html",
        "title": "Calculadora de Ergonomía y Esfuerzo Doméstico: Cuidar Espalda y Articulaciones",
        "btn": "🛒 Abrir Calculadora Ergonomía y Columna (+65) ↗"
    },
    39: {
        "file": "SIMULADOR_ILUMINACION_CUIDADO_OCULAR_SENIORS.html",
        "title": "Guía Interactiva de Iluminación Accesible, Contraste y Cuidado Ocular",
        "btn": "💡 Abrir Simulador Iluminación y Cuidado Ocular (+65) ↗"
    },
    40: {
        "file": "SIMULADOR_CUIDADO_PIEL_CICATRIZACION_SENIORS.html",
        "title": "Los 5 Niveles de Regeneración Cutánea, Cuidado de la Piel y Cicatrización",
        "btn": "🧴 Abrir Guía Cuidado de la Piel y Cicatrización (+65) ↗"
    },
    41: {
        "file": "SIMULADOR_CONECTIVIDAD_WIFI_HOGAR_SENIORS.html",
        "title": "Los 6 Niveles de Conectividad Digital, Wi-Fi del Hogar y Videollamadas Familiares",
        "btn": "📶 Abrir Simulador Wi-Fi y Videollamadas (+65) ↗"
    },
    42: {
        "file": "SIMULADOR_CIBERSEGURIDAD_CONTRASENAS_2FA_SENIORS.html",
        "title": "Los 5 Niveles de Blindaje Digital: Contraseñas Fuertes, Verificación en Dos Pasos y Privacidad",
        "btn": "🔐 Abrir Blindaje de Contraseñas y 2FA (+65) ↗"
    },
    43: {
        "file": "SIMULADOR_ACCESIBILIDAD_PANTALLAS_TEXTO_SENIORS.html",
        "title": "Los 6 Niveles de Resolución, Tamaño de Letra y Accesibilidad en Pantallas",
        "btn": "🔍 Abrir Guía Accesibilidad y Pantallas (+65) ↗"
    },
    44: {
        "file": "SIMULADOR_COPIAS_SEGURIDAD_FOTOS_NUBE_SENIORS.html",
        "title": "Los 5 Niveles del Archivo Digital: Copias de Seguridad, Fotos Familiares y la Nube",
        "btn": "☁️ Abrir Copias de Seguridad y Recuerdos (+65) ↗"
    },
    45: {
        "file": "SIMULADOR_BATERIA_CONSUMO_DISPOSITIVOS_SENIORS.html",
        "title": "Los 6 Niveles de Energía en Dispositivos: Cuidado de Baterías, Cargadores y Autonomía",
        "btn": "🔋 Abrir Guía Baterías y Autonomía (+65) ↗"
    },
    46: {
        "file": "SIMULADOR_ROBOTICA_ASISTENTES_HOGAR_SENIORS.html",
        "title": "Los 5 Niveles de la Robótica Doméstica: Robots Aspiradores, Sensores y Asistencia Vital",
        "btn": "🤖 Abrir Robótica y Asistentes del Hogar (+65) ↗"
    },
    47: {
        "file": "SIMULADOR_VIAJES_VIRTUALES_ESTIMULACION_SENIORS.html",
        "title": "Los 6 Niveles de Exploración Virtual, Viajes sin Salir de Casa y Estimulación Sensorial",
        "btn": "🌍 Abrir Viajes Virtuales y Estimulación (+65) ↗"
    },
    48: {
        "file": "SIMULADOR_EFICIENCIA_ELECTRODOMESTICOS_FACTURA_SENIORS.html",
        "title": "Los 5 Niveles de Eficiencia en Electrodomésticos: Ahorro de Luz y Manejo Sencillo",
        "btn": "⚡ Abrir Calculadora Eficiencia Electrodomésticos (+65) ↗"
    },
    49: {
        "file": "SIMULADOR_TRAMITES_DIGITALES_CERTIFICADO_SENIORS.html",
        "title": "Los 6 Niveles de Trámites Digitales: Certificado Digital, Cl@ve y Citas Médicas sin Colas",
        "btn": "🏛️ Abrir Trámites Digitales y Cl@ve Pin (+65) ↗"
    },
    50: {
        "file": "SIMULADOR_COMUNICACION_WHATSAPP_CONVIVENCIA_SENIORS.html",
        "title": "Los 5 Niveles de Comunicación Digital: WhatsApp Familiar, Grupos y Convivencia Serena",
        "btn": "💬 Abrir Guía WhatsApp y Convivencia Serena (+65) ↗"
    }
}

def update_map_html(content, session_num, session_path=None):
    # 1. Actualizar tarjeta NIV si la sesión tiene micro-app configurada
    if session_num in NIV_CONFIG:
        cfg = NIV_CONFIG[session_num]
        sim_file = cfg["file"]
        sim_title = cfg["title"]
        sim_btn = cfg["btn"]
        
        # 1A. Buscar el archivo PDF real en la carpeta de la sesión
        pdf_file = None
        if session_path and os.path.exists(session_path):
            for f in sorted(os.listdir(session_path)):
                if f.startswith(f"9. NIV-{session_num:03d}") and f.endswith(".pdf"):
                    pdf_file = f
                    break
        
        if not pdf_file:
            # Fallback determinista usando la misma regla de export_niv_pdfs.py
            clean_title = re.sub(r'[^A-Za-z0-9_ -]', '', sim_title).strip().replace(' ', '_')
            clean_title = re.sub(r'_+', '_', clean_title)[:40].rstrip('_')
            pdf_file = f"9. NIV-{session_num:03d}_{clean_title}.pdf"
            
        pdf_href = urllib.parse.quote(pdf_file)
        
        # 1B. Si ya es una tarjeta especial, actualizar enlaces hacia el PDF real
        pattern_btn_pdf = re.compile(
            r'<a href="[^"]*NIV[^"]*\.pdf"[^>]*?class="btn-launch-interactive"[^>]*?>\s*'
            r'📄[^<]*?</a>',
            re.IGNORECASE | re.DOTALL
        )
        new_btn_pdf = (
            f'<a href="{pdf_href}" target="_blank" class="btn-launch-interactive" '
            f'style="margin-top:6px; background: rgba(30, 41, 59, 0.85); border-color: rgba(255, 255, 255, 0.15); '
            f'font-weight: 600; font-size: 0.78rem;" title="Abrir Ficha Técnica y Prompts en PDF">\n'
            f'                            📄 Ver Ficha Técnica y Prompts (PDF) ↗\n'
            f'                        </a>'
        )
        content = pattern_btn_pdf.sub(new_btn_pdf, content)

        pattern_special_top = re.compile(
            r'(<div class="file-card file-card-special"[^>]*background:\s*rgba\(16,\s*185,\s*129[^>]*>\s*)'
            r'<a href="[^"]*"\s*target="_blank"\s*class="file-card-special-top"[^>]*?>',
            re.IGNORECASE
        )
        def repl_top(m):
            return m.group(1) + f'<a href="{pdf_href}" target="_blank" class="file-card-special-top" title="Abrir Ficha Técnica Didáctica (PDF)">'
        content = pattern_special_top.sub(repl_top, content)

        # 1C. Si es un enlace simple previo, convertir a tarjeta especial completa
        pattern_simple = re.compile(
            r'<a href="([^"]*NIV[^"]*\.pdf)" target="_blank" class="file-card">\s*'
            r'<div class="file-left">\s*'
            r'<span class="file-num">(#[0-9]+\s*\[NIV\])</span>\s*'
            r'<span class="file-tag tag-pdf">PDF</span>\s*'
            r'<div class="file-details">\s*'
            r'<span class="file-title">[^<]*</span>\s*'
            r'<span class="file-desc">[^<]*</span>\s*'
            r'</div>\s*</div>\s*<span class="file-arrow">↗</span>\s*</a>',
            re.IGNORECASE | re.DOTALL
        )
        
        def repl_simple(m):
            step_num = m.group(2)
            return f"""<div class="file-card file-card-special" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.35);">
                        <a href="{pdf_href}" target="_blank" class="file-card-special-top" title="Abrir Ficha Técnica Didáctica (PDF)">
                            <div class="file-left">
                                <span class="file-num">{step_num}</span>
                                <span class="file-tag" style="background: rgba(16, 185, 129, 0.25); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.5);">MICRO-APP</span>
                                <div class="file-details">
                                    <span class="file-title">{sim_title}</span>
                                    <span class="file-desc">Escalafones y Niveles • Micro-App Interactiva (+65)</span>
                                </div>
                            </div>
                            <span class="file-arrow">↗</span>
                        </a>
                        <a href="{sim_file}" target="_blank" class="btn-launch-interactive" style="background: linear-gradient(135deg, #059669 0%, #10b981 100%); border-color: #34d399; box-shadow: 0 0 14px rgba(16, 185, 129, 0.4);" title="Abrir Micro-App Oficial">
                            {sim_btn}
                        </a>
                        <a href="{pdf_href}" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background: rgba(30, 41, 59, 0.85); border-color: rgba(255, 255, 255, 0.15); font-weight: 600; font-size: 0.78rem;" title="Abrir Ficha Técnica y Prompts en PDF">
                            📄 Ver Ficha Técnica y Prompts (PDF) ↗
                        </a>
                    </div>"""
                    
        content = pattern_simple.sub(repl_simple, content)
        
    return content

def main():
    print("=== Sincronizando Tarjetas Interactivas [NIV] en Mapas de Sesión ===")
    print(f"Ruta SESSIONS_DIR: {SESSIONS_DIR} (Existe: {os.path.exists(SESSIONS_DIR)})")
    count = 0
    for s_num in range(1, 41):
        s_folder = f"{s_num:02d}_Sesion"
        s_path = os.path.join(SESSIONS_DIR, s_folder)
        if not os.path.exists(s_path):
            print(f"  ⚠ Saltando carpeta no encontrada: {s_path}")
            continue
            
        for map_name in [f"MAPA_SESION_{s_num:02d}.html", f"MAPA_CLASE_SESION_{s_num:02d}.html"]:
            map_file = os.path.join(s_path, map_name)
            if os.path.exists(map_file):
                try:
                    with open(map_file, 'r', encoding='utf-8') as f:
                        old_html = f.read()
                    new_html = update_map_html(old_html, s_num, s_path)
                    if new_html != old_html:
                        with open(map_file, 'w', encoding='utf-8') as f:
                            f.write(new_html)
                        count += 1
                        print(f"  ✓ Actualizado: {s_folder}/{map_name}")
                except Exception as ex:
                    print(f"  ⚠ Error procesando {map_file}: {ex}")
                    
    print(f"=== Sincronización finalizada. Archivos modificados: {count} ===")

if __name__ == '__main__':
    main()

