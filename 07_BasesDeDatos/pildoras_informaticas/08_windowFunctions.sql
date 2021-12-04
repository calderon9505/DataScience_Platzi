-- A window function performs an aggregate-like operation on a set of query rows. 
-- However, whereas an aggregate operation groups query rows into a single result row, 
-- a window function produces a result for each query row.

SELECT SECCION, SUM(PRECIO) AS TOTAL FROM PRODUCTOS GROUP BY SECCION ORDER BY TOTAL;
SELECT NOMBREARTICULO, SECCION, PRECIO, 
	SUM(PRECIO) OVER() AS PRECIO_TOTAL, 
    SUM(PRECIO) OVER(PARTITION BY SECCION) AS PRECIO_SECCION
	FROM PRODUCTOS ORDER BY SECCION, PRECIO;

-- The first OVER clause is empty, which treats the entire set of query rows as a single partition.
-- The window function thus produces a global sum, but does so for each row.
-- The second OVER clause partitions rows by "seccion", producing a sum per partition (per seccion).
-- The function produces this sum for each partition row.

-- The OVER clause is permitted for many aggregate functions, which therefore can be used as 
-- window or nonwindow functions, depending on whether the OVER clause is present or absent:
-- MySQL also supports nonaggregate functions that are used only as window functions.

SELECT NOMBREARTICULO, SECCION, PRECIO, 
	ROW_NUMBER() OVER(PARTITION BY SECCION) AS ROW_NUM1, 
    ROW_NUMBER() OVER(PARTITION BY SECCION ORDER BY PRECIO) AS ROW_NUM2
	FROM PRODUCTOS ORDER BY SECCION, PRECIO;

-- En las Window Functions no se puede hacer WHERE ni HAVING, se debe hacer una subconsulta
SELECT * 
	FROM (SELECT NOMBREARTICULO, SECCION, PRECIO, 
		RANK() OVER(PARTITION BY SECCION ORDER BY PRECIO DESC) AS RANKING
		FROM PRODUCTOS
        ) AS RANKED
	WHERE RANKING < 3
    ORDER BY RANKING;
	
SELECT NOMBREARTICULO, SECCION, PRECIO, 
    FIRST_VALUE(PRECIO) OVER(PARTITION BY SECCION ORDER BY PRECIO) AS FIRST_,
    FIRST_VALUE(PRECIO) OVER(PARTITION BY SECCION ORDER BY PRECIO DESC) AS LAST_,
    -- LAST_VALUE(PRECIO) OVER(PARTITION BY SECCION ORDER BY PRECIO) AS LAST_ERRONEO
    NTH_VALUE(PRECIO, 3) OVER(PARTITION BY SECCION ORDER BY PRECIO) AS THIRD_
	FROM PRODUCTOS ORDER BY SECCION, PRECIO;




