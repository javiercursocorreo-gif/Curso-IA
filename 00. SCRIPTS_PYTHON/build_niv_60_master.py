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

    # =========================================================================
    # LOTE 4 (SESIONES 31 A 40): MICRO-APLICACIONES INTERACTIVAS SENIORS (+65)
    # =========================================================================
    add_senior_microapp(
        '[NIV-031]',
        'Los 6 Estratos del Océano, Respiración Pulmonar y Calma Mental',
        'Guía interactiva que combina la batimetría marina (desde la superficie fótica soleada hasta las fosas abisales) con ejercicios de respiración diafragmática consciente (técnica 4-7-8) para reducir la ansiedad, estabilizar pulsaciones, facilitar el sueño y oxigenar el cerebro en personas mayores.',
        'Actúa como un médico neumólogo y pedagogo de relajación para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar una guía interactiva en HTML que use las profundidades del mar como metáfora para enseñar la respiración pausada (técnica 4-7-8) y oxigenar el cuerpo.',
        'Genera la aplicación interactiva en HTML con selector de los 6 estratos marinos, guía animada de respiración (inhalar 4s, retener 7s, exhalar 8s), contador de ciclos y consejos para calmar palpitaciones y dormir mejor.',
        '• 6 Estratos Marinos: 1. Zona Epipelágica (0-200m, Sol y brisa marina), 2. Zona Mesopelágica (200-1000m, Penumbra y serenidad), 3. Zona Batipelágica (1000-4000m, Silencio profundo), 4. Zona Abisal (4000-6000m, Calma absoluta), 5. Fosa Hadal (6000-11000m, Presión controlada y paz interior), 6. Chimeneas Hidrotermales (Calor vital y regeneración).\n• Animador de respiración: Círculo expansivo/contráctil con temporizador (Inhalar 4s - Retener 7s - Exhalar 8s).\n• Indicadores: Frecuencia cardíaca estimada, nivel de oxígeno y reducción de estrés (%).\n• Pautas médicas: No forzar si hay EPOC o mareo, sentarse cómodo con la espalda apoyada y realizar 4 ciclos antes de dormir.',
        'SIMULADOR_PROFUNDIDAD_OCEANO_RESPIRACION_SENIORS.html',
        'Respiración y Calma Marina (+65)'
    )

    add_senior_microapp(
        '[NIV-032]',
        'Los 5 Niveles de la Pirámide Nutricional y Digestión Saludable Senior',
        'Herramienta interactiva de nutrición clínica adaptada a mayores de 65 años: organiza los 5 niveles de alimentos según su facilidad de asimilación gástrica, aporte de proteína magra para no perder músculo, fibra soluble contra el estreñimiento y recetas tradicionales digestivas.',
        'Actúa como un médico geriatra y nutricionista clínico para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar un semáforo interactivo en HTML que clasifique los alimentos diarios según lo bien que sientan al estómago y el aporte proteico que necesitan los mayores.',
        'Genera la aplicación interactiva en HTML con 5 escalones nutricionales, calculadora de raciones de proteína diaria (pescado, huevos, legumbres suaves), balance de hidratación y fibra, y platos tradicionales recomendados.',
        '• 5 Escalones: 1. Base Hidratante y Caldos (Agua, infusiones, caldos desgrasados), 2. Frutas Maduras y Verduras Cocidas (Purés, compotas, calabacín, manzana asada), 3. Proteínas Nobles de Fácil Masticación (Pescado blanco, tortilla, legumbres pasadas por pasapurés), 4. Cereales Integrales y Aceite de Oliva Virgen Extra (Pan de masa madre, arroz, AOVE crudo), 5. Moderación Absoluta (Embutidos grasos, fritos pesados y azúcares industriales).\n• Calculadora de proteína: Deslizador de peso corporal (50-100 kg) calculando el gramaje ideal (1.0 a 1.2 g de proteína/kg/día para evitar sarcopenia).\n• Consejos digestivos: Masticar despacio (20 veces por bocado), cenar 2 horas antes de acostarse y pasear 10 minutos tras la comida.',
        'SIMULADOR_NUTRICION_DIGESTION_SALUDABLE_SENIORS.html',
        'Guía Nutrición y Digestión (+65)'
    )

    add_senior_microapp(
        '[NIV-033]',
        'Los 6 Niveles de Vitalidad Celular, Mitocondrias y Masa Muscular',
        'Simulador clínico de prevención de la sarcopenia y fragilidad en mayores: evalúa la fuerza de piernas y agarre, enseña ejercicios sencillos con botellas de agua o levantarse de la silla, y explica cómo las mitocondrias se reactivan con el movimiento diario a cualquier edad.',
        'Actúa como un fisioterapeuta geriátrico y médico rehabilitador para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar una herramienta interactiva en HTML que evalúe la fuerza muscular cotidiana y anime a hacer ejercicios suaves de fuerza en casa sin máquinas de gimnasio.',
        'Genera el archivo HTML interactivo con el test de levantarse de la silla (5 repeticiones), selector de 6 niveles de vitalidad mitocondrial, rutina guiada de ejercicios con botellas de agua y consejos de seguridad.',
        '• 6 Niveles de Vitalidad: 1. Reposo Prolongado / Sedentarismo Crónico, 2. Movilidad Básica Doméstica, 3. Caminante Habitual (Paseos llanos), 4. Fuerza Funcional Activa (Sube escaleras con soltura), 5. Autonomía Robusta (Carga compras y cuida el jardín), 6. Plenitud y Reserva Funcional Óptima.\n• Test de la Silla interactivo: Cronómetro para medir el tiempo en levantarse y sentarse 5 veces (< 11 seg = Excelente, 11-14 seg = Normal, > 15 seg = Necesita refuerzo).\n• Rutina sin riesgos: Sentadillas con silla detrás, elevación de talones para gemelos y flexiones de brazos apoyados contra la pared.',
        'SIMULADOR_VITALIDAD_MUSCULAR_SARCOPENIA_SENIORS.html',
        'Test Vitalidad y Fuerza Muscular (+65)'
    )

    add_senior_microapp(
        '[NIV-034]',
        'Los 5 Pilares de la Longevidad Activa: El Secreto de las Zonas Azules',
        'Calculadora del estilo de vida centenario basada en las 5 Zonas Azules del mundo (Okinawa, Cerdeña, Icaria, Nicoya y Loma Linda): evalúa el propósito de levantarse cada mañana (Ikigai), la red de amigos y vecinos, el movimiento natural constante, la alimentación frugal y la serenidad mental.',
        'Actúa como un epidemiólogo social y divulgador de las Zonas Azules para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar una calculadora en HTML que mida los 5 hábitos de los pueblos más longevos del mundo y los traslade a la vida de un jubilado en España.',
        'Genera la aplicación interactiva en HTML con selector de los 5 pilares de longevidad, puntuación de 0 a 100 de Índice Zona Azul, mapa interactivo de las 5 regiones y compromisos cotidianos alcanzables.',
        '• 5 Pilares: 1. Moverse con Naturalidad (Caminar a los recados, cuidar plantas), 2. Propósito de Vida / Ikigai (Tener un motivo ilusionante cada mañana), 3. Bajar el Ritmo (Siesta breve, tertulia con amigos), 4. Regla del 80% (Hara Hachi Bu: comer hasta no estar saciado del todo), 5. Tribu y Familia (Poner a los seres queridos en primer lugar).\n• Índice de Longevidad: Puntuación de 0 a 100 puntos con semáforo y diagnóstico afectuoso.\n• Metáforas de Cerdeña y Okinawa adaptadas a las costumbres de nuestros mayores (el café con los amigos, el paseo de la tarde y la comida familiar).',
        'SIMULADOR_ZONAS_AZULES_LONGEVIDAD_SENIORS.html',
        'Calculadora Zonas Azules y Longevidad (+65)'
    )

    add_senior_microapp(
        '[NIV-035]',
        'Los 6 Estratos del Bosque, Paseos Verdes y Baños de Bosque (Shinrin-Yoku)',
        'Aplicación médica y pedagógica de salud natural: explica cómo el contacto con árboles y parques reduce el cortisol, regula la tensión arterial y estimula las defensas gracias a los fitoncidas vegetales. Incluye un planificador de salidas a parques urbanos, jardines y senderos accesibles.',
        'Actúa como un médico naturista y pedagogo ambiental para personas mayores (+65).\nExplícame en 3 viñetas cómo estructurar una guía interactiva en HTML que explique con base científica por qué pasear bajo los árboles mejora la salud y ayude a planificar paseos agradables.',
        'Genera el archivo HTML interactivo con los 6 niveles del ecosistema forestal, medidor de beneficios médicos (reducción de tensión y estrés), planificador de paseos semanales y pautas para caminar con calzado cómodo.',
        '• 6 Niveles Forestales: 1. Asfalto y Ciudad sin Árboles (Mayor fatiga y ruido), 2. Plazas y Jardines de Barrio (Primer alivio visual), 3. Parques Urbanos Frondosos (Fitoncidas y sombra fresca), 4. Dehesas y Pinares Accesibles (Inmersión en naturaleza llana), 5. Bosques Maduros y Valles Húmedos (Máxima pureza de aire y calma), 6. Cumbres y Miradores Panorámicos (Perspectiva y expansión espiritual).\n• Beneficios clínicos demostrados: Reducción del cortisol salival en un 16%, descenso de 5 mmHg en la tensión sistólica y mejora de la calidad del sueño.\n• Protocolo del paseo sereno: 40 minutos a paso suave, respirar profundo por la nariz, escuchar a los pájaros y sentarse en un banco a contemplar.',
        'SIMULADOR_BANOS_BOSQUE_NATURALEZA_SENIORS.html',
        'Guía Baños de Bosque y Salud (+65)'
    )

    add_senior_microapp(
        '[NIV-036]',
        'El Radar de Toxicidad en el Hogar: Químicos de Limpieza, Humos y Prevención',
        'Guía interactiva de prevención y seguridad doméstica vital para mayores: advierte del peligro mortal de mezclar lejía con amoníaco o salfumán (gas cloramina tóxico), enseña a ventilar adecuadamente braseros, estufas de butano y calderas (intoxicación silenciosa por monóxido de carbono CO) y proporciona un escáner de símbolos de peligro con soluciones ecológicas seguras (vinagre y bicarbonato).',
        'Actúa como un jefe de bomberos y toxicólogo médico especializado en el hogar de personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar un detector interactivo en HTML que alerte de las mezclas peligrosas de limpieza y de los humos invisibles en casa.',
        'Genera la aplicación interactiva en HTML con matriz de mezclas prohibidas (lejía + amoníaco, etc.), semáforo de monóxido de carbono en calefacción, alternativas de limpieza natural segura y botón de urgencia toxicológica (91 562 04 20).',
        '• Matriz de Mezclas Prohibidas: Lejía + Amoníaco = Vapores de cloramina (asfixia pulmonar inmediata), Lejía + Vinagre/Salfumán = Gas cloro letal, Lejía + Alcohol = Cloroformo tóxico.\n• Semáforo de Calefacción y CO: La "muerte dulce" del monóxido de carbono: llama azul (correcta) vs llama amarilla/naranja (mala combustión peligrosa), ventilación obligatoria de rejillas.\n• Alternativas domésticas 100% seguras: Vinagre blanco para la cal, bicarbonato para fregar fregaderos y jabón neutro tradicional.\n• Directorio de Emergencias: Instituto Nacional de Toxicología (91 562 04 20) y 112 visible en tipografía gigante.',
        'SIMULADOR_TOXICIDAD_HOGAR_PREVENCION_SENIORS.html',
        'Radar Seguridad Doméstica y Tóxicos (+65)'
    )

    add_senior_microapp(
        '[NIV-037]',
        'Los 6 Niveles de Termorregulación Corporal, Abrigarse Bien y Evitar Caídas por Frío',
        'Micro-aplicación interactiva de confort térmico y salud geriátrica: explica por qué el cuerpo de los mayores pierde grasa subcutánea y siente más frío en manos y pies, enseña a vestirse por capas (método cebolla), a mantener la casa a 21 °C sin despilfarrar y a evitar el agarrotamiento articular matutino que provoca tropiezos.',
        'Actúa como un médico geriatra y especialista en medicina del confort doméstico para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar una herramienta interactiva en HTML que enseñe a regular la temperatura del hogar y protegerse del frío sin riesgos de caídas ni braseros peligrosos.',
        'Genera el archivo HTML interactivo con termómetro de confort (18 °C a 24 °C), selector de los 6 niveles de respuesta térmica corporal, recomendador de ropa por capas y protocolo para salir a la calle en días fríos.',
        '• 6 Niveles Térmicos: 1. Hipotermia y Frío Severo (< 16 °C en casa: riesgo cardiovascular y agarrotamiento), 2. Ambiente Fresco (17-19 °C: requiere chaqueta y zapatillas abrigadas), 3. Confort Óptimo de Salud (20-21 °C: equilibrio perfecto según el Ministerio de Sanidad), 4. Ambiente Agradable (22-23 °C: ideal para lectura y reposo), 5. Calor Excesivo (24-26 °C: reseca vías respiratorias y encarece la factura), 6. Riesgo de Golpe de Calor (> 27 °C en verano: deshidratación urgente).\n• Técnica de la cebolla: 1ª capa transpirable (algodón), 2ª capa térmica (jersey de lana o forro polar ligero), 3ª capa cortavientos para la calle.\n• Protección de zonas clave: Calcetines de lana sin costuras opresivas, guantes finos y bufanda tapando garganta y boca para no inhalar aire helado directo.',
        'SIMULADOR_TERMORREGULACION_CONFORT_SENIORS.html',
        'Guía Termorregulación y Confort (+65)'
    )

    add_senior_microapp(
        '[NIV-038]',
        'Calculadora de Ergonomía y Esfuerzo Doméstico: Cuidar Espalda y Articulaciones',
        'Simulador de biomecánica postural y cuidado de la columna para la vida cotidiana: enseña cómo doblar rodillas al agacharse a por un paquete, la ventaja de empujar un carro de 4 ruedas en vez de arrastrarlo con dos, cómo repartir las bolsas de la compra en ambas manos y la altura correcta para planchar o barrer sin sufrir lumbalgias ni ciáticas.',
        'Actúa como un traumatólogo y fisioterapeuta ergonómico para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una calculadora interactiva en HTML que muestre cuánto sufre la columna lumbar según la postura adoptada en tareas de la casa y enseñe a evitar lesiones.',
        'Genera el archivo HTML interactivo con calculadora de carga lumbar en kg (según postura recta vs doblada), comparador de 5 tareas cotidianas (carro de la compra, fregar el suelo, planchar, levantar peso), y decálogo visual de higiene postural.',
        '• Calculadora de Presión Discal en L5-S1: Levantar 5 kg con piernas flexionadas = 50 kg de presión en columna; levantar los mismos 5 kg con piernas rectas y lomo doblado = ¡180 kg de sobrecarga discal peligrosa!\n• 5 Situaciones Cotidianas: 1. Carro de la compra (Empujar con 4 ruedas reduce el esfuerzo un 60%), 2. Bolsas de la compra (Dividir 8 kg en dos bolsas de 4 kg para equilibrar la pelvis), 3. Barrer y Fregar (Mango largo que llegue a la altura de la nariz sin arquear la espalda), 4. Planchar (Apoyar un pie en un taburete bajo para descansar la zona lumbar), 5. Hacer la cama (Arrodillarse o flexionar piernas en lugar de doblar la cintura a plomo).\n• Semáforo de advertencia: Mensajes claros en verde (postura segura) y rojo (postura lesiva).',
        'SIMULADOR_ERGONOMIA_COLUMNA_ARTICULACIONES_SENIORS.html',
        'Calculadora Ergonomía y Columna (+65)'
    )

    add_senior_microapp(
        '[NIV-039]',
        'Guía Interactiva de Iluminación Accesible, Contraste y Cuidado Ocular',
        'Micro-aplicación interactiva de ergonomía visual y seguridad ambiental para personas mayores: calcula la necesidad de lúmenes reales (una persona de 70 años necesita hasta el triple de luz que una de 20 para leer con la misma nitidez), enseña a contrastar los bordes de los escalones e interruptores para no tropezar, y desmitifica los cuidados de cataratas, vista cansada (presbicia) y sequedad ocular.',
        'Actúa como un médico oftalmólogo y diseñador de accesibilidad para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar un simulador interactivo en HTML que muestre cuánta luz necesita un hogar senior para leer y caminar seguro sin tropezar por sombras o reflejos.',
        'Genera el archivo HTML interactivo con simulador de luminosidad por estancia (salón, cocina, pasillo, lectura), recomendador de bombillas LED cálidas (3000K, sin parpadeos), contraste visual antideslumbrante y consejos oftalmológicos preventivos.',
        '• Fisiología visual geriátrica: A los 65 años el cristalino se vuelve más opaco y la pupila responde más lenta; se necesitan 500-750 lux para lectura confortable sin forzar la vista ni producir dolor de cabeza.\n• Niveles de Iluminación Recomendados: 1. Pasillo y Escaleras (200-300 lux con luces nocturnas guía automáticas para ir al baño), 2. Salón y Estar (300-400 lux luz difusa), 3. Cocina y Baño (500 lux para manipular cuchillos y medicamentos sin error), 4. Rincón de Lectura y Labores (750 lux con foco directo orientable desde atrás/lateral).\n• Prevención de Tropiezos: Cinta adhesiva de alto contraste en el borde de escalones, interruptores con piloto luminoso visible en la oscuridad y eliminación de alfombras resbaladizas sin base de goma.\n• Salud ocular diaria: Uso de lágrimas artificiales sin conservantes si hay ojo seco por la calefacción y revisión anual de graduación y tensión ocular.',
        'SIMULADOR_ILUMINACION_CUIDADO_OCULAR_SENIORS.html',
        'Simulador Iluminación y Cuidado Ocular (+65)'
    )

    add_senior_microapp(
        '[NIV-040]',
        'Los 5 Niveles de Regeneración Cutánea, Cuidado de la Piel y Cicatrización',
        'Guía interactiva de dermatología preventiva y cuidados de la piel en la madurez: explica cómo la piel madura se vuelve más fina ("piel de cebolla" o fragilidad capilar), enseña a aplicar cremas hidratantes con urea al 10%, a desinfectar y proteger pequeños rasguños con apósitos de silicona que no rasgan al retirar, y facilita el método clínico ABCD para vigilar pecas y manchas solares con serenidad.',
        'Actúa como un médico dermatólogo y enfermero geriátrico para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar una herramienta interactiva en HTML que enseñe a cuidar la piel frágil de las piernas y brazos, curar rozaduras sin dolor y vigilar manchas solares sin alarmismo.',
        'Genera el archivo HTML interactivo con los 5 niveles de salud de la piel madura, guía de hidratación diaria (urea), protocolo de cura en 3 pasos para heridas leves, y la regla ABCD de lunares explicada de forma sencilla.',
        '• 5 Niveles de la Piel Madura: 1. Sequedad Severa y Prurito (Picor por falta de lípidos y jabones agresivos), 2. Piel Fina / Fragilidad Capilar (Moratones por roces cotidianos leves), 3. Piel Hidratada y Protegida (Elasticidad recuperada con crema diaria), 4. Cicatrización Eficaz y Limpia (Cura adecuada sin arrancar costras), 5. Piel Blindada y Equilibrada (Barrera cutánea íntegra con protección solar).\n• Regla ABCD de Lunares: A de Asimetría, B de Bordes irregulares, C de Color no homogéneo, D de Diámetro mayor a 6 mm (tamaño de la goma de un lápiz). Si cambia, se consulta al médico de cabecera con total tranquilidad.\n• Pautas de higiene geriátrica: Duchas templadas (no agua ardiendo), geles syndet "sin jabón", secado suave con toalla a toques (sin frotar con fuerza) y aplicación de crema hidratante en los 3 minutos posteriores a la ducha.',
        'SIMULADOR_CUIDADO_PIEL_CICATRIZACION_SENIORS.html',
        'Guía Cuidado de la Piel y Cicatrización (+65)'
    )

    # =========================================================================
    # LOTE 5 (SESIONES 41 A 50): MICRO-APLICACIONES INTERACTIVAS SENIORS (+65)
    # =========================================================================
    add_senior_microapp(
        '[NIV-041]',
        'Los 6 Niveles de Conectividad Digital, Wi-Fi del Hogar y Videollamadas Familiares',
        'Guía interactiva de conectividad doméstica para personas mayores: explica de la vieja red telefónica de cobre a la fibra óptica y Wi-Fi de alta cobertura, enseña a ubicar el router sobre una mesita despejada (sin esconderlo en cajones ni tras muros de carga) para hablar con los nietos por videollamada sin cortes de imagen ni voz de robot, y proporciona la regla de oro de los 30 segundos para reiniciar el router con tranquilidad.',
        'Actúa como un técnico de telecomunicaciones y pedagogo digital para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar un simulador interactivo en HTML que muestre por qué la Wi-Fi no llega bien a todas las habitaciones y enseñe a colocar el router en alto para hablar con los nietos por videollamada sin cortes.',
        'Genera la aplicación interactiva en HTML con selector de estancia del router (salón, pasillo, escondido), grosor de tabiques, medidor de cobertura Wi-Fi y velocidad de fibra, y el protocolo paso a paso de los 30 segundos para reiniciar el router con tranquilidad.',
        '• 6 Niveles de Cobertura: 1. Zona Ciega / Sin Señal (Router oculto en muebles o muros gruesos), 2. Señal Débil / Inestable (1 barra, voz entrecortada de robot), 3. Conectividad Básica (Lectura de prensa y WhatsApp fluido), 4. Conexión Óptima de Fibra (Videollamada HD con nietos sin interrupciones), 5. Cobertura Total con Repetidor (Pasillo intermedio cubriendo terraza y dormitorios), 6. Red Simétrica de Alta Velocidad (Múltiples dispositivos familiares a la vez).\n• Regla de los 30 segundos: Desenchufar de la pared, contar despacio hasta 30 para vaciar la memoria interna y volver a conectar; soluciona el 90% de los fallos cotidianos.\n• Recomendaciones de ubicación: En alto sobre un mueble, despejado, lejos de microondas o espejos grandes que rebotan la señal.',
        'SIMULADOR_CONECTIVIDAD_WIFI_HOGAR_SENIORS.html',
        'Simulador Wi-Fi y Videollamadas (+65)'
    )

    add_senior_microapp(
        '[NIV-042]',
        'Los 5 Niveles de Blindaje Digital: Contraseñas Fuertes, Verificación en Dos Pasos y Privacidad',
        'Herramienta interactiva de ciberseguridad práctica y tranquilidad para mayores: sustituye las contraseñas imposibles de memorizar por el método de "Frases Llave Memorables" en español (4 palabras familiares fáciles de recordar pero imposibles de hackear), fomenta el uso de la huella dactilar en el móvil (biometría que no se olvida en casa) y advierte con firmeza de la regla sagrada del código SMS del banco que jamás se debe dictar por teléfono.',
        'Actúa como un experto en ciberseguridad bancaria y docente para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar una herramienta interactiva en HTML que enseñe a crear contraseñas memorables mediante frases en español sin agobios y alerte de no compartir jamás el código SMS del banco.',
        'Genera la aplicación interactiva en HTML con comprobador de frases llave en tiempo real, generador de contraseñas memorables en español, interruptor de biometría (huella dactilar), medidor de tiempo de descifrado y advertencia antifraude telefónico.',
        '• 5 Niveles de Blindaje: 1. Peligro Crítico (Claves tipo 123456 o cumpleaños: hackeo en 1 seg), 2. Seguridad Básica Vulnerable (Palabra con número al final), 3. Frase Llave Memorable (Ej: "MiNietoLucasNacioEn2021!": descifrado requeriría 400 años), 4. Doble Factor 2FA (Frase llave + Huella dactilar en el móvil), 5. Blindaje Absoluto y Paz Mental (Gestor seguro, libreta física en cajón de casa y desconfianza total ante llamadas del supuesto banco).\n• Regla de Oro Bancaria: Ningún empleado bancario legítimo te pedirá nunca por teléfono o SMS tus claves ni el código recibido por SMS. Ante la duda, colgar de inmediato.\n• La Libreta Física Segura: Anotar contraseñas en una libreta de papel guardada en un cajón en casa es 100% seguro frente a hackers de internet.',
        'SIMULADOR_CIBERSEGURIDAD_CONTRASENAS_2FA_SENIORS.html',
        'Blindaje de Contraseñas y 2FA (+65)'
    )

    add_senior_microapp(
        '[NIV-043]',
        'Los 6 Niveles de Resolución, Tamaño de Letra y Accesibilidad en Pantallas',
        'Simulador de ergonomía visual y accesibilidad digital adaptado a personas mayores: enseña a ajustar el tamaño de texto del móvil y tablet (de 14px a 22px) para leer periódicos y prospectos sin cansar la vista ni forzar las cervicales, muestra el modo alto contraste blanco/negro y el filtro cálido ámbar nocturno para conciliar el sueño, y explica cómo activar la lupa integrada de la cámara con un solo toque.',
        'Actúa como un oftalmólogo geriátrico y diseñador de accesibilidad digital para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una guía interactiva en HTML que demuestre la importancia de agrandar la letra en el móvil (a 20-22px) y activar el modo cálido nocturno para no cansar la vista.',
        'Genera la aplicación interactiva en HTML con deslizador de tamaño de letra en tiempo real (14px a 26px), caja de previsualización de mensajes, selector de contraste alto y filtro ámbar, y medidor de fatiga visual geriátrica.',
        '• 6 Niveles de Confort Visual: 1. Texto Diminuto de Fábrica (14px: picor de ojos y cefaleas), 2. Tamaño Básico (16px: aún requiere entrecerrar los ojos con presbicia), 3. Confort Estándar (18-20px: lectura natural a 40 cm), 4. Accesibilidad Óptima Senior (22px: lectura relajada sin buscar las gafas de cerca), 5. Modo Contraste Alto + Filtro Ámbar (Protección del sueño frente a luz azul), 6. Accesibilidad Plena (Lupa con luz activada con 3 toques para prospectos y cartas).\n• Prevención de fatiga visual: Regla 20-20-20 (cada 20 minutos mirar a 20 pies / 6 metros durante 20 segundos para relajar el músculo ciliar ocular).\n• Higiene postural: Sostener la pantalla a la altura del pecho sin doblar el cuello hacia abajo para no sobrecargar las vértebras cervicales.',
        'SIMULADOR_ACCESIBILIDAD_PANTALLAS_TEXTO_SENIORS.html',
        'Guía Accesibilidad y Pantallas (+65)'
    )

    add_senior_microapp(
        '[NIV-044]',
        'Los 5 Niveles del Archivo Digital: Copias de Seguridad, Fotos Familiares y la Nube',
        'Guía pedagógica para preservar el patrimonio fotográfico y recuerdos familiares: explica qué es "la nube" sin jerga técnica (como una caja fuerte privada que no se moja ni se quema), enseña a configurar la copia automática nocturna por Wi-Fi de Google Fotos o iCloud para que no gaste datos, y fomenta la maravillosa costumbre de imprimir una vez al año un álbum en papel para hojear en el salón.',
        'Actúa como un archivero digital y pedagogo familiar para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una herramienta interactiva en HTML que explique qué es la nube con metáforas sencillas y enseñe a activar la copia automática de fotos familiares para no perder los recuerdos.',
        'Genera la aplicación interactiva en HTML con calculadora de fotos protegidas, selector de sistemas de respaldo (móvil, pendrive, nube, álbum impreso), explicación tranquilizadora de la nube y medidor de riesgo de pérdida por extravío del teléfono.',
        '• 5 Niveles del Archivo: 1. Riesgo Crítico (Fotos solo en la memoria del móvil; si cae al agua se pierden recuerdos de años), 2. Copia Manual Ocasional (Pendrive una vez al año), 3. Copia Automática en la Nube (Subida silenciosa con Wi-Fi mientras se carga el móvil de noche), 4. Doble Bóveda Digital + Álbum en Papel (Nube + 50 fotos impresas al año), 5. Legado Familiar Inmortal (Álbumes organizados por años compartidos con hijos y nietos).\n• Explicación de la Nube: Si se cambia de teléfono o se avería, introduciendo el correo y la contraseña todas las fotos reaparecen intactas en el nuevo dispositivo.\n• Ahorro de datos: Configurar "Sincronizar solo con Wi-Fi" evita cualquier consumo de datos de la tarifa mensual.',
        'SIMULADOR_COPIAS_SEGURIDAD_FOTOS_NUBE_SENIORS.html',
        'Copias de Seguridad y Recuerdos (+65)'
    )

    add_senior_microapp(
        '[NIV-045]',
        'Los 6 Niveles de Energía en Dispositivos: Cuidado de Baterías, Cargadores y Autonomía',
        'Micro-aplicación interactiva de autonomía y seguridad eléctrica doméstica: enseña a mantener el teléfono con carga suficiente para salir de paseo o al médico con serenidad, desmiente el viejo mito de descargar la batería al 0%, enseña la zona de salud del 20% al 80%, y previene accidentes identificando cables deshilachados y cargadores homologados con sello CE.',
        'Actúa como un ingeniero de hardware y especialista en seguridad doméstica para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una herramienta interactiva en HTML que enseñe a cuidar la batería del móvil, desmitifique viejos bulos y advierta de los riesgos de cables pelados o dejar el móvil cargando bajo la almohada.',
        'Genera la aplicación interactiva en HTML con simulador de porcentaje de batería, estimador de horas de autonomía según pantalla y linterna, comprobador de seguridad de cargadores homologados CE y desmentido de bulos de baterías de litio.',
        '• 6 Niveles de Carga: 1. Alerta Crítica (< 15%: riesgo inminente de apagado, activar ahorro de batería y apagar linterna), 2. Reserva de Emergencia (15-25%: llamadas urgentes breves), 3. Autonomía Media de Recados (25-50%: paseos de 3-4 horas), 4. Zona de Oro de Batería de Litio (50-80%: máxima durabilidad en años), 5. Carga Completa para Excursiones (80-100%: días largos fuera), 6. Cuidado Inteligente Homologado (Cargador CE frío sobre mesita ventilada).\n• Desmentido de Bulos: Las baterías actuales de iones de litio no tienen "efecto memoria"; se pueden enchufar en cualquier momento sin esperar a que se agoten.\n• Prevención de Incendios: Nunca dejar cargando el teléfono bajo la almohada ni en sofás blandos; desechar cables con cables de cobre visibles.',
        'SIMULADOR_BATERIA_CONSUMO_DISPOSITIVOS_SENIORS.html',
        'Guía Baterías y Autonomía (+65)'
    )

    add_senior_microapp(
        '[NIV-046]',
        'Los 5 Niveles de la Robótica Doméstica: Robots Aspiradores, Sensores y Asistencia Vital',
        'Simulador de ayudas técnicas y autonomía en el hogar: muestra cómo un robot aspirador y friegasuelos evita lumbalgias y mareos al limpiar debajo de muebles y camas, cómo las luces con sensor de paso en el pasillo impiden caídas nocturnas, y cómo los relojes con detección de caídas y botón SOS garantizan independencia y tranquilidad para vivir en el propio hogar.',
        'Actúa como un terapeuta ocupacional y pedagogo en gerontotecnología para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar un simulador interactivo en HTML que muestre cómo los robots aspiradores y sensores de luz nocturna evitan dolores de espalda y tropiezos en casa.',
        'Genera la aplicación interactiva en HTML con checklist de equipamiento doméstico (sensores nocturnos, robot aspirador, avisos por voz, reloj SOS), calculadora de horas de esfuerzo físico ahorradas y medidor de autonomía e independencia en el hogar.',
        '• 5 Niveles de Ayuda Doméstica: 1. Esfuerzo Físico Manual Completo (Barrer agachándose, riesgo de lumbagos y mareos), 2. Luces Nocturnas con Sensor de Paso (Pilotos en pasillo y baño que se iluminan al poner el pie en el suelo), 3. Limpieza Automatizada con Robot Aspirador (Suelo limpio mientras sales a pasear, ahorrando 18h al mes), 4. Asistente de Voz y Recordatorios (Avisos de pastillas y música por la voz), 5. Escudo de Autonomía Plena (Reloj con detección de caídas conectado a teleasistencia 24h).\n• Filosofía de la Tecnología Asistencial: Herramientas al servicio del ser humano para prolongar la estancia en el hogar propio con confort, dignidad y seguridad.\n• Ahorro muscular: Evitar levantar muebles pesados o estirarse en posturas forzadas protege discos lumbares y caderas.',
        'SIMULADOR_ROBOTICA_ASISTENTES_HOGAR_SENIORS.html',
        'Robótica y Asistentes del Hogar (+65)'
    )

    add_senior_microapp(
        '[NIV-047]',
        'Los 6 Niveles de Exploración Virtual, Viajes sin Salir de Casa y Estimulación Sensorial',
        'Guía interactiva de reminiscencia y exploración cultural: enseña a utilizar Street View para pasear virtualmente por las calles del pueblo natal, visitar museos como el Prado o la Alhambra con zoom fotorrealista para contemplar cuadros sin prisas, y compartir viajes en la televisión del salón con los nietos narrando anécdotas de la infancia para reforzar la memoria y el vínculo afectivo.',
        'Actúa como un neuropsicólogo y divulgador cultural para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una herramienta interactiva en HTML que anime a los mayores a pasear por su pueblo natal y visitar museos desde la pantalla del salón, explicando los beneficios de la reminiscencia para la memoria.',
        'Genera la aplicación interactiva en HTML con selector de destinos virtuales (calles del pueblo, museos, naturaleza), selección de pantalla (tablet, televisor), medidor de estimulación cognitiva y guía para compartir recuerdos con los nietos.',
        '• 6 Niveles de Viaje Virtual: 1. Álbum en Papel Estático, 2. Búsqueda Guiada de Fotos Actuales en Internet, 3. Paseo Callejero en 360° (Street View por las esquinas y plazas de la juventud), 4. Visita Virtual a Museos (Salas del Prado con zoom microscópico en obras maestras), 5. Sonidos de la Naturaleza y Calma Inmersiva (Olas del mar y bosques que reducen la ansiedad), 6. Viaje Compartido Intergeneracional (Enseñar en la tele a los nietos el pueblo natal).\n• Beneficio neurocognitivo: La evocación de recuerdos episódicos tempranos refuerza la plasticidad sináptica y mejora el estado de ánimo.\n• Uso relajado: Sesiones de 20 a 30 minutos sentado en el sillón con buena iluminación ambiental.',
        'SIMULADOR_VIAJES_VIRTUALES_ESTIMULACION_SENIORS.html',
        'Viajes Virtuales y Estimulación (+65)'
    )

    add_senior_microapp(
        '[NIV-048]',
        'Los 5 Niveles de Eficiencia en Electrodomésticos: Ahorro de Luz y Manejo Sencillo',
        'Calculadora de economía doméstica y uso eficiente de la energía: desmitifica el programa "Eco" de la lavadora y lavavajillas (demostrando por qué lavar a 30°C ahorra el 60% de electricidad al no calentar agua con resistencias), enseña a desactivar el consumo fantasma de televisores con regletas de botón (ahorro de hasta 45 € al año) y ajusta el frigorífico a 4°C para no generar escarcha innecesaria.',
        'Actúa como un asesor energético y divulgador de economía doméstica para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una calculadora interactiva en HTML que explique cómo usar el programa Eco de la lavadora y apagar las regletas para recortar la factura de la luz sin pasar frío ni complicaciones.',
        'Genera la aplicación interactiva en HTML con calculadora de ahorro eléctrico anual en euros, selector de programas de lavado (eco vs caliente), ajuste óptimo del frigorífico a 4°C, semáforo de etiquetas energéticas y explicación del consumo fantasma (standby).',
        '• 5 Niveles de Eficiencia: 1. Despilfarro Involuntario (Lavados a 60°C con media carga y standby permanente), 2. Hábitos Básicos (Apagar luces y tapar cacerolas al hervir), 3. Uso Inteligente del Programa Eco (Lavado a 30°C con ahorro del 60% en luz protegiendo la ropa), 4. Regletas con Interruptor y Termostato a 21°C (Cero consumo fantasma en televisor ahorrando 45 €/año), 5. Eficiencia Máxima con Tecnología Inverter (Aparatos clase A/B y bombillas LED cálidas en toda la casa).\n• La Ciencia del Modo Eco: El 85% de la electricidad de una lavadora se destina a la resistencia para calentar el agua; el modo Eco lava con agua tibia y más tiempo, gastando una fracción de kilovatios.\n• Frigorífico Saludable: 4°C en la zona de refrigeración y -18°C en el congelador garantizan seguridad alimentaria sin sobrecostes.',
        'SIMULADOR_EFICIENCIA_ELECTRODOMESTICOS_FACTURA_SENIORS.html',
        'Calculadora Eficiencia Electrodomésticos (+65)'
    )

    add_senior_microapp(
        '[NIV-049]',
        'Los 6 Niveles de Trámites Digitales: Certificado Digital, Cl@ve y Citas Médicas sin Colas',
        'Guía de soberanía ciudadana y alfabetización administrativa: enseña a pedir cita en el centro de salud en 30 segundos con la aplicación móvil oficial de la comunidad autónoma, a descargar el justificante de la pensión o vida laboral mediante el sistema Cl@ve Pin con código al móvil por SMS (sin instalaciones engorrosas), y enseña a identificar las webs oficiales seguras del Estado que terminan siempre en ".gob.es".',
        'Actúa como un mediador administrativo y pedagogo de alfabetización digital para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar un simulador interactivo en HTML que enseñe a pedir cita médica y descargar certificados de pensión mediante Cl@ve Pin sin necesidad de hacer colas en ventanilla.',
        'Genera la aplicación interactiva en HTML con simulador de trámites frecuentes (cita médica, justificante de pensión, empadronamiento), comparador de métodos de acceso (presencial vs Cl@ve SMS vs Certificado Digital), calculadora de horas ahorradas en colas y filtro de webs oficiales seguras (.gob.es).',
        '• 6 Niveles de Autonomía: 1. Dependencia Presencial Total (Madrugar a las 7:30 para colas en ventanilla bajo el frío), 2. Cita Telefónica Automatizada (Esperas en línea y contestadores saturados), 3. Cita Médica por App Móvil (Gestión en 30 segundos sentado en el sofá con tarjeta sanitaria), 4. Sistema Cl@ve Pin por SMS (Acceso a la Seguridad Social con código de 3 letras al móvil), 5. Certificado Digital Instalado (Descargas oficiales de empadronamiento y pensión con un clic), 6. Soberanía Digital y Serenidad (Gestión autónoma de derechos ciudadanos).\n• Identificación de Webs Oficiales: Todas las páginas oficiales de Ministerios y Seguridad Social terminan en ".gob.es"; nunca pagar a intermediarios comerciales por pedir citas gratuitas.\n• Salud y Comodidad: Evitar desplazamientos bajo lluvia o heladas de invierno protege contra resfriados y caídas en aceras.',
        'SIMULADOR_TRAMITES_DIGITALES_CERTIFICADO_SENIORS.html',
        'Trámites Digitales y Cl@ve Pin (+65)'
    )

    add_senior_microapp(
        '[NIV-050]',
        'Los 5 Niveles de Comunicación Digital: WhatsApp Familiar, Grupos y Convivencia Serena',
        'Guía interactiva de convivencia digital y comunicación positiva: enseña el gran truco del micrófono del teclado para dictar mensajes con la voz sin tener que teclear despacio en pantalla pequeña, explica cómo "Silenciar grupos para siempre" para disfrutar de la tranquilidad sin ruidos molestos y sin que nadie se entere, y facilita un detector de bulos y cadenas alarmistas para mantener las conversaciones limpias de bulos.',
        'Actúa como un pedagogo de convivencia digital y relaciones familiares para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una guía interactiva en HTML que enseñe a silenciar grupos ruidosos de WhatsApp sin salirse, dictar mensajes por voz y no reenviar cadenas o noticias falsas.',
        'Genera la aplicación interactiva en HTML con simulador de dictado por voz frente al teclado tradicional, botón interactivo para "Silenciar grupo para siempre", detector de cadenas de mensajes falsos y decálogo de convivencia serena en WhatsApp.',
        '• 5 Niveles de Convivencia: 1. Agobio Sonoro y Saturación (Grupos sonando a todas horas y angustia por responder), 2. Escritura Tecla a Tecla con Fatiga (Borrar errores repetidamente en pantalla pequeña), 3. Comunicación Cómoda por Dictado de Voz (Hablar con soltura y que el móvil escriba solo con ortografía), 4. Grupos Silenciados para Siempre (Paz mental absoluta; los mensajes se leen solo cuando apetece), 5. Sabiduría Digital y Cariño Familiar (Cero cadenas alarmistas, fotos de momentos bonitos y llamadas de voz reconfortantes).\n• Filtro Antibulados: Si un mensaje pide "Reenvía a todos tus contactos o cerrarán WhatsApp" o promete regalos gratis, es 100% un engaño; no reenviar jamás.\n• Filosofía Senior: El teléfono está para servirte y acercarte a tus seres queridos, no para estresarte; no existe ninguna obligación de contestar de inmediato.',
        'SIMULADOR_COMUNICACION_WHATSAPP_CONVIVENCIA_SENIORS.html',
        'Guía WhatsApp y Convivencia Serena (+65)'
    )

    # =========================================================================
    # LOTE 6 (SESIONES 51 A 60): MICRO-APLICACIONES INTERACTIVAS SENIORS (+65)
    # =========================================================================
    add_senior_microapp(
        '[NIV-051]',
        'Los 6 Niveles de Altura, Escaleras y Accesibilidad: Diseñar un Hogar sin Barreras',
        'Guía interactiva de accesibilidad y arquitectura para la autonomía de los mayores: enseña a eliminar resaltes peligrosos en el suelo, sustituir la bañera por un plato de ducha enrasado a cota cero, colocar doble pasamanos continuo en escaleras y aprovechar las subvenciones comunitarias para bajar los ascensores a nivel de calle sin peldaños previos.',
        'Actúa como un arquitecto técnico y terapeuta ocupacional especializado en diseño accesible para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar un simulador interactivo en HTML que enseñe a eliminar barreras arquitectónicas en el hogar, sustituyendo la bañera por ducha a cota cero y adaptando desniveles con rampas suaves.',
        'Genera la aplicación interactiva en HTML con selector de vivienda (piso cota cero, portal con escalones, chalet), deslizador de altura de resaltes (0-25 cm), semáforo de riesgo de caídas domésticas y guía de ayudas públicas para reformas de accesibilidad.',
        '• 6 Niveles de Accesibilidad: 1. Cota Cero Absoluta (Plato de ducha enrasado al nivel del suelo sin bordillo ni escalón alguno), 2. Bordillo con Rampa Suave (Rampas antideslizantes con pendiente inferior al 6%), 3. Escalera Segura con Doble Pasamanos (Pasamanos continuo a ambos lados e iluminación peldaño a peldaño), 4. Silla Salvaescaleras Motorizada (Mecanismo electromecánico suave para subir plantas sin sobreesfuerzo articular), 5. Ascensor a Cota Cero en Portal (Bajar el ascensor comunitario a nivel de calle eliminando peldaños previos), 6. Hábitat Universal Pleno (+65) (Puertas de 82 cm para andador/silla y giro de 1,5 metros).\n• La Regla de Oro de la Cota Cero: El 70% de las caídas domésticas ocurren por tropezar con bordillos de ducha o alfombrillas sueltas.\n• Subvenciones: Ayudas autonómicas y municipales financian hasta el 80% de la adaptación.',
        'SIMULADOR_ARQUITECTURA_HOGAR_ACCESIBLE_SENIORS.html',
        'Accesibilidad y Hogar sin Barreras (+65)'
    )

    add_senior_microapp(
        '[NIV-052]',
        'Los 5 Niveles de la Ciudad Amigable con las Personas Mayores: Calles, Bancos y Vida de Barrio',
        'Herramienta de urbanismo participativo según el estándar de la OMS: evalúa la amabilidad del barrio analizando la presencia de bancos con respaldo cada 150-200 metros para descansar con dignidad, tiempos semafóricos adaptados a paso tranquilo, aceras anchas sin coches aparcados y la vitalidad del comercio de proximidad a menos de 400 metros.',
        'Actúa como un sociólogo urbano y consultor de la Red Mundial de Ciudades Amigables con las Personas Mayores (OMS).\nExplícame en 3 viñetas cómo crear una herramienta interactiva en HTML que evalúe si un vecindario es accesible y seguro para salir a pasear, valorando bancos, semáforos y tiendas cercanas.',
        'Genera la aplicación interactiva en HTML con simulador de radio de paseo (15 minutos), comprobador de amabilidad del barrio (bancos con respaldo, pasos rebajados, fuentes potables) y decálogo OMS de convivencia comunitaria.',
        '• 5 Niveles de Amabilidad Urbana: 1. Ciudad Barrera (Aceras estrechas rotas y semáforos de menos de 12 segundos), 2. Urbanismo Básico sin Confort (Aceras continuas pero sin asientos de descanso ni fuentes), 3. Ciudad de Proximidad / 15 Minutos (Farmacia, frutería y centro de salud a menos de 400 m a pie), 4. Entorno Verde con Bancos cada 150 m (Bancos ergonómicos con respaldo y apoyabrazos para levantarse fácilmente bajo árboles de sombra), 5. Ciudad Amigable y Cuidadora (Pasos sobreelevados, baños públicos limpios y comerciantes con paciencia y trato humano).\n• El Banco como Medicina Social: Poder sentarse 3 minutos a descansar los gemelos y charlar con vecinos es el mayor antidepresivo natural.\n• Pasos de Peatones: La sobreelevación obliga al coche a frenar y deja el cruce a nivel continuo.',
        'SIMULADOR_CIUDAD_AMIGABLE_URBANISMO_SENIORS.html',
        'Ciudad Amigable y Vida de Barrio (+65)'
    )

    add_senior_microapp(
        '[NIV-053]',
        'Los 6 Niveles de Movilidad, Transporte Público y Conducción Segura en la Madurez',
        'Guía de transporte inteligente y seguridad vial: ayuda a elegir el medio óptimo para cada trayecto, promueve el calzado antideslizante al caminar, enseña a aprovechar el autobús de piso bajo y el Servicio Atendo gratuito de Renfe en trenes, y fomenta la conducción serena y autorregulada de día, desmitificando el paso al taxi como una ganancia de libertad y ahorro económico.',
        'Actúa como un formador vial y especialista en movilidad sostenible para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una aplicación interactiva en HTML que ayude a elegir el medio de transporte más cómodo y seguro para cada situación, fomentando el transporte público y la conducción autorregulada de día.',
        'Genera la aplicación interactiva en HTML con selector de trayecto y clima, comparativa económica de mantener coche propio vs usar transporte bonificado y taxis, y guía del Servicio Atendo de ayuda en estaciones de tren.',
        '• 6 Niveles de Movilidad Serena: 1. Caminar con Seguridad Diaria (Calzado con relieve antideslizante y bastón ergonómico si aporta confianza), 2. Autobús Urbano de Piso Bajo (Rampa arrodillada kneeling y asientos reservados azules), 3. Metro y Tranvía con Ascensores Operativos (Verificación de accesibilidad previa en app municipal), 4. Tren con Servicio Atendo Renfe (Asistencia gratuita para acompañamiento y maletas), 5. Conducción Autorregulada y Serena (Evitar la noche con faros deslumbrantes y preferir mañanas despejadas), 6. Copiloto Feliz y Alternativa del Taxi/VTC (Ahorro de 2.500 a 3.500 €/año en seguro, garaje e ITV usándolos en taxis de puerta a puerta sin estrés).\n• Filosofía Senior: Dejar el coche cuando genera ansiedad no es perder autonomía, sino ganar calidad de vida.',
        'SIMULADOR_MOVILIDAD_TRANSPORTE_SEGURO_SENIORS.html',
        'Movilidad y Conducción Segura (+65)'
    )

    add_senior_microapp(
        '[NIV-054]',
        'Los 5 Niveles del Agua en el Hogar: Calidad del Grifo, Ahorro e Hidratación Saludable',
        'Guía interactiva sobre el agua potable y la salud geriátrica: advierte sobre la pérdida biológica de la sed con la edad y establece la rutina de 6 a 8 vasos diarios repartidos, defiende la pureza del agua municipal frente al coste y peso de las garrafas plásticas, enseña a regular los grifos con tope a 38°C para evitar quemaduras y a instalar aireadores perlizadores para recortar el consumo un 50%.',
        'Actúa como un médico geriatra e ingeniero sanitario para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una calculadora interactiva en HTML que promueva la hidratación regular sin esperar a tener sed, defienda la seguridad del agua del grifo y prevenga quemaduras con grifería termostática.',
        'Genera la aplicación interactiva en HTML con planificador de ingesta de líquidos diaria (vasos e infusiones), calculadora de ahorro económico de agua de grifo vs garrafas plásticas y recomendaciones de seguridad antiquemaduras.',
        '• 5 Niveles de Cultura del Agua: 1. Alerta de Deshidratación Silenciosa (El hipotálamo pierde sensibilidad con la edad; no esperar a tener sed), 2. Garantía Sanitaria del Agua del Grifo (Más de 40 controles analíticos diarios en España; pura, ecológica y económica), 3. Rutina Hidratante de 6 a 8 Vasos (Vaso al despertar, infusiones a media mañana y jarra visible en la mesa), 4. Grifería Termostática Segura (Tope a 38°C para evitar quemaduras accidentales en piel fina), 5. Ahorro con Boquillas Perlizadoras (Filtros de 2 € que reducen el gasto un 50% con la misma fuerza de chorro).\n• Salud y Espalda: Cargar garrafas de 5 litros daña la columna; el agua de red en España es de altísima calidad sanitaria.',
        'SIMULADOR_AGUA_POTABLE_HIDRATACION_SENIORS.html',
        'Calidad del Agua e Hidratación (+65)'
    )

    add_senior_microapp(
        '[NIV-055]',
        'Los 6 Niveles de la Medicina Preventiva: Revisiones, Vacunación y Relación con el Médico de Cabecera',
        'Guía de medicina preventiva y cuidado integral del adulto mayor: fomenta el estilo de vida activo y la dieta mediterránea, enseña el método de la libreta con 2 preguntas escritas para la consulta del médico de cabecera, resume el calendario vacunal oficial (gripe, neumococo, herpes zóster), programa chequeos de tensión arterial y cribados de colon, y desmitifica cirugías ambulatorias modernas como cataratas.',
        'Actúa como un especialista en medicina preventiva y médico de atención primaria para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una guía interactiva en HTML que recuerde las revisiones periódicas, el calendario vacunal del adulto mayor y pautas para aprovechar al máximo la consulta con el médico de cabecera.',
        'Genera la aplicación interactiva en HTML con lista interactiva de chequeos médicos recomendados por edad, calendario vacunal del adulto mayor, bloc de notas para la consulta médica y desmitificación de cirugías ambulatorias modernas.',
        '• 6 Niveles de Salud Preventiva: 1. Autocuidado y Dieta Serena (Paseos de 40 min y dieta mediterránea de legumbres y verduras), 2. Consulta con Libreta de Dudas (Anotar preguntas antes de entrar para salir sin dudas), 3. Calendario Vacunal Oficial (Gripe anual, neumococo, herpes zóster y refuerzos estacionales), 4. Chequeos Periódicos Programados (Tensión mensual, analítica anual y revisión ocular/auditiva), 5. Detección Precoz y Cribados (Sangre oculta en heces a partir de 50 años y revisiones periódicas), 6. Cirugías Mínimamente Invasivas (Operaciones de cataratas con gotas en 15 minutos sin ingreso).\n• Alianza con tu Médico: La atención primaria es el mayor escudo de longevidad; consultar con confianza y serenidad.',
        'SIMULADOR_MEDICINA_PREVENTIVA_SALUD_SENIORS.html',
        'Medicina Preventiva y Revisiones (+65)'
    )

    add_senior_microapp(
        '[NIV-056]',
        'Los 5 Niveles de la Huerta Tradicional, Alimentos de Temporada y Consumo de Proximidad',
        'Guía de nutrición tradicional y economía del hogar: explica por qué consumir frutas y verduras de temporada en España multiplica el sabor y los nutrientes reduciendo la factura un 40%, apoya la compra en mercados municipales de abastos con trato humano de confianza y anima a iniciar un macetohuerto de hierbas aromáticas en balcón como ejercicio físico y placer sensorial.',
        'Actúa como un agrónomo divulgador y experto en nutrición mediterránea para personas mayores (+65).\nExplícame en 3 viñetas cómo diseñar una herramienta interactiva en HTML que muestre el calendario de frutas y verduras de temporada en España, defendiendo el mercado municipal y el cultivo en macetas de balcón.',
        'Genera la aplicación interactiva en HTML con rueda estacional de alimentos de temporada (primavera a invierno), comparativa de sabor y ahorro en la cesta de la compra, y guía para iniciar un macetohuerto de hierbas aromáticas en el balcón.',
        '• 5 Niveles de Sabiduría Agrícola: 1. Ultraprocesados Industriales (Sal y grasas saturadas que sobrecargan la tensión), 2. Frescos de Cadena Larga (Madurados en cámaras frigoríficas con pérdida de sabor y sobreprecio), 3. Alimentos de Temporada en España (Alcachofas y naranjas en invierno, tomates y melón en verano: más vitaminas y 40% más baratos), 4. Mercado Tradicional y Comercio de Barrio (El frutero te aconseja la pieza en su punto justo y mantiene la vida comunitaria), 5. Macetohuerto en Balcón (Macetas de romero, perejil o tomates cherry: ejercicio suave y estímulo para la mente).\n• La Tradición Culinaria: El puchero de legumbres 2 o 3 veces por semana es salud digestiva y ahorro familiar.',
        'SIMULADOR_AGRICULTURA_HUERTA_ALIMENTACION_SENIORS.html',
        'Huerta Tradicional y Temporada (+65)'
    )

    add_senior_microapp(
        '[NIV-057]',
        'Los 6 Niveles del Mantenimiento Seguro del Hogar: Materiales, Reformas y Confort Térmico',
        'Simulador de mantenimiento preventivo y reformas amigables: alerta sobre pavimentos resbaladizos tipo terrazo pulido, promueve suelos antideslizantes Clase 2/3 en baños, aislamiento con ventanas de doble acristalamiento Climalit para ahorrar calefacción y eliminar ruidos, pinturas ecológicas sin olores (cero COVs), colocación de enchufes a 70 cm del suelo y tramitación de subvenciones de accesibilidad.',
        'Actúa como un arquitecto de interiores y perito en reformas seguras para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una calculadora interactiva en HTML que oriente sobre materiales antideslizantes, aislamiento térmico con doble acristalamiento y colocación ergonómica de enchufes para el confort diario.',
        'Genera la aplicación interactiva en HTML con simulador de reformas prioritarias en el hogar, test de aislamiento de ventanas y pavimento antideslizante, y guía de subvenciones públicas para accesibilidad y eficiencia.',
        '• 6 Niveles de Confort Seguro: 1. Pavimentos Deslizantes de Alto Riesgo (Terrazo brillante o mármol que resbalan con una gota de agua), 2. Suelos Antideslizantes Certificados (Clase 2 o 3 mate rugoso seguro en baño y cocina), 3. Ventanas con Doble Cristal Climalit (Aislamiento térmico que ahorra el 35% en calefacción y quita ruidos de la calle), 4. Pinturas Ecológicas al Agua (Sin compuestos químicos volátiles irritantes), 5. Enchufes a 70 cm e Iluminación LED (Evitar agacharse al suelo protegiendo la espalda lumbar), 6. Subvenciones Públicas de Rehabilitación (Ayudas oficiales para costear el cambio de bañera por ducha).\n• Ergonomía en Casa: Pequeños cambios en materiales aportan una seguridad inestimable.',
        'SIMULADOR_MATERIALES_REFORMAS_HOGAR_SENIORS.html',
        'Mantenimiento del Hogar y Reformas (+65)'
    )

    add_senior_microapp(
        '[NIV-058]',
        'Los 5 Niveles de Astronomía Cotidiana, Fases Lunares y Maravilla del Cosmos para Seniors',
        'Guía de contemplación del cielo y asombro nocturno: enseña a identificar la Estrella Polar, Venus y Orión a simple vista desde la terraza, explica la regla mnemotécnica de las fases lunares ("la luna es mentirosa: en forma de C mengua, en forma de D crece"), anima al uso de prismáticos ligeros 7x50 para ver cráteres sin telescopios pesados y promueve la serenidad cósmica como fuente de paz mental.',
        'Actúa como un astrónomo divulgador y docente para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una guía interactiva en HTML para observar la Luna y las estrellas a simple vista o con prismáticos ligeros, explicando las fases lunares con trucos mnemotécnicos sencillos.',
        'Genera la aplicación interactiva en HTML con simulador de fases lunares (regla de la C y la D), guía de estrellas y planetas visibles a simple vista desde el balcón y pautas ergonómicas para disfrutar del cielo nocturno sin sobrecargar el cuello.',
        '• 5 Niveles de Contemplación Cósmica: 1. El Cielo a Simple Vista (Reconocer la Estrella Polar para situar el norte y el brillo de Venus al atardecer), 2. El Baile de las Fases Lunares (Regla mnemotécnica de la C y la D en el ciclo de 29,5 días), 3. Prismáticos Ligeros 7x50 con Apoyo Cómodo (Descubrir los mares lunares y satélites de Júpiter sin trípodes pesados), 4. Estrellas Fugaces en el Pueblo (Las Perseidas en agosto con tumbona y manta tibia), 5. Serenidad Cósmica en la Madurez (Contemplar la inmensidad del universo aporta paz y demuestra que la curiosidad no envejece jamás).\n• Equipamiento Práctico: Unos prismáticos de mano apoyados en la barandilla superan en comodidad a cualquier telescopio complejo.',
        'SIMULADOR_ASTRONOMIA_EXPLORACION_COSMOS_SENIORS.html',
        'Astronomía Cotidiana y Cosmos (+65)'
    )

    add_senior_microapp(
        '[NIV-059]',
        'Los 6 Niveles de la Despensa Saludable: Conservación de Alimentos, Fechas de Caducidad y Congelación Segura',
        'Guía práctica de seguridad alimentaria y orden doméstico: distingue con claridad la fecha de caducidad estricta del consumo preferente para evitar tirar comida buena, enseña a organizar el frigorífico por zonas térmicas (carnes abajo a 2°C, verduras al cajón a 7°C), explica el protocolo de descongelar siempre dentro de la nevera con 24 horas de antelación y fomenta la cocina de aprovechamiento casera.',
        'Actúa como un especialista en seguridad alimentaria y divulgador culinario para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una guía interactiva en HTML que aclare la diferencia entre fecha de caducidad y consumo preferente, enseñe a colocar los alimentos en la nevera y descongelar con seguridad.',
        'Genera la aplicación interactiva en HTML con clasificador interactivo de alimentos según su método de conservación (despensa, frío, congelador), semáforo de caducidad vs consumo preferente y protocolo higiénico de descongelación en nevera.',
        '• 6 Niveles de Despensa Segura: 1. Caducidad vs Consumo Preferente (Caducidad por seguridad estricta en frescos; Consumo preferente en conservas/pasta que duran meses sin riesgo), 2. Conservas Tradicionales en Vidrio (Fondo de despensa saludable de legumbres y pescado que dura años sin frío), 3. Organización Térmica del Frigorífico (Carnes y pescados a 2°C en bandeja inferior, platos cocinados al centro a 4°C y verduras en cajón templado), 4. Congelación en Porciones y Descongelación en Nevera (Descongelar despacio dentro de la nevera; nunca sobre la encimera al aire), 5. Recipientes de Cristal con Cinta y Fecha (Identificar sobras para consumir en 48-72 h), 6. Cocina de Aprovechamiento (+65) (Croquetas, caldos y purés caseros con desperdicio cero).\n• Ahorro Doméstico: Evitar tirar botes de conservas perfectamente sanos ahorra más de 200 € al año.',
        'SIMULADOR_CONSERVACION_ALIMENTOS_DESPENSA_SENIORS.html',
        'Despensa Saludable y Conservación (+65)'
    )

    add_senior_microapp(
        '[NIV-060]',
        'Los 5 Niveles de la Lectura Activa, Memoria y el Legado Escrito de la Historia Personal',
        'Guía interactiva sobre el placer de las letras, estimulación cognitiva y memoria viva: explica los beneficios cerebrales de leer 30 minutos al día, fomenta el uso de libros de letra grande (Large Print) y la visita a la biblioteca municipal de barrio, desmitifica el lector de tinta electrónica (e-reader) que permite agrandar la letra y no pesa, y anima a redactar un cuaderno de memorias con anécdotas y recetas para los nietos.',
        'Actúa como un pedagogo humanista y bibliotecario divulgador para personas mayores (+65).\nExplícame en 3 viñetas cómo crear una herramienta interactiva en HTML que motive la lectura diaria, recomiende libros de letra grande o e-readers que no pesan y anime a escribir un cuaderno de memorias familiares.',
        'Genera la aplicación interactiva en HTML con planificador de lectura diaria y estimulación de memoria, comparativa ergonómica de formatos (papel, tinta electrónica, audiolibro) y plantilla guiada para escribir los recuerdos familiares.',
        '• 5 Niveles del Libro y la Memoria: 1. Lectura como Gimnasio Cerebral (Leer 30 min al día reduce el estrés un 68% y mantiene vivo el vocabulario), 2. Papel de Letra Grande y Biblioteca de Barrio (Préstamo gratuito y socialización en clubes de lectura), 3. E-reader con Pantalla de Tinta Electrónica (Letra ajustable al tamaño óptimo y peso ligero de 170 g para no cansar las manos), 4. Audiolibros con Voz Humana Cálida (Novelas y biografías narradas para escuchar paseando o descansando en el sillón), 5. El Legado Escrito de la Vida para los Nietos (Plasmar anécdotas de juventud, recetas y valores familiares: el mayor tesoro imborrable para las generaciones futuras).\n• El Saber no Envejece: Mantener la mente activa leyendo y escribiendo es la mayor garantía de vitalidad y serenidad.',
        'SIMULADOR_HISTORIA_LIBRO_LEGADO_SABIDURIA_SENIORS.html',
        'Lectura Activa y Legado Personal (+65)'
    )

    return items
