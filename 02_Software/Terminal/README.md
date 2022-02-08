# PREWORK

## Instalación de WSL

- Activar la virtualización en la BIOS
- Abrir un Powershell con permisos de administrador
- $ wsl --install
- $ wsl -l -v
- $ wsl --version
- ya no es necesario nada más.
- Instalar Windows Terminal (opcional)
- sudo apt-get -y install python3-pip

## Instalacion VSCode

- Activar sincronización de extensiones
- export as pdf, python script y HTML.

### extensiones

- Remote - WSL
- Python
- Rainbow Brackets
- Remote Development
- Visual Studio IntelliCode
- Material Icon
- Jupyter

## Instalación Anaconda

- se obtiene el enlace de la página https://www.anaconda.com/products/individual
$ wget -O anaconda.sh https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
$ bash anaconda.sh
$ conda info
$ jupyter-notebook

### Conda

$ conda env list
$ conda create --name [name] python=3.5 pandas
$ conda activate env_name
$ conda deactivate
$ conda list
$ conda list pandas
$ conda update pandas
$ conda install python=3.9 pandas=1.2
$ conda create --name [name] --copy --clone [name]
$ conda remove pandas
$ conda env remove --name [name]

$ conda install --channel conda-forge boltons (-c)
$ conda list --revision
$ conda install --revision 0
$ conda env export
$ conda env export --no-builds
$ conda env export --from-history --file enviroment.yml
$ conda env create --file enviroment.yml

- ajustar siempre el ambiente(kernel) en VSCode

## Mamba

https://labs.epi2me.io/conda-or-mamba-for-production/

## Snakemake

Un mismo proyecto con varios ambientes
así el modificar un paquete se modifica solo para
una sección del proyecto
Etapas de proyectos basadas en python
Divide y vencerás
Mamba permite acelerar la creación de ambientes 
virtuales a través de la descarga paralela de datos y paquetes.