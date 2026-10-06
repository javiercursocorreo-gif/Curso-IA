# -*- coding: utf-8 -*-
"""
build_nat_60_master.py
Define los datos maestros de las 60 Infografías Científicas y Artísticas [NAT-001 a NAT-060]
incorporando:
1. Tema/Sujeto (Fauna noble, extintos/fósiles, virus/nanomundo, supercolonias, criaturas míticas, leyendas del cine).
2. Estilo artístico histórico (Códice Da Vinci, Ukiyo-e, Blueprint, Manuscrito medieval, etc.).
3. Soporte / Papel (Lino, pergamino vitela, cianotipia, washi, pizarra negra, seda, etc.).
4. Estructura de particiones / viñetas explícita (tríptico, 4 recuadros, circular diana, etc.).
5. Metodología en 3 Pasos del Alumno:
   - Paso 1: Prompt corto y natural de encargo a Gemini (con los 4 ingredientes claros).
   - Paso 2: Gemini redacta el Súper Prompt Maestro técnico en inglés con módulos y rigor.
   - Paso 3: El alumno ordena "Ejecuta este prompt y genera la imagen".
   - Reto de Autonomía: "Ahora haz tú lo mismo para otro ser o criatura".
"""

NAT_ITEMS = [
    {
        "id": "NAT-001",
        "num": 1,
        "title": "El Caballo Salvaje y la Biomecánica del Galope",
        "category": "Fauna Salvaje Noble & Depredadores",
        "subject": "El Caballo Salvaje (Equus ferus)",
        "style_art": "Códice Renacentista de Leonardo da Vinci a tinta sepia y sanguina",
        "paper": "Papel de lino renacentista tostado con leves manchas de cera",
        "layout": "Cuadrícula de 4 viñetas explicativas más boceto central en movimiento",
        "details_es": "1. El casco amortiguador de 1 tonelada de impacto; 2. La columna vertebral flexible; 3. El pistón intestinal que acopla la respiración al galope; 4. Los cuartos traseros propulsores.",
        "concept": "Descubre cómo el galope de un caballo no es solo fuerza bruta, sino una perfecta máquina de palancas biológicas donde la respiración y los pasos están matemáticamente acoplados.",
        "short_prompt": (
            "Actúa como un ilustrador científico del Renacimiento y experto en biomecánica equina. "
            "Quiero una lámina anatómica sobre el CABALLO SALVAJE en estilo boceto de Leonardo da Vinci "
            "a tinta sepia sobre papel de lino tostado. La composición debe estar organizada en una cuadrícula "
            "de 4 viñetas explicativas alrededor de un gran dibujo central del caballo al galope: "
            "1. Corte del casco y almohadilla amortiguadora; 2. Columna vertebral elástica; "
            "3. Pistón visceral acoplado a los pulmones; 4. Musculatura de los cuartos traseros. "
            "Redáctame el prompt maestro completo en inglés, con máxima resolución y sin textos borrosos, "
            "para generar esta infografía con IA."
        ),
        "master_prompt_en": (
            "A masterwork Renaissance scientific codex in the style of Leonardo da Vinci's anatomical notebooks. "
            "Subject: The Wild Horse (Equus ferus) in full gallop. Drawn with sepia ink, fine cross-hatching, and sanguine red chalk on aged textured toasted linen paper with subtle foxing and deckled edges. "
            "Composition: Centered around a highly detailed dynamic sketch of a wild stallion galloping at full speed, breaking into the foreground. "
            "Surrounding the central subject are precisely 4 numbered rectangular modular inset sketches connected by delicate calligraphic guide lines: "
            "Inset 1: Cross-section anatomical diagram of the equine hoof showing the digital cushion absorbing high-impact shock. "
            "Inset 2: Biomechanical skeletal sketch of the flexible lumbar spine acting as a spring. "
            "Inset 3: Respiratory thoracic diagram showing the visceral piston synchronizing breath with each stride. "
            "Inset 4: Muscular diagram of the hindquarters displaying explosive propulsive tendons. "
            "Clean layout, museum editorial quality, ultra-sharp 8k resolution, authentic antique manuscript atmosphere, zero watermarks, zero modern elements."
        ),
        "scientific_tip": "¿Por qué los veterinarios afirman que un caballo al galope sólo puede respirar exactamente una vez por cada zancada que da?",
        "creative_challenge": "Pide ahora a Gemini: 'Hazme este mismo encargo con el mismo estilo de Leonardo da Vinci pero para un LEOPARDO cazando'."
    },
    {
        "id": "NAT-002",
        "num": 2,
        "title": "El Mamut Lanudo: Termorregulación en la Edad de Hielo",
        "category": "Criaturas Extinguidas & Dinosaurios",
        "subject": "El Mamut Lanudo (Mammuthus primigenius)",
        "style_art": "Diario de expedición polar siberiana del siglo XIX",
        "paper": "Cuaderno de campo de explorador ártico con manchas de óxido y hielo",
        "layout": "Tríptico de 3 paneles verticales más vista central del mamut en ventisca",
        "details_es": "1. Pelaje de triple capa y glándulas sebáceas; 2. Joroba lipídica de reserva calórica; 3. Colmillos curvados quitanieves para desbrozar pastos helados.",
        "concept": "Explora cómo este titán del Pleistoceno sobrevivía a temperaturas de 50 grados bajo cero gracias a un blindaje térmico natural y una sangre anticongelante.",
        "short_prompt": (
            "Actúa como un naturalista y explorador ártico del siglo XIX. "
            "Quiero una lámina científica sobre el MAMUT LANUDO en estilo diario de expedición siberiana, "
            "dibujada a tinta negra y aguadas grises sobre papel envejecido de cuaderno de campo. "
            "Organiza la lámina en un tríptico de 3 paneles anatómicos: "
            "1. Corte del pelaje de triple capa con aislamiento térmico; 2. La joroba de grasa en el lomo; "
            "3. La curvatura de los colmillos gigantes como palas quitanieves. "
            "Redáctame el prompt maestro completo en inglés para generar esta infografía con rigor paleontológico."
        ),
        "master_prompt_en": (
            "A 19th-century Arctic expedition field journal page illustrating the anatomy and survival mechanisms of the Woolly Mammoth (Mammuthus primigenius). "
            "Rendered in vintage black ink cross-hatching and subtle charcoal wash on heavily weathered parchment with frosty edges and ice-crystal watermarks. "
            "Composition: Dominated by a central majestic drawing of a woolly mammoth walking through an ice age blizzard. "
            "Structured into a three-panel vertical triptych layout: "
            "Panel 1: Microscopic cutaway of the triple-layer fur system showing the dense 1-meter guard hairs and insulating woolly undercoat. "
            "Panel 2: Anatomical diagram of the large dorsal fat hump storing metabolic energy and lipids against subzero temperatures. "
            "Panel 3: Biomechanical study of the 4-meter spiraled ivory tusks used as snow shovels to uncover tundra vegetation. "
            "Authentic naturalist handwriting annotations, museum catalog labels, high precision linework, 8k resolution, timeless historical illustration."
        ),
        "scientific_tip": "¿Qué mutación en la hemoglobina del mamut lanudo le permitía transportar oxígeno por su sangre a temperaturas donde otros mamíferos se congelaban?",
        "creative_challenge": "Pide a Gemini: 'Redáctame el prompt maestro con este mismo estilo polar del siglo XIX pero para un RINOCERONTE LANUDO'."
    },
    {
        "id": "NAT-003",
        "num": 3,
        "title": "El Bacteriófago T4: El Nanorobot de la Naturaleza",
        "category": "Micro-Mundo, Virus, Bacterias & Insectos",
        "subject": "Bacteriófago T4 (Virus destructor de bacterias)",
        "style_art": "Blueprint cuántico y diagrama de nanotecnología industrial",
        "paper": "Plano técnico cianotipia de fondo azul cobalto con líneas milimétricas blancas",
        "layout": "Despiece técnico de 4 módulos de maquinaria biológica numerados",
        "details_es": "1. Cápside icosaédrica con ADN presurizado; 2. Collarín y rotor central; 3. Vaina contráctil inyectora; 4. Las 6 patas basales articuladas de aterrizaje.",
        "concept": "Descubre el virus con forma de módulo lunar que parece una máquina diseñada por ingenieros y funciona como una jeringuilla molecular microscópica.",
        "short_prompt": (
            "Actúa como un ingeniero en nanotecnología y microbiólogo. "
            "Quiero una infografía técnica sobre el BACTERIÓFAGO T4 en estilo plano blueprint arquitectónico, "
            "con fondo azul cobalto oscuro y líneas vectoriales blancas de alta precisión. "
            "La lámina debe mostrar un despiece esquemático de 4 piezas numeradas: "
            "1. La cabeza icosaédrica con ADN empaquetado; 2. El cuello o collarín mecánico; "
            "3. La vaina contráctil que perfora la membrana; 4. Las 6 patas basales de anclaje. "
            "Redáctame el prompt maestro completo en inglés para generar este plano de nanotecnología."
        ),
        "master_prompt_en": (
            "An ultra-detailed technical engineering blueprint schematic of the T4 Bacteriophage virus, treating it as biological nanotechnology. "
            "Rendered in deep cobalt blue cyanotype architectural blueprint style with crisp white technical drafting lines, millimeter grids, and geometric callouts. "
            "Composition: Centered isometric cutaway of the bacteriophage virus resembling an Apollo lunar lander. "
            "Arranged in 4 mechanical exploded-view technical modules: "
            "Module 1: Icosahedral capsid head displaying tightly spooled double-stranded DNA under high internal pressure. "
            "Module 2: Central neck collar and whiskers functioning as sensory mechanical triggers. "
            "Module 3: Contractile helical sheath acting as a spring-loaded nano-syringe piercing cell walls. "
            "Module 4: Six tail fibers articulated like robotic landing legs with receptor landing pins. "
            "Clean technical vector aesthetics, patent diagram styling, 8k resolution, crisp drafting typography, zero blur."
        ),
        "scientific_tip": "¿Sabías que la presión dentro de la cabeza del bacteriófago T4 es de 50 atmósferas, equivalente a la presión de una botella de champán multiplicada por diez?",
        "creative_challenge": "Pide a Gemini: 'Hazme este mismo plano blueprint técnico pero para un VIRUS DE LA GRIPE (Influenza) y sus espículas de proteína'."
    },
    {
        "id": "NAT-004",
        "num": 4,
        "title": "La Abeja Melífera y el Panal: Matemáticas del Hexágono",
        "category": "Arquitectura Animal & Supercolonias",
        "subject": "La Abeja Melífera (Apis mellifera) y la Celda Hexagonal",
        "style_art": "Tratado de Geometría Sagrada euclidiana y manuscrito renacentista",
        "paper": "Pergamino de vitela con círculos de compás en tinta sepia y toques dorados",
        "layout": "4 viñetas geométricas concéntricas con demostración matemática",
        "details_es": "1. Teorema del panal: por qué el hexágono gasta menos cera que el triángulo o el cuadrado; 2. Glándulas cereras del abdomen; 3. Inclinación de 13° de las celdas para que no caiga la miel; 4. La danza del ocho para indicar flores.",
        "concept": "Comprende por qué matemáticos y arquitectos llevan siglos fascinados con las abejas: construyen la estructura más resistente y ligera posible con el mínimo gasto de material.",
        "short_prompt": (
            "Actúa como un matemático y botánico renacentista. "
            "Quiero una lámina infográfica sobre LA ABEJA Y EL PANAL HEXAGONAL en estilo tratado de geometría "
            "de Euclides sobre pergamino vitela, con líneas de compás en tinta sepia. "
            "Distribuye la información en 4 recuadros geométricos: "
            "1. Demostración geométrica del hexágono frente al círculo y cuadrado; "
            "2. Las glándulas cereras del abdomen de la abeja; "
            "3. La inclinación de 13 grados de las celdas para retener la miel líquida; "
            "4. Diagrama de la danza en ocho con ángulos respecto al sol. "
            "Redáctame el prompt maestro completo en inglés con máxima precisión gráfica."
        ),
        "master_prompt_en": (
            "A classical Renaissance mathematical treatise and natural philosophy manuscript illustrating the architectural genius of the Honeybee (Apis mellifera) and the hexagonal comb. "
            "Drawn in sepia ink with compass construction lines, golden section ratios, and faint gold leaf highlights on antique vellum parchment. "
            "Composition: Centered around an intricate cross-section of a honeycomb frame populated by worker bees. "
            "Surrounded by 4 geometric explanatory insets: "
            "Inset 1: Mathematical proof of the Honeycomb Conjecture comparing circle packing, triangles, and hexagons showing minimum wax surface area. "
            "Inset 2: Microscopic anatomical sketch of the abdominal wax mirror glands secreting beeswax flakes. "
            "Inset 3: Architectural incline diagram showing the 9-14 degree upward tilt of each cell preventing honey leakage. "
            "Inset 4: Celestial navigation map illustrating the waggle dance figure-eight angle relative to solar polarization. "
            "Sacred geometry drafting lines, Latin and Spanish scientific notes, immaculate detail, 8k resolution, elegant museum piece."
        ),
        "scientific_tip": "¿Por qué las abejas no hacen las celdas redondas si sus cuerpos son redondeados? ¿Quién demostró matemáticamente en 1999 que el hexágono es perfecto?",
        "creative_challenge": "Pide a Gemini: 'Redáctame un prompt maestro en estilo tratado renacentista pero sobre LA ESPIRAL ÁUREA DE LA CONCHA DEL NAUTILUS'."
    },
    {
        "id": "NAT-005",
        "num": 5,
        "title": "El Unicornio: Fisiología del Cuerno de Alabastro",
        "category": "Animales Mitológicos, Fantásticos & Legendarios",
        "subject": "El Unicornio Clásico (Monoceros)",
        "style_art": "Bestiario Iluminado Medieval del siglo XIII con pan de oro",
        "paper": "Pergamino de cuero de vitela con orlas góticas florales y miniaturas doradas",
        "layout": "4 medallones heráldicos circulares alrededor de la criatura mítica",
        "details_es": "1. Fusión ósea del cuerno en la sutura frontal del cráneo; 2. Estrías helicoidales de queratina y calcita; 3. Cascos hendidos de ciervo para escalar riscos escarpados; 4. Neutralización química de toxinas en manantiales.",
        "concept": "Imagina cómo habría analizado un erudito medieval la anatomía fantástica del unicornio, considerándolo una especie real de los bosques boreales.",
        "short_prompt": (
            "Actúa como un monje miniaturista y naturalista del siglo XIII. "
            "Quiero una lámina anatómica de bestiario medieval sobre EL UNICORNIO, "
            "pintada sobre pergamino iluminado con pan de oro y tintas minerales (rojo bermellón y azul lapislázuli). "
            "Organiza la lámina en 4 medallones góticos circulares: "
            "1. Anclaje del cuerno en el hueso frontal del cráneo; 2. Corte transversal de la espiral helicoidal; "
            "3. Pezuñas hendidas de antílope; 4. Reacción del cuerno al purificar agua envenenada. "
            "Redáctame el prompt maestro completo en inglés para generar esta obra de arte medieval."
        ),
        "master_prompt_en": (
            "A genuine 13th-century illuminated medieval bestiary manuscript page depicting the mythical anatomy of the Unicorn (Monoceros). "
            "Executed with lapis lazuli blues, vermilion red gouache, intricate burnished gold leaf filigree, and gall ink calligraphy on aged calfskin vellum with Gothic border flourishes. "
            "Composition: Centered on an elegant, noble white unicorn reclining beside an enchanted forest fountain. "
            "Arranged with 4 circular Gothic medallion vignettes revealing mythical anatomy: "
            "Medallion 1: Cranial osteology showing the seamless fusion of the frontal suture anchoring the spiral horn. "
            "Medallion 2: Transverse cross-section of the alicorn horn displaying helical keratin rings and mineralized calcite core. "
            "Medallion 3: Detail of the cloven hooves adapted like an alpine ibex for leaping across treacherous stone crags. "
            "Medallion 4: Alchemical purification test showing the horn dipping into murky marsh water turning it crystalline clear. "
            "Authentic medieval heraldic elegance, gilded leaf accents, museum illumination masterpiece, 8k resolution."
        ),
        "scientific_tip": "¿Qué animal real del Ártico engañó a reyes y comerciantes durante siglos vendiendo sus colmillos como auténticos cuernos de unicornio?",
        "creative_challenge": "Pide a Gemini: 'Genera este mismo estilo de bestiario medieval iluminado con pan de oro pero para EL AVE DE FUEGO FÉNIX'."
    },
    {
        "id": "NAT-006",
        "num": 6,
        "title": "Lassie (El Collie de Pastor): Olfato y Acústica de Rescate",
        "category": "Leyendas Animales del Cine y la Cultura Popular",
        "subject": "Lassie / El Rough Collie (Collie de pelo largo)",
        "style_art": "Cartel litográfico vintage de cine de los años 40/50 y lámina zoológica",
        "paper": "Papel litográfico de imprenta retro ligeramente satinado y envejecido",
        "layout": "4 recuadros de facultades sensoriales caninas con tipografía clásica",
        "details_es": "1. Los 300 millones de receptores olfativos del hocico; 2. Los 18 músculos de la oreja para captar ultrasonidos de socorro; 3. El pelaje de doble capa aislante; 4. El mapa cognitivo de memoria de rutas.",
        "concept": "Descubre la ciencia real detrás del perro más famoso de la historia: cómo la genética del perro de pastor le otorga una capacidad de rescate y memoria que parece sobrenatural.",
        "short_prompt": (
            "Actúa como un ilustrador editorial de los años 50 y veterinario canino. "
            "Quiero una lámina infográfica sobre LASSIE (EL ROUGH COLLIE DE PASTOR) en estilo litografía "
            "retro de mediados del siglo XX sobre papel crema con marcos clásicos. "
            "La infografía debe tener 4 viñetas explicativas: "
            "1. Corte del hocico con sus 300 millones de receptores olfativos; "
            "2. Sistema de 18 músculos que orientan las orejas hacia llamadas lejanas; "
            "3. Corte del pelaje impermeable de rescate; "
            "4. Mapa mental de orientación para regresar a casa desde cientos de kilómetros. "
            "Redáctame el prompt maestro completo en inglés con estética entrañable y rigurosa."
        ),
        "master_prompt_en": (
            "A 1950s classic vintage lithograph and canine veterinary chart celebrating the heroic biology of Lassie the Rough Collie sheepdog. "
            "Warm mid-century nostalgic print palette on heavy cream bond paper with elegant serif typography and lithographic hatching. "
            "Composition: Centered around a majestic full-body oil-tinted portrait of Lassie in proud rescue stance against a pastoral highland landscape. "
            "Flanked by 4 vintage scientific explanatory insets: "
            "Inset 1: Anatomical nasal diagram showing 300 million olfactory receptors and the vomeronasal organ tracking faint scent trails. "
            "Inset 2: Ear muscular diagram showing 18 independent muscles swiveling the semi-pricked ears to pinpoint ultrasonic distress frequencies. "
            "Inset 3: Cross-section of the dense double coat: coarse waterproof outer guard hairs over soft insulating wool. "
            "Inset 4: Cognitive spatial navigation chart illustrating canine geomagnetic and episodic memory for long-distance homecoming. "
            "Classic Golden Age print look, warm colors, nostalgic Americana naturalist aesthetic, 8k resolution, crisp artwork."
        ),
        "scientific_tip": "¿Sabías que los perros de pastor pueden oír ruidos a una distancia cuatro veces mayor que el oído humano más fino?",
        "creative_challenge": "Pide a Gemini: 'Hazme una lámina litográfica retro de los años 50 pero para EL PASTOR ALEMÁN REX (POLICÍA)'."
    },
    {
        "id": "NAT-007",
        "num": 7,
        "title": "El Pulpo Común: 9 Cerebros y Camuflaje Dinámico",
        "category": "Fauna Salvaje Noble & Depredadores",
        "subject": "El Pulpo Común (Octopus vulgaris)",
        "style_art": "Grabado xilográfico tradicional japonés Ukiyo-e",
        "paper": "Papel de arroz Washi japonés fibroso con textura de madera prensada",
        "layout": "Composición circular concéntrica marina con 4 zonas de detalle",
        "details_es": "1. Cromatóforos elásticos y papilas de piel reflectante; 2. Tres corazones independientes; 3. Sistema nervioso distribuido con un minicerebro en cada tentáculo; 4. El sifón de propulsión a chorro de agua.",
        "concept": "Descubre al invertebrado más inteligente del océano: una criatura que ve con la piel, piensa con sus brazos y cambia de color y textura en milisegundos.",
        "short_prompt": (
            "Actúa como un maestro del grabado japonés Ukiyo-e y biólogo marino. "
            "Quiero una infografía sobre EL PULPO COMÚN en estilo grabado en madera sobre papel de arroz Washi, "
            "con tinta china sumi-e y tonos añil y coral. "
            "Organiza la lámina en un diagrama circular con 4 áreas explicativas: "
            "1. La piel con cromatóforos que cambian de color como píxeles; 2. Los 3 corazones que bombean sangre azul; "
            "3. La red de 9 cerebros distribuidos por los tentáculos; 4. El sifón de propulsión a chorro. "
            "Redáctame el prompt maestro completo en inglés para generar este grabado japonés de museo."
        ),
        "master_prompt_en": (
            "A master Japanese Edo-period Ukiyo-e woodblock print infographical chart of the Common Octopus (Octopus vulgaris). "
            "Carved in the style of Hokusai and Hiroshige with deep indigo blue sumi inks, mineral vermilion, and fine woodgrain embossment on fibrous mulberry Washi paper. "
            "Composition: Centered dynamic depiction of an octopus moving weightlessly through a turbulent sea wave. "
            "Arranged in a concentric wave-like circular structure with 4 illustrated anatomical vignettes: "
            "Vignette 1: Microscopic skin texture diagram showing elastic chromatophores, iridophores, and muscular papillae mimicking coral texture. "
            "Vignette 2: Circulatory study of the 3 independent hearts pumping hemocyanin copper-based blue blood. "
            "Vignette 3: Neurological diagram mapping the distributed nervous system: central donut brain plus 8 autonomous arm ganglion brains. "
            "Vignette 4: Hydrodynamic jet siphon propelling water with cloud ink defense mechanism. "
            "Japanese calligraphy seals, authentic woodblock relief impression, museum oriental collection, 8k resolution."
        ),
        "scientific_tip": "¿Por qué la sangre del pulpo es de color azul brillante en lugar de roja como la de los humanos?",
        "creative_challenge": "Pide a Gemini: 'Genera este mismo estilo de grabado japonés Ukiyo-e en madera pero sobre LA SEPIA Y SU CAMUFLAJE'."
    },
    {
        "id": "NAT-008",
        "num": 8,
        "title": "El Tiranosaurio Rex: Biomecánica Craneal Triturahuesos",
        "category": "Criaturas Extinguidas & Dinosaurios",
        "subject": "Tyrannosaurus rex (El rey de los dinosaurios)",
        "style_art": "Atlas paleontológico académico de principios del siglo XX",
        "paper": "Papel sepia cartográfico grueso de archivo de museo geológico",
        "layout": "Tríptico de 3 grandes bloques anatómicos de impacto y visión",
        "details_es": "1. Huesos nasales fusionados para soportar 6 toneladas de mordida; 2. Dientes serrados de 30 cm en forma de plátano que perforan blindajes; 3. Visión estereoscópica profunda binocular como la de un halcón.",
        "concept": "Descubre la física de la mordedura más demoledora de la historia terrestre: un cráneo reforzado capaz de pulverizar los huesos de un Triceratops sin romperse.",
        "short_prompt": (
            "Actúa como un paleontólogo de museos y dibujante anatómico de 1900. "
            "Quiero una lámina científica sobre EL CRÁNEO DEL TIRANOSAURIO REX en estilo atlas "
            "paleontológico sobre cartulina sepia envejecida con grabado a tinta. "
            "Estructura la lámina en 3 bloques anatómicos: "
            "1. La arquitectura de huesos fusionados que absorbía 50.000 Newtons de fuerza; "
            "2. Corte de un diente serrado con raíz profunda; "
            "3. Ángulo de visión binocular estereoscópica frontal. "
            "Redáctame el prompt maestro completo en inglés con absoluto rigor fósil."
        ),
        "master_prompt_en": (
            "An early 20th-century academic paleontological museum atlas plate illustrating the cranial biomechanics of the Tyrannosaurus rex. "
            "Executed in rigorous Victorian lithographic engraving with fine cross-hatching on heavy, warm archival sepia cardstock with specimen measurements. "
            "Composition: Centered around an impressive three-quarter skeletal reconstruction of a T-rex skull roaring in aggressive perspective. "
            "Featuring 3 scientific analytical panels: "
            "Panel 1: Structural cranial stress map demonstrating fused nasal bones and kinetic hinges dissipating 50,000 Newtons of crushing bite force. "
            "Panel 2: Dental cross-section of a 30-centimeter serrated 'banana tooth' showing deep anchoring root and bone-splintering enamel serrations. "
            "Panel 3: Optical alignment diagram illustrating binocular 55-degree forward vision field rivaling modern birds of prey. "
            "Antique museum accession stamps, metric millimeter measurement scales, impeccable anatomical precision, 8k resolution."
        ),
        "scientific_tip": "¿Sabías que los dientes del T-Rex no estaban afilados como cuchillos finos sino redondeados y gruesos como estacas para no partirse al chocar contra huesos macizos?",
        "creative_challenge": "Pide a Gemini: 'Genera este mismo atlas paleontológico de principios del siglo XX para EL TRICERATOPS Y SU CORAZA ÓSEA'."
    },
    {
        "id": "NAT-009",
        "num": 9,
        "title": "El Tardígrado: Criptobiosis y Resistencia al Espacio",
        "category": "Micro-Mundo, Virus, Bacterias & Insectos",
        "subject": "El Tardígrado / Oso de Agua (Hypsibius dujardini)",
        "style_art": "Ilustración de microscopio del siglo XVIII estilo Anton van Leeuwenhoek",
        "paper": "Placa circular con marco de latón envejecido y pergamino iluminado",
        "layout": "4 módulos microscópicos de estados de resistencia extrema",
        "details_es": "1. El estado de 'ton' (barril desecado al 1% de agua); 2. Proteínas Dsup que blindan el ADN contra radiación; 3. Sus 8 patas con garras telescópicas; 4. Supervivencia en el vacío absoluto del espacio y a -200 °C.",
        "concept": "Conoce al ser vivo más indestructible del planeta: puede congelarse, hervirse, someterse a la radiación espacial o pasar 30 años sin comer ni beber y revivir con una gota de agua.",
        "short_prompt": (
            "Actúa como un pionero de la microscopía del siglo XVIII. "
            "Quiero una lámina científica sobre EL TARDÍGRADO (OSO DE AGUA) en estilo grabado antiguo "
            "de microscopio con marco circular de latón pulido sobre pergamino. "
            "Organiza la infografía en 4 módulos explicativos: "
            "1. El proceso de desecación hasta convertirse en barrilete inerte (criptobiosis); "
            "2. Las proteínas especiales que protegen su ADN de la radiación; "
            "3. Anatomía de sus 8 patas con garfios; "
            "4. Su resistencia al vacío del espacio exterior y temperaturas extremas. "
            "Redáctame el prompt maestro completo en inglés con encanto histórico y detalle celular."
        ),
        "master_prompt_en": (
            "An 18th-century early microscopy scientific manuscript illustration of the Water Bear or Tardigrade (Hypsibius dujardini). "
            "Drawn with sepia ink engraving inside an ornate circular polished brass microscope lens frame on warm aged parchment with hand-tinted watercolor washes. "
            "Composition: Centered around a highly magnified, transparent view of a tardigrade crawling among aquatic moss droplets. "
            "Arranged into 4 circular micro-insets detailing extreme survival biology: "
            "Inset 1: Cryptobiosis transformation diagram showing water loss down to 1% contracting into an indestructible glass-like tun state. "
            "Inset 2: Molecular shield study illustrating unique Dsup (damage suppressor) proteins coating and repairing DNA strands against lethal radiation. "
            "Inset 3: Micro-anatomy of the 8 lobopodial legs terminating in microscopic curved chitinous claws. "
            "Inset 4: Environmental resilience chart showing survival at absolute zero (-272 °C), boiling points (150 °C), and open cosmic space vacuum. "
            "Historic Enlightenment engraving style, delicate hand-drawn calligraphy, 8k resolution, authentic antique plate."
        ),
        "scientific_tip": "¿Sabías que en 2007 se enviaron tardígrados vivos a la órbita terrestre expuestos al vacío espacial y regresaron a la Tierra sanos y capaces de poner huevos?",
        "creative_challenge": "Pide a Gemini: 'Genera este mismo estilo de grabado de microscopio del siglo XVIII para EL ROTÍFERO Y SU CORONA CILIADA'."
    },
    {
        "id": "NAT-010",
        "num": 10,
        "title": "Hormigas Cortadoras de Hojas: Granjas Subterráneas de Hongos",
        "category": "Arquitectura Animal & Supercolonias",
        "subject": "Hormigas Cortahojas (Atta cephalotes) y su Nido Agrícola",
        "style_art": "Corte geológico de minería e ingeniería del siglo XIX",
        "paper": "Papel técnico de topografía subterránea con estratos de roca y tierra",
        "layout": "Gran corte vertical de la tierra con 4 niveles de cámaras especializadas",
        "details_es": "1. Mandíbulas cortadoras que cortan hojas como tijeras mecánicas; 2. Cámaras de cultivo del hongo Leucoagaricus; 3. Sistema de chimeneas de ventilación por convección; 4. Vertedero profundo de residuos tóxicos.",
        "concept": "Descubre a las primeras agricultoras del planeta: las hormigas no comen hojas, sino que las recolectan para cultivar un hongo que es su única fuente de alimento.",
        "short_prompt": (
            "Actúa como un ingeniero de minas y entomólogo del siglo XIX. "
            "Quiero una infografía sobre EL HORMIGUERO DE HORMIGAS CORTAHOJAS en estilo corte geológico "
            "transversal de la tierra, sobre papel cuadriculado sepia de minería. "
            "La infografía debe mostrar un gran corte de tierra con 4 cámaras subterráneas: "
            "1. La superficie con hormigas talando hojas con sus mandíbulas; "
            "2. Las cámaras de cultivo donde fermentan el hongo; "
            "3. Las chimeneas que renuevan el aire caliente por efecto chimenea; "
            "4. La fosa séptica profunda donde aíslan la basura tóxica. "
            "Redáctame el prompt maestro completo en inglés con riqueza arquitectónica subterránea."
        ),
        "master_prompt_en": (
            "A 19th-century geological mining cross-section plate illustrating the subterranean agricultural mega-nest of the Leafcutter Ants (Atta cephalotes). "
            "Drawn with technical drafting ink and earth pigment washes on antique sepia mining survey paper showing geological soil strata and root systems. "
            "Composition: A massive vertical cutaway of the earth exposing an 8-meter deep colonial super-structure. "
            "Detailing 4 distinct underground engineering chambers: "
            "Level 1 (Surface): Foraging column of worker ants utilizing vibrating scissor mandibles to slice tropical leaves. "
            "Level 2: Agricultural fungal farming chambers showing symbiotic Leucoagaricus fungal gardens cultivated on chewed leaf pulp. "
            "Level 3: Thermodynamic ventilation shafts demonstrating passive air convection drawing cool breezes through the nest core. "
            "Level 4: Deep waste disposal chambers where specialized elderly waste-hauler ants sequester toxic debris and pathogens. "
            "Elevation depth markers, architectural scale bars, nineteenth-century expedition engraving, 8k resolution."
        ),
        "scientific_tip": "¿Por qué las hormigas ancianas son las encargadas de cuidar el vertedero tóxico de la colonia y nunca vuelven a las cámaras del hongo?",
        "creative_challenge": "Pide a Gemini: 'Genera este corte arquitectónico geológico subterráneo para LA COLONIA DE PERRITOS DE LA PRADERA'."
    }
]

