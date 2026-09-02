import os

script_path = '/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/build_repositorio_maestro.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Reemplazamos la función add_taller_item para soportar tuplas (Paso 1 y Paso 2)
idx_def = text.find('def add_taller_item(')
idx_def_end = text.find('add_header_2(', idx_def)

new_taller_def = """def add_taller_item(num_str, title, desc_taller, prompt_gemini):
    p_h = doc.add_heading(f'{num_str} {title}', level=3)
    for r in p_h.runs:
        r.font.size = Pt(12)
        r.font.color.rgb = RGBColor(0x1A, 0x0A, 0x2E)
    
    p_d = doc.add_paragraph()
    p_d.add_run('• Objetivo del Taller: ').bold = True
    p_d.add_run(desc_taller)
    
    if isinstance(prompt_gemini, tuple) and len(prompt_gemini) == 2:
        p1, p2 = prompt_gemini
        p_g1 = doc.add_paragraph()
        r_h1 = p_g1.add_run('• 🔴 Paso 1 (Prompt Previo para Generar la Foto Base en Gemini): ').bold = True
        r_h1.font.color.rgb = RGBColor(0xB2, 0x22, 0x22)
        r_t1 = p_g1.add_run(f'\"{p1}\"')
        r_t1.bold = True
        r_t1.font.color.rgb = RGBColor(0x8B, 0x00, 0x00)
        p_g1.add_run(f'  [{len(p1)} car.]').italic = True
        
        p_g2 = doc.add_paragraph()
        r_h2 = p_g2.add_run('• 🟢 Paso 2 (Orden en la misma conversación para la Magia / Transformación NIQUELADA): ').bold = True
        r_h2.font.color.rgb = RGBColor(0x00, 0x64, 0x00)
        r_t2 = p_g2.add_run(f'\"{p2}\"')
        r_t2.bold = True
        r_t2.font.color.rgb = RGBColor(0x00, 0x5A, 0x9E)
        p_g2.add_run(f'  [{len(p2)} car.]').italic = True
    else:
        p_g = doc.add_paragraph()
        p_g.add_run('• 🧪 Orden / Prompt listo para pegar en Gemini (gemini.google.com): ').bold = True
        r_gt = p_g.add_run(f'\"{prompt_gemini}\"')
        r_gt.bold = True
        r_gt.font.color.rgb = RGBColor(0x00, 0x5A, 0x9E)
        p_g.add_run(f'  [{len(prompt_gemini)} car.]').italic = True
    doc.add_paragraph()

"""

if idx_def != -1 and idx_def_end != -1:
    text = text[:idx_def] + new_taller_def + text[idx_def_end:]
    print('-> add_taller_item actualizado correctamente.')

# 2. Buscamos el inicio del Módulo A y el final del Módulo D (hasta output_path = ...)
idx_b4 = text.find('add_header_2(\'1. Módulo A: Retoque Fotográfico y Mejora Cotidiana\')')
if idx_b4 == -1:
    idx_b4 = text.find('add_header_2("1. Módulo A: Retoque Fotográfico y Mejora Cotidiana")')

idx_end_b4 = text.find('output_path = ', idx_b4)

