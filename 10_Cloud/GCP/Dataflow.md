# Dataflow

[Introducción a Dataflow](https://www.youtube.com/watch?v=Bo8ztVTWWA8&ab_channel=GoogleCloudTech)
[Escribiendo tu primer flujo de datos](https://www.youtube.com/watch?v=bGA3QwpF4SU&ab_channel=GoogleCloudTech)

Servicio **unificado** de procesamiento streaming y batch, totalmente administrado, con modelo de programación de código abierto y con capacidad de escalar inteligentemente a millones de operaciones por segundo.

Cuando se tiene procesamiento streaming se obtienen resultados inmediatos pero no tan precisos. Cuando se tiene procesamiento batch se obtienen resultados más precisos pero más lentos. De aquí surge la arquitectura Lambda

## Arquitectura Lambda

Arquitectura donde se tiene tanto procesamiento en streaming como batch. Pero, aquí no se tienen dos flujos distintos (streaming y batch), sino que se tiene un *modelo de datos unificado*.

Para esto se usa el SDK de Apache Beam, en donde se define un flujo de datos; se puede emitir resultados rápidamente (antes de que los datos estén completos), y se encarga de que los datos que lleguen tarde vuelvan a se calculados para tener resultados completos y precisos.

Los flujos de datos son portables. Se pueden ejecutar en Spark, Flink o en Dataflow.

# Conceptos

## Pipelines (flujos de procesamiento)

Encapsulan toda la tarea de procesamiento de principio a fin. Es decir, todo el proceso ETL.

## PCollection (Contenedor de datos ilimitado e inmutable)

Conjunto de datos que procesará. Es ilimitado en el sentido que se lee de una fuente de datos que se actualiza continuamente (e.g. Pub/Sub o Kafka). Son inmutable, por lo que al operar con ellos se creará otro PCollection con los datos modificados.

## PTransform (cambio de datos)

Toman una PCollection, procesan los datos, y entregan cero, una o más PCollection.

## I/O transforms

Leer y escribir en distintos sistemas.


# El "Stack"

* **Flujo de datos** final.
* **Bibliotecas**. Transformaciones, fuentes/destinos, etc.
* **SDK específico del lenguaje**. Java, Python, etc.
* **Modelo Beam**. ParDo, GBK, Windowing.
* **Ejecutor**. Dataflow, Spark, Apache Flink.
* **Entorno de ejecución**. Nube, On premise, local.

Apache Beam se involucra en el SDK, el Modelo Beam y el Ejecutor.


# Laboratorio

En este laboratorio se crea una canalización en Dataflow con Python

1. Habilitar las API necesarias

    - Dataflow API
    - Compute Engine API
    - Cloud Logging API
    - Cloud Storage
    - Google Cloud Storage JSON API
    - BigQuery API
    - Cloud Pub/Sub API
    - Cloud Datastore API
    - Cloud Resource Manager API

1. Crear permisos en IAM al **Compute Engine default service account**

    - Dataflow > Trabajador
    - Dataflow > Administrador
    - Cloud Storage > Administrador de objetos de almacenamiento

1. El SDK de Apache Beam solo es compatible con Python 3.8. Sin embargo, Cloud Shell ejecuta Python 3.9. Para solucionar esto, instala `pyenv`. Ignora la advertencia sobre la ruta de carga 


# Curso

[Apache Beam Python SDK Quickstart](https://www.youtube.com/watch?v=xSgTsKWhU0Y&ab_channel=SoftwareGuru)

[Paso a paso para nuestro primer pipeline con Apache Beam y Dataflow](https://beam.apache.org/get-started/quickstart-py/)

Crear archivo main
crear ambiente virtual y activarlo

```sh
cd .\10_Cloud\GCP\Dataflow\
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\activate
```

```sh
pip install apache-beam
pip install 'apache-beam[gcp]'
```

para ejecutar el código en local. el comando `--runner DirectRunner` creo que indica que es en local, pero no es necesario.

```sh
py main.py --n-palabras 500 --entrada el_quijote.txt --salida output.csv
```

El mismo código se puede ejecutar tanto en Spark, Flink o Dataflow.

Para ejecutar en Dataflow

```sh
gcloud config set ace-thought-348115
gcloud config set account calderon950527@gmail.com
gcloud auth login
gsutil cp .\el_quijote.txt gs://test_my_first_dataflow/
```

```sh
py main.py --n-palabras 500 --entrada gs://test_my_first_dataflow/el_quijote.txt --salida gs://test_my_first_dataflow/output.csv --runner DataflowRunner --project ace-thought-348115 --region us-east1 --temp_location gs://test_my_first_dataflow/tmp/
```