# Generar los 50 elementos restantes completando los 60 items del catálogo oficial
# Manteniendo la rigurosa rotación entre los 6 universos temáticos, 10 estilos, 6 papeles y estructuras variadas.

REST_ITEMS_DATA = [
    # 11: Mítico
    ("NAT-011", 11, "El Dragón Europeo: Glándulas de Biogás e Ignición", "Animales Mitológicos, Fantásticos & Legendarios",
     "El Dragón Europeo (Draco occidentalis)", "Tratado anatómico del Renacimiento tardío (s. XVI)", "Papel grueso tostado con notas en latín",
     "Corte anatómico interno de 4 órganos fantásticos", "Doble pulmón de metano, buche con pirita para chispa, escamas ignífugas y quilla pectoral de 6 metros.",
     "¿Cómo explicaría la ciencia la llamarada de un dragón a través de biogás y piedras de pedernal?", "UN DRAGÓN ORIENTAL CHINO Y SUS PERLAS DE SABIDURÍA"),

    # 12: Leyendas Cine/Historia
    ("NAT-012", 12, "Hachiko (Akita Inu): El Reloj Mental y la Lealtad Canina", "Leyendas Animales del Cine y la Cultura Popular",
     "Hachiko / El Akita Inu (Canis lupus familiaris)", "Grabado Shinhanga tradicional japonés de principios del s. XX", "Papel de arroz Washi con marco de madera y sello rojo",
     "4 viñetas de reloj circadiano y morfología de nieve", "Reloj circadiano de la estación, cola rizada térmica, osamenta de montaña y corteza cerebral de apego.",
     "¿Cómo saben los perros la hora exacta a la que su dueño vuelve a casa sólo con el olfato?", "EL PERRO DE SALVAMENTO SAN BERNARDO CON SU BARRIL"),

    # 13: Fauna Salvaje
    ("NAT-013", 13, "El Halcón Peregrino: Aerodinámica de Picado a 380 km/h", "Fauna Salvaje Noble & Depredadores",
     "El Halcón Peregrino (Falco peregrinus)", "Blueprint aeronáutico militar y cianotipia", "Plano cianotipo azul cobalto con cotas de viento",
     "5 módulos aeronáuticos con vectores de velocidad", "Tubérculos nasales rompevientos, alas en delta rígidas, párpado nictitante de alta presión y garras de impacto.",
     "¿Por qué los motores de los aviones de caza modernos copiaron la nariz del halcón peregrino para no ahogarse a gran velocidad?", "EL ÁGUILA CALVA AMERICANA PESCANDO"),

    # 14: Extintos
    ("NAT-014", 14, "El Tigre Dientes de Sable: Mordida Traqueal y Salto", "Criaturas Extinguidas & Dinosaurios",
     "Smilodon fatalis (Dientes de Sable)", "Grabado al aguafuerte barroco en blanco y negro", "Papel de grabado con barbas de algodón puro",
     "4 módulos de biomecánica de lucha", "Mandíbula con apertura de 120°, debilidad de mordida vs fuerza de empuje cervical, hombros hipertrofiados y caninos de sable.",
     "¿Sabías que la mordida del Smilodon era más débil que la de un león moderno y necesitaba el peso de todo su cuerpo para clavar los sables?", "EL LEÓN DE LAS CAVERNAS DEL PLEISTOCENO"),

    # 15: Micro-Mundo
    ("NAT-015", 15, "El Mosquito Común: Cirugía de 6 Agujas de la Trompa", "Micro-Mundo, Virus, Bacterias & Insectos",
     "El Mosquito hembra (Culex pipiens)", "Diagrama forense quirúrgico médico de precisión", "Papel milimetrado de quirófano en micras",
     "Despiece vertical de las 6 agujas de la probóscide", "Dos maxilas dentadas de sierra, mandíbulas separadoras, cánula inyectora de saliva anticoagulante y canal labral de succión.",
     "¿Por qué la picadura del mosquito no duele en el momento exacto en que te clava sus seis agujas?", "LA GARRAPATA Y SU APARATO DE FIJACIÓN HIPOSTOMA"),

    # 16: Supercolonias
    ("NAT-016", 16, "El Termitero Catedral: Aire Acondicionado Pasivo", "Arquitectura Animal & Supercolonias",
     "Termitero gigante de brújula (Macrotermes)", "Diagrama de arquitectura bioclimática moderna", "Papel vegetal translúcido de arquitecto con flechas de calor",
     "4 módulos de termodinámica y convección", "Chimenea central de escape térmico, conductos inferiores de aire fresco nocturno, humedad al 100% y cemento de saliva.",
     "¿Qué famoso edificio de oficinas en Zimbabue se construyó copiando exactamente el sistema de ventilación de los termiteros para no usar aire acondicionado?", "EL HORMIGUERO TEJEDOR DE HOJAS CON SEDA"),

    # 17: Mítico
    ("NAT-017", 17, "El Ave Fénix: Ciclo de Pirobiosis y Regeneración", "Animales Mitológicos, Fantásticos & Legendarios",
     "El Ave Fénix (Bennu)", "Manuscrito alquímico hermético egipcio/alejandrino", "Papiro vegetal egipcio con tintas minerales rojas y oro",
     "Ciclo circular en 4 cuartos evolutivos", "Fase solar de canela y mirra, combustión espontánea por hipertermia, huevo de ceniza condensada y eclosión del pichón renovado.",
     "¿Qué árboles y plantas de la naturaleza real necesitan arder completamente en incendios forestales para que sus semillas puedan brotar?", "EL PÁJARO TRUENO DE LA MITOLOGÍA NATIVA AMERICANA"),

    # 18: Leyendas Cine/Historia
    ("NAT-018", 18, "Moby Dick (Cachalote): Órgano de Espermaceti y Ecosonar", "Leyendas Animales del Cine y la Cultura Popular",
     "El Cachalote Albino (Physeter macrocephalus)", "Grabado ballenero en madera de barco del s. XIX", "Papel envejecido manchado con gotas de aceite marino",
     "Gran corte craneal con 4 detalles acústicos", "Cubeta con 3.000 litros de espermaceti para flotabilidad térmica, cañón acústico de 230 dB que aturde calamares y piel albina.",
     "¿Sabías que el chasquido del cachalote es el sonido más potente del reino animal y puede romper los tímpanos de un buzo bajo el agua?", "EL TIBURÓN BLANCO DE LA PELÍCULA TIBURÓN"),

    # 19: Fauna Salvaje
    ("NAT-019", 19, "El Búho Real: Plumas Aserradas y Vuelo Silencioso", "Fauna Salvaje Noble & Depredadores",
     "El Búho Real (Bubo bubo)", "Manuscrito gótico nocturno de ornitología", "Papel carbón oscuro y tinta plateada",
     "4 viñetas de óptica nocturna y acústica", "Borde de pluma en peine que rompe el aire, disco facial parabólico, oídos asimétricos y giro de cuello de 270 grados.",
     "¿Por qué los búhos pueden girar la cabeza 270 grados sin cortar el flujo de sangre a su cerebro?", "LA LECHUZA COMÚN EN EL CAMPANARIO"),

    # 20: Extintos
    ("NAT-020", 20, "El Dodo de Mauricio: Atrofia de la Quilla y Pérdida de Vuelo", "Criaturas Extinguidas & Dinosaurios",
     "El Dodo (Raphus cucullatus)", "Diario náutico de la Compañía Holandesa de 1600", "Papel de trapo con sellos de la marina colonial",
     "3 módulos de evolución insular aislada", "Atrofia de la quilla pectoral por ausencia de depredadores, pico gancho para frutas duras y patas caminadoras.",
     "¿Por qué los animales que evolucionan en islas sin depredadores pierden la capacidad de volar y el miedo a los humanos?", "EL ALCA GIGANTE DEL ATLÁNTICO NORTE"),

    # 21: Micro-Mundo
    ("NAT-021", 21, "El Ojo de la Libélula: 30.000 Omatidios a 300 FPS", "Micro-Mundo, Virus, Bacterias & Insectos",
     "La Libélula Emperador (Anax imperator)", "Diagrama óptico geométrico estilo Bauhaus 1925", "Papel técnico axonométrico de diseño industrial",
     "Macro y micro en 3 niveles de resolución visual", "Campo de visión esférico de 360°, estructura interna del omatidio hexagonal y procesamiento a 300 fotogramas por segundo.",
     "¿Por qué es casi imposible atrapar a una libélula con la mano en pleno vuelo?", "EL OJO DE LA MOSCA DE LA FRUTA"),

    # 22: Supercolonias
    ("NAT-022", 22, "La Telaraña Orbital: Ingeniería de 5 Tipos de Seda", "Arquitectura Animal & Supercolonias",
     "Araña de Jardín (Araneus diadematus)", "Blueprint de física de tracción de puentes colgantes", "Fondo azul blueprint con líneas y tensiones en Newtons",
     "5 módulos de física de materiales proteicos", "Hilos de anclaje de seda mayor resistente como el acero, espiral pegajosa de captura, buje central libre y absorción de impacto.",
     "¿Por qué la tela de araña es proporcionalmente cinco veces más resistente que el acero del mismo grosor?", "LA TELA DE EMBUDO DE LA TARÁNTULA"),

    # 23: Mítico
    ("NAT-023", 23, "El Grifo: Hibridación Biomecánica de Rapaz y León", "Animales Mitológicos, Fantásticos & Legendarios",
     "El Grifo Clásico (Gryphus)", "Códice heráldico del Sacro Imperio del siglo XV", "Pergamino iluminado con escudos nobiliarios en bordes",
     "4 módulos anatómicos comparativos", "Clavículas de águila fusionadas con lomo felino, pico triturador vs mandíbula corta, patas de rapaz delanteras y cuartos traseros de león.",
     "¿Qué fósiles de dinosaurios del desierto de Gobi inspiraron probablemente la leyenda del grifo en la Antigüedad?", "LA QUIMERA CON CABEZAS DE LEÓN Y CABRA"),

    # 24: Leyendas Cine/Historia
    ("NAT-024", 24, "Laika: Fisiología en Microgravedad y Cápsula Sputnik 2", "Leyendas Animales del Cine y la Cultura Popular",
     "Laika / La Perra Espacial (Canis lupus)", "Propaganda técnica aeroespacial soviética de 1957", "Papel de póster constructivista ruso rojo y negro",
     "4 módulos técnicos de soporte vital en órbita", "Sensores de pulso y respiración en el tórax, contenedor presurizado, regenerador de oxígeno de potasio y efecto de aceleración.",
     "¿Cómo midieron por primera vez en la historia que el corazón de un mamífero podía seguir latiendo en ingravidez orbital?", "LOS CHIMPANCÉS DEL PROGRAMA ESPACIAL MERCURY"),

    # 25: Fauna Salvaje
    ("NAT-025", 25, "El Cocodrilo del Nilo: Válvula Subacuática y 16.000 Newtons", "Fauna Salvaje Noble & Depredadores",
     "El Cocodrilo del Nilo (Crocodylus niloticus)", "Enciclopedia Científica Francesa de Diderot (1751)", "Papel vitela con márgenes grabados en cobre",
     "4 módulos de biomecánica de caza marina", "Mandíbula de 16.000 N, válvula palatal para sumergirse con boca abierta, osteodermos dérmicos y sensores de vibración en el hocico.",
     "¿Por qué un cocodrilo puede ahogar a su presa bajo el agua sin que a él le entre una sola gota de agua en los pulmones?", "EL CAIMÁN NEGRO DEL AMAZONAS"),

    # 26: Extintos
    ("NAT-026", 26, "El Pteranodon: Cresta Timón y Despegue Cuadrúpedo", "Criaturas Extinguidas & Dinosaurios",
     "Pteranodon longiceps", "Esquema de patente mecánica victoriana", "Papel cuadriculado azul grisáceo con diagramas mecánicos",
     "4 viñetas de aerodinámica de vuelo sin motor", "Cresta craneal como timón de rumbo, 4º dedo alargado que sostiene el ala membranosa, huesos neumáticos y salto con 4 patas.",
     "¿Sabías que los pterosaurios gigantes no saltaban con dos patas como las aves sino como una catapulta usando sus cuatro extremidades?", "EL QUETZALCOATLUS DE 11 METROS DE ENVERGADURA"),

    # 27: Micro-Mundo
    ("NAT-027", 27, "La Mantis Marina: Golpe de Bala y Burbuja de Cavitación", "Micro-Mundo, Virus, Bacterias & Insectos",
     "Mantis Marina / Estomatópodo (Odontodactylus scyllarus)", "Infografía balística de física naval de laboratorio", "Fondo azul abisal con ondas de choque acústicas",
     "4 viñetas de física de impacto extremo", "Resorte muela de titanio biológico, golpe a 80 km/h en 2 milisegundos, burbuja de cavitación a 4.000 °C y ojos de 16 fotorreceptores.",
     "¿Por qué el golpe de una mantis marina puede romper el cristal reforzado de un acuario?", "EL CAMARÓN PISTOLA Y SU DISPARO SÓNICO"),

    # 28: Supercolonias
    ("NAT-028", 28, "El Nido del Pájaro Tejedor: Nudos y Cestería de Pasto", "Arquitectura Animal & Supercolonias",
     "Pájaro Tejedor Africano (Ploceus cucullatus)", "Tratado botánico japonés de cestería y mimbre", "Papel Washi vegetal con fibras vistas y tonos ocres",
     "Paso a paso de 5 fases de confección textil", "Nudo inicial en horquilla de acacia, lazo corredizo, tejido de la cámara circular, túnel vertical de entrada y prueba de la hembra.",
     "¿Por qué si el nido construido por el macho no supera la inspección de resistencia de la hembra, el macho lo destruye y empieza de cero?", "EL NIDO DE ARCILLA DEL PÁJARO HORNERO"),

    # 29: Mítico
    ("NAT-029", 29, "La Hidra de Lerna: Mitosis y Regeneración por Corte", "Animales Mitológicos, Fantásticos & Legendarios",
     "La Hidra de Lerna (Lernaea hydra)", "Cerámica griega clásica de figuras negras sobre arcilla", "Mosaico de barro cocido antiguo con craquelado",
     "4 viñetas de mitosis celular descontrolada", "Blastema de células madre totipotentes, duplicación vascular tras decapitación, neurotoxina paralizante y cauterización por fuego.",
     "¿Qué diminuto animal de agua dulce real se llama Hydra y es prácticamente inmortal porque sus células se regeneran sin envejecer?", "LA QUIMERA Y SUS TRES CABEZAS"),

    # 30: Leyendas Cine/Historia
    ("NAT-030", 30, "Dolly (La Oveja): Transferencia Nuclear y Clonación", "Leyendas Animales del Cine y la Cultura Popular",
     "La Oveja Dolly (Ovis aries)", "Esquema científico de laboratorio de la revista Nature (1997)", "Papel blanco estucado con diagramas de citometría",
     "4 fases ilustradas del hito genético", "Enucleación de óvulo no fertilizado, inserción de núcleo de ubre mediante pulso eléctrico, desarrollo celular y acortamiento de telómeros.",
     "¿Por qué la oveja Dolly nació genéticamente con la edad biológica de la oveja adulta donante?", "EL PERRO SNOOPY PRIMER PERRO CLONADO"),

    # 31: Fauna Salvaje
    ("NAT-031", 31, "El Guepardo: Columna Elástica de Resorte y Tracción", "Fauna Salvaje Noble & Depredadores",
     "El Guepardo (Acinonyx jubatus)", "HUD Vectorial Sci-Fi y radiografía digital", "Fondo negro azabache con trazos vector verde neón",
     "Secuencia horizontal de 5 fases de zancada a 110 km/h", "Flexión de columna en arco, clavículas flotantes, garras fijas tipo clavos de atletismo, timón de cola y fatiga térmica.",
     "¿Por qué el guepardo debe abandonar la persecución a los 30 segundos si no caza a su presa?", "LA GACELA DE THOMSON Y SUS GIROS EN ZIGZAG"),

    # 32: Extintos
    ("NAT-032", 32, "El Megalodón: Cinta Transportadora de Dientes", "Criaturas Extinguidas & Dinosaurios",
     "Otodus megalodon", "Grabado barroco marino de monstruos abisales", "Papel sepia con manchas de salitre y marcas de agua",
     "4 viñetas de osteología marina gigante", "Hileras de dientes en cinta transportadora infinita, mandíbula de 2 metros de apertura, esqueleto cartilaginoso y tamaño relativo vs humano.",
     "¿Cuántos dientes llegaba a perder y reemplazar un megalodón a lo largo de toda su vida?", "EL MOSASAURIO DE LOS MARES DEL CRETÁCICO"),

    # 33: Micro-Mundo
    ("NAT-033", 33, "El Coronavirus: La Llave de Espícula y Bicapa Lipídica", "Micro-Mundo, Virus, Bacterias & Insectos",
     "Coronavirus / Virus Envuelto (SARS-CoV-2)", "Microscopía crioelectrónica de alta resolución en tonos pastel", "Placa de laboratorio con cuadrícula micrométrica",
     "4 viñetas de penetración y disolución química", "Proteína S encajando en receptor ACE2, bicapa lipídica que el jabón destruye, cápside de ARN y replicación ribosomal.",
     "¿Por qué lavarse las manos con agua y jabón corriente es el arma más demoledora contra un virus envuelto?", "EL VIRUS DE LA VIRUELA"),

    # 34: Supercolonias
    ("NAT-034", 34, "La Presa del Castor: Ingeniería Hidráulica Fluvial", "Arquitectura Animal & Supercolonias",
     "El Castor Europeo (Castor fiber)", "Plano topográfico del cuerpo de ingenieros militares del s. XIX", "Mapa topográfico con curvas de nivel y río",
     "Corte transversal y vista cenital con 4 detalles", "Base de rocas en fondo fluvial, troncos colocados a contracorriente, sellado con lodo y ramas, y madriguera con entrada subacuática.",
     "¿Cómo detecta un castor dónde hay una fuga de agua en su presa usando únicamente el sentido del oído?", "LA MADRIGUERA SUBTERRÁNEA DE LOS TEJONES"),

    # 35: Mítico
    ("NAT-035", 35, "El Kraken: Cefalópodo Abisal de 50 Metros", "Animales Mitológicos, Fantásticos & Legendarios",
     "El Kraken de las Fosas Nórdicas", "Carta marina de Olaus Magnus (Carta Marina s. XVI)", "Mapa pergamino de monstruos marinos de borde del mundo",
     "Gran escena atacando navío más 4 detalles de órganos", "Tentáculos con garfios giratorios de queratina, ojo descomunal adaptado a bioluminiscencia, pico de loro demoledor y tinta negra tóxica.",
     "¿Qué calamar real de los fondos marinos inspiró las leyendas del kraken con sus ojos del tamaño de platos de mesa?", "LA SERPIENTE MARINA DE MIDGARD"),

    # 36: Leyendas Cine/Historia
    ("NAT-036", 36, "Flipper (El Delfín): Melón Acústico y Sueño Hemisférico", "Leyendas Animales del Cine y la Cultura Popular",
     "El Delfín Mular (Tursiops truncatus)", "Ilustración marina años 60 estilo Jacques Cousteau", "Papel satinado azul acuamarina con diagramas técnicos",
     "4 módulos de biofísica marina", "Órgano melón de grasa acústica para ecolocalización 3D, espiráculo valvular, sueño unihemisférico alternado y propulsión laminar.",
     "¿Cómo pueden los delfines dormir plácidamente en el mar sin ahogarse ni perder el control de su respiración?", "LA ORCA LIBERADORA KEIKO (LIBERAD A WILLY)"),

    # 37: Fauna Salvaje
    ("NAT-037", 37, "El León Africano: Maseteros y Almohadillas Silenciosas", "Fauna Salvaje Noble & Depredadores",
     "El León Africano (Panthera leo)", "Barroco Flamenco claroscuro estilo Rembrandt", "Lienzo rústico al óleo y claroscuro profundo",
     "4 módulos de fisiología de cazador supremo", "Músculos maseteros de agarre asfixiante, visión nocturna tapetum lucidum, garras retráctiles y almohadillas silenciosas.",
     "¿Por qué las garras del león no se desafilan al caminar por el suelo pedregoso de la sabana?", "LA LEONA JEFA DE CAZA EN EQUIPO"),

    # 38: Extintos
    ("NAT-038", 38, "El Velociraptor: Plumaje Dinámico y Garra Falciforme", "Criaturas Extinguidas & Dinosaurios",
     "Velociraptor mongoliensis", "Paleoilustración moderna de alta fidelidad científica", "Papel mate de revista científica internacional",
     "4 módulos de anatomía fósil emplumada", "Garra falciforme retráctil en dedo 2 para aferrar presas, plumas de timón y freno, cola con tendones osificados y agilidad bípeda.",
     "¿Por qué los velociraptors reales eran del tamaño de un pavo grande cubierto de plumas y no los monstruos calvos de las películas?", "EL DEINONYCHUS EL PRIMER RAPTOR CON GARRA"),

    # 39: Micro-Mundo
    ("NAT-039", 39, "El Escarabajo Bombardero: Cámara Química a 100 °C", "Micro-Mundo, Virus, Bacterias & Insectos",
     "Escarabajo Bombardero (Brachinus crepitans)", "Tratado de alquimia y química experimental del s. XVII", "Papel tostado con símbolos alquímicos y matraces",
     "Corte del reactor químico abdominal en 4 fases", "Tanque A de hidroquinonas, tanque B de peróxido de hidrógeno, cámara de reacción con enzimas catalasas y tobera de disparo a 100 °C.",
     "¿Cómo evita el escarabajo bombardero explotar por dentro al mezclar dos compuestos químicos que hierven a temperatura volcánica?", "LA HORMIGA BALA Y SU NEUROTOXINA"),

    # 40: Supercolonias
    ("NAT-040", 40, "El Arrecife de Coral: Simbiosis con Algas Zooxantelas", "Arquitectura Animal & Supercolonias",
     "El Arrecife de Coral Hermatípico", "Litografía botánica marina Art Nouveau de Ernst Haeckel", "Cartulina marfil con orlas de conchas y pólipos",
     "Zoom en 3 escalas desde el pólipo al arrecife", "Pólipo individual con tentáculos urticantes, algas microscópicas fotosintéticas dentro de sus células y precipitación de roca caliza.",
     "¿Por qué los corales se vuelven blancos como esqueletos cuando la temperatura del agua sube apenas uno o dos grados?", "LA ANÉMONA Y EL PEZ PAYASO"),

    # 41: Mítico
    ("NAT-041", 41, "El Basilisco: Glándula Ocular de Neurotoxina", "Animales Mitológicos, Fantásticos & Legendarios",
     "El Basilisco / El Rey de los Reptiles", "Bestiario renacentista de Ulisse Aldrovandi (1600)", "Papel impreso con tipos móviles y xilografía en tinta negra",
     "4 módulos de fisiología de reptil venenoso", "Cresta cartilaginosa en corona, glándula lacrimal que emite aerosol letal volátil, escamas sulfuradas y punto débil: el canto del gallo.",
     "¿Qué reptil real de Centroamérica se llama basilisco y puede correr literalmente por encima del agua sin hundirse?", "LA SALAMANDRA DE FUEGO MITOLÓGICA"),

    # 42: Leyendas Cine/Historia
    ("NAT-042", 42, "Balto (El Husky): Intercambio de Calor en Patas a -50 °C", "Leyendas Animales del Cine y la Cultura Popular",
     "Balto / Perro de Trineo de Alaska", "Crónica de prensa de expedición polar ártica de 1925", "Papel prensa amarillento con tipos de imprenta de plomo",
     "4 viñetas de resistencia extrema en hielo", "Red circulatoria contracorriente en almohadillas para no congelarse, cola espesa filtro de ventiscas, metabolismo de glucógeno y guía por viento.",
     "¿Por qué los perros nórdicos de trineo pueden correr cientos de kilómetros sobre nieve virgen sin que sus patas sufran congelación?", "TOGO EL VERDADERO HÉROE DE NOME"),

    # 43: Fauna Salvaje
    ("NAT-043", 43, "La Ballena Azul: Filtrado de Barbas y Volumen Cardíaco", "Fauna Salvaje Noble & Depredadores",
     "La Ballena Azul (Balaenoptera musculus)", "Carta náutica hidrográfica del siglo XVIII", "Mapa pergamino con rosa de los vientos y compás",
     "Gran corte longitudinal con 3 ventanas de órganos gigantes", "Barbas de queratina que filtran 4 toneladas de krill al día, corazón del tamaño de un coche pequeño y lengua que pesa como un elefante.",
     "¿Por qué las arterias principales de una ballena azul son tan anchas que un niño pequeño podría nadar por dentro de ellas?", "EL CACHALOTE CAZADOR DE CALAMARES GIGANTES"),

    # 44: Extintos
    ("NAT-044", 44, "El Megaterio: El Tanque Blindado del Pleistoceno", "Criaturas Extinguidas & Dinosaurios",
     "Megatherium americanum (Perezoso Gigante)", "Litografía del Museo de Historia Natural de Londres s. XIX", "Cartón litográfico con filete dorado fino de colección",
     "4 módulos de osteología y defensa", "Fémures gigantescos para postura bípeda erguida, garras curvadas de 30 cm, huesecillos dérmicos bajo la piel como chaleco antibalas y digestivo masivo.",
     "¿Sabías que bajo la piel del perezoso gigante había miles de pequeños huesos incrustados que frenaban los ataques de los depredadores?", "EL GLIPTODONTE EL ARMADILLO DEL TAMAÑO DE UN COCHE"),

    # 45: Micro-Mundo
    ("NAT-045", 45, "Motor de la Bacteria E. coli: 100.000 RPM de Flagelo", "Micro-Mundo, Virus, Bacterias & Insectos",
     "Escherichia coli (Motor flagelar bacteriano)", "Patente de ingeniería mecánica y motor eléctrico", "Plano técnico industrial con engranajes y estator",
     "4 módulos de física y flujo de protones", "Anillo estator de proteínas, rotor magnético que gira a 100.000 RPM impulsado por protones, codo universal flexible y hélice propulsora.",
     "¿Cómo es posible que una bacteria tenga un motor giratorio idéntico a un motor eléctrico con rotor y estator creado por la evolución?", "EL FLAGELO DEL ESPERMATOZOIDE"),

    # 46: Supercolonias
    ("NAT-046", 46, "El Nido del Hornero: Tabique Espiral Anti-Viento", "Arquitectura Animal & Supercolonias",
     "El Hornero Común (Furnarius rufus)", "Guía ornitológica campera del s. XIX ilustrada a mano", "Papel de paja artesanal con tonos terracota",
     "Corte horizontal del nido de barro con 3 zonas", "Mezcla de arcilla, paja y estiércol horneada al sol, pared divisoria interior curva que bloquea ráfagas y cámara de huevos segura.",
     "¿Por qué la entrada al nido del hornero tiene una pared curva en espiral que impide que entren serpientes y viento frío?", "EL NIDO DE RAMAS DE LA CIGÜEÑA"),

    # 47: Mítico
    ("NAT-047", 47, "El Pegaso: Doble Cintura Escapular para Vuelo", "Animales Mitológicos, Fantásticos & Legendarios",
     "Pegaso (El Caballo Alado)", "Estudio anatómico de Bellas Artes de París s. XIX", "Papel carboncillo sepia sobre fondo marfil con tiza blanca",
     "Disección esquelética y biomecánica de 4 puntos", "Segunda cintura escapular dorsal anclada en vértebras, quilla muscular en el pecho equino, reducción ósea neumática y balance de alas.",
     "¿Qué problema anatómico real tendrían los caballos alados para batir las alas sin chocar con sus patas delanteras?", "EL QUETZAL AVE SAGRADA DE LOS MAYAS"),

    # 48: Leyendas Cine/Historia
    ("NAT-048", 48, "King Kong: Ley Cuadrático-Cúbica del Gigantismo", "Leyendas Animales del Cine y la Cultura Popular",
     "King Kong / Megaprimus gorilla", "Boceto de producción de Hollywood de 1933", "Papel borrador de estudio manchado con carboncillo y grafito",
     "4 módulos de física y biomecánica de escala", "Por qué al multiplicar el tamaño x10 el peso crece x1000, necesidad de huesos 10 veces más anchos, corazón hipertrofiado y fuerza de agarre.",
     "¿Por qué un gorila real de 15 metros de altura no podría dar ni tres pasos sin que sus propios huesos se rompieran por su peso?", "GODZILLA Y LA BIOLOGÍA DE LOS TITANES"),

    # 49: Fauna Salvaje
    ("NAT-049", 49, "El Camaleón Pantera: Lengua Catapulta y Ojos 360°", "Fauna Salvaje Noble & Depredadores",
     "El Camaleón Pantera (Furcifer pardalis)", "Litografía botánica Art Nouveau de Alphonse Mucha", "Cartulina marfil con orlas florales y vegetales",
     "4 viñetas de órganos prensiles y balísticos", "Resorte acelerador de la lengua en 20 milisegundos, ventosa lingual pegajosa, conos oculares independientes y dedos en pinza zigodáctila.",
     "¿Sabías que la lengua del camaleón acelera más rápido que un coche deportivo de Fórmula 1 para cazar insectos?", "EL GECKO Y SUS PATAS ADHESIVAS VAN DER WAALS"),

    # 50: Extintos
    ("NAT-050", 50, "El Celacanto: Aletas Lobuladas Precursoras de Patas", "Criaturas Extinguidas & Dinosaurios",
     "El Celacanto (Latimeria chalumnae)", "Acuarela ictiológica victoriana coloreada a mano", "Papel verjurado crema con aguadas marinas",
     "4 viñetas de anatomía de fósil viviente", "Aletas lobuladas articuladas con huesos precursores de brazos, órgano rostral electrorreceptor, articulación intracraneal y vejiga de grasa.",
     "¿Cómo sobrevivió el celacanto durante 400 millones de años en cuevas volcánicas marinas mientras todos los dinosaurios se extinguían?", "EL TIKTAALIK EL PEZ QUE SALIÓ A LA TIERRA"),

    # 51: Micro-Mundo
    ("NAT-051", 51, "La Pulga: Resina Elástica de Resilina y Salto de 100 G", "Micro-Mundo, Virus, Bacterias & Insectos",
     "La Pulga Común (Pulex irritans)", "Micrographia de Robert Hooke (1665)", "Grabado en cobre de página desplegable de gran formato",
     "4 módulos de biomecánica de salto por resorte", "Almohadilla de resilina que almacena y devuelve el 97% de energía, gatillo esquelético pleural, aceleración de 100 G y garras tarsales.",
     "¿Por qué si los humanos saltáramos con la potencia relativa de una pulga podríamos superar la altura de la Torre Eiffel de un solo brinco?", "EL SALTAMONTES Y SU MECANISMO DE RESORTE"),

    # 52: Supercolonias
    ("NAT-052", 52, "La Galería del Topo: Trampa de Lombrices y Despensa", "Arquitectura Animal & Supercolonias",
     "El Topo Europeo (Talpa europaea)", "Corte geológico inglés ilustrado para escolares victorianos", "Papel verjurado y acuarela de tierra fértil oscura",
     "4 viñetas de arquitectura subterránea", "Túneles de caza donde caen lombrices, cámara despensa con presas inmovilizadas de un mordisco en la cabeza, manos pala con hueso extra y pelo reversible.",
     "¿Cómo consiguen los topos almacenar cientos de lombrices vivas en una despensa sin que se mueran ni se escapen?", "EL TEJÓN Y SU COMPLEJA TEJONERA"),

    # 53: Mítico
    ("NAT-053", 53, "El Leviatán: Coraza Escamosa de Fondos Abisales", "Animales Mitológicos, Fantásticos & Legendarios",
     "El Leviatán de las Profundidades", "Grabado bíblico barroco de Gustave Doré", "Grabado en acero de alto contraste blanco y negro",
     "4 módulos de defensa y fisiología abisal", "Escamas trabadas sin resquicio donde no entra el aire, respiraderos termales de vapor, ojos con tapetum adaptados a oscuridad total y bioluminiscencia.",
     "¿Qué animales reales de las fosas abisales tienen placas y bioluminiscencia parecidas a las del monstruo Leviatán?", "EL PEZ DIABLO NEGRO ABISAL CON LINTERNA"),

    # 54: Leyendas Cine/Historia
    ("NAT-054", 54, "Koko (La Gorila): Lengua de Signos y Empatía Humana", "Leyendas Animales del Cine y la Cultura Popular",
     "Koko / La Gorila de las Tierras Bajas", "Cuaderno etológico de investigación de campo y psicología", "Libreta de notas de campo con bocetos a lápiz",
     "4 módulos de cognición y lenguaje de primates", "Flexibilidad de dedos para 1.000 signos gestuales, modulación de gruñidos, empatía inter-especie cuidando a su gatito All Ball y área cerebral de Broca.",
     "¿Cómo demostró la gorila Koko que los primates no humanos tienen la capacidad de inventar palabras nuevas combinando signos?", "EL CHIMPANCÉ WASHIE APRENDIENDO SIGNOS"),

    # 55: Fauna Salvaje
    ("NAT-055", 55, "El Carnero Cimarrón: Amortiguadores Neumáticos de 60 G", "Fauna Salvaje Noble & Depredadores",
     "El Carnero Cimarrón (Ovis canadensis)", "Litografía victoriana de historia natural clásica", "Pergamino satinado con sellos de archivo biológico",
     "Tríptico de absorción de impactos alpinos", "Cráneo alveolar con cámaras de aire que amortiguan impactos de 60 G, espiral de cuernos disipadora de energía y tendones del cuello de halterofilia.",
     "¿Cómo es posible que dos carneros choquen sus cabezas a 40 km/h sin sufrir jamás una conmoción cerebral?", "LA CABRA MONTÉS IBÉRICA EN LOS RISCOS"),

    # 56: Extintos
    ("NAT-056", 56, "El Trilobites: El Primer Ojo con Lentes de Calcita", "Criaturas Extinguidas & Dinosaurios",
     "Trilobites (Asaphus kowalewskii)", "Placa geológica grabada en pizarra de piedra mineral", "Pizarra negra con trazos de tiza blanca y talco",
     "Macro-zoom en 3 niveles de fósil marino", "Ojo compuesto con lentes de cristal de calcita pura sin aberración óptica, exoesqueleto segmentado enrollable en bola y apéndices dobles pata-branquia.",
     "¿Sabías que los trilobites fueron los primeros animales de la historia de la Tierra en desarrollar ojos complejos hace más de 500 millones de años?", "EL AMMONITE Y SU CONCHA EN ESPIRAL"),

    # 57: Micro-Mundo
    ("NAT-057", 57, "La Ameba: Locomoción por Flujo Citoplasmático", "Micro-Mundo, Virus, Bacterias & Insectos",
     "La Ameba Proteo (Amoeba proteus)", "Acuarela biológica translúcida estilo Ernst Haeckel", "Fondo acuático con tintes acuosos transparentes",
     "4 fases de movimiento celular y fagocitosis", "Endoplasma líquido que fluye hacia el pseudópodo, ectoplasma gelatinoso que sostiene la pared, fagocitosis engullendo bacterias y vacuola pulsátil.",
     "¿Cómo puede una sola célula sin cerebro ni patas 'caminar' y cazar presas en una gota de agua?", "EL PARAMECIO Y SUS CILIOS PROPULSORES"),

    # 58: Supercolonias
    ("NAT-058", 58, "El Nido del Pez Betta: Cemento de Saliva y Cuidado", "Arquitectura Animal & Supercolonias",
     "El Pez Betta / Luchador de Siam (Betta splendens)", "Pintura clásica china a la tinta sumi-e y aguada sobre seda", "Seda pura beige con trazos de tinta fluida y bermellón",
     "4 fases de arquitectura y cuidado parental", "Secreción de saliva mucosa que estabiliza burbujas flotantes, recogida de huevos del fondo por el macho, custodia del nido y oxigenación continua.",
     "¿Por qué en los peces Betta es el padre y no la madre quien construye el nido y cuida a los alevines día y noche?", "EL PEZ GLOBO Y SUS CÍRCULOS GEOMÉTRICOS EN LA ARENA"),

    # 59: Mítico
    ("NAT-059", 59, "La Sirena: Sistema Dual Branquias y Pulmones", "Animales Mitológicos, Fantásticos & Legendarios",
     "La Sirena / Homínido Marino (Sirenia mythologica)", "Cuaderno de bitácora y autopsia naval de la Royal Navy", "Papel de bitácora manchado con sello oficial naval inglés",
     "4 viñetas de fisiología marina híbrida", "Sistema dual de pulmones y hendiduras branquiales faríngeas, pelvis vestigial de mamífero, capa de grasa subcutánea contra hipotermia y manos palmeadas.",
     "¿Qué mamífero marino herbívoro y pacífico inspiró a los marineros antiguos los cantos de las sirenas?", "EL MONSTRUO DEL LAGO NESS"),

    # 60: Leyendas Cine/Historia
    ("NAT-060", 60, "Cher Ami (Paloma Mensajera): Magnetorrecepción", "Leyendas Animales del Cine y la Cultura Popular",
     "Cher Ami / Paloma Mensajera de Guerra (Columba livia)", "Despacho de Estado Mayor militar de 1918 con medalla", "Papel oficial de cuartel con sello de cera lacrada y condecoración",
     "4 módulos de orientación y vuelo heroico", "Cristales de magnetita en el pico que detectan el campo magnético terrestre, criptocromos oculares que ven líneas magnéticas, memoria olfativa y cápsula de aluminio en la pata.",
     "¿Cómo logró la paloma Cher Ami salvar a 194 soldados del Batallón Perdido en la Primera Guerra Mundial volando herida durante 40 kilómetros?", "LOS HALCONES CORREO DE LA EDAD MEDIA")
]

