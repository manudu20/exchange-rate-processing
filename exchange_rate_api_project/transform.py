import pandas as pd

def transform_data(data: dict) -> pd.DataFrame:
    try:
        prices = data.get('prices', [])
        if not prices:
            raise ValueError("No price data available")
        
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        # Calculate daily returns
        df['daily_return_pct'] = df['price'].pct_change() * 100
        df['7_day_moving_avg'] = df['price'].rolling(window=7).mean()
        return df
    except Exception as e:
        print(f'Error transforming data: {e}')
        raise

def calculate_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    try:
        summary = {
            'Latest price': df['price'].iloc[-1] if not df.empty else None,
            'Average price': df['price'].mean(),
            'Max_price': df['price'].max() if not df.empty else None,
            'Min_price': df['price'].min() if not df.empty else None,
            "Volatility (%)": df['daily_return_pct'].std() if 'daily_return_pct' in df.columns else None
        }
        return pd.DataFrame([summary], index=[0])
    except Exception as e:
        print(f'Error calculating summary statistics: {e}')
        raise