CREATE DATABASE transporte;
CREATE TABLE tren (
    id serial NOT NULL, 
    modelo character varying,
    capacidad integer,
    CONSTRAINT tren_pkey PRIMARY KEY (id) );
INSERT INTO tren( modelo, capacidad ) VALUES (‘Volvo 1’, 100);
UPDATE tren SET modelo = 'Honda 0726' Where id = 1;
DELETE FROM tren WHERE id = 1;