for item in REST_ITEMS_DATA:
    code, num, title, cat, subj, style, paper, layout, details, tip, ch = item
    NAT_ITEMS.append({
        "id": code,
        "num": num,
        "title": title,
        "category": cat,
        "subject": subj,
        "style_art": style,
        "paper": paper,
        "layout": layout,
        "details_es": details,
        "concept": f"Infografía científica y artística para la sesión {num:02d}. Aprende a pedir a Gemini que redacte el prompt maestro y cree una obra de arte visual.",
        "short_prompt": (
            f"Actúa como un ilustrador científico y experto en diseño editorial. "
            f"Quiero una lámina infográfica sobre {subj.upper()} en estilo {style} "
            f"sobre {paper}. Organiza la composición en {layout} que explique: {details}. "
            f"Redáctame el prompt maestro completo en inglés, con máxima resolución y sin textos borrosos, "
            f"para generar esta infografía con IA."
        ),
        "master_prompt_en": (
            f"A magnificent scientific and historical infographic illustration of {subj}. "
            f"Rendered in {style} on authentic {paper}. "
            f"Composition: Beautifully centered main subject portrait surrounded by an informative {layout}. "
            f"Depicting with extreme biological and physical accuracy: {details}. "
            f"Ultra-high resolution 8k, crisp technical linework, vintage editorial presentation, zero watermarks, perfectly balanced aesthetic."
        ),
        "scientific_tip": tip,
        "creative_challenge": f"Pide ahora a Gemini: '{ch}'."
    })

def get_nat_items():
    return NAT_ITEMS

if __name__ == "__main__":
    items = get_nat_items()
    print(f"✅ Cargados {len(items)} ítems maestros de [NAT-001 a NAT-060].")
    print(f"Ejemplo NAT-001: {items[0]['title']}")
    print(f"Ejemplo NAT-060: {items[59]['title']}")

