-- CONSULTAS CON UNION EXTERNA
-- Cuando hay información fraccionada en distintas tablas.
-- Una tabla bajo la otra.
-- Igual cantidad de columnas y tipos de datos compatibles.

-- UNION elimina los registros repetidos, a diferencia de UNION ALL 
SELECT * FROM PRODUCTOS WHERE SECCION = 'DEPORTES'
UNION SELECT * FROM PRODUCTOSNUEVOS WHERE SECCION = 'DEPORTES DE RIESGO';

--------------------------------------------------------------------

-- CONSULTAS CON UNION INTERNA
-- Se hace uso de las relaciones entre tablas.
-- La relación se especifica en la consulta.
-- Interpretar como parte del FROM.

-- INNER JOIN
-- conjunto interseccion
SELECT * FROM CLIENTES 
INNER JOIN PEDIDOS 
ON CLIENTES.CODIGOCLIENTE = PEDIDOS.CODIGOCLIENTE;

-- LEFT JOIN
-- conjunto left
SELECT * FROM CLIENTES 
LEFT JOIN PEDIDOS 
ON CLIENTES.CODIGOCLIENTE = PEDIDOS.CODIGOCLIENTE;
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
-- conjunto right - left
SELECT * FROM CLIENTES 
RIGHT JOIN PEDIDOS 
ON CLIENTES.CODIGOCLIENTE = PEDIDOS.CODIGOCLIENTE
WHERE CLIENTES.CODIGOCLIENTE IS NULL;

-- Para el conjunto union o diferencia simetrica
-- se usa union junto con las consultas anteriores
-- o con FULL JOIN
