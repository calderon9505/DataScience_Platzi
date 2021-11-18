# TIPOS DE DATOS

https://dev.mysql.com/doc/refman/8.0/en/data-types.html

## Texto

* CHAR : Espacio fijo en memoria para caracteres
* VARCHAR: Espacio dinámico en memoria para caracteres (255 max.)
* TEXT: Para cadenas de texto muy grandes

## Números

* TINYINT: 1 byte
* SMALLINT: 2 bytes
* INTEGER/INT: 4 bytes
* BIGINT: 8 bytes
* FLOAT: 4 bytes
* DOUBLE: 8 bytes
* DECIMAL(n,s): #dígitos, #decimales. Siempre conserva "s" cantidad de decimales
* NUMERIC (n,s): #dígitos, #decimales. Conserva mínimo "s" cantidad de decimales

 In MySQL, NUMERIC is implemented as DECIMAL, so the following remarks about DECIMAL apply equally to NUMERIC.

## Fecha/hora

* DATE: "AAAA-MM-DD"
* TIME: "HH:MM:SS"
* DATETIME: "AAAA-MM-DD HH:MM:SS"
* TIMESTAMP: "AAAA-MM-DD HH:MM:SS"

A DATETIME or TIMESTAMP value can include a trailing fractional seconds part in up to microseconds (6 digits) precision. 

YYYY-MM-DD hh:mm:ss[.fraction]

## Lógicos

* BOOLEAN
