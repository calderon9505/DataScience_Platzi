Resumen de todas las opciones de uso para los comandos DML

Command + From + Where + Group by + Having + Order by

## Clauses

* FROM
* WHERE
* GROUP BY
* HAVING
* ORDER BY (ASC, DESC)
* OFFSET
* LIMIT

## Alias

* AS

## Aggregation

Se aplican sobre grupos.

* AVG( )
* SUM( )
* COUNT( )
* MIN( )
* MAX( )

Otras funciones de agregación

* IF()
* CASE

## Operators

* \>, <, >=, <=, =, !=, <>
* AND, OR, NOT
* BETWEEN
* LIKE (with wildcards)
* IN
* ALL
* ANY
* EXISTS

## Join

Union interna

* INNER JOIN
* LEFT JOIN
* RIGHT JON

Union externa

* UNION (FULL OUTER JOIN / FULL JOIN)
* UNION ALL (Incluye repetidos)
* EXCEPT (No soportada mysql)
* INTERSECT (No soportada mysql)
* MINUS (No soportada mysql)

## Funciones

Las funciones se salen del estandar SQL. Las siguientes suelen ser comunes a muchos gestores.

Se aplican sobre registros individuales.

* ROUND()
* TRUNCATE()
* NOW()
* DATEDIFF()
* DATE_FORMAT()
* CONCAT()

# Recursos

* Interpretación de los JOIN

![](https://ingenieriadesoftware.es/wp-content/uploads/2018/07/sqljoin.jpeg)

* Subconsultas

    * Subconsulta Escalonada
    * Subconsulta de lista
    * Subconsulta correlacionada

* Consultas de acción

    * Actualización
    * Creación de tabla
    * Elliminación
    * Datos anexados

* Consultas de predicado

    * DISTINC
    * DISTINCROW
