# -*- coding: utf-8 -*-
"""
Repositorio Maestro de 60 Infografías Científico-Enciclopédicas V2
Estilo: Escalafones, Pirámides y Clasificación por Niveles ([NIV] - Cultura 101)
"""

def get_niv_items():
    items = []
    
    def make_prompt(title, concept, num_levels, apex_desc, levels_list):
        step1 = (
            f"Actúa como un diseñador infográfico senior y docente divulgador. "
            f"Diseña y redacta un prompt maestro detallado en español para crear una infografía piramidal o escalafón vertical "
            f"sobre '{title}' ({concept}). "
            f"Describe con gran rigor los {num_levels} estratos desde la base hasta la cima con metáforas visuales claras, "
            f"un icono 3D en la cúspide ({apex_desc}) y la regla estricta de todos los rótulos 100% en español. "
            f"NO generes la imagen todavía, solo entrégame el prompt de texto listo para copiar."
        )
        step2 = "¡Perfecto! Genera ahora la imagen de esta infografía piramidal en máxima resolución 8K siguiendo exactamente la estructura y metáforas visuales que acabas de redactar."
        return (step1, step2)

    def add_it(code, title, concept, num_l, apex, levels, tips_extra):
        p = make_prompt(title, concept, num_l, apex, levels)
        t = (
            f"<b>Paso 1:</b> Pídele a Gemini que diseñe el prompt con la orden del Paso 1.<br/>"
            f"<b>Paso 2:</b> En la misma conversación de chat, pídele que pinte la infografía.<br/><br/>"
            f"<b>👉 Ahora te toca a ti: ¡Haz tú una modificación que se te ocurra y sorpréndenos!</b> Pídele a Gemini en el chat: <i>\"{tips_extra}\"</i>"
        )
        items.append({
            'id_code': code,
            'is_senior_microapp': False,
            'block_dir': '09. [NIV] BLOQUE_9_ESCALAFONES_Y_NIVELES_CULTURA101',
            'block_name': 'BLOQUE X: ESCALAFONES Y NIVELES DE CLASIFICACIÓN UNIVERSAL [NIV] (Cultura 101)',
            'title': title,
            'concept': concept,
            'concept_text': concept,
            'prompt': p,
            'prompt_data': p,
            'tips': t,
            'tips_text': t,
            'extra': None
        })

    def add_senior_microapp(code, title, concept, seed_step1, seed_step2, blueprint, sim_file, sim_title):
        items.append({
            'id_code': code,
            'is_senior_microapp': True,
            'block_dir': '09. [NIV] BLOQUE_9_ESCALAFONES_Y_NIVELES_CULTURA101',
            'block_name': 'BLOQUE X: ESCALAFONES Y MICRO-APLICACIONES DE VIDA REAL [NIV] (+65)',
            'title': title,
            'concept': concept,
            'concept_text': concept,
            'seed_step1': seed_step1,
            'seed_step2': seed_step2,
            'blueprint': blueprint,
            'sim_file': sim_file,
            'sim_title': sim_title,
            'prompt': (seed_step1, seed_step2),
            'prompt_data': f"PASO 1 (PROMPT SEMILLA):\n{seed_step1}\n\nPASO 2 (ORDEN DE EJECUCIÓN):\n{seed_step2}",
            'tips': f"<b>Paso 1:</b> Dicta o escribe la orden semilla en Gemini.<br/><b>Paso 2:</b> Da la orden de generar la Micro-App HTML.<br/><b>Garantía Oficial:</b> Si tu IA tarda, pulsa en el simulador terminado: <i>{sim_file}</i>",
            'tips_text': f"Paso 1: Dicta o escribe la orden semilla en Gemini.\nPaso 2: Da la orden de generar la Micro-App HTML.\nGarantía Oficial: Si tu IA tarda, pulsa en el simulador terminado: {sim_file}",
            'extra': None
        })

    # =========================================================================
    # LOTE 1 (SESIONES 01 A 10): MICRO-APLICACIONES INTERACTIVAS SENIORS (+65)
    # =========================================================================
    add_senior_microapp(
        '[NIV-001]',
        'Los 5 Escalones de la Tranquilidad en la Jubilación',
        'Micro-aplicación interactiva de diagnóstico financiero familiar para personas mayores (+65). Permite visualizar con total claridad cómo se combinan la pensión pública mensual, los ahorros guardados y la vivienda en propiedad para garantizar paz mental y solvencia vitalicia sin depender de nadie.',
        'Actúa como un orientador familiar y pedagogo para personas mayores de 65 años.\nExplícame en 3 puntos claros cómo estructurar una calculadora sencilla en HTML para valorar la tranquilidad en la jubilación, teniendo en cuenta la pensión vitalicia, los ahorros guardados y la vivienda propia.',
        'Perfecto. Ahora genera en un único archivo HTML interactivo la calculadora completa: con diseño oscuro accesible, deslizadores fáciles, tipografía grande (17px) y mensajes tranquilizadores sin jerga financiera inglesa.',
        '• Controles (Sliders): Pensión mensual (0-4.000 €), Gastos mensuales (0-4.000 €), Ahorros bancarios (0-300.000 €), Valor vivienda propia (0-600.000 €).\n• Lógica sin contradicciones: Si la pensión cubre los gastos, los ahorros no se tocan jamás ("Vitalicio"). Si hay déficit mensual, calcula cuántos años de colchón quedan.\n• 5 Escalones visuales: 1. Ajuste necesario, 2. Respiro mensual, 3. Colchón de seguridad, 4. Disfrutar de la jubilación, 5. Paz y serenidad total.\n• Interfaz: Modo oscuro (#060913), alto contraste, botones amplios, tipografía grande y advertencias en color verde/ámbar.',
        'SIMULADOR_TRANQUILIDAD_JUBILACION.html',
        'Calculadora Tranquilidad Jubilación (+65)'
    )

    add_senior_microapp(
        '[NIV-002]',
        'Radar de Detección de Fraudes y Estafas para Mayores',
        'Micro-aplicación interactiva diseñada como escudo protector contra las estafas más habituales dirigidas a seniors: llamadas urgentes haciéndose pasar por el banco, mensajes SMS de paquetes falsos, falsos revisores del gas o timos del hijo en apuros. Evalúa el nivel de riesgo en segundos y ofrece pautas de acción seguras.',
        'Actúa como un inspector de policía especializado en ciberseguridad para mayores.\nExplícame en 3 puntos cómo crear un detector interactivo en HTML que ayude a mis padres a identificar si un mensaje, llamada telefónica o visita a casa es una estafa.',
        'Genera en un único archivo HTML la aplicación completa del Radar Antifraude: con preguntas claras de respuesta Sí/No, semáforo de peligro (Verde, Ámbar, Rojo), botones de marcado rápido de emergencia (091/062) y textos grandes.',
        '• Cuestionario dinámico: 6 situaciones cotidianas (urgencia por hacer transferencia, pedir claves secretas por SMS, visita no avisada del gas, link desconocido).\n• Algoritmo de puntuación: 0 puntos = Seguro (Verde), 1-2 puntos = Sospechoso (Ámbar), 3+ puntos = Estafa Inminente (Rojo).\n• Panel de socorro: Botones directos para llamar al 091 (Policía Nacional), 062 (Guardia Civil) o bloquear tarjeta bancaria.\n• Diseño: Tipografía de 18px, iconos nítidos, colores contrastados y sin tecnicismos informáticos.',
        'SIMULADOR_RADAR_ESTAFAS_SENIORS.html',
        'Radar Antifraude para Seniors (+65)'
    )

    add_senior_microapp(
        '[NIV-003]',
        'Los 5 Niveles del Poder Geopolítico y la Economía del Hogar',
        'Herramienta pedagógica interactiva que conecta los grandes movimientos de la geopolítica mundial (crisis energéticas, aranceles, conflictos y tipos de interés) con su impacto directo en el bolsillo diario del jubilado: la factura de la luz, el precio del gasóleo, la barra de pan y el coste del aceite.',
        'Actúa como un divulgador económico cercano para personas mayores.\nExplícame en 3 puntos cómo diseñar una aplicación interactiva que muestre cómo las noticias de conflictos y mercados mundiales influyen en los precios de la compra diaria en España.',
        'Crea el código HTML completo con una escala de 5 niveles geopolíticos, simulador de cesta de la compra con deslizadores para luz, carburante y alimentos, y consejos prácticos de ahorro doméstico.',
        '• 5 Niveles de Impacto: Local, Nacional, Europeo, Geopolítico Global, Cambio de Orden Mundial.\n• Deslizadores de costes del hogar: Factura de electricidad (30-200 €), Calefacción/Gas (20-180 €), Cesta de alimentos (150-600 €).\n• Simulador de escenarios: "Paz y estabilidad", "Subida de petróleo", "Tensión internacional".\n• Métricas: Inflación estimada en el hogar y recomendaciones prácticas de optimización de tarifas.',
        'SIMULADOR_RADAR_GEOPOLITICA_SENIORS.html',
        'Radar Geopolítica y Cesta de la Compra (+65)'
    )

    add_senior_microapp(
        '[NIV-004]',
        'Los 6 Niveles de Aporte de Valor y Sabiduría Senior',
        'Micro-aplicación de autodiagnóstico del capital humano y vital. Ayuda a las personas mayores a poner en valor su inmensa trayectoria profesional y personal: resolución de conflictos familiares, mentoría a nietos o emprendedores, voluntariado social y transmisión de valores éticos.',
        'Actúa como un psicólogo y orientador de talento sénior.\nExplícame en 3 puntos cómo crear un test interactivo en HTML que valore las 6 formas en que una persona jubilada aporta sabiduría y valor a su familia y a la sociedad.',
        'Genera el código HTML completo en un único archivo: con preguntas sencillas tipo test, gráfico de radar de fortalezas, tipografía grande y diploma descargable de Mentor Vitalicio.',
        '• 6 Niveles de Sabiduría: 1. Experiencia técnica, 2. Resolución de problemas, 3. Templanza emocional, 4. Mediación de conflictos familiares, 5. Mentoría generacional, 6. Legado ético y cultural.\n• Cuestionario de 6 preguntas con escala 1 a 5.\n• Resultado: Gráfico de radar visual y cálculo de la "Puntuación de Sabiduría Activa".',
        'SIMULADOR_APORTE_VALOR_EMPRESA_SENIORS.html',
        'Simulador Sabiduría y Valor Senior (+65)'
    )

    add_senior_microapp(
        '[NIV-005]',
        'Los 5 Niveles de la Evolución del Dinero: Del Trueque a Bizum',
        'Guía interactiva e histórica pensada para mayores que vivieron la transición de las pesetas al euro, las libretas de ahorro tradicionales y ahora se enfrentan a Bizum, pagos contactless y tarjetas virtuales. Explica el funcionamiento seguro de cada medio de pago.',
        'Actúa como un pedagogo financiero para mayores de 65 años.\nExplícame en 3 pasos cómo crear una aplicación interactiva que explique la historia del dinero desde las monedas de plata hasta Bizum, transmitiendo tranquilidad y seguridad.',
        'Genera el archivo HTML interactivo con las 5 etapas del dinero, comparativa de seguridad en el pago con móvil, y consejos paso a paso para usar Bizum y tarjeta sin miedo.',
        '• 5 Niveles: 1. Moneda física y peseta, 2. Libreta de ahorro bancaria, 3. Tarjeta de débito/crédito, 4. Banca online en el ordenador, 5. Bizum y pago con teléfono móvil.\n• Pestaña de práctica: Simulador guiado de un envío de Bizum paso a paso (sin dinero real) para perder el miedo.\n• Protocolos de seguridad: Cómo evitar pagos duplicados y límites de seguridad en la app del banco.',
        'SIMULADOR_EVOLUCION_DINERO_SENIORS.html',
        'Simulador Evolución del Dinero (+65)'
    )

    add_senior_microapp(
        '[NIV-006]',
        'Calculadora de Poder Adquisitivo y Cesta de la Compra Real',
        'Simulador doméstico que compara el coste de los productos esenciales del supermercado (leche, pan, huevos, aceite de oliva, carne) con la revalorización de la pensión. Permite calcular el poder adquisitivo real y detectar desajustes en el presupuesto mensual.',
        'Actúa como un economista doméstico para personas jubiladas.\nExplícame en 3 puntos cómo hacer una calculadora en HTML que compare la evolución de la pensión frente a la subida de los alimentos básicos en el supermercado.',
        'Genera la aplicación interactiva en HTML con deslizadores para la pensión y los artículos de la cesta básica, mostrando el porcentaje de revalorización real y recomendaciones de compra inteligente.',
        '• Deslizadores de productos: Aceite de oliva, huevos, panadería, lácteos, carnes/pescados y productos de higiene.\n• Deslizador de Pensión: Comparación interanual (IPC vs. Subida real).\n• Semáforo de holgura: Verde (Pensión supera a la cesta), Ámbar (Empate técnico), Rojo (Pérdida de poder adquisitivo).\n• Consejos de ahorro: Marcas de distribución, compra por temporadas y trucos de conservación de alimentos.',
        'SIMULADOR_PODER_ADQUISITIVO_COSTE_VIDA_SENIORS.html',
        'Calculadora Poder Adquisitivo (+65)'
    )

    add_senior_microapp(
        '[NIV-007]',
        'Los 5 Niveles de Automatización e IA en el Hogar de los Mayores',
        'Laboratorio interactivo de domótica y tecnologías de asistencia doméstica para la tercera edad. Muestra desde electrodomésticos convencionales hasta asistentes de voz (Alexa/Google), sensores de caída en el baño, cerraduras inteligentes y recordatorios médicos automatizados.',
        'Actúa como un especialista en tecnología accesible para el cuidado de mayores.\nExplícame en 3 puntos cómo crear un simulador en HTML que enseñe cómo la domótica y los altavoces inteligentes pueden ayudar a vivir de forma independiente y segura en casa.',
        'Genera el archivo HTML interactivo con los 5 niveles de tecnología para el hogar, un plano interactivo de la casa con dispositivos activables (luz, voz, alarma) y guía de privacidad.',
        '• 5 Niveles: 1. Electrodomésticos tradicionales, 2. Programadores y mandos a distancia, 3. Asistentes de voz y bombillas automáticas, 4. Sensores de salud y teleasistencia conectada, 5. IA preventiva de caídas.\n• Plano interactivo del hogar: Habitaciones donde activar sensores de seguridad y luces con sensor nocturno.\n• Medidor de tranquilidad familiar: Incremento de seguridad y autonomía personal.',
        'SIMULADOR_AUTOMATIZACION_TRABAJO_IA_SENIORS.html',
        'Simulador Asistencia e IA en el Hogar (+65)'
    )

    add_senior_microapp(
        '[NIV-008]',
        'Radar Antimanipulación: Los 6 Niveles de Persuasión y Venta Agresiva',
        'Detector interactivo de técnicas de venta abusivas y presión psicológica: llamadas comerciales a la hora de la siesta, comerciales a puerta fría vendiendo colchones milagro o contratos de luz engañosos, y ofertas exprés con límite de 24 horas.',
        'Actúa como un experto en derechos del consumidor para personas mayores.\nExplícame en 3 puntos cómo hacer un test interactivo en HTML para detectar cuándo un comercial por teléfono o en persona está usando técnicas de manipulación o venta agresiva.',
        'Genera el código HTML del Radar Antimanipulación: con preguntas sencillas, detector de "trampas típicas", frases comodín para decir NO con asertividad y botón para inscribirse en la Lista Robinson.',
        '• 6 Niveles de Persuasión comercial: 1. Información neutra, 2. Halago y simpatía forzada, 3. Falsa urgencia ("Solo hoy"), 4. Miedo a perder un beneficio, 5. Confusión contractual, 6. Intimidación psicológica.\n• Guión asertivo: Frases prefabricadas grandes para colgar el teléfono o despedir comerciales amablemente.\n• Enlace informativo a la Lista Robinson y derecho de desistimiento de 14 días.',
        'SIMULADOR_RADAR_PERSUASION_PUBLICIDAD_SENIORS.html',
        'Radar Antimanipulación y Ventas (+65)'
    )

    add_senior_microapp(
        '[NIV-009]',
        'Semáforo de Seguridad Ciudadana y Prevención en el Hogar',
        'Herramienta interactiva de prevención y seguridad física para el día a día: cómo evitar descuidos al sacar dinero en el cajero, precauciones en la calle frente al timo de la estampita o el abrazo solidario, y revisión de cerraduras y mirillas de seguridad en el domicilio.',
        'Actúa como un delegado de participación ciudadana de la Policía Nacional.\nExplícame en 3 puntos cómo estructurar una guía interactiva en HTML para prevenir robos y descuidos habituales tanto en la calle como en el portal y el domicilio.',
        'Genera la aplicación HTML interactiva con un semáforo de seguridad en 3 entornos (Calle y Cajero, Portal y Puerta, Interior del Hogar), checklist de verificación y teléfonos de auxilio.',
        '• 3 Escenarios Clave: 1. Cajero automático (cubrir teclado, acompañamiento), 2. Portal y descansillo (no abrir a desconocidos, mirilla digital), 3. Seguridad en la calle (bolso cruzado, desconfiar de empujones extraños).\n• Semáforo de Hábitos: Puntuación según el cumplimiento de buenas prácticas.\n• Tarjeta de emergencia con teléfonos directos: 091, 062 y 112.',
        'SIMULADOR_SEGURIDAD_PREVENCION_SENIORS.html',
        'Semáforo Seguridad Ciudadana (+65)'
    )

    add_senior_microapp(
        '[NIV-010]',
        'Los 6 Niveles de Alfabetización y Blindaje Patrimonial Familiar',
        'Simulador de orden patrimonial y legado familiar: testamento ordenado ante notario, titularidad y autorización en cuentas bancarias para evitar bloqueos por herencia, poderes notariales preventivos y donaciones en vida según fiscalidad autonómica.',
        'Actúa como un notario y asesor patrimonial de confianza para familias.\nExplícame en 3 pasos cómo hacer una aplicación interactiva en HTML que ayude a una persona mayor a comprobar si tiene sus papeles, testamento y cuentas ordenadas para proteger a sus hijos.',
        'Genera la aplicación HTML en un archivo único: con un checklist de 6 pilares de tranquilidad jurídica, explicaciones claras sobre la diferencia entre heredero y autorizado en el banco, y semáforo de orden patrimonial.',
        '• 6 Pilares de Blindaje: 1. Testamento al día, 2. Cuentas bancarias claras (cotitularidad vs. autorización), 3. Poder notarial preventivo, 4. Organización de escrituras de inmuebles, 5. Registro de seguros de vida, 6. Voluntades anticipadas médicas.\n• Diagnóstico: Porcentaje de protección familiar completado y pasos recomendados a seguir.',
        'SIMULADOR_SALUD_FINANCIERA_SENIORS.html',
        'Blindaje Patrimonial y Cuentas (+65)'
    )

    # =========================================================================
    # LOTE 2 (SESIONES 11 A 20): MICRO-APLICACIONES INTERACTIVAS SENIORS (+65)
    # =========================================================================
    add_senior_microapp(
        '[NIV-011]',
        'Los 7 Niveles de Inteligencia Cognitiva y Sabiduría en la Madurez',
        'Micro-aplicación de estimulación y evaluación de la reserva cognitiva. Muestra cómo el cerebro sénior compensa la velocidad con sabiduría cristalizada, razonamiento estratégico, intuición basada en patrones acumulados y resolución madura de problemas.',
        'Actúa como un neuropsicólogo especializado en envejecimiento activo.\nExplícame en 3 puntos cómo crear un test interactivo en HTML que ayude a una persona mayor a reconocer y entrenar su inteligencia cristalizada y reserva cognitiva.',
        'Genera la aplicación HTML interactiva con ejercicios breves de agilidad mental (sin estrés), diagnóstico de reserva cognitiva y consejos diarios de nutrición y ejercicio cerebral.',
        '• 7 Dimensiones cognitivas: Vocabulario, razonamiento verbal, juicio ético, memoria de trabajo, creatividad vital, templanza y síntesis de experiencias.\n• 3 Minijuegos de gimnasia mental: Asociación de palabras, cálculo mental cotidiano y reconocimiento de patrones.\n• Puntuación de "Reserva Cognitiva Activa" y recomendaciones de actividades.',
        'SIMULADOR_INTELIGENCIA_COGNITIVA_SENIORS.html',
        'Diagnóstico Reserva Cognitiva (+65)'
    )

    add_senior_microapp(
        '[NIV-012]',
        'Los 6 Niveles de Conciencia, Ritmos Circadianos y Alerta Serena',
        'Guía interactiva del sueño y la energía vital para mayores: cómo adaptar los ritmos circadianos con la edad, higiene del sueño frente al despertar temprano, la siesta española reparadora (20 min) y técnicas de respiración para calmar la mente y lograr alerta serena.',
        'Actúa como un médico especialista en medicina del sueño y gerontología.\nExplícame en 3 pasos cómo hacer un planificador interactivo en HTML para ayudar a una persona mayor a dormir mejor y tener energía estable durante el día.',
        'Crea la aplicación en HTML con un reloj interactivo de 24 horas que organice la luz solar matutina, las comidas, la siesta corta y las horas de descanso nocturno sin recurrir a somníferos innecesarios.',
        '• Reloj circadiano de 24 horas: Horas óptimas de paseo al sol, ingesta de líquidos, cena ligera y desconexión de pantallas.\n• Calculadora del sueño: Evaluación de horas dormidas y calidad del descanso.\n• Ejercicio guiado de respiración 4-7-8 con animación relajante para conciliar el sueño.',
        'SIMULADOR_CONCIENCIA_ALERTA_NEUROLOGICA_SENIORS.html',
        'Simulador Ritmos y Alerta Serena (+65)'
    )

    add_senior_microapp(
        '[NIV-013]',
        'Los 5 Niveles de Memoria Práctica y Retención Cotidiana',
        'Entrenador interactivo para la memoria del día a día: recordar nombres de personas, dónde se han dejado las gafas o las llaves, la toma de medicamentos a su hora y citas del médico. Distingue los despistes normales de la edad de síntomas que requieren consulta médica.',
        'Actúa como un terapeuta ocupacional de memoria para adultos mayores.\nExplícame en 3 puntos cómo crear una aplicación en HTML con trucos mnemotécnicos prácticos para recordar tareas y objetos cotidianos sin agobios.',
        'Genera el archivo HTML completo con un simulador de "Puntos Fijos en Casa", técnicas de asociación visual para nombres y un semáforo de tranquilidad sobre la memoria.',
        '• 5 Niveles de Memoria: 1. Sensorial, 2. Inmediata (las llaves), 3. Procedural (cocinar/conducir), 4. Episódica (recuerdos de juventud), 5. Prospectiva (acordarse de la cita de mañana).\n• Métodos prácticos: "El rincón de las cosas fijas", técnica de la cadena visual y notas de voz en el móvil.\n• Guía tranquilizadora sobre olvidos benignos vs. señales de alarma.',
        'SIMULADOR_MEMORIA_RETENCION_BIOLOGICA_SENIORS.html',
        'Simulador Memoria Cotidiana (+65)'
    )

    add_senior_microapp(
        '[NIV-014]',
        'Los 6 Niveles de Toma de Decisiones y Filtro de Sesgos Mentales',
        'Herramienta interactiva para tomar decisiones familiares o económicas importantes con serenidad: ayudar económicamente a un hijo, cambiar de vivienda a una más accesible, vender un coche o afrontar un tratamiento médico. Enseña a filtrar el miedo y las presiones externas.',
        'Actúa como un mediador y consejero de familia para personas mayores.\nExplícame en 3 pasos cómo hacer una balanza interactiva de decisiones en HTML que ayude a sopesar pros, contras y emociones ante un cambio importante de vida.',
        'Genera la aplicación HTML con una balanza digital donde introducir argumentos a favor y en contra, filtro de sesgos (miedo a la pérdida, presión familiar) y un consejo final de templanza.',
        '• Balanza interactiva: Ponderación de factores emocionales, económicos y de salud.\n• Filtro de los 4 Sesgos comunes: Aversión a cambiar de casa, culpa por decir no, exceso de confianza y efecto ancla en precios antiguos.\n• Informe de decisión serena con resumen para hablarlo en familia.',
        'SIMULADOR_TOMA_DECISIONES_SESGOS_SENIORS.html',
        'Filtro de Sesgos y Decisiones (+65)'
    )

    add_senior_microapp(
        '[NIV-015]',
        'Los 5 Niveles de Resiliencia Emocional y Fortaleza Interior',
        'Micro-aplicación de bienestar psicológico y adaptación a las etapas de la jubilación: afrontar el síndrome del nido vacío, sobrellevar pérdidas de seres queridos, aceptar limitaciones físicas con dignidad y redescubrir propósitos vitales ilusionantes.',
        'Actúa como un psicólogo humanista experto en la etapa de la madurez.\nExplícame en 3 puntos cómo crear un termómetro emocional interactivo en HTML que ayude a fortalecer la resiliencia y el ánimo diario.',
        'Genera el código HTML interactivo con el "Termómetro de Resiliencia", diario de agradecimiento guiado en 3 clics y caja de herramientas emocionales para días difíciles.',
        '• 5 Niveles de Fortaleza: 1. Desánimo o soledad, 2. Aceptación serena, 3. Conexión social activa, 4. Sentido de utilidad vital, 5. Sabiduría y plenitud interior.\n• Diario positivo de 3 cosas buenas del día.\n• Recursos de apoyo: Directorio de centros de día, teléfonos de la esperanza y asociaciones de voluntariado.',
        'SIMULADOR_RESILIENCIA_SALUD_MENTAL_SENIORS.html',
        'Simulador Resiliencia y Paz Interior (+65)'
    )

    add_senior_microapp(
        '[NIV-016]',
        'Los 6 Niveles de Prevención de Hábitos y Seguridad Farmacológica',
        'Organizador y semáforo de seguridad farmacológica para mayores: cómo prevenir interacciones entre medicamentos recetados por distintos especialistas, evitar automedicarse con pastillas para dormir o analgésicos, y organizar el pastillero semanal sin errores.',
        'Actúa como un farmacéutico comunitario y geriatra.\nExplícame en 3 puntos cómo crear una aplicación interactiva en HTML para ayudar a una persona mayor a gestionar su pastillero semanal y evitar mezclas peligrosas de medicinas.',
        'Genera el archivo HTML interactivo con un pastillero digital interactivo (Mañana, Mediodía, Tarde, Noche), verificador de precauciones básicas y consejos para hablar con el médico de cabecera.',
        '• Pastillero visual interactivo: Configuración de tomas con colores y recordatorios.\n• Semáforo de advertencias: Alertas sobre no duplicar dosis si se olvida una toma, no mezclar con alcohol ni zumo de pomelo, y revisión semestral de recetas.\n• Tarjeta imprimible de medicación actual para llevar siempre en la cartera al acudir a urgencias.',
        'SIMULADOR_PREVENCION_ADICCIONES_HABITOS_SENIORS.html',
        'Semáforo Seguridad Farmacológica (+65)'
    )

    add_senior_microapp(
        '[NIV-017]',
        'Los 5 Niveles de Empatía, Vínculo Familiar e Inteligencia Emocional',
        'Guía interactiva para fortalecer las relaciones afectivas entre generaciones: cómo comunicarse con hijos adultos respetando su independencia, conectar con nietos adolescentes a través de sus intereses, y expresar necesidades propias con afecto sin caer en el reproche.',
        'Actúa como un orientador familiar y pedagogo intergeneracional.\nExplícame en 3 pasos cómo hacer una aplicación en HTML que dé pautas para mejorar la comunicación y el cariño entre abuelos, hijos y nietos.',
        'Genera la aplicación interactiva en HTML con situaciones cotidianas (consejos no pedidos, visitas familiares, uso del móvil en la mesa) y frases constructivas para dialogar con empatía.',
        '• 5 Niveles de Conexión: 1. Distanciamiento o reproche, 2. Convivencia educada, 3. Escucha activa sin juicio, 4. Complicidad y apoyo mutuo, 5. Vínculo intergeneracional profundo.\n• Simulador de conversaciones: Respuestas ante frases difíciles de hijos o nietos.\n• Ideas para compartir tiempo de calidad: Cocinar juntos, contar historias de infancia, paseos.',
        'SIMULADOR_EMPATIA_INTELIGENCIA_EMOCIONAL_SENIORS.html',
        'Simulador Empatía Familiar (+65)'
    )

    add_senior_microapp(
        '[NIV-018]',
        'Los 6 Niveles de Disciplina Serena y Hábitos de Longevidad Activa',
        'Planificador interactivo de hábitos saludables para vivir con vitalidad e independencia: caminata diaria (7.000 pasos), ejercicios de fuerza y equilibrio para prevenir caídas, hidratación suficiente, lectura activa y vida social estimulante.',
        'Actúa como un médico especialista en geriatría preventiva y ejercicio en mayores.\nExplícame en 3 puntos cómo crear un planificador diario en HTML para mantener hábitos de longevidad activa adaptados a cada ritmo físico.',
        'Genera la aplicación HTML con un contador de hábitos saludables (Paseo, Agua, Lectura, Equilibrio, Conversación), gráfico de progreso semanal y mensajes motivadores.',
        '• Los 5 Pilares de Longevidad: 1. Movimiento diario (paseo y fuerza suave), 2. Nutrición mediterránea rica en proteína, 3. Hidratación regular (1,5L agua), 4. Entrenamiento de equilibrio sobre una pierna, 5. Interacción social diaria.\n• Panel de seguimiento semanal sencillo con casillas marcables.\n• Medidor de energía física y bienestar corporal.',
        'SIMULADOR_DISCIPLINA_HABITOS_VIDA_SENIORS.html',
        'Simulador Hábitos y Longevidad (+65)'
    )

    add_senior_microapp(
        '[NIV-019]',
        'Los 5 Niveles de Comunicación y Lenguaje Claro para Mayores',
        'Asistente interactivo para entender y redactar documentos complejos: cartas del banco con tecnicismos, informes médicos incomprensibles, notificaciones de la Seguridad Social o facturas de la luz. Enseña a usar la IA para traducir la jerga al lenguaje llano de la calle.',
        'Actúa como un experto en lenguaje claro y derechos del ciudadano mayor.\nExplícame en 3 pasos cómo hacer un traductor interactivo en HTML que transforme cartas bancarias y avisos médicos complicados en explicaciones sencillas.',
        'Genera el archivo HTML interactivo con un cuadro de texto donde pegar o seleccionar una carta formal confusa, y un botón que genere la versión en español claro, destacando lo urgente y los plazos.',
        '• Simulador de traducción: Ejemplos de cartas de banco, cartas de pensión y prospectos médicos con su versión "en lenguaje claro".\n• Guía para preguntar al médico en consulta: Lista de las 3 preguntas clave que todo paciente debe hacer.\n• Asistente de redacción: Modelo de reclamación sencilla para solicitar aclaraciones.',
        'SIMULADOR_COMUNICACION_LENGUAJE_SENIORS.html',
        'Guía Comunicación Médica y Bancaria (+65)'
    )

    add_senior_microapp(
        '[NIV-020]',
        'Los 6 Niveles de Creatividad, Curiosidad e Innovación Vital',
        'Laboratorio interactivo de estimulación creativa y proyectos vitales para la jubilación: escribir las memorias familiares, recuperar la pintura o la fotografía, iniciarse en la botánica o el huerto urbano, viajar con asociaciones culturales y mantenerse eternamente curioso.',
        'Actúa como un dinamizador cultural y mentor de proyectos de jubilación creativa.\nExplícame en 3 puntos cómo crear un explorador interactivo en HTML que despierte nuevas aficiones y proyectos creativos en personas mayores.',
        'Genera la aplicación interactiva en HTML con una "Rueda de Nuevas Pasiones", cuestionario de intereses (arte, escritura, naturaleza, tecnología) y plan de acción para arrancar un proyecto personal.',
        '• 6 Niveles de Creatividad: 1. Curiosidad latente, 2. Aprendizaje de un oficio o técnica, 3. Creación personal de obras o relatos, 4. Compartir con la comunidad o familia, 5. Proyectos colaborativos, 6. Legado cultural y vivencial.\n• Rueda de intereses: Sugerencias prácticas con talleres municipales y recursos gratuitos online.\n• Diario de ideas y proyectos ilusionantes para este mes.',
        'SIMULADOR_CREATIVIDAD_INNOVACION_SENIORS.html',
        'Diagnóstico Creatividad y Legado (+65)'
    )

    # =========================================================================
    # LOTE 3 (SESIONES 21 A 30): MICRO-APLICACIONES INTERACTIVAS SENIORS (+65)
    # =========================================================================
    add_senior_microapp(
        '[NIV-021]',
        'Los 7 Escalones de la Escala del Universo',
        'Micro-aplicación interactiva de perspectiva cósmica y serenidad cotidiana para personas mayores (+65). Permite recorrer los 7 órdenes de magnitud del universo: desde el mundo subatómico y las células biológicas, hasta la escala humana del hogar, los planetas y las galaxias, enseñando a relativizar las prisas y disfrutar del milagro de la vida.',
        'Actúa como un divulgador científico humanista y docente para personas mayores (+65).\nExplícame en 3 puntos cómo conectar la inmensidad de los 7 órdenes de magnitud del cosmos con la serenidad de la vida cotidiana en la jubilación, sin fórmulas matemáticas complejas.',
        'Genera en un único archivo HTML la aplicación completa: con diseño oscuro accesible, deslizador de zoom cósmico (potencias de 10), tipografía grande (17px), reflexiones de paz mental y sin tecnicismos en inglés.',
        '• 7 Escalones Cósmicos: 1. Reino Cuántico (Quarks y Planck), 2. El Átomo y las Moléculas del Agua, 3. La Célula Biológica y el ADN, 4. La Escala Humana y el Hogar (1m - 100m), 5. La Tierra y el Sistema Solar, 6. La Galaxia Vía Láctea, 7. El Universo Observable y Filamentos.\n• Controles: Selector de escalón (1 a 7), selector de potencias de 10 (-35 a +26) y conmutador de enfoque ("Cotidiano" vs. "Filosófico").\n• KPIs en tiempo real: Dimensión real, tiempo de viaje de la luz, metáfora familiar comprensible e índice de serenidad.\n• Filosofía senior: Enseña a valorar el momento presente frente a las preocupaciones efímeras.',
        'SIMULADOR_ESCALA_UNIVERSO_SENIORS.html',
        'Explorador Escala del Universo (+65)'
    )

    add_senior_microapp(
        '[NIV-022]',
        'Los 5 Niveles de Energía, Escala Kardashev y Consumo en el Hogar',
        'Herramienta interactiva pedagógica que conecta la evolución energética de la humanidad y la escala Kardashev (desde el fuego de leña hasta el dominio solar) con la optimización práctica del recibo de la luz en el hogar de los jubilados: ajuste de potencia contratada, horas valle y prevención de cobros abusivos.',
        'Actúa como un orientador energético y pedagogo cercano para personas mayores (+65).\nExplícame en 3 viñetas cómo ayudar a una persona mayor a entender su recibo de electricidad, ajustar la potencia y ahorrar sin pasar frío en invierno.',
        'Genera la aplicación interactiva en HTML con una escala de 5 niveles de civilización energética, simulador de potencia doméstica (kW), cálculo de ahorro anual en euros y consejos contra seguros innecesarios.',
        '• 5 Niveles Energéticos: 1. Biológico y Leña (la mesa camilla ancestral), 2. Fósil y Carbón (revolución industrial), 3. Red Eléctrica Actual (Tipo 0.73), 4. Dominio Planetario Limpio (Autoconsumo solar y fusión), 5. Dominio Estelar (Esfera de Dyson).\n• Calculadora doméstica: Potencia contratada (2.3 a 6.9 kW), porcentaje de uso en horas valle (lavadora/lavavajillas) y bombillas LED.\n• Métricas de ahorro: Factura mensual estimada en euros y cálculo de ahorro familiar anual (80 € a 180 €/año).\n• Escudo legal: Consejos para dar de baja servicios de mantenimiento no solicitados en la factura.',
        'SIMULADOR_ENERGIA_KARDASHEV_HOGAR_SENIORS.html',
        'Optimizador Energía y Kardashev (+65)'
    )

    add_senior_microapp(
        '[NIV-023]',
        'Los 7 Niveles de Temperatura en el Cosmos y Confort Térmico en el Hogar',
        'Termómetro comparativo interactivo desde los límites térmicos del cosmos hasta el confort del hogar senior: cómo regular el termostato a 21 °C para proteger el corazón, ahorrar un 7% por cada grado en la factura y prevenir la deshidratación y golpes de calor en verano.',
        'Actúa como un médico especialista en salud ambiental y geriatría preventiva.\nExplícame en 3 viñetas cómo diseñar un simulador que ayude a una persona mayor a mantener 21 °C en casa, ahorrar calefacción y proteger su tensión arterial.',
        'Genera el archivo HTML interactivo con un termómetro dinámico, semáforo de salud cardiovascular (frío vs calor), cálculo de desviación en la factura de calefacción y consejos estacionales.',
        '• 7 Niveles Térmicos: 1. Cero Absoluto (-273 °C), 2. Fondo Cósmico Espacial (-270 °C), 3. Ola de Frío Invernal (-5 °C a 5 °C), 4. Confort Térmico Saludable (19 °C a 22 °C, ideal 21 °C), 5. Ola de Calor Veraniega (38 °C a 44 °C), 6. Lava y Fotosfera Solar (1.200 °C a 5.500 °C), 7. Núcleo Solar y Supernovas (15 a 100 Millones °C).\n• Lógica médica: Alerta sobre vasoconstricción y subidas de tensión en invierno, y pérdida de sed en olas de calor veraniegas.\n• Desviación de gasto: Cada grado por encima de 21 °C en invierno encarece un 7% la factura.',
        'SIMULADOR_TEMPERATURA_CONFORT_HOGAR_SENIORS.html',
        'Termómetro Confort y Salud (+65)'
    )

    add_senior_microapp(
        '[NIV-024]',
        'Los 6 Niveles de Gravedad en el Cosmos, Equilibrio y Prevención de Caídas',
        'Simulador interactivo de gravedad cósmica y salud muscular: calcula el peso real del usuario en 6 mundos (Luna, Marte, Tierra, Júpiter...) y ofrece un plan de equilibrio, fuerza de cuádriceps y revisión del hogar para prevenir tropiezos y caídas en mayores.',
        'Actúa como un médico fisioterapeuta y divulgador científico para adultos mayores (+65).\nExplícame en 3 viñetas cómo estructurar una báscula cósmica que calcule el peso en otros planetas y enseñe ejercicios sencillos de equilibrio para casa.',
        'Crea la aplicación en HTML con un selector de peso en kg, visualizador de gravedad cósmica, el test de la silla (levantarse 5 veces) y checklist de seguridad en el hogar.',
        '• 6 Mundos Gravitatorios: 1. Microgravedad Orbital (0 g - Estación Espacial), 2. Luna (0.166 g), 3. Marte (0.38 g), 4. Tierra Estándar (1.0 g = 9.8 m/s²), 5. Júpiter (2.53 g), 6. Enana Blanca y Agujero Negro (> 300.000 g).\n• Báscula Cósmica: Calcula el peso exacto en cada astro al deslizar el peso corporal del usuario (45 a 110 kg).\n• Prevención de caídas: Ejercicio de la silla para fortalecer cuádriceps, zapatillas con suela antideslizante y fijación de alfombras con cinta de doble cara.',
        'SIMULADOR_GRAVEDAD_EQUILIBRIO_SENIORS.html',
        'Báscula Cósmica y Equilibrio (+65)'
    )

    add_senior_microapp(
        '[NIV-025]',
        'Los 5 Niveles de Velocidad en el Universo y el Elogio de la Lentitud Serena',
        'Herramienta interactiva de reflexión y salud cardiovascular: contrapone las velocidades vertiginosas del cosmos con el valor del paso humano consciente (4 km/h) en la jubilación, midiendo los beneficios del paseo diario y desterrando las prisas innecesarias.',
        'Actúa como un médico cardiólogo y filósofo humanista para personas mayores (+65).\nExplícame en 3 viñetas cómo estructurar una calculadora del paseo diario que mida distancia y minutos activos y fomente caminar sin prisas.',
        'Genera la aplicación interactiva en HTML con calculadora de pasos diarios (2.000 a 12.000), estimación de km y tiempo, comparador con 5 niveles de velocidad cósmica y reflexiones sobre el derecho a la calma.',
        '• 5 Niveles de Velocidad: 1. Deriva Tectónica Continental (3 cm/año), 2. El Paso Humano Consciente (4 km/h = 1.1 m/s), 3. Transporte Terrestre y Vehicular (50 a 120 km/h), 4. Velocidad de Escape y Sondas Espaciales (11 a 70 km/s), 5. La Velocidad de la Luz (300.000 km/s).\n• Calculadora del paseo: Conversión de pasos a kilómetros reales (zancada de 0.70 m) y minutos al aire libre.\n• Decálogo de la lentitud serena: No correr tras el autobús, saborear las comidas y pasear mirando el entorno.',
        'SIMULADOR_VELOCIDAD_RITMO_VIDA_SENIORS.html',
        'Simulador Velocidad y Calma (+65)'
    )

    add_senior_microapp(
        '[NIV-026]',
        'Los 6 Niveles del Espectro Electromagnético, Luz, Ondas y Salud',
        'Guía interactiva divulgativa y científica que disipa con rigor médico los bulos sobre las radiaciones: explica la diferencia entre ondas no ionizantes (radio, TV, Wi-Fi, móvil) 100% seguras y radiaciones ionizantes médicas, junto con pautas de iluminación y protección visual para seniors.',
        'Actúa como un médico oftalmólogo y físico divulgador para personas mayores (+65).\nExplícame en 3 viñetas cómo desmontar con ciencia tranquila el miedo al Wi-Fi y dar consejos prácticos de iluminación y cuidado de la vista en la madurez.',
        'Genera el código HTML interactivo con un selector de las 6 franjas del espectro, semáforo de seguridad (ionizante vs no ionizante), desmitificador de bulos y consejos de luz cálida nocturna para dormir bien.',
        '• 6 Franjas del Espectro: 1. Ondas de Radio, TV y Wi-Fi (No ionizante, totalmente segura), 2. Microondas (Calor molecular inofensivo), 3. Infrarrojo (Calor térmico reconfortante y fisioterapia), 4. Luz Visible (Iluminación óptima para lectura), 5. Ultravioleta (Vitamina D y protección con gafas UV400), 6. Rayos X y Gamma (Diagnóstico médico hospitalario regulado).\n• Detector de mitos: Certificación de la OMS sobre la inocuidad de las redes Wi-Fi y telefonía en el hogar.\n• Cuidado visual: Uso de bombillas LED cálidas (3000K) en el salón para no fatigar la vista.',
        'SIMULADOR_ESPECTRO_ELECTROMAGNETICO_SALUD_SENIORS.html',
        'Guía Espectro, Ondas y Salud (+65)'
    )

    add_senior_microapp(
        '[NIV-027]',
        'Los 5 Niveles del Tiempo: De los Segundos al Legado Familiar y la Edad Cósmica',
        'Micro-aplicación interactiva de perspectiva temporal y plenitud vital para personas mayores: calcula el tesoro de días vividos, latidos cardíacos y órbitas al Sol cumplidas, invitando a disfrutar del tiempo libre sin culpas y a transmitir vivencias a las nuevas generaciones.',
        'Actúa como un orientador vital y pedagogo humanista para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar una calculadora del tiempo vivido que valore los días y latidos cumplidos, y regale serenidad para saborear la jubilación sin prisas.',
        'Genera la aplicación en HTML con selector de edad (60 a 95 años), cálculo de días y latidos acumulados, comparador de 5 escalas temporales (del milisegundo a la edad cósmica) y reflexiones de plenitud.',
        '• 5 Escalas del Tiempo: 1. Instante Biológico y Sinapsis (Milisegundos), 2. Ciclo Circadiano y Día Solar (24 Horas), 3. Biografía Humana y Longevidad (80 a 100 Años), 4. Tiempo Geológico y Evolución (Millones de Años), 5. Tiempo Cósmico (13.800 Millones de Años).\n• Calculadora del Legado: Introduce los años cumplidos y muestra los días vividos (ej: 25.000 días), los latidos del corazón y las vueltas dadas al Sol.\n• Mensaje tranquilizador: El descanso y la contemplación en la jubilación son derechos ganados con honor tras décadas de trabajo.',
        'SIMULADOR_TIEMPO_LEGADO_SENIORS.html',
        'Calculadora de Tiempo y Legado (+65)'
    )

    add_senior_microapp(
        '[NIV-028]',
        'Los 6 Niveles de Presión Físico-Química, Clima y Tensión Arterial',
        'Simulador interactivo que une la física barométrica con la salud cardiovascular cotidiana: explica por qué las bajadas de presión antes de llover provocan molestias articulares reales y proporciona un tensiómetro interactivo con semáforo médico oficial para el control en casa.',
        'Actúa como un médico internista y divulgador meteorológico para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar un tensiómetro interactivo con semáforo médico y explicación científica clara de por qué nos duele la rodilla cuando cambia el tiempo.',
        'Genera el archivo HTML interactivo con deslizadores de tensión sistólica y diastólica en mmHg, semáforo de salud arterial, barómetro del clima y consejos para medirse la tensión correctamente.',
        '• 6 Niveles de Presión: 1. Vacío Intergaláctico (0 Atm), 2. Presión Atmosférica Terrestre (1 Atm = 1.013 hPa = 760 mmHg), 3. Borrascas y Dolores Articulares (Meteoropatía con 985 hPa), 4. Presión en Olla Express Doméstica (2 a 3 Atm), 5. Fosa Abisal de las Marianas (1.100 Atm), 6. Presión Cuántica en Estrellas de Neutrones (> 10²⁸ Atm).\n• Tensiómetro interactivo: Evaluación médica de valores sistólicos y diastólicos (Óptima < 120/80, Normal < 130/85, Seguimiento < 140/90, Consulta > 140/90).\n• Pautas médicas: Medir la tensión sentados, en silencio tras 5 minutos de reposo, y cocinar con especias para reducir la sal.',
        'SIMULADOR_PRESION_CLIMA_TENSION_SENIORS.html',
        'Tensiómetro y Presión Barométrica (+65)'
    )

    add_senior_microapp(
        '[NIV-029]',
        'Los 5 Estados de la Materia, el Ciclo del Agua y la Hidratación Saludable',
        'Herramienta interactiva de divulgación física y salud nutricional: explica los 5 estados de la materia (sólido, líquido, gas, plasma y condensado) y establece un planificador diario de hidratación pautada para personas mayores, superando la pérdida biológica de la sensación de sed.',
        'Actúa como un médico nefrólogo y divulgador de ciencias naturales para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar un contador de vasos de agua que ayude a prevenir mareos y cuide los riñones en la madurez.',
        'Genera la aplicación interactiva en HTML con contador de vasos diarios (litros totales), semáforo de función renal y lucidez mental, comparador de los 5 estados físicos y pauta horaria de consumo de líquidos.',
        '• 5 Estados de la Materia: 1. Condensado Cuántico Bose-Einstein (Frío extremo cuántico), 2. Estado Sólido Cristalino (Hielo, minerales y huesos), 3. Estado Líquido Fluido (El agua de la vida y la sangre), 4. Estado Gaseoso Expansivo (Vapor, aire y respiración), 5. Estado Plasma Ionizado (El Sol y relámpagos).\n• Planificador de hidratación: Contador de 1 a 10 vasos diarios (1.5L a 2.0L recomendados) con diagnóstico de alerta mental y salud renal.\n• Alerta médica para mayores: Explicación de por qué los osmorreceptores atenúan la sed en la madurez y la necesidad de beber agua de forma pautada.',
        'SIMULADOR_ESTADOS_MATERIA_HIDRATACION_SENIORS.html',
        'Planificador de Hidratación y Materia (+65)'
    )

    add_senior_microapp(
        '[NIV-030]',
        'Los 6 Niveles de Radioactividad, Pruebas Médicas y Tranquilidad Senior',
        'Comparador interactivo y tranquilizador de dosis de radiación: desmitifica con ciencia rigurosa el miedo a las pruebas médicas de rayos X y TAC, demostrando que una radiografía equivale a unos pocos días de vida natural en la Tierra y aporta un inmenso beneficio diagnóstico para la salud.',
        'Actúa como un médico especialista en radiología y pedagogía sanitaria para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar un comparador en microSieverts que tranquilice a una persona mayor y desmitifique el miedo infundado a las pruebas médicas de rayos X.',
        'Genera la aplicación interactiva en HTML con selector de los 6 niveles de radiación, comparador de dosis en microSieverts (µSv), equivalencia en días de vida cotidiana en la naturaleza y mensajes de confianza médica.',
        '• 6 Niveles de Radiación: 1. Fondo Natural y Alimentos (0.1 µSv por plátano / 2.4 mSv al año en la Tierra), 2. Vuelos en Avión y Radiación Cósmica (20 a 40 µSv por vuelo transatlántico), 3. Radiografías de Diagnóstico Médico (5 a 20 µSv en tórax o dental), 4. Tomografía Computarizada (TAC) (3 a 6 mSv supervisados), 5. Radioterapia Oncológica Dirigida (Tratamiento curativo de precisión), 6. Accidentes Industriales Nucleares (> 1.000 mSv, Chernóbil / no aplicable a medicina).\n• Comparador en microSieverts: Una radiografía de tórax (20 µSv) equivale a solo 3 días paseando por el campo.\n• Tranquilidad sanitaria: Mensaje claro para no aplazar ni rechazar placas recetadas por el médico.',
        'SIMULADOR_RADIOACTIVIDAD_MEDICINA_SENIORS.html',
        'Comparador de Radiación y Medicina (+65)'
    )

    # GRUPO D: ESCALAS Y NIVELES DEL MUNDO BIOLÓGICO Y ECOLÓGICO (NIV-031 a NIV-040)
    add_it('[NIV-031]', 'Los 6 Estratos de Profundidad del Océano y Adaptación',
           'Viaje batimétrico por zonas marinas desde la epipelágica fótica superficial hasta la batipelágica bioluminiscente, abisal helada y quimiotróficos hadales.',
           6, 'Un batiscafo de exploración oceanográfica en 3D de esfera de titanio amarillo con potentes focos LED iluminando un calamar gigante abisal.',
           [
               ("Zona Epipelágica - Luz Solar (0 a 200 metros)", "El océano superficial y cálido bañado por el sol donde abunda el fitoplancton, los arrecifes de coral coloridos, delfines y tiburones veloces."),
               ("Zona Mesopelágica - Penumbra (200 a 1.000 metros)", "El reino de las sombras del atardecer perpetuo donde viven el pez espada, calamares y bancos de krill realizando migraciones verticales diarias."),
               ("Zona Batipelágica - Oscuridad (1.000 a 4.000 metros)", "Tiniebla absoluta donde los peces lucio y rape abisal encienden señuelos de bioluminiscencia química para atraer presas con dientes afilados."),
               ("Zona Abisopelágica - Abismo Helado (4.000 a 6.000 metros)", "El inmenso fondo fangoso marino cubierto por nieve marina orgánica, habitado por pepinos de mar y arañas marinas gigantes."),
               ("Zona Hadal - Fosas de las Marianas (6.000 a 11.000 metros)", "Las trincheras tectónicas más profundas de la Tierra en una oscuridad congelada y bajo 1.100 atmósferas de presión brutal."),
               ("Ecosistemas Quimiotróficos de Chimeneas Térmicas", "Gusanos tubo gigantes de 2 metros de largo prosperando en total ausencia de sol, alimentándose de azufre y calor volcánico en las profundidades.")
           ],
           'Dibuja en el Peldaño 3 un pez abisal con una linterna brillante en su cabeza atrayendo pececillos con textos en castellano.')

    add_it('[NIV-032]', 'Los 5 Niveles de Organización Ecológica (Trofo-Dinámica)',
           'Cadena alimentaria y flujo de energía según la Ley del 10% desde productores primarios fotosintéticos hasta herbívoros, superdepredadores ápice y descomponedores.',
           5, 'Un águila imperial dorada majestuosa en 3D con las alas desplegadas en la cúspide de una pirámide verde viva repleta de vegetación y mamíferos en equilibrio.',
           [
               ("Productores Primarios Fotosintéticos", "Praderas frondosas, bosques densos y fitoplancton marino capturando la energía solar para sintetizar materia orgánica alimentaria viva."),
               ("Herbívoros y Consumidores Primarios", "Ciervos, cebras, orugas y conejos alimentándose directamente de plantas y convirtiendo la celulosa vegetal en proteína animal accesible."),
               ("Depredadores Secundarios (Carnívoros Pequeños)", "Zorros veloces, ranas insectívoras, aves rapaces medianas y halcones que controlan las poblaciones de roedores e insectos herbívoros."),
               ("Superdepredadores Ápice (La Cúspide Trófica)", "Leones en la sabana, lobos pardos en el bosque, orcas en el mar y águilas calvas regulando el equilibrio general de todo el ecosistema desde lo alto."),
               ("Descomponedores y Recicladores del Suelo", "Hongos de sombrero, lombrices de tierra y bacterias invisibles que descomponen los restos orgánicos devolviendo minerales puros al suelo forestal para iniciar el ciclo.")
           ],
           'Ilustra en el Peldaño 5 hongos coloridos y lombrices trabajando el suelo fértil oscuro con rótulos en español.')

    add_it('[NIV-033]', 'Los 6 Niveles de Organización Biológica Celular',
           'Jerarquía biológica pluricelular desde la biomolécula inerte y el organelo mitocondrial hasta células especializadas, tejidos, órganos y sistemas completos.',
           6, 'Una figura anatómica humana translúcida y deportiva en 3D en la cima, revelando en su interior engranajes relucientes de su corazón, redes vasculares y células en armonía.',
           [
               ("Biomoléculas y Átomo de Carbono", "El armazón de proteínas, fosfolípidos, azúcares y nucleótidos de ADN formados por átomos de carbono, hidrógeno y oxígeno enlazados."),
               ("Organelo Celular (La Central Energética)", "La mitocondria celular respirando y quemando glucosa con oxígeno para fabricar moléculas de ATP que dan energía pura al organismo."),
               ("Célula Especializada y Membrana", "Una neurona estrellada, un glóbulo rojo bicóncavo o una célula muscular estriada, siendo la unidad mínima dotada de vida autónoma."),
               ("Tejido Biológico Cohesivo", "Millones de células especializadas idénticas unidas firmemente para formar el tejido óseo resistente, el músculo cardíaco o la piel protectora."),
               ("Órgano Funcional Especializado", "El corazón palpitando como bomba muscular doble o el estómago segregando ácidos para cumplir una función vital concreta en el cuerpo."),
               ("Sistema o Aparato Corporal Completo", "El sistema cardiovascular completo de corazón, arterias, venas y capilares transportando oxígeno y nutrientes a los 30 billones de células de una persona.")
           ],
           'Dibuja en el Peldaño 2 una mitocondria brillante de color naranja cortada por la mitad mostrando sus pliegues internos con rótulos en castellano.')

    add_it('[NIV-034]', 'Los 5 Niveles de Longevidad Biológica y Envejecimiento',
           'Esperanza de vida evolutiva desde efímeras insectiles de 24 horas y ratones veloces hasta humanos centenarios de Zonas Azules y medusas biológicamente inmortales.',
           5, 'El árbol de la vida milenario en 3D cuyas raíces doradas se enlazan con un reloj de arena cósmico, simbolizando la extensión biológica celular.',
           [
               ("Vida Efímera Ultracorta (Horas a Días)", "El insecto efímera eclosionando del agua, volando, reproduciéndose al atardecer y muriendo en menos de 24 horas continuas sin boca para comer."),
               ("Metabolismo Veloz y Vida Corta (2 a 10 Años)", "Ratones de campo, colibríes de altísima frecuencia cardíaca y perros que viven intensamente quemando su energía metabólica en una década."),
               ("Longevidad Humana y Centenarios (80 a 110 Años)", "Seres humanos ancianos y sabios en las Zonas Azules manteniendo agilidad y salud mental gracias a dieta comunitaria y movimiento activo."),
               ("Gigantes Marinos y Matusalenes (200 a 400 Años)", "La ballena de Groenlandia y el tiburón de Groenlandia nadando lentamente en aguas árticas heladas con metabolismos pausados y células súper-reparadoras."),
               ("Inmortalidad Biológica (Reversión Celular)", "La pequeña medusa Turritopsis dohrnii que, al envejecer o ser dañada, revierte sus células adultas de nuevo a estado de pólipo juvenil reanudando su vida indefinidamente.")
           ],
           'Ilustra en el Peldaño 4 un gran tiburón de Groenlandia nadando pacíficamente entre bloques de hielo azul marino con textos en castellano.')

    add_it('[NIV-035]', 'Los 6 Estratos de Altura en el Bosque Tropical',
           'Estratificación de la biodiversidad en selvas pluviales luchando por luz solar desde el suelo fúngico al subbosque, dosel principal y ceibas emergentes de 60m.',
           6, 'Una gran ceiba amazónica gigantesca en 3D cortada en sección vertical, mostrando desde sus raíces tabulares subterráneas de micelio hasta la copa superior dorada bañada por el sol.',
           [
               ("Suelo Forestal y Red de Micelio (0 a 1 metro)", "El suelo oscuro y húmedo alfombrado por hojarasca en descomposición, donde escarabajos, tapires y millones de hongos reciclan los nutrientes en silencio."),
               ("Subbosque de Arbustos y Helechos (1 a 5 metros)", "Plantas de grandes hojas anchas evolucionadas para capturar los escasos rayos de sol que logran filtrarse, hogar de jaguares y ranas venenosas."),
               ("Dosel Inferior y Lianas (5 a 20 metros)", "El estrato intermedio repleto de troncos jóvenes y lianas leñosas retorcidas por donde trepan ágilmente osos hormigueros, serpientes boa y monos nocturnos."),
               ("Dosel Principal Continuo (20 a 40 metros)", "El techo verde denso y entrelazado del bosque donde florece el 80% de la vida selvática con tucanes coloridos, monos aulladores, perezosos y orquídeas epífitas."),
               ("Árboles Emergentes Gigantes (40 a 60 metros)", "Las torres solitarias de ceibas y castaños superando el techo forestal para recibir el viento fuerte y el sol directo, nido del águila arpía."),
               ("Atmósfera Superior y Lluvia de Transpiración", "La nube de vapor de agua y oxígeno puro que los millones de hojas forestales liberan al cielo ecuatorial, creando los ríos voladores del planeta.")
           ],
           'Dibuja en el Peldaño 4 un perezoso simpático colgando boca abajo de una rama verde al lado de un tucán de pico naranja con rótulos en español.')

    add_it('[NIV-036]', 'Los 5 Niveles de Toxicidad y Veneno Biológico',
           'Armas bioquímicas naturales desde los pelos urticantes leves defensivos hasta hemotoxinas de víbora, neurotoxinas paralizantes y batracotoxina letal instantánea.',
           5, 'Una gota de veneno cristalina y verde esmeralda en 3D cayendo sobre un modelo molecular celular, ilustrando la precisión bio-quirúrgica de las toxinas.',
           [
               ("Irritantes Leves y Pelo Urticante", "Orugas difusas y ortigas liberando ácido fórmico en la piel de los depredadores para causar picor molesto y una advertencia clara de no tocar."),
               ("Hemotoxinas Coagulantes y Destructoras", "Víboras cascabel inyectando veneno por colmillos huecos que destruye los glóbulos rojos, rompe capilares y causa inflamación severa."),
               ("Citotoxinas Necróticas Celulares", "Arañas reclusa parda o violinista cuyo veneno disuelve localmente el tejido celular en el punto de picadura mediante enzimas digestivas potentes."),
               ("Neurotoxinas Bloqueadoras Sinápticas", "Cobras reales, mambas negras y pulpos de anillos azules disparando péptidos que paralizan el sistema nervioso muscular impidiendo la respiración instantáneamente."),
               ("Toxinas Letales Instantáneas de Contacto", "La pequeña rana dorada venenosa de Colombia cuya secreción cutánea de batracotoxina pura puede detener el corazón de 10 hombres adultos con un solo roce.")
           ],
           'Ilustra en el Peldaño 5 una pequeña rana amarilla brillante sobre una hoja verde húmeda del bosque con textos en castellano estricto.')

    add_it('[NIV-037]', 'Los 6 Niveles de Adaptación Térmica Biológica',
           'Termorregulación biológica desde la ectotermia reptiliana y endotermia caliente hasta la hibernación, estivación, tardígrados en criptobiosis e hipertermófilos.',
           6, 'Un escudo térmico biológico en 3D mitad hielo ártico azul brillante y mitad fuego volcánico rojo ardiente, representando la resiliencia en todos los climas.',
           [
               ("Ectotermia y Sangre Fría (Reptiles)", "Lagartos y serpientes tomando el sol matutino sobre rocas calientes para elevar su temperatura corporal inerte y poder moverse a cazar presas veloces."),
               ("Endotermia y Sangre Caliente (Mamíferos y Aves)", "Pingüinos antárticos y osos polares generando calor metabólico interno constante a 37 °C abrigados con grasa gruesa y capas de plumas aislantes impermeables."),
               ("Hibernación Metabólica Invernal", "Osos pardos y marmotas bajando sus latidos a 5 pulsaciones por minuto y durmiendo 5 meses dentro de cuevas nevadas consumiendo su reserva de grasa invernal."),
               ("Estivación y Tolerancia al Desierto", "Caracoles del desierto y peces pulmonados enterrándose en barro seco durante meses calurosos sin agua, sellando su concha para evitar deshidratación total."),
               ("Criptobiosis y Animación Suspendida (Tardígrados)", "El minúsculo oso de agua perdiendo el 99% de su agua interior y cristalizando sus proteínas para sobrevivir al vacío espacial y a -200 °C de temperatura cósmica."),
               ("Hipertermófilos en Calderas Volcánicas", "Arqueobacterias extremófilas prosperando felices en estanques de ácido hirviendo a 120 °C del Parque Yellowstone, con enzimas súper-estables termo-resistentes.")
           ],
           'Dibuja en el Peldaño 5 un tardígrado simpático microscópico flotando en su cápsula protectora redonda con rótulos en castellano.')

    add_it('[NIV-038]', 'Los 5 Niveles de Fuerza y Capacidad de Carga Animal',
           'Biomecánica muscular de fuerza absoluta en grandes paquidermos y gorilas frente al prodigio de la fuerza relativa récord en hormigas y escarabajo hércules.',
           5, 'Un escarabajo hércules gigante en 3D sosteniendo en sus cuernos robustos una pesa dorada descomunal, simbolizando el prodigio biomecánico en la escala minúscula.',
           [
               ("Fuerza Absoluta Colosal (El Elefante Africano)", "Un mamut o elefante adulto levantando troncos de árboles de 300 kilos con su trompa muscular y empujando obstáculos pesados en la selva."),
               ("Fuerza Muscular en Primates (El Gorila Espalda Plateada)", "Un macho gorila de 200 kilos destrozando ramas de bambú gruesas con una fuerza en sus brazos 6 veces superior a la de un levantador olímpico humano."),
               ("Potencia Aerodinámica y Carga (El Águila Arpía)", "Una rapaz amazónica con garras del tamaño de las de un oso pardo arrancando a un mono o perezoso pesado de las ramas del árbol en vuelo directo."),
               ("Fuerza Relativa Asombrosa (La Hormiga Tejedora)", "Una hormiga obrera minúscula levantando con sus mandíbulas una hoja verde o una presa que pesa 50 veces más que su propio cuerpo esbelto."),
               ("El Récord Biológico de Tracción (Escarabajo Hércules y Pelotero)", "Un escarabajo con cuernos de coraza empujando o levantando cargas equivalentes a 850 veces su propio peso corporal sin sufrir daño estructural en su exoesqueleto.")
           ],
           'Ilustra en el Peldaño 4 una hormiga roja levantando una hoja verde gigante sobre su cabeza con textos en español castellano.')

    add_it('[NIV-039]', 'Los 6 Niveles de Camuflaje y Cripsis en la Naturaleza',
           'Invisibilidad biológica por homocromía estacional, rayas disruptivas, mimetismo de hoja, cripsis de textura y camuflaje neuronal instantáneo de cromatóforos en pulpos.',
           6, 'Un pulpo mímico de arrecife en 3D transformando la mitad izquierda de su piel en roca rugosa grisácea y su mitad derecha en coral rojo brillante.',
           [
               ("Mimetismo de Color Simple (Homocromía)", "Una liebre ártica o zorro de las nieves cambiando su pelaje marrón de verano por un manto blanco inmaculado al llegar las primeras nevadas del invierno."),
               ("Contraste Disruptivo de Contornos", "Las rayas blancas y negras de una cebra deslumbrando al león en la sabana y rompiendo la silueta individual del cuerpo cuando corre en manada."),
               ("Mimetismo de Forma (Hoja y Rama)", "El insecto palo inmóvil como una ramita seca y el insecto hoja imitando las nervaduras verdosas de un arbusto de la selva para ser invisible."),
               ("Cripsis de Textura y Rugosidad Corporal", "El pez piedra o lagarto diablo espinoso cuya piel rugosa llena de bultos parece un trozo exacto de roca volcánica o coral muerto cubierto de algas."),
               ("Aposematismo y Falso Engaño Mímico (Batesiano)", "La mosca cernícalo inofensiva imitando las rayas amarillas y negras de una avispa venenosa para asustar a los pájaros depredadores sin tener aguijón real."),
               ("Camuflaje Óptico Activo en Tiempo Real (Cefalópodos)", "Pulpos y sepias contrayendo millones de sacos de color cromatóforos bajo el mando directo de su cerebro para cambiar de color y textura en 200 milisegundos.")
           ],
           'Dibuja en el Peldaño 3 un insecto hoja de color verde esmeralda idéntico a la hoja del árbol en el que está posado con textos en castellano.')

    add_it('[NIV-040]', 'Los 5 Niveles de Regeneración Celular en el Reino Animal',
           'Capacidad biológica regenerativa desde la cicatrización fibrosa humana y crecimiento hepático hasta la regeneración de extremidades en ajolote y planaria total.',
           5, 'Un ajolote mexicano rosado en 3D en el centro regenerando su pata delantera y sus branquias plumosas con destellos de luz celular dorada resplandeciente.',
           [
               ("Cicatrización Superficial y Fibrosis (Ser Humano)", "La piel humana curando un corte epidérmico mediante coágulo de plaquetas y costra, dejando una cicatriz de colágeno fibroso sin regenerar folículos ni sudor."),
               ("Regeneración Hepática y Ósea (Poder Oculto Humano)", "El hígado humano regenerando hasta el 70% de su masa perdida tras una cirugía gracias al crecimiento celular compensatorio en un par de semanas."),
               ("Regeneración de Colas y Extremidades Simples", "La lagartija o salamanquesa desprendiendo voluntariamente su cola para distraer al halcón depredador y haciendo crecer una nueva cola ósea en dos meses."),
               ("Regeneración de Órganos Complejos y Cerebro (Ajolote y Pez Cebra)", "El ajolote reconstruyendo una pata amputada completa con huesos, músculos, nervios y hasta partes cortadas de su propio corazón o médula espinal."),
               ("Regeneración Corporal Total desde Fragmentos (Planaria y Estrella de Mar)", "El gusano planaria cortado en 10 trozos diminutos, donde cada trocito regenera por completo una cabeza, ojos y cuerpo de un animal entero funcional.")
           ],
           'Ilustra en el Peldaño 4 al simpático ajolote mexicano rosado sonriendo bajo el agua limpia con rótulos exactos en español.')

    # GRUPO E: TECNOLOGÍA, COMPUTACIÓN E INMERSIÓN (NIV-041 a NIV-050)
    add_it('[NIV-041]', 'Los 6 Niveles de Conectividad y Velocidad Digital',
           'Evolución de telecomunicaciones desde el módem telefónico analógico de los 90, ADSL, fibra óptica y 5G hasta satélites Starlink LEO y la inminente red cuántica fotónica.',
           6, 'Un cable de fibra óptica cuántica tridimensional con el núcleo brillante de pura luz azul deslumbrante enviando terabits instantáneos a un satélite orbital.',
           [
               ("Módem Telefónico Analógico 56 kbps (Años 90)", "Un viejo ordenador de escritorio emitiendo el característico pitido electrónico al conectar por cable de cobre telefónico tardando minutos en abrir una foto."),
               ("Banda Ancha ADSL y Cable de Cobre (Años 2000)", "Hogares conectados sin bloquear la línea de teléfono fija, permitiendo las primeras descargas de canciones MP3 y navegación fluida por páginas web."),
               ("Fibra Óptica hasta el Hogar - FTTH (1 Gbps)", "Haces fotónicos viajando por filamentos de vidrio purísimo a la velocidad de la luz permitiendo videollamadas 4K sin interrupciones ni latencia percibida."),
               ("Red Móvil Celular 5G Masiva (Conectividad Total)", "Antenas urbanas inteligentes conectando millones de sensores, coches autónomos, farolas y teléfonos móviles simultáneamente con latencia de un milisegundo."),
               ("Constelaciones Orbitales por Satélite (Starlink / LEO)", "Miles de pequeños satélites en órbita baja interconectados con rayos láser en el vacío espacial dando internet veloz a la selva más remota y mitad del océano."),
               ("Internet Cuántico y Enredo Fotónico (El Futuro Infranqueable)", "Redes que transmiten información cuántica instantánea inhackeable mediante fotones entrelazados donde cualquier intento de espionaje destruye la señal al momento.")
           ],
           'Dibuja en el Peldaño 5 una red de satélites girando alrededor del globo terráqueo azul con rayos de luz y rótulos en castellano.')

    add_it('[NIV-042]', 'Los 5 Niveles de Ciberseguridad y Blindaje Informático',
           'Protección de datos y redes desde contraseñas simples vulnerables, cifrado SSL HTTPS y autenticación biométrica 2FA hasta enclaves de hardware TPM y post-cuántica.',
           5, 'Un candado de seguridad cibernética en 3D forjado en titanio plateado con un escáner biométrico de iris brillante en su centro, bloqueando un ataque de virus rojos.',
           [
               ("Contraseña Simple en Texto Plano (Peligro Crítico)", "Un usuario escribiendo palabras vulnerables como 123456 o el nombre de su mascota en una web sin cifrar, fácilmente interceptadas por hackers basales."),
               ("Cifrado Simétrico y Conexión Segura (SSL / HTTPS)", "El candado verde en la barra del navegador que encripta la comunicación entre tu ordenador y el banco usando algoritmos matemáticos estándar."),
               ("Autenticación Multifactor Biométrica (2FA)", "Verificación de seguridad en dos pasos combinando algo que sabes (contraseña), algo que tienes (teléfono móvil) y algo que eres (huella dactilar o rostro)."),
               ("Enclaves de Hardware Seguros (Chip TPM / Encriptación Total)", "Procesadores con una cámara acorazada física independiente aislada del resto del ordenador donde se guardan claves de cifrado inalcanzables por virus."),
               ("Criptografía Post-Cuántica e Inmutabilidad (Blockchain Segura)", "Algoritmos matemáticos ultra-robustos diseñados específicamente para resistir el descifrado masivo por supercomputadoras cuánticas del futuro.")
           ],
           'Ilustra en el Peldaño 3 un teléfono móvil mostrando una huella dactilar verde brillante en la pantalla con textos en castellano.')

    add_it('[NIV-043]', 'Los 6 Niveles de Resolución Visual e Imagen Digital',
           'Evolución de pantallas desde el píxel primitivo 8-bit de tubo CRT de los 80, definición analógica SD, Full-HD y 4K hasta 8K inmersivo y pantallas retina 16K.',
           6, 'Un ojo humano fotorrealista en 3D mirando a través de una lente cristalina que enfoca y transforma un mosaico de grandes píxeles cuadrados en una imagen 8K perfecta.',
           [
               ("Píxel Gráfico Primitivo 8-Bit (Años 80)", "Videojuegos clásicos retro con personajes formados por bloques cuadrados visibles multicolor en monitores de tubo CRT con líneas de escaneo palpables."),
               ("Definición Estándar SD - 480p (Televisión Analógica)", "La calidad de imagen del VHS y las emisiones de televisión de los años 90 en pantallas cuadradas de relación de aspecto 4:3."),
               ("Alta Definición Full-HD 1080p (El Estándar Digital)", "Televisores planos panorámicos 16:9 y discos Blu-ray revelando por primera vez detalles precisos de textura, gotas de sudor y cabello en películas de cine."),
               ("Ultra-HD 4K Cinematográfico (8 Millones de Píxeles)", "El estándar de las plataformas de streaming actuales y cámaras profesionales, mostrando colores HDR profundos y nitidez milimétrica en grandes pantallas modernas."),
               ("Resolución 8K e Inmersión Total (33 Millones de Píxeles)", "Paneles hiper-densos donde los píxeles individuales son tan diminutos que el ojo humano no puede distinguirlos ni pegando la nariz a la pantalla."),
               ("Resolución Retina Microscópica y Holografía 16K", "La barrera biológica final del nervio óptico humano en gafas de realidad mixta donde la luz digital se funde de manera absoluta con la percepción real.")
           ],
           'Añade en el Peldaño 1 un personaje de videojuego clásico de bloques tipo pixel-art con rótulos en castellano.')

    add_it('[NIV-044]', 'Los 5 Niveles del Almacenamiento de Información Humana',
           'Retención del conocimiento histórico desde tablillas de arcilla, pergaminos, tarjetas perforadas mecánicas y discos duros HDD/SSD flash hasta almacenamiento biológico de ADN molecular.',
           5, 'Un microchip SSD moderno en 3D del cual emerge una doble hélice de ADN brillante y luminosa, mostrando la convergencia entre silicio y densidad biológica.',
           [
               ("Tablilla de Arcilla y Pergamino Físico", "Escribas antiguos grabando caracteres cuneiformes en arcilla húmeda o monjes copiando códices a mano en monasterios con durabilidad física limitada."),
               ("Tarjetas Perforadas de Papel (Inicios del Siglo XX)", "Las primeras computadoras electromecánicas leyendo agujeros perforados en cartulinas de cartón para procesar los censos de población de 1900."),
               ("Discos Magnéticos Mecánicos (HDD y Cintas de Carretes)", "Carretes giratorios de cintas magnéticas de los 60 y discos duros con agujas lectoras microscópicas almacenando megabytes y gigabytes girando a miles de revoluciones."),
               ("Memoria Flash de Estado Sólido (SSD y NVMe)", "Chips de silicio sin piezas móviles que guardan terabytes de datos al instante mediante impulsos eléctricos en compuertas microscópicas en teléfonos y portátiles veloces."),
               ("Almacenamiento Biológico en ADN Molecular", "Ingeniería biotecnológica que codifica todos los libros, música y películas de la humanidad en los 4 pares de bases moleculares del ADN humano dentro de una probeta.")
           ],
           'Ilustra en el Peldaño 3 un disco duro antiguo con su aguja de lectura metálica brillante y textos en español.')

    add_it('[NIV-045]', 'Los 6 Niveles de Miniaturización del Transistor y Ley de Moore',
           'Evolución del interruptor electrónico desde la gran válvula de vacío caliente de los años 40, el transistor discreto y circuito integrado hasta compuertas FinFET 2nm y límite cuántico atómico.',
           6, 'Una lupa de nanotecnología en 3D enfocando sobre la cabeza de un alfiler de metal para mostrar millones de transistores de silicio fotolitografiados por láser EUV.',
           [
               ("Válvula de Vacío de Vidrio (Años 40 - ENIAC)", "Tubos de cristal calientes del tamaño de bombillas que consumían electricidad masiva y se fundían constantemente en el primer ordenador gigante del mundo."),
               ("Transistor de Silicio Discreto (1947 - Bell Labs)", "El primer interruptor semiconductor sólido de tres patas de alambre metálico que reemplazó a las frágiles válvulas revolucionando la electrónica portátil del siglo XX."),
               ("El Circuito Integrado de Silicio - Microchip (Años 70)", "El microprocesador 4004 de Intel empaquetando 2.300 transistores juntos en una pastilla milimétrica para impulsar las primeras calculadoras y ordenadores de hogar."),
               ("Litografía en Nanómetros - 14 nm a 7 nm (Años 2010)", "Miles de millones de transistores microscópicos empaquetados en cada chip de smartphone con compuertas tridimensionales FinFET ultra-eficientes."),
               ("Microarquitectura de 2 Nanómetros (El Presente Límite)", "Transistores tan inconcebiblemente diminutos que el grosor de su compuerta es de apenas unas docenas de átomos de silicio ordenados por láser EUV."),
               ("El Límite Cuántico Atómico y Electrónica Molecular", "La barrera física insuperable donde los electrones saltan por efecto túnel cuántico entre átomos, obligando al paso inevitable a la computación cuántica fotónica.")
           ],
           'Dibuja en el Peldaño 1 una gran válvula de vidrio antigua encendida con luz naranja caliente y rótulos en castellano.')

    add_it('[NIV-046]', 'Los 5 Niveles de la Robótica y Autonomía Mecánica',
           'Autonomía de máquinas de movimiento desde autómatas mecánicos de cuerda sin sensores y brazos industriales de cadena de montaje hasta humanoides bípedos adaptativos y enjambres IA.',
           5, 'Un robot humanoide blanco y elegante en 3D de articulaciones ágiles y rostro con visor LED azul, caminando con perfecto equilibrio dinámico por escaleras del mundo real.',
           [
               ("Autómata de Relojería y Engranajes (Siglo XVIII)", "Muñecos mecánicos clásicos de cuerda y levas de madera que escribían notas o tocaban instrumentos con trayectorias estrictamente pre-grabadas sin visión."),
               ("Brazo Industrial Programado de Cadenas de Montaje", "Robots amarillos pesados en fábricas de coches repitiendo soldaduras a milímetro exacto en jaulas de seguridad aisladas para no dañar a trabajadores cercanos."),
               ("Robot Móvil con Sensores LiDAR y Navegación (AGV)", "Robots aspiradores y carretillas autónomas de almacenes que escanean la habitación con rayos láser por infrarrojos para trazar mapas y esquivar obstáculos."),
               ("Robot Humanoide Adaptativo Bi-pedal (Atlas / Optimus)", "Máquinas de piernas y brazos antropomórficos manteniendo equilibrio dinámico ante empujones, subiendo escaleras y utilizando herramientas con manos de 5 dedos."),
               ("Enjambres Robóticos Autónomos con IA Distributiva", "Cientos de drones y robots coordinándose en red sin un control centralizado como un bando de pájaros para construir puentes o rescatar víctimas.")
           ],
           'Ilustra en el Peldaño 4 un robot humanoide blanco recogiendo suavemente una manzana roja con su mano articulada en castellano.')

    add_it('[NIV-047]', 'Los 6 Niveles de Inmersión Virtual y Realidad Extendida (XR)',
           'Interfaz con mundos digitales desde pantalla 2D plana tradicional, gafas 3D anaglifo, cascos VR cerrados inmersivos, Realidad Mixta passthrough y lentillas de retina hasta conexión BCI neuronal directa.',
           6, 'Unas gafas de realidad mixta futuristas en 3D flotando en el centro proyectando hologramas luminosos interactivos de planetas flotando en medio del salón de una casa real.',
           [
               ("Pantalla Plana Bidimensional 2D (El Monitor Estándar)", "El usuario sentado frente al rectángulo de cristal de un ordenador o televisión mirando mundos virtuales a través de un marco delimitado sin profundidad real."),
               ("Gafas Estereoscópicas 3D de Cine (Anaglifo y Polarizado)", "Lentes con filtros rojos/azules o polarizados que engañan a cada ojo enviando imágenes ligeramente desplazadas para dar ilusión de relieve emergente en el cine."),
               ("Realidad Virtual Inmersiva de Casco - VR (6DoF)", "El usuario con un visor cerrado que bloquea la luz exterior rodeado en 360 grados por un mundo digital artificial con mandos de movimiento en las manos."),
               ("Realidad Mixta y Passthrough Fotorrealista (MR / AR)", "Cámaras de ultra-alta definición en el visor capturando el salón real del usuario y superponiendo hologramas digitales interactivos anclados en su mesa de trabajo."),
               ("Lentillas Inteligentes de Retina Holográfica (Sin Gafas)", "Micro-lentes oculares transparentes imperceptibles que proyectan fotones directamente en la mácula ocular con información continua y traducción instantánea."),
               ("Interfaz Cerebro-Computadora Directa (Inmersión Neuronal)", "Conexión cortical por bio-sensores sin pantalla donde el cerebro experimenta mundos virtuales enviando tacto, olor y sonido directamente a la corteza sensorial.")
           ],
           'Dibuja en el Peldaño 4 un joven con gafas futuristas tocando con su mano un planeta Saturno holográfico flotante en castellano.')

    add_it('[NIV-048]', 'Los 5 Niveles de Eficiencia Termodinámica y Energética en Motores',
           'Conversión de energía en trabajo mecánico desde la máquina de vapor del siglo XVIII (10% eficiencia), motor de gasolina e híbridos hasta motores eléctricos magnéticos (95%) y superconductores sin pérdida.',
           5, 'Un rotor de motor eléctrico magnético súper-eficiente en 3D girando a alta velocidad dentro de un campo magnético luminoso azul eléctrico sin rozamiento ni pérdida por calor.',
           [
               ("Máquina de Vapor de Carbón Primitiva (10% Eficiencia)", "Locomotoras antiguas quemando toneladas de carbón mineral donde el 90% del calor se disipa inútil al aire y solo un 10% empuja los pistones de las ruedas."),
               ("Motor de Combustión Interna de Gasolina (30% Eficiencia)", "El motor de cuatro tiempos del automóvil del siglo XX quemando gasolina en cilindros perdiendo la mayor parte de la energía por el escape en gases calientes."),
               ("Turbina Aeronáutica y Ciclo Combinado de Gas (50% Eficiencia)", "Motores de reacción en aviones y grandes centrales eléctricas que aprovechan los gases de escape calientes para mover segundas turbinas de vapor en cascada térmica."),
               ("Motor Eléctrico Magnético Sin Escobillas (95% Eficiencia)", "El motor de un coche eléctrico o tren bala donde los campos electromagnéticos convierten casi toda la electricidad de la batería directamente en movimiento rotatorio frío."),
               ("Superconductor Cuántico y Levitación (100% Eficiencia Teórica)", "Bobinas enfriadas a temperaturas criogénicas por donde la corriente eléctrica fluye eternamente sin resistencia, fricción cero ni pérdida térmica.")
           ],
           'Ilustra en el Peldaño 1 una locomotora de vapor antigua soltando humo negro con flechas rojas de pérdida de calor en castellano.')

    add_it('[NIV-049]', 'Los 6 Niveles de Capacidad y Supercómputo Mundial',
           'Potencia de cálculo matemática medido en FLOPS desde el ábaco, Pascalina mecánica, mainframes electromecánicos y Cray-1 vectorial hasta el clúster ExaFLOP Frontier y procesadores cuánticos de superposición.',
           6, 'Un candelabro de refrigeración de computadora cuántica en 3D forjado en tubos de oro y cobre dorado suspendido en el vacío procesando algoritmos cuánticos en frío absoluto.',
           [
               ("Ábaco y Calculadora Mecánica de Engranajes (Siglo XVII)", "El ábaco de cuentas de madera y la Pascalina con ruedas numéricas dentadas giradas a mano para sumar y restar cifras contables sin electricidad."),
               ("El Mainframe Electrónico a Válvulas (Años 50 - MegaFLOP)", "Habitaciones enteras llenas de armarios metálicos procesando miles de operaciones por segundo para calcular las tablas balísticas y el censo mundial."),
               ("El Superordenador Vectorial (Años 80 - GigaFLOP)", "La famosa supercomputadora Cray-1 con su forma cilíndrica rodeada de sofás de cuero refrigerada por freón para simular aerodinámica aeroespacial."),
               ("Clústeres Masivos de Servidores en Nube (Años 2010 - PetaFLOP)", "Centros de datos inmensos con miles de racks de servidores conectados por fibra óptica en paralelo resolviendo simulaciones biomédicas y redes sociales globales."),
               ("Supercómputo ExaFLOP - Frontier (El Límite de Silicio Actual)", "La supercomputadora más potente del mundo realizando más de un trillón (10¹⁸) de cálculos matemáticos en un solo segundo continuado."),
               ("Computación Cuántica de Qubits Lógicos (La Revolución Exponencial)", "Procesadores que aprovechan la superposición cuántica para evaluar todas las soluciones posibles de una molécula compleja simultáneamente al instante en un ciclo.")
           ],
           'Añade en el Peldaño 5 una fila de armarios negros de servidores con luces parpadeantes azules y textos en español.')

    add_it('[NIV-050]', 'Los 5 Niveles de Evolución de las Redes e Internet (Web 1.0 a Web3)',
           'Arquitectura de la web desde el directorio estático de lectura de los años 90, redes sociales interactivas Web 2.0 y economía de atención predictiva IA hasta la soberanía criptográfica Web3 y Metaverso persistente.',
           5, 'Una red esférica tridimensional luminosa conectando nodos ciudadanos mundiales sin servidores bancarios centrales simbolizando inmutabilidad Web3 descentralizada.',
           [
               ("Web 1.0 - El Directorio Estático de Lectura (1991 - 2004)", "Páginas web de texto plano y enlaces azules creadas por programadores donde el usuario común solo era un lector pasivo que consultaba información sin poder opinar."),
               ("Web 2.0 - La Red Social Interactiva y de Blogs (2004 - 2012)", "El nacimiento de YouTube, Wikipedia y las primeras redes sociales donde cualquier ciudadano podía subir vídeos, comentar y compartir su propia voz al mundo."),
               ("Web Algorítmica y Móvil de Atención (2012 - Presente)", "El smartphone en el bolsillo con feeds adictivos infinitos impulsados por Inteligencia Artificial que aprenden exactamente qué te gusta para retener tu mirada ante anuncios."),
               ("Web3 - Descentralización, Criptografía y Propiedad Digital", "Redes sin servidores corporativos centrales donde el usuario es el dueño criptográfico real de sus datos, identidades digitales e intercambios mediante blockchain."),
               ("El Metaverso Espacial y Neuro-Inmersivo del Futuro", "Un internet tridimensional persistente donde entramos corporalmente con avatares o hologramas para estudiar, trabajar y comerciar dentro de espacios digitales.")
           ],
           'Ilustra en el Peldaño 1 un viejo navegador con página web gris de texto plano con rótulos en castellano.')

    # GRUPO F: HISTORIA, ARQUITECTURA Y CIVILIZACIÓN (NIV-051 a NIV-060)
    add_it('[NIV-051]', 'Los 6 Niveles de Altura en la Arquitectura Humana',
           'Ingeniería estructural contra la gravedad desde chozas neolíticas, la Pirámide de Guiza apilada por gravedad y catedrales góticas de arbotante, hasta el rascacielos de acero, ascensor eléctrico, Burj Khalifa de 828m y megatorre vertical de 2 km.',
           6, 'La esbelta aguja del rascacielos Burj Khalifa de Dubái en 3D perforando las nubes sobre un cielo estrellado mostrando prodigio estructural en viento alto.',
           [
               ("Choza Neolítica y Estructura de Madera (5 a 10 metros)", "Aldeanos prehistóricos entrelazando troncos y barro con tejados de paja en viviendas de un solo piso limitadas por la resistencia de los árboles del entorno."),
               ("Pirámide de Guiza - Piedra Apilada por Gravedad (146 metros)", "La maravilla del mundo antiguo construida en Egipto apilando millones de bloques de piedra caliza maciza sin espacio interior habitable para resistir el paso del tiempo."),
               ("Catedral Gótica - Arbotantes y Bóvedas de Piedra (160 metros)", "Maestros canteros medievales inventando arcos apuntados y arbotantes exteriores para aligerar los muros y abrir enormes ventanales de vitrales celestiales."),
               ("El Rascacielos de Acero e Invención del Ascensor (Siglo XX - 300m)", "El Empire State y la Escuela de Chicago usando jaulas estructurales de vigas de acero soldadas y ascensores eléctricos rápidos para superar al ladrillo."),
               ("Super-Rascacielos - Burj Khalifa (828 metros / Casi 1 km)", "Torres modernas con núcleo de hormigón de ultra-alta resistencia y contrafuertes aerodinámicos en forma de Y para soportar vientos huracanados a altitud de nubes."),
               ("Mega-Estructura Vertical de Dos Kilómetros (El Futuro Urbano)", "Proyectos arquitectónicos visionarios con ascensores magnéticos sin cables y ecosistemas urbanos completos albergando a 100.000 personas en una sola torre bioclimática.")
           ],
           'Dibuja en el Peldaño 3 una catedral gótica medieval con vitrales de colores e imponentes arbotantes de piedra con rótulos en español.')

    add_it('[NIV-052]', 'Los 5 Niveles de Urbanismo y Ciudad en la Historia',
           'Evolución del asentamiento colectivo desde la aldea neolítica autogestionada, la polis clásica amurallada, metrópolis industrial del carbón del siglo XIX y megaciudadas modernas, hasta la eco-ciudad bioclimática circular verde de cero residuos.',
           5, 'Una eco-ciudad futurista verde en 3D con rascacielos cubiertos de jardines verticales colgantes, canales de agua purificada limpia y monorraíles magnéticos silenciosos.',
           [
               ("Aldea Agrícola Neolítica Autosuficiente", "Pequeños asentamientos de 100 personas alrededor de cultivos de trigo y ganado fluvial, donde todos los habitantes colaboraban directamente en la cosecha común."),
               ("Ciudad-Estado Amurallada Antigua y Clásica", "Urbs romanas o polis griegas con ágora central, templo, teatro, murallas defensivas de piedra e incipiente división del trabajo artesanal y comercial."),
               ("Metrópolis Industrial Densa del Siglo XIX", "Ciudades coronadas por chimeneas soltando humo de carbón, con barrios obreros densos cerca de ferrocarriles y fábricas de textiles bulliciosas."),
               ("Megaciudad Conectada Contemporánea (10 a 30 Millones)", "Ecosistemas urbanos masivos como Tokio o Nueva York con redes de metro subterráneo interminables, autopistas elevadas y distritos financieros de cristal."),
               ("Eco-Ciudad Verde y Circular Inteligente (El Modelo Regenerativo)", "Urbanismo bioclimático del siglo XXI sin residuos, donde los tejados cosechan energía solar, el agua pluvial se recicla al 100% y los huertos alimentan el vecindario.")
           ],
           'Ilustra en el Peldaño 5 una calle peatonal verde con árboles altos y paneles solares limpios con textos en castellano.')

    add_it('[NIV-053]', 'Los 6 Niveles del Transporte Terrestre y Velocidad',
           'Desplazamiento humano terrestre desde la marcha a pie, caravanas de carga y carruaje a caballo sobre calzadas, hasta la locomotora de vapor del siglo XIX, automóvil de autopista, tren bala Maglev japonés de 600 km/h y cápsulas Hyperloop en vacío de 1.000 km/h.',
           6, 'Un tren de levitación magnética japonés Maglev en 3D flotando milimétricamente sobre vías de imanes azules y rompiendo el viento a 600 kilómetros por hora sin rozar el suelo.',
           [
               ("A Pie y Caravana de Carga a Sangre (5 km/h)", "Viajeros y comerciantes recorriendo senderos de tierra durante semanas cargando fardos a la espalda o guiando caravanas de camellos y burros lentos."),
               ("Carruaje y Caballo con Rueda de Madera (20 km/h)", "Diligencias de correos y enganches de caballos galopando por calzadas romanas o caminos de tierra, el medio terrestre más rápido durante cuatro milenios."),
               ("Ferrocarril de Vapor de Carbón - Siglo XIX (80 km/h)", "Locomotoras de hierro resoplando vapor a presión por vías férreas continentales que unificaron países enteros y acortaron viajes de meses a pocos días directos."),
               ("Automóvil de Autopista con Motor y Neumático (120 km/h)", "La democratización de la movilidad individual de gasolina sobre redes pavimentadas de asfalto con neumáticos de caucho y suspensión confortable."),
               ("Tren Bala de Alta Velocidad y Levitación Maglev (350 a 600 km/h)", "Trenes aerodinámicos en Japón o Europa que no tienen ruedas mecánicas rozando rieles, sino que levitan suspendidos por potentes imanes superconductores."),
               ("Hyperloop en Tubo al Vacío (1.000 km/h - Mach 0.8)", "Cápsulas de pasajeros viajando dentro de largos tubos subterráneos sellados sin aire ni resistencia atmosférica a velocidades cercanas a las del sonido.")
           ],
           'Añade en el Peldaño 2 un carruaje de caballos clásico de madera por un camino rural con rótulos en castellano.')

    add_it('[NIV-054]', 'Los 5 Niveles de Gestión y Suministro del Agua Potable',
           'Ingeniería sanitaria desde pozos aldeanos y acueductos romanos por gravedad con pendiente milimétrica calculada, hasta la cloración industrial de las metrópolis, plantas desalinizadoras por ósmosis inversa en el desierto y el ciclo biológico cerrado regenerativo de la Estación Espacial.',
           5, 'Un acueducto romano clásico de arcos de piedra en 3D del cual brota una cascada de agua cristalina cayendo hacia un moderno módulo de filtración por ósmosis inversa.',
           [
               ("Pozos Manuales e Ingenios Aldeanos Primitivos", "Mujeres y aldeanos extrayendo agua con cubos de madera desde pozos o ríos expuestos a contaminación biológica y bacterias causantes de epidemias antiguas."),
               ("Acueductos Romanos y Canales por Gravedad", "Arquerías monumentales de piedra transportando agua fresca de manantiales lejanos por kilómetros sin bombas mecánicas gracias a una pendiente milimétrica calculada."),
               ("Red Urbana de Potabilización y Cloración Industrial", "La mayor revolución médica del siglo XX: añadir cloro y filtrar el agua en acueductos de hierro para erradicar el cólera, el tifus y la disentería de las ciudades europeas."),
               ("Ósmosis Inversa y Desalinización Marina", "Plantas costeras de alta tecnología empujando agua del mar salada a altísima presión a través de membranas semipermeables que retienen la sal para dar agua dulce al desierto."),
               ("Ciclo Cerrado de Regeneración Biológica Espacial", "El sistema vital de la Estación Espacial Internacional que recupera, filtra y recicla el 98% del sudor y humedad de la respiración de los astronautas convirtiéndolo en agua pura perpetua.")
           ],
           'Ilustra en el Peldaño 4 una moderna planta desalinizadora al lado de la playa con tuberías azules y textos en español.')

    add_it('[NIV-055]', 'Los 6 Niveles de la Medicina y Cirugía a lo Largo de los Siglos',
           'Evolución del arte de curar desde la trepanación neolítica e ilustración anatómica de Vesalio, pasando por el milagro médico de la anestesia, antisepsia y descubrimiento de la penicilina en 1928, hasta la cirugía mínimamente invasiva por laparoscopia y el brazo robótico Da Vinci nanométrica.',
           6, 'El brazo robótico médico Da Vinci de cuatro pinzas quirúrgicas en 3D operando con exactitud nanométrica dentro de una gota de sangre sin tocar el tejido sano adyacente.',
           [
               ("Trepanación y Herbolaria Empírica Antigua", "Chamanes y médicos neolíticos perforando agujeros en el cráneo con pedernales para liberar malos espíritus o aplicando emplastos de hierbas silvestres en heridas abiertas."),
               ("Anatomía Renacentista e Ilustración Científica", "Andréas Vesalio y Leonardo da Vinci diseccionando cuerpos para dibujar por primera vez con exactitud la musculatura, nervios y el sistema circulatorio real humano."),
               ("Anestesia y Antisepsia del Siglo XIX (La Gran Revolución)", "El fin del dolor insoportable con éter y la orden quirúrgica de lavarse las manos con fenol para esterilizar instrumentos, reduciendo las muertes por infección hospitalaria."),
               ("La Penicilina y el Imperio de los Antibióticos (1928)", "El descubrimiento de Alexander Fleming del hongo Penicillium que destruye bacterias mortales, salvando a cientos de millones de personas de morir por una simple pulmonía o corte."),
               ("Cirugía Mínimamente Invasiva por Laparoscopia", "Cirujanos operando órganos internos observando una pantalla 4K a través de incisiones minúsculas de un centímetro con cámaras de fibra óptica sin abrir el abdomen."),
               ("Cirugía Robótica Nanométrica y Terapia Génica Molecular", "Bisturís asistidos por IA eliminando tumores con precisión microscópica inalcanzable por el pulso humano y edición del ADN con CRISPR para curar enfermedades hereditarias.")
           ],
           'Dibuja en el Peldaño 3 a un cirujano del siglo XIX lavándose las manos en una pila de agua limpia antes de operar con rótulos en castellano.')

    add_it('[NIV-056]', 'Los 5 Niveles de Producción y Agricultura Humana',
           'Obtención alimentaria desde el nomadismo recolector-cazador de la prehistoria, el descubrimiento de semillas de la Revolución Agrícola Neolítica y tractor de acero, hasta la Revolución Verde de fijación de nitrógeno Haber-Bosch y la moderna granja vertical hidropónica LED automatizada por IA.',
           5, 'Un invernadero vertical hidropónico en 3D iluminado con luces LED fucsia y azul, donde crecen lechugas y fresas sin tierra y consumiendo un 95% menos de agua que en el campo.',
           [
               ("Recolección y Caza Itinerante (Nomadismo Prehistórico)", "Pequeños clanes de humanos prehistóricos recolectando bayas silvestres y cazando venados con lanzas de sílex moviéndose constantemente tras el alimento."),
               ("Revolución Agrícola Neolítica y Riego Ancestral", "El primer gran asentamiento humano plantando semillas de trigo, domesticando ovejas y canalizando arroyos en Mesopotamia y Egipto hace 10.000 años."),
               ("Mecanización e Industrialización del Tractor (Siglo XX)", "Tractores con motor diésel y cosechadoras mecánicas de acero labrando miles de hectáreas por día sustituyendo el trabajo agotador de mil bueyes y arados manuales."),
               ("La Revolución Verde - Fertilizantes y Agronomía Química", "La síntesis de nitrógeno por el método Haber-Bosch y semillas híbridas resistentes que multiplicaron por 4 la cosecha mundial de cereales evitando hambrunas globales."),
               ("Agricultura Vertical de Precisión por IA e Hidroponía", "Granjas urbanas de varios pisos en ambiente controlado por sensores sin pesticidas ni clima externo, cultivando alimentos frescos a 100 metros del consumidor en todo el año.")
           ],
           'Ilustra en el Peldaño 3 un gran tractor verde cosechando trigo dorado en un campo soleado con textos en español castellano.')

    add_it('[NIV-057]', 'Los 6 Niveles de Resistencia y Materiales Estructurales',
           'Ciencia de materiales según tenacidad y compresión: adobes primitivos secados al sol, sillería megalítica y mármoles clásicos, hierro fundido, acero estructural con hormigón armado, aleaciones de titanio aeroespacial e indestructibles nanotubos de carbono y grafeno molecular cuántico.',
           6, 'Una estructura celular hexagonal de grafeno purísimo en 3D de color negro brillante y transparente doscientas veces más fuerte que el acero arquitectónico pero más ligero que el papel.',
           [
               ("Barro, Adobe Cocido y Madera Primitiva", "Ladrillos secados al sol de arcilla con paja y troncos de roble cortados, materiales accesibles en la naturaleza pero de baja resistencia a la humedad y fuego."),
               ("Piedra Tallada Megalítica y Mármol Clásico", "Bloques de granito y caliza maciza cortados con cincel capaces de soportar enormes cargas de compresión por milenios en templos griegos y murallas incas."),
               ("Hierro Forjado y Bronce de Aleación", "Metales fundidos en hornos de carbón a alta temperatura que aportaron por primera vez tenacidad flexible para espadas, arados resistentes y rejas de arcos."),
               ("Acero Estructural y Hormigón Armado del Siglo XX", "Aleación de hierro con carbono reforzando el interior del hormigón, permitiendo construir puentes colgantes gigantescos y rascacielos sismorresistentes."),
               ("Aleaciones Aeroespaciales de Titanio y Fibra de Carbono", "Materiales ultraligeros que no se oxidan jamás ni pierden forma bajo temperaturas extremas de fricción supersónica en aviones de combate y cohetes orbitales."),
               ("Nanotubos de Carbono y Grafeno Molecular (El Límite Físico)", "Cilindros y láminas de una sola capa de átomos de carbono unidos en enlaces covalentes indestructibles, la única materia capaz de sostener un Ascensor Espacial desde la órbita.")
           ],
           'Dibuja en el Peldaño 2 las grandes piedras talladas encajadas sin cemento de los muros incas de Cuzco con rótulos en español.')

    add_it('[NIV-058]', 'Los 5 Niveles de Exploración Espacial Humana',
           'Conquista humana del cosmos: desde el bip orbital del Sputnik y el vuelo suborbital valiente de Gagarin, el paso inmortal de Neil Armstrong en el Apolo 11 y la habitación continua en microgravedad de la ISS, hasta las bases polares lunares Artemis y cúpulas bioclimáticas permanentes de colonización en Marte.',
           5, 'Una base de colonización cúpula sobre la superficie roja de Marte en 3D con invernaderos solares transparentes y rovers de exploración interplanetaria moviéndose entre los cráteres.',
           [
               ("Vuelo Suborbital y Primeros Satélites en Órbita Baja (Años 50-60)", "El Sputnik soviético emitiendo su bip en el cielo y el primer vuelo valiente de Yuri Gagarin completando una sola vuelta en torno a la Tierra en caída libre de 90 minutos."),
               ("Aterrizaje Lunar Tripulado - Apolo 11 (1969 - 380.000 km)", "Neil Armstrong dejando la primera huella de bota humana sobre el regolito lunar y regresando a casa sano y salvo con rocas extraterrestres de la Luna."),
               ("Estación Espacial Habitada en Microgravedad Continua (ISS)", "Laboratorio orbital multi-nacional a 400 km de altura donde astronautas viven y trabajan durante 6 meses continuados realizando experimentos biológicos sin gravedad terrestre."),
               ("Base Permanente en el Polo Sur de la Luna (Programa Artemis)", "Módulos habitables soterrados en cuevas lunares alimentados por energía nuclear para extraer agua helada de los cráteres oscuros y fabricar combustible de cohete."),
               ("Colonización Interplanetaria y Base en Marte (El Salto Multi-Planeta)", "Una sociedad humana independiente habitando cúpulas presurizadas sobre el planeta rojo a 56 millones de kilómetros de la Tierra, cultivando sus alimentos en suelo marciano.")
           ],
           'Ilustra en el Peldaño 2 el módulo lunar Eagle plateado posado en la superficie de la Luna con la Tierra azul al fondo en español.')

    add_it('[NIV-059]', 'Los 6 Niveles de Conservación de Alimentos en la Humanidad',
           'Biotecnología de preservación de cosechas contra bacterias: salazón primitivo al sol y fermentación probiótica en tinajas antiguas, enlatado hermético al vacío de Nicolás Appert para marineros, pasteurización de Pasteur, refrigeración eléctrica del hogar y criogenia por liofilización espacial al vacío.',
           6, 'Una cápsula de liofilización al vacío en 3D donde fresas y raciones espaciales conservan su forma, color y nutrientes en un 100% durante 25 años continuados sin estropearse.',
           [
               ("Secado al Sol y Salazón Primitivo (Deshidratación Natural)", "Aldeanos prehistóricos secando tiras de carne al sol y cubriendo pescado con sal marina para extraer el agua celular interior y matar las bacterias por ósmosis."),
               ("Fermentación Controlada en Vasijas de Barro (Vino, Queso y Yogur)", "La genialidad ancestral de utilizar bacterias lácticas o levaduras benéficas controladas para acidificar el alimento, produciendo pan y yogur que no se pudre al instante."),
               ("Enlatado Hermético al Vacío - Nicolás Appert (Siglo XIX)", "Alimentos hervidos y sellados en latas de hojalata sin aire en su interior para alimentar a los ejércitos de Napoleón y marineros sin riesgo de escorbuto ni putrefacción."),
               ("Pasteurización Científica y Esterilización Térmica (Louis Pasteur)", "Calentar la leche y caldos a temperaturas controladas exactas de 72 °C para fulminar gérmenes patógenos sin destruir el sabor ni las vitaminas."),
               ("Refrigeración y Congelación Eléctrica Doméstica (Siglo XX)", "El frigorífico en la cocina de cada hogar bajando la temperatura para adormecer el metabolismo bacteriano, permitiendo comer pescado y frutas frescas a miles de kilómetros del origen."),
               ("Liofilización Criogénica por Sublimación en Vacío (Comida Espacial)", "Congelar el alimento a -50 °C y someterlo a vacío para que el hielo pase directamente de sólido a vapor, preservando su estructura molecular ligera por décadas.")
           ],
           'Dibuja en el Peldaño 3 latas de conservas antiguas de hojalata cerradas herméticamente con textos exactos en español.')

    add_it('[NIV-060]', 'Los 5 Niveles de Evolución del Libro y el Conocimiento Escrito',
           'Soporte del pensamiento humano: tablillas de arcilla cuneiforme pesadas en Mesopotamia y rollos de papiro/pergaminos copiados por monjes en monasterios durante años, la revolución de la imprenta de tipos móviles de Gutenberg (1440), e-readers de tinta electrónica y la biblioteca neuronal universal en red y grafos IA.',
           5, 'Una imprenta clásica de madera del siglo XV de Gutenberg en 3D cuyos pliegos de papel impreso salen volando en el aire transformándose en tabletas luminosas de tinta electrónica e interfaces neuronales.',
           [
               ("Tablillas de Arcilla Cuneiforme en Mesopotamia (Hace 5.000 Años)", "Escribas sumerios presionando cuñas de caña sobre tabletas pesadas de barro húmedo cocido al sol para llevar la contabilidad de granos de trigo y reyes antiguos."),
               ("Rollo de Papiro y Códice Pergamino en Monasterios", "Monjes medievales pasando años enteros de su vida copiando con pluma de ave un solo ejemplar de la Biblia o filosofía griega sobre costosas pieles de oveja raspadas."),
               ("La Imprenta de Tipos Móviles de Gutenberg (1440 - La Revolución)", "Letras individuales de plomo en una prensa mecánica que bajó el coste de un libro en un 99%, permitiendo que millones de ciudadanos aprendieran a leer en Europa."),
               ("Libro Digital y Tinta Electrónica - E-reader (Siglo XXI)", "Una pantalla ligera sin brillo ocular que almacena 10.000 libros completos en una sola mano, pesando lo mismo que un solo cuaderno de papel."),
               ("Biblioteca Neuronal Conectada e Interfaz de Grafos por IA", "El conocimiento universal indexado y sintetizado por algoritmos interconectados, donde el estudiante consulta y conversa en tiempo real con la sabiduría total de la humanidad en segundos.")
           ],
           'Ilustra en el Peldaño 2 a un monje medieval sentado con una vela copiando un libro antiguo con textos en castellano estricto.')

    return items
