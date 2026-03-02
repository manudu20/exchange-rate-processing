import pandas as pd

def validate_dataframe(df: pd.DataFrame) -> None:
    
    if df.empty:
        raise ValueError('DataFrame is empty')
    
    if df['price'].isnull().any():
        raise ValueError('Price column contains null values')
    
    return True