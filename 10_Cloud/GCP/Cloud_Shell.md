# Cloud Shell

It is a browser-based interactive shell(CLI) enviroment for GCP that you can access from the GCP console.

Cloud Shell is a **temporary Virtual Machine** with 5 GB of persistent disk storage that has the **Cloud SDK pre-installed**. It has built-in authorization for access to resources and instances.

It is similar to the **gcloud command line** tool, which is whitin the Cloud SDK. The Google Cloud SDK provides the commands to manage the resources. Some commands are:

- `gcloud`
- `gsutil`
- `bq`
- `kubectl`


# Variables de entorno

Para ver la variable de entorno

```sh
echo $<ENVIROMENT_VARIABLE>
```

Project ID

```sh
$DEVSHELL_PROJECT_ID    # Opcion 1
$GOOGLE_CLOUD_PROJECT   # Opcion 2
```

Para crear mi propia variable de entorno

```sh
LOCATION=US         # Opcion 1
export LOCATION=US  # Opcion 2
```

Para crear variables de entorno que no desaparezcan al cerrar el Shell

```sh
mkdir infraclass
touch infraclass/config
echo INFRACLASS_REGION=$INFRACLASS_REGION >> ~/infraclass/config
echo INFRACLASS_PROJECT_ID=$DEVSHELL_PROJECT_ID >> ~/infraclass/config
cat ~/infraclass/config
```
```sh
nano .profile

# at the end of the file
source infraclass/config
```

# `gcloud` commands

Listar las cuentas activas
```
gcloud auth list
```

Cambiar proyecto al que apunta el Shell
```
gcloud config set project <PROJECT_ID>
```

Autenticarse con una nueva cuenta
```
gcloud config set account <ACCOUNT>
gcloud auth login
```

Configuraciones del proyecto
```
gcloud config list

gcloud config list project
gcloud config list account

gcloud config get-value compute/region
gcloud config get-value compute/zone
```


Propiedades de mi proyecto
```
gcloud compute project-info describe
gcloud compute project-info describe --project <PROJECT_ID>
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
gcloud config set compute/region <REGION>
gcloud config set compute/zone <ZONE>
```

Para listar las instancias

```
gcloud compute instances list
```