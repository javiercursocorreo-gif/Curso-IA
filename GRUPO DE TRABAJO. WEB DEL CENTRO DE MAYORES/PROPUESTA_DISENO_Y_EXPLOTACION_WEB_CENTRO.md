# 🏛️ Proyecto de Investigación Sénior con IA: Web Oficial del Centro de Mayores
## Memoria de Propuesta Final, Diseño de Interfaz y Plan de Explotación en Producción

**Ubicación de esta carpeta:**  
`CLASES DE TECNOLOGÍA / CURSO-IA / GRUPO DE TRABAJO. WEB DEL CENTRO DE MAYORES/`

**Archivos y Maquetas incluidas en esta carpeta:**
* 🌐 **Web Pública para Mayores (Frontend):** [`WEB_PUBLICA_CENTRO_MAYORES.html`](file:///Users/externo/Library/Mobile%20Documents/com~apple~CloudDocs/PERSONAL/CLASES%20DE%20TECNOLOGÍA/CURSO-IA/GRUPO%20DE%20TRABAJO.%20WEB%20DEL%20CENTRO%20DE%20MAYORES/WEB_PUBLICA_CENTRO_MAYORES.html)
* ✍️ **Gestor de Contenidos para Alumnos (Backend):** [`GESTOR_CONTENIDOS_BACKEND.html`](file:///Users/externo/Library/Mobile%20Documents/com~apple~CloudDocs/PERSONAL/CLASES%20DE%20TECNOLOGÍA/CURSO-IA/GRUPO%20DE%20TRABAJO.%20WEB%20DEL%20CENTRO%20DE%20MAYORES/GESTOR_CONTENIDOS_BACKEND.html)
* 📑 **Versión Maquetada para Imprimir / PDF:** [`PROPUESTA_DISENO_Y_EXPLOTACION_WEB_CENTRO.html`](file:///Users/externo/Library/Mobile%20Documents/com~apple~CloudDocs/PERSONAL/CLASES%20DE%20TECNOLOGÍA/CURSO-IA/GRUPO%20DE%20TRABAJO.%20WEB%20DEL%20CENTRO%20DE%20MAYORES/PROPUESTA_DISENO_Y_EXPLOTACION_WEB_CENTRO.html)

---

## 🎯 1. Resumen Ejecutivo y Misión del Proyecto

### 1.1. Puesta en Práctica Inmediata con los Alumnos
No hace falta esperar al final del curso: **el gestor de contenidos y la web se ponen en práctica de forma inmediata desde las próximas clases con los alumnos**.

Los alumnos comienzan a utilizar la herramienta desde ya como taller práctico central del curso:
* **Práctica viva con Gemini:** redactan, sintetizan y adaptan avisos reales con un tono cálido y cercano.
* **Trabajo en equipo por comités temáticos:** excursiones, clases, menús, normas y guías de salud.
* **Impacto motivacional directo:** comprueban al instante cómo sus textos e imágenes se publican en la web y en la pantalla del centro sin esperar meses.

### 1.2. Problemas Reales que Resuelve de Forma Inmediata
1. **El corcho de anuncios físico:** Papeles amontonados, letras pequeñas, desactualizados o que los socios solo pueden leer si se desplazan al centro.
2. **La televisión en bucle del vestíbulo:** Pasa diapositivas apresuradas que nadie puede pausar ni consultar desde su domicilio.
3. **La soledad digital de los mayores:** Falta de guías redactadas en un lenguaje verdaderamente comprensible sobre trámites cotidianos, citas médicas y prevención de estafas.

---

## 🎨 2. Arquitectura de Diseño: Dos Caras de la Misma Moneda

```
┌────────────────────────────────────────────────────────────────────────┐
│                   WEB OFICIAL DEL CENTRO DE MAYORES                   │
├───────────────────────────────────┬────────────────────────────────────┤
│     FRONTEND (Público y Socios)   │     BACKEND (Gestor de Alumnos)    │
├───────────────────────────────────┼────────────────────────────────────┤
│ • Botones gigantes (Cero menús)   │ • Reparto por 5 comités de trabajo │
│ • Navegación por niveles fijos    │ • Asistente Gemini contextual      │
│ • Lectura en voz alta             │ • Vista previa en tiempo real      │
│ • Modo Pantalla TV (vestíbulo)    │ • Bandeja de validación del Administrador    │
└───────────────────────────────────┴────────────────────────────────────┘
```

### 2.1. El Frontend (Web Pública Accesible)
Diseñado con los criterios más exigentes de accesibilidad cognitiva y visual para la tercera edad:
* **Diseño 100% Adaptable al Móvil (Responsive Senior):** Como la inmensa mayoría de los mayores consulta Internet exclusivamente desde su teléfono móvil, la interfaz se adapta de forma fluida a pantallas verticales: botones de ancho completo, objetivos táctiles de gran tamaño (mínimo 48 px), tipografía sin deformación y cero desplazamiento horizontal.
* **Cero menús desplegables ni hamburguesas:** Se eliminan los menús pequeños que exigen precisión motriz o generan desorientación.
* **Nivel 1 (Portal):** 5 grandes bloques temáticos a toda pantalla con iconos y colores contrastados:
  * 🚌 **Excursiones y Viajes**
  * 🎨 **Clases y Talleres**
  * ☕ **Cafetería y Menú del Día**
  * 📜 **Normas y Secretaría**
  * 💡 **Guías Ciudadanas con IA**
* **Nivel 2 (Sublistado):** Nuevamente tarjetas horizontales grandes con el resumen de las noticias del área.
* **Nivel 3 (Ficha Detalle):** Tipografía grande y escalable (`A+ / A-`), recuadros con datos clave (fechas, precio, plazas) y herramientas de apoyo:
  * 🔊 **«Escuchar en Voz Alta»** (narración automática mediante voz nativa del dispositivo).
  * 🖨️ **«Imprimir Folio»** (para quien desee guardarlo en papel).
  * ⬅️ **Botón «VOLVER ATRÁS» Gigante** visible permanentemente en la parte superior e inferior.
* **Web Pública 100% Limpia (Sin Botones Innecesarios de TV):** Para no confundir a los mayores, la web pública no contiene botones técnicos de televisión. Se centra exclusivamente en su lectura personal (con control de letra `A+ / A-`). La emisión de la televisión se controla y lanza de forma independiente desde el Backend mediante el canal dedicado [`PANTALLA_TV_VESTIBULO.html`](file:///Users/externo/Library/Mobile%20Documents/com~apple~CloudDocs/PERSONAL/CLASES%20DE%20TECNOLOGÍA/CURSO-IA/GRUPO%20DE%20TRABAJO.%20WEB%20DEL%20CENTRO%20DE%20MAYORES/PANTALLA_TV_VESTIBULO.html).

---

### 2.2. El Backend (Gestor de Contenidos - CMS)
Diseñado para que los alumnos mayores trabajen de forma autónoma sin miedo a cometer errores técnicos:
* **Reparto de Trabajo por Áreas:** El alumno solo tiene que elegir su equipo de trabajo arriba (`[🚌 Excursiones]`, `[🎨 Talleres]`, `[☕ Menú]`, `[📜 Normas]`, `[💡 Guías]`).
* **Campos Guiados:** Título claro, fecha, precio/plazas y descripción.
* **Asistente Gemini Contextual (Tono Cercano y Humano):**
  Al pulsar `🪄 Pulir y enriquecer con IA`, la inteligencia artificial transforma las notas breves del alumno en un texto cálido, entusiasta y perfectamente redactado (evitando formalismos fríos como *"Nos complace anunciarles..."* y usando expresiones naturales como *"¡Nos vamos de excursión! Pásate a hablar con el Administrador para reservar tu sitio..."*).
* **Vista Previa en Vivo:** Según escribe el alumno, a la derecha se renderiza la tarjeta exacta tal y como saldrá en la web pública.
* **Bandeja del Administrador:** Permite guardar como borrador para que la coordinadora del centro solo tenga que hacer clic en `✓ Aprobar` antes de que el contenido sea visible.

---

## ⚙️ 3. Modelo Operativo y Simbiosis Humano-IA

El debate estratégico clave quedó zanjado con un principio operativo claro:  
**La IA genera el código y el contenedor técnico en minutos; pero el contenido vivo lo mantienen las personas.**

| Rol | Agente | Responsabilidad Principal |
| :--- | :--- | :--- |
| **Arquitectura Técnica** | Profesor + IA (Antigravity) | Diseño del sistema, automatización y despliegue inicial. Cero soporte 24/7. |
| **Dirección Institucional** | Administrador y Director del Centro | Deciden qué eventos se publican y aprueban con un solo clic los borradores. |
| **Gabinete de Redacción** | Alumnos del Grupo de Investigación | Investigan, redactan con Gemini, ilustran y cargan las noticias desde casa. |
| **Destinatarios** | Socios del Centro y Familias | Consultan la web desde el móvil o en la Smart TV del vestíbulo. |

**El «Efecto Alivio para el Administrador»:** El Administrador no escribe ni maqueta. Solo envía una nota de voz o un apunte en un papel: *"Chicos, excursión a Chinchón el 20 de junio, 25€ con comida"*. El equipo de alumnos coge ese dato, lo pasa por Gemini, genera el itinerario completo, añade la imagen y se lo deja listo para validar.

---

## 🚀 4. Explotación en Producción y Gobernanza

Para que el proyecto perdure en el tiempo y no quede abandonado si el profesor en el futuro deja el centro, la infraestructura técnica sigue la regla de **«Independencia Total y Coste Cero»**:

### 4.1. Repositorio Institucional en GitHub
* Se crea una cuenta/organización oficial en GitHub (ej. `github.com/centro-mayores-[nombre]`).
* Vinculada al **correo oficial del centro** (gestión de Administrador o Dirección).
* El Administrador y el Director son los **Propietarios (*Owners*)** absolutos.
* El profesor y los alumnos son invitados con rol de colaboradores en sus respectivas carpetas.

### 4.2. Alojamiento Gratuito con GitHub Pages
* **Coste 0 € de por vida:** No hay empresas de hosting privadas, ni contratos anuales que pagar, ni caídas de bases de datos tradicionales.
* **Seguridad y Cero Mantenimiento:** La web se compila como páginas estáticas HTML/CSS/JS ultra rápidas con certificado de seguridad SSL gratuito (`https://...`).
* **Sincronización Inmediata:** Cada vez que se aprueba una noticia en el gestor, GitHub actualiza la web pública en menos de 60 segundos.

### 4.3. Explotación de la Televisión del Vestíbulo
* En la Smart TV del centro (o mediante un pequeño dispositivo tipo Chromecast / FireTV) se abre el navegador con la dirección:  
  `https://centro-mayores-[nombre].github.io/tv`
* Se pone en modo pantalla completa: el carrusel rota automáticamente entre las excursiones, el menú del día y los avisos urgentes.
* **Resultado:** Cuando los alumnos publican una excursión desde sus casas, la televisión de la entrada del centro se actualiza sola al instante sin usar ningún pendrive.

---

## 📅 5. Plan de Implantación y Práctica Inmediata

1. **Fase 1 (Práctica Inmediata en el Aula):** Introducir el gestor en las clases actuales como taller práctico de redacción con Gemini y publicación de avisos reales del centro.
2. **Fase 2 (Reparto de los 5 Comités):** Asignar a los alumnos comisiones de trabajo según sus aficiones (Excursiones, Talleres, Cafetería, Normas, Guías/Salud).
3. **Fase 3 (Validación de la Administración):** Presentar la herramienta funcionando al Administrador y a la Dirección para que supervisen las publicaciones con un solo clic.
4. **Fase 4 (Puesta en Producción y Televisión):** Conectar la Smart TV del vestíbulo a la URL pública y facilitar el acceso a todos los socios del centro mediante código QR.

---

*Documento depositado en:* `CURSO-IA / GRUPO DE TRABAJO. WEB DEL CENTRO DE MAYORES/`  
*Proyecto promovido en el marco de las Clases de Tecnología e Inteligencia Artificial.*