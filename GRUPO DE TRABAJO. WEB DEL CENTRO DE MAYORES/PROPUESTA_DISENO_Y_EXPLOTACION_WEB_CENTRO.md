# 🏛️ Documento Maestro de Diseño, Arquitectura y Dinámica de Aula
## Proyecto de Innovación Sénior con IA: Web del Centro Municipal de Mayores

**Ubicación del Proyecto:**  
`/CLASES DE TECNOLOGÍA/CURSO-IA/GRUPO DE TRABAJO. WEB DEL CENTRO DE MAYORES/`

---

## 🗺️ 1. Mapa de Recursos del Proyecto

| Archivo | Tipo | Función Principal en el Curso |
| :--- | :--- | :--- |
| **`CUESTIONARIO_REQUISITOS_FRONTEND.html`** | Herramienta Día 1 | Cuestionario interactivo por pestañas (Grupos 1, 2 y 3) + Pantalla del Profesor con Maqueta en Vivo y Súper-Prompt. |
| **`CUESTIONARIO_REQUISITOS_BACKEND.html`** | Herramienta Día 1 | Cuestionario para diseñar los formularios de alta, el botón de IA, el OCR de menús y las estadísticas. |
| **`PRESENTACION_ARQUITECTURA_WEB_CENTRO.html`** | Explicación Día 1 | Presentación animada para el aula: La metáfora de la Panadería (Trastienda, Almacén, Escaparate y Smart TV). |
| **`WEB_PUBLICA_CENTRO_MAYORES.html`** | Producto Día 2 (Frontend) | Web pública accesible para mayores: 5 baldosas gigantes, fotos HD, voz en alta voz, navegación limpia y enlace a Backend. |
| **`GESTOR_CONTENIDOS_BACKEND.html`** | Herramienta Día 2 (Backend) | Gestor de contenidos para los alumnos con IA de Gemini, vista previa en vivo y botón de **Aula Limpia (Reset)**. |
| **`PANTALLA_TV_VESTIBULO.html`** | Canal Digital | Cartelera automática para la televisión de la entrada (rotación cada 12 segundos y reloj digital). |
| **`INFORME_VIABILIDAD_Y_RIESGOS_WEB_CENTRO_MAYORES.pdf`** | Documento Jurídico | Informe oficial de 3 páginas para la Coordinadora (Derecho de imagen, LOPD, alérgenos, ENS y TI municipal). |
| **`PROPUESTA_DISENO_Y_EXPLOTACION_WEB_CENTRO.md`** | Referencia Técnica | Este documento maestro de especificaciones y guía de mantenimiento futuro. |

---

## 👥 2. Dinámica Pedagógica del Taller en 2 Jornadas

### Jornada 1: Toma de Requisitos y Co-Diseño Visual
* **Organización:** 12 alumnos sénior distribuidos en 3 grupos naturales de trabajo (4 alumnos por mesa).
  * **Grupo 1:** Módulo de Excursiones, Viajes y Secretaría.
  * **Grupo 2:** Módulo de Clases, Talleres Formativos y Rincón de Ayuda.
  * **Grupo 3:** Módulo de Cafetería (Menú del Día) y Smart TV del Vestíbulo.
* **El papel del alumno en su PC:**
  * Abre `CUESTIONARIO_REQUISITOS_FRONTEND.html`.
  * Debate con sus compañeros de mesa y marca las casillas deseadas en su pantalla.
  * Si se les ocurre un dato nuevo (ej. calzado recomendado, paradas de café, alérgenos), lo escriben en el campo libre de su sección.
