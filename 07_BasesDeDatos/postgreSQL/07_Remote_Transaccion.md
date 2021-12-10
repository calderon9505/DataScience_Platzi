# Conexión a bases de datos remotas

Las consultas con conexiones remotas se deben encapsular para no tener que compartir la contraseña. Se pueden usar vistas para ocultar esta información.

```CREATE EXTENSION dblink;```

```
SELECT * FROM pasajeros
FULL JOIN
dblink ('dbname=remota 
        port=5432 
        host=127.0.0.1 
        user=usuario_consulta 
        password=2705',
        'SELECT * FROM vip')
		AS datos_remotos(id integer, fecha date)
USING (id);
```

``USING (id) `` es *similar* a `` ON (pasajeros.id = datos_remotos.id)``

# Transacciones

[Comandos de transacciones en PostgreSQL](https://www.todopostgresql.com/comandos-de-transacciones-en-postgresql/)

Desactivar el autocommit.

```
BEGIN;
    <sql_sentence>;
    <sql_sentence>;
    <sql_sentence>;
COMMIT;
```