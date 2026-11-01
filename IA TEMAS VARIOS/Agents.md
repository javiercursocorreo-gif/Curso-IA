# Directrices del Proyecto Matriz: IA TEMAS VARIOS

Este documento define la operativa general, la estructura de trabajo y las normas estrictas de ejecución para los agentes y asistentes de IA en la carpeta matriz **IA TEMAS VARIOS**.

---

## 🏆 REGLA DE ORO (Ejecución y Flujo de Trabajo)

1. **Trabajo 100% en Sandbox:**
   - Todas las tareas, generación de código, procesamiento de textos, análisis de datos y creación de documentos deben ejecutarse **estrictamente dentro del entorno Sandbox estándar** (`BypassSandbox: false`).
   - El agente **NO debe solicitar elevación de permisos ni autorizaciones manuales en mitad del proceso**.
   - **Cero interrupciones:** No lanzar ventanas modales, formularios ni solicitudes de confirmación (*submits*) durante la ejecución.

2. **Entrega Final con Comando de Terminal:**
   - Si una acción requiere interactuar con el sistema operativo fuera del sandbox (por ejemplo, sincronizaciones de iCloud, apertura de aplicaciones nativas, copia de ficheros protegidos o instalación global), el agente completará todo su trabajo interno y **al final de su respuesta facilitará un comando limpio y listo para copiar y pegar en la terminal del usuario**.

---

## 📁 Estructura del Proyecto Matriz y Subcarpetas

La carpeta **`IA TEMAS VARIOS`** actúa como contenedor raíz donde se irán incorporando diferentes temáticas y consultas estructuradas:

* **Raíz (`IA TEMAS VARIOS/`):**
  * `Agents.md`: Reglas generales, flujos y arquitectura de agentes.
  * `Gemini.md`: Protocolos y directrices específicas para el modelo Gemini.
* **Subcarpetas temáticas:** Cada consulta o bloque temático dispondrá de su propia subcarpeta independiente:
  * `INFECCIONES DE ORINA/`: Informes, antibiogramas, análisis de sensibilidad y PDFs resumen.
  * `ESPALDA/`: Historiales clínicos, pruebas de imagen, traumatología y seguimiento de columna.
  * *Futuras subcarpetas:* Nuevos temas médicos, personales o técnicos según se requieran.

---

## 🩺 Rigor en Consultas Médicas y de Salud

* **Microbiología y Analíticas:**
  * No interpretar la CMI como escala ordinal de potencia; evaluar siempre los puntos de corte clínicos oficiales (Sensible / Intermedio / Resistente).
  * Distinguir rigurosamente entre foco de infección bajo (vejiga/cistitis) y alto/sistémico (riñón/pielonefritis).
  * Señalar resistencias intrínsecas conocidas de cada especie bacteriana.
* **Informes Clínicos y Traumatología:**
  * Estructuración cronológica y anatómica clara.
  * Resúmenes ejecutivos orientados a la toma de decisiones médicas, con advertencia expresa de supervisión facultativa.

---

## 📄 Estándares de Documentación y Entregables

* **Documentos PDF:** Acabado editorial profesional (encabezados, numeración de páginas "Página X de Y", márgenes limpios, tablas comparativas y cajas de alerta).
* **Navegabilidad:** Enlaces directos a los archivos generados mediante el esquema `file://`.