* **El papel del profesor (Tablero Maestro en iPad + Proyector):**
  * El profesor está proyectando la pestaña **«🧩 PANTALLA PROFESOR»**.
  * Cada grupo expone de viva voz sus decisiones (2 minutos por grupo).
  * El profesor marca los checks correspondientes en el iPad con el dedo (cero teclado virtual delante de los alumnos).
  * Si el grupo propone un campo extra o una baldosa nueva (ej. Podología, Torneo de Mus), el profesor lo teclea en 3 segundos en la barra superior y pulsa `➕ Añadir`.
  * Al pulsar **`🔄 Actualizar Maqueta`**, los alumnos ven en el proyector su web nacer en tiempo real: baldosas interactivas, navegación a Nivel 2 y lectura por voz en español.
  * Al terminar la clase, el profesor abre el desplegable inferior `🤖 Súper-Prompt para Gemini` y se copia el resumen consolidado.

### Entre Clases: Ensamblado en Casa con Antigravity
* En casa, el profesor abre Antigravity en el Mac con el Súper-Prompt generado.
* Antigravity ensambla la versión definitiva del Frontend y Backend incorporando todos los campos extras y baldosas votadas en el aula, dejando el código sincronizado y subido a GitHub Pages.

### Jornada 2: Estreno y Taller de Pruebas Cruzadas (Backend ➔ Frontend)
* **Paso 0 (Modo Aula Limpia):** El profesor abre `GESTOR_CONTENIDOS_BACKEND.html` y pulsa el botón rojo **`🗑️ Vaciar Datos (Aula Limpia)`**, dejando la base de datos a cero.
* **Práctica de los alumnos en clase:**
  * **Grupo 1:** Da de alta en el Backend el viaje a Toledo con fotos, plazas y datos del calzado. Pulsa `🪄 Pulir con IA` y luego `Guardar Noticia`.
  * **Grupo 2:** Da de alta el taller de Sevillanas y una guía de Cita Médica.
  * **Grupo 3:** Sube la foto del menú del catering y genera el menú de la semana con IA.
* **Comprobación en vivo:** Cada grupo pulsa el botón superior `🌐 Ver Web Pública ↗` y comprueba en el Frontend cómo su noticia ya está publicada con su foto, su ficha detallada y su botón de audio funcional.

---

## 🎨 3. Especificaciones del Frontend (`WEB_PUBLICA_CENTRO_MAYORES.html`)

### 3.1. Ergonomía Sénior (+65)
1. **Fondo luminoso y de alto contraste:** Fondo general `#f1f5f9`, cabecera institucional blanca `#ffffff` con escudo `🏛️` y texto oscuro `#0f172a`.
2. **Cero menús desplegables / hamburguesa:** Toda la navegación se basa en **grandes baldosas táctiles** de ancho completo con fotos reales de Unsplash y flechas direccionales `➔`.
3. **Navegación multinivel limpia:**
   * **Nivel 1 (Portada):** Las baldosas principales del centro.
   * **Nivel 2 (Sección):** Listado de fichas temáticas con botón gigante arriba: **`⬅️ VOLVER AL INICIO DE LA WEB`**.
   * **Nivel 3 (Ficha de Detalle):** Fotografía panorámica de 240px, badges de colores vivos, píldoras de datos (fechas, precios, plazas libres) y botón de audio.
4. **Accesibilidad Universal y Lectura por Voz:**
   * Botón superior `🔊 Escuchar en Voz Alta` que lee de forma inteligente la pantalla activa (no una frase fija).
   * Botones individuales `🔊 Escuchar` en cada baldosa de portada para personas con baja visión.
   * Motor nativo `SpeechSynthesisUtterance` calibrado a `rate: 0.90` (habla pausada) en `es-ES`, con salvaguarda en memoria `window.currentUtterance` para evitar que Safari/iOS corte la voz a mitad de frase.
   * Selector de tamaño de tipografía sénior (`20px`, `24px`, `28px`).

---

## ⚙️ 4. Especificaciones del Backend (`GESTOR_CONTENIDOS_BACKEND.html`)

