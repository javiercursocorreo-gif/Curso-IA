# 🧭 GUÍA METODOLÓGICA: EL MÉTODO DE LOS 3 PASOS (PROMPT SEMILLA ➔ PLANO ➔ CÓDIGO)

Este documento contiene la plantilla y el ejemplo práctico de cómo estructurar las clases para que los alumnos aprendan a crear aplicaciones interactivas con IA sin memorizar ni copiar prompts técnicos incomprensibles.

---

## 🎯 El Flujo Didáctico

```
┌──────────────────────────────────────┐
│  PASO 1: EL PROMPT SEMILLA (Humano) │  El alumno aporta el "QUÉ" (Objetivo pedagógico/negocio)
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  PASO 2: EL PLANO TÉCNICO (La IA)    │  La IA genera el "CÓMO" (Especificación arquitectónica)
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  PASO 3: LA CONSTRUCCIÓN (Producto)  │  La IA programa el archivo HTML completo y funcional
└──────────────────────────────────────┘
```

---

## 🟢 1. El Prompt Semilla Oficial (Listo para Copiar y Pegar)

Este es el texto que se le da al alumno (o que el alumno escribe) en Gemini / ChatGPT:

```text
Actúa como un experto en educación financiera, psicología del dinero y arquitectura web. 
Quiero crear una aplicación didáctica e interactiva en un solo archivo HTML para que mis alumnos comprendan los 5 escalones de la libertad financiera:
1. Dependencia / Supervivencia (Deudas de consumo, gastos mayores que ingresos).
2. Estabilidad / Solvencia (Ingresos > Gastos, sin deudas malas, 1 mes de colchón).
3. Seguridad Financiera (Fondo de emergencia completo de 6 meses de gastos).
4. Independencia Financiera / FIRE (Los ingresos pasivos cubren el 100% de los gastos).
5. Abundancia / Libertad Plena (Ingresos pasivos superan con creces el estilo de vida ideal).

No programes todavía. Escribe el prompt técnico maestro más exhaustivo, detallado y profesional posible para que un desarrollador de IA construya esta aplicación web interactiva con calculadora en tiempo real, sliders dinámicos y diagnóstico patrimonial.
```

---

## 🔵 2. El Plano Técnico que Genera la IA

La IA responde devolviendo este pliego de condiciones de ingeniería:

```text
Crea una aplicación web interactiva completa, autocontenida y profesional en un único archivo HTML (con CSS3 y JavaScript moderno integrados) que funcione como un simulador visual de "Los 5 Escalones de la Libertad Financiera".

Requisitos específicos:
1. Arquitectura y Layout:
   - Panel izquierdo: Calculadora interactiva con sliders en tiempo real para: Ingresos netos (€/mes), Gastos esenciales (€/mes), Ahorro líquido actual (€), Ingresos pasivos (€/mes) y Deudas de consumo (€).
   - KPIs automáticos: Tasa de ahorro (%), Meses de cobertura de emergencia, Flujo neto mensual (€) y Cobertura pasiva (%).
   - Panel derecho: Visualización vertical de los 5 escalones en forma de pirámide/termómetro dinámico.

2. Lógica de Diagnóstico en Tiempo Real:
   - El sistema debe recalcular dinámicamente y encender con resplandor el escalón exacto donde se ubica el usuario según sus números.
   - Tarjeta Hero: Mostrar el título del nivel, color semafórico y explicación psicológica de su estado financiero.
   - Plan de Acción: Indicar la cifra matemática exacta que le falta para subir al siguiente escalón (ej. "Te faltan 2.400 € para alcanzar el Escalón 3").

3. Diseño Visual:
   - Modo oscuro premium (fondo #060913), tipografías Inter y JetBrains Mono.
   - Paleta cromática por niveles: Rojo (Supervivencia), Ámbar (Estabilidad), Azul Cian (Seguridad), Esmeralda (Independencia) y Púrpura (Abundancia).
   - Responsive, limpio y sin librerías externas pesadas.
```

---

## 🟣 3. La Ejecución Final

El alumno solo tiene que responder a la IA:

```text
Excelente. Ejecuta este prompt técnico y genera el código completo en un único archivo HTML listo para guardar y abrir en el navegador.
```

El resultado es la aplicación interactiva que se encuentra en:
`SIMULADORES_INTERACTIVOS/01_SIMULADORES/DEMO_LIBERTAD_FINANCIERA.html`

