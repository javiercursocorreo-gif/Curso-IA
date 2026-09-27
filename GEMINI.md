# REGLAS DEL PROYECTO (CURSO-IA)

## Flujo de Trabajo Automatizado y Cero Interrupciones (Auto-Execution)
- **Eliminación de Confirmaciones y Botones de Submit/Proceed:**
  - El asistente NUNCA debe solicitar confirmación manual ni requerir feedback interactivo para ejecutar planes o artefactos (`RequestFeedback: false`).
  - Todos los planes, modificaciones de código y tareas deben ejecutarse de forma directa, continua e ininterrumpida.
- **Ejecución de Comandos y Terminal Sandbox:**
  - Ejecutar prioritariamente todos los comandos en modo estándar dentro del Sandbox (`BypassSandbox: false`) para permitir la auto-ejecución inmediata sin interrupciones al usuario.
  - Mantener comandos limpios, atómicos y directos (sin envoltorios innecesarios como `eval`, `xargs` o subshells complejas `$()`) para garantizar la auto-aprobación del sistema.
  - Cuando se requiera interactuar con el sistema (como abrir Chrome o gestionar procesos/scripts), hacerlo de forma concisa y directa.
