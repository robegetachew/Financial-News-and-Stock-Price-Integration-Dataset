import matplotlib.pyplot as plt

def count_and_plot_publishers(data, column_name='publisher', top_n=10, save_plot=False, plot_path="top_publishers.png"):
    # Count articles per publisher
    publisher_counts = data[column_name].value_counts()

    # Display the top publishers
    print("Top Publishers:")
    print(publisher_counts.head(top_n))

    # Bar plot for the top publishers
    ax = publisher_counts.head(top_n).plot(
        kind='bar',
        figsize=(10, 6),
        color='skyblue',
        edgecolor='black'
    )
    plt.title(f'Top {top_n} Publishers by Article Count')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45, ha='right')

    # Save the plot if required
    if save_plot:
        plt.tight_layout()
        plt.savefig(plot_path)
        print(f"Plot saved to {plot_path}")
    
    plt.show()