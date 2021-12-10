# Jerarquía de Bases de Datos

* **Motor de base de datos**: Software que provee un conjunto de servicios encargados de administrar y estructurar la información en una base de datos. PostgreSQL es un motor de base de datos.

* **Servidor de base de datos**: Computador que tiene un motor de base de datos instalado y en ejecución.

* **Base de datos**: Grupo de datos que pertenecen a un mismo contexto.

* **Esquemas de base de datos en PostgreSQL**: Grupo de objetos de base de datos que guardan relación entre sí (tablas, funciones, relaciones, secuencias).

* **Tablas de base de datos**: Estructura que organiza los datos en filas y columnas formando una matriz.

# Particiones

* **Separación física de datos**: Guardas varias partes de la misma tabla en varios espacios del disco, o incluso, distintos discos.

* **Misma esctructura lógica**: Funcionan igual las consultas

```
CREATE TABLE bitacora_viajes_2010_01
PARTITION OF bitacora_viajes
FOR VALUES FROM ('2010-01-01') TO ('2010-02-01');
```

# Roles

```
CREATE ROLE usuario_consulta;
ALTER ROLE usuario_consulta WITH LOGIN SUPERUSER;
ALTER ROLE usuario_consulta WITH PASSWORD 'etc123';
DROP ROLE usuario_consulta;
```

```\dg``` para consultar roles.

En Login/Group Roles se crea el usuario nuevo con opción de login y herencia de superusuario.

En Schemas -> public -> Tables se selecciona Grant Wizard... y allí se seleccionan las tablas deseadas y los privilegios deseados.
