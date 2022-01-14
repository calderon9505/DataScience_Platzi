import lxml.html as html
import requests
import os
import datetime

HOME_URL = 'https://www.larepublica.co/'

# XPATH_LINKS = '//h2[@class]/a[contains(@href,"www.larepublica.co")]/@href'
XPATH_LINKS = '//text-fill/a[contains(@href,"www.larepublica.co/economia")]/@href'
# XPATH_TITLE = '//div[@class="mb-auto"]/h2/span/text()'
XPATH_TITLE = '//div[@class="mb-auto"]/text-fill/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p/descendant-or-self::text()'


def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                # title = title.replace('\"','')
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                # summary = summary.replace('\"','')
                body = parsed.xpath(XPATH_BODY)
            except IndexError as ie: # Para cuando no existe summary
                print(ie)
                return

            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')

        else:
            raise ValueError(f'Error: {response.status_code}') 
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')

            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINKS)
            print(len(links_to_notices))

            today = str(datetime.date.today())
            if not os.path.isdir(today):
                os.mkdir(today)
            
            for link in links_to_notices:
                response = parse_notice(link, today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()

# Los h2 que contienen el atributo "class" hacen parte de las tendencias
# y por tanto pueden ser noticias repetidas. O tambien hacen parte de
# ciertas secciones especiales que no son noticias como tal

# Al hacer home = response.content.decode('utf-8') los "h2" se 
# eliminan y surgen "text-fill" que no tienen atrituto @class

# Al crear un archivo con "open" y ejecutar el código con ctrl+alt+r
# el archivo se crea por defecto en la carpeta del entorno de trabajo de
# VSCode. por lo que debo ir hasta la carpeta del archivo python.
# ¿Será igual para leer? 
