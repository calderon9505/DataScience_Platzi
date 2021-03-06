# https://git-scm.com/book/en/v2
# https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
# https://danielkummer.github.io/git-flow-cheatsheet/
# https://learngitbranching.js.org/

shift + Ins                         #para pegar codigo en terminal Git bash (Insert)
cat .gitignore                      #lista de archivos o patrones a ignorar (*.ini)
git branch -M main                  #nombrar la rama como "main"
git config --global alias.grafico 'log --graph --pretty=oneline -15' #git grafico
git config --global alias.total 'log --oneline --graph --all -15' #git total


# GIT Configuration
git init                            #crea repositorio
git clone _url_                     #clonar repositorio existente
git config                          #todas las configuraciones de Git
git config --list (-l)              #configuracion actual de Git
git config --list --show-origin     #origen del archivo gitconfig(avanzado)
git config --global user.name "Sebastian Calderon"
git config --global user.email "calderon950527@gmail.com"
git config --global core.editor "code --wait"


# First steps                       #master. rama principal
git add archivo.xxx                 #añade archivo al Staging Area (ram)
git commit -m " "                   #envia el archivo al repositorio
git commit -am " "                  #-a saltarse el add; (-ma no sirve)
git status                          #estado de los archivos
git status -s (--short)             #estado conciso de los archivos
                                    #left-staged; right-unstaged
                                    #??-untracked; A-staged(nuevo); M-modified


# Commit history and comparations   #HEAD. apuntador a la rama local en la que estoy
git show archivo.xxx                #historial de cambios del archivo (git show, ultimo cambio)
git log archivo.xxx                 #historial del archivo (git log)
git log -p -2                       #-p diferencias introduc. -2 solo dos commits
git log --stat                      #archivos en que se hicieron cambios por commit
git log --pretty=oneline            #cada commit es una linea (short, full, fuller)
git log --graph                     #grafico ASCII muestra historial (usar con oneline)
git log --graph --oneline
git log --since=" "                 #(2.weeks)("2008-01-15")("2 years 1 day 3 minutes ago")
git log --author " " --grep " " --all-match
git diff                            #Working directory vs staging area (WD vs Rep medio enreado)
git diff --staged (--cached)        #staging Area vs Repositorio
git diff old_code new_code          #comparar versiones de commit


# Undoing Things
git restore archivo.xxx             #discard changes in working directory
git restore --staged archivo.xxx    #unstage. back to working directory
git commit --amend                  #rehacer commit adicionando lo que esté en staging
git reset old_code --soft           #version anterior pero manteniendo el staging
git reset old_code --hard           #version anterior borrando todo los demás commits
git checkout old_code archivo.xxx   #revisar archivo en commit indicado (commit para manter cambio)
git checkout master archivo.xxx     #archivo de vuelta a su version actual


#Branching
git branch                          #listar ramas
git branch nombreRama               #crear una rama
git branch -d nombreRama            #borrar rama
git branch -D nombreRama            #forzar borrado de rama que no ha sido fusionada
git branch -v                       #último commit de cada rama
git branch --all                    #ver ramas locales y remotas (-r solo remotas)
git checkout nombreRama             #pasarme a una rama (-b crear y pasar a la rama)
git checkout -                      #volver a la rama anterior
git checkout --track _ramaremota_   #crear rama local teniendo en cuenta la rama remota
git merge branch-name               #trae todo lo de la otra rama a mi rama actual
git merge --abort                   #si hay conflicto, se solucionan y se hace commit o se aborta el merge

# Working with Remotes              #Origin. nombre servidor remoto del que cloné
git clone _url_                     #al clonar ya tengo conexión al remoto
git remote -v                       #remotos que tengo configurados (-v ver url)
git remote add origin _url_         #crear origen remoto
git remote show [remote-name]       #inspeccionar un remoto (raname, rm)
git pull origin main                #traer repo de github (fetch + merge)
git pull origin main --allow-unrelated-histories
git push origin main                #enviar repo local al github
git fetch [remote-name]             #trae actualizaciones al Repo local pero no al WD (merge)


