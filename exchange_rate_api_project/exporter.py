import pandas as pd
from datetime import datetime
import os

filedir = 'output' 
os.makedirs(filedir, exist_ok=True)

def export_to_excel(price_df: pd.DataFrame, summary_df: pd.DataFrame):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'exchange_rate_data_{timestamp}.xlsx'  
    filepath = os.path.join(filedir, filename)   
    
    try:
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            price_df.to_excel(writer, sheet_name="priceData", index=False)
            summary_df.to_excel(writer, sheet_name="summaryData", index=False)

        print(f'Data exported to {filepath}')
    except Exception as e:
        print(f'Error exporting price and summary data to excel: {e}')
        raise

def export_to_exel_v2(data: dict) -> pd.DataFrame:
    exchnageRate_df = pd.DataFrame(data)
    timestamp = datetime.now().strftime('%Y%m%d')
    filename = f'exchange_rate_complete_data_{timestamp}.xlsx'  
    filepath = os.path.join(filedir, filename)   
    
    try:
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer2:
            exchnageRate_df.to_excel(writer2, sheet_name="exchangeRateData", index=False)

        print(f'Complete data exported to {filepath}')
    except Exception as e:
        print(f'Error exporting complete data to excel: {e}')
        raise