#!/usr/bin/env python3
import base64
import os
import shutil

ROOT = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
GLB_SRC = os.path.join(ROOT, "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/brain.glb")
B64_SRC = os.path.join(ROOT, "SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/brain_b64.js")

S06_DIR = os.path.join(ROOT, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/06_Sesion")
GLB_DEST = os.path.join(S06_DIR, "brain.glb")
B64_DEST = os.path.join(S06_DIR, "brain_b64.js")

def main():
    if not os.path.exists(GLB_SRC):
        print(f"Error: {GLB_SRC} no existe.")
        return

    size_mb = os.path.getsize(GLB_SRC) / (1024 * 1024)
    print(f"📦 Procesando {GLB_SRC} ({size_mb:.2f} MB)...")

    with open(GLB_SRC, "rb") as f:
        data = f.read()

    b64_str = base64.b64encode(data).decode("ascii")
    js_content = f'window.BRAIN_GLB_B64 = "data:model/gltf-binary;base64,{b64_str}";\n'

    with open(B64_SRC, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"✅ Generado {B64_SRC}")

    os.makedirs(S06_DIR, exist_ok=True)
    shutil.copy2(GLB_SRC, GLB_DEST)
    shutil.copy2(B64_SRC, B64_DEST)
    print(f"✅ Copiado a {S06_DIR}")

if __name__ == "__main__":
    main()

