#!/bin/bash
# ==============================================================================
# LANZADOR AUTOMÁTICO DEL ATRIL KORG EK-50 PARA EL IPAD (0 SEGUNDOS)
# ==============================================================================
DIR="/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
cd "$DIR" || exit 1

echo "Iniciando servidor de alta velocidad en puerto 8888..."

# 1. Liberar el puerto 8888 si ya estaba en uso
lsof -ti:8888 | xargs kill -9 2>/dev/null || true

# 2. Iniciar el servidor local en segundo plano con enlace a todas las interfaces
nohup python3 -m http.server 8888 --bind 0.0.0.0 --directory "CURSO_MUSICA" > /tmp/korg_server_8888.log 2>&1 &
sleep 1

# 3. Detectar la IP del Mac en la red local
IP_LOCAL=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || ifconfig | grep "inet " | grep -v 127.0.0.1 | head -1 | awk '{print $2}')
[ -z "$IP_LOCAL" ] && IP_LOCAL="192.168.1.130"
HOST_MDNS="$(hostname -s).local"

# 4. Notificación nativa en macOS
osascript -e "display notification \"Servidor activo en http://${IP_LOCAL}:8888/\" with title \"🎼 Servidor Atril Korg Activo\"" 2>/dev/null || true

clear
echo "======================================================================"
echo "🎹  SERVIDOR DE ATRIL KORG EK-50 ACTIVADO CON ÉXITO (PUERTO 8888)"
echo "======================================================================"
echo ""
echo "📱 EN TU IPAD (Safari o Web MIDI Browser), ACCEDE A:"
echo ""
echo "     👉   http://${IP_LOCAL}:8888/   👈"
echo "     👉   http://${HOST_MDNS}:8888/   👈"
echo ""
echo "     Canción 25 directa:"
echo "     👉   http://${IP_LOCAL}:8888/CANCION_25_CANT_HELP_FALLING_IN_LOVE.html"
echo ""
echo "======================================================================"
echo "✓ Servidor blindado con nohup: seguirá activo aunque cierres la terminal."
echo ""
read -n 1 -s -r -p "Presiona cualquier tecla para cerrar este aviso..."
