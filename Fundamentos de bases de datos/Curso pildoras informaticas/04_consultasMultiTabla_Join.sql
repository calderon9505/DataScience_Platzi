create database curso_SQL2;
use curso_SQL2;
select * from clientes;
select * from productos;
select * from pedidos;
show columns from clientes;
show columns from productos;
show columns from pedidos;
show columns from productospedidos;

desc productos;

show variables where variable_name in('hostname','port');

alter table clientes change ﻿CODIGOCLIENTE CODIGOCLIENTE text not null;
alter table pedidos change ﻿NUMERODEPEDIDO NUMERODEPEDIDO int(11);
alter table productos change ﻿CODIGOARTICULO CODIGOARTICULO text;
#hay un espacio rarisimo al comienzo del primer CODIGOCLIENTE
#ALTER TABLE clientes ADD PRIMARY KEY (codigocliente);

#----------------------------------------------------------------------------------
#CONSULTAS DE UNION INTERNA
#(OUTER JOINS) COMPOSICIONES EXTERNAS

#clientes de madrid que han hecho pedidos
select clientes.codigocliente, poblacion, direccion, numerodepedido from clientes 
inner join pedidos on clientes.codigocliente = pedidos.codigocliente
where poblacion='madrid';
#clientes de madrid TODOS, así no hayan hecho pedidos
select clientes.codigocliente, pedidos.codigocliente, poblacion, direccion, numerodepedido from clientes 
left join pedidos on clientes.codigocliente = pedidos.codigocliente
where poblacion='madrid';
#no es necesario tener la relaciones ni las llaves para hacer inner join

#clientes de madrid que NO han hecho pedidos
#es decir, el conjunto de la izquierda menos la union
#SOLO ES POSIBLE SI LAS TABLAS ESTAN RELACIONADAS(FALSO)
#la instruccion join crea una relacion temporal
select clientes.codigocliente, poblacion, direccion, numerodepedido from clientes 
left join pedidos on clientes.codigocliente = pedidos.codigocliente
where poblacion='madrid' and pedidos.CODIGOCLIENTE is null;



#SECCION DE PRUEBAS
delete from productos where codigoarticulo = "AR99";
SELECT * FROM PRODUCTOS;