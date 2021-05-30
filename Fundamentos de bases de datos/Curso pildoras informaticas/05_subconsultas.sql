#SUBCONSULTA ESCALONADA
#nombre y sección de aquellos productos cuyo valor sea mayor a la media
select nombrearticulo, precio, seccion from productos 
where precio > (select avg(precio) from productos);

#SUBCONSULTA DE LISTA #ALL #ANY
#articulos cuyo precio es superior que todos los articulos de ceramica
select * from productos  
where precio > all (select precio from productos where seccion='cerámica');
#articulos cuyo precio es superior que cualquiera de los articulos de ceramica
select * from productos  
where precio > any (select precio from productos where seccion='cerámica');
#Tambien se pudo haber usado un max(precio), osea, consulta escalonada

#SUBCONSULTA CORRELACIONADA
select nombrearticulo, precio, codigoarticulo from productos 
where codigoarticulo in (select codigoarticulo from productospedidos where unidades>20);
select nombrearticulo, precio, productos.codigoarticulo from productos
inner join productospedidos on productos.codigoarticulo=productospedidos.codigoarticulo
where unidades > 20;
#la subconsulta es mas corta, además, si las dos tablas no tuvieran una relacion
#directa, la consulta con inner join sería mucho mas larga

#mostrar clientes que no han pagado con tarjeta o que no han realizado pedidos
select empresa, poblacion from clientes
where codigocliente not in (select codigocliente from pedidos where formadepago='tarjeta');