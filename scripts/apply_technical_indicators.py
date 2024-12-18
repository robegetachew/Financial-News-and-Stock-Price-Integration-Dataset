import talib as ta

def apply_technical_indicators(df):
    """
    Apply technical indicators (SMA, RSI, MACD) to the stock data.

    Parameters:
    - df: pandas DataFrame containing stock data with a 'Close' column.

    Returns:
    - df: pandas DataFrame with added technical indicators.
    """
    # Calculate Simple Moving Average (SMA)
    df['SMA_20'] = ta.SMA(df['Close'], timeperiod=20)
    
    # Calculate Relative Strength Index (RSI)
    df['RSI_14'] = ta.RSI(df['Close'], timeperiod=14)
    
    # Calculate Moving Average Convergence Divergence (MACD)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = ta.MACD(df['Close'], 
                                                              fastperiod=12, 
                                                              slowperiod=26, 
                                                              signalperiod=9)

    return df
