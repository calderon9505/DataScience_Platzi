# Common Table Expressions CTE

La cláusula cable `WITH` provee una forma de escribir declaraciones auxiliares para usarse en consultas largas. Proveen una forma de desestructurar largos *queries* que a su vez pueden contener sub-queries o anidaciones. Estas declaraciones, comunmente conocidas como CTE, pueden ser consideradas como la definición de tablas temporales que existen solo para una consulta.

Cada declaración auxiliar en un `WITH` puede ser un ``SELECT``, ``INSERT``, ``UPDATE`` o ``DELETE``; y la cláusula ``WITH`` en sí misma se adjunta a una declaración principal que puede ser tambien ``SELECT``, ``INSERT``, ``UPDATE`` o ``DELETE``.

The basic value of SELECT in WITH is to break down complicated queries into simpler parts.

```sql
WITH regional_sales AS (
    SELECT region, SUM(amount) AS total_sales
    FROM orders
    GROUP BY region
), top_regions AS (
    SELECT region
    FROM regional_sales
    WHERE total_sales > (SELECT SUM(total_sales)/10 FROM regional_sales)
)
SELECT region,
       product,
       SUM(quantity) AS product_units,
       SUM(amount) AS product_sales
FROM orders
WHERE region IN (SELECT region FROM top_regions)
GROUP BY region, product;
```

En este caso, de declaran las tablas temporales ``regional_sales`` y ``top_regions``, donde la salida de `regional_sales` es usada en `top_regions`, y la salida de `top_regions` es usada en la consulta principal.

Este ejemplo podría haberse escrito sin ``WITH``, pero habríamos necesitado dos niveles de sub-SELECTs anidados. Es un poco más fácil seguir este camino. Además de ser más eficiente.

## RECURSIVE

Usando ``RECURSIVE`` en una cláusula ``WITH`` se puede hacer referencia a su propia salida, algo que es imposible con SQL estandar.

Sumar los enteros desde 1 hasta 100:

```sql
WITH RECURSIVE t(n) AS (
    VALUES(1)
    UNION ALL
    SELECT n+1 FROM t WHERE n < 100
)
SELECT sum(n) FROM t;
```

[WITH Queries (Common Table Expressions)](https://www.postgresql.org/docs/12/queries-with.html)