# Comandos de la terminal SQL Shell (psql)

version ```SELECT version();```

## Comandos de navegación y consulta de información


listar todos los comandos ```\?```

comandos SQL ```\h```, ```\h ALTER```

listar bases de datos ```\l```

camibar BBDD platzi ```\c platzi```

listar tablas ```\dt```

listar los esquemas ```\dn```

describir tabla ```\d <nombre_tabla>```

## Comandos de inspección y ejecución

ejecutar consulta anterior ```\g```


ejecutar comandos desde archivo ```\i <nombre_archivo>```

ver el historial de comandos ejecutados ```\s```

guardar lista de comandos ejecutados en un archivo ```\s <nombre_archivo>```

## Comandos para debug, optimización y otros

medir tiempo de consultas ```\timing```

cerrar consola ```\q```

## Archivos de configuración

mostrar archivo de configuración ```SHOW config_file;```

* postgresql.conf: Configuración general de postgres, múltiples opciones referentes a direcciones de conexión de entrada, memoria, cantidad de hilos de pocesamiento, replica, etc.
* pg_hba.conf: Muestra los roles así como los tipos de acceso a la base de datos.
* pg_ident.conf: Permite realizar el mapeo de usuarios. Permite definir roles a usuarios del sistema operativo donde se ejecuta postgres.

[Configuración Básica De PostgreSQL](https://e-mc2.net/es/configuracion-basica-de-postgresql)
