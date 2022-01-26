import requests
import bs4

from common import config

class NewsPage:

    def __init__(self, news_site_uid, url) -> None:
        self._config = config()['news_sites'][news_site_uid] # url y querys
        self._queries = self._config['queries'] # esto no es necesario. arriba.
        self._html = None
        self._url = url

        self._visit(url)

    def _visit(self, url):
        response = requests.get(url)
        if response.encoding != 'utf-8':
            response.encoding = response.apparent_encoding # cosa rarísima
        response.raise_for_status()
        self._html = bs4.BeautifulSoup(response.text, 'html.parser')

    def _select(self, query_string):
        nodes = self._html.select(query_string)

        if not nodes:
            # print('_select ha retornado None')
            return None

        return nodes
    
    def _print_html(self):
        print(self._html)

class HomePage(NewsPage):

    def __init__(self, news_site_uid, url) -> None:
        super().__init__(news_site_uid, url)

    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

        # Algunos enlaces tienen espacios raros al final y al comienzo
        return set(link['href'].strip() for link in link_list)

    
class ArticlePage(NewsPage):

    def __init__(self, news_site_uid, url) -> None:
        super().__init__(news_site_uid, url)

    @property
    def title(self):
        result = self._select(self._queries['article_title'])
        return None if result is None else result[0].text
    
    @property
    def body(self):
        result = self._select(self._queries['article_body'])
        return None if result is None else result[0].text
    
    @property
    def url(self):
        return self._url