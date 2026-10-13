# REGLAS DEL PROYECTO (CURSO-IA)

## Flujo de Trabajo Automatizado y Cero Interrupciones (Auto-Execution)
- **Eliminación de Confirmaciones y Botones de Submit/Proceed:**
  - El asistente NUNCA debe solicitar confirmación manual ni requerir feedback interactivo para ejecutar planes o artefactos (`RequestFeedback: false`).
  - Todos los planes, modificaciones de código y tareas deben ejecutarse de forma directa, continua e ininterrumpida.
- **Ejecución de Comandos y Terminal Sandbox:**
  - Ejecutar prioritariamente todos los comandos en modo estándar dentro del Sandbox (`BypassSandbox: false`) para permitir la auto-ejecución inmediata sin interrupciones al usuario.
  - Mantener comandos limpios, atómicos y directos (sin envoltorios innecesarios como `eval`, `xargs` o subshells complejas `$()`) para garantizar la auto-aprobación del sistema.
  - Cuando se requiera interactuar con el sistema (como abrir Chrome o gestionar procesos/scripts), hacerlo de forma concisa y directa.
- **Operaciones Masivas y Tareas Largas (Comando de Terminal para el Usuario):**
  - Cuando se trate de tareas largas, masivas o que requieran múltiples comandos/permisos fuera del sandbox (por ejemplo, procesamiento por lotes, git push pesado de muchos archivos, etc.), NUNCA encadenar decenas de solicitudes de aprobación/Submit por la interfaz de chat.
  - Proporcionar directamente al usuario el bloque de comando(s) listo para copiar y pegar en su terminal externa para que se ejecute de una sola vez sin pedir confirmaciones intermedias.

## Regla de Oro: Sincronización Inmediata Simulador 3D ⟷ Prompt de Gemini en Ficha [COD]
- **Sincronización Biunívoca en Tiempo Real:**
  - Cada vez que se agregue, modifique, elimine o ajuste cualquier característica técnica, visual, botón o funcionalidad interactiva en un simulador (o en el probador de código), el asistente DEBE actualizar simultáneamente en ese mismo turno el **Prompt Maestro para Gemini** en el script generador de la ficha didáctica `build_pdf_cod_XXX.py` y regenerar el PDF oficial del alumno.
  - El alumno debe poder copiar el prompt de su ficha en Gemini y obtener exactamente el 100% de las funciones implementadas en el simulador oficial.
  - Confirmar explícitamente en la respuesta al usuario que dicha sincronización ha quedado sellada en la ficha.


