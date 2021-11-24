#VISTAS
-- permite mayor privacidad de la información
-- optimiza las consutas a la BBDD
-- es un entorno de prueba seguro

-- las vistas reflejan la información real
-- si cambia algo en una tabla, la vista lo nota

create view art_deportes as
select nombrearticulo, seccion, precio from productos
where seccion='deportes';
select * from art_deportes;
drop view art_deportes;

alter view art_deportes as
select nombrearticulo, seccion, paisdeorigen from productos
where paisdeorigen='españa';