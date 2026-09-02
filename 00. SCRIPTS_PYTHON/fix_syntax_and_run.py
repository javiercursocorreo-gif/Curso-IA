import os

script_path = '/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/build_repositorio_maestro.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Corregir el nodo raíz en .mm
idx_node = text.find('root_node = ET.SubElement(root_xml, "node", {')
if idx_node != -1:
    idx_node_end = text.find('})', idx_node)
    if idx_node_end != -1:
        text = text[:idx_node] + 'root_node = ET.SubElement(root_xml, "node", {\n    "ID": get_id(),\n    "TEXT": "REPOSITORIO MAESTRO DE IA"\n})' + text[idx_node_end+2:]
        print("-> Nodo raíz de .mm corregido sintácticamente.")

# 2. Corregir y asegurar el título interior de portada (p_title)
idx_title = text.find("p_title = doc.add_paragraph()")
if idx_title != -1:
    idx_title_hr = text.find("----------------------------------------------------------------------------------------------------", idx_title)
    if idx_title_hr != -1:
        new_title_block = """p_title = doc.add_paragraph()
r_t = p_title.add_run('REPOSITORIO MAESTRO DE IA\\n')
r_t.bold = True
r_t.font.size = Pt(22)
r_t.font.color.rgb = RGBColor(0x0D, 0x1B, 0x4A)

p_sub = doc.add_paragraph()
r_s1 = p_sub.add_run('Manual y Repositorio Integral para el Aula (Mayores 60+): Crear en cualquier IA (< 200 car.) y Transformar en Gemini\\n')
r_s1.italic = True
r_s1.font.size = Pt(13)
r_s1.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

p_sub.add_run('4 Bloques Maestros | 48+ Estilos Catalogados | 120+ Ejemplos Reales y Prácticas de Edición en 2 y 3 Pasos\\n').font.size = Pt(11)

doc.add_paragraph('"""
        text = text[:idx_title] + new_title_block + text[idx_title_hr:]
        print("-> Portada interior corregida y maquetada como 'REPOSITORIO MAESTRO DE IA'.")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("=== CORRECCIÓN LISTA. EJECUTANDO BUILD DEFINITIVO... ===")
