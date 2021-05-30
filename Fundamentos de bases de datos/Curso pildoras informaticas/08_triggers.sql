#TRIGGERS

create table regproductos (codigoarticulo varchar(25), 
							nombrearticulo varchar(30), 
                            precio int(4), 
                            insertado datetime);

#A de after, I de insert; for each statement(bloque)
create trigger productos_AI 
after insert on productos for each row
insert into regproductos(codigoarticulo, nombrearticulo, precio, insertado)
values(new.codigoarticulo, new.nombrearticulo, new.precio, now());
drop trigger productos_AI;
insert into productos(codigoarticulo,nombrearticulo,precio,paisdeorigen)
values('AR75','pantalon',50,'españa');
select * from productos where paisdeorigen='españa';
select * from regproductos order by insertado desc;


#--------------------------------------------------------------------------
create table respaldo (old_codigoarticulo varchar(25),
						old_precio int,
                        new_codigoarticulo varchar(25),
                        new_precio int,
						usuario varchar(20),
                        modificacion datetime);
create trigger productos_BU
before update on productos for each row 
insert into respaldo(old_codigoarticulo, old_precio, 
new_codigoarticulo, new_precio, usuario, modificacion)
values(old.codigoarticulo, old.precio, new.codigoarticulo, new.precio,
current_user(), now());
update productos set precio=precio+20 where codigoarticulo='AR07';
select * from productos;
select * from respaldo order by modificacion desc;
drop trigger productos_BU;

#create trigger productos_AD before delete on

#para modificar un trigger se elimina y se vuelve a crear ó
#drop trigger if exists NOMBRE_TRIGGER; create trigger .......alter
#así se hace todo en una sola linea