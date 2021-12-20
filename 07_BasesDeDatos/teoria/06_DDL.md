
# CREATE

## database

```sql
CREATE DATABASE platziblog DEFAULT CHARACTER SET utf8;
USE DATABASE platziblog;
```

## table

```sql
CREATE TABLE people (
  person_id INT NOT NULL AUTO_INCREMENT,
  last_name VARCHAR(45) NULL,
  first_name VARCHAR(45) NULL,
  address VARCHAR(45) NULL,
  city VARCHAR(45) NULL,
  PRIMARY KEY (person_id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
```

## view

```sql
CREATE OR REPLACE VIEW platzi_people AS
SELECT * FROM platziblog.people;
```

``SELECT * FROM platzi_people;``

## stored procedures

```sql
CREATE PROCEDURE actualizaproductos(precionuevo double, codigo varchar(4))
UPDATE productos SET precio = precionuevo WHERE codigoarticulo=codigo;
```

``call actualizaproductos(60,'AR22');``

##  triggers

```sql
CREATE TRIGGER productos_AI 
AFTER INSERT ON productos FOR EACH ROW
INSERT INTO regproductos(codigoarticulo, nombrearticulo, precio, insertado)
VALUES(new.codigoarticulo, new.nombrearticulo, new.precio, now());
```


# ALTER

```sql
ALTER TABLE people 
ADD COLUMN date_of_birth DATE NULL AFTER city;
```

```sql
ALTER TABLE people
DROP COLUMN date_of_birth;
```

```sql
ALTER TABLE people
ALTER COLUMN date_of_birth year;
```


# DROP

```sql
DROP TABLE `platziblog`.`people` ;
```

```sql
DROP DATABASE `platziblog`;
```