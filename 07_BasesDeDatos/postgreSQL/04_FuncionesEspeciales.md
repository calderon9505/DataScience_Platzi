# Funciones especiales de PostgreSQL

* **ON CONFLICT DO** : Solucionar problemas al insertar o modificar datos para despues hacer la actualización correcta. Al insertar un dato existente, esta funcion permite indicar si lo que se quiere es hacer una actualización sobre el dato.

```sql
INSERT INTO public.estaciones(
	id, nombre, direccion)
	VALUES (1, 'Canaveral', 'Canaveral')
	ON CONFLICT DO NOTHING;
```

```sql
INSERT INTO public.estaciones(
	id, nombre, direccion)
	VALUES (1, 'Canaveral', 'Canaveral')
	ON CONFLICT(id) DO UPDATE 
	SET nombre='Canaveral', direccion='Canaveral';
```

```sql
INSERT INTO public.estaciones(
	id, nombre, direccion)
	VALUES (1, 'Canaveral', 'Canaveral')
	ON CONFLICT(id) DO UPDATE 
	SET nombre=EXCLUDED.nombre, direccion = EXCLUDED.direccion;
```

* **RETURNING** : Mostrar los cambios hechos sobre la BBDD. Si hay un campo tipo serial, devuelve el valor asignado.

```sql
INSERT INTO public.estaciones
	(nombre, direccion)
	VALUES ('Provenza', 'Provenza')
	RETURNING id;
```
```sql
INSERT INTO public.estaciones
	(nombre, direccion)
	VALUES ('Centro', 'Centro')
	RETURNING *;
```

* **LIKE / ILIKE** : Busqueda con REGEX.

Se usa "%" y "_" como en cualquier otra base de datos.

LIKE distingue mayusculas y minusculas, ILIKE no lo hace.

* **IS / IS NOT** : Comparar dos tipos de datos que no sean estandar (object, null, etc)

```sql
SELECT *
	FROM public.trenes
	WHERE modelo IS null;
```

* **COALESCE** : Comparar dos valores y retornar el que no es NULL.

```sql
SELECT COALESCE(nombre,'nadie') AS nombre
	FROM public.pasajeros WHERE id = 1;
```

* **NULLIF** : Comparar dos valores. Retorna NULL si son iguales o cero si son diferentes. Util para hacer comparaciones númericas antes de hacer operaciones prohibidas.

```sql
SELECT NULLIF (0,0);
```

* **GREATEST** : Retorna el mayor de un arreglo.

```sql
SELECT GREATEST (4,5,6,5,2);
```

* **LEAST** : Retorna el menor de un arreglo.

```sql
SELECT LEAST (4,5,6,5,2);
```

* **BLOQUES ANONIMOS** : Ingresar condicionales dentro de una consulta.

```sql
SELECT *,
	CASE
		WHEN fecha_nacimiento > '2005-01-01'
		THEN 'menor'
		ELSE 'mayor'
	END
	FROM public.pasajeros;
```