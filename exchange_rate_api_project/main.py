from api_client import fetch_crypto_data
from transform import transform_data, calculate_summary_stats
from exporter import export_to_excel, export_to_exel_v2
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from config import COINS
from validator import validate_dataframe
from logger import logger


def process_coin(coin: str) -> pd.DataFrame:
    try:
        logger.info(f'Processing {coin}...')
        data = fetch_crypto_data(coin_id=coin, days=30)
        df = transform_data(data, coin)
        validate_dataframe(df)
        summary_df = calculate_summary_stats(df)
        export_to_excel(df, summary_df)
        export_to_exel_v2(data) 
        logger.info(f'Finished processing {coin_id}.')
        return price_df
    except Exception as e:
        logger.error(f'Error processing {coin_id}: {e}')
        raise

def run_process(): 
    try:
        logger.info('Fetching cryptocurrency data...')
        data =  fetch_crypto_data(coin_id='bitcoin', days=30)

        logger.info('Transforming data...')
        df = transform_data(data, coin_id='bitcoin')

        logger.info('Calculating summary statistics...')
        summary_df = calculate_summary_stats(df)

        logger.info('Exporting data to Excel...')
        export_to_excel(df, summary_df)
        export_to_exel_v2(data) 

        logger.info('Process completed successfully.')
    except Exception as e:
        logger.error(f'An error occurred: {e}')


if __name__ == "__main__":
    run_process()