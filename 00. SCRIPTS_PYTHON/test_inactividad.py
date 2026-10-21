#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import time
import sys

def get_idle_seconds():
    try:
        out = subprocess.check_output("ioreg -c IOHIDSystem | awk '/HIDIdleTime/ {print $NF}'", shell=True).decode()
        val = out.strip().splitlines()[0]
        return int(int(val) / 1000000000)
    except Exception as e:
        return -1

def main():
    print("=" * 70)
    print("⏱️ MONITOR DE INACTIVIDAD REAL DEL SISTEMA (HIDIdleTime)")
    print("=" * 70)
    
    idle_start = get_idle_seconds()
    print(f"\n1. TIEMPO DE INACTIVIDAD DETECTADO POR macOS AL INICIAR:")
    print(f"   macOS dice que llevas inactivo: {idle_start} segundos ({round(idle_start/60, 1)} minutos)")
    print(f"   (El apagado está programado a los 180 segundos / 3 minutos)")

    print("\n2. MONITORIZANDO SI ALGO REINICIA EL CONTADOR EN SECRETO (5 segundos)...")
    history = []
    for i in range(5):
        time.sleep(1)
        s = get_idle_seconds()
        history.append(s)
        print(f"   Segundo {i+1}: Inactividad = {s} s")

    # Diagnóstico del comportamiento
    print("\n3. DIAGNÓSTICO:")
    if history[-1] > history[0]:
        print("   ✅ El contador de inactividad SUBE correctamente (nadie está simulando ratón).")
        if history[-1] >= 180:
            print("   ⚠️ ¡ATENCIÓN! La inactividad ha superado los 180s pero la pantalla no se apaga.")
            print("      Causa: En pantallas externas o ciertos monitores, el perfil de brillo")
            print("      o el driver de vídeo necesita un comando de refresco de pantalla.")
        else:
            faltan = 180 - history[-1]
            print(f"   ℹ️ Faltan {faltan} segundos reales de inactividad continua para los 3 minutos.")
    else:
        print("   🚨 ¡ALERTA! El contador se ha reiniciado a 0 sin que tocaras nada.")
        print("      Causa: El ratón óptico tiene micro-vibración o Amphetamine tiene activo")
        print("      el modo 'Drive Alive' / simulación de movimiento.")

    # Guardar reporte
    with open("resultado_inactividad.txt", "w", encoding="utf-8") as f:
        f.write(f"Idle start: {idle_start}\nHistory: {history}\n")

    print("\n" + "=" * 70)

if __name__ == '__main__':
    main()