# Public and private key             #una clave privada y pública por cada computadora y usuario
ssh-keygen -t rsa -b 4096 -C "calderon950527@gmail.com" #(id_rsa.pub publica)(id_rsa privada)(estando en el home)
eval $(ssh-agent -s)                #revisar que servidor de llaves ssh esté prendido (Agent pid 869)
ssh-add ~/.ssh/id_rsa               #agregar llave privada al entorno y debo agregarla en github
git remote set-url origin git@github.com:calderon9505/Curso_Git.git

# Tag
git tag                             #lista de tags
git tag -a v0.1 -m " " _commit_     #crear un tag
git tag -d _tag_                    #borrar tag
git show-ref --tags                 #referencias de tags
git push origin --tags              #enviar tags al remoto
git push origin :refs/tags/_tag_    #borrar tags del remoto

# Branches in Github
git show-branch
git show-branch --all               #tambien muestra ramas remotas
gitk                                #entorno gráfico para las ramas
git pull origin _branch_            #traerme rama especifica de github

# Pull request
#Pull request es una caracteristica propia de Github, no de Git
#estado intermedio antes de enviar el merge
#crear rama para hacer cambios 
#hacer push normal de la rama creada
#en github puedo hacer un pull request para hacer merge de la rama
#puedo agregar revisores (los revisores verifican el codigo y aprueban)
#el merge lo puede hacer el dueño del repositorio o los miembros 

# Fork
#Caracteristica propia de Github, no de Git
#sirve para hacer aporte a un repositorio en el que no soy miembro
#se forkea el repositorio que quiero
#se clona mi fork en mi pc local
#se hacen cambios, se hace push y se crea un pull request en github
#el dueño del repositorio puede aceptar el pull request o rechazar
#si el repo fuente cambia, mi repo(fork) se desactualiza
#entonces yo puedo crear otra fuente(remoto) para hacer pull
git remote add upstream https://github.com/calderon9505/Curso_Git.git
#tengo dos remotos: el mio y el original(upstream)
#hago pull del remoto upstream y hago push al remoto origin
#con esto mi repo fork ya está actualizado

# Deployment to Server
#en la carpeta donde están los archivos del servidor se hace un git clone
#para cualquier cambio en el github se debe hacer pull en el servidor
#En realidad esto es mala practica, pero es básico
#Travis-CI conecta las ramas de github con los servidores
#Jenkins hace los mismo que Travis pero más poderoso

# Gitignore
#Archivo oculto .gitignore
#imgur.com para subir fotos a la nube y poder refereciar externamente
#comparar con otros archivos .gitignore de otros repositorios (arduino)

# Readme.md
#Aprender del Readme de repositorios famosos
#https://pandao.github.io/editor.md/en.html

# Rebase
#reorganiza los commits de una rama al final de otra rama
#estando ubicada en la rama secundaria, realizo el rebase.
git rabase _ramaARebasar_
#luego paso a la rama principal y hago merge (fas-forward) (merge normal)

# Stash
#Cuando quiero cambiar de rama pierdo los cambios a los que NO haya hecho comit
#pero puedo enviar los cambios a Stash, y cambiar de rama sin perder los cambios
git stash                           #WIP(work in progress)
git stash list
git stash pop                       #debo volver a la rama principal y deshacer el stash
git stash branch _nuevaRama_        #para guardar los cambios del stash en una nueva rama
git stash drop                      #eliminar lo que esté en el stash
#stash es util cuando se hacen pequeños experimientos que no merecen una rama
#stash se usa mucho cuando son proyectos grandes y complejos, sin duda lo voy a usar

# Clean
git clean --dry-run                 #simular lo que se va a borrar
git clean -f                        #borrar (sin la -f no funciona)

# Cherry-pick
# añadir a la rama principal commits específicos de otra rama
git cherry-pick _codigoCommit_      # parado en la rama principal
#dicho commit se pega al final de la rama principal (automaticamente)
#los cambios no son específicamente del commit, son tambien todos los commits anteriores 

# Reflog
#todo un historial de cosas que he hecho en git, incluye:
#commits, checkouts, amends, resets.... se muestra TODOS el historial

# Grep
git grep _palabra_                  #busca en los archivos la palabra 
                                    #(-n ver linea, -c count)
git log -S _palabra_                #relacion de la palabra con commit

# Alias interesantes
git shortlog -sn --all --no-merges  #contar todos commits de todas personas 
                                    #(incluso commits borrados pero no merge)
git blame archivo.xxx -L35,42 -c    #ver quien escribio cada linea (de la 35 a 42)