# Bases de datos no relacionales

No es un solo tipo de bases de datos, pero todas se engloban en la categoría de No Relacionales.

Surgieron como una respuesta a la necesidad de poder recuperar y escribir grandes volúmenes de información de una manera rápida.

Las bases de datos no relacionales son un conjunto de soluciones enfocadas en resolver el problema de la *disponibilidad* y la *estabilidad* en detrimento de la *consistencia* y la *atomicidad*.

## Tipos

* **Clave-valor**

*Cassandra*(Facebook), *DynamoDB*(AWS)

Guardan la información y la acceden utilizando un hash map que vincula un conjunto de datos a una clave.

Son rápidas para acceder a datos si conocemos su hash y excepcionales para manejar diccionarios pero no son recomendables para querys complejas.

* **Basadas en documentos**

*MongoDB*, *Firestore*(Google)

Son las más utilizadas fuera del estándar SQL. Son, básicamente, una implementación de las bases clave-valor pero con una estructura mas definida ya que almacenan los datos como objetos de tipo JSON.

Son ideales para guardar el estado actual de una aplicación y restaurarlo con facilidad pero no responden muy bien a búsquedas y ordenamientos.

Están optimizadas para mantener el estado de la aplicación, no tanto para hacer querys.

* **Basadas en grafos**

*Neo4j*, *Titan*

Basadas en nodos (entidades) que tienen múltiples relaciones.

Ideales para almacenar datos que presentan interconexiones complejas pero la escalabilidad supone un desafío matemático de gran complejidad.

* **En memoria**

*Memcached*, *Redis*

Son muy rápidas pero Son volátiles.

* **Optimizadas para búsquedas**

*BigQuery*, *Elasticsearch*

Son utilizadas para almacenar volúmenes de datos enormes a los que es necesario consultar frecuentemente para obtener información compleja y detallada.

Las búsquedas complejas se hacen sencillas.

Son sistemas altamente especializados para entornos que van a manejar enormes volúmenes de datos, por lo que su uso se desaconseja para proyectos pequeños en donde podríamos incurrir en una sobre-ingeniería.

---
---
---

# Estructura NoSQL basada en documentos

![](https://static.platzi.com/media/user_upload/FireStore-5474c032-0994-423f-a39e-2b33c1c9ef60.jpg)

## Firebase

* Firestore : Es la Base de Datos No Relacional
* Firebase : Es el Servicio Administrado que brinda Google para poder tener una Base de Datos FireStore.

https://console.firebase.google.com/

Creando proyecto en Firebase:
platziblog-sca

Un proyecto de Firebase es un proyecto de Cloud.
Cuando creas un nuevo proyecto de Firebase en Firebase Console, lo que en realidad estás creando es un proyecto de Google Cloud.

* Un *top level collection* se utilizaria para relaciones de tipo “agregacion”. 
* Una *subcollection* se utilizaria para relaciones tipo “composicion”.

Por ejemplo:

Tenemos Estudiantes, Cursos y Notas. Los estudiantes tiene cursos y los cursos tiene estudiantes. Si se elimina un curso los estudiantes no deben ser eliminados. Lo mismo si se elimina un estudiante los cursos no deben ser elimiandos. Esto es una relacion de agregacion. Aqui se usaria top level collection para estudiantes y cursos.

Los estudiantes tienen notas y las notas pertenecen a un estudiante. Si se elimina un estudiante, tiene sentido eliminar las notas. Esto es una relacion de composicion. Aqui se usarian las subcollections. El estudiante tendría una subcollection de notas.

https://www.mongodb.com/developer/how-to/new-time-series-collections/
https://firebase.google.cn/docs/firestore/data-model?hl=es_419