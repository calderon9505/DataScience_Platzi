# Vistas

* Vista volatil. Siempre se realiza una consulta a la BBDD con esta vista, por lo tanto siempre se tiene información actualizada.

* Vista materializada. La consulta se realiza una vez y queda en memoria, las demás consultas acceden a esa memoria.

```sql
SELECT * FROM <nombre_vista>
```

```sql
REFRESH MATERIALIZED VIEW <nombre_vista>
```

# PL/SQL

PL/pgSQL is a loadable procedural language for the PostgreSQL database system. Desarrollar código directamente sobre la base de datos.

The design goals of PL/pgSQL were to create a loadable procedural language that

* can be used to create **functions**, **procedures**, and **triggers**,

* adds control structures to the SQL language,

* can perform complex computations,

* inherits all user-defined types, functions, procedures, and operators,

* can be defined to be trusted by the server,

* is easy to use.

```sql
[<label>]
[DECLARE
    declarations]
BEGIN
    statements
END [label]
```

```sql
DO $$
DECLARE
	rec record;
	contador integer := 0;
BEGIN
	FOR rec IN SELECT * FROM pasajeros LOOP
		RAISE NOTICE 'Un pasajero se llama %', rec.nombre;
		contador = contador+1;
	END LOOP;
	RAISE NOTICE 'Contador es %', contador;
END
$$
```

## **Procedures**

Se hacen con el lenguaje *sql*.

Se llaman con `CALL`.

No retornan nada.

```sql
CREATE OR REPLACE PROCEDURE test_procedure()
LANGUAGE SQL
AS $$
DROP TABLE IF EXISTS tabla_prueba;
CREATE TABLE tabla_prueba 
	(columna1 char(5) CONSTRAINT firstkey PRIMARY KEY):
$$;

CALL test_procedure();
```


## **Functions**

Se hacen con el lenguaje *plpgsql* porque son propias de PostgreSQL.

Se llaman con `SELECT`.

```sql
CREATE OR REPLACE FUNCTION test_function()
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
	DROP TABLE IF EXISTS tabla_prueba2;
	CREATE TABLE tabla_prueba2 
		(columna1 char(5) CONSTRAINT secondkey PRIMARY KEY, 
		contador integer,
		tiempo timestamp);
END
$$;
```

`test_function` crea una tabla llamada `tabla_prueba2` donde se va a guardar la copia de cada registro insertado en ``tabla_prueba``, junto con un conteo de registros y la fecha y hora.

El siguiente fué mi primera funcion creada.

```sql
CREATE OR REPLACE FUNCTION miPrimerPL() 
	RETURNS INTEGER 
	LANGUAGE plpgsql
AS $$
DECLARE
	rec record;
	contador integer := 0;
BEGIN
	FOR rec IN SELECT * FROM pasajeros LOOP
		RAISE NOTICE 'Un pasajero se llama %', rec.nombre;
		contador = contador+1;
	END LOOP;
	RAISE NOTICE 'Contador es %', contador;
	RETURN contador;
END
$$;
```


## **Triggers**

Se crea una **function** que regresa un **trigger**.

```sql
CREATE OR REPLACE FUNCTION duplicate_records() 
	RETURNS TRIGGER 
	LANGUAGE'plpgsql'
AS $$
DECLARE
	contador integer := 0;
BEGIN
	SELECT count(*) INTO contador FROM tabla_prueba;
	INSERT INTO tabla_prueba2(columna1, contador, tiempo) 
		VALUES (NEW.columna1, contador, now());
	RETURN NEW;
END
$$;
```

Se crea un **trigger** que se asocia a la tabla ``tabla_prueba`` y ejecuta la función ``duplicate_records()``.

```sql
CREATE TRIGGER changes
AFTER INSERT
ON tabla_prueba
FOR EACH ROW
EXECUTE PROCEDURE duplicate_records();
```

``INSERT INTO tabla_prueba VALUES (555);``