# 🎙️ PROYECTO: ASISTENTE PERSONAL POR VOZ (iPHONE ➔ ANTIGRAVITY EN MAC)
*Espacio de Trabajo: `IA TEMAS VARIOS / ASISTENTE PERSONAL`*  
*Documento vivo de arquitectura, métodos de enlace y registro de avances.*

---

## 🎯 1. EL OBJETIVO DEL SISTEMA
Poder **dictar ideas de viva voz en cualquier momento desde el iPhone** (mientras caminas, conduces o estás fuera de casa) y que esas ideas queden **registradas de forma inmediata en el Mac** para que yo (Antigravity) pueda:
1. Leerlas y analizarlas en cuanto abras una sesión.
2. Clasificarlas por temáticas (Robótica, IA, Salud, Música, Proyectos personales).
3. Evaluar su viabilidad técnica.
4. Implementarlas contigo paso a paso cuando tú me indiques: *«Vamos a trabajar hoy en la idea número 3 del buzón»*.

---

## ⚡ 2. LA CLAVE TÉCNICA: EL PUENTE INVISIBLE (iCLOUD DRIVE)
Dado que tu espacio de trabajo ya reside dentro del ecosistema de Apple:
`/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/`

Todo lo que se guarde en esta carpeta **se sincroniza en milisegundos entre tu iPhone y tu Mac sin coste, sin servidores externos y sin intermediarios**.

Por tanto, no necesitamos montar servidores complejos en la nube ni pagar APIs de terceros: **el archivo receptor ya existe en tu iPhone y en tu Mac simultáneamente**.

---

## 🛠️ 3. LAS 3 VÍAS DE COMUNICACIÓN (COMPARATIVA)

### 🥇 VÍA 1 (LA RECOMENDADA): «Atajo de Siri de un Toque» (Dictado Directo a Markdown)
* **Cómo funciona en el iPhone:**
  1. Creas un **Atajo de Apple (Shortcuts)** de solo 2 pasos llamado *"Nueva Idea"*.
  2. Puedes activarlo de 3 formas sencillísimas:
     * Diciendo a viva voz: **«Oye Siri, nueva idea»**.
     * O tocando un **icono grande en la pantalla de inicio** del iPhone.
     * O pulsando el **Botón de Acción** del iPhone (si tienes iPhone 15 Pro o 16).
  3. El iPhone activa el micrófono, tú hablas libremente en español (ej: *«Quiero hacer un simulador de agujeros negros para la clase 6.4 de Interstellar con Three.js»*), y el iPhone transcribe tu voz a texto con el motor nativo de Apple.
  4. La acción del atajo añade automáticamente una nueva línea con fecha y hora al archivo:  
     `📁 IA TEMAS VARIOS/ASISTENTE PERSONAL/BUZON_IDEAS_VOZ.md`
* **Ventajas:**
  * Cero coste, 100% nativo de iOS.
  * Funciona con el iPhone bloqueado o con la pantalla apagada vía Siri.
  * Cuando te sientas al Mac, el texto ya está esperando dentro de Antigravity.

---

### 🥈 VÍA 2: «Notas de Voz Nativas + Transcripción por IA en el Mac»
* **Cómo funciona:**
  1. Abres la app nativa **Notas de Voz** de Apple en el iPhone y grabas tu audio (puedes hablar 5 o 10 minutos seguidos desahogándote sin preocuparte de pausas de dictado).
  2. Como Notas de Voz se sincroniza por iCloud, el archivo de audio `.m4a` aparece en tu Mac en segundos.
  3. En el Mac, un pequeño script procesa el audio con el modelo de transcripción de voz (Whisper / motor de voz nativo de macOS) y vuelca el texto limpio y estructurado en `BUZON_IDEAS_VOZ.md`.
* **Ventajas:**
  * Ideal si te gusta hablar mucho tiempo seguido o reflexionar en voz alta sin cortes de puntuación.
  * Conservas el audio original grabado.

---

### 🥉 VÍA 3: «Bot Privado de Telegram / WhatsApp Webhook»
* **Cómo funciona:**
  1. Te creas un chat contigo mismo o con un Bot privado de Telegram.
  2. Le envías un audio de voz o un mensaje de texto.
  3. Un script en tu Mac recibe el mensaje y lo anota en tu buzón.
* **Inconveniente:** Requiere que el Mac esté encendido y conectado a Internet en ese instante para recibir el mensaje en tiempo real, mientras que **iCloud (Vía 1) guarda el mensaje en la nube y se lo descarga al Mac en cuanto lo enciendes**.

---

## 📋 4. EL PROTOCOLO DE TRABAJO EN EL AULA Y EN EL MAC

```
[TU IPHONE]                          [NUBE ICLOUD]                     [TU MAC (ANTIGRAVITY)]
Dictado de viva voz        ➔     Sincronización silenciosa    ➔     BUZON_IDEAS_VOZ.md
("Oye Siri, nueva idea...")      en la carpeta de proyecto          actualizado al instante
                                                                               │
                                                                               ▼
                                                                Tú me dices en el chat:
                                                                "Antigravity, revisa el buzón"
                                                                               │
                                                                               ▼
                                                                Yo leo las nuevas ideas,
                                                                las organizo en un cuadro,
                                                                y tú eliges cuál programar.
```

---

## 🚀 5. CÓMO CREAR EL ATAJO EN EL IPHONE (PASO A PASO EN 2 MINUTOS)

En tu iPhone, abre la app **Atajos (Shortcuts)** y dale al botón **+** (Nuevo atajo):

1. **Paso 1:** Añade la acción **«Dictar texto»** (Idioma: Español).
2. **Paso 2:** Añade la acción **«Añadir a archivo»**:
   * Texto a añadir:  
     `- [ ] **[Fecha y hora actual]**: Texto dictado`
   * Ruta de archivo: Selecciona en la app Archivos:  
     `iCloud Drive / PERSONAL / CLASES DE TECNOLOGÍA / IA TEMAS VARIOS / ASISTENTE PERSONAL / BUZON_IDEAS_VOZ.md`
3. **Nombre del atajo:** Nómbralo **«Apunta esto»** o **«Nueva Idea»**.

A partir de ese momento, solo dices:  
👉 **«Oye Siri, apunta esto»** ... hablas ... ¡y ya está en mi memoria de trabajo!

---

## 📝 6. ESTADO DE IMPLEMENTACIÓN Y PRÓXIMOS PASOS
* [x] Carpeta `ASISTENTE PERSONAL` creada en `IA TEMAS VARIOS`.
* [x] Documento maestro de arquitectura redactado (`PROPUESTA_ARQUITECTURA_ASISTENTE_VOZ.md`).
* [x] Archivo receptor `BUZON_IDEAS_VOZ.md` inicializado y listo para recibir dictados.
* [ ] Prueba piloto: Configurar el atajo en el iPhone y dictar la primera idea de prueba.
* [ ] Añadir automatización para que Antigravity compruebe el buzón al iniciar cada sesión.
