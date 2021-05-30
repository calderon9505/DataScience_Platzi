create database curso_SQL;
select * from clientes;
select * from productos;
select * from productosnuevos;
select * from pedidos;
show columns from clientes;
show columns from productos;
show columns from productosnuevos;
ALTER TABLE productos modify COLUMN PRECIO DOUBLE;
ALTER TABLE productos modify COLUMN FECHA date;

alter table productos change CODIGOARTICULO CÓDIGOARTÍCULO TEXT;
alter table productos change ﻿﻿SECCION SECCION TEXT;

#en excel cambiar la separación de comas por separacion
#de puntos y tener en cuenta el formato de la fecha
#al momento de importatlo (agrandar la ventana)

#No me permite cambiar al nombre a los campos
#depronto por las tildes