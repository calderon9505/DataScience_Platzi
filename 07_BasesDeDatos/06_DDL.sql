
-- CREATE

--database
CREATE DATABASE `platziblog` DEFAULT CHARACTER SET utf8;
USE DATABASE `platziblog`;

-- table
CREATE TABLE `platziblog`.`people` (
  `person_id` INT NOT NULL AUTO_INCREMENT,
  `last_name` VARCHAR(45) NULL,
  `first_name` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  PRIMARY KEY (`person_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- view
USE `platziblog`;
CREATE OR REPLACE VIEW `platzi_people` AS
SELECT * FROM platziblog.people;
SELECT * FROM platzi_people;


-- triggers
create trigger productos_AI 
after insert on productos for each row
insert into regproductos(codigoarticulo, nombrearticulo, precio, insertado)
values(new.codigoarticulo, new.nombrearticulo, new.precio, now());

-- stored procedures
create procedure actualizaproductos(precionuevo double, codigo varchar(4))
update productos set precio = precionuevo where codigoarticulo=codigo;
call actualizaproductos(60,'AR22');

-- ALTER

ALTER TABLE `platziblog`.`people` 
ADD COLUMN `date_of_birth` DATE NULL AFTER `city`;

ALTER TABLE `platziblog`.`people` 
DROP COLUMN `date_of_birth`;

ALTER TABLE `people`
ALTER COLUMN `date_of_birth` year;




-- DROP

DROP TABLE `platziblog`.`people` ;

DROP DATABASE `platziblog`;