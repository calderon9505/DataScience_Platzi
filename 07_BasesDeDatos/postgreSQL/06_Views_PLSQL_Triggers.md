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

PL/pgSQL is a loadable procedural language for the PostgreSQL database system. Desarrollar código directamente sobre la base de datos. Se compone de: nombre de funcion, declaraciones y bloques de código.

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

```sql
CREATE OR REPLACE FUNCTION miPrimerPL() 
	RETURNS integer AS
$$
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
$$
LANGUAGE PLPGSQL;
```

```SELECT miPrimerPL();```

```DROP FUNCTION miprimerpl();```

# Triggers

Se crea la tabla "conteo_pasajeros" con id, total y tiempo.

```sql
CREATE OR REPLACE FUNCTION miPrimerPL() 
	RETURNS TRIGGER 
	LANGUAGE 'plpgsql'
	AS
$$
DECLARE
	rec record;
	contador integer := 0;
BEGIN
-- 	SELECT count(*) FROM pasajeros;
	FOR rec IN SELECT * FROM pasajeros LOOP
		contador = contador+1;
	END LOOP;
	INSERT INTO conteo_pasajeros(total, tiempo) 
		VALUES (contador, current_time);
	RETURN NEW;
END
$$
```

```sql
CREATE OR REPLACE FUNCTION miPrimerPL() 
	RETURNS TRIGGER 
	LANGUAGE'plpgsql'
	AS
$$
DECLARE
	contador integer := 0;
BEGIN
	SELECT count(*) INTO contador FROM pasajeros;
	INSERT INTO conteo_pasajeros(total, tiempo) 
		VALUES (contador, current_time);
END
$$
```

```sql
CREATE TRIGGER mitrigger
AFTER INSERT
ON pasajeros
FOR EACH ROW
EXECUTE PROCEDURE miprimerpl();
```