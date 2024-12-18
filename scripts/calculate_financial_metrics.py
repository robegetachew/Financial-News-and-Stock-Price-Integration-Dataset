def calculate_financial_metrics(data):
    # Example: Calculate daily returns using PyNance
    data['daily_return'] = data['Close'].pct_change()
    

    return data