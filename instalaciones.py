import subprocess
import sys
import os

programa_python = sys.executable
carpeta_pip = os.path.dirname(programa_python)
os.chdir(carpeta_pip)
comando_pip = [programa_python, "-m", "pip", "install", "requests"]
#comando_request = [programa_python, "-m", "pip", "install", "requests"]

print(programa_python)
print(carpeta_pip)
print()

try:
    subprocess.run(comando_pip, check=True)
except subprocess.CalledProcessError as e:
    print("Error durante la instalación:", e)

