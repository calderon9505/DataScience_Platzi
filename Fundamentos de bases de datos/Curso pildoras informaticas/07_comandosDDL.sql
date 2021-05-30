#COMANDOS DDL

create table prueba1 (nombre varchar(20));
drop table prueba1;

create table prueba2(nombre varchar(20),
					apellido varchar(20),
                    edad tinyint,
                    fechanacimiento date,
                    carnet bool);
show columns from prueba2;
drop table prueba2;

create table prueba3(idalumno int auto_increment,
					nombre varchar(20),
					apellido varchar(20),
                    edad tinyint,
                    fechanacimiento date,
                    carnet bool,
                    primary key(idalumno));
show columns from prueba3;

alter table prueba3 add poblacion varchar(20);
#alter table prueba3 add column poblacion varchar(20); SIRVE
alter table prueba3 drop poblacion;
#alter table prueba3 drop column poblacion; SIRVE
alter table prueba3 modify carnet varchar(10);
#alter table prueba3 alter column carnet varchar(12); #XXNO SIRVEXX

alter table prueba3 add lugarnacimiento varchar(20);
#las 2 instrucciones a continuacion funcionan
alter table prueba3 modify lugarnacimiento varchar(20) default 'desconocido';
alter table prueba3 alter column lugarnacimiento set default 'desconocido';
#las 2 instrucciones a continuacion funcionan
alter table prueba3 modify lugarnacimiento varchar(20);
alter table prueba3 alter column lugarnacimiento drop default;

#CONCLUSIONES
#la opcion ALTER COLUMN solo sirve para usar con set o con drop
#de lo contrario usar con MODIFY
#se puede usar ADD COLUMN o solo ADD, de igual manera con drop


#INDICES
#indice clave primaria
alter table prueba3 add primary key(nombre, apellido); #XXno sirveXX
#solo una llave primaria por tabla
#indice ordinario
#sí duplicados, sí null
create index miindice on prueba3 (edad);
drop index miindice on prueba3;
#indice unico y/o compuestos
#no duplicados, si null
create unique index miindice2 on prueba3 (carnet);
drop index miindice2 on prueba3;
create unique index miindice2 on prueba3 (nombre, apellido);

alter table prueba3 drop primary key; #no sirve XXX

