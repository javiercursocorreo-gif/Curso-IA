#!/bin/bash
# ==============================================================================
# LANZADOR DEL SERVIDOR LOCAL WI-FI (0 SEGUNDOS) - KORG EK-50
# ==============================================================================
BASE_DIR="/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CURSO_MUSICA"
cd "$BASE_DIR" || exit 1

echo "Configurando servidor local de alta velocidad..."

# 1. Liberar absolutamente el puerto 8888 de procesos anteriores o bloqueados
pkill -9 -f "http.server 8888" 2>/dev/null || true
lsof -ti:8888 | xargs kill -9 2>/dev/null || true
sleep 0.5

# 2. Iniciar el servidor directamente en la carpeta de música (sin rutas intermedias)
nohup python3 -m http.server 8888 > /tmp/korg_server_8888.log 2>&1 &
sleep 1.2

# 3. Detectar la IP Wi-Fi real del Mac en este preciso instante
IP_WIFI=$(ipconfig getifaddr en0 2>/dev/null)
[ -z "$IP_WIFI" ] && IP_WIFI=$(ipconfig getifaddr en1 2>/dev/null)
[ -z "$IP_WIFI" ] && IP_WIFI=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | head -1 | awk '{print $2}')
[ -z "$IP_WIFI" ] && IP_WIFI="192.168.1.130"

HOST_NAME="$(hostname -s).local"

# 4. Probar respuesta inmediata
HTTP_CODE=$(curl -sI -o /dev/null -w "%{http_code}" -m 2 "http://127.0.0.1:8888/index.html" 2>/dev/null)

# 5. Copiar la dirección exacta al portapapeles del Mac e iPad
echo -n "http://${IP_WIFI}:8888/" | pbcopy

clear
echo "======================================================================"
echo "🎹  SERVIDOR LOCAL WI-FI KORG EK-50 ACTIVO (0 SEGUNDOS)"
echo "======================================================================"
echo ""
if [ "$HTTP_CODE" = "200" ]; then
    echo "🟢 Estado del Servidor: FUNCIONANDO AL 100% (HTTP 200 OK)"
else
    echo "🟡 Estado del Servidor: Activo en puerto 8888 (Respuesta: $HTTP_CODE)"
fi
echo ""
echo "📱 EN TU IPAD, ACCEDE A ESTA DIRECCIÓN EXACTA:"
echo ""
echo "     👉   http://${IP_WIFI}:8888/   👈"
echo ""
echo "     (O alternativa de red Apple: http://${HOST_NAME}:8888/ )"
echo ""
echo "     Acceso directo a Canción 25 (Elvis Presley · 70 BPM):"
echo "     👉   http://${IP_WIFI}:8888/CANCION_25_CANT_HELP_FALLING_IN_LOVE.html"
echo ""
echo "======================================================================"
echo "💡 NOTA: La dirección ya está copiada en el portapapeles para 'Pegar'."
echo "======================================================================"
