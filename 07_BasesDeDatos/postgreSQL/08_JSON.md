# Trabajando con objetos JSON

En otros manejadores de bases de datos se pueden guardar los JSON como texto normal, y despues extraerlos y analizarlos con otros lenguajes como Python. Pero PostgreSQL ofrece herramientas para trabajar con JSON como si fueran datos primitivos.

El uso de objetos JSON hace más lentas y complicadas las consultas. Pero da mayor flexibilidad en el trabajo.

PostgreSQL tiene dos versiones de implementación de JSON:

* **JSON normal (json)**  - Es un string de texto.
* **JSON binary (jsonbi)** - Es un objeto binario. Permite transacciones más rápidas.

Creando tabla con tipo de dato JSON

```sql
CREATE TABLE ordenes (
   ID serial NOT NULL PRIMARY KEY,
   info json NOT NULL
);
```

Insertando datos a la tabla

```sql
INSERT INTO ordenes (info)
VALUES
   ('{ "cliente": "David Sanchez", 
		"items": {"producto": "Biberón","cantidad": 24}}'),
   ('{ "cliente": "Edna Cardenas", 
		"items": {"producto": "Carro de juguete","cantidad": 1}}'),
   ('{ "cliente": "Israel Vazquez", 
		"items": {"producto": "Tren de juguete","cantidad": 2}}');
```

El operador `->` accede al "valor" a partir de la "clave". Devuelve un objeto tipo ``json``

```sql
SELECT info -> 'cliente' AS cliente
FROM ordenes;
```

El operador `->>` accede al "valor" a partir de la "clave". Devuelve un tipo de dato ``text``

```sql
SELECT info ->> 'cliente' AS cliente
FROM ordenes
WHERE info -> 'items' ->> 'producto' = 'Biberón'
```

```sql
SELECT info -> 'items' ->> 'cantidad' AS cantidad
FROM ordenes;
```

Operador `cast` para realizar cálculos con los datos del JSON

```sql
SELECT 
	MIN(CAST(info -> 'items' ->> 'cantidad' AS INTEGER)),
	AVG((info -> 'items' ->> 'cantidad') :: INTEGER)
FROM ordenes;
```