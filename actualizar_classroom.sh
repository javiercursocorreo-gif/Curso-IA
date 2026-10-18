#!/bin/bash
cd "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"

echo "=== 1. Guardando cambios y sincronizando con GitHub... ==="
git add -A
git commit -m "feat(s24): simulador 3D interactivo 11 dimensiones del universo (Teoria M) [COD-024]" || true
git push origin main

echo "=== 2. Replicando en carpeta de Sesion 24... ==="
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/24_Sesion"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/24_SIMULADOR_11_DIMENSIONES_UNIVERSO.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/24_Sesion/SIMULADOR_11_DIMENSIONES_UNIVERSO.html" 2>/dev/null || true

echo "=== 3. Abriendo Simulador 3D de las 11 Dimensiones en Google Chrome... ==="
open -a "Google Chrome" "SIMULADORES_INTERACTIVOS/01_SIMULADORES/24_SIMULADOR_11_DIMENSIONES_UNIVERSO.html"
open -a "Google Chrome" "SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/INDICE_10_SIMULACIONES_INTERACTIVAS_3D.html"

echo "=== COMPLETADO CON EXITO ==="
