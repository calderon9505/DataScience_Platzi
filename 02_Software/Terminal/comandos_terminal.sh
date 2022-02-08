# Aplicaciones y caracteristicas ->
# programas y caracteristicas ->
# Activar o desactivar las caracteristicas de windows ->
# Subsistema de windows para linux

# https://linuxjourney.com/

# IMPORTANTE LA ACTUALIZACION
# sudo apt update
# sudo apt install tree

# en WSL escoger carpeta y poner "code ."
# instalar Remote-WSL en VSC

# diferencia entre apt y apt-get
# apt al parecer es más moderno y mejor (casi siempre)

# dos guiones cuando es una palabra completa y no solo una letra
# {--help | --manual | --version}

# cuando ponemos $ estamos accediendo a las variables de entorno
echo $0			    #-bash
echo $SHELL		    #/bin/bash
echo $TERM		    #xterm-256color
env			        #Todos los datos del entorno
printenv		    #variables de entorno


file		        #descripcion de un archivo especifico


# bandera de ls:
l		        #long
a		        #all, archivos ocultos (empiezan con punto)
A               #all except . and ..
h		        #human
S		        #size orden
r		        #reverse (z-a)
t		        #orden fecha modificacion
ls -d */		#listar solo los directorios

#tree
tree
tree -L	2	    #level, dos niveles

# Creacion y manipulacion de archivos
mkdir		
touch				                    #crear archivos
cp fileSource fileObject	            #copiar archivo
cp *.jpg /home/pete/Pictures
cp -ri Pumpkin/ /home/pete/Documents
mv fileX _destination		            #mueve archivo o directorio al destino indicado
mv fileX fileY			                #renombrar archivo y directorios
rm -irf fileX			                #borrar archivo (interactive, recursive, force)
rmdir				                    #borrar carpeta vacia

cd - 				                    #(previous directory)

# historial de comandos
ctrl+r				                    #comandos anteriores (filtro)
history				                    #comandos anteriores
!numero				                    #ejecuta el numero de comando de history

# visualizacion de archivos
cat fileX.txt			                #muestra el archivo
less fileX.txt			                #less is more
q, g, G, /search                        #para navegar en less
head fileX.txt -n 15		            #primeras 15 lineas (10 defecto)
tail
xdg-open fileX.txt		                #abre con el editor de codigo predet.
nautilus

cat > archivonuevo.txt		            crear un archivo nuevo y puedo escribir de una(ctrl+d para salir)


# Un comando puede ser 4 cosas:
# Un programa ejecutable: que se compilo en algun lenguaje de programación y se puede ejecutar
# Un comando de utilidad de la shell.
# Una función de shell
# Un alias

type cd                 #cd is a shell builtin
type mkdir              #mkdir is /usr/bin/mkdir
type ls                 #ls is aliased to 'ls --color=auto'

alias l="ls -lh"        #creacion de alias
alias la="ls -lA"                       
# abrir archivo .bashrc para poner los alias. ejecutar "bash" para ver los cambios

cd --help		    #ayuda del comando
help cd
man ls				#manual
info ls
whatis ls

# WILDCARDS
* 		            #the wildcard of wildcards
? 		            #used to represent one character
[] 		            #used to represent any character within the brackets [1-6]
ls [[:upper:]]*	    #archivos que inician con mayuscula (ls */ para directorios)


# https://www.linuxtotal.com.mx/index.php?cont=redireccionamiento-en-linux
# redireccionamiento
# file descriptors


# 0 - stdin
# 1 - stdout
# 2 - stderr

ls Downloads > misarchivos.txt 	            #(>> concatena) (2> stderr)
ls Documents > output.txt 2>&1 	            #(Redirecciona stderr hacía donde stdout apunte)
sort < lista_de_servidores.txt 	            #(ordena lo que haya en lista_de_servidores.txt)
sort < lista_desordenada.txt > lista_ordenada.txt

# pipe operator
ls -lh | less
tree | tee output.txt | less	            #tee redirecciona a terminal y a un archivo a la vez
# cowsay y lolcat			curiosidades

