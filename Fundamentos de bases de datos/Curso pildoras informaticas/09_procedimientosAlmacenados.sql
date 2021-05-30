create procedure muestraclientes()
select * from clientes where poblacion='madrid';
select * from clientes;

call muestraclientes();

#este proc. tambien lo uso en java video 209
create procedure actualizaproductos(precionuevo double, codigo varchar(4))
update productos set precio = precionuevo where codigoarticulo=codigo;
call actualizaproductos(60,'AR22');
select * from productos;
drop procedure actualizaproductos;

delimiter $$pedidos
create procedure calculaedad(ano_nac int)
	begin
		declare ano_act int default 2019;
        declare edad int;
        set edad=ano_act-ano_nac;
        select edad;
    end;$$
delimiter ;

call calculaedad(2018); #pasa algo raro

#tambien se pueden crear procedimientos 
#almacenados dentro de triggers

delimiter $$
create trigger revisa_precio_BU 
before update on productos for each row
	begin
		if(new.precio<0 or new.precio>100) then 
			set new.precio=old.precio;
		end if;
    end;$$
delimiter ;
drop trigger revisa_precio_BU;

#tuve que borrar el trigger anterior por que no permite
#dos triggers para la misma tabla
update productos set precio=8000 where codigoarticulo='AR01';
select * from productos;

#------------------------------------------------------------------
#VISTAS
create view art_deportes as
select nombrearticulo, seccion, precio from productos
where seccion='deportes';
select * from art_deportes;
drop view art_deportes;

alter view art_deportes as
select nombrearticulo, seccion, paisdeorigen from productos
where paisdeorigen='españa';