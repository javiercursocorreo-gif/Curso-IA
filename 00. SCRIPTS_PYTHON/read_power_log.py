#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess

def main():
    print("=" * 70)
    print("📜 HISTORIAL DEL KERNEL: ¿POR QUÉ SE ENCIENDE O NO SE APAGA LA PANTALLA?")
    print("=" * 70)
    
    try:
        # Obtener los últimos eventos de pantalla del registro oficial del sistema
        cmd = "pmset -g log | grep -iE '(display|darkwake|wake from|sleep prevented)' | tail -n 25"
        out = subprocess.check_output(cmd, shell=True).decode('utf-8', errors='ignore')
        print(out)
        with open("registro_energia_log.txt", "w", encoding="utf-8") as f:
            f.write(out)
    except Exception as e:
        print(f"Error leyendo log: {e}")

    print("=" * 70)

if __name__ == '__main__':
    main()

