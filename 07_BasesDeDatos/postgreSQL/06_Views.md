# Vistas

* Vista volatil. Siempre se realiza una consulta a la BBDD con esta vista, por lo tanto siempre se tiene información actualizada.

* Vista materializada. La consulta se realiza una vez y queda en memoria, las demás consultas acceden a esa memoria.

```
REFRESH MATERIALIZED VIEW <nombre_vista>
```