# BASES DE DATOS EN LA VIDA REAL

[Uber’s Big Data Platform: 100+ Petabytes with Minute Latency](https://eng.uber.com/uber-big-data-platform/)


# Big Data

Necesidad de almacenar grandes cantidades de datos de diferentes fuentes de manera rápida.

* **Volumen**. Las organizaciones recopilan datos de diversas fuentes, incluyendo transacciones comerciales, medios sociales e información de sensores o que se transmite de una máquina a otra. En el pasado, almacenarlos habría sido un problema – pero nuevas tecnologías (como Hadoop) han aligerado la tarea.

* **Velocidad**. Los datos se transmiten a una velocidad sin precedentes y se deben distribuir de manera oportuna. Etiquetas FID, sensores y la medición inteligente crean la necesidad de distribuir torrentes de datos casi en tiempo real.

* **Variedad**. Los datos vienen en toda clase de formatos – desde datos numéricos estructurados en bases de datos tradicionales hasta documentos de texto no estructurados, correo electrónico, video, audio, datos de teletipo bursátil y transacciones financieras. Los datos de la actualidad provienen de múltiples fuentes, lo que hace difícil vincular, empatar, depurar y transformar datos entre diferentes sistemas. Sin embargo, es necesario conectar y correlacionar relaciones, jerarquías y múltiples vínculos de datos o sus datos se pueden salir de control en un segundo.

* **Veracidad**. Conocer qué datos son veraces.


# Data Warehouse

[Data Warehouse: todo lo que necesitas saber sobre almacenamiento de datos](https://www.powerdata.es/data-warehouse)

Grandes almacenes(depósitos) de datos. No son para grandes transacciones de datos sino para almacenar "datos muertos" en enormes cantidades. No es muy bueno para hacer muchas consultas.

Es el repositorio central de la información de la empresa que integra los datos de todas las áreas o departamentos de esta. Los Data Warehouse almacenan información histórica de la empresa por lo tanto es muy útil para generar informes de tendencia en los que se muestra la información año tras año.

La información ingresada al Data Warehouse debe pasar por el proceso ETL, ya que debe ser información íntegra y limpia. Esto quiere decir que la información que se puede obtener de un Data Warehouse es información fidedigna y confiable para la toma de decisión.

Entre las desventajas de un Data Warehouse están:
* Su elevado costo de implementación y mantención
* Es solo aplicable a grandes empresas, ya que el esfuerzo de crear un Data Warehouse sería muy superior a los beneficios obtenidos.

DW no es un producto que pueda ser comprado en el mercado, sino más bien un concepto que debe ser construido. DW es una combinación de conceptos y tecnología que cambian significativamente la manera en que es entregada la información a la gente de negocios. El objetivo principal es satisfacer los requerimientos de información internos de la empresa para una mejor gestión, con eficiencia y facilidad de acceso.


# Data mining

> Data mining, consiste en torturar los datos hasta que confiesen

Data Mining o Knowledge Discovery in Databases (KDD) consiste en extraer información de un conjunto de datos y transformarla en una estructura comprensible, esto es, en información útil y accesible para que pueda ser usada posteriormente.

Cuando se tiene gran cantidad de datos pero que no están guardados de forma correcta se recurre al Data Mining. Consiste en extraer los datos de donde sea que estén, transformarlos para darles un sentido y guardarlos de forma aprovechable.


# ETL

[¿Qué son los procesos ETL? Conócelos a fondo](https://platzi.com/blog/que-es-un-etl/?utm_source=google&utm_medium=cpc&utm_campaign=12915366154&utm_adgroup=&utm_content=&gclid=CjwKCAiA1uKMBhAGEiwAxzvX9786MIdKaKdby20AXhRHRCpvRU8_A56yDPfI4kFnGHPDPObjLKWHeRoCnboQAvD_BwE&gclsrc=aw.ds)

> Extract, Transform and Load.

consiste en *Extraer* los datos crudos desde su origen (Source), *Transformarlos* según nuestras necesidades de analítica y *Cargarlos* a una base de datos orientada a procesos analíticos (Target).

## **Extract**

Extracción de datos que pueden venir de distintas fuentes y en distintos formatos. El éxito de una buena extracción es que cause el menor impacto en el origen de los datos.

## **Transform**

* Filtrar filas por ciertas características.
* Eliminar duplicados.
* Transformar datos (i.e. Colombia -> 1, México -> 2, etc...).
* Calcular datos nuevos (i.e. obtener edad a partir de fehca de nacimiento).
* Agrupar datos (máximos, mínimos, promedios, conteos, etc...).
* Unir o combinar datos de distintas fuentes.
* Pivotar las tablas.
* Dividir columnas (nombre completo dividirlos en sus partes).

Las transformaciones no se realizan ni en el "source" ni en el "target" sino en el area de "staging", un repositorio temporal.

## **Load**

Carga de datos en la base de datos de analítica (comunmente un Data Warehouse)


# Business Intelligence

[¿Qué es Inteligencia de Negocio o Business Intelligence?](https://platzi.com/blog/que-es-bi-business-intelligence/?utm_source=google&utm_medium=cpc&utm_campaign=12915366154&utm_adgroup=&utm_content=&gclid=CjwKCAiA1uKMBhAGEiwAxzvX90hKJp7-7kPkejDA1r6WYS8gC1iGk5Fizgom5ppPuqJzNmg9JjpLkBoCCx8QAvD_BwE&gclsrc=aw.ds)

La inteligencia del negocio es tener la información de manera oportuna y clara para que la empresa pueda tomar las decisiones adecuadas.

BI son las prácticas, herramientas o métodos que las empresas utilizan para observar, analizar y comprender todos los datos que tienen relación con su modelo de negocio u organización.

El BI contribuye en el análisis de los datos históricos, actuales y predicciones, esto con el propósito de mejorar las decisiones y por lo tanto, ser más competitivos y rentables como empresa.

En cuanto a estos datos que tanto se mencionan en BI, surge la pregunta respecto a las fuentes de las que se obtienen, algunas de ellas pueden ser:
* CRM (Customer Relationship Management).
* ERP (Enterprise Resource Planning).
* Sitio web
* SCM (Supply Chain Management)

![](https://static.platzi.com/media/user_upload/etl-processes-da196ddc-5707-4a58-93fe-ea074ab4df73.jpg)

# Machine Learning

Es el tratamiento de datos para entrenar modelos que encuentren patrones en los datos. Sus principales usos son en *clasificación* y *predicción*.