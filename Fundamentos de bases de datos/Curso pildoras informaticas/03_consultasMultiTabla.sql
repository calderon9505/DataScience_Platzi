#CONSULTAS DE UNION EXTERNA
#union, union all, except, intersect, minus
#los tres ultimos no los soporta mySQL
#SE UNEN REGISTRSO

select * from productos
where sección='deportes'
union select * from productosnuevos
where sección='deportes de riesgo';
#el titulo es el de la tabla 1

select * from productos where precio>500 union
select * from productosnuevos where sección='alta costura';

insert into productosnuevos values('AR06', 'DEPORTES', 
	'MANCUERNAS', '60', '2000-09-13 00:00:00', 'VERDADERO', 'USA', '');
select * from productos
where sección='deportes'
union select * from productosnuevos;
select * from productos
where sección='deportes'
union all select * from productosnuevos;
#diferencia entre UNION y UNION ALL
#UNION no muestra registros repetidos


#---------------------------------------------
#CONSULTAS DE UNION INTERNA
#(OUTER JOINS) COMPOSICIONES EXTERNAS
#SE UNEN CAMPOS

#clientes de madrid que han hecho pedidos
ALTER TABLE clientes modify COLUMN códigocliente text not null;
ALTER TABLE clientes ADD PRIMARY KEY (CÓDIGOCLIENTE);
select * from clientes 
inner join pedidos on clientes.códigocliente= pedidos.códigocliente
where población='madrid';

#A PARTIR DE AQUÍ ME VOY PARA LA BASE DE DATOS curso_sql2
#donde manejo las cosas sin acentos



