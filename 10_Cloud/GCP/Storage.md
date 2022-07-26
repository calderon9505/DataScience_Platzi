# ALMACENAMIENTO EN GCP


![](https://1.bp.blogspot.com/-H4a0slANRLg/XXFGsDshuKI/AAAAAAAAAAU/Ov1pyV1IOqQJvSfTJy50eL6dGCrCBHk-wCLcBGAs/s1600/storageoptions.jpg)










![](https://static.platzi.com/media/user_upload/Screenshot_26-ff620129-2ba2-4c0f-aa8e-78aa6f91cfab.jpg)








# CLOUD STORAGE (GCS)

Es un servicio de almacenamiento de objetos. un objeto es una pieza de datos inmutable identificada por un nombre de objeto.

La seguridad se maneja con
- Control de acceso y autenticación con IAM
- Cifrado de datos en reposo y en transito
- Reglas de retención. Evitar que un archivo sea borrado o actualizado por cierto tiempo.
- Control de versiones disponible.
- LLaves de cifrado automáticas(default), gestionadas(CMEK) o personalizadas(CSEK).

Un bucket y los objetos que almacena pueden estar ubicados en una o multiples regiones.

## Ubicación

- **Regional**. Se almacena en una región específica (por ejemplo us-east1).
- **Dual-region**. Los objetos se almacenan en dos regiones distintas de forma redundante.
- **Multi-region**. Los objetos se almacenan en más de dos regiones pero solo es redundante en dos regiones. (objeto 1 se guarda en region A y B. objeto 1 se guarda en region A y C.)

El territorio hace referencia a:
- United States
- Europe Union
- Asia
- South America

## Clases

- **Standard**: Acceso muy frecuentemente (más caro).
- **Nearline**: Acceso una vez al mes.
- **Coldline**: Acceso una vez al trimestre.
- **Archive**: Acceso una vez al año.

# `gsutil` commands

gsutil es una aplicación de Python que te permite acceder a **Cloud Storage** desde la línea de comandos. Puedes usar gsutil para realizar las siguientes tareas de administración de objetos y depósitos:

- Crear y borrar depósitos.
- Subir, descargar y borrar objetos
- Crear listas de depósitos y objetos
- Mover, copiar y cambiar nombres de objetos
- Editar LCA de objetos y depósitos



## Crear bucket desde el Cloud Shell

Para listar los **buckets** que tiene el proyecto
```sh
gsutil ls
```

Crear un bucket (mb: make bucket)
```sh
gsutil mb gs://<BUCKET_NAME>
```

Para listar los **objetos** que tiene el proyecto
```sh
gsutil ls gs://<BUCKET_NAME>
```

Crear bucket con más detalles (territorio `-l`, clase `-c`, politica acceso publico `--pap`, acceso uniforme con IAM `-b`, retención `--retencion`)

```sh
LOCATION=US
gsutil mb -c standard -l $LOCATION --pap enforced -b on --retention 10y gs://$DEVSHELL_PROJECT_ID
```



Ahora copio una imagen desde un sitio público en Cloud Storage a mi Cloud Shell, y de mi Cloud Shell a mi bucket.
```sh
gsutil cp gs://route/to/file.txt .
gsutil cp file.txt gs://$DEVSHELL_PROJECT_ID/file.txt
```

[Use Object Versioning](https://cloud.google.com/storage/docs/using-object-versioning#gsutil)

permitir que cualquier pueda leer el objeto(la imagen) (acl: access control list)

```sh
gsutil acl ch -u allUsers:R gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png
```


# CLOUD SQL

Servicio de base de datos **SQL** completamente administrado. Garantiza transacciones ACID. Ayuda a realizar réplicas y Copias de seguridad.

> Se puede escalar verticalmente.

Las migraciones a Cloud SQL son sencillas gracias a **Database Migration Service.**

Cloud SQL se usa cuando se tienen usuarios en una región específica, y donde la latencia no sea un gran problema.

Este es el único servicio basado en VMs.



# CLOUD SPANNER

Otro servicio de base de datos **SQL** completamente administrado con transacciones ACID. Es de nivel empresarial (y global). 

A diferencia de Cloud SQL, Cloud Spanner tiene muy baja latencia, y se usa para aplicaciones que requieren presencia a nivel mundial.

> Se puede escalar horizontalmente.

Cuando el número de solicitudes es alto o el volumen de datos es alto, Cloud Spanner se fragmenta automáticamente, es decir, distribuye la carga para evitar que se caiga el sistema.

En Cloud Spanner se tienen instancias, cada instancia puede tener muchas bases de datos. y cada base de datos puede tener muchas tablas.





# CLOUD BIGTABLE

Servicio de base de datos **NoSQL** de tipo *clave-valor* completamente administrado.

Las BBDD NoSQL como Bigtable se usan principalmente cuando se tiene crecimiento acelerado, picos de usuarios no previstos o para usar varios servidores de datos.

Bigtable tiene procesamiento de baja latencia, alta capacidad, cambio de tamaño sin tiempo de inactividad

Para interactuar con BigTable se puede usar la API de aplicación, Streaming o Batch Processing.

En las BBDD NoSQL no es necesario el uso de tablas, pues la información se puede almacenar en documentos. Pero, BigTable sí almacena en una tabla. 
- Las columnas (con relación entre sí) se agrupan en familias `column-familys`. 
- Cada columna dentro del column-family se llama `column-qualifiers`
- Los registros (filas) tienen un identificador(llave) `row-keys`.
- La intersección entre column-qualifier y row-key se llama `cells`
- Se pueden tener múltiples registros en las celdas

```sh
echo project = `gcloud config get-value project` > ~/.cbtrc
echo instance = my-instance >> ~/.cbtrc

# create table
create table my-table
cbt ls
# create column family
cbt createfamily my-table my-family
cbt ls my-table
# create row key and column qualifier
# create cell
cbt set my-table my-row-key my-family:my-column=my-cell

# read table
cbt read my-table
```





# CLOUD FIRESTORE

Base de datos **NoSQL** basada en documentos. 

> ideal para aplicaciones web, móviles y de servidor

- Serverless. 
- Real time (web y movil muestran los mismos datos)
- "Offline" support
- Escalable
- Transaccional

Un documento es equivalente a un registro.

una colección es equivalente a una tabla

Casos de uso:
- perfiles de usuario
- inventario en tiempo real
- gestion de sesiones de usuario
- cambio de estado
- sincronización de datos

Firestore tiene dos modos:
- Native mode
- Datastore mode

---
---

# BigQuery

- Data warehouse totalmente administrado y serverless.
- Escala a petabytes y baja latencia
- Disponible en multiples regiones
- Separa almacenamiento y cómputo
- Posee librerias para ML
- Se puede conectar con Sheets de Google
