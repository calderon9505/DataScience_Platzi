create database proyecto_jsp;
use proyecto_jsp;

create table if not exists usuarios(
	usuario_id integer unsigned primary key auto_increment,
    nombre varchar(20) not null,
    apellido varchar(20) not null,
    usuario varchar(20) not null unique,
    contrasena varchar(20) not null,
    pais varchar(20) not null,
    tecnologia varchar(20) default null
);

select * from usuarios;

insert into usuarios values(null,'b','b','b','b','b','b');

drop table usuarios;