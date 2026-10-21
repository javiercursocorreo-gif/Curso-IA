#!/bin/bash
# ==============================================================================
# LANZADOR AUTOMÁTICO DEL ATRIL KORG EK-50 PARA EL IPAD (0 SEGUNDOS)
# ==============================================================================
DIR="/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
cd "$DIR" || exit 1

echo "Iniciando servidor de alta velocidad en puerto 8888..."

# 1. Liberar el puerto 8888 si ya estaba en uso
lsof -ti:8888 | xargs kill -9 2>/dev/null || true

# 2. Iniciar el servidor local en segundo plano
nohup python3 -m http.server 8888 --directory "CURSO_MUSICA" > /tmp/korg_server_8888.log 2>&1 &
sleep 1

# 3. Detectar la IP del Mac
IP_LOCAL=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || ifconfig | grep "inet " | grep -v 127.0.0.1 | head -1 | awk '{print $2}')
[ -z "$IP_LOCAL" ] && IP_LOCAL="192.168.1.130"

# 4. Abrir en Chrome local
open -a "Google Chrome" "http://localhost:8888/" 2>/dev/null || true

# 5. Notificación nativa en macOS
osascript -e "display notification \"Servidor activo en http://${IP_LOCAL}:8888/\" with title \"🎼 Atril Korg EK-50 Activo\"" 2>/dev/null || true

clear
echo "======================================================================"
echo "🎹  SERVIDOR DE ATRIL KORG EK-50 ACTIVADO CON ÉXITO"
echo "======================================================================"
echo ""
echo "📱 EN TU IPAD (App MIDIWeb Browser), ESCRIBE ESTA DIRECCIÓN:"
echo ""
echo "     👉   http://${IP_LOCAL}:8888/   👈"
echo ""
echo "     (O también: http://$(hostname -s).local:8888/ )"
echo ""
echo "======================================================================"
echo "✓ Ya puedes cerrar esta ventana. El servidor seguirá funcionando."
echo ""
read -n 1 -s -r -p "Presiona cualquier tecla para cerrar este aviso..."
