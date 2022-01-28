import argparse
import logging
from urllib.parse import urlparse
import pandas as pd
import hashlib
import nltk
from nltk.corpus import stopwords

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(path):
    logger.info('Starting Data Wragling')
    df = _read_data(path)
    _remove_duplicates(df, 'title')
    _fill_miising_titles(df)
    _drop_rows_with_missing_values(df)
    _remove_new_lines_from_body(df)
    _add_newspaper_uid_column(df, path)
    _add_host_column(df)
    _generate_uids_index(df)
    _add_tokenize_column(df, 'title')
    _add_tokenize_column(df, 'body')
    _save_data(df, path)
    return df

def _read_data(path):
    logger.info(f'Reading {path}')
    return pd.read_csv(path)

def _add_newspaper_uid_column(df, path):
    # No sirve para cualquier Path
    newspaper_uid = path.split('\\')[2].split('_')[0]
    df['newspaper_uid'] = newspaper_uid
    logger.info(f'newspaper uid column filled: {newspaper_uid}')

def _add_host_column(df):
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)
    logger.info('host column filled')

def _fill_miising_titles(df):
    missing_titles_mask = df['title'].isna()
    missing_titles = (
        df[missing_titles_mask]['url']
        .str.extract(r'(?P<missing_titles>[^/]+)$')['missing_titles']
        .str.replace('-',' ').str.capitalize()
    )
    df.loc[missing_titles_mask, 'title'] = missing_titles
    logger.info('missing titles filled')

def _generate_uids_index(df):
    uids = (
        df.apply(
            lambda row: hashlib.md5(bytes(row['url'].encode())).hexdigest(),
            axis='columns'
        )
    )
    df['uid'] = uids
    df.set_index('uid', inplace=True)
    logger.info('hash index generated')

def _remove_new_lines_from_body(df):
    df['body'] = df['body'].str.replace('\n','')
    logger.info('new lines removed from body')

def _add_tokenize_column(df, column):
    stop_words = stopwords.words('Spanish')
    df['n_tokens_'+column] = (
        df[column].dropna()
        .apply(lambda row: nltk.word_tokenize(row))
        .apply(lambda words: list(filter(lambda word: word.isalpha(), words)))
        .apply(lambda words: list(map(lambda word: word.lower(), words)))
        .apply(lambda words: list(filter(lambda word: word not in stop_words, words)))
        .apply(lambda words: len(words))
    )
    logger.info('tokenize column filled')

def _remove_duplicates(df, column):
    df.drop_duplicates(subset=[column], inplace=True)
    logger.info(f'duplicates removed based on: {column}')

def _drop_rows_with_missing_values(df):
    df.dropna()
    logger.info('rows with missing values dropped')

def _save_data(df, path):
    filename = path.split('\\')[2]
    filename = f'.\Transform\clean_{filename}'
    # df.to_csv(filename)
    # La codificación es importante para excel
    # aunque se puede ajustar desde excel
    df.to_csv(filename, encoding='utf-8-sig')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='The path to the dirty data', type=str)
    args = parser.parse_args()
    df = main(args.path)
    print(df.loc[:,'newspaper_uid':])


# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# cd .\09_DataEngineer\ETL\
# .\venv\Scripts\activate
# py .\Transform\newspaper_receipe.py .\Extract\elpais_2022_01_25.csv
# py .\Transform\newspaper_receipe.py .\Extract\eluniversal_2022_01_25.csv
