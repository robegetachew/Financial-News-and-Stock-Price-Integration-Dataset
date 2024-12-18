
import pandas as pd
import numpy as np

def apply_technical_indicators(data):
    """
    Apply technical indicators to the stock data.
    Adds columns for Simple Moving Average (SMA), Relative Strength Index (RSI), and MACD.
    """
    try:
        # Simple Moving Average (SMA)
        data['SMA_50'] = data['Close'].rolling(window=50).mean()
        data['SMA_200'] = data['Close'].rolling(window=200).mean()
        
        # Relative Strength Index (RSI)
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        data['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD (12-day EMA - 26-day EMA) and Signal Line (9-day EMA of MACD)
        ema_12 = data['Close'].ewm(span=12, adjust=False).mean()
        ema_26 = data['Close'].ewm(span=26, adjust=False).mean()
        data['MACD'] = ema_12 - ema_26
        data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
        
        return data
    
    except Exception as e:
        raise RuntimeError(f"Error applying technical indicators: {e}")

def calculate_financial_metrics(data):
    """
    Calculate financial metrics for the stock data.
    Adds columns for Daily Returns and Cumulative Returns.
    """
    try:
        # Daily Returns
        data['Daily_Returns'] = data['Close'].pct_change()
        
        # Cumulative Returns
        data['Cumulative_Returns'] = (1 + data['Daily_Returns']).cumprod()
        
        return data
    
    except Exception as e:
        raise RuntimeError(f"Error calculating financial metrics: {e}")

import matplotlib.pyplot as plt

def visualize_stock_data(data):
    """
    Visualize the stock data along with technical indicators.
    Creates subplots for prices, SMA, RSI, and MACD.
    """
    try:
        # Create subplots
        fig, axs = plt.subplots(3, 1, figsize=(14, 10), sharex=True)
        
        # Plot Closing Prices and SMAs
        axs[0].plot(data.index, data['Close'], label='Close', color='blue')
        axs[0].plot(data.index, data['SMA_50'], label='SMA 50', color='orange')
        axs[0].plot(data.index, data['SMA_200'], label='SMA 200', color='green')
        axs[0].set_title('Closing Prices and SMAs')
        axs[0].legend()
        
        # Plot RSI
        axs[1].plot(data.index, data['RSI'], label='RSI', color='purple')
        axs[1].axhline(70, color='red', linestyle='--', label='Overbought')
        axs[1].axhline(30, color='green', linestyle='--', label='Oversold')
        axs[1].set_title('Relative Strength Index (RSI)')
        axs[1].legend()
        
        # Plot MACD and Signal Line
        axs[2].plot(data.index, data['MACD'], label='MACD', color='blue')
        axs[2].plot(data.index, data['Signal_Line'], label='Signal Line', color='orange')
        axs[2].set_title('MACD')
        axs[2].legend()
        
        plt.tight_layout()
        return plt.show()
    
    except Exception as e:
        raise RuntimeError(f"Error visualizing stock data: {e}")
