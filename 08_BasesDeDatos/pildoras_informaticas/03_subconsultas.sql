-- SUBCONSULTAS
-- un select(hijo) dentro de otro select(padre).
-- comparar registros del select hijo con el select padre.
-- pueden volver lenta la consulta, usar con cuidado.
-- tambien le puedo poner nombre a la subconsulta con AS

-- SUBCONSULTA ESCALONADA
-- el select hijo devuelve un único valor
-- articulos cuyo precio es superior a la media.
SELECT * FROM PRODUCTOS WHERE PRECIO > (SELECT AVG(PRECIO) FROM PRODUCTOS);

-- SUBCONSULTA DE LISTA
-- el select hijo devuelve toda una columna
-- articulos cuyo precio es superior a todos los articulos de ceramica.
SELECT * FROM PRODUCTOS WHERE PRECIO > ALL(SELECT PRECIO FROM PRODUCTOS WHERE SECCION='CERAMICA');
-- articulos cuyo precio es superior a cualquier articulo de ceramica.
SELECT * FROM PRODUCTOS WHERE PRECIO > ANY(SELECT PRECIO FROM PRODUCTOS WHERE SECCION='CERAMICA');

-- SUBCONSULTA CORRELACIONADA
-- el select hijo devuelve toda una columna
-- articulos que se han pedido más de 20 unidades
SELECT * FROM PRODUCTOS WHERE CODIGOARTICULO IN(SELECT CODIGOARTICULO FROM PRODUCTOSPEDIDOS WHERE UNIDADES>20);
SELECT * FROM PRODUCTOS INNER JOIN PRODUCTOSPEDIDOS ON PRODUCTOS.CODIGOARTICULO=PRODUCTOSPEDIDOS.CODIGOARTICULO WHERE UNIDADES>20;
-- clientes que no han pagado con tarjeta
SELECT * FROM CLIENTES WHERE CODIGOCLIENTE NOT IN(SELECT CODIGOCLIENTE FROM PEDIDOS WHERE FORMADEPAGO='TARJETA');
-- de lo anterior, NO mostrar los que no han hecho pedido nunca
SELECT * FROM CLIENTES 
WHERE CODIGOCLIENTE NOT IN(SELECT CODIGOCLIENTE FROM PEDIDOS WHERE FORMADEPAGO='TARJETA')
AND CODIGOCLIENTE NOT IN(SELECT CLIENTES.CODIGOCLIENTE FROM CLIENTES LEFT JOIN PEDIDOS ON CLIENTES.CODIGOCLIENTE = PEDIDOS.CODIGOCLIENTE WHERE PEDIDOS.CODIGOCLIENTE IS NULL);