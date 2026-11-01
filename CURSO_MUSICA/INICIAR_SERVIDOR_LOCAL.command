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

# 2. Iniciar el servidor directamente en la carpeta de música con bind 0.0.0.0 (IPv4 universal)
nohup python3 -m http.server --bind 0.0.0.0 8888 > /tmp/korg_server_8888.log 2>&1 &
sleep 1.2

# 3. Detectar la interfaz de red por defecto y la IP exacta del Mac
DEFAULT_IFACE=$(route -n get default 2>/dev/null | awk '/interface:/ {print $2}')
[ -z "$DEFAULT_IFACE" ] && DEFAULT_IFACE="en0"
IP_ACTIVA=$(ipconfig getifaddr "$DEFAULT_IFACE" 2>/dev/null)

if [ -z "$IP_ACTIVA" ]; then
    IP_ACTIVA=$(ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -1)
fi
[ -z "$IP_ACTIVA" ] && IP_ACTIVA="127.0.0.1"

LOCAL_HOST=$(scutil --get LocalHostName 2>/dev/null || hostname -s)
BONJOUR_URL="http://${LOCAL_HOST}.local:8888/"
IP_URL="http://${IP_ACTIVA}:8888/"

# 4. Probar respuesta inmediata en localhost
HTTP_CODE=$(curl -sI -o /dev/null -w "%{http_code}" -m 2 "http://127.0.0.1:8888/index.html" 2>/dev/null)

# 5. Copiar la dirección exacta al portapapeles universal de Apple
echo -n "$IP_URL" | pbcopy

clear
echo "======================================================================"
echo "🎹  SERVIDOR LOCAL WI-FI KORG EK-50 (ACTIVO EN PUERTO 8888)"
echo "======================================================================"
echo "🟢 Estado: Servidor HTTP activo en macOS (HTTP $HTTP_CODE)"
echo "📡 Interfaz activa: $DEFAULT_IFACE"
echo ""
echo "📱 COPIA O ESCRIBE EN SAFARI DE TU IPAD ESTA DIRECCIÓN EXACTA:"
echo ""
echo "         👉👉👉   $IP_URL   👈👈👈"
echo ""
echo "   Acceso directo a Canción 25 (Elvis Presley · 70 BPM):"
echo "         👉   ${IP_URL}CANCION_25_CANT_HELP_FALLING_IN_LOVE.html"
echo ""
echo "----------------------------------------------------------------------"
echo "🍎 ALTERNATIVA APPLE BONJOUR (SIN NÚMEROS DE IP):"
echo "         👉   $BONJOUR_URL"
echo "----------------------------------------------------------------------"
echo "🌐 ALTERNATIVA INTERNET (GITHUB PAGES OFICIAL):"
echo "         👉   https://externo2024.github.io/CURSO-IA/CURSO_MUSICA/CANCION_25_CANT_HELP_FALLING_IN_LOVE.html"
echo "======================================================================"

# Mostrar cartel emergente nativo en macOS para que no se pierda en la terminal
osascript -e 'display notification "'"$IP_URL"'" with title "Servidor Korg EK-50 Activo" subtitle "Dirección lista para tu iPad"' 2>/dev/null || true
osascript -e 'display dialog "Servidor Korg EK-50 funcionando en tu Mac.\n\nEn tu iPad escribe en Safari:\n\n'"$IP_URL"'\n\n(O la opción Bonjour: '"$BONJOUR_URL"')\n\nLa dirección ya está en tu portapapeles." with title "Atril Digital Korg EK-50" buttons {"Aceptar"} default button 1 giving up after 15' 2>/dev/null || true
