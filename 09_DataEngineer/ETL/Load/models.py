# Aquí se aplica ORM (Object Relational Mapper)
# Es una utilidad que permite manipular tablas de bases de datos
# como si fueran objetos de python.
# Una tabla corresponde a una clase.
# Una fila corresponde a un objeto (instancia de la clase)
# https://j2logo.com/python/sqlalchemy-tutorial-de-python-sqlalchemy-guia-de-inicio/


from sqlalchemy import Column, String, Integer, Text

from db import Base

# class Article(Base):
#     __tablename__ = 'articles'

#     id = Column(String, primary_key=True)
#     body = Column(String)
#     title = Column(String)
#     url = Column(String, unique=True)
#     newspaper_uid = Column(String)
#     host = Column(String)
#     n_tokens_title = Column(Integer)
#     n_tokens_body = Column(Integer)

#     def __init__(self,
#                  uid,
#                  body,
#                  title,
#                  url,
#                  newspaper_uid,
#                  host,
#                  n_tokens_title,
#                  n_tokens_body,
#                  ):
#         self.id = uid
#         self.body = body
#         self.title = title
#         self.url = url
#         self.newspaper_uid = newspaper_uid
#         self.host = host
#         self.n_tokens_title = n_tokens_title
#         self.n_tokens_body = n_tokens_body

# Dialecto para Mysql
class Article(Base):
    __tablename__ = 'articles'

    id = Column(String(32), primary_key=True)
    body = Column(Text)
    title = Column(Text)
    url = Column(Text)
    newspaper_uid = Column(String(32))
    host = Column(String(32))
    n_tokens_title = Column(Integer)
    n_tokens_body = Column(Integer)

    def __init__(self,
                 uid,
                 body,
                 title,
                 url,
                 newspaper_uid,
                 host,
                 n_tokens_title,
                 n_tokens_body,
                 ):
        self.id = uid
        self.body = body
        self.title = title
        self.url = url
        self.newspaper_uid = newspaper_uid
        self.host = host
        self.n_tokens_title = n_tokens_title
        self.n_tokens_body = n_tokens_body