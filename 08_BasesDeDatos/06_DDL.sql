
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