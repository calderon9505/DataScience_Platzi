# Amazon Relational Database Service (Amazon RDS)

It is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud.

Crear una base de datos PostreSQL version 12.9 para que pueda ser gratuita.

* DB instance identifier: **database-platzi**
* Master username: **postgres**
* Master password: **Scalderona27**
* Initial database name: **database_platzi**

En la instancia de EC2 instalo postgresql `sudo yum install postgresql`. (Al parecer no es necesario hacerlo en la instancia de EC2, pero lo hago ahí para tener "como" un ambiente virtual)

Obtenemos un archivo sql de ejemplo 
`$ wget https://raw.githubusercontent.com/mauropm/aws-platzi-python/master/sample-uk-zipcodes.sql`. Aunque en realidad ya lo tenia descargado en la instancia de EC2.

Desisto, no pude conectarme a la base de datos.

---

Platzi puso nuevas clases al final del curso, despues de gastarle horas a esto jaja.

Lo primero es ir a la base de datos en AWS y me seguro que la base de datos tenga acceso público. Además modifico los "security groups" para crear una "inbound rule" de tipo "postgresql".

Despues crear el nuevo servidor en pgadmin4 usando el host `database-platzi.c3pcqo7q2pdc.us-east-1.rds.amazonaws.com`

```sql
CREATE TABLE films (
	code CHAR(5) CONSTRAINT firstkey PRIMARY KEY,
	title VARCHAR(40) NOT NULL,
	did INTEGER NOT NULL,
	date_prod DATE,
	kind VARCHAR(10),
	len INTERVAL HOUR TO MINUTE
);


INSERT INTO films (code, title, did, date_prod, kind, len)
VALUES('UA502', 'Bananas', 105, '1971-07-13', 'Comedy', '82 minutes');


SELECT * FROM films;
```