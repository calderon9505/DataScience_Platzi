import logging
logging.basicConfig(level=logging.INFO)

import subprocess
# The subprocess module allows you to spawn new processes, 
# connect to their input/output/error pipes, and obtain their return codes

import datetime
import os

logger = logging.getLogger(__name__)
news_sites_uids = ['eluniversal', 'elpais']

now = datetime.date.today().strftime('%Y_%m_%d')

def main():
    _extract()
    _transform()
    _load()


def _extract():
    for news_site_uid in news_sites_uids:
        subprocess.run(['py', 'main.py', news_site_uid], cwd='./Extract') # Con 'python' no funcionó

    # os.chdir('Extract')
    # for file in os.listdir():
    #     if file.endswith('.csv'):
    #         file_dest = file.split('_')[0]+'.csv'
    #         os.rename(file, file_dest)
    # os.chdir('..')

    logger.info('Extract process ended')


def _transform():
    for news_site_uid in news_sites_uids:
        dirty_filename = f'{news_site_uid}_{now}.csv'
        subprocess.run(['py', 'main.py', '..\\Extract\\'+dirty_filename], cwd='./Transform')

    os.chdir('Extract')
    for file in os.listdir():
        if file.endswith('.csv'):
            os.remove(file)
    os.chdir('..')

    logger.info('Transform process ended')


def _load():
    for news_site_uid in news_sites_uids:
        clean_filename = f'clean_{news_site_uid}_{now}.csv'
        subprocess.run(['py', 'main.py', '..\\Transform\\'+clean_filename], cwd='./Load')

    os.chdir('Transform')
    for file in os.listdir():
        if file.endswith('.csv'):
            os.remove(file)
    os.chdir('..')

    logger.info('Load process ended')


if __name__ == '__main__':
    main()