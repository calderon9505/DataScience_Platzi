#CONSULTAS BASICAS

SELECT NOMBREARTÍCULO, SECCIÓN, PRECIO FROM PRODUCTOS 
WHERE SECCIÓN = 'CERÁMICA' OR SECCIÓN='DEPORTES';
#IMPORTANTE: operador lógico OR para que funcione

SELECT * FROM PRODUCTOS 
WHERE SECCIÓN = "DEPORTES" AND PAÍSDEORIGEN="USA" 
	AND PRECIO>100;
    
SELECT * FROM PRODUCTOS
WHERE FECHA BETWEEN '2000-03-01' AND '2000-4-30';
SELECT * FROM PRODUCTOS
WHERE FECHA BETWEEN '2000-03-18' AND '2000-4-17'
ORDER BY FECHA;
#INCLUYE LAS FECHAS LIMITES

#EJERCICIOS
select nombreartículo, precio from productos
where sección='deportes' and precio between 100 and 200;
select nombreartículo, paísdeorigen from productos
where paísdeorigen != 'españa';
select * from productos
where (sección='deportes' and paísdeorigen='españa') or
precio > 350;
select NOMBREARTÍCULO, sección, fecha from productos
where fecha between '2001/05/1' and '2001/12/15';

#--------------------------------------------------------
SELECT * FROM PRODUCTOS 
WHERE SECCIÓN = 'CERÁMICA' OR SECCIÓN='DEPORTES'
order by sección asc, paísdeorigen asc, precio asc;
#se pueden hacer varios niveles para ordenar

select sección, sum(precio) as suma_precios from productos
group by sección order by suma_precios;

select sección, NOMBREARTÍCULO, sum(precio) as suma_precios 
from productos
group by sección order by suma_precios;
#el campo adicional no es util, no da ninguna info.
#campo de agrupacion es sección
#campo de calculo es precio

select sección, avg(precio) as prom_precio
from productos
group by sección 
having sección='deportes' or sección = 'confección'
order by prom_precio;
#el HAVING sustituye al WHERE en las consultas
#de agrupación o totales

select población, count(﻿códigocliente) as conteo
from clientes 
group by población;
#count no cuenta campos vacios, usar sobre IDs

select sección, max(precio) as precio_maximo
from productos 
where sección='confección' 
group by sección;
#todo falla al poner otro campo en el select

#EJERCICIOS
select dirección, teléfono, población as Residencia 
from clientes order by residencia desc;
select población from clientes group by población;
select sección, sum(precio) as suma_seccion
from productos group by sección;
select sección, avg(precio) as MediaPorSeccion
from productos where sección != 'juguetería'
group by sección;
select sección, count(códigoartículo) as conteo
from productos where sección='deportes'
group by sección;

#---------------------------------------------------------
#las consultas de calculo se hacen sobre
#registros individuales, no sobre grupos
#en realidad es sobre campos

select nombreartículo, sección, precio, round(precio*1.21,2) as ConIva
from productos;
select nombreartículo, fecha, 
	date_format(now(),'%d-%m-%Y') as hoy, 
    datediff(now(),fecha) as fecha_diff
from productos
where sección='deportes';
select nombreartículo, fecha, 
	date(now()) as hoy,  #uso del curdate() y curtime() y date()
    datediff(now(),fecha) as fecha_diff
from productos
where sección='deportes';

#EJERCICIOS;

select nombreartículo, sección, precio, 
	round(precio*0.93,2) as Descuento_7
from productos;
select fecha, nombreartículo, sección, precio,
	round(precio-2,2) as DTO2€_EN_CERAMICA
from productos
where sección='cerámica'
order by fecha desc;