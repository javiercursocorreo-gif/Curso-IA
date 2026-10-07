# -*- coding: utf-8 -*-
"""
build_pat_60_master.py
Genera los 60 ítems oficiales de la etiqueta:
[PAT] CULTURA PATRIMONIAL, DERECHOS Y FINANZAS CLARAS 101

Diseñado para personas mayores (60+):
- Cero especulación, cero cripto, cero recomendaciones de inversión bursátil arriesgada.
- 100% Educación, Tranquilidad Legal, Derechos Bancarios, Notaría y Protección del Ahorro.
- Distribución rotatoria (intercalada aleatoriamente) de las 4 temáticas para mantener variedad pedagógica en cada sesión.
- Metodología limpia en 2 Pasos (Paso 1: encargo breve a Gemini; Paso 2: generar esquema/infografía visual; + Reto de autonomía).
"""

RAW_PAT_TOPICS = [
    # --- TEMÁTICA A: NOTARÍA, TESTAMENTOS Y HERENCIAS (15 temas) ---
    {
        "cat": "Notaría y Herencias",
        "title": "El Testamento Abierto ante Notario: Claves, precio y mitos",
        "concept": "Aprender qué es el testamento notarial abierto, desmontar el mito del coste excesivo y entender su valor de paz familiar.",
        "p1": "Actúa como un notario y pedagogo experto. Explícame de forma muy sencilla y afectuosa cómo se hace un testamento abierto en España, qué precio orientativo tiene y por qué es el mejor regalo de paz para los hijos. Redáctame una guía breve en 4 puntos claros y comprensibles sin latinajos.",
        "p2": "Ahora genera una infografía limpia y elegante en estilo lámina notarial clásica con tipografía clara en español: un escritorio de madera noble con pluma, sello notarial y un esquema explicativo de los 3 pasos para hacer testamento sin complicaciones.",
        "reto": "Pídele a Gemini: '¿Qué pasa si una persona fallece sin haber hecho testamento? Explícamelo en 3 frases sencillas'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "Los Tres Tercios de la Herencia: Legítima, Mejora y Libre Disposición",
        "concept": "Descifrar el sistema hereditario en España para comprender cómo se reparte legalmente el patrimonio familiar.",
        "p1": "Actúa como un profesor de derecho civil para personas mayores. Explícame con la metáfora de una tarta dividida en 3 porciones los tres tercios de una herencia en España: la Legítima estricta, la Mejora y la Libre Disposición, en lenguaje 100% de la calle.",
        "p2": "Genera una infografía didáctica y muy visual que represente una tarta o gráfico circular 3D dividido exactamente en 3 porciones de colores suaves con rótulos grandes en español: 'Legítima', 'Mejora' y 'Libre Disposición'.",
        "reto": "Pregúntale a Gemini: 'Si quiero dejarle una joya o un recuerdo especial a una persona que no es de mi familia, ¿de cuál de los 3 tercios sale?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "El Usufructo del Cónyuge Viudo: Vivir tranquilo en la propia casa",
        "concept": "Diferenciar entre ser dueño (nuda propiedad) y tener derecho a disfrutar de la vivienda (usufructo vitalicio).",
        "p1": "Actúa como un asesor jurídico familiar. Explícame de forma tranquilizadora la diferencia entre usufructo vitalicio y nuda propiedad, y por qué el cónyuge viudo tiene pleno derecho a vivir en su casa de siempre sin que nadie le pueda obligar a salir.",
        "p2": "Crea una ilustración conceptual y cálida: una casa acogedora con jardín donde se ve un salón iluminado que transmite seguridad, acompañada de un esquema visual que compare con iconos claros 'Usufructo (vivir y usar)' frente a 'Propiedad'. Rótulos en español.",
        "reto": "Pídele a Gemini: '¿El viudo con usufructo puede alquilar la vivienda a un tercero si se va a vivir con sus hijos? Explícamelo'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "Donación en Vida vs. Dejar en Herencia: La balanza fiscal",
        "concept": "Comprender las diferencias tributarias y de seguridad personal entre regalar bienes en vida o transmitirlos tras el fallecimiento.",
        "p1": "Actúa como un economista divulgador. Explícame con pros y contras muy claros si conviene más donar un piso o dinero a los hijos en vida o esperar a la herencia. Incluye la advertencia de nunca descapitalizarse por ayudar a terceros.",
        "p2": "Genera una imagen con una balanza dorada antigua en equilibrio sobre una mesa de madera: en un plato una escritura de 'Donación en Vida' y en el otro una de 'Herencia Futura', con etiquetas flotantes que resuman ventajas e impuestos en español.",
        "reto": "Pídele a Gemini: 'Dime las 3 preguntas clave que debo hacerle a un gestor antes de donar dinero a un hijo'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "El Poder Notarial Preventivo: Blindar tus decisiones futuras",
        "concept": "La herramienta legal fundamental para designar de antemano quién gestionará tus asuntos en caso de enfermedad o pérdida de facultades.",
        "p1": "Actúa como un jurista especializado en mayores. Explícame qué es un poder notarial preventivo, en qué se diferencia de un poder ordinario y por qué protege mi voluntad antes de que sobrevenga una demencia o incapacidad.",
        "p2": "Genera una ilustración vectorial moderna de alta calidad: un escudo protector transparente sobre una firma notarial y documentos familiares, con una infografía en español que detalle los 3 blindajes del poder preventivo.",
        "reto": "Pregunta a Gemini: '¿Puedo revocar o cancelar un poder notarial preventivo si cambio de opinión mientras esté lúcido?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "La Aceptación de Herencia a Beneficio de Inventario",
        "concept": "El mecanismo legal para evitar que los herederos respondan con su propio patrimonio si el fallecido tenía deudas.",
        "p1": "Actúa como un abogado pedagogo. Explícame qué significa 'aceptar una herencia a beneficio de inventario' y cómo esta fórmula protege a los hijos y nietos de heredar posibles deudas imprevistas.",
        "p2": "Genera una infografía ilustrada con estilo editorial limpio: un muro de contención elegante que separa un cofre con bienes de una zona de facturas pendientes, con flechas y textos explicativos 100% en español.",
        "reto": "Pregúntale a Gemini: '¿Cuánto tiempo hay de plazo legal en España para gestionar una herencia tras el fallecimiento?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "La Declaración de Herederos Abintestato (Sin testamento)",
        "concept": "Conocer los trámites notariales necesarios cuando un familiar fallece sin haber otorgado testamento previo.",
        "p1": "Actúa como un notario cercano. Explícame qué es el acta de notoriedad de declaración de herederos abintestato, qué documentos hay que llevar al notario y por qué hacer testamento en vida ahorra meses de papeleos.",
        "p2": "Genera un esquema infográfico tipo diagrama de flujo con 4 pasos numerados y colores pastel: 1. Certificados, 2. Libro de Familia, 3. Dos testigos, 4. Acta notarial. Todo rotulado con gran nitidez en español.",
        "reto": "Pídele a Gemini: '¿Quiénes pueden ser los dos testigos que exige el notario para la declaración de herederos?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "El Impuesto sobre Sucesiones y las Bonificaciones por Comunidades",
        "concept": "Entender por qué los impuestos de herencia varían según la comunidad autónoma de residencia y los grados de parentesco.",
        "p1": "Actúa como un asesor fiscal divulgador. Explícame de forma serena y didáctica qué es el Impuesto de Sucesiones, cómo funcionan los grupos de parentesco (hijos y cónyuges frente a sobrinos) y por qué en muchas autonomías está bonificado al 99%.",
        "p2": "Genera un mapa infográfico estilizado de España en relieve con iconos de porcentajes suaves y una tabla comparativa esquemática al pie con títulos claros en español: 'Grupo I y II (Hijos y cónyuge)' vs 'Grupo III y IV (Colaterales y extraños)'.",
        "reto": "Pregúntale a Gemini: '¿Dónde tributa la herencia si el fallecido vivía en una comunidad pero los hijos en otra?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "La Plusvalía Municipal en Inmuebles Heredados",
        "concept": "Descifrar el impuesto sobre el incremento de valor de los terrenos urbanos al heredar una vivienda familiar.",
        "p1": "Actúa como un gestor administrativo. Explícame qué es la Plusvalía Municipal (IIVTNU) al heredar un piso, cuándo se paga en el Ayuntamiento y qué ocurre si el piso no ha ganado valor desde que se compró.",
        "p2": "Genera una ilustración esquemática estilo plano arquitectónico con un edificio residencial y un sello municipal que muestre de forma clara las dos opciones de cálculo legal (método real vs objetivo) en español.",
        "reto": "Pídele a Gemini: '¿Hay alguna bonificación municipal si el heredero convivía con el fallecido en la vivienda habitual?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "El Albacea y el Contador-Partidor: Mediadores de paz familiar",
        "concept": "La figura del mediador designado en el testamento para evitar disputas entre hermanos durante el reparto.",
        "p1": "Actúa como un mediador de sucesiones. Explícame para qué sirve nombrar un contador-partidor o un albacea en el testamento, quién puede desempeñar ese rol y cómo previene discusiones y bloqueos familiares.",
        "p2": "Genera una ilustración clásica de un apretón de manos cordial sobre una mesa con planos y documentos ordenados, con un cuadro sinóptico que defina en 3 puntos las funciones del contador-partidor en español.",
        "reto": "Pregúntale a Gemini: '¿Un hijo puede ser contador-partidor de la herencia de sus propios hermanos?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "El Registro de la Propiedad: Inscribir los bienes a tu nombre",
        "concept": "Por qué es vital inscribir las viviendas en el Registro de la Propiedad y qué garantías otorga frente a terceros.",
        "p1": "Actúa como un registrador de la propiedad divulgador. Explícame la diferencia entre el Catastro y el Registro de la Propiedad, y por qué inscribir un inmueble heredado es el paso definitivo para ser el dueño legal incuestionable.",
        "p2": "Genera una infografía comparativa con dos columnas claras: 'El Catastro (fines fiscales y metros)' frente a 'El Registro de la Propiedad (titularidad jurídica y seguridad)'. Estilo profesional y nítido en español.",
        "reto": "Pídele a Gemini: '¿Qué es una Nota Simple del Registro de la Propiedad y cómo puedo solicitarla por internet?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "La Desheredación en España: Requisitos estrictos de la ley",
        "concept": "Desmontar la creencia de que se puede desheredar libremente y conocer las causas tasadas por el Código Civil.",
        "p1": "Actúa como un profesor de derecho sucesorio. Explícame por qué en el derecho común español no se puede desheredar a un hijo por un simple enfado, cuáles son las causas tasadas (como el maltrato físico o psicológico acreditado) y cómo se redacta.",
        "p2": "Genera una lámina infográfica sobria y equilibrada con una balanza y un libro de leyes abierto que destaque con iconos de advertencia las causas tasadas por ley en perfecto español.",
        "reto": "Pregunta a Gemini: '¿Qué jurisprudencia reciente del Tribunal Supremo admite el desapego y maltrato psicológico continuado?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "El Cuaderno Particional: El reparto formal ante notario",
        "concept": "El documento que detalla el inventario de bienes, deudas y la adjudicación exacta a cada uno de los herederos.",
        "p1": "Actúa como un jurista didáctico. Explícame paso a paso qué es un cuaderno particional, qué partes lo componen (inventario, avalúo, liquidación y adjudicación) y cómo se formaliza en escritura pública.",
        "p2": "Genera una infografía paso a paso con 4 fichas ordenadas horizontalmente con flechas dinámicas: '1. Inventario', '2. Valoración', '3. Liquidación', '4. Adjudicación'. Textos legibles en español.",
        "reto": "Pídele a Gemini: '¿Qué sucede si uno de los coherederos se niega a firmar el cuaderno particional?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "La Legítima de los Nietos y el Derecho de Representación",
        "concept": "Cómo heredan los nietos cuando un progenitor ha fallecido antes que el abuelo o abuela.",
        "p1": "Actúa como un abogado de familia. Explícame qué es el derecho de representación en el Código Civil español y cómo se reparte la herencia de los abuelos entre los nietos si uno de sus hijos ha fallecido previamente.",
        "p2": "Genera un árbol genealógico infográfico ilustrado con iconos elegantes que muestre con líneas de colores el reparto 'por estirpes' hacia los nietos en español.",
        "reto": "Pregúntale a Gemini: '¿Los nietos tienen legítima directa si todos los hijos del causante siguen con vida?'."
    },
    {
        "cat": "Notaría y Herencias",
        "title": "El Registro General de Actos de Última Voluntad",
        "concept": "El certificado oficial que revela cuál fue el último testamento otorgado y en qué notaría se firmó.",
        "p1": "Actúa como un funcionario del Ministerio de Justicia. Explícame qué es el Certificado de Últimas Voluntades, cómo demuestra cuál es el testamento válido y final, y cómo pedirlo con el certificado de defunción.",
        "p2": "Genera una infografía oficial y pulcra que ilustre el flujo de solicitud del certificado con tiempos, sedes electrónicas y documentos requeridos en español.",
        "reto": "Pídele a Gemini: '¿Cuántos días deben pasar desde el fallecimiento para poder solicitar las Últimas Voluntades?'."
    },

    # --- TEMÁTICA B: BANCA CLARA Y PROTECCIÓN DEL PATRIMONIO (15 temas) ---
    {
        "cat": "Banca Clara y Protección",
        "title": "El Fondo de Garantía de Depósitos (FGD): El límite de 100.000 €",
        "concept": "Conocer la protección legal pública del dinero en los bancos y cómo organizar los ahorros entre entidades.",
        "p1": "Actúa como un analista financiero prudente. Explícame con máxima claridad qué es el Fondo de Garantía de Depósitos en España y la Unión Europea, por qué garantiza hasta 100.000 euros por titular y banco, y cómo diversificar ahorros familiares.",
        "p2": "Genera una infografía ilustrada con la fachada de un banco sólido con un escudo dorado central que lleve el rótulo 'Garantizado 100.000 € por Titular', con notas explicativas en español.",
        "reto": "Pregúntale a Gemini: 'Si una cuenta corriente tiene 180.000 euros y dos cotitulares (marido y mujer), ¿está cubierto el 100% por el FGD?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "Titular vs. Autorizado en Cuentas Bancarias: Efectos tras el fallecimiento",
        "concept": "La enorme diferencia legal entre figurar como cotitular o como simple autorizado cuando fallece el dueño de la cuenta.",
        "p1": "Actúa como un director de sucursal transparente. Explícame la trampa común de poner a un hijo como autorizado pensando que podrá disponer del dinero tras el fallecimiento del titular, y por qué la autorización se extingue al instante.",
        "p2": "Genera una tabla comparativa gráfica muy limpia de dos columnas: 'Cotitular (Dueño del 50%, no se extingue)' frente a 'Autorizado (Representante en vida, cesa en el acto)'. Iconos claros y textos en español.",
        "reto": "Pídele a Gemini: '¿Qué justificantes exige el banco a los herederos para desbloquear el dinero de una cuenta?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "Renta Fija vs. Renta Variable: Entender el riesgo sin miedo",
        "concept": "Desmitificar los términos financieros y entender que prestar dinero a un Estado no es apostar en la bolsa.",
        "p1": "Actúa como un educador financiero senior. Explícame con metáforas sencillas la diferencia entre prestar dinero (Renta Fija / Letras del Tesoro) y comprar un pedazo de una empresa (Renta Variable / Bolsa), explicando el concepto de volatilidad.",
        "p2": "Genera una infografía visual que enfrente dos conceptos: a la izquierda, un camino llano y pavimentado con una meta fija ('Renta Fija: Interés pactado'); a la derecha, una montaña rusa ('Renta Variable: Subidas y bajadas'). Rótulos en español.",
        "reto": "Pregúntale a Gemini: '¿Qué es una Letra del Tesoro a 12 meses y cómo se compra directamente sin intermediarios bancarios?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "La Ley de Atención Presencial Bancaria a Mayores de 65 Años",
        "concept": "Conocer los derechos legales que obligan a las entidades a prestar servicio en ventanilla sin costes añadidos.",
        "p1": "Actúa como un defensor de los derechos del consumidor senior. Explícame el protocolo de atención presencial que la banca acordó en España para mayores de 65 años: horarios de ventanilla ampliados, atención telefónica preferente y trato humano sin obligar al cajero.",
        "p2": "Genera una infografía reivindicativa y positiva: una ventanilla bancaria acogedora con un empleado atendiendo amablemente a una persona mayor, con una lista de 4 derechos garantizados con casillas de verificación en español.",
        "reto": "Pídele a Gemini: '¿Cómo puedo reclamar formalmente ante el Servicio de Atención al Cliente de mi banco si no me quieren atender en ventanilla?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "Comisiones Bancarias Abusivas: Cómo identificarlas y reclamarlas",
        "concept": "Reconocer comisiones de mantenimiento, custodia o transferencias que se pueden eliminar o reducir.",
        "p1": "Actúa como un experto en banca ética. Explícame cuáles son las principales comisiones que cobran los bancos en las cuentas de pensionistas, en qué casos son ilegales (como cobrar por ingresar en cuenta ajena) y qué modelo de carta presentar para anularlas.",
        "p2": "Genera una ilustración infográfica con una lupa sobre un extracto bancario destacando en rojo las comisiones típicas y al lado un botón verde con el texto 'Carta de Reclamación Gratuita' y 3 consejos prácticos en español.",
        "reto": "Pídele a Gemini: 'Redáctame un párrafo modelo para pedir a mi banco que me devuelva una comisión de mantenimiento de 60 euros'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "La Inflación Explicada con el Carrito de la Compra",
        "concept": "Comprender la pérdida de poder adquisitivo del dinero parado en cuenta y la diferencia entre valor nominal y real.",
        "p1": "Actúa como un catedrático de economía didáctica. Explícame qué es la inflación utilizando el ejemplo de la cesta de la compra de 1990 frente a la de hoy con un billete de 50 euros, y por qué dejar todos los ahorros quietos en cuenta corriente hace que pierdan valor lentamente.",
        "p2": "Genera una ilustración comparativa de dos carritos de supermercado: uno en el año 2000 repleto de productos con una etiqueta de 50€, y otro actual con menos productos por los mismos 50€, con un gráfico de barras suave y rótulos en español.",
        "reto": "Pregúntale a Gemini: '¿Cómo se calcula si la subida anual de mi pensión ha cubierto o no la inflación del IPC?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "La Cuenta de Pago Básica: El derecho legal a una cuenta por 3 € al mes",
        "concept": "La normativa europea que garantiza a cualquier ciudadano una cuenta sin comisiones abusivas para su pensión.",
        "p1": "Actúa como un asesor jurídico social. Explícame qué es por ley la 'Cuenta de Pago Básica', quién tiene derecho a solicitarla en cualquier banco, por qué no pueden denegártela y su coste máximo legal regulado por el Banco de España.",
        "p2": "Genera una infografía institucional con el logo representativo de la justicia bancaria y un listado de los servicios incluidos por ley: nómina/pensión, tarjeta de débito y transferencias, con tipografía clara en español.",
        "reto": "Pídele a Gemini: '¿En qué casos la Cuenta de Pago Básica es totalmente gratuita para personas en situación de vulnerabilidad?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "Seguros Vinculados a Cuentas y Tarjetas: Lo que pagas sin saberlo",
        "concept": "Auditar los pequeños cobros recurrentes de seguros de accidentes o vida que a menudo se contratan por despiste.",
        "p1": "Actúa como un auditor financiero familiar. Enséñame a revisar los extractos bancarios de los últimos 6 meses para detectar seguros accesorios o coberturas duplicadas que el banco cobra de forma silenciosa y cómo cancelarlos formalmente.",
        "p2": "Genera una infografía visual que muestre un 'Escáner de Gastos Hormiga Bancarios' con iconos de tijeras recortando recibos de seguros innecesarios, con un paso a paso de cancelación en español.",
        "reto": "Pregunta a Gemini: '¿Con cuántos días de preaviso antes del vencimiento anual debo avisar a la aseguradora para no renovar?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "Las Cuentas Indivisas y los Conflictos de Bloqueo Bancario",
        "concept": "Cómo evitar que el banco congele temporalmente los saldos familiares durante una disputa de herencia.",
        "p1": "Actúa como un abogado especialista en derecho bancario. Explícame en qué supuestos el banco puede bloquear el saldo de una cuenta corriente tras el fallecimiento de uno de los titulares y qué pagos esenciales (luz, comunidad, funeral) está obligado a seguir atendiendo.",
        "p2": "Genera un esquema infográfico con un semáforo legal: en verde 'Pagos que el banco SÍ debe pagar aunque esté bloqueada (entierro, IBI)', en rojo 'Operaciones suspendidas'. Textos muy legibles en español.",
        "reto": "Pídele a Gemini: '¿Qué documento del notario o de Hacienda es necesario presentar para que el banco levante el bloqueo?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "El Defensor del Cliente y el Reclamo ante el Banco de España",
        "concept": "El cauce oficial y gratuito de dos pasos para resolver conflictos bancarios sin acudir a los tribunales.",
        "p1": "Actúa como un mediador de consumo. Explícame la vía de reclamación oficial en dos fases: primero ante el Servicio de Atención al Cliente (SAC) del propio banco y, si no responden en un mes o deniegan, ante el Banco de España de forma gratuita.",
        "p2": "Genera una infografía en forma de escalera de 2 peldaños: 'Peldaño 1: SAC de tu banco (plazo 1 mes)' -> 'Peldaño 2: Departamento de Conducta del Banco de España'. Rótulos en español.",
        "reto": "Pregúntale a Gemini: '¿Los informes del Banco de España son de obligado cumplimiento para la entidad bancaria?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "El Depósito a Plazo Fijo: Cómo negociar intereses y penalizaciones",
        "concept": "Comprender cómo funcionan las imposiciones a plazo fijo tradicionales y qué ocurre si necesitas retirar el dinero antes.",
        "p1": "Actúa como un asesor financiero clásico. Explícame de forma didáctica qué es un depósito bancario a plazo fijo (IPF), cómo se devengan los intereses, qué retención de IRPF se aplica y qué dice la ley sobre penalizaciones por rescate anticipado.",
        "p2": "Genera un gráfico infográfico con una línea de tiempo horizontal clara: 'Día 1: Depósito del capital' -> 'Transcurso del año: Seguridad del 100%' -> 'Vencimiento: Recuperación del dinero + Intereses'. Español.",
        "reto": "Pídele a Gemini: '¿Puede la penalización por cancelación anticipada hacerme perder parte del capital invertido inicialmente?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "Las Tarjetas Revolving: La trampa de las cuotas pequeñas e intereses infinitos",
        "concept": "Identificar las tarjetas de crédito que aplican intereses desproporcionados y nunca terminan de pagarse.",
        "p1": "Actúa como un experto en derecho de consumidores. Explícame qué es una tarjeta de crédito 'revolving', cómo funciona la trampa psicológica de pagar una cuota fija mensual muy baja (ej. 30 €) mientras la deuda crece por intereses del 20% TAE, y cómo reclamar.",
        "p2": "Genera una infografía con una espiral o remolino financiero que ilustre visualmente la diferencia abismal entre 'Tarjeta de Débito/Crédito normal a fin de mes' frente a 'Tarjeta Revolving con intereses encadenados'. Español.",
        "reto": "Pregúntale a Gemini: '¿Qué ha dicho el Tribunal Supremo sobre las tarjetas revolving con intereses superiores al 20%?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "El Secreto Bancario y la Transparencia con los Hijos",
        "concept": "Cómo equilibrar la privacidad financiera personal con la conveniencia de dejar instrucciones a personas de confianza.",
        "p1": "Actúa como un consejero de familia y patrimonio. Explícame cómo gestionar el secreto de nuestras cuentas frente a la familia, qué datos es conveniente compartir con los hijos por tranquilidad práctica y qué cosas pertenecen a nuestra intimidad económica.",
        "p2": "Genera una ilustración serena de un archivador doméstico ordenado con una llave dorada al lado, con una lista visual titulada 'La Carpeta de la Tranquilidad Familiar' con 4 puntos en español.",
        "reto": "Pídele a Gemini: 'Escribe un modelo de índice para organizar los papeles importantes de casa en una carpeta única'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "La CIRBE del Banco de España: Saber qué deudas figuran a tu nombre",
        "concept": "Conocer la base de datos pública del Banco de España que registra todos los préstamos y avales de un ciudadano.",
        "p1": "Actúa como un analista del Banco de España. Explícame qué es la CIRBE (Central de Información de Riesgos), por qué es bueno pedir nuestro informe gratuito cada cierto tiempo para verificar que nadie ha suplantado nuestra identidad pidiendo créditos, y cómo se solicita.",
        "p2": "Genera una infografía con el escudo oficial del Banco de España y un informe con sello verde de 'Cero deudas registradas', con los 3 pasos para pedir el informe con certificado digital o por correo en español.",
        "reto": "Pregúntale a Gemini: '¿Figuran en la CIRBE las deudas que tengo como avalista de un préstamo de mi hijo?'."
    },
    {
        "cat": "Banca Clara y Protección",
        "title": "El Peligro de Avalar Préstamos Ajenos: Responsabilidad solidaria",
        "concept": "Entender que firmar como avalista significa responder con la propia casa y pensión si el deudor principal no paga.",
        "p1": "Actúa como un notario prudente. Explícame con toda la delicadeza pero con máxima firmeza qué implica legalmente firmar como avalista de una hipoteca o préstamo de un hijo o familiar, qué es la renuncia a los beneficios de orden y excusión, y cómo protegerse.",
        "p2": "Genera una lámina infográfica de advertencia responsable: una balanza donde se compara 'Amor familiar' con 'Riesgo del patrimonio propio', con 4 preguntas vitales que hacerse antes de firmar un aval en español.",
        "reto": "Pídele a Gemini: '¿Se hereda la condición de avalista si fallece el padre que avaló al hijo?'."
    },

    # --- TEMÁTICA C: VIVIENDA, LIQUIDEZ Y PATRIMONIO INMOBILIARIO (15 temas) ---
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "La Hipoteca Inversa: Qué es de verdad, ventajas y precauciones",
        "concept": "Desgranar el producto financiero que permite obtener liquidez mensual manteniendo la propiedad de la casa de por vida.",
        "p1": "Actúa como un economista independiente experto en jubilación. Explícame con total imparcialidad qué es una hipoteca inversa para mayores de 65 años, cómo se cobra la renta, qué sucede con la deuda al fallecer y qué papel juegan los herederos.",
        "p2": "Genera una infografía didáctica sobre la silueta de una vivienda acogedora con flechas que muestren: 'Sigues viviendo en tu casa' + 'Cobras una mensualidad' -> 'Tus herederos deciden si pagar la deuda o vender'. Textos en español.",
        "reto": "Pregúntale a Gemini: '¿Tributan en el IRPF las cantidades mensuales recibidas por una hipoteca inversa?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "La Venta de la Nuda Propiedad con Usufructo Vitalicio",
        "concept": "Vender la titularidad del inmueble recibiendo un pago único pero reservándose el derecho a vivir en él hasta el último día.",
        "p1": "Actúa como un asesor inmobiliario ético. Explícame la fórmula de vender la 'nuda propiedad' de una vivienda reservándose el usufructo vitalicio: cómo se calcula el precio según la edad del propietario y qué garantías notariales blindan que nadie pueda echarte.",
        "p2": "Genera una ilustración infográfica elegante con dos llaves: una llave dorada que simboliza 'Tu derecho a vivir en ella de por vida' y un cheque que representa 'El capital recibido', con un cuadro explicativo en español.",
        "reto": "Pídele a Gemini: '¿Quién paga los gastos de comunidad y el IBI cuando se vende la nuda propiedad y se mantiene el usufructo?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "La Renta Vitalicia Inmobiliaria: Tu casa como complemento de pensión",
        "concept": "Transformar el valor del inmueble en una mensualidad periódica garantizada hasta el final de los días.",
        "p1": "Actúa como un consultor actuarial divulgador. Explícame qué es una renta vitalicia inmobiliaria, en qué se diferencia de la venta directa y qué cláusulas notariales garantizan que el cobro no se interrumpa nunca.",
        "p2": "Genera un gráfico ilustrado de flujo mensual: un calendario con pagos automáticos asegurados mes a mes conviviendo con el disfrute de la vivienda habitual, rotulado con tipografía clara en español.",
        "reto": "Pregúntale a Gemini: '¿Qué ventajas fiscales en el IRPF tienen las rentas vitalicias constituidas por mayores de 70 años?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "La Exención de IRPF al Vender la Vivienda Habitual (+65 años)",
        "concept": "El gran beneficio fiscal que exime de tributar por la ganancia patrimonial al vender la casa habitual pasados los 65 años.",
        "p1": "Actúa como un técnico de Hacienda didáctico. Explícame el beneficio fiscal que tienen las personas mayores de 65 años al vender su vivienda habitual: la exención total del IRPF por la plusvalía obtenida, sin obligación de reinvertir el dinero.",
        "p2": "Genera una infografía tributaria clara con un sello verde oficial de 'Exento 100% de IRPF para mayores de 65 años en vivienda habitual' y los 3 requisitos legales para que la casa sea considerada legalmente habitual. Español.",
        "reto": "Pídele a Gemini: '¿Qué ocurre si la casa que vendo pasados los 65 años era una segunda residencia en la playa o pueblo?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "Vender una Segunda Vivienda y Reinyectar en Renta Vitalicia",
        "concept": "Cómo evitar pagar impuestos por la venta de un piso no habitual destinando el dinero a una renta vitalicia.",
        "p1": "Actúa como un planificador financiero senior. Explícame la norma fiscal que permite a los mayores de 65 años no pagar IRPF al vender cualquier bien (segunda vivienda, acciones o terrenos) si destinan hasta 240.000 euros a contratar una renta vitalicia en 6 meses.",
        "p2": "Genera un esquema con un puente gráfico que conecte la venta de una finca/piso con un fondo de renta vitalicia bajo el título 'Puente Fiscal: Límite 240.000 € y 6 meses', con textos en español.",
        "reto": "Pregúntale a Gemini: '¿Qué requisitos debe tener la entidad aseguradora para que Hacienda acepte la renta vitalicia exenta?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "Derramas Comunitarias e Instalación de Ascensores a Cota Cero",
        "concept": "La Ley de Propiedad Horizontal y la obligación de la comunidad de hacer accesible el edificio para mayores de 70 años.",
        "p1": "Actúa como un administrador de fincas experto. Explícame el artículo 10 de la Ley de Propiedad Horizontal: por qué las obras de accesibilidad (rampas, ascensor cota cero) son obligatorias si las solicita un vecino mayor de 70 años o con discapacidad y cómo se pagan.",
        "p2": "Genera una infografía arquitectónica limpia de un portal moderno con ascensor a cota cero y rampa suave, con un cuadro sinóptico que resuma el límite de las 12 mensualidades ordinarias de gasto anual en español.",
        "reto": "Pídele a Gemini: '¿Qué ayudas y subvenciones autonómicas existen para comunidades de propietarios que instalen ascensor?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "El Alquiler Seguro de un Piso Propio: Avales y seguros de impago",
        "concept": "Cómo alquilar un inmueble heredado o secundario con total tranquilidad jurídica y sin sobresaltos.",
        "p1": "Actúa como un gestor de arrendamientos. Explícame las medidas indispensables para alquilar una vivienda con seguridad: el seguro de protección de pagos, la selección de inquilino con nómina solvente y el depósito de la fianza en el organismo autonómico oficial.",
        "p2": "Genera una infografía con un 'Decálogo del Alquiler Seguro' con iconos de cerradura, póliza y contrato oficial visado, con explicaciones claras en español.",
        "reto": "Pregúntale a Gemini: '¿Por qué es obligatorio depositar la fianza legal del alquiler en la entidad de la Comunidad Autónoma?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "El Contrato de Alquiler de Renta Antigua: Derechos y subrogaciones",
        "concept": "Conocer la protección de los contratos anteriores a 1985 (Ley Boyer) y cómo funcionan los derechos del inquilino histórico.",
        "p1": "Actúa como un abogado especialista en arrendamientos históricos. Explícame qué es un contrato de renta antigua, qué protecciones vitalicias otorga al titular y qué límites existen para que el cónyuge o hijos puedan subrogarse en caso de fallecimiento.",
        "p2": "Genera una ilustración con un contrato clásico mecanografiado con sello histórico, acompañada de una guía en 3 puntos que resuma los derechos irrenunciables del arrendatario en español.",
        "reto": "Pídele a Gemini: '¿En qué casos el propietario de un piso de renta antigua puede reclamar la vivienda para uso propio?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "El Cohousing Senior y las Cooperativas de Vivienda Colaborativa",
        "concept": "La alternativa moderna a las residencias tradicionales: envejecer en comunidad propia con servicios compartidos.",
        "p1": "Actúa como un sociólogo y arquitecto de vivienda colaborativa. Explícame qué es el modelo de 'Cohousing Senior' (viviendas colaborativas en régimen de cesión de uso), cómo se financia, qué autonomía ofrece frente a una residencia y cómo protege el patrimonio de los socios.",
        "p2": "Genera una perspectiva arquitectónica alegre y luminosa de un complejo de cohousing con apartamentos privados y jardines comunes donde conviven mayores activos, con rótulos en español que detallen las ventajas.",
        "reto": "Pregunta a Gemini: '¿Qué ocurre con la aportación económica si un cooperativista decide marcharse o fallece?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "La Extinción de Condominio entre Hermanos: Reparto de un piso heredado",
        "concept": "Cómo liquidar la copropiedad de una vivienda cuando uno de los herederos quiere quedarse con ella compensando a los demás.",
        "p1": "Actúa como un notario conciliador. Explícame qué es la extinción de condominio, por qué tributa infinitamente menos que una compraventa tradicional (solo Actos Jurídicos Documentados) y cómo facilita que un hermano compre su parte al resto.",
        "p2": "Genera un gráfico infográfico con una vivienda que se divide simbólicamente en dos mitades y una flecha de compensación económica, bajo el título 'Extinción de Condominio: Ventaja Fiscal vs Compraventa', en español.",
        "reto": "Pídele a Gemini: '¿Qué porcentaje aproximado de impuestos se ahorra haciendo extinción de condominio frente a comprar la mitad del piso?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "El Seguro de Hogar: Coberturas esenciales y qué no te cubre",
        "concept": "Auditar la póliza de la vivienda familiar para no pagar por duplicado y saber reclamar daños por agua o roturas.",
        "p1": "Actúa como un perito de seguros independiente. Explícame la diferencia entre Continente (las paredes y tuberías) y Contenido (muebles y enseres), qué coberturas son indispensables en la madurez y cómo evitar el infraseguro al renovar la póliza.",
        "p2": "Genera una sección transversal esquemática de una vivienda donde el 'Continente' aparezca marcado en azul y el 'Contenido' en naranja, con un listado de los 4 siniestros más frecuentes y cómo declararlos en español.",
        "reto": "Pregúntale a Gemini: 'Si hay una gotera en el techo que viene del vecino de arriba, ¿a qué seguro debo llamar primero?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "La Descalificación de una Vivienda de Protección Oficial (VPO)",
        "concept": "Comprobar si un piso protegido antiguo ha cumplido los años de calificación y se puede vender a precio libre.",
        "p1": "Actúa como un experto en vivienda pública. Explícame cómo saber si una vivienda que compramos hace décadas bajo régimen de VPO ya es libre, qué plazo suele exigir la ley (ej. 30 años) y qué certificado de descalificación o precio máximo legal hay que pedir a la Consejería.",
        "p2": "Genera una infografía con un sello que pase de 'Vivienda Protegida' a 'Régimen Libre', con un cronograma explicativo de plazos y trámites autonómicos en español.",
        "reto": "Pídele a Gemini: '¿Qué ocurre si vendo una vivienda que todavía tiene la calificación de VPO por encima del precio oficial?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "La Segregación o División de un Piso Grande en Dos Pequeños",
        "concept": "Convertir una vivienda familiar amplia en dos unidades independientes para alquilar o adaptar.",
        "p1": "Actúa como un arquitecto urbanista. Explícame los requisitos legales para dividir un piso grande en dos: autorización de los estatutos de la comunidad de vecinos, licencia municipal de obras, cédulas de habitabilidad y escrituras notariales independientes.",
        "p2": "Genera un plano en planta ilustrado y moderno de un piso de 140 m² dividido limpiamente en dos apartamentos de 70 m², con iconos de las licencias requeridas rotuladas en español.",
        "reto": "Pregunta a Gemini: '¿Qué mayoría de la junta de propietarios exige la Ley de Propiedad Horizontal para autorizar la división de un piso?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "El Certificado de Eficiencia Energética: Obligaciones al vender o alquilar",
        "concept": "Conocer la etiqueta energética obligatoria por ley en cualquier transmisión o arrendamiento de vivienda.",
        "p1": "Actúa como un certificador energético y pedagogo. Explícame qué es el Certificado de Eficiencia Energética, por qué es obligatorio tenerlo para publicar un anuncio de venta o alquiler, qué miden las letras de la A a la G y qué validez temporal tiene.",
        "p2": "Genera una infografía con la famosa escala de colores de la A (verde oscuro de máxima eficiencia) a la G (rojo), acompañada de 4 consejos de aislamiento doméstico para subir de letra, en español.",
        "reto": "Pídele a Gemini: '¿Qué multas existen por vender o alquilar una vivienda sin disponer del certificado energético registrado?'."
    },
    {
        "cat": "Vivienda y Liquidez Senior",
        "title": "La Donación del Dinero de la Venta de una Casa a los Hijos",
        "concept": "Cómo transferir el fruto de una venta inmobiliaria a los descendientes cumpliendo la normativa fiscal.",
        "p1": "Actúa como un asesor tributario. Explícame cómo donar a los hijos el dinero obtenido de una venta inmobiliaria, por qué debe formalizarse en escritura pública notarial para beneficiarse de las bonificaciones fiscales y qué plazos marca la ley.",
        "p2": "Genera un diagrama infográfico con los pasos del banco a la notaría y de la notaría a la liquidación del impuesto autonómico modelo 651 en español con diseño elegante.",
        "reto": "Pregúntale a Gemini: '¿Por qué nunca se debe transferir una cantidad grande de dinero a un hijo mediante simple transferencia sin pasar por notario?'."
    },

    # --- TEMÁTICA D: PENSIONES, IMPUESTOS PRÁCTICOS Y CONSUMO INTELIGENTE (15 temas) ---
    {
        "cat": "Pensiones y Consumo",
        "title": "Cómo Leer la Nómina de la Pensión: Bruto, neto y retención de IRPF",
        "concept": "Descifrar el justificante mensual de la pensión de la Seguridad Social y entender las retenciones fiscales.",
        "p1": "Actúa como un graduado social divulgador. Enséñame a leer punto por punto el justificante de la pensión pública: la cuantía bruta, el porcentaje de retención del IRPF que aplica la Seguridad Social y el líquido neto que entra en la cuenta bancaria.",
        "p2": "Genera una ilustración infográfica simulando una nómina de pensión en formato legible con flechas explicativas en azul y verde que señalen: 'Pensión Bruta' -> 'Retención IRPF' -> 'Ingreso Neto en Cuenta'. Todo en perfecto español.",
        "reto": "Pídele a Gemini: '¿Cómo puedo solicitar a la Seguridad Social que me suba voluntariamente la retención del IRPF para no pagar de golpe en la Renta?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "La Factura de la Luz: Mercado Regulado (PVPC) vs. Mercado Libre",
        "concept": "Comprender la diferencia crucial entre las tarifas oficiales del Gobierno y las ofertas comerciales de las eléctricas.",
        "p1": "Actúa como un analista del mercado energético independiente. Explícame de forma sencillísima qué es el PVPC (Precio Voluntario para el Pequeño Consumidor) frente al mercado libre con precio fijo, y cómo mirar en la factura qué contrato tengo actualmente.",
        "p2": "Genera una infografía comparativa con dos columnas muy claras: a la izquierda 'Mercado Regulado PVPC (fijado por el Estado)' y a la derecha 'Mercado Libre (precio pactado con la compañía)', con los iconos de la CNMC en español.",
        "reto": "Pregúntale a Gemini: '¿En qué apartado de la factura de la luz viene indicado si estoy en mercado regulado o libre?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "El Bono Social Eléctrico y Térmico para Pensionistas",
        "concept": "El descuento directo de hasta el 40% o 65% en la factura de la luz y la ayuda anual de calefacción para jubilados.",
        "p1": "Actúa como un trabajador social experto en energía. Explícame los requisitos para solicitar el Bono Social Eléctrico como pensionista con ingresos mínimos o familia, qué descuento aplica en la factura y cómo genera automáticamente el Bono Social Térmico anual.",
        "p2": "Genera una infografía con un termómetro y una bombilla luminosa que representen los dos bonos, con un cuadro sinóptico de requisitos de renta y los 3 pasos para tramitarlo con la comercializadora de referencia en español.",
        "reto": "Pídele a Gemini: '¿Es obligatorio estar en tarifa PVPC para poder solicitar el Bono Social Eléctrico?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "La Declaración de la Renta en Jubilados: Cuándo es obligatorio presentarla",
        "concept": "Conocer los límites de ingresos (22.000 € con un pagador o 15.000 € con dos pagadores) que obligan a declarar.",
        "p1": "Actúa como un técnico de la Agencia Tributaria amable y pedagogo. Explícame cuándo está obligado un pensionista a presentar la Declaración del IRPF: los límites con un solo pagador frente al cobro de dos pensiones (ej. Seguridad Social + plan de pensiones privado).",
        "p2": "Genera una infografía tipo árbol de decisión con preguntas '¿Cobras de un solo pagador?' -> 'Límite 22.000 €', '¿Tienes dos pagadores?' -> 'Límite 15.000 €', con colores suaves y textos claros en español.",
        "reto": "Pregúntale a Gemini: '¿Si no llego al límite mínimo me conviene presentar la declaración igualmente si me sale a devolver?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "Rescatar un Plan de Pensiones: En forma de renta o en capital",
        "concept": "La trascendencia fiscal de no retirar todo el plan de pensiones de golpe para no disparar el tipo marginal de IRPF.",
        "p1": "Actúa como un asesor fiscal senior. Explícame por qué rescatar un plan de pensiones de golpe en forma de capital puede hacer que Hacienda se quede con casi la mitad por salto de tramo de IRPF, y por qué rescatarlo en forma de renta mensual es mucho más ventajoso.",
        "p2": "Genera una infografía comparativa con dos gráficos de barras: uno que muestre el impacto fiscal de rescatar 60.000 € de golpe (gran bocado fiscal rojo) frente a cobrar 500 € al mes de forma progresiva (impacto suave verde). Español.",
        "reto": "Pídele a Gemini: '¿Qué reducción del 40% existe en el IRPF para las aportaciones al plan de pensiones anteriores al año 2007?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "El Complemento para la Reducción de la Brecha de Género",
        "concept": "La ayuda económica mensual añadida a la pensión para personas que tuvieron hijos y vieron afectada su carrera laboral.",
        "p1": "Actúa como un experto en Seguridad Social. Explícame qué es el complemento de pensiones para la reducción de la brecha de género (antiguo complemento de maternidad), cuánto dinero mensual suma por cada hijo y quién puede solicitarlo si no se lo incluyeron de oficio.",
        "p2": "Genera una infografía ilustrada con iconos familiares de padres, madres e hijos con un símbolo de suma dorada junto a la nómina de la pensión, detallando los requisitos y cuantías por hijo en español.",
        "reto": "Pregúntale a Gemini: '¿Pueden los hombres solicitar este complemento de pensión si demuestran lagunas de cotización por cuidado de hijos?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "La Pensión de Viudedad: Porcentajes y compatibilidad con el trabajo",
        "concept": "Comprender cómo se calcula la base reguladora (52%, 60% o 70%) y su compatibilidad con la propia pensión de jubilación.",
        "p1": "Actúa como un asesor de la Seguridad Social. Explícame cómo se calcula la pensión de viudedad en España, en qué casos se cobra el 60% o el 70% de la base del cónyuge fallecido y cómo se compatibiliza con la propia pensión de jubilación hasta el tope máximo de pensiones.",
        "p2": "Genera una infografía visual que muestre la suma de dos ingresos: 'Mi Pensión de Jubilación' + 'Pensión de Viudedad' con un indicador del límite máximo legal de pensión pública en España en español.",
        "reto": "Pídele a Gemini: '¿Se pierde la pensión de viudedad si la persona viuda contrae un nuevo matrimonio civil?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "La Ley de Dependencia: Grados, prestaciones y copago residencial",
        "concept": "El sistema público para solicitar ayuda a domicilio, centro de día o prestación económica para cuidados en el entorno familiar.",
        "p1": "Actúa como un coordinador de servicios sociales. Explícame qué es el Sistema para la Autonomía y Atención a la Dependencia (SAAD), los 3 grados de dependencia (moderada, severa y gran dependencia) y qué ayudas concretas se pueden solicitar en los servicios sociales municipales.",
        "p2": "Genera una infografía en forma de pirámide con 3 niveles: 'Grado I (Moderada)', 'Grado II (Severa)' y 'Grado III (Gran Dependencia)', detallando las horas de ayuda a domicilio y servicios en cada caso en español.",
        "reto": "Pregúntale a Gemini: '¿Cómo influye el patrimonio del dependiente en el cálculo del copago de una plaza de residencia concertada?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "El Certificado Digital de la FNMT y Cl@ve Permanente: Tu firma pública",
        "concept": "La llave digital segura para consultar tus cotizaciones, citas médicas y certificados oficiales desde casa sin colas.",
        "p1": "Actúa como un formador en competencias digitales públicas. Explícame con paciencia infinita qué es el Certificado Digital de la Fábrica Nacional de Moneda y Timbre y el sistema Cl@ve Permanente, para qué sirven y cómo tramitarlos con una única visita de acreditación.",
        "p2": "Genera una infografía didáctica con la imagen de una llave maestra dorada que abre tres puertas oficiales: 'Seguridad Social (Tu Pensión)', 'Hacienda (Tu Renta)' y 'Salud (Tus Recetas y Citas)', rotulada con claridad en español.",
        "reto": "Pídele a Gemini: '¿Cómo puedo instalar el Certificado Digital en el navegador de mi ordenador paso a paso?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "El Documento de Voluntades Anticipadas o Testamento Vital",
        "concept": "Expresar legalmente los deseos sobre tratamientos médicos y cuidados paliativos ante una situación terminal irreversible.",
        "p1": "Actúa como un médico especialista en bioética y jurista. Explícame con serenidad y respeto qué es el Testamento Vital (Instrucciones Previas), por qué alivia a la familia de tomar decisiones desgarradoras y cómo se inscribe en el Registro oficial de Sanidad.",
        "p2": "Genera una ilustración tranquila de un documento médico oficial con un símbolo de corazón protector, con los 4 puntos clave que se suelen plasmar (sedación paliativa, no ensañamiento terapéutico y donación) en español.",
        "reto": "Pregúntale a Gemini: '¿Quién puede actuar como mi representante legal en el documento de voluntades anticipadas?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "La Carpeta Familiar de Emergencia: Todo organizado para tus seres queridos",
        "concept": "Cómo recopilar en una sola carpeta física ordenada toda la información esencial de la vida de un adulto.",
        "p1": "Actúa como un organizador patrimonial familiar. Enséñame a crear 'La Carpeta Maestra de Casa': qué 7 documentos indispensables deben estar juntos (escrituras, testamento, pólizas de seguros, certificado de matrimonio, cuentas bancarias, claves de acceso y voluntades).",
        "p2": "Genera una ilustración infográfica de una carpeta ejecutiva abierta con separadores de colores claramente etiquetados: '1. Inmuebles', '2. Notaría', '3. Bancos', '4. Seguros', '5. Sanidad'. Estilo pulcro en español.",
        "reto": "Pídele a Gemini: 'Redáctame una lista de comprobación de 10 puntos para imprimir y pegar en la portada de mi carpeta de casa'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "Desahucios de Vivienda Arrendada a Mayores Vulnerables",
        "concept": "Las protecciones legales extraordinarias que paralizan desalojos en personas mayores de 65 años en situación vulnerable.",
        "p1": "Actúa como un abogado de derechos humanos y vivienda. Explícame qué medidas de protección social existen en España para inquilinos mayores de 65 años que afrontan el fin de un contrato de alquiler o una subida desproporcionada, y cómo intervienen los servicios sociales.",
        "p2": "Genera una infografía con un escudo de protección social que destaque los criterios de vulnerabilidad económica y las vías de mediación municipal antes de cualquier desalojo en español.",
        "reto": "Pregúntale a Gemini: '¿Qué es el informe de vulnerabilidad social que emiten los ayuntamientos ante un juzgado?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "Derecho de Desistimiento en Compras por Teléfono o a Domicilio",
        "concept": "Los 14 días naturales para anular cualquier contrato o compra de enciclopedias, colchones o luz sin dar explicaciones.",
        "p1": "Actúa como un inspector de consumo. Explícame el derecho legal de desistimiento de 14 días para compras firmadas en el domicilio o acordadas por teléfono (compañías telefónicas, gas, libros), por qué no requiere justificación alguna y cómo ejercerlo fehacientemente.",
        "p2": "Genera una infografía con un calendario que marque los 14 días con un tick verde y un modelo de carta de desistimiento con el texto 'Anulación sin penalización garantizada por ley' en español.",
        "reto": "Pídele a Gemini: 'Escribe un modelo de mensaje para enviar por burofax o correo certificado desistiendo de un contrato de gas firmado ayer'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "La Tarjeta Dorada de Renfe y Descuentos en Transportes Senior",
        "concept": "Aprovechar al máximo los descuentos oficiales en trenes, autobuses interurbanos y abonos de transporte metropolitano.",
        "p1": "Actúa como un guía de movilidad para mayores. Explícame cómo funciona la Tarjeta Dorada de Renfe para mayores de 60 años: precios, descuentos en AVE y Cercanías (hasta el 40%), cómo renovarla por internet o en taquilla y los abonos de transporte metropolitanos.",
        "p2": "Genera una infografía con una tarjeta dorada estilizada sobre la silueta de un tren de alta velocidad, con una tabla comparativa de descuentos según los días de la semana (lunes a jueves vs fin de semana) en español.",
        "reto": "Pregúntale a Gemini: '¿Se puede asociar la Tarjeta Dorada a los billetes comprados por internet desde la aplicación del móvil?'."
    },
    {
        "cat": "Pensiones y Consumo",
        "title": "El Pacto Intergeneracional: Ayudar a los hijos sin poner en riesgo tu vejez",
        "concept": "La regla de oro de la prudencia económica familiar: apoyar a la siguiente generación desde la solvencia y la serenidad.",
        "p1": "Actúa como un psicólogo y asesor financiero de familias. Explícame cómo establecer límites sanos y afectuosos al prestar o regalar dinero a los hijos adultos para bodas, hipotecas o negocios, recordando la regla de oro: 'Tu mejor legado es no ser una carga económica futura para ellos'.",
        "p2": "Genera una ilustración emotiva y sabia de tres generaciones familiares charlando sonrientes en un jardín, con un decálogo visual titulado 'Las 4 Reglas del Apoyo Familiar Sano' en español.",
        "reto": "Pídele a Gemini: '¿Cómo documentar un préstamo entre familiares a interés cero ante Hacienda para que no parezca una donación encubierta?'."
    }
]

