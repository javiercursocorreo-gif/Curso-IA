#!/bin/bash
cd "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"

echo "=== 1. Guardando cambios y sincronizando con GitHub... ==="
git add -A
git commit -m "fix(s02): corregir titulo de tarjeta #13 a El Mamut Lanudo en Mapa Sesion 02" || true
git push origin main

echo "=== 2. Abriendo Mapa de la Sesion 02 en Chrome... ==="
open -a "Google Chrome" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/02_Sesion/MAPA_SESION_02.html"

echo "=== COMPLETADO CON EXITO ==="
