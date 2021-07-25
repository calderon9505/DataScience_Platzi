# The Zen of python
import this

# Documentacion de Python
# https://docs.python.org/es/3/
# https://www.python.org/dev/peps/pep-0008/  IMPORTANTE!!! leerlo!!!

# Virtual Enviroment
#Un módulo es codigo de otros progrmadores (librerias)(los import)
#entorno virtual: tener python aislado para un proyecto que tiene sus propios módulos,
#está pensado para funcionar únicamente con ese proyecto
#en un directorio específico se define un venv con una version particular de python (no la global)
"sudo apt install python3.8-venv"       # libreria para crear venv (necesaria en wsl)
"python3 -m venv venv"                  # creacion entorno (-m module). (se crea carpeta venv)
#en la carpeta bin está el comando que activa el venv (en windows es "Script")
"source venv/bin/activate"              # crear alias y llamar activate
"deactivate"

# Package Installer for Python PIP
#correr todo esto con el venv activado
"pip freeze"                            #módulos que se tienen instalados (pip3)
"pip install pandas"                    #pandas incluye pandas, pytz, numpy, puthon_dateutil, six
"pip freeze > requirements.txt"         
"pip install -r requirements.txt"       #instala las dependencias específicas del proyecto
#PYENV es otro manejador de paquetes más complejo pero más completo
"pip show paquete"
"pip list"