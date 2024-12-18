# Function to analyze statistical properties
def analyze_statistics(data, columns):
    print(data[columns].describe())