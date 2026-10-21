#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import re

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=" * 70)
    print("🔍 DIAGNÓSTICO ENERGÉTICO DIRECTO DE macOS (PANTALLA Y REPOSO)")
    print("=" * 70)
    
    # 1. Configuración de pmset y quién bloquea
    pmset_g = run_cmd("pmset -g")
    print("\n1. CONFIGURACIÓN ACTUAL DE REPOSO (pmset -g):")
    display_line = ""
    for line in pmset_g.splitlines():
        if any(k in line.lower() for k in ['sleep', 'displaysleep', 'disksleep']):
            print("   " + line.strip())
            if "displaysleep" in line.lower():
                display_line = line.strip()

    # 1B. Estado de Chrome
    ps_chrome = run_cmd("ps aux | grep -i 'Google Chrome' | grep -v grep")
    print("\n1B. ¿SIGUE CHROME ABIERTO EN SEGUNDO PLANO?:")
    if ps_chrome.strip():
        print("   ⚠️ SÍ, Google Chrome sigue activo en memoria (no se cerró del todo con Cmd+Q).")
        print("      Procesos de Chrome encontrados: " + str(len(ps_chrome.strip().splitlines())))
    else:
        print("   ✅ Google Chrome está 100% CERRADO (no queda ningún proceso en memoria).")
            
    # 2. Aserciones que impiden el reposo de pantalla
    assertions = run_cmd("pmset -g assertions")
    print("\n2. PROGRAMAS QUE BLOQUEAN LA PANTALLA (PreventUserIdleDisplaySleep):")
    
    # Buscar qué proceso tiene PreventUserIdleDisplaySleep
    lines = assertions.splitlines()
    display_blockers = []
    current_pid_info = ""
    in_details = False
    
    for line in lines:
        if "PreventUserIdleDisplaySleep" in line and not in_details:
            print("   -> Estado global: " + line.strip())
        if "Listed by owning process:" in line:
            in_details = True
        if in_details:
            if "pid " in line:
                current_pid_info = line.strip()
            if "PreventUserIdleDisplaySleep" in line:
                display_blockers.append(f"{current_pid_info} -> {line.strip()}")
                
    if display_blockers:
        print("\n   🚨 ¡CULPABLE ENCONTRADO! Estos programas prohíben apagar la pantalla:")
        for b in display_blockers:
            print("      • " + b)
    else:
        print("   ✅ Ningún programa tiene bloqueada la pantalla explícitamente.")
        
    # 3. Comprobar si hay procesos caffeinate activos
    ps_caff = run_cmd("ps aux | grep -iE 'caffeinate' | grep -v grep")
    print("\n3. PROCESOS 'CAFFEINATE' EN SEGUNDO PLANO:")
    if ps_caff.strip():
        for l in ps_caff.splitlines():
            print("   • " + l.strip())
    else:
        print("   ✅ No hay comandos 'caffeinate' en ejecución.")

    # 4. Guardar copia en archivo para lectura silenciosa
    with open("diagnostico_pantalla_resultado.txt", "w", encoding="utf-8") as f:
        f.write("=== PMSET -G ===\n" + pmset_g + "\n")
        f.write("=== ASSERTIONS ===\n" + assertions + "\n")
        f.write("=== DISPLAY BLOCKERS ===\n" + "\n".join(display_blockers) + "\n")
        
    print("\n" + "=" * 70)
    print("📋 Diagnóstico guardado en: diagnostico_pantalla_resultado.txt")
    print("=" * 70)

if __name__ == '__main__':
    main()

