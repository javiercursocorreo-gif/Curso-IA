#!/bin/bash
cd "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"

echo "=== 1. Guardando cambios y sincronizando con GitHub... ==="
git add -A
git commit -m "feat(Classroom): asegurar tarjeta 09B COBOL en Mapa Sesion 02" || true
git push origin main

echo "=== 2. Abriendo Mapa Local en Chrome... ==="
open -a "Google Chrome" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/02_Sesion/MAPA_SESION_02.html"

echo "=== 3. Abriendo Version GitHub Pages en Chrome... ==="
open -a "Google Chrome" "https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100.%20[SESSIONS]%20TERNAS_LISTAS_PARA_CLASSROOM/02_Sesion/MAPA_SESION_02.html?v=s02_cobol_update"

echo "=== COMPLETADO CON EXITO ==="

