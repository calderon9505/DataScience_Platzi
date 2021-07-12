# https://git-scm.com/book/en/v2
# https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
# https://danielkummer.github.io/git-flow-cheatsheet/
shift + Ins                         #para pegar codigo en terminal Git bash (Insert)


# GIT Configuration
git init                            #crea repositorio
git config                          #todas las configuraciones de Git
git config --list                   #configuracion actual de Git
git config --list --show-origin     #origen del archivo gitconfig(avanzado)
git config --global user.name "Sebastian Calderon"
git config --global user.email "calderon950527@gmail.com"
git config --global core.editor "code --wait"


# First steps
git add archivo.xxx                 #añade archivo al Staging Area (ram)
git commit -m " "                   #envia el archivo al repositorio
git commit -am " "                  #-a saltarse el add; (-ma no sirve)
git status                          #estado de los archivos
git status -s (--short)             #estado conciso de los archivos
                                    #left-staged; right-unstaged
                                    #??-untracked; A-staged(nuevo); M-modified


# Commit history and comparations
git show archivo.xxx                #historial de cambios del archivo (git show)
git log archivo.xxx                 #historial del archivo (git log)
git log -p -2                       #-p diferencias introduc. -2 solo dos commits
git log --stat                      #archivos en que se hicieron cambios por commit
git log --pretty=oneline            #cada commit es una linea (short, full, fuller)
git log --graph                     #grafico ASCII muestra historial (usar con oneline)
git log --since=" "                 #(2.weeks)("2008-01-15")("2 years 1 day 3 minutes ago")
git log --author " " --grep " " --all-match
git diff old_code new_code          #comparar versiones de commit
git diff                            #Working directory vs Repositorio
git diff --staged (--cached)        #staging Area vs Repositorio


# Undoing Things
git restore archivo.xxx             #discard changes in working directory
git restore --staged archivo.xxx    #unstage. back to working directory
git commit --amend                  #rehacer commit adicionando lo que esté en staging
git reset old_code --soft           #version anterior pero manteniendo el staging
git reset old_code --hard           #version anterior borrando todo los demás commits


git checkout old_code archivo.xxx   #puedo revisar el archivo en su commit especificado
git checkout master archivo.xxx     #vuelo a tener el archivo del ultimo commit


# Traer cambios del repositorio
checkout                            #


# Branch


# Merge


# Clone
git clone https://github.com/calderon9505/DataScience_Platzi.git


# Ignore
cat .gitignore                      #lista de archivos o patrones a considerar (*.ini)