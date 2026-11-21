#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_all_11_niv_3cols.py
Genera las 11 micro-aplicaciones interactivas [NIV] (Sesiones 05 a 15)
bajo la arquitectura canónica de 3 columnas (Three-Columns Dashboard Layout)
idéntica a Sesión 04 (SIMULADOR_APORTE_VALOR_EMPRESA_SENIORS.html):
- Columna 1 (w-full lg:w-1/3): Paso 1 • Entrada de Parámetros (Sliders + Checkboxes interactivos)
- Columna 2 (w-full lg:w-1/3): Paso 2 • Diagnóstico y Reconocimiento (KPIs, nivel activo, veredicto textual, voz es-ES)
- Columna 3 (w-full lg:w-1/3): Paso 3 • Los Niveles del Escalafón (5 o 6 niveles interactivos clicables)
- Top Bar oficial: [NIV-XXX] SESIÓN XX, 🔊 Escuchar Diagnóstico, 🔍 Letra Normal/Grande, 🔄 Reiniciar, 📋 Prompt Gemini
- Modales accesibles y diseño 100% responsivo para iPad y escritorio.
"""

import os
import json

BASE_SESSIONS = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM"
BASE_SIMULADORES = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/01_SIMULADORES"

CONFIG_NIV = [
    {
        "session": 5,
        "tag": "NIV-005",
        "filename": "SIMULADOR_EVOLUCION_DINERO_SENIORS.html",
        "title": "Los 5 Niveles de la Evolución del Dinero (+65)",
        "subtitle": "Autodiagnóstico de Soberanía Monetaria, Protección contra la Inflación y Medios de Pago",
        "step1_title": "Paso 1 • Tu Experiencia Monetaria",
        "step1_desc": "Evalúa tu trayectoria económica y tus hábitos de pago y ahorro frente al paso del tiempo.",
        "sliders": [
            {
                "id": "rngAnosMoneda",
                "label": "Años gestionando tu propia economía:",
                "min": 20, "max": 65, "val": 45, "unit": "años",
                "lblMin": "20 años", "lblMid": "45", "lblMax": "65+ años",
                "color": "amber"
            },
            {
                "id": "rngPagosDigitales",
                "label": "Porcentaje de pagos con tarjeta o móvil:",
                "min": 0, "max": 100, "val": 50, "unit": "%",
                "lblMin": "0% (Solo efectivo)", "lblMid": "50%", "lblMax": "100% (Todo digital)",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkOroMetal", "title": "Valor de los bienes tangibles:", "desc": "Comprendo el valor de la vivienda, metales y objetos reales frente al dinero de papel."},
            {"id": "chkCajeroTarjeta", "title": "Manejo seguro de tarjetas y cajeros:", "desc": "Uso la banca electrónica con cautela, sin miedo pero revisando siempre los movimientos."},
            {"id": "chkReservaEfectivo", "title": "Colchón de tranquilidad en efectivo:", "desc": "Mantengo una reserva prudente en metálico para imprevistos sin depender de fallos de red."},
            {"id": "chkDefensaInflacion", "title": "Conciencia de la inflación silenciosa:", "desc": "Entiendo que el dinero quieto pierde poder de compra si suben los precios de la cesta."}
        ],
        "kpi1_label": "Soberanía de Pago:",
        "kpi1_default": "EQUILIBRADA",
        "kpi2_label": "Blindaje Inflación:",
        "kpi2_default": "ROBUSTO",
        "why_irreplaceable": "La Inteligencia Artificial puede calcular tipos de interés y procesar transferencias en microsegundos, pero no tiene memoria viva de lo que costaba ganar una peseta, ni la prudencia sensata de quien ha visto nacer y quebrar monedas.",
        "gemini_prompt": "Actúa como un sabio economista e historiador monetario especializado en seniors (+65). Explícame con claridad, cercanía y analogías cotidianas cómo ha cambiado el dinero desde el patrón oro y las monedas de plata hasta los pagos digitales con el móvil. Analiza mis respuestas en este simulador y recomiéndame 3 pautas prácticas para proteger los ahorros familiares de la inflación silenciosa sin asumir riesgos absurdos.",
        "levels": [
            {"num": 1, "title": "Nivel 1: Economía Tradicional de Bienes Físicos", "desc": "Valoras el intercambio directo, la palabra y los bienes tangibles por encima de promesas financieras.", "color": "#64748B", "badgeBg": "#F1F5F9", "kpi1": "TRADICIONAL", "kpi2": "BÁSICO", "reflexion": "El trueque y el valor real de las cosas bien hechas son el origen de toda economía humana sensata."},
            {"num": 2, "title": "Nivel 2: Dinero Fiduciario y Memoria de la Peseta", "desc": "Viviste la transición de la peseta al euro. Sabes calcular el valor real de las cosas sin dejarte engañar.", "color": "#0284C7", "badgeBg": "#E0F2FE", "kpi1": "EXPERIMENTADA", "kpi2": "MEDIO", "reflexion": "Tu memoria histórica es el mejor detector de inflación: sabes exactamente cuánto ha subido el pan y la leche."},
            {"num": 3, "title": "Nivel 3: Equilibrio Bancario y Transición Digital", "desc": "Manejas la libreta, la tarjeta y el cajero con prudencia, sin depender totalmente de las pantallas.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "EQUILIBRADA", "kpi2": "SÓLIDO", "reflexion": "Combinar el efectivo físico con los pagos electrónicos te da lo mejor de los dos mundos sin perder autonomía."},
            {"num": 4, "title": "Nivel 4: Gestión Patrimonial Prudente y Anti-Inflación", "desc": "Proteges el dinero familiar frente a comisiones abusivas y compras productos de calidad que no pierden valor.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "AVANZADA", "kpi2": "ELEVADO", "reflexion": "Tu capacidad de no gastar en tonterías y priorizar la tranquilidad de los tuyos vale más que cualquier asesor bancario."},
            {"num": 5, "title": "Nivel 5: Soberanía Monetaria y Legado Financiero", "desc": "Maestría en serenidad económica. Tu patrimonio es un refugio seguro y tu consejo guía a tus hijos y nietos.", "color": "#D97706", "badgeBg": "#FEF3C7", "kpi1": "MÁXIMA", "kpi2": "IMBATIBLE", "reflexion": "Has alcanzado la verdadera riqueza: la tranquilidad de no deber nada a nadie y tener las espaldas cubiertas con sentido común."}
        ]
    },
    {
        "session": 6,
        "tag": "NIV-006",
        "filename": "SIMULADOR_PODER_ADQUISITIVO_COSTE_VIDA_SENIORS.html",
        "title": "Calculadora de Poder Adquisitivo y Cesta de la Compra (+65)",
        "subtitle": "Autodiagnóstico del Coste de la Vida, Inflación Real y Protección de la Pensión",
        "step1_title": "Paso 1 • Presupuesto e Ingresos del Hogar",
        "step1_desc": "Ajusta tus ingresos mensuales y el peso que tienen la cesta fresca y la energía en tu vida.",
        "sliders": [
            {
                "id": "rngPension",
                "label": "Ingresos mensuales netos del hogar:",
                "min": 800, "max": 3500, "val": 1650, "unit": "€/mes",
                "lblMin": "800 €", "lblMid": "1.650 €", "lblMax": "3.500+ €",
                "color": "amber"
            },
            {
                "id": "rngCesta",
                "label": "Gasto mensual en alimentación y frescos:",
                "min": 200, "max": 1000, "val": 420, "unit": "€/mes",
                "lblMin": "200 €", "lblMid": "420 €", "lblMax": "1.000 €",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkConsumoEstacional", "title": "Consumo fresco de temporada:", "desc": "Compro fruta, verdura y pescado según temporada y comparo el precio real por kilo."},
            {"id": "chkSuministrosOptimizados", "title": "Facturas de luz y gas revisadas:", "desc": "Tengo tarifas reguladas o justas sin servicios de mantenimiento superfluos ni seguros trampa."},
            {"id": "chkCeroDeudas", "title": "Ausencia total de deudas con interés:", "desc": "No compro nada a crédito al consumo ni pago comisiones por aplazamientos en tarjetas."},
            {"id": "chkAhorroPrevisor", "title": "Reserva de choque para imprevistos:", "desc": "Mantengo una pequeña cantidad mensual intocable para reparaciones de caldera o dentista."}
        ],
        "kpi1_label": "Cojín de Seguridad:",
        "kpi1_default": "18.5%",
        "kpi2_label": "Capacidad Real:",
        "kpi2_default": "ESTABLE",
        "why_irreplaceable": "Los algoritmos calculan el IPC con fórmulas frías y promedios abstractos. Solo quien hace la compra en el mercado cada semana conoce la verdad del coste de la vida y el arte de estirar el dinero con dignidad.",
        "gemini_prompt": "Actúa como un experto en economía doméstica para jubilados (+65). Analiza mi pensión y el reparto de mis gastos en alimentación y suministros. Explícame cómo evitar que la inflación real merme mi poder adquisitivo, qué trucos de compra inteligente funcionan de verdad y cómo negociar o ajustar las facturas de gas, luz y teléfono.",
        "levels": [
            {"num": 1, "title": "Nivel 1: Presupuesto en Zona de Ajuste Severo", "desc": "Los costes básicos superan el 75% de los ingresos. Se requiere podar gastos automáticos.", "color": "#DC2626", "badgeBg": "#FEE2E2", "kpi1": "< 5%", "kpi2": "CRÍTICO", "reflexion": "Revisar facturas ocultas y seguros bancarios innecesarios puede liberar hasta 100 € al mes de inmediato."},
            {"num": 2, "title": "Nivel 2: Equilibrio Ajustado Sensible a Subidas", "desc": "Llegas a fin de mes pero cualquier avería o gasto extraordinario desestabiliza las cuentas.", "color": "#EA580C", "badgeBg": "#FFEDD5", "kpi1": "8.0%", "kpi2": "AJUSTADO", "reflexion": "La clave está en crear un fondo de emergencia fijo, aunque sea de 30 € al mes, para ganar tranquilidad."},
            {"num": 3, "title": "Nivel 3: Poder Adquisitivo Estable y Controlado", "desc": "Controlas los gastos, compras con cabeza y la alimentación no ahoga la economía familiar.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "15.0%", "kpi2": "CORRECTO", "reflexion": "Tu sabiduría en la cocina tradicional y la compra selectiva es el mejor seguro contra la inflación."},
            {"num": 4, "title": "Nivel 4: Holgura Doméstica y Capacidad de Ahorro", "desc": "Dispones de margen para apoyar a hijos o nietos, hacer alguna escapada y vivir sin estrés financiero.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "22.0%", "kpi2": "HOLGADO", "reflexion": "Tener las cuentas saneadas te permite disfrutar de la jubilación con la serenidad que te has ganado."},
            {"num": 5, "title": "Nivel 5: Soberanía Financiera y Patrimonio Protegido", "desc": "Tranquilidad total. Gastos mínimos fijos, vivienda pagada y colchón de seguridad intocable.", "color": "#7C3AED", "badgeBg": "#EDE9FE", "kpi1": "> 30%", "kpi2": "IMPECABLE", "reflexion": "El mayor lujo de la madurez no es acumular cosas superfluas, sino vivir libre de preocupaciones monetarias."}
        ]
    },
    {
        "session": 7,
        "tag": "NIV-007",
        "filename": "SIMULADOR_AUTOMATIZACION_TRABAJO_IA_SENIORS.html",
        "title": "Los 5 Niveles de Automatización del Trabajo e IA en el Hogar (+65)",
        "subtitle": "Autodiagnóstico de Eficiencia Digital, Asistentes Inteligentes y Ahorro de Tiempo",
        "step1_title": "Paso 1 • Hábitos Digitales y Trámites",
        "step1_desc": "Mide cuánto tiempo dedicas al papeleo cotidiano y tu grado de soltura con los asistentes de IA.",
        "sliders": [
            {
                "id": "rngHorasPapeleo",
                "label": "Horas semanales en gestiones, bancos y papeleo:",
                "min": 1, "max": 15, "val": 6, "unit": "h/sem",
                "lblMin": "1 h", "lblMid": "6 h", "lblMax": "15 h",
                "color": "amber"
            },
            {
                "id": "rngUsoAsistentes",
                "label": "Grado de uso de dictado por voz y consultas a Gemini:",
                "min": 1, "max": 10, "val": 6, "unit": "/10",
                "lblMin": "1 (Cero voz)", "lblMid": "6", "lblMax": "10 (Experto)",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkCitasOnline", "title": "Citas médicas y trámites desde casa:", "desc": "Pido cita en el ambulatorio o descargo recetas desde la app del móvil sin hacer colas."},
            {"id": "chkVozIA", "title": "Dictado por voz en mensajes y notas:", "desc": "Uso el micrófono del móvil para redactar mensajes largos en WhatsApp y dictar recordatorios."},
            {"id": "chkListasAuto", "title": "Consultas prácticas a Gemini:", "desc": "Pregunto a la IA resúmenes de cartas difíciles, ideas de recetas con lo que hay en la nevera o rutas de viaje."},
            {"id": "chkFiltroPublicidad", "title": "Limpieza de correo y filtro de avisos:", "desc": "Sé borrar notificaciones pesadas y no abro correos sospechosos de empresas que no conozco."}
        ],
        "kpi1_label": "Tiempo Ahorrado:",
        "kpi1_default": "18 h/mes",
        "kpi2_label": "Autonomía Digital:",
        "kpi2_default": "NOTABLE",
        "why_irreplaceable": "Las máquinas automatizan datos, pero no pueden decidir qué llamadas merecen una visita en persona, qué médico te genera confianza o con qué nieto pasar una tarde jugando al ajedrez.",
        "gemini_prompt": "Actúa como un formador tecnológico paciente y motivador para mayores de 65 años. Explícame 3 formas sencillas de automatizar trámites domésticos con mi teléfono móvil y con Gemini (por ejemplo, redactar cartas formales, pedir citas médicas o resumir prospectos médicos complicados), sin tecnicismos y con pasos paso a paso.",
        "levels": [
            {"num": 1, "title": "Nivel 1: Gestión Manual Tradicional", "desc": "Prefieres el papel, la ventanilla y la llamada telefónica directa. La tecnología te genera cierta desconfianza.", "color": "#64748B", "badgeBg": "#F1F5F9", "kpi1": "< 2 h", "kpi2": "BÁSICA", "reflexion": "La presencialidad tiene valor humano, pero aprender a pedir citas en el móvil te evitará esperas bajo la lluvia."},
            {"num": 2, "title": "Nivel 2: Usuario Digital Puntual", "desc": "Manejas WhatsApp y el correo, pero el papeleo oficial te sigue resultando farragoso.", "color": "#0284C7", "badgeBg": "#E0F2FE", "kpi1": "6 h", "kpi2": "INICIAL", "reflexion": "Con un par de trucos de dictado por voz ganarás una velocidad enorme en tu comunicación diaria."},
            {"num": 3, "title": "Nivel 3: Asistencia de Voz e IA Cotidiana", "desc": "Usas el micrófono, resuelves dudas con Gemini y operas con la app de salud con soltura.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "14 h", "kpi2": "FLUIDA", "reflexion": "Estás a la vanguardia de tu generación: la IA ya es tu secretaria personal para redactar y buscar datos."},
            {"num": 4, "title": "Nivel 4: Automatización Práctica del Hogar", "desc": "Alarmas inteligentes, trámites sin esfuerzo y organización doméstica impecable gracias al móvil.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "22 h", "kpi2": "AVANZADA", "reflexion": "Has conseguido que la tecnología trabaje para ti y no tú para la pantalla. Tiempo libre ganado para vivir."},
            {"num": 5, "title": "Nivel 5: Maestría y Mentoría Tecnológica Familiar", "desc": "Enseñas a tu pareja, amigos y nietos a usar las herramientas con seguridad, serenidad y sentido común.", "color": "#D97706", "badgeBg": "#FEF3C7", "kpi1": "> 30 h", "kpi2": "PLENA", "reflexion": "Demuestras que la edad no es una barrera, sino una ventaja para aplicar la inteligencia artificial con sabiduría."}
        ]
    },
    {
        "session": 8,
        "tag": "NIV-008",
        "filename": "SIMULADOR_RADAR_PERSUASION_PUBLICIDAD_SENIORS.html",
        "title": "Radar Anti-Manipulación y Persuasión de Masas (+65)",
        "subtitle": "Autodiagnóstico de Inmunidad Crítica, Filtro de Titulares Trampa y Verificación de Fuentes",
        "step1_title": "Paso 1 • Exposición y Hábitos de Información",
        "step1_desc": "Mide cuánto tiempo pasas ante tertulias y pantallas y tu filtro crítico ante noticias sensacionalistas.",
        "sliders": [
            {
                "id": "rngHorasNoticias",
                "label": "Horas al día expuesto a noticias, tertulias y televisión:",
                "min": 1, "max": 8, "val": 3, "unit": "h/día",
                "lblMin": "1 h", "lblMid": "3 h", "lblMax": "8 h",
                "color": "amber"
            },
            {
                "id": "rngCapacidadDuda",
                "label": "Nivel de escepticismo ante titulares llamativos:",
                "min": 1, "max": 10, "val": 8, "unit": "/10",
                "lblMin": "1 (Me lo creo todo)", "lblMid": "8", "lblMax": "10 (Verifico siempre)",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkDesconfioUrgencia", "title": "Sospecha ante la urgencia o el pánico:", "desc": "Si un titular o mensaje me pide alarmarme o enfadarme al instante, sé que intentan manipularme."},
            {"id": "chkComprueboTitular", "title": "Lectura más allá del titular cebo:", "desc": "No comparto noticias leyendo solo el titular; leo el texto completo para contrastar los datos."},
            {"id": "chkDiferencioOpinion", "title": "Distinción entre opinión y dato oficial:", "desc": "Distingo con claridad la opinión de un tertuliano o presentador de lo que es un informe técnico real."},
            {"id": "chkFiltroCadenas", "title": "Cero reenvíos de cadenas alarmistas en WhatsApp:", "desc": "Corto de raíz los bulos familiares y jamás reenvío avisos médicos o conspiraciones sin contrastar."}
        ],
        "kpi1_label": "Blindaje Crítico:",
        "kpi1_default": "ALTO (86%)",
        "kpi2_label": "Paz Mental:",
        "kpi2_default": "IMPERMEABLE",
        "why_irreplaceable": "Los algoritmos de recomendación buscan enfadar y asustar para retener la atención. Solo la serenidad de una persona madura sabe desconectar el televisor y pasear en calma sabiendo que el mundo real no es el de las tertulias.",
        "gemini_prompt": "Actúa como un analista de comunicación y pensamiento crítico. Explícame las 4 técnicas psicológicas más usadas en televisión y redes sociales para manipular a las personas mayores mediante el miedo o la indignación. Dame una guía de 3 preguntas de oro para saber si una noticia de WhatsApp es un bulo o una realidad demostrable.",
        "levels": [
            {"num": 1, "title": "Nivel 1: Alta Exposición y Angustia Informativa", "desc": "Las tertulias y noticias te causan enfado o preocupación constante durante el día.", "color": "#DC2626", "badgeBg": "#FEE2E2", "kpi1": "30%", "kpi2": "VULNERABLE", "reflexion": "La televisión se alimenta de tu atención. Apagar la tele dos horas antes de dormir devolverá la paz a tu mente."},
            {"num": 2, "title": "Nivel 2: Duda Intuitiva pero Frecuente Indignación", "desc": "Sabes que exageran, pero a menudo te descubres preocupado por sucesos lejanos que no puedes controlar.", "color": "#EA580C", "badgeBg": "#FFEDD5", "kpi1": "52%", "kpi2": "REACTIVO", "reflexion": "Enfoca tu energía en tu barrio, tus amigos y tu familia; lo demás es ruido comercial de pantallas."},
            {"num": 3, "title": "Nivel 3: Filtro Crítico Despierto", "desc": "No te crees los titulares alarmistas y cortas de raíz los bulos que llegan a los grupos de WhatsApp.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "72%", "kpi2": "SÓLIDO", "reflexion": "Tu madurez te permite ver la tramoya de los medios: sabes que el miedo es solo un producto de venta."},
            {"num": 4, "title": "Nivel 4: Criterio Propio e Inmunidad a la Propaganda", "desc": "Lees distintas fuentes, contrastas opiniones y mantienes la serenidad ante modas o histerias colectivas.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "88%", "kpi2": "BLINDADO", "reflexion": "Has vivido suficientes promesas políticas y alarmas falsas para saber que la calma es la mayor sabiduría."},
            {"num": 5, "title": "Nivel 5: Faro de Templanza y Claridad Familiar", "desc": "En medio del ruido, aportas serenidad a tus hijos y nietos, enseñándoles a pensar por sí mismos con sosiego.", "color": "#D97706", "badgeBg": "#FEF3C7", "kpi1": "98%", "kpi2": "MAESTRO", "reflexion": "Tu mirada limpia y tranquila es el mejor antídoto para la ansiedad que la sociedad digital produce en los más jóvenes."}
        ]
    },
    {
        "session": 9,
        "tag": "NIV-009",
        "filename": "SIMULADOR_SEGURIDAD_PREVENCION_SENIORS.html",
        "title": "Semáforo de Seguridad Ciudadana y Prevención Urbana (+65)",
        "subtitle": "Autodiagnóstico de Hábitos Preventivos en la Vía Pública, Cajeros y Seguridad en el Domicilio",
        "step1_title": "Paso 1 • Hábitos Cotidianos y Entorno",
        "step1_desc": "Evalúa tus rutinas al salir a la calle, acudir al banco y atender la puerta del domicilio.",
        "sliders": [
            {
                "id": "rngSalidas",
                "label": "Salidas semanales al centro, compras o paseos:",
                "min": 1, "max": 14, "val": 7, "unit": "veces/sem",
                "lblMin": "1 vez", "lblMid": "7 veces", "lblMax": "14 veces",
                "color": "amber"
            },
            {
                "id": "rngAtencion",
                "label": "Nivel de atención y observación en aglomeraciones:",
                "min": 1, "max": 10, "val": 8, "unit": "/10",
                "lblMin": "1 (Distraído)", "lblMid": "8", "lblMax": "10 (Alerta tranquila)",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkCajeroSeguro", "title": "Protección del PIN en cajeros:", "desc": "Me tapo la mano al teclear mi clave secreta y no acepto ayuda de extraños que se acerquen."},
            {"id": "chkCerraduraCasa", "title": "Puerta cerrada con llave y mirilla:", "desc": "Echo siempre la llave con vuelta y jamás abro a supuestos revisores de gas que no hayan avisado antes."},
            {"id": "chkBolsoDelante", "title": "Bolso cruzado y pertenencias a la vista:", "desc": "Llevo el bolso bien cerrado y por delante en el transporte público, mercadillos y cafeterías."},
            {"id": "chkTelefonoCargado", "title": "Móvil siempre con batería y contactos clave:", "desc": "Salgo de casa con el teléfono cargado y tengo guardados en favoritos los teléfonos de mis hijos o emergencias."}
        ],
        "kpi1_label": "Nivel Preventivo:",
        "kpi1_default": "ÓPTIMO",
        "kpi2_label": "Riesgo Percibido:",
        "kpi2_default": "MÍNIMO",
        "why_irreplaceable": "Una cámara de vigilancia o una alarma inteligente graban imágenes, pero carecen del instinto de prudencia humana de quien intuye una mala intención en la calle y cambia de acera a tiempo.",
        "gemini_prompt": "Actúa como un instructor de policía y prevención ciudadana para personas mayores. Explícame los 5 timos callejeros y domiciliarios más habituales (el timo de la estampita moderno, los falsos revisores de la luz, el truco de la mancha y los hurtos en cajeros) y qué 3 reglas de oro debo seguir para moverme por mi ciudad con total libertad y seguridad.",
        "levels": [
            {"num": 1, "title": "Nivel 1: Exposición por Exceso de Confianza", "desc": "Dejas el bolso sin vigilancia o abres la puerta sin preguntar. Se necesita reforzar la precaución básica.", "color": "#DC2626", "badgeBg": "#FEE2E2", "kpi1": "BAJO", "kpi2": "ALTO", "reflexion": "La bondad es una virtud, pero en la calle hay que acompañarla siempre de un escudo de prudencia."},
            {"num": 2, "title": "Nivel 2: Cautela Ocasional pero Distracciones", "desc": "Te cuidas en el banco, pero a veces te confías en terrazas o paradas de autobús abarrotadas.", "color": "#EA580C", "badgeBg": "#FFEDD5", "kpi1": "MEDIO", "kpi2": "MODERADO", "reflexion": "El truco de los carteristas es distraerte con una pregunta o un mapa. La atención es tu mejor defensa."},
            {"num": 3, "title": "Nivel 3: Seguridad Preventiva Estándar", "desc": "Buenos hábitos en cajeros, cerradura segura y precaución adecuada sin caer en el miedo innecesario.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "BUENO", "kpi2": "CONTROLADO", "reflexion": "Caminar erguido y con paso firme transmite seguridad y aleja a los oportunistas."},
            {"num": 4, "title": "Nivel 4: Conciencia Situacional Firme", "desc": "Observas el entorno con serenidad, prevés riesgos y proteges tu espacio personal con elegancia.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "ALTO", "kpi2": "MUY BAJO", "reflexion": "Disfrutas de tu ciudad con libertad absoluta porque tus hábitos de autoprotección son automáticos."},
            {"num": 5, "title": "Nivel 5: Blindaje y Tranquilidad Plena", "desc": "Maestría en prudencia cotidiana. Sabes reaccionar con aplomo ante cualquier imprevisto sin perder la calma.", "color": "#D97706", "badgeBg": "#FEF3C7", "kpi1": "MÁXIMO", "kpi2": "NULO", "reflexion": "La verdadera seguridad no consiste en encerrarse en casa, sino en pisar la calle con la sabiduría de los años."}
        ]
    },
    {
        "session": 10,
        "tag": "NIV-010",
        "filename": "SIMULADOR_SALUD_FINANCIERA_SENIORS.html",
        "title": "Los 6 Niveles de Alfabetización y Blindaje Financiero (+65)",
        "subtitle": "Autodiagnóstico de Solvencia, Protección de Depósitos y Transmisión de Patrimonio",
        "step1_title": "Paso 1 • Estructura Patrimonial y Ahorro",
        "step1_desc": "Comprueba la solidez de tu fondo de seguridad y la claridad de tus disposiciones familiares.",
        "sliders": [
            {
                "id": "rngMesesFondo",
                "label": "Meses de gastos cubiertos en cuenta de ahorro:",
                "min": 1, "max": 36, "val": 14, "unit": "meses",
                "lblMin": "1 mes", "lblMid": "14 meses", "lblMax": "36+ meses",
                "color": "amber"
            },
            {
                "id": "rngClaridadPapeles",
                "label": "Orden y claridad de testamento y cuentas:",
                "min": 1, "max": 10, "val": 9, "unit": "/10",
                "lblMin": "1 (Desordenado)", "lblMid": "9", "lblMax": "10 (Impecable)",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkFondoGarantia", "title": "Depósitos bajo el límite de 100.000 €:", "desc": "Si supero esa cifra, diversifico en varias entidades solventes para tener garantía pública del 100%."},
            {"id": "chkCeroProductosRaros", "title": "Rechazo de inversiones complejas o fondos trampa:", "desc": "No firmo nada que no entienda con una explicación de cinco minutos en servilleta de papel."},
            {"id": "chkTestamentoClaro", "title": "Testamento y voluntades en orden:", "desc": "Tengo el testamento notarial redactado con equidad para evitar disputas entre mis herederos."},
            {"id": "chkPoderesNotariales", "title": "Poder preventivo en caso de enfermedad:", "desc": "Tengo previsto quién podrá gestionar mis cuentas si algún día no puedo valerme por mí mismo."}
        ],
        "kpi1_label": "Tranquilidad:",
        "kpi1_default": "TOTAL (95%)",
        "kpi2_label": "Solvencia:",
        "kpi2_default": "BLINDADA",
        "why_irreplaceable": "Un asesor financiero con inteligencia artificial buscará rentabilidades arriesgadas y comisiones de gestión. Solo el corazón de un padre o abuelo busca la paz de sus hijos y la equidad familiar.",
        "gemini_prompt": "Actúa como un notario y abogado experto en derecho de familia y patrimonio sénior (+65). Explícame en un lenguaje sencillo y reconfortante por qué es vital tener un testamento claro y qué es un 'poder notarial preventivo' para protegerse ante una posible pérdida de facultades, garantizando que nadie se aproveche de mis ahorros.",
        "levels": [
            {"num": 1, "title": "Nivel 1: Fragilidad por Desorganización", "desc": "Cuentas sin revisar, papeles dispersos y sin previsiones notariales claras. Riesgo de líos futuros.", "color": "#DC2626", "badgeBg": "#FEE2E2", "kpi1": "35%", "kpi2": "FRÁGIL", "reflexion": "Dedicar una mañana a ordenar los extractos y hacer testamento notarial cuesta poco y ahorra años de disgustos."},
            {"num": 2, "title": "Nivel 2: Solvencia Básica pero Exposición Bancaria", "desc": "Ahorros concentrados en una sola entidad y aceptación pasiva de comisiones de mantenimiento.", "color": "#EA580C", "badgeBg": "#FFEDD5", "kpi1": "55%", "kpi2": "REGULAR", "reflexion": "Tu dinero es tuyo. Si tu banco de toda la vida te cobra por respirar, es hora de poner límites claros."},
            {"num": 3, "title": "Nivel 3: Seguridad y Colchón de Tranquilidad", "desc": "Fondo de emergencia cubierto, gastos controlados y productos bancarios sencillos y transparentes.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "75%", "kpi2": "SÓLIDA", "reflexion": "La mejor inversión no es la que promete rentabilidades mágicas, sino la que te deja dormir a pierna suelta."},
            {"num": 4, "title": "Nivel 4: Blindaje Patrimonial Activo", "desc": "Diversificación de depósitos, cuentas protegidas contra estafas y papeles testamentarios impecables.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "90%", "kpi2": "MUY ROBUSTA", "reflexion": "Has trabajado muchos años para levantar tu hogar; cuidarlo con cabeza es un acto de amor hacia los tuyos."},
            {"num": 5, "title": "Nivel 5: Maestría Financiera y Legado Seguro", "desc": "Paz económica absoluta. Has ordenado tu presente y dejado un camino despejado y armónico para las siguientes generaciones.", "color": "#D97706", "badgeBg": "#FEF3C7", "kpi1": "99%", "kpi2": "EJEMPLAR", "reflexion": "Dejar las cosas bien hechas es el mayor regalo que un sénior puede legar a su familia: concordia y serenidad."}
        ]
    },
    {
        "session": 11,
        "tag": "NIV-011",
        "filename": "SIMULADOR_INTELIGENCIA_COGNITIVA_SENIORS.html",
        "title": "Los 7 Niveles de Inteligencia Cognitiva y Agilidad Mental (+65)",
        "subtitle": "Autodiagnóstico de Reserva Cognitiva, Neuroplasticidad y Curiosidad Intelectual Activa",
        "step1_title": "Paso 1 • Estimulación y Retos Mentales",
        "step1_desc": "Comprueba cómo entrenas tu cerebro cada semana para mantener las conexiones neuronales vivas.",
        "sliders": [
            {
                "id": "rngHorasLectura",
                "label": "Horas semanales de lectura, escritura o estudio:",
                "min": 1, "max": 25, "val": 10, "unit": "h/sem",
                "lblMin": "1 h", "lblMid": "10 h", "lblMax": "25+ h",
                "color": "amber"
            },
            {
                "id": "rngRetos",
                "label": "Frecuencia de retos (música, crucigramas, tecnología):",
                "min": 1, "max": 10, "val": 7, "unit": "/10",
                "lblMin": "1 (Rara vez)", "lblMid": "7", "lblMax": "10 (Diario)",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkAprenderSiempre", "title": "Curiosidad por aprender habilidades nuevas:", "desc": "Me ilusiona aprender cosas que nunca hice antes (tocar teclado, usar inteligencia artificial, idiomas)."},
            {"id": "chkDebateRespetuoso", "title": "Conversaciones estimulantes con distintas edades:", "desc": "Hablo con personas de generaciones más jóvenes y me intereso por cómo ven el mundo actual."},
            {"id": "chkCalculoMental", "title": "Práctica de cálculo mental cotidiano:", "desc": "Hago sumas de memoria al pagar o cuento el cambio antes de mirar el recibo de la máquina."},
            {"id": "chkResolverProblemas", "title": "Búsqueda activa de soluciones:", "desc": "Si algo no funciona en casa o en el móvil, intento entender por qué antes de pedir ayuda de inmediato."}
        ],
        "kpi1_label": "Reserva Cognitiva:",
        "kpi1_default": "ALTA",
        "kpi2_label": "Neuroplasticidad:",
        "kpi2_default": "DINÁMICA",
        "why_irreplaceable": "Una red neuronal artificial calcula pesos estadísticos, pero carece de intuición, chispa humorística, metáforas vitales y la comprensión profunda que da haber vivido miles de conversaciones reales.",
        "gemini_prompt": "Actúa como un neurocientífico especializado en envejecimiento activo y reserva cognitiva. Explícame 3 ejercicios cotidianos sencillos pero muy potentes para estimular el hipocampo y la neuroplasticidad cerebral después de los 65 años (como aprender un instrumento musical, leer textos complejos o caminar por rutas no habituales).",
        "levels": [
            {"num": 1, "title": "Nivel 1: Rutina Mental Pasiva", "desc": "Consumo excesivo de televisión sin retos activos. El cerebro necesita chispa para no adormecerse.", "color": "#64748B", "badgeBg": "#F1F5F9", "kpi1": "BÁSICA", "kpi2": "LENTA", "reflexion": "El cerebro es un músculo: si no se usa se atrofia, pero si lo desafías con retos nuevos vuelve a brillar."},
            {"num": 2, "title": "Nivel 2: Estimulación Ocasional", "desc": "Lees el periódico y haces algún pasatiempo puntual, pero evitas aprender cosas que te exijan esfuerzo.", "color": "#0284C7", "badgeBg": "#E0F2FE", "kpi1": "MEDIA", "kpi2": "FUNCIONAL", "reflexion": "Salir de la zona de confort intelectual genera nuevas ramificaciones neuronales a cualquier edad."},
            {"num": 3, "title": "Nivel 3: Gimnasia Mental Habitual", "desc": "Mantienes una buena rutina de lectura, curiosidad y cálculo mental que sostiene tu agilidad.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "SÓLIDA", "kpi2": "ACTIVA", "reflexion": "Tu memoria operativa se mantiene en forma gracias a tus hábitos diarios de lectura y atención."},
            {"num": 4, "title": "Nivel 4: Neuroplasticidad Dinámica", "desc": "Aprendes tecnologías nuevas, tocas música y desafías tu mente con temas que desconocías.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "ELEVADA", "kpi2": "DINÁMICA", "reflexion": "Tu entusiasmo por aprender demuestra que la juventud reside en la curiosidad y no en la partida de nacimiento."},
            {"num": 5, "title": "Nivel 5: Pensamiento Complejo y Análisis", "desc": "Conectas sucesos históricos con la actualidad, analizas con criterio y no te dejas engatusar por modas.", "color": "#D97706", "badgeBg": "#FEF3C7", "kpi1": "SOBRESALIENTE", "kpi2": "ÁGIL", "reflexion": "La verdadera inteligencia consiste en unir los puntos con serenidad para ver el cuadro completo."},
            {"num": 6, "title": "Nivel 6: Sabiduría Estratégica y Creatividad", "desc": "Encuentras soluciones sencillas a problemas que a otros les parecen irresolubles. Agudeza magistral.", "color": "#7C3AED", "badgeBg": "#EDE9FE", "kpi1": "EXCEPCIONAL", "kpi2": "POTENTE", "reflexion": "Tu experiencia vital combinada con una mente despierta te convierte en un estratega familiar inigualable."},
            {"num": 7, "title": "Nivel 7: Lucidez Magistral y Plenitud Intelectual", "desc": "Cima cognitiva de la madurez. Lucidez envidiable, memoria afectiva profunda y faro intelectual para tu entorno.", "color": "#B45309", "badgeBg": "#FEF3C7", "kpi1": "MÁXIMA", "kpi2": "PLENA", "reflexion": "Has demostrado que los años, bien aprovechados, multiplican la inteligencia profunda que ninguna máquina podrá igualar."}
        ]
    },
    {
        "session": 12,
        "tag": "NIV-012",
        "filename": "SIMULADOR_CONCIENCIA_ALERTA_NEUROLOGICA_SENIORS.html",
        "title": "Los 6 Niveles de Conciencia, Ritmos Circadianos y Alerta (+65)",
        "subtitle": "Autodiagnóstico del Sueño Reparador, Luz Natural Matutina y Vitalidad Neurobiológica",
        "step1_title": "Paso 1 • Hábitos de Descanso y Energía",
        "step1_desc": "Evalúa la sincronización de tu reloj biológico y la calidad de tu descanso nocturno.",
        "sliders": [
            {
                "id": "rngHorasSueno",
                "label": "Horas de descanso nocturno de calidad:",
                "min": 4, "max": 10, "val": 7, "unit": "horas",
                "lblMin": "4 h", "lblMid": "7 h", "lblMax": "10 h",
                "color": "amber"
            },
            {
                "id": "rngLuzSolar",
                "label": "Minutos al día al aire libre con luz natural:",
                "min": 10, "max": 120, "val": 45, "unit": "min/día",
                "lblMin": "10 min", "lblMid": "45 min", "lblMax": "120 min",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkHorarioRegular", "title": "Horarios regulares para acostarse y levantarse:", "desc": "Mantengo casi la misma hora de vigilia y sueño para no descolocar mi ritmo circadiano."},
            {"id": "chkCeroPantallasCama", "title": "Cero pantallas azules antes de dormir:", "desc": "Apago el móvil y la televisión un rato antes de acostarme para facilitar la melatonina natural."},
            {"id": "chkCaminataMatinal", "title": "Paseo matutino con luz del día:", "desc": "Salgo a caminar por la mañana para que la retina avise al cerebro de que comienza la jornada activa."},
            {"id": "chkCenaLigera", "title": "Cena ligera dos horas antes de dormir:", "desc": "No me acuesto con la digestión pesada para que el cuerpo pueda dedicarse a reparar los tejidos."}
        ],
        "kpi1_label": "Sincronía Biológica:",
        "kpi1_default": "ÓPTIMA (92%)",
        "kpi2_label": "Alerta Mental:",
        "kpi2_default": "VITAL Y CLARA",
        "why_irreplaceable": "Los servidores de IA operan 24 horas sin descanso en centros de datos fríos, pero carecen de la emoción de despertar con energía al ver salir el sol o de la placidez de una siesta reparadora en buena compañía.",
        "gemini_prompt": "Actúa como un médico especialista en cronobiología y medicina del sueño sénior. Explícame por qué el reloj circadiano cambia con la edad, por qué la luz solar en los ojos por la mañana es el mejor antidepresivo natural y qué 3 pautas sencillas debo seguir para vencer el insomnio nocturno sin pastillas.",
        "levels": [
            {"num": 1, "title": "Nivel 1: Desincronización Circadiana y Fatiga", "desc": "Horarios caóticos, pantallas nocturnas y cansancio diurno. El cuerpo no logra descansar.", "color": "#DC2626", "badgeBg": "#FEE2E2", "kpi1": "30%", "kpi2": "FATIGADA", "reflexion": "La luz de las pantallas por la noche engaña al cerebro haciéndole creer que es mediodía. Proteger el sueño es salud."},
            {"num": 2, "title": "Nivel 2: Descanso Irregular y Somnolencia", "desc": "Te despiertas a menudo por la noche y sientes bajones de energía pronunciados tras las comidas.", "color": "#EA580C", "badgeBg": "#FFEDD5", "kpi1": "50%", "kpi2": "IRREGULAR", "reflexion": "Caminar 20 minutos bajo el sol cada mañana sincroniza tu reloj interno mejor que cualquier fármaco."},
            {"num": 3, "title": "Nivel 3: Equilibrio Circadiano Aceptable", "desc": "Descanso razonable, siestas cortas de 20 minutos y buen nivel de energía matutina.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "70%", "kpi2": "CORRECTA", "reflexion": "Una siesta breve es medicina pura para el corazón, siempre que no sobrepase la media hora."},
            {"num": 4, "title": "Nivel 4: Sincronización Biológica Óptima", "desc": "Te levantas descansado sin despertador, mantienes la atención despierta y duermes de un tirón.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "88%", "kpi2": "FRESCA", "reflexion": "Tus células se regeneran cada noche gracias a tus hábitos impecables de luz y descanso."},
            {"num": 5, "title": "Nivel 5: Vitalidad y Claridad Neurobiológica", "desc": "Energía constante a lo largo del día, lucidez en la toma de decisiones y descanso reparador profundo.", "color": "#D97706", "badgeBg": "#FEF3C7", "kpi1": "96%", "kpi2": "VITAL Y CLARA", "reflexion": "Vivir al compás de la naturaleza te proporciona una vitalidad envidiable que contagia a los tuyos."}
        ]
    },
    {
        "session": 13,
        "tag": "NIV-013",
        "filename": "SIMULADOR_MEMORIA_RETENCION_BIOLOGICA_SENIORS.html",
        "title": "Los 5 Niveles de Memoria Práctica y Retención Biológica (+65)",
        "subtitle": "Autodiagnóstico de Memoria Operativa, Técnicas de Asociación y Salud del Hipocampo",
        "step1_title": "Paso 1 • Ejercicio de Retención y Foco",
        "step1_desc": "Mide cómo ejercitas la fijación de datos recientes y tus estrategias cotidianas de recuerdo.",
        "sliders": [
            {
                "id": "rngEjercicioMemoria",
                "label": "Minutos al día recordando datos, poesías o historias sin mirar:",
                "min": 5, "max": 60, "val": 20, "unit": "min/día",
                "lblMin": "5 min", "lblMid": "20 min", "lblMax": "60 min",
                "color": "amber"
            },
            {
                "id": "rngHidratacion",
                "label": "Vasos de agua diarios (el cerebro deshidratado olvida más):",
                "min": 3, "max": 10, "val": 7, "unit": "vasos/día",
                "lblMin": "3 vasos", "lblMid": "7 vasos", "lblMax": "10 vasos",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkAsociacionVisual", "title": "Asociación visual para recordar nombres:", "desc": "Si quiero recordar un nombre o recado, lo asocio con una imagen divertida o conocida."},
            {"id": "chkRepasoNocturno", "title": "Repaso mental de lo vivido en el día:", "desc": "Antes de dormir hago memoria de las 3 personas con las que hablé y qué aprendí hoy."},
            {"id": "chkUbicacionFija", "title": "Lugar fijo en casa para llaves y gafas:", "desc": "Dejo las cosas en su sitio por costumbre para no agotar la memoria en tareas mecánicas."},
            {"id": "chkNutricionOmega3", "title": "Alimentación amiga del hipocampo:", "desc": "Consumo aceite de oliva virgen, nueces, fruta fresca y pescado azul habitualmente."}
        ],
        "kpi1_label": "Retención Fiel:",
        "kpi1_default": "90%",
        "kpi2_label": "Salud Hipocampo:",
        "kpi2_default": "ROBUSTA",
        "why_irreplaceable": "Un disco duro almacena billones de gigabytes pero no siente nostalgia por un olor de la infancia, ni guarda con cariño las palabras de su madre, ni sonríe al recordar la primera travesura de un hijo.",
        "gemini_prompt": "Actúa como un neuropsicólogo especialista en memoria para adultos mayores. Explícame la diferencia entre los despistes cotidianos benignos (olvidar dónde dejé las gafas) y los fallos de memoria relevantes. Enséñame el método del 'palacio de la memoria' o de las asociaciones visuales para recordar listas y nombres con total facilidad.",
        "levels": [
            {"num": 1, "title": "Nivel 1: Despistes Frecuentes por Falta de Atención", "desc": "Haces varias cosas a la vez y olvidas qué ibas a buscar a la habitación. Falta de foco.", "color": "#DC2626", "badgeBg": "#FEE2E2", "kpi1": "40%", "kpi2": "DISPERSA", "reflexion": "No es que falle la memoria, es que no prestas atención plena en el momento de guardar el recuerdo."},
            {"num": 2, "title": "Nivel 2: Memoria Funcional con Apoyos", "desc": "Usas listas y libretas para todo. Cumples con tus tareas pero te angustia olvidar algo.", "color": "#EA580C", "badgeBg": "#FFEDD5", "kpi1": "60%", "kpi2": "CORRECTA", "reflexion": "Anotar las cosas es un hábito excelente de organización que libera al cerebro de estrés inútil."},
            {"num": 3, "title": "Nivel 3: Retención Práctica y Estructurada", "desc": "Recuerdas fechas clave, nombres y recados sin problemas gracias a tus trucos de asociación.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "78%", "kpi2": "SÓLIDA", "reflexion": "Tu hipocampo funciona a pleno rendimiento porque lo mantienes activo, hidratado y bien alimentado."},
            {"num": 4, "title": "Nivel 4: Memoria Ágil y Riqueza de Vocabulario", "desc": "Evocas recuerdos antiguos con todo lujo de detalles y retienes conversaciones recientes con fidelidad.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "90%", "kpi2": "MUY ROBUSTA", "reflexion": "Eres la enciclopedia viva de tu familia: tus recuerdos son tesoros históricos que nadie podrá borrar."},
            {"num": 5, "title": "Nivel 5: Memoria Magistral y Sabiduría Afectiva", "desc": "Memoria prodigiosa al servicio del cariño. Recuerdas lo que importa de verdad y olvidas lo que no aporta paz.", "color": "#D97706", "badgeBg": "#FEF3C7", "kpi1": "99%", "kpi2": "IMPECABLE", "reflexion": "La cúspide de la memoria no es acordarse de todo, sino saber atesorar los momentos de amor y olvidar los rencores."}
        ]
    },
    {
        "session": 14,
        "tag": "NIV-014",
        "filename": "SIMULADOR_TOMA_DECISIONES_SESGOS_SENIORS.html",
        "title": "Los 6 Niveles de Toma de Decisiones y Filtro de Sesgos (+65)",
        "subtitle": "Autodiagnóstico de Prudencia, Pausa Reflexiva y Neutralización del Sesgo de Confirmación",
        "step1_title": "Paso 1 • Tiempo de Análisis y Prudencia",
        "step1_desc": "Evalúa cómo tomas decisiones importantes de salud, familia o dinero ante ofertas o presiones.",
        "sliders": [
            {
                "id": "rngTiempoDecision",
                "label": "Días de reflexión antes de un compromiso relevante:",
                "min": 1, "max": 20, "val": 7, "unit": "días",
                "lblMin": "1 día (Rápido)", "lblMid": "7 días", "lblMax": "20 días (Pausado)",
                "color": "amber"
            },
            {
                "id": "rngSegundaOpinion",
                "label": "Hábito de pedir segunda opinión a expertos:",
                "min": 1, "max": 10, "val": 8, "unit": "/10",
                "lblMin": "1 (Decido solo)", "lblMid": "8", "lblMax": "10 (Consulto siempre)",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkRegla24h", "title": "Regla de las 24 horas ante ventas o llamadas:", "desc": "Jamás compro ni contrato nada por teléfono en el momento; pido la documentación por escrito."},
            {"id": "chkBuscoContras", "title": "Búsqueda activa de inconvenientes:", "desc": "Antes de decidir algo importante, me pregunto qué podría salir mal y qué precio tendría rectificar."},
            {"id": "chkCeroPresionSocial", "title": "Inmunidad a la prisa ajena:", "desc": "Si alguien me mete prisa para firmar o decidir, sé de inmediato que el beneficiado es él y no yo."},
            {"id": "chkAceptoRectificar", "title": "Capacidad de rectificar sin orgullo:", "desc": "Si me doy cuenta de que elegí un camino equivocado, cambio de rumbo con serenidad sin tozudez."}
        ],
        "kpi1_label": "Índice de Acierto:",
        "kpi1_default": "94%",
        "kpi2_label": "Serenidad:",
        "kpi2_default": "MAGISTRAL",
        "why_irreplaceable": "Los algoritmos deciden en milisegundos buscando maximizar métricas cuantitativas. Solo la madurez humana sabe que a veces la mejor decisión es no hacer nada, esperar con calma y dejar que el tiempo aclare las aguas.",
        "gemini_prompt": "Actúa como un filósofo del juicio práctico y la toma de decisiones serenas. Explícame qué es el 'sesgo de confirmación' y cómo nos engaña a todos haciéndonos buscar solo lo que nos da la razón. Dame 3 consejos de oro para tomar decisiones médicas o económicas de calado en la madurez con el máximo acierto y cero arrepentimientos.",
        "levels": [
            {"num": 1, "title": "Nivel 1: Decisión Impulsiva o Presionada", "desc": "Cedes ante la insistencia de comerciales o tomas decisiones en caliente guiado por el enfado o el miedo.", "color": "#DC2626", "badgeBg": "#FEE2E2", "kpi1": "40%", "kpi2": "REACTIVA", "reflexion": "La prisa es la mejor aliada del engaño. Aprende a decir: 'Me lo voy a pensar con la almohada y ya le diré'."},
            {"num": 2, "title": "Nivel 2: Prudencia Básica pero Dudas Frecuentes", "desc": "Sospechas de las prisas pero a veces te cuesta decir que no por educación o compromiso social.", "color": "#EA580C", "badgeBg": "#FFEDD5", "kpi1": "60%", "kpi2": "INDECISA", "reflexion": "Decir 'no' con educación y firmeza es la herramienta de libertad más poderosa que existe."},
            {"num": 3, "title": "Nivel 3: Análisis Sistemático de Opciones", "desc": "Pides presupuestos, comparas alternativas y no firmas nada sin leer la letra pequeña con calma.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "78%", "kpi2": "ORDENADA", "reflexion": "Tu método de contrastar datos antes de actuar te evita el 90% de los disgustos cotidianos."},
            {"num": 4, "title": "Nivel 4: Filtro Activo contra Falacias y Sesgos", "desc": "Sabes que lo barato sale caro, detectas las promesas vacías y sabes pedir segundas opiniones médicas.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "90%", "kpi2": "FIRME", "reflexion": "Tu experiencia vital te ha enseñado que los atajos mágicos no existen: el sentido común nunca falla."},
            {"num": 5, "title": "Nivel 5: Juicio Experto, Sosiego y Templanza", "desc": "Decides con paz interior absoluta. Tus hijos y amigos acuden a ti buscando consejo porque transmites claridad.", "color": "#D97706", "badgeBg": "#FEF3C7", "kpi1": "98%", "kpi2": "MAGISTRAL", "reflexion": "Has alcanzado la cima del buen juicio: saber qué batallas merecen la pena y cuáles es mejor dejar pasar."},
            {"num": 6, "title": "Nivel 6: Sabiduría Magistral y Consejo Paternal Certero", "desc": "Faro ético de la familia. Tus decisiones no solo son acertadas, sino que siembran concordia y unión en todo tu entorno.", "color": "#7C3AED", "badgeBg": "#EDE9FE", "kpi1": "100%", "kpi2": "INQUEBRANTABLE", "reflexion": "Tu serenidad al decidir es el mayor ancla de seguridad para las generaciones que vienen detrás de ti."}
        ]
    },
    {
        "session": 15,
        "tag": "NIV-015",
        "filename": "SIMULADOR_RESILIENCIA_SALUD_MENTAL_SENIORS.html",
        "title": "Los 5 Niveles de Resiliencia Emocional y Paz Mental (+65)",
        "subtitle": "Autodiagnóstico de Fortaleza Psicológica, Adaptabilidad al Cambio y Bienestar Interior",
        "step1_title": "Paso 1 • Hábitos de Serenidad y Afecto",
        "step1_desc": "Mide tus espacios diarios de tranquilidad interior y la solidez de tus lazos afectivos.",
        "sliders": [
            {
                "id": "rngMinutosPaz",
                "label": "Minutos diarios de desconexión, música o paseo en calma:",
                "min": 10, "max": 90, "val": 40, "unit": "min/día",
                "lblMin": "10 min", "lblMid": "40 min", "lblMax": "90 min",
                "color": "amber"
            },
            {
                "id": "rngRedApoyo",
                "label": "Grado de cercanía con personas de confianza:",
                "min": 1, "max": 10, "val": 8, "unit": "/10",
                "lblMin": "1 (Solitario)", "lblMid": "8", "lblMax": "10 (Muy arropado)",
                "color": "emerald"
            }
        ],
        "checks": [
            {"id": "chkAceptacionSerena", "title": "Distinción entre lo que controlo y lo que no:", "desc": "No me amargo por cosas que escapan a mi control; pongo mi energía en lo que sí puedo mejorar."},
            {"id": "chkGratitudDiaria", "title": "Práctica de la gratitud cotidiana:", "desc": "Valoro cada día las cosas sencillas: la salud, una buena charla, el sol en la ventana y el cariño de los míos."},
            {"id": "chkPerdonDesapego", "title": "Cero rencores del pasado:", "desc": "No cargo con heridas viejas; el perdón es el mejor desinfectante para vivir con el corazón ligero."},
            {"id": "chkPropositoVivo", "title": "Ilusión y proyectos de futuro:", "desc": "Tengo siempre algo entre manos que me despierta entusiasmo cada mañana (aprender, ayudar, crear)."}
        ],
        "kpi1_label": "Paz Interior:",
        "kpi1_default": "PLENA",
        "kpi2_label": "Resiliencia:",
        "kpi2_default": "INQUEBRANTABLE",
        "why_irreplaceable": "Una inteligencia artificial puede simular frases de autoayuda, pero jamás ha sentido el nudo en la garganta ante una despedida, la emoción de ver crecer a un nieto o la paz profunda de haber cumplido con el deber.",
        "gemini_prompt": "Actúa como un sabio psicólogo humanista y filósofo estoico especializado en adultos mayores (+65). Explícame cómo cultivar una resiliencia emocional inquebrantable ante los achaques de la edad o las pérdidas inevitables de la vida, y qué 3 reflexiones diarias me ayudarán a mantener la alegría de vivir y el corazón agradecido cada día.",
        "levels": [
            {"num": 1, "title": "Nivel 1: Vulnerabilidad al Agobio y Preocupación", "desc": "Te cuesta adaptarte a los cambios y los achaques o imprevistos te desaniman con facilidad.", "color": "#DC2626", "badgeBg": "#FEE2E2", "kpi1": "FRÁGIL", "kpi2": "SENSIBLE", "reflexion": "La vida cambia siempre. En vez de resistirte a la corriente, aprende a flotar con dulzura y paciencia."},
            {"num": 2, "title": "Nivel 2: Recuperación Lenta tras la Dificultad", "desc": "Superas los baches pero arrastras tristeza o preocupación durante demasiado tiempo.", "color": "#EA580C", "badgeBg": "#FFEDD5", "kpi1": "MEDIA", "kpi2": "VULNERABLE", "reflexion": "Compartir lo que sientes con un buen amigo o dar un paseo largo aclara la mente más que mil pensamientos en bucle."},
            {"num": 3, "title": "Nivel 3: Resiliencia Equilibrada y Adaptación Firme", "desc": "Aceptas las dificultades con entereza, sabes pedir ayuda cuando hace falta y mantienes la ilusión.", "color": "#2563EB", "badgeBg": "#DBEAFE", "kpi1": "BUENA", "kpi2": "SÓLIDA", "reflexion": "Has superado suficientes tormentas en tu vida para saber que tras los nubarrones siempre vuelve a brillar el sol."},
            {"num": 4, "title": "Nivel 4: Paz Interior Sólida y Serenidad Inquebrantable", "desc": "Vives sin rencores, disfrutas de los pequeños regalos diarios y tu mirada transmite calma a tu alrededor.", "color": "#059669", "badgeBg": "#D1FAE5", "kpi1": "ELEVADA", "kpi2": "FUERTE", "reflexion": "La verdadera victoria de la madurez no es evitar los dolores, sino no permitir que ninguno te quite la paz."},
            {"num": 5, "title": "Nivel 5: Plenitud Vital, Sabiduría Afectiva y Faro de Paz", "desc": "Cúspide de la salud mental humana. Corazón agradecido, bondad generosa y una serenidad que ilumina a toda tu familia.", "color": "#D97706", "badgeBg": "#FEF3C7", "kpi1": "PLENA", "kpi2": "INQUEBRANTABLE", "reflexion": "Eres el refugio de paz que tus hijos y nietos necesitan en este mundo acelerado. Tu presencia amorosa es un tesoro irrepetible."}
        ]
    }
]

def render_niv_html(cfg):
    num_str = f"{cfg['session']:02d}"
    tag = cfg['tag']
    title = cfg['title']
    subtitle = cfg['subtitle']
    step1_title = cfg['step1_title']
    step1_desc = cfg['step1_desc']
    sliders = cfg['sliders']
    checks = cfg['checks']
    levels = cfg['levels']
    kpi1_label = cfg['kpi1_label']
    kpi2_label = cfg['kpi2_label']
    kpi1_default = cfg['kpi1_default']
    kpi2_default = cfg['kpi2_default']
    why_irreplaceable = cfg['why_irreplaceable']
    gemini_prompt = cfg['gemini_prompt']
    total_levels = len(levels)

    # HTML de los Sliders
    sliders_html = ""
    for s in sliders:
        sliders_html += f'''
        <!-- Slider {s["id"]} -->
        <div class="bg-stone-50 border border-stone-200 rounded-xl p-3.5 flex flex-col gap-2">
          <div class="flex justify-between items-center text-xs sm:text-sm font-semibold text-stone-800">
            <span>{s["label"]}</span>
            <span id="lbl_{s["id"]}" class="font-mono text-sm font-extrabold text-{s["color"]}-700 bg-{s["color"]}-100 px-2 py-0.5 rounded border border-{s["color"]}-300">
              {s["val"]} {s["unit"]}
            </span>
          </div>
          <input type="range" id="{s["id"]}" min="{s["min"]}" max="{s["max"]}" value="{s["val"]}" oninput="updateSimulation()">
          <div class="flex justify-between text-[11px] text-stone-400 font-mono">
            <span>{s["lblMin"]}</span>
            <span>{s["lblMid"]}</span>
            <span>{s["lblMax"]}</span>
          </div>
        </div>
        '''

    # HTML de los Checkboxes
    checks_html = ""
    for c in checks:
        checks_html += f'''
          <label class="flex items-start gap-3 p-2.5 rounded-lg border border-stone-200 hover:bg-stone-50 cursor-pointer">
            <input type="checkbox" id="{c["id"]}" checked class="check-custom mt-0.5" onchange="updateSimulation()">
            <div class="text-xs sm:text-sm leading-tight text-stone-800">
              <strong class="text-stone-900 block">{c["title"]}</strong>
              {c["desc"]}
            </div>
          </label>
        '''

    # HTML de las tarjetas de nivel en la Columna 3
    cards_html = ""
    for lvl in levels:
        cards_html += f'''
        <!-- Tarjeta Nivel {lvl["num"]} -->
        <div id="cardLvl{lvl["num"]}" onclick="selectManualLevel({lvl["num"]})" class="card-step flex flex-col gap-2">
          <div class="flex items-center justify-between">
            <span class="step-badge" style="background:{lvl["badgeBg"]}; color:{lvl["color"]}; border:1px solid {lvl["color"]}40;">
              NIVEL {lvl["num"]}
            </span>
            <div class="w-6 h-6 rounded-full flex items-center justify-center font-mono font-extrabold text-xs" style="background:{lvl["badgeBg"]}; color:{lvl["color"]};">
              {lvl["num"]}
            </div>
          </div>
          <h3 class="text-sm font-extrabold text-stone-900 leading-snug">
            {lvl["title"]}
          </h3>
          <p class="text-xs text-stone-600 leading-relaxed">
            {lvl["desc"]}
          </p>
        </div>
        '''

    # JSON de niveles para JS
    levels_json = json.dumps({l["num"]: l for l in levels}, ensure_ascii=False, indent=6)

    # Prompt Gemini escapado para JS
    gemini_prompt_escaped = gemini_prompt.replace('"', '\\"').replace('\n', '\\n')

    # Slider IDs para JS
    slider_js_lines = ""
    for s in sliders:
        slider_js_lines += f'''
      const val_{s["id"]} = parseInt(document.getElementById('{s["id"]}').value);
      document.getElementById('lbl_{s["id"]}').innerText = val_{s["id"]} + " {s["unit"]}";
        '''

    html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} • Sesión {num_str} [{tag}]</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@600;800&display=swap" rel="stylesheet">
  <style>
    /* =========================================================================
       REGLAS BASE Y ERGONOMÍA SENIOR (3 COLUMNAS SIN SUPERPOSICIONES)
       ========================================================================= */
    *, *::before, *::after {{
      box-sizing: border-box;
    }}

    :root {{
      --base-font-size: 16px;
    }}

    html {{
      font-size: var(--base-font-size);
    }}

    html.large-text {{
      --base-font-size: 18.5px;
    }}

    html, body {{
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      overflow-x: hidden;
      background: #F4F1EA;
      color: #1C1917;
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      line-height: 1.45;
      word-wrap: break-word;
      overflow-wrap: break-word;
    }}

    .app-shell {{
      display: flex;
      flex-direction: column;
      height: 100vh;
      width: 100%;
      overflow: hidden;
    }}

    .top-bar {{
      flex-shrink: 0;
      background: #FFFFFF;
      border-bottom: 2px solid #D6D3D1;
      padding: 10px 16px;
      width: 100%;
    }}

    .three-cols {{
      flex: 1;
      min-height: 0;
      width: 100%;
      display: flex;
      flex-direction: row;
      gap: 12px;
      padding: 12px;
      overflow: hidden;
    }}

    .col {{
      min-width: 0;
      height: 100%;
      overflow-y: auto;
      background: #FFFFFF;
      border: 1px solid #E7E5E4;
      border-radius: 14px;
      padding: 16px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .step-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 9999px;
    }}

    .card-step {{
      border: 2px solid #E7E5E4;
      border-radius: 12px;
      padding: 14px;
      background: #FAFAF9;
      transition: all 0.2s ease;
      cursor: pointer;
    }}

    .card-step:hover {{
      border-color: #CBD5E1;
      background: #FFFFFF;
    }}

    .card-step.active {{
      border-color: #D97706;
      background: #FFFBEB;
      box-shadow: 0 4px 14px rgba(217, 119, 6, 0.15);
    }}

    input[type="range"] {{
      width: 100%;
      height: 8px;
      border-radius: 4px;
      background: #E2E8F0;
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
      accent-color: #D97706;
    }}

    .check-custom {{
      accent-color: #059669;
      width: 1.25rem;
      height: 1.25rem;
      cursor: pointer;
    }}

    .is-speaking {{
      animation: pulse-ring 1.4s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }}

    @keyframes pulse-ring {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.5; }}
    }}

    @media (max-width: 1024px) {{
      .app-shell {{
        height: auto;
        min-height: 100vh;
        overflow-y: auto;
      }}
      .three-cols {{
        flex-direction: column;
        height: auto;
        overflow: visible;
      }}
      .col {{
        height: auto;
        overflow: visible;
      }}
    }}
  </style>
</head>
<body>

  <div class="app-shell">

    <!-- BARRA SUPERIOR PERSISTENTE (TOP BAR) -->
    <header class="top-bar flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-3">
        <span class="bg-amber-100 text-amber-900 border border-amber-300 font-extrabold text-xs px-2.5 py-1 rounded-md tracking-wider font-mono">
          [{tag}] SESIÓN {num_str}
        </span>
        <div>
          <h1 class="text-base sm:text-lg font-extrabold text-stone-900 leading-tight">
            {title}
          </h1>
          <p class="text-xs text-stone-500 font-medium hidden sm:block">
            {subtitle}
          </p>
        </div>
      </div>

      <div class="flex items-center flex-wrap gap-2">
        <button id="btn-speak-main" onclick="speakDiagnosis()" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-semibold bg-emerald-700 hover:bg-emerald-800 text-white transition-colors shadow-sm">
          <span>🔊</span>
          <span id="speak-main-label">Escuchar Diagnóstico</span>
        </button>

        <button onclick="toggleFontSize()" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-semibold bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-300 transition-colors">
          <span>🔍</span>
          <span id="font-size-label">Letra: Normal</span>
        </button>

        <button onclick="resetSimulation()" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-semibold bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-300 transition-colors">
          <span>🔄</span>
          <span>Reiniciar</span>
        </button>

        <button onclick="openGeminiModal()" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-semibold bg-amber-600 hover:bg-amber-700 text-white transition-colors shadow-sm">
          <span>📋</span>
          <span>Prompt Gemini</span>
        </button>
      </div>
    </header>

    <!-- CUERPO PRINCIPAL: 3 COLUMNAS SIN SOLAPAMIENTO -->
    <main class="three-cols">

      <!-- COLUMNA 1: PARÁMETROS VITALES -->
      <section class="col w-full lg:w-1/3">
        <div class="border-b border-stone-200 pb-2">
          <span class="step-badge bg-blue-100 text-blue-800 border border-blue-300">
            {step1_title}
          </span>
          <h2 class="text-base font-bold text-stone-900 mt-1">
            Datos y Parámetros Vitales
          </h2>
          <p class="text-xs text-stone-600">
            {step1_desc}
          </p>
        </div>

        {sliders_html}

        <!-- Checklist Pilares -->
        <div class="flex flex-col gap-2">
          <span class="text-xs font-bold text-stone-700 uppercase tracking-wide">
            Pilares y Prácticas Clave:
          </span>

          {checks_html}
        </div>
      </section>

      <!-- COLUMNA 2: DIAGNÓSTICO Y RECONOCIMIENTO -->
      <section class="col w-full lg:w-1/3">
        <div class="border-b border-stone-200 pb-2">
          <span class="step-badge bg-amber-100 text-amber-800 border border-amber-300">
            Paso 2 • Tu Diagnóstico
          </span>
          <h2 class="text-base font-bold text-stone-900 mt-1">
            Evaluación y Estado Activo
          </h2>
          <p class="text-xs text-stone-600">
            El valor real de tu experiencia analizado con rigor y cercanía.
          </p>
        </div>

        <!-- Tarjeta Hero Diagnóstico -->
        <div id="statusHero" class="border-2 rounded-2xl p-4 sm:p-5 flex flex-col gap-3 transition-all" style="border-color:#D97706; background:#FFFBEB;">
          <div class="flex items-center justify-between">
            <span id="heroBadge" class="font-mono text-xs font-extrabold uppercase px-2.5 py-1 rounded bg-white border font-bold" style="color:#D97706; border-color:#FDE68A;">
              NIVEL ALCANZADO
            </span>
            <div id="heroCircle" class="w-10 h-10 rounded-full flex items-center justify-center font-extrabold font-mono text-lg bg-white shadow-sm border-2" style="border-color:#D97706; color:#D97706;">
              <span id="heroNum">{total_levels}</span>
            </div>
          </div>

          <div>
            <h3 id="heroTitle" class="text-base sm:text-lg font-extrabold text-stone-900 leading-snug">
              Cargando nivel...
            </h3>
            <p id="heroDesc" class="text-xs sm:text-sm text-stone-700 mt-1.5 leading-relaxed">
              Cargando descripción...
            </p>
          </div>

          <!-- Métricas de Impacto -->
          <div class="grid grid-cols-2 gap-2 pt-2 border-t border-amber-200">
            <div class="bg-white/80 p-2.5 rounded-lg border border-amber-200 text-center">
              <span class="block text-[11px] text-stone-500 font-bold uppercase">{kpi1_label}</span>
              <span id="valKpi1" class="font-mono text-base font-extrabold text-amber-900">{kpi1_default}</span>
            </div>
            <div class="bg-white/80 p-2.5 rounded-lg border border-amber-200 text-center">
              <span class="block text-[11px] text-stone-500 font-bold uppercase">{kpi2_label}</span>
              <span id="valKpi2" class="font-mono text-base font-extrabold text-emerald-800">{kpi2_default}</span>
            </div>
          </div>
        </div>

        <!-- Diploma de Reflexión Positiva -->
        <div class="bg-emerald-50 border border-emerald-300 rounded-xl p-3.5 flex flex-col gap-2">
          <div class="flex items-center gap-2 text-emerald-900 font-bold text-xs sm:text-sm">
            <span>🌱</span>
            <span>Por qué tu valor es insustituible por la IA:</span>
          </div>
          <p id="txtReflexion" class="text-xs sm:text-sm text-emerald-950 leading-relaxed font-medium">
            {why_irreplaceable}
          </p>
        </div>

        <!-- Botón Reproducir Voz -->
        <button onclick="speakDiagnosis()" class="w-full py-3 px-4 rounded-xl bg-stone-900 hover:bg-stone-800 text-white font-bold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-sm transition-all mt-auto">
          <span>🔊</span>
          <span id="speak-btn-bottom-label">Escuchar Explicación Completa</span>
        </button>
      </section>

      <!-- COLUMNA 3: LOS NIVELES DEL ESCALAFÓN -->
      <section class="col w-full lg:w-1/3">
        <div class="border-b border-stone-200 pb-2">
          <span class="step-badge bg-emerald-100 text-emerald-800 border border-emerald-300">
            Paso 3 • La Pirámide
          </span>
          <h2 class="text-base font-bold text-stone-900 mt-1">
            Los {total_levels} Niveles del Escalafón
          </h2>
          <p class="text-xs text-stone-600">
            Pulsa en cualquier tarjeta para explorar sus pautas y reflexiones.
          </p>
        </div>

        <div class="flex flex-col gap-3">
          {cards_html}
        </div>
      </section>

    </main>

  </div>

  <!-- MODAL PARA COPIAR PROMPT DE GEMINI -->
  <div id="modalGemini" class="fixed inset-0 bg-stone-900/60 backdrop-blur-sm hidden items-center justify-center p-4 z-50">
    <div class="bg-white rounded-2xl max-w-xl w-full p-6 shadow-2xl border border-stone-200 flex flex-col gap-4">
      <div class="flex justify-between items-center border-b border-stone-200 pb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">📋</span>
          <h3 class="font-extrabold text-stone-900 text-base sm:text-lg">Prompt Oficial para Gemini</h3>
        </div>
        <button onclick="closeGeminiModal()" class="text-stone-400 hover:text-stone-700 font-extrabold text-xl p-1">&times;</button>
      </div>

      <p class="text-xs text-stone-600">
        Copia este texto y pégalo directamente en <strong>Gemini</strong> (<a href="https://gemini.google.com" target="_blank" class="text-amber-700 underline font-bold">gemini.google.com</a>) para profundizar en tu diagnóstico con la IA:
      </p>

      <textarea id="txtPromptArea" readonly class="w-full h-40 p-3 bg-stone-50 border border-stone-300 rounded-xl text-xs sm:text-sm font-mono text-stone-800 leading-relaxed resize-none focus:outline-none">{gemini_prompt}</textarea>

      <div class="flex justify-end gap-3 pt-2">
        <button onclick="closeGeminiModal()" class="px-4 py-2 rounded-lg text-xs sm:text-sm font-bold bg-stone-100 hover:bg-stone-200 text-stone-700">
          Cerrar
        </button>
        <button onclick="copyToClipboard()" id="btnCopyPrompt" class="px-5 py-2 rounded-lg text-xs sm:text-sm font-extrabold bg-amber-600 hover:bg-amber-700 text-white shadow-sm flex items-center gap-2">
          <span>📋 Copiar Prompt</span>
        </button>
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT REACTIVO Y SÍNTESIS DE VOZ -->
  <script>
    const LEVEL_DATA = {levels_json};
    const TOTAL_LEVELS = {total_levels};

    let manualLevelOverride = null;
    let isLargeText = false;
    let synth = window.speechSynthesis;
    let currentUtterance = null;
    let isSpeaking = false;

    function updateSimulation() {{
      {slider_js_lines}

      let checks = 0;
      document.querySelectorAll('.check-custom').forEach(chk => {{
        if (chk.checked) checks++;
      }});

      let calculatedLvl = 1;
      const totalChecks = document.querySelectorAll('.check-custom').length;
      const checkRatio = checks / Math.max(1, totalChecks);

      if (checkRatio >= 0.25) calculatedLvl = 2;
      if (checkRatio >= 0.50) calculatedLvl = Math.min(TOTAL_LEVELS, 3);
      if (checkRatio >= 0.75) calculatedLvl = Math.min(TOTAL_LEVELS, 4);
      if (checkRatio >= 1.00) calculatedLvl = TOTAL_LEVELS;

      const activeLvl = manualLevelOverride !== null ? manualLevelOverride : calculatedLvl;
      renderLevel(activeLvl);
    }}

    function selectManualLevel(lvl) {{
      manualLevelOverride = lvl;
      renderLevel(lvl);
      if (isSpeaking) {{
        stopSpeaking();
        speakDiagnosis();
      }}
    }}

    function renderLevel(lvl) {{
      const data = LEVEL_DATA[lvl] || LEVEL_DATA[TOTAL_LEVELS];

      document.getElementById('heroNum').innerText = data.num;
      document.getElementById('heroNum').style.color = data.color;
      document.getElementById('heroCircle').style.borderColor = data.color;
      document.getElementById('heroBadge').style.color = data.color;
      document.getElementById('heroBadge').style.borderColor = data.color + '40';
      document.getElementById('statusHero').style.borderColor = data.color;
      document.getElementById('statusHero').style.backgroundColor = data.badgeBg;

      document.getElementById('heroTitle').innerText = data.title;
      document.getElementById('heroDesc').innerText = data.desc;
      document.getElementById('valKpi1').innerText = data.kpi1 || "{kpi1_default}";
      document.getElementById('valKpi2').innerText = data.kpi2 || "{kpi2_default}";
      document.getElementById('txtReflexion').innerText = data.reflexion;

      for (let i = 1; i <= TOTAL_LEVELS; i++) {{
        const card = document.getElementById('cardLvl' + i);
        if (card) {{
          if (i === data.num) {{
            card.classList.add('active');
            card.style.borderColor = data.color;
            card.style.backgroundColor = data.badgeBg;
          }} else {{
            card.classList.remove('active');
            card.style.borderColor = '#E7E5E4';
            card.style.backgroundColor = '#FAFAF9';
          }}
        }}
      }}
    }}

    function speakDiagnosis() {{
      if (!('speechSynthesis' in window)) {{
        alert("Tu navegador no soporta la lectura por voz.");
        return;
      }}

      if (isSpeaking) {{
        stopSpeaking();
        return;
      }}

      const title = document.getElementById('heroTitle').innerText;
      const desc = document.getElementById('heroDesc').innerText;
      const reflexion = document.getElementById('txtReflexion').innerText;
      const textToRead = `${{title}}. ${{desc}}. Reflexión importante: ${{reflexion}}`;

      currentUtterance = new SpeechSynthesisUtterance(textToRead);
      currentUtterance.lang = 'es-ES';
      currentUtterance.rate = 0.95;

      const voices = synth.getVoices();
      const spanishVoice = voices.find(v => v.lang.startsWith('es') || v.lang.includes('es-ES'));
      if (spanishVoice) currentUtterance.voice = spanishVoice;

      currentUtterance.onstart = () => {{
        isSpeaking = true;
        document.getElementById('speak-main-label').innerText = "Detener Voz";
        document.getElementById('speak-btn-bottom-label').innerText = "Detener Lectura de Voz";
        document.getElementById('btn-speak-main').classList.add('is-speaking');
      }};

      currentUtterance.onend = () => {{
        stopSpeaking();
      }};

      currentUtterance.onerror = () => {{
        stopSpeaking();
      }};

      synth.speak(currentUtterance);
    }}

    function stopSpeaking() {{
      if (synth.speaking || synth.pending) {{
        synth.cancel();
      }}
      isSpeaking = false;
      document.getElementById('speak-main-label').innerText = "Escuchar Diagnóstico";
      document.getElementById('speak-btn-bottom-label').innerText = "Escuchar Explicación Completa";
      document.getElementById('btn-speak-main').classList.remove('is-speaking');
    }}

    function toggleFontSize() {{
      isLargeText = !isLargeText;
      const htmlEl = document.documentElement;
      const lbl = document.getElementById('font-size-label');
      if (isLargeText) {{
        htmlEl.classList.add('large-text');
        lbl.innerText = "Letra: Grande (+)";
      }} else {{
        htmlEl.classList.remove('large-text');
        lbl.innerText = "Letra: Normal";
      }}
    }}

    function resetSimulation() {{
      manualLevelOverride = null;
      document.querySelectorAll('input[type="range"]').forEach(r => {{
        r.value = r.defaultValue || r.getAttribute('value');
      }});
      document.querySelectorAll('.check-custom').forEach(c => {{
        c.checked = true;
      }});
      stopSpeaking();
      updateSimulation();
    }}

    function openGeminiModal() {{
      document.getElementById('modalGemini').classList.remove('hidden');
      document.getElementById('modalGemini').classList.add('flex');
    }}

    function closeGeminiModal() {{
      document.getElementById('modalGemini').classList.add('hidden');
      document.getElementById('modalGemini').classList.remove('flex');
    }}

    function copyToClipboard() {{
      const txt = document.getElementById('txtPromptArea').value;
      navigator.clipboard.writeText(txt).then(() => {{
        const btn = document.getElementById('btnCopyPrompt');
        btn.innerHTML = "<span>✅ ¡Copiado con Éxito!</span>";
        btn.classList.remove('bg-amber-600', 'hover:bg-amber-700');
        btn.classList.add('bg-emerald-600');
        setTimeout(() => {{
          btn.innerHTML = "<span>📋 Copiar Prompt</span>";
          btn.classList.remove('bg-emerald-600');
          btn.classList.add('bg-amber-600', 'hover:bg-amber-700');
          closeGeminiModal();
        }}, 1400);
      }}).catch(() => {{
        alert("Selecciona y copia el texto manualmente.");
      }});
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      updateSimulation();
      if ('speechSynthesis' in window) {{
        speechSynthesis.onvoiceschanged = () => {{}};
      }}
    }});
  </script>
</body>
</html>
'''
    return html_content

def main():
    print("=================================================================")
    print("=== GENERACIÓN CANÓNICA DE LAS 11 FICHAS NIV (3 COLUMNAS S04) ===")
    print("=================================================================")

    for cfg in CONFIG_NIV:
        s_num = cfg['session']
        s_folder = os.path.join(BASE_SESSIONS, f"{s_num:02d}_Sesion")
        target_path_session = os.path.join(s_folder, cfg['filename'])
        target_path_sim = os.path.join(BASE_SIMULADORES, cfg['filename'])

        content = render_niv_html(cfg)

        # 1. Guardar en la carpeta de la sesión correspondiente
        if os.path.exists(s_folder):
            with open(target_path_session, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Sesión {s_num:02d}: {cfg['filename']} -> Guardado en {s_folder}")
        else:
            print(f"⚠️ No existe carpeta de sesión: {s_folder}")

        # 2. Guardar en SIMULADORES_INTERACTIVOS/01_SIMULADORES
        if os.path.exists(BASE_SIMULADORES):
            with open(target_path_sim, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"   ↳ Copiado a SIMULADORES_INTERACTIVOS: {cfg['filename']}")

    print("=================================================================")
    print("🎉 ¡LAS 11 FICHAS NIV HAN SIDO TRANSFORMADAS AL MODELO 3 COLUMNAS!")
    print("=================================================================")

if __name__ == '__main__':
    main()
