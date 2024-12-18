import matplotlib.pyplot as plt

def visualize_stock_data(data):
    plt.figure(figsize=(14, 7))
    
    # Plot Closing Price
    plt.subplot(3, 1, 1)
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.plot(data.index, data['SMA_20'], label='20-Day SMA')
    plt.title('Stock Closing Price and SMA')
    plt.legend()
    
    # Plot RSI
    plt.subplot(3, 1, 2)
    plt.plot(data.index, data['RSI_14'], label='RSI (14)')
    plt.axhline(y=70, color='r', linestyle='--')
    plt.axhline(y=30, color='g', linestyle='--')
    plt.title('RSI (14)')
    plt.legend()
    
    # Plot MACD
    plt.subplot(3, 1, 3)
    plt.plot(data.index, data['MACD'], label='MACD')
    plt.plot(data.index, data['MACD_signal'], label='Signal Line')
    plt.bar(data.index, data['MACD_hist'], label='MACD Histogram')
    plt.title('MACD')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
