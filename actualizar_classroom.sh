#!/bin/bash
cd "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"

echo "=== 1. Copiando ilustraciones oficiales recortadas del cartel... ==="
mkdir -p "SIMULADORES_INTERACTIVOS/01_SIMULADORES/cards_11d"
cp -r "/Users/externo/.gemini/antigravity/brain/cbfe82a5-4265-4c02-9b6a-03745e403571/scratch/cards/"* "SIMULADORES_INTERACTIVOS/01_SIMULADORES/cards_11d/" 2>/dev/null || true
cp "/Users/externo/.gemini/antigravity/brain/cbfe82a5-4265-4c02-9b6a-03745e403571/scratch/card_images.js" "SIMULADORES_INTERACTIVOS/01_SIMULADORES/card_images.js" 2>/dev/null || true

echo "=== 2. Guardando cambios y sincronizando con GitHub... ==="
git add -A
git commit -m "feat(s24): integrar ilustraciones oficiales del cartel de las 11 dimensiones [COD-024]" || true
git push origin main

echo "=== 3. Replicando en carpeta de Sesion 24... ==="
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/24_Sesion"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/24_SIMULADOR_11_DIMENSIONES_UNIVERSO.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/24_Sesion/SIMULADOR_11_DIMENSIONES_UNIVERSO.html" 2>/dev/null || true
cp -r "SIMULADORES_INTERACTIVOS/01_SIMULADORES/cards_11d" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/24_Sesion/" 2>/dev/null || true

echo "=== 4. Abriendo en Google Chrome (forzando recarga sin cache)... ==="
TS=$(date +%s)
open -a "Google Chrome" "SIMULADORES_INTERACTIVOS/01_SIMULADORES/24_SIMULADOR_11_DIMENSIONES_UNIVERSO.html?v=$TS"

echo "=== COMPLETADO CON EXITO ==="
