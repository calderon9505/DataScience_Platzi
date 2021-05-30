#CONSULTAS DE ACCIÓN

#actualizacion, aumentar 10 al precio de los articulos de deportes
update productos set precio=precio+10 where seccion='deportes';
update productos set seccion='DEPORTES' where seccion='deportivos';

#creacion de tabla a partir de otra (no es nueva, eso sería lenguaje de definicion)
create table CLIENTES_MADRID select * from clientes where poblacion='madrid';
select * from clientes_madrid;

#eliminacion de registros
delete from clientes where poblacion='madrid' and precio between 50 and 100;


#DISTINCT(no informacion repetida)
#DISTINCTROW(DISTINCTROW is a synonym for DISTINCT.)
select distinct * from clientes 
inner join pedidos on clientes.codigocliente=pedidos.codigocliente;
select distinct empresa, formadepago from clientes 
inner join pedidos on clientes.codigocliente=pedidos.codigocliente;
select * from clientes 
inner join pedidos on clientes.codigocliente=pedidos.codigocliente;
#para elimanar clientes que no hayan hecho pedidos debo hacer
#delete distinctrow clientes.*, pedidos.codigocliente from cliente left ....

#agregar registros de una tabla en otra
insert into clientes select * from clientes_madrid;
#insert into clientes (campo 1, campo 3, campo 4) ...