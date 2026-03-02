import requests
import time
from logger import logger
from config import VS_CURRENCY, REQUEST_TIMEOUT, MAX_RETRIES, BACKOFF_FACTOR, DAYS
from typing import Dict, Any

base_url = 'https://api.coingecko.com/api/v3'

def  fetch_crypto_data(coin_id: str, days: int = 30):
    url = f'{base_url}/coins/{coin_id}/market_chart'
    params = {"vs_currency": VS_CURRENCY
            , "days": DAYS
            }
    
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            data = response.json()
            logger.info(f'Successfully fetched data for {coin_id}')
            return data
        except requests.RequestException as e:
            logger.error(f'Attempt {attempt} - Error fetching crypto data: {e}')
            if attempt < MAX_RETRIES:
                sleep_time = BACKOFF_FACTOR ** (attempt - 1)
                logger.info(f'Retrying in {sleep_time} seconds...')
                time.sleep(sleep_time)
            else:
                logger.error('Max retries reached. Failed to fetch crypto data.')
                raise   