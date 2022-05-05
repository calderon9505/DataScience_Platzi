# Compute Engine

In this lab, you will create virtual machines (VMs) and connect to them. You will also create connections between the instances.

## Crear VM desde la consola

> **Compute Engine** > **VM instances** > **create instance**

El nombre de la VM es **my-vm-1**. Permitir trafico HTTP. Esta VM se crea en **us-central1-a**

## Crear VM desde el Cloud Shell

Definir default zone

```
gcloud config set compute/zone us-central1-b
```

Crear VM **my-vm-2**

```
gcloud compute instances create "my-vm-2" \
--machine-type "n1-standard-1" \
--image-project "debian-cloud" \
--image-family "debian-10" \
--subnet "default"
```

En este momento tengo dos VM en distintas zonas, pero la misma región.

## Conectar las instancias

Conectarme por SSH a **my-vm-2** (desde consola).

Luego, hacer ping a la VM 1

```
ping my-vm-1.us-central1-a
```

Conectarme por ssh a VM

```
ssh my-vm-1.us-central1-a
```

# App Engine

Inicializar un App Engine

```
gcloud app create --project=$DEVSHELL_PROJECT_ID
```

Crear proyecto **hello_world**

```sh
git clone https://github.com/GoogleCloudPlatform/python-docs-samples
cd python-docs-samples/appengine/standard_python3/hello_world
```

Crear archivo llamado ``Dockerfile``

```
FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install gunicorn
RUN pip install -r requirements.txt
ENV PORT=8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app
```

crear contenedor y correr aplicación. Pero presionar `ctrl + c` para abortar el despliegue.

```
docker build -t test-python . 
docker run --rm -p 8080:8080 test-python 
```

para desplegar usando el App Engine

```
cd ~/python-docs-samples/appengine/standard_python3/hello_world
gcloud app deploy
gcloud app browse
```


# `gcloud` commands

El grupo de comandos **gcloud** permite administar los recursos de **Compute Engine**

para listar las cuentas activas
```
gcloud auth list
```

para listar la configuración del proyecto
```
gcloud config list
gcloud config list project
```

para cambiar el proyecto al que apunta el Cloud Shell
```
gcloud config set <PROJECT_ID>
```

Propiedades predeterminadas de mi VM
```
gcloud compute project-info describe --project <PROJECT_ID>
```

Para ver la region/zona predeterminada

```
gcloud config get-value compute/region
gcloud config get-value compute/zone
```

Para listar regiones/zonas disponibles

```
gcloud compute regions list
gcloud compute zones list
gcloud compute zones list | grep us
```

Los comandos `gcloud compute` requieren marcas para `--region` o `--zone`. Se puede establecer una región o zona *predeterminada* y así evitar el uso de las marcas. Si a un comando se le pasa marca de región/zona, se anulan la region/zona predeterminada. 

La región/zona predeterminada se puede hacer de tres maneras(cada una sobreescribe la otra):
- En el servidor de metadatos
- En el cliente local
- En las variables de entorno

Para establecer region/zona en el cliente local

```
gcloud config set compute/region REGION
gcloud config set compute/zone ZONE
```

Para listar las instancias

```
gcloud compute instances list
```