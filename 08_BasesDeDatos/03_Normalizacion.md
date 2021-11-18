# NORMALIZACIÓN

campos = columnas
registros = filas

https://docs.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description

## Primera Forma Normal (1FN)

* Atributos atómicos. Todos los atributos, valores almacenados en las columnas, deben ser indivisibles.

* No deben existir grupos de valores repetidos.  Siempre que al muestrear la información de una tabla aparezcan datos repetidos, existe la posibilidad de crear una tabla independiente con ellos.

* No debe existir variación en el número de columnas.

* Los campos no clave deben identificarse por la clave (dependencia funcional).

* Debe existir una independencia del orden tanto de las filas como de las columnas; es decir, si los datos cambian de orden no deben cambiar sus significados.

## Segunda Forma Normal (2FN)

* No deben existir dependencias funcionales parciales. Esto significa que *todos los valores de las columnas de una fila* deben depender de la clave primaria de dicha fila. Es decir, cada registro debe tener una clave única.

## Tercera forma Normal (3FN)

* No deben existir dependencias transitivas entre las columnas de una tabla, lo cual significa que las columnas que no forman parte de la clave primaria deben depender sólo de la clave, nunca de otra columna no clave. Es decir, los campos que no son clave no deben tener dependencias.

## Cuarta Forma Normal (4FN)

* Los campos multivaluados se identifican por una clave única.