### 4.1. Funcionalidades para los Alumnos
1. **Formulario guiado por áreas:** Selector temático (Excursiones, Talleres, Cafetería, Secretaría, Guías).
2. **Botón Mágico `🪄 Pulir y enriquecer con IA (Gemini)`:** Transforma notas telegráficas escritas por los alumnos en redacciones cordiales, atractivas y sin faltas ortográficas.
3. **Vista previa en tiempo real (lado derecho):** Muestra al instante la tarjeta exacta que verá el socio en el móvil antes de publicar.
4. **Bandeja de Aprobación del Administrador:** Permite guardar como borrador o aprobar para publicación inmediata con un solo toque.

### 4.2. Conexión de Datos y Modo Aula Limpia
* **Base de datos compartida:** Utiliza la clave `localStorage['centro_mayores_noticias_v1']`. Toda noticia guardada en el Backend se refleja de inmediato en el Frontend sin requerir servidor externo.
* **Botón Aula Limpia:**
  ```javascript
  function resetAllDataClean() {
    if (confirm("⚠️ ¿Estás seguro de que deseas VACIAR todos los datos de prueba?")) {
      localStorage.removeItem('centro_mayores_noticias_v1');
      alert("✅ Base de datos vaciada. El aula comienza desde cero.");
      location.reload();
    }
  }
  ```

---

## 📺 5. Canal Smart TV del Vestíbulo (`PANTALLA_TV_VESTIBULO.html`)
* Modo de emisión continua a pantalla completa (1920x1080 px).
* Rotación automática cada 12 segundos entre:
  1. Menú del Día de Cafetería (2 primeros y 2 segundos).
  2. Próxima Excursión Oficial (Toledo).
  3. Talleres Semanales y Avisos Urgentes.
* Reloj digital visible permanentemente y saludo institucional.

---

## ⚖️ 6. Resumen de Viabilidad Legal y Riesgos Institucionales
*(Detallado en `INFORME_VIABILIDAD_Y_RIESGOS_WEB_CENTRO_MAYORES.pdf` para la Coordinadora)*

1. **Derecho a la Propia Imagen (LO 1/1982 y Art. 18 CE):** Prohibido publicar fotos de socios en talleres o viajes sin autorización firmada previa por escrito.
2. **Protección de Datos y LOPD/AEPD:** No almacenar listas públicas de socios apuntados a excursiones ni datos de salud (medicación, movilidad).
3. **Responsabilidad Civil del Centro:** Si la web anuncia una excursión o menú y se cancela o modifica, el centro asume responsabilidad; requiere cláusula obligatoria de descargo (*disclaimer*).
4. **Información Alimentaria (Reglamento UE 1169/2011):** Obligación de indicar los 14 alérgenos oficiales si se publican menús de catering.
5. **Esquema Nacional de Seguridad (RD 311/2022) y TI Municipal:** Una web con panel de administración abierta no puede alojarse en servidores municipales oficiales sin auditoría del CCN-CERT y autenticación segura (Cl@ve / Doble Factor).

---

## 🛠️ 7. Guía de Modificación Futura para Antigravity

Cuando el usuario pida añadir una nueva sección, baldosa o campo:
1. **En `CUESTIONARIO_REQUISITOS_FRONTEND.html`:**
   * Añadir el checkbox o campo libre en el grupo correspondiente.
   * En `renderLiveMockup()`, leer el nuevo campo y renderizarlo dentro de `frameTilesGrid` o en la vista `frameDetailCard`.
   * Incluirlo en el texto de `masterPromptBox`.
2. **En `WEB_PUBLICA_CENTRO_MAYORES.html`:**
   * Si es una baldosa nueva, añadirla al grid `grid-giant-buttons` y crear su sección `view-[nombre]`.
   * Mantener el esquema de colores de alto contraste y el botón de audio con `speakText()`.
3. **En `GESTOR_CONTENIDOS_BACKEND.html`:**
   * Añadir la categoría en el desplegable de redacción de noticias para que los alumnos puedan seleccionarla y guardarla en `localStorage`.
