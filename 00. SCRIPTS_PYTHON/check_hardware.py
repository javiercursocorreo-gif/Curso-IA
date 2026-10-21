#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess

def main():
    try:
        hw = subprocess.check_output("system_profiler SPHardwareDataType", shell=True).decode()
        disp = subprocess.check_output("system_profiler SPDisplaysDataType", shell=True).decode()
        with open("hardware_info.txt", "w", encoding="utf-8") as f:
            f.write("=== HARDWARE ===\n" + hw + "\n=== PANTALLAS ===\n" + disp)
    except Exception as e:
        with open("hardware_info.txt", "w", encoding="utf-8") as f:
            f.write(f"Error: {e}")

if __name__ == '__main__':
    main()

