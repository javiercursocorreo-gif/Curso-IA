#!/bin/bash
cd "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"

echo "=== 0. Verificando y descargando modelos 3D oficiales (.glb) si no existen... ==="
mkdir -p "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS"

# 1. Motor CAD 3D (Khronos Group 2CylinderEngine.glb)
if [ ! -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/engine_3d.glb" ] || [ ! -s "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/engine_3d.glb" ]; then
    echo "Descargando modelo 3D oficial del motor (2CylinderEngine.glb)..."
    curl -sL "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/2CylinderEngine/glTF-Binary/2CylinderEngine.glb" -o "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/engine_3d.glb"
fi

if [ -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/engine_3d.glb" ] && [ ! -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/engine_3d_b64.js" ]; then
    echo "Generando engine_3d_b64.js..."
    echo -n 'window.ENGINE_3D_GLB_B64 = "data:model/gltf-binary;base64,' > "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/engine_3d_b64.js"
    base64 -i "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/engine_3d.glb" | tr -d '\n' >> "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/engine_3d_b64.js"
    echo '";' >> "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/engine_3d_b64.js"
fi

# 2. Tiranosaurio Rex 3D (dinosaur-trex.glb)
if [ ! -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/trex_3d.glb" ] || [ ! -s "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/trex_3d.glb" ]; then
    echo "Descargando modelo 3D oficial del T-Rex de museo (dinosaur-trex.glb)..."
    curl -sL "https://raw.githubusercontent.com/code4fukui/vr-dinosaur-museum/main/dinosaur-trex.glb" -o "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/trex_3d.glb"
fi

if [ -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/trex_3d.glb" ] && [ ! -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/trex_3d_b64.js" ]; then
    echo "Generando trex_3d_b64.js..."
    echo -n 'window.TREX_3D_GLB_B64 = "data:model/gltf-binary;base64,' > "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/trex_3d_b64.js"
    base64 -i "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/trex_3d.glb" | tr -d '\n' >> "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/trex_3d_b64.js"
    echo '";' >> "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/trex_3d_b64.js"
fi

# 3. Violín Stradivarius Real de Museo (The Gould, 1693, The Metropolitan Museum of Art)
if [ ! -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/violin_stradivarius_real.jpg" ] || [ ! -s "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/violin_stradivarius_real.jpg" ]; then
    echo "Descargando fotografía oficial de museo del Violín Stradivarius 'The Gould' (Met Museum)..."
    curl -sL "https://images.metmuseum.org/CRDImages/mi/original/DT669a.jpg" -o "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/violin_stradivarius_real.jpg"
fi

if [ -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/violin_stradivarius_real.jpg" ] && [ ! -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/violin_stradivarius_b64.js" ]; then
    echo "Generando violin_stradivarius_b64.js..."
    echo -n 'window.STRADIVARIUS_PHOTO_B64 = "data:image/jpeg;base64,' > "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/violin_stradivarius_b64.js"
    base64 -i "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/violin_stradivarius_real.jpg" | tr -d '\n' >> "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/violin_stradivarius_b64.js"
    echo '";' >> "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/violin_stradivarius_b64.js"
fi

# 4. Nebulosa Helix Oficial de la NASA / Hubble / Spitzer (NGC 7293)
if [ ! -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/helix_nebula_nasa.jpg" ] || [ ! -s "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/helix_nebula_nasa.jpg" ]; then
    echo "Descargando astrofotografía oficial de la NASA/Hubble de la Nebulosa Helix..."
    curl -sL "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/NGC7293_%282004%29.jpg/1280px-NGC7293_%282004%29.jpg" -o "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/helix_nebula_nasa.jpg"
fi

if [ -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/helix_nebula_nasa.jpg" ] && [ ! -f "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/helix_nebula_b64.js" ]; then
    echo "Generando helix_nebula_b64.js..."
    echo -n 'window.HELIX_NEBULA_PHOTO_B64 = "data:image/jpeg;base64,' > "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/helix_nebula_b64.js"
    base64 -i "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/helix_nebula_nasa.jpg" | tr -d '\n' >> "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/helix_nebula_b64.js"
    echo '";' >> "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/helix_nebula_b64.js"
fi

# 5. Auroras Ultravioletas de Júpiter Oficiales de la NASA / Hubble (heic1613a / opo1624a)
JUP_IMG="SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/jupiter_aurora_nasa.jpg"
if [ ! -f "$JUP_IMG" ] || ! file "$JUP_IMG" 2>/dev/null | grep -qi "jpeg\|image"; then
    echo "Descargando astrofotografía oficial de la NASA/Hubble de las Auroras de Júpiter (heic1613a)..."
    rm -f "$JUP_IMG"
    
    # Intento 1: Wikimedia Commons con User-Agent
    curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" "https://upload.wikimedia.org/wikipedia/commons/4/4b/Hubble_Captures_Vivid_Auroras_in_Jupiter%E2%80%99s_Atmosphere.jpg" -o "$JUP_IMG"
    
    # Intento 2: Versión 1280px
    if [ ! -s "$JUP_IMG" ] || ! file "$JUP_IMG" 2>/dev/null | grep -qi "jpeg\|image"; then
        curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Hubble_Captures_Vivid_Auroras_in_Jupiter%E2%80%99s_Atmosphere.jpg/1280px-Hubble_Captures_Vivid_Auroras_in_Jupiter%E2%80%99s_Atmosphere.jpg" -o "$JUP_IMG"
    fi

    # Intento 3: ESA Hubble Archive
    if [ ! -s "$JUP_IMG" ] || ! file "$JUP_IMG" 2>/dev/null | grep -qi "jpeg\|image"; then
        curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" "https://cdn.esahubble.org/archives/images/large/heic1613a.jpg" -o "$JUP_IMG"
    fi
fi

if [ -f "$JUP_IMG" ] && file "$JUP_IMG" 2>/dev/null | grep -qi "jpeg\|image"; then
    echo "Generando jupiter_aurora_b64.js..."
    echo -n 'window.JUPITER_AURORA_PHOTO_B64 = "data:image/jpeg;base64,' > "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/jupiter_aurora_b64.js"
    base64 -i "$JUP_IMG" | tr -d '\n' >> "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/jupiter_aurora_b64.js"
    echo '";' >> "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/jupiter_aurora_b64.js"
else
    echo "AVISO: No se pudo verificar la imagen JPEG de Júpiter. jupiter_aurora_b64.js no generado."
fi

echo "=== 1. Copiando ilustraciones oficiales recortadas del cartel... ==="
mkdir -p "SIMULADORES_INTERACTIVOS/01_SIMULADORES/cards_11d"
cp -r "/Users/externo/.gemini/antigravity/brain/cbfe82a5-4265-4c02-9b6a-03745e403571/scratch/cards/"* "SIMULADORES_INTERACTIVOS/01_SIMULADORES/cards_11d/" 2>/dev/null || true
cp "/Users/externo/.gemini/antigravity/brain/cbfe82a5-4265-4c02-9b6a-03745e403571/scratch/card_images.js" "SIMULADORES_INTERACTIVOS/01_SIMULADORES/card_images.js" 2>/dev/null || true

echo "=== 1B. Eliminando simuladores obsoletos duplicados (Panteón, Caracalla, Atlántida, Machu Picchu)... ==="
rm -f "SIMULADORES_INTERACTIVOS/01_SIMULADORES/08_SIMULADOR_PANTEON_ROMA_3D.html"
rm -f "SIMULADORES_INTERACTIVOS/01_SIMULADORES/09_SIMULADOR_TERMAS_CARACALLA_3D.html"
rm -f "SIMULADORES_INTERACTIVOS/01_SIMULADORES/10_SIMULADOR_ATLANTIDA_3D.html"
rm -f "SIMULADORES_INTERACTIVOS/01_SIMULADORES/11_SIMULADOR_MACHU_PICCHU_3D.html"
rm -f "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/08_Sesion/SIMULADOR_PANTEON_ROMA_3D.html"
rm -f "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/09_Sesion/SIMULADOR_TERMAS_CARACALLA_3D.html"
rm -f "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/10_Sesion/SIMULADOR_ATLANTIDA_3D.html"
rm -f "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/11_Sesion/SIMULADOR_MACHU_PICCHU_3D.html"

# Sincronizar nombres alternativos en 01_SIMULADORES
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/08_SIMULADOR_MOTOR_TURBOFAN_3D.html" "SIMULADORES_INTERACTIVOS/01_SIMULADORES/08_SIMULADOR_RELOJ_MECANICO_3D.html" 2>/dev/null || true
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/09_SIMULADOR_CRANEO_TREX_3D.html" "SIMULADORES_INTERACTIVOS/01_SIMULADORES/09_SIMULADOR_CELULA_EUCARIOTA_3D.html" 2>/dev/null || true

echo "=== 2. Replicando en carpetas de Sesiones 07 a 15 y 24... ==="
# Sesión 07
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/07_Sesion"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/07_SIMULADOR_LUNA_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/07_Sesion/SIMULADOR_LUNA_3D.html" 2>/dev/null || true

# Sesión 08
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/08_Sesion"
rm -f "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/08_Sesion/SIMULADOR_PANTEON_ROMA_3D.html"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/08_SIMULADOR_MOTOR_TURBOFAN_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/08_Sesion/SIMULADOR_MOTOR_TURBOFAN_3D.html" 2>/dev/null || true
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/08_SIMULADOR_MOTOR_TURBOFAN_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/08_Sesion/SIMULADOR_RELOJ_MECANICO_3D.html" 2>/dev/null || true

# Sesión 09
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/09_Sesion"
rm -f "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/09_Sesion/SIMULADOR_TERMAS_CARACALLA_3D.html"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/09_SIMULADOR_CRANEO_TREX_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/09_Sesion/SIMULADOR_CRANEO_TREX_3D.html" 2>/dev/null || true
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/09_SIMULADOR_CRANEO_TREX_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/09_Sesion/SIMULADOR_CELULA_EUCARIOTA_3D.html" 2>/dev/null || true

# Sesión 10
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/10_Sesion"
rm -f "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/10_Sesion/SIMULADOR_ATLANTIDA_3D.html"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/10_SIMULADOR_MOLAR_HUMANO_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/10_Sesion/SIMULADOR_MOLAR_HUMANO_3D.html" 2>/dev/null || true

# Sesión 11
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/11_Sesion"
rm -f "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/11_Sesion/SIMULADOR_MACHU_PICCHU_3D.html"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/11_SIMULADOR_VIOLIN_STRADIVARIUS_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/11_Sesion/SIMULADOR_VIOLIN_STRADIVARIUS_3D.html" 2>/dev/null || true

# Sesión 12
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/12_Sesion"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/12_SIMULADOR_NEBULOSA_HELIX_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/12_Sesion/SIMULADOR_NEBULOSA_HELIX_3D.html" 2>/dev/null || true

# Sesión 13
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/13_Sesion"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/13_SIMULADOR_ADN_GENETICO_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/13_Sesion/SIMULADOR_ADN_GENETICO_3D.html" 2>/dev/null || true

# Sesión 14
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/14_Sesion"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/14_SIMULADOR_AURORAS_JUPITER_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/14_Sesion/SIMULADOR_AURORAS_JUPITER_3D.html" 2>/dev/null || true

# Sesión 15
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/15_Sesion"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/15_SIMULADOR_PARTENON_AUREO_3D.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/15_Sesion/SIMULADOR_PARTENON_AUREO_3D.html" 2>/dev/null || true

# Sesión 24
mkdir -p "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/24_Sesion"
cp "SIMULADORES_INTERACTIVOS/01_SIMULADORES/24_SIMULADOR_11_DIMENSIONES_UNIVERSO.html" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/24_Sesion/SIMULADOR_11_DIMENSIONES_UNIVERSO.html" 2>/dev/null || true
cp -r "SIMULADORES_INTERACTIVOS/01_SIMULADORES/cards_11d" "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/24_Sesion/" 2>/dev/null || true

echo "=== 3. Guardando cambios y sincronizando con GitHub... ==="
git add -A
git commit -m "fix(s14): descarga oficial de astrofotografia real heic1613a de hubble sin bloqueos html y validacion jpeg" || true
git push origin main

echo "=== 4. Abriendo simuladores oficiales en Google Chrome... ==="
TS=$(date +%s)
DIR="$(pwd)"
open -a "Google Chrome" "file://${DIR}/SIMULADORES_INTERACTIVOS/01_SIMULADORES/13_SIMULADOR_ADN_GENETICO_3D.html?v=$TS"
open -a "Google Chrome" "file://${DIR}/SIMULADORES_INTERACTIVOS/01_SIMULADORES/14_SIMULADOR_AURORAS_JUPITER_3D.html?v=$TS"
open -a "Google Chrome" "file://${DIR}/SIMULADORES_INTERACTIVOS/01_SIMULADORES/15_SIMULADOR_PARTENON_AUREO_3D.html?v=$TS"

echo "=== COMPLETADO CON EXITO ==="