new_block_iv = """add_header_2("1. Módulo A: Retoque Fotográfico y Mejora Cotidiana")
add_taller_item("4.1.1.", "Mejora automática de foto oscura o quemada",
    "Corregir automáticamente el balance de blancos, la exposición y el contraste de una fotografía tomada en malas condiciones de luz.",
    ("Genera una fotografía amateur de muy mala calidad tomada con un móvil en el interior de un restaurante poco iluminado. Se ve un plato de paella en una mesa, pero la foto ha salido exageradamente oscura, subexpuesta y con mucho ruido granular.",
     "Ahora corrige automáticamente la exposición y la iluminación de esta foto oscura. Sube el brillo, recupera detalles ocultos en las sombras, elimina el ruido y ajusta el balance de blancos para que la paella quede niquelada y apetecible."))

add_taller_item("4.1.2.", "Corrección e iluminación facial de retratos",
    "Eliminar imperfecciones temporales como acné, brillos o sombras duras en la piel, manteniendo los rasgos naturales del rostro.",
    ("Genera un retrato casero con iluminación dura y desfavorable de un hombre de 60 años con brillos intensos en la frente por un flash directo, sombras marcadas bajo los ojos y algunas rojeces en la mejilla.",
     "Retoca suavemente este retrato como un fotógrafo profesional: elimina los brillos cegadores en la frente, suaviza las sombras bajo los ojos y borra las rojeces manteniendo una piel niquelada y natural."))

add_taller_item("4.1.3.", "Restauración y coloreado de fotos antiguas",
    "Recuperar fotos familiares en blanco y negro, sepia o dañadas por el paso del tiempo, devolviéndoles la nitidez y un color realista 8K.",
    ("Genera una fotografía antigua y deteriorada en blanco y negro de los años 40 de una pareja de novios, con rasguños en el papel, manchas amarillentas del paso del tiempo y bordes desgastados.",
     "Restaura por completo esta foto antigua: repara los rasguños del papel, elimina las manchas amarillentas, devuélvele una nitidez impecable 8K y coloréala con tonos reales y naturales."))

add_taller_item("4.1.4.", "Foto de Perfil Profesional para LinkedIn / Currículum",
    "Transformar una foto informal (de vacaciones o callejera) en un retrato profesional de estudio con vestimenta elegante y fondo sobrio.",
    ("Genera una foto informal de un hombre con camiseta colorida y gafas de sol en una playa abarrotada de turistas, sonriendo relajadamente frente a cámara.",
     "Transforma esta foto informal en un retrato profesional para LinkedIn: sustituye su camiseta y gafas por una chaqueta o camisa elegante y cambia la playa por un estudio gris neutro."))

add_header_2("2. Módulo B: Edición Selectiva, Eliminación y Sustitución de Elementos")
add_taller_item("4.2.1.", "Eliminación de objetos o personas molestos",
    "Quitar elementos no deseados de una foto (turistas de fondo, farolas, cables, cubo de basura) rellenando el fondo de manera inteligente.",
    ("Genera una hermosa fotografía de un faro junto al mar al amanecer, pero justo en primer plano coloca a un turista despistado con camisa llamativa y un cubo de basura grande afeando la vista.",
     "Elimina por completo al turista despistado y el cubo de basura del primer plano, rellenando el fondo marino y las rocas con total naturalidad para que el faro luzca despejado."))

add_taller_item("4.2.2.", "Añadir ropa y complementos al retrato",
    "Incorporar prendas o accesorios realistas a una persona en la foto, ajustándose a la iluminación y postura.",
    ("Genera el retrato frontal de una mujer elegante de 55 años sonriendo, vestida simplemente con un jersey beige liso sobre un fondo urbano suave.",
     "Añade a la mujer de la fotografía una bufanda de lana roja elegante rodeando su cuello y un moderno sombrero de fieltro oscuro, integrando perfectamente las sombras y la luz."))

add_taller_item("4.2.3.", "Cambio de look y peinado retro (Estilo Años 80)",
    "Modificar el corte de pelo, el peinado y el color capilar de una persona en foto para adaptarlo a una estética o década concreta.",
    ("Genera un retrato realista actual de un hombre de 50 años con pelo corto formal y barba arreglada, mirando a cámara en un interior iluminado.",
     "Cambia el look capilar de este hombre para darle un estilo rockero de los años 80: ponle una melena con volumen cardado de época y cambia su camisa por una chupa de cuero negro."))

add_taller_item("4.2.4.", "Probador virtual de ropa (E-commerce)",
    "Vestir de forma realista a una modelo en una foto utilizando otra imagen de referencia donde se muestre la prenda por separado.",
    ("Genera en la misma imagen dos paneles divididos: a la izquierda, la foto frontal de una mujer con ropa sencilla de estar por casa; y a la derecha, la foto de un elegante vestido de fiesta azul zafiro.",
     "Viste a la mujer de la izquierda con el vestido de fiesta azul zafiro de la derecha, ajustando perfectamente la caída de la tela y los reflejos al cuerpo de forma fotorrealista."))

add_taller_item("4.2.5.", "Reconstrucción de objetos o fotos rotas",
    "Reconstruir una imagen cortada por la mitad o reparar objetos rotos que aparezcan en ella (como una cerámica o espejo fracturado).",
    ("Genera la foto de un hermoso plato de cerámica artesanal pintado con motivos florales, pero el plato aparece partido en tres trozos sobre una mesa de madera con pedazos sueltos.",
     "Reconstruye mágicamente el plato de cerámica roto juntando todos los pedazos, sellando las grietas por completo y dejándolo impecable como recién salido del taller."))

add_header_2("3. Módulo C: Transformaciones Avanzadas, de Boceto a Realidad y Modelos 3D")
add_taller_item("4.3.1.", "Restauración digital de monumentos históricos",
    "Reconstruir digitalmente ruinas o monumentos antiguos (como el Coliseo de Roma o el Alcázar real) para mostrarlos en su esplendor original.",
    ("Genera una fotografía realista de las ruinas del Coliseo Romano tal y como se ven hoy en día, con partes derrumbadas, piedra desgastada y cielo despejado.",
     "Reconstruye digitalmente el Coliseo Romano devolviéndole su esplendor arquitectónico original del siglo I: completa los muros faltantes, las estatuas y el mármol exterior."))

add_taller_item("4.3.2.", "Reinterpretación fantástica de lugares conocidos",
    "Transformar una fotografía urbana o paisaje célebre en un escenario de ciencia ficción o fantasía pura.",
    ("Genera una fotografía diurna clara y realista del Palacio de Cibeles y la fuente en Madrid, con tráfico moderno y viandantes paseando.",
     "Transforma esta fotografía del Palacio de Cibeles en una metrópolis futurista cyberpunk de ciencia ficción por la noche, con coches voladores de neón y cielo galáctico."))

add_taller_item("4.3.3.", "De Boceto a Foto Real (Sketch to Real 8K)",
    "Subir una foto de un dibujo a lápiz, boceto esquemático o acuarela simple y convertirlo en una fotografía fotorrealista 8K.",
    ("Genera un dibujo o boceto a lápiz sobre papel blanco, con líneas esquemáticas que representan una acogedora cabaña de madera en un bosque nevado con humo en la chimenea.",
     "Interpreta este boceto a lápiz y conviértelo en una fotografía fotorrealista 8K de alta calidad, con texturas de madera de pino reales, nieve esponjosa y luz cálida en las ventanas."))

add_taller_item("4.3.4.", "De Captura de Mapa a Vista Fotorrealista 3D",
    "Convertir una captura de pantalla de un plano, mapa o callejero topográfico en una vista aérea fotorrealista en relieve de la zona.",
    ("Genera la captura de pantalla de un mapa callejero topográfico 2D simple con líneas amarillas y grises mostrando varias manzanas de edificios y un parque central verde.",
     "Convierte este plano 2D esquemático en una impresionante maqueta fotorrealista en 3D vista en ángulo isométrico, donde los edificios y árboles cobren volumen y sombra real."))

add_taller_item("4.3.5.", "De Foto a Diseño de Tatuaje Minimalista",
    "Extraer la silueta y rasgos de una fotografía real para convertirla en un diseño artístico lineal de tatuaje en tinta negra.",
    ("Genera una fotografía macro muy nítida de la cara de un león rugiendo con su majestuosa melena bajo luz dramática lateral.",
     "Extrae la esencia del león de esta fotografía y conviértela en un diseño de tatuaje minimalista lineal en tinta negra sobre fondo blanco, con trazos geométricos finos."))

add_taller_item("4.3.6.", "Extracción y Aislamiento 3D de un objeto",
    "Aislar un objeto o producto del fondo de una foto de manera impecable y generarlo con iluminación neutra como modelo de catálogo 3D.",
    ("Genera la foto de unas zapatillas deportivas rojas y blancas muy chulas puestas sobre una mesa desordenada con libros, tazas de café y cables alrededor.",
     "Aísla y recorta únicamente las zapatillas rojas eliminando toda la mesa y el desorden de fondo, y preséntalas flotando sobre un fondo blanco neutro de catálogo comercial 3D."))

add_header_2("4. Módulo D: Proyectos Creativos, Model Sheet, Escenas, Tipografía y Merchandising")
add_taller_item("4.4.1.", "Creación de hoja de personaje (Model Sheet)",
    "A partir de la foto de un solo personaje, generar una lámina técnica con sus 3 vistas: frontal, perfil y trasera sobre fondo blanco.",
    ("Genera el retrato de cuerpo entero de un explorador aventurero estilo animación 3D, con sombrero de cuero, mochila y brújula, sonriendo frente a cámara.",
     "A partir de este personaje, crea una lámina técnica de estudio (Model Sheet) que muestre al mismo explorador en 3 vistas alineadas: de frente, de perfil y de espaldas sobre fondo blanco."))

add_taller_item("4.4.2.", "Escenas coherentes manteniendo el personaje",
    "Utilizar al personaje recién creado para colocarlo en diferentes situaciones, aventuras y encuadres sin que cambie su rostro ni ropa.",
    ("Genera la foto de referencia de un simpático abuelo con gafas redondas, chaleco verde y bastón de paseo sentado en un banco de parque.",
     "Coloca a este mismo abuelo de las gafas redondas y chaleco verde dentro de una moderna biblioteca examinando un globo terráqueo antiguo, manteniendo exactamente su rostro y ropa."))

add_taller_item("4.4.3.", "Escena de acción a partir de boceto y personajes",
    "Combinar las imágenes de los personajes de referencia con un boceto esquemático para crear una composición dinámica de acción.",
    ("Genera en una sola imagen dos elementos: a un lado, la foto de un caballero medieval con armadura plateada; y al otro, un boceto esquemático a lápiz luchando contra un dragón.",
     "Combina la referencia del caballero con el boceto del puente y crea una ilustración de acción cinemática 8K donde el caballero luche contra un imponente dragón escupiendo fuego."))

add_taller_item("4.4.4.", "Collage Múltiple Inteligente (Hasta 13 referencias)",
    "Poner a trabajar juntas múltiples imágenes de referencia (personajes, objetos, fondo, iluminación) y fusionarlas en un solo cuadro magistral.",
    ("Genera un collage en cuadrícula que muestre 4 elementos separados: una guitarra acústica, una fogata nocturna, una tienda de campaña retro y un cielo estrellado del bosque.",
     "Une e integra todos los elementos de esta cuadrícula (la guitarra, la fogata, la tienda y las estrellas) en una única fotografía fotorrealista coherente de una noche de campamento en el bosque."))

add_taller_item("4.4.5.", "Textos con Texturas 3D (Efecto CGI)",
    "Escribir palabras o frases en pantalla aplicando a las letras la textura física de un objeto de referencia (lana, hielo, pan de oro, peluche).",
    ("Genera un primer plano macro muy detallado de un ovillo de lana gruesa trenzada de color turquesa y amarillo con fibras suaves y esponjosas.",
     "Escribe en el centro de la pantalla la palabra 'CREATIVIDAD' en letras mayúsculas gruesas 3D, pero aplicando exactamente la textura, volumen y esponjosidad de la lana turquesa."))

add_taller_item("4.4.6.", "Diseño de tipografía a partir de referencia",
    "Imitar el estilo de letra o tipografía artística que aparece en una foto de referencia para escribir un nuevo título en español.",
    ("Genera la foto de un antiguo cartel de circo vintage del siglo XIX con letras góticas doradas muy ornamentadas y sombras rojas.",
     "Imita el estilo tipográfico exacto, los adornos dorados y la sombra roja de ese cartel para escribir en español la frase 'GRAN ESCUELA DE IA' en un nuevo letrero festivo."))

add_taller_item("4.4.7.", "Diseño de Logotipos profesionales desde descripción",
    "Crear emblemas vectoriales, logotipos o insignias limpias para asociaciones, cursos o marcas desde una instrucción de texto.",
    ("Genera una lámina con 3 bocetos preliminares en blanco y negro para el logotipo de una asociación cultural de mayores llamada 'Saber y Arte', combinando un libro y un árbol.",
     "Elige el concepto central del libro con el árbol y conviértelo en un logotipo vectorial definitivo e impecable a color, con trazos dorados y azules sobre fondo blanco, elegante y limpio."))

add_taller_item("4.4.8.", "Variaciones automáticas de un Logotipo",
    "A partir de un logo existente, crear múltiples adaptaciones prácticas: en blanco y negro, en sello circular, en metálico dorado o bordado.",
    ("Genera un logotipo vectorial moderno de una taza de café humeante con forma de corazón en colores marrón y crema para una cafetería llamada 'Café del Buen Día'.",
     "A partir de este logotipo, crea 4 adaptaciones en una lámina: 1) Versión monocromática negra para sello; 2) Pegatina circular; 3) Relieve metálico dorado; 4) Bordado en delantal."))

add_taller_item("4.4.9.", "Diseño y Aplicación de Etiquetas de Producto",
    "Crear una etiqueta comercial (para una botella de vino, aceite de oliva o cerveza artesanal) y aplicarla en una foto de producto real.",
    ("Genera el diseño plano frontal de una etiqueta gourmet para una botella de aceite de oliva virgen extra llamado 'Oro de Andalucía', con ilustraciones en oro sobre verde oscuro.",
     "Aplica esta etiqueta que acabas de diseñar sobre la fotografía realista de una botella de vidrio oscuro de aceite de oliva colmada sobre una mesa rústica de madera junto a aceitunas frescas."))

add_taller_item("4.4.10.", "Banners Publicitarios Completos",
    "Combinar en un solo cartel publicitario la foto de un producto, el logotipo de la marca y un fondo atractivo en perfecta armonía.",
    ("Genera la fotografía de estudio de un elegante reloj de pulsera con correa de cuero marrón y esfera azul zafiro flotando sobre fondo blanco puro con iluminación comercial.",
     "Toma la foto de este reloj y crea un banner publicitario apaisado completo: colócalo sobre un fondo oscuro elegante con reflejos dorados, añade el logotipo 'CHRONOS' y el eslogan 'El tiempo en tus manos'."))

add_taller_item("4.4.11.", "Rediseño Cultural de Marca (Locales Internacionales)",
    "Adaptar la estética de un anuncio o cartel occidental al estilo visual de otra cultura (por ejemplo, al minimalismo zen japonés).",
    ("Genera un colorido cartel publicitario occidental para una hamburguesería americana estilo diner de los años 50 con luces de neón rosa, ajedrezado blanco y negro y letras audaces.",
     "Rediseña por completo este anuncio de hamburguesería para adaptarlo a la estética cultural japonesa: conviértelo en un cartel minimalista zen en madera clara con tipografía japonesa y tinta sumi-e."))

"""

if idx_b4 != -1 and idx_end_b4 != -1:
    text = text[:idx_b4] + new_block_iv + text[idx_end_b4:]
    print('-> Bloque IV reescrito al 100% con formato en 2 pasos.')
else:
    print('-> ERROR encontrando límites del Bloque IV:', idx_b4, idx_end_b4)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('=== GUARDADO COMPLETO. EJECUTANDO BUILD REPOSITORIO MAESTRO ===')
