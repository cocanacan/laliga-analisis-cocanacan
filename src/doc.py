import subprocess
import os

# Ruta raíz del proyecto 
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(root, "src")
doc_path = os.path.join(root, "doc")

os.makedirs(doc_path, exist_ok=True)

modulos = [
    "exercises.ex1",
    "exercises.ex2",
    "exercises.ex3",
    "exercises.ex4",
    "exercises.ex5",
    "exercises.ex6",
    "exercises.ex7",
]

# Añadimos src/ al PYTHONPATH para que encuentre los módulos
entorno = os.environ.copy()
entorno["PYTHONPATH"] = src_path

# Generamos la documentación
for modulo in modulos:
    subprocess.run(
        ["python", "-m", "pydoc", "-w", modulo],
        cwd=doc_path,   # genera el HTML en doc/
        env=entorno     # pero encuentra los módulos gracias al PYTHONPATH
    )
