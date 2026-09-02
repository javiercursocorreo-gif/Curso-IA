import os

script_path = '/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/build_repositorio_maestro.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Cambiamos el nombre de los archivos de salida (.docx y .mm) en el script
text = text.replace('ESTILOS DE IMAGENES CON IA.docx', 'REPOSITORIO MAESTRO DE IA.docx')
text = text.replace('mapa_mental_repositorio_maestro.mm', 'REPOSITORIO MAESTRO DE IA.mm')

# 2. Cambiamos el título interior del documento Word (donde decía REPOSITORIO MAESTRO: ESTILOS DE IMÁGENES CON IA V2 o similar)
idx_title_run = text.find("r_t = p_title.add_run(")
if idx_title_run != -1:
    idx_end_run = text.find(")", idx_title_run)
    text = text[:idx_title_run] + "r_t = p_title.add_run('REPOSITORIO MAESTRO DE IA\\n')" + text[idx_end_run+1:]
    print("-> Título interior de portada actualizado a 'REPOSITORIO MAESTRO DE IA'.")

# 3. Cambiamos el texto del nodo raíz del mapa mental (.mm)
idx_node_text = text.find('TEXT": "REPOSITORIO MAESTRO:')
if idx_node_text != -1:
    idx_node_end = text.find('"}', idx_node_text)
    if idx_node_end != -1:
        text = text[:idx_node_text] + 'TEXT": "REPOSITORIO MAESTRO DE IA"' + text[idx_node_end+2:]
        print("-> Nodo raíz interior de Freeplane (.mm) actualizado a 'REPOSITORIO MAESTRO DE IA'.")

# Guardar cambios en build_repositorio_maestro.py
with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

# 4. Eliminar los archivos antiguos de la carpeta si existen para no dejar duplicados confusos
folder = '/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/'
old_docx = os.path.join(folder, 'ESTILOS DE IMAGENES CON IA.docx')
old_mm = os.path.join(folder, 'mapa_mental_repositorio_maestro.mm')

if os.path.exists(old_docx):
    os.remove(old_docx)
    print("-> Eliminado archivo antiguo ESTILOS DE IMAGENES CON IA.docx")
if os.path.exists(old_mm):
    os.remove(old_mm)
    print("-> Eliminado archivo antiguo mapa_mental_repositorio_maestro.mm")

print("=== CAMBIO DE NOMBRES COMPLETADO. EJECUTANDO BUILD PARA GENERAR ARCHIVOS DEFINITIVOS... ===")
