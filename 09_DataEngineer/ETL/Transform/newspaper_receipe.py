import argparse
import logging
from urllib.parse import urlparse
import pandas as pd
import hashlib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(filename):
    logger.info('Starting Data Wragling')
    df = _read_data(filename)
    _add_newspaper_uid_column(df, filename)
    _add_host_column(df)
    _fill_miising_titles(df)
    _generate_uids_index(df)
    _remove_new_lines_from_body(df)
    return df

def _read_data(filename):
    logger.info(f'Reading {filename}')
    return pd.read_csv(filename)

def _add_newspaper_uid_column(df, filename):
    newspaper_uid = filename.split('\\')[2].split('_')[0]
    df['newspaper_uid'] = newspaper_uid
    logger.info(f'newspaper uid column filled: {newspaper_uid}')

def _add_host_column(df):
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)
    logger.info(f'host column filled')

def _fill_miising_titles(df):
    missing_titles_mask = df['title'].isna()
    missing_titles = (
        df[missing_titles_mask]['url']
        .str.extract(r'(?P<missing_titles>[^/]+)$')['missing_titles']
        .str.replace('-',' ').str.capitalize()
    )
    df.loc[missing_titles_mask, 'title'] = missing_titles
    logger.info(f'missing titles filled')

def _generate_uids_index(df):
    uids = (
        df.apply(
            lambda row: hashlib.md5(bytes(row['url'].encode())).hexdigest(),
            axis='columns'
        )
    )
    df['uid'] = uids
    df.set_index('uid', inplace=True)
    logger.info(f'hash index generated')

def _remove_new_lines_from_body(df):
    df['body'] = df['body'].str.replace('\n','')
    logger.info(f'new lines removed from body')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The path to the dirty data', type=str)
    args = parser.parse_args()
    print(args.filename)
    df = main(args.filename)
    print(df[['newspaper_uid','host']])