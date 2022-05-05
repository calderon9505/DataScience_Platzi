# Apache Spark

[Primeros pasos en ingenieria de datos con Apache Spark. SPARK MEXICO](https://www.youtube.com/watch?v=0rKrDGS2gkA&ab_channel=SparkMexico)

[Spark Study Group. DATA ENGINEERING LATAM](https://www.youtube.com/playlist?list=PLdxuOh58KNA6CH3sQS6zhuIVKoPllmXiB)

[Ultimate Guide for Setting up PySpark in Google Colab. MEDIUM](https://medium.com/analytics-vidhya/ultimate-guide-for-setting-up-pyspark-in-google-colab-7637f697daf1)

[Spark en Deepnote](https://docs.deepnote.com/integrations/spark)

[Spark by {examples}](https://sparkbyexamples.com/)

Spark es un **framework** de desarrollo de procesos de Big Data enfocado en la velocidad del proceso, esto lo logra con un procesamiento de datos desde la memoria RAM y con procesamiento distribuido usando paralelización.

Apache Spark es un motor de procesamiento analítico de código abierto para potentes aplicaiones de ML y procesamiento de datos distribuidos a gran escala.

Es tolerante a fallos, con estructuras de datos inmutables y de evaluación perezosa (el código corre con las funciones de **acción**, pero no con las funciones de **transformación**)

Spark maneja arquitectura *master-slave* (**Driver-Worker**). Cuando ejecuto una aplicación Spark, el **Driver** crea un contexto que es un **entry point** a la aplicación, y todas las operaciones (transformaciones y acciones) son ejecutadas en los nodos **Worker**, y los recursos son administrados por el **Cluster Manager**

![](https://i0.wp.com/sparkbyexamples.com/wp-content/uploads/2020/02/spark-cluster-overview.png?w=596&ssl=1)

## RDD

> Es el lenguaje ensamblador que posee Spark.

[Spark RDD Tutorial](https://sparkbyexamples.com/spark-rdd-tutorial/)

Resilient Distributed Dataset. Se trata de datasets tolerantes a fallos, inmutables y capaces de operar en paralelo. los RDD son ejecutados en varias JVM en multiples servidores físicos tambien llamados **nodos**. 

Es una de las dos principales estructuras que soporta Spark (Aunque realmente los RDD no poseen estrucuta estrictamente). Los RDD son el componente mínimo con el cual podemos comunicarnos con Spark. Son la principal **abstracción de datos**.

Los RDD distribuyen y particionan los datos para correr los cómputos en parelelo en varios nodos. Mientras se realizan transformaciones sobre el RDD la mayoría del tiempo no nos procupamos por el paralelismo, ya que Spark lo provee por defecto. 

La ejecución es **perezosa**. Hasta no ejecutar una acción, el código no corre. Aquí se muestran entonces las acciones y las transformaciones.

Transformaciones | Acciones
---------------- | --------
orderBy() | show()
groupBy() | take()
filter() | count()
select() | collect()
join() | save()

* Los RDD me permiten controlar el flujo de Spark
* Permite mejor control de datos desde Python
* Son la única opción en versiones antiguas de Spark

El objetivo de RDD es proveer un modelo de programacion por lotes(batch) eficiente.

## DataFrame

> Capa superior sobre los RDD

Los DataFrame poseen estructura (es decir, columnas con tipos de datos). Los DataFrame poseen una mejor implementación, lo cual los hace preferibles en optimización.

Se pueden crear desde un database externo, archivo o desde un RDD existente.

* Los DF son útiles en instrucciones complicadas
* Son mejores en tareas de alto nivel (filtros, mapeos, agregaciones, promedios, sumas ...)
* Para sentencias SQL-like

# Instalación

En WSL2

```
sudo apt-get update && sudo apt-get upgrade -y
```

Para usar Spark se necesita instalar Java 8, Python3, pip3, Scala y Spark. 

## Java

```
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt-get -y install openjdk-8-jre
```

## Scala

```
sudo apt-get -y install scala
```

## Spark

[Download Apache Spark](https://spark.apache.org/downloads.html)

ubicado en el home

```
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
tar -xvf spark-3.2.1-bin-hadoop3.2.tgz
rm spark-3.2.1-bin-hadoop3.2.tgz
mv spark-3.2.1-bin-hadoop3.2 spark
```

## venv

He creado un ambiente virtual llamado `spark-env`.

He creado un alias para activar el venv: `act-spark-env`

## paquete py4j

He instalado py4j en el venv creado

```
pip3 install py4j==0.10.9.3
```

esto debido a ERROR: pyspark 3.2.1 has requirement py4j==0.10.9.3, but you'll have py4j 0.10.9.5 which is incompatible.

## Variables de entorno

Al final del archivo `.bashrc`

```
## Path de Java
export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
export PATH=$JAVA_HOME:$PATH

## Spark
export SPARK_HOME='/home/calderon/spark'
export PATH=$SPARK_HOME:$PATH

## Python para ser utilizable por Spark
export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
export PYSPARK_PYTHON=python3
```

Ejecutar `bash` para activar los cambios de `.bashrc`

## Ejecutar Spark en la terminal

Ingresando a la carpeta `spark` ejecutar el comando `pyspark`

---

Para ejecutar código de spark se usa `spark/bin/pyspark`.

Para ejecutar código de python se usa `spark/bin/spark-submit`.

Descargué los archivos de ejemplo y los guardé en una carpeta llamada spark-codigos.

```
../spark/bin/spark-submit codeExample.py data.csv
```

La ejecución desde la terminal se usa principalmente para ejecutar códigos probados y listos para entrar en producción. Para ambientes de pruebas se usan los Jupyter notebooks.

Creé un archivo `ejemplo1.ipynb` y lo abrí con VSCode, el cual se encarga de instalar lo necesario para usarlo.



python3 -m venv spark-env-scala

source spark-env-scala/bin/activate

pip3 install spylon-kernel

 rm -r spark-env-scala/