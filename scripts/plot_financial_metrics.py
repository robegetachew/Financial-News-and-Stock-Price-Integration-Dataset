import matplotlib.pyplot as plt

# Function to visualize financial metrics
def plot_financial_metrics(data):

    plt.figure(figsize=(12, 8))
    plt.plot(data['Date'], data['Daily_Return'], label='Daily Return', color='purple')
    plt.title('Daily Return')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.legend()
    plt.grid()
    plt.show()