# Aquí se aplica ORM (Object Relational Mapper)
# Es una utilidad que permite manipular tablas de bases de datos
# como si fueran objetos de python.
# Una tabla corresponde a una clase.
# Una fila corresponde a un objeto (instancia de la clase)
# https://j2logo.com/python/sqlalchemy-tutorial-de-python-sqlalchemy-guia-de-inicio/


import argparse
import logging
import pandas as pd
from models import Article
from db import Base, Engine, Session


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(filename):
    
    # Crear (si no existe) las tablas de todos los modelos
    Base.metadata.create_all(Engine)
    # Obtener una Session
    session = Session()

    articles = pd.read_csv(filename)

    for index, row in articles.iterrows():
        logger.info(index)
        logger.info('Loading article uid {} into DB'.format(row['uid']))
        article = Article(
                        row['uid'],
                        row['body'],
                        row['title'],
                        row['url'],
                        row['newspaper_uid'],
                        row['host'],
                        row['n_tokens_title'],
                        row['n_tokens_body'],
                        )

        session.add(article)

    session.commit()
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The file you want to load into the db',
                        type=str)

    args = parser.parse_args()

    main(args.filename)