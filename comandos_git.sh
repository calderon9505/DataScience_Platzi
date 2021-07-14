# https://git-scm.com/book/en/v2
# https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
# https://danielkummer.github.io/git-flow-cheatsheet/
# https://learngitbranching.js.org/

shift + Ins                         #para pegar codigo en terminal Git bash (Insert)
cat .gitignore                      #lista de archivos o patrones a ignorar (*.ini)
git branch -M main                  #nombrar la rama como "main"


# GIT Configuration
git init                            #crea repositorio
git clone _url_                     #clonar repositorio existente
git config                          #todas las configuraciones de Git
git config --list                   #configuracion actual de Git
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


# Commit history and comparations   #HEAD. apuntador a la rama local en al que estoy
git show archivo.xxx                #historial de cambios del archivo (git show, ultimo cambio)
git log archivo.xxx                 #historial del archivo (git log)
git log -p -2                       #-p diferencias introduc. -2 solo dos commits
git log --stat                      #archivos en que se hicieron cambios por commit
git log --pretty=oneline            #cada commit es una linea (short, full, fuller)
git log --graph                     #grafico ASCII muestra historial (usar con oneline)
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
git brach nombreRama                #crear una rama
git brach -b nombreRama             #borrar rama
git checkout nombreRama             #pasarme a una rama (-b crear y pasar a la rama)
git merge branch-name               #trae todo lo de la otra rama a mi rama actual
                                    #si hay conflicto, se solucionan y se hace commit


# Working with Remotes              #Origin. nombre servidor remoto del que cloné
git clone _url_                     #al clonar ya tengo conexión al remoto
git remote -v                       #remotos que tengo configurados (-v ver url)
git remote add origin _url_         #crear origen remoto
git remote show [remote-name]       #inspeccionar un remoto (raname, rm)
git pull origin main                #traer repo de github (fetch + merge)
git pull origin main --allow-unrelated-histories
git push origin main                #enviar repo local al github
git fetch [remote-name]             #trae actualizaciones al Repo local pero no al WD (merge)


