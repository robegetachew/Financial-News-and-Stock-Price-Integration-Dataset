import pandas as pd

def load_stock_data(file_path):
    # Load the stock price data
    data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    
    # Ensure the data has the necessary columns
    required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    if not all(column in data.columns for column in required_columns):
        raise ValueError(f"Data must include the following columns: {required_columns}")
    
    
    return data
