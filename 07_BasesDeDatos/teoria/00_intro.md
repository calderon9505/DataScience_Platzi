# BASES DE DATOS RELACIONALES

https://www.mindmeister.com/es/1079684487/las-12-reglas-de-codd-del-modelo-relacional?fullscreen=1#

![](https://static.platzi.com/media/user_upload/img-2e2fc1ba-ad77-4045-b7a5-f74a65e3f55e.jpg)

https://de.wikipedia.org/wiki/Chen-Notation

---

## Entidad

Representa algo en el mundo real (incluso algo abstracto).

* **Atributos**: Atributos ligados a la entidad.

* **Atributos compuestos**: Están formados por otros atributos

* **Atributo llave**: Identifican a la entidad y no pueden ser repetidos

    * **Naturales**: Son inherentes al objeto. (ej. número de serie)
    * **artificiales**: No son inherente al objeto. Se asignan de manera arbitraria.

* **Entidades fuertes (entidades)**: Entidades que pueden sobrevivir por sí solas.

* **Entidades débiles**: No pueden existir sin una entidad fuerte.

    * **Entidades débiles por identidad**: no se diferencian entre sí más que por la clave de su identidad fuerte.
    * **Entidades débiles por existencia**: se les asigna una clave propia.

![](https://static.platzi.com/media/user_upload/ENTIDAD%20LAPTOPS-4910405e-b261-44c6-9193-a68d85a92541.jpg)

## RELACION/CARDINALIDAD

* 1:1
* 0:1
* 1:N
* 0:N
* N:N

# DRIAGRAMA ER

Un diagrama es como un mapa y nos ayuda a entender cuáles son las entidades con las que vamos a trabajar, cuáles son sus relaciones y qué papel van a jugar en las aplicaciones de la base de datos.


