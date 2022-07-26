import argparse
# funciona como una alternativa a la función input que 
# permite agregar los tipos de variables que va a recibir

import logging
# Permite enviar mensajes por consola de manera automatica 
# asignandole un level de importancia a cada tipo de mensaje

import re
import datetime
import csv

# from urllib.error import HTTPError
from requests import HTTPError
# from urllib3.exceptions import MaxRetryError

from common import config
import news_page_objects as news


logging.basicConfig(level=logging.INFO)
# No mostrar mensajes con nivel menor a INFO
logger = logging.getLogger(__name__)
# Instancia de un logging

is_well_formed_link = re.compile(r'^https?://.+/.+$')
is_root_path = re.compile(r'^/.+$')


def _news_scraper(news_site_uid):
    # URL del periodico seleccionado
    host = config()['news_sites'][news_site_uid]['url']

    # Mostrar mensaje de tipo INFO
    logger.info('Beginning scraper for {}'.format(host))
    # logging.info('Finding links in homepage...')

    # Instancia de news_page_objects para el periodico seleccionado
    homepage = news.HomePage(news_site_uid, host)
    print('Cantidad de articulos encontrados: ', len(homepage.article_links))

    articles = []
    for link in homepage.article_links:
        article = _fetch_article(news_site_uid, host, link)
        if article:
            articles.append(article)
            # print(article.title)
            # break # for tests
    
    print('Cantidad de articulos scrapeados: ', len(articles))

    _save_articles(news_site_uid, articles)


def _fetch_article(news_site_uid, host, link):

    article = None
    try:
        full_link = _build_link(host, link)
        print(full_link)
        article = news.ArticlePage(news_site_uid, full_link)
    except HTTPError:
        logger.warning('Error while fetching the article', exc_info=False)

    if article and not article.body:
        logger.warning('Invalid article. There is no body')
        return None
    
    return article


def _build_link(host, link):
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return f'{host}{link}'
    else:
        return f'{host}/{link}'


def _save_articles(news_site_uid, articles):
    now = datetime.date.today().strftime('%Y_%m_%d')
    # now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = f'{news_site_uid}_{now}.csv'
    # Obtener los atributos del objeto ArticlePage (title y body en este caso)
    # y usarlos como cabeceras del CSV. 
    # Buenas prácticas de programación, se hace lo más general posible.
    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))

    # Se configura para guardarse la carpeta correspondiente
    with open(out_file_name, mode='w+', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)


if __name__ == '__main__':
    # Instancia de un objeto analizador de argumentos
    parser = argparse.ArgumentParser()

    # lista de los nombres de periodicos usados
    news_site_choices = list(config()['news_sites'].keys())

    # Leer de la consola
    # 'news_site': variable donde se guardará el valor recibido por consola
    # help: ayuda para el usuario usando el comando -h
    # type: tipo de dato destino
    # choices: opciones válidas de entrada.
    parser.add_argument('news_site',
                        help='The news site that you want to scrape',
                        type=str,
                        choices=news_site_choices)

    # Instancia de la clase NameSpace retornada por parse_args()
    # cuyos atributos son los nombre definidos en add_argument()
    # Uno solo en este caso. news_site
    args = parser.parse_args()
    _news_scraper(args.news_site)

# Ejecutar de la siguente manera
# $ py Extract\main.py eluniversal
# Ejecutar dentro de la carpeta de archivos para VSCode ETL
    