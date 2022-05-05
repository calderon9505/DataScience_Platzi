# Curso Big Data con Python y Spark - De Cero a Heroe

Instalación de todo el entorno necesario para usar SPARK en Windows (no funcionó)

## Anaconda

Descargar e instalar Anaconda

He creado ambiente virtual con Python 3.8 llamado `bigdata`. Puedo activar el ambiente desde el cmd con `activate bigdata`.

## Java

Descargar el JDK. En este caso version 8u321. instalar en `C:\jdk\`

Descargar el JRE. En este caso version 8u321. instalar en `C:\jre\`

## Spark

Descargar Spark la version más reciente. Spark 3.2.1.

Descomprimir archivos y guardar en `C:\spark\`

Renombrar archivo `conf\lo4j.properties.template` por `conf\lo4j.properties`. Cambiar linea 19 de `log4j.rootCategory=INFO, console` por `log4j.rootCategory=ERROR, console`.

## winutils

Descargar de `https://github.com/steveloughran/winutils/blob/master/hadoop-2.7.1/bin/winutils.exe`.

Guardar en `C:\winutils\bin\`

## Enviroment variables

Crear nuevas variables de entorno

`SPARK_HOME` -> `C:\spark`
`JAVA_HOME` -> `C:\jdk`
`SPARK_HOME` -> `C:\spark`

editar la variable de entorno **Path** y agregar

`%SPARK_HOME%\bin`
`%JAVA_HOME%\bin`

