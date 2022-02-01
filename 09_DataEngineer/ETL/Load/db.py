# Aquí se aplica ORM (Object Relational Mapper)
# Es una utilidad que permite manipular tablas de bases de datos
# como si fueran objetos de python.
# Una tabla corresponde a una clase.
# Una fila corresponde a un objeto (instancia de la clase)
# https://j2logo.com/python/sqlalchemy-tutorial-de-python-sqlalchemy-guia-de-inicio/

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Una Session es como una transacción. Un conjunto de operacioens que
# se ejecutan todas correctamente o no se ejecuta ninguna.


# {database_type}://{user}:{password}@{host}/{database}
# Engine = create_engine('sqlite:///newspaper.db')
database_type = 'mysql+mysqldb'
user = 'root'
password = '2705'
host = 'localhost:3306'
database = 'newspaper'
conn_string = f'{database_type}://{user}:{password}@{host}/{database}'
Engine = create_engine(conn_string)
# Engine = create_engine( '{"mysql"}://{"root"}:{"2705"}@{"localhost:3306"}/{"newspaper"}' )

# Método factoría (patrón de diseño) usado para crear la Session.
Session = sessionmaker(bind=Engine)

# Esta clase será de la que hereden todos los modelos
Base = declarative_base()