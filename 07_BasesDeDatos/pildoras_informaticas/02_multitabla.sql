-- CONSULTAS CON UNION EXTERNA
-- Cuando hay información fraccionada en distintas tablas.
-- Una tabla bajo la otra.
-- Igual cantidad de columnas y tipos de datos compatibles.

-- UNION elimina los registros repetidos, a diferencia de UNION ALL 
SELECT * FROM PRODUCTOS WHERE SECCION = 'DEPORTES'
UNION
SELECT * FROM PRODUCTOSNUEVOS WHERE SECCION = 'DEPORTES DE RIESGO';

--------------------------------------------------------------------

-- CONSULTAS CON UNION INTERNA
-- Se hace uso de las relaciones entre tablas.
-- La relación se especifica en la consulta.
-- Interpretar como parte del FROM.

-- INNER JOIN
-- conjunto "interseccion"
SELECT * FROM CLIENTES 
INNER JOIN PEDIDOS 
ON CLIENTES.CODIGOCLIENTE = PEDIDOS.CODIGOCLIENTE;

-- LEFT JOIN
-- conjunto left
SELECT * FROM CLIENTES 
LEFT JOIN PEDIDOS 
ON CLIENTES.CODIGOCLIENTE = PEDIDOS.CODIGOCLIENTE;
-- EXCLUSIVE LEFT JOIN
-- conjunto left - right
SELECT * FROM CLIENTES 
LEFT JOIN PEDIDOS 
ON CLIENTES.CODIGOCLIENTE = PEDIDOS.CODIGOCLIENTE
WHERE PEDIDOS.CODIGOCLIENTE IS NULL;

-- RIGHT JOIN
-- conjunto right
SELECT * FROM CLIENTES 
RIGHT JOIN PEDIDOS 
ON CLIENTES.CODIGOCLIENTE = PEDIDOS.CODIGOCLIENTE;
-- EXCLUSIVE RIGHT JOIN
-- conjunto right - left
SELECT * FROM CLIENTES 
RIGHT JOIN PEDIDOS 
ON CLIENTES.CODIGOCLIENTE = PEDIDOS.CODIGOCLIENTE
WHERE CLIENTES.CODIGOCLIENTE IS NULL;

-- FULL JOIN / FULL OUTER JOIN
-- Para el conjunto "union" se usa UNION
-- junto con las consultas anteriores

-- EXCLUSIVE FULL OUTER JOIN
-- Para el conjunto "diferencia simetrica"
-- se usa UNION junto con las consultas anteriores

--------------------------------------------------------------------

-- DISTINCT
-- Clientes que han hecho pedido y sus formas de pago
-- el distintc se puede aplicar a todas las consultas de accion
SELECT DISTINCT CODIGOCLIENTE, FORMADEPAGO FROM PEDIDOS ORDER BY CODIGOCLIENTE;
SELECT CODIGOCLIENTE, FORMADEPAGO FROM PEDIDOS GROUP BY CODIGOCLIENTE, FORMADEPAGO ORDER BY CODIGOCLIENTE;
SELECT CODIGOCLIENTE, GROUP_CONCAT(DISTINCT FORMADEPAGO) FROM PEDIDOS GROUP BY CODIGOCLIENTE ORDER BY CODIGOCLIENTE;
-- conteo de las formas de pago de cada cliente
SELECT CODIGOCLIENTE, FORMADEPAGO, COUNT(*) AS TOTAL FROM PEDIDOS GROUP BY CODIGOCLIENTE, FORMADEPAGO ORDER BY CODIGOCLIENTE;