import matplotlib.pyplot as plt

def visualize_sentiment_distribution(data):
    # Count the occurrences of each sentiment category
    sentiment_counts = data['sentiment_label'].value_counts()
    
    # Plot a bar chart of the sentiment distribution
    plt.figure(figsize=(10, 6))
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
    plt.title('Distribution of News Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=0)
    plt.show()

def visualize_sentiment_by_publisher(data, top_n=5):
    # Select the top N publishers
    top_publishers = data['publisher'].value_counts().head(top_n).index
    filtered_df = data[data['publisher'].isin(top_publishers)]
    
    # Group by publisher and sentiment label, then count
    sentiment_by_publisher = filtered_df.groupby(['publisher', 'sentiment_label']).size().unstack(fill_value=0)
    
    # Plot the sentiment distribution by publisher
    sentiment_by_publisher.plot(kind='bar', stacked=True, figsize=(12, 8))
    plt.title('Sentiment Distribution by Publisher')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.show()