# operadores de control
cal				                        #calendario en la terminal
date				                    #fecha en la terminal
ls; mkdir otroDirectorio; ls; cal	    #ejecucion de manera sincrona (uno despues del otro)
ls & date & cal				            #ejecucion asincrona (un hilo por cada proceso)
mkdir test && cd test && echo ok	    #uno depende del exito del otro
mkdir test || cd test || echo ok        #solo ejecuta el primero que no de errrores

# PERMISOS
# user group others
chmod u-r mitexto.txt			    #quita permisos de lectura al usuario
chmod u-x,go+w mitexto.txt
chmod go=w mitexto.txt			    #sobreescribe permisos, solo lectura
whoami					            #quien soy yo
id					                #uid-userid, gid-groupid
su root					            #switch user (no funciona XD)
sudo su	(sudo su root)			    #para ubuntu (el cd de root es diferente)(su calderon)
psswd					            #cambiar contraseña
# entrar al usuario root y cambiar la contraseña (950527) por seguridad
# despues de hacer esto ya se puede usar "su root"
ln -s Ruta/Deseada RutaDeseada		#acceso directo desde la terminal(se acceden con cd)
ln -s /mnt/c/Users/User/Documents/ documentosWindows

# VARIABLES DE ENTORNO
printenv                #imprime todas las variables de entorno
echo $HOME
echo $PATH				#rutas de todos los binarios que ejecuta el sistema
# en .bashrc estan todas las variables de entorno
# abrir archivo .bashrc para poner los alias. ejecutar "bash" para ver los cambios

# COMANDOS DE BUSQUEDA
which code				                #ruta donde se aloja code
find ruta -name 'ArchivoABuscar'	    #busca todos los archivos que coincidan
find . -type df -iname '*.txt'		    #(directory or file)
find -type f -name '*.log'              #
find -size +10M	(10M)			        #archivos mayores a 10MB (10M aprox)
-mmin (minutos), -mtime (horas)         #
find . -perm 644 -maxdepth 2            #buscar por permisos y maxima profundidad
find . -type f -empty                   #archivos vacios
find . -type d -iname "*.log" -delete	#PELIGRO. borra todo lo que encuentre

l $(find . -size 10M)                   #crea un shell dentro de otro shell

grep Towers movies.csv                  #busca coincidencias dentro de los archivos
grep -i the movies.csv | less		    #ignore case sensitive
grep -ci the movies.csv			        #cuenta las ocurrencias (-v las no coincidencias)
wc movies.csv				            #cuenta lineas, palabras, bytes (-l -w -c)
ls -al | grep alguntexto                
cat unArchivoLargo.txt | grep "La línea que busco"


# UTILIDADES DE RED
ping -c 4 www.google.com				#solo cuatro pings
curl www.google.com					    #trae un archivo (text) de la red
wget www.google.com					    #creo que es igual a curl
traceroute www.google.com				#traza la ruta de conexión a google
netstat -i 						        #muestra dispositivos de red

# COMPRIMIENDO ARCHIVOS
tar -cvf ToCompress.tar ToCompress			#-c comprimir -v verbose -f file
tar -cvzf ToCompress.tar.gz ToCompress	    #-z compresion gzip
tar -xzvf ToCompress.tar.gz				    #descomprimir
zip -r ToCompress.zip ToCompress
unzip ToCompress.zip
# tar es mejor para compresion de archivos en texto plano 
# rar y unrar se usa casi igual que zip

# MANEJO DE PROCESOS
ps							#procesos que estan corriendo 
ps ax
top							#procesos y recursos que usan
htop
cat & 					    #ejecutar procesos en background
cat > mi_nota.txt &			#envia el proceso directo al background
kill PID					#matar procesos por ID
killall


ctrl+D							#termina el proceso de escritura cat
ctrl+Z							#suspense el job([1]+  Stopped  cat > mi_nota.txt)
ctrl+C							#finaliza o mata proceso
jobs							#procesos en background (id del job)
fg 1							#traer job al foreground
kill %job				        #matar procesor por numero de trabajo

# si abro $google-chrome-stable se ejecuta pero no me deja escribir en terminal
# si le doy ctrl+z suspende el proceso, es decir, no me deja usar google chrome
# pero si le doy bg 1 se envia al background y puedo usar tanto terminal como chrome
# lo que esta en bg se esta ejecutando, a lo que le doy ctrl+Z NO. 

# EDITORES DE TEXTO
# vim, emacs, nano