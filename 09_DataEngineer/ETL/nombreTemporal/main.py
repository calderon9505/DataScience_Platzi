import argparse
# funciona como una alternativa a la función input que 
# permite agregar los tipos de variables que va a recibir

import logging
from threading import main_thread
# Permite enviar mensajes por consola de manera automatica 
# asignandole un level de importancia a cada tipo de mensaje

from common import config
import news_page_objects as news


logging.basicConfig(level=logging.INFO)
# No mostrar mensajes con nivel menor a INFO
logger = logging.getLogger(__name__)
# Instancia de un logging 


def _news_scraper(news_site_uid):
    # lista con los url definidos en el YAML
    host = config()['news_sites'][news_site_uid]['url']

    # Mostrar mensaje de tipo INFO
    logger.info('Beginning scraper for {}'.format(host))
    # logging.info('Finding links in homepage...')

    # Instancia de news_page_objects
    homepage = news.HomePage(news_site_uid)

    for link in homepage.article_links:
        print(link)
    
    print(len(homepage.article_links))


if __name__ == '__main__':
    # Instancia de un objeto analizador de argumentos
    parser = argparse.ArgumentParser()

    # lista de los nombres de periodicos usados
    news_site_choices = list(config()['news_sites'].keys())

    # Leer de la consola
    # 'news_site': variable donde se guardará el valor recibido por consola
    # help: ayuda para el usuario usando el comando -h
    # type: tipo de dato destino
    # choices: opcioens válidas de entrada.
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
# $ py main.py eluniversal

    