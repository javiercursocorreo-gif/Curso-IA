# 📋 MANUAL DE PROCEDIMIENTOS Y CONFIGURACIÓN DEL SISTEMA (CURSO-IA)

Este documento registra los procedimientos operativos, configuraciones de sistema y ajustes en macOS para garantizar la ejecución desatendida del asistente sin desperdicio de energía y permitiendo el funcionamiento normal del salvapantallas.

---

## ⚡ PROCEDIMIENTO 01: CONFIGURACIÓN INTELIGENTE DE AMPHETAMINE (CERO INTERVENCIÓN MANUAL)

### Objetivo:
1. **Evitar que el usuario tenga que acordarse de encender/apagar la pastilla.**
2. **Permitir que el salvapantallas y el apagado de pantalla salten con normalidad** mientras Antigravity trabaja en segundo plano.
3. **Enviar el Mac a SLEEP profundo automáticamente** 5 minutos después de que el procesador termine de trabajar, ahorrando 100% de energía por la noche.

---

### Paso a Paso para la Configuración en macOS:

#### 1. Abrir Preferencias de Amphetamine:
* Haz clic en el icono de la pastilla en la barra superior.
* Pulsa en **Preferences…** (o el atajo `⌘ ,`).

#### 2. Activar el Reposo de Pantalla (Para que el Salvapantallas salte):
* Ve a la pestaña **Session Defaults** (2ª pestaña, icono de cronómetro).
* Marca la casilla: **☑️ "Allow display to sleep"** *(Permitir que la pantalla entre en reposo)*.
* *(Con esto, el Mac no se dormirá pero la pantalla sí tiene permiso de mostrar el salvapantallas o apagarse).*

#### 3. Configurar el Disparador Automático por CPU (Triggers):
* Ve a la pestaña **Triggers** (icono de rayo o diana).
* Marca la casilla superior: **☑️ "Enable Triggers"** *(Activar disparadores)*.
* Haz clic en el botón **`+`** (abajo a la izquierda) para añadir un disparador:
  * **Nombre del disparador:** `Antigravity / CPU Activa`
* En la lista de criterios (**Criteria**), haz clic en el botón **`+`** y selecciona la penúltima opción:
  * **CPU Utilization:**
    * Configura: *"When CPU utilization is above: 10%"* (o 5%).
* En las opciones de finalización (**Session End** abajo):
  * Marca: *"End session after CPU is idle for: 5 minutes"* *(Finalizar sesión cuando la CPU esté inactiva durante 5 minutos)*.
* Guarda y cierra las preferencias.

---

### Resultado Final:
* **Automatización 100%:** No necesitas tocar la pastilla nunca más.
* Cuando Antigravity trabaje, Amphetamine se activará sola en silencio.
* Tu pantalla activará el salvapantallas o se apagará para no gastar luz.
* Cuando el trabajo termine y pasen 5 minutos sin actividad de CPU, Amphetamine se apagará sola y **tu Mac entrará en Sleep profundo** para descansar toda la noche.

