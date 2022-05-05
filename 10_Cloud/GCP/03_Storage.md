# Cloud Storage

## Crear bucket desde el Cloud Shell

Existe una variable de entorno que almacena mi Project ID

```sh
echo $DEVSHELL_PROJECT_ID
or
echo $GOOGLE_CLOUD_PROJECT
```

Procedo a crear el bucket (mb: make bucket)

```sh
LOCATION=US
export LOCATION=US #another option to enviroment variables
gsutil mb -l $LOCATION gs://$DEVSHELL_PROJECT_ID

# or
gsutil mb gs://<BUCKET_NAME>
```

Ahora cargo una imagen desde un sitio público en Cloud Storage a mi bucket
```sh
gsutil cp gs://cloud-training/gcpfci/my-excellent-blog.png my-excellent-blog.png
gsutil cp my-excellent-blog.png gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png
```

permitir que cualquier pueda leer el objeto(la imagen) (acl: access control list)

```sh
gsutil acl ch -u allUsers:R gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png
```


# Cloud SQL

## Crear RDB desde la consola

> **SQL** > **Create instance** > **MySQL**




# `gsutil` commands

gsutil es una aplicación de Python que te permite acceder a **Cloud Storage** desde la línea de comandos. Puedes usar gsutil para realizar las siguientes tareas de administración de objetos y depósitos:

- Crear y borrar depósitos.
- Subir, descargar y borrar objetos
- Crear listas de depósitos y objetos
- Mover, copiar y cambiar nombres de objetos
- Editar LCA de objetos y depósitos