# Distribución intercalada / rotatoria uniforme de los 60 temas:
# Tenemos 4 bloques de 15 temas (A: Notaría, B: Banca, C: Vivienda, D: Pensiones).
# Los intercalamos en orden A, B, C, D, A, B, C, D... para que en ninguna sesión se repita la misma temática consecutiva.
def get_pat_items():
    items = []
    bloques = [
        RAW_PAT_TOPICS[0:15],   # A
        RAW_PAT_TOPICS[15:30],  # B
        RAW_PAT_TOPICS[30:45],  # C
        RAW_PAT_TOPICS[45:60]   # D
    ]
    
    intercalados = []
    for i in range(15):
        for b in range(4):
            intercalados.append(bloques[b][i])
            
    for idx, raw in enumerate(intercalados, 1):
        id_code = f"[PAT-{idx:03d}]"
        prompt_tuple = (raw["p1"], raw["p2"])
        tips_text = (
            f"👉 <b>Reto Práctico de Aula:</b> {raw['reto']}<br/>"
            f"<i>Área de Conocimiento:</i> {raw['cat']} • Cultura y Derechos 101."
        )
        items.append({
            "block_dir": "14. [PAT] BLOQUE_14_CULTURA_PATRIMONIAL_Y_DERECHOS",
            "block_name": "BLOQUE 14: CULTURA PATRIMONIAL, DERECHOS Y FINANZAS CLARAS [PAT]",
            "id_code": id_code,
            "title": raw["title"],
            "concept": raw["concept"],
            "prompt": prompt_tuple,
            "tips": tips_text,
            "extra": raw["cat"]
        })
    return items

if __name__ == '__main__':
    items = get_pat_items()
    print(f"✅ Generados {len(items)} ítems para [PAT] (Cultura Patrimonial y Derechos 101)")
    for it in items[:4]:
        print(f" - {it['id_code']} {it['title']} ({it['extra']})")

