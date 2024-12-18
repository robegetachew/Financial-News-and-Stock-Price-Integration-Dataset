from gensim import corpora
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models import LdaModel

def perform_topic_modeling_gensim(df, num_topics=5, num_words=10, sample_size=None):
    # Subsample the data if a sample size is provided
    if sample_size:
        df = df.sample(n=sample_size, random_state=42)

    # Initialize CountVectorizer for basic keyword extraction
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(df['headline'])
    vocab = vectorizer.get_feature_names_out()

    # Convert to gensim format
    corpus = [[(i, freq) for i, freq in zip(doc.indices, doc.data)] for doc in dtm]
    id2word = corpora.Dictionary([vocab])

    # Fit LDA model using gensim
    lda_model = LdaModel(corpus=corpus, num_topics=num_topics, id2word=id2word, passes=15, random_state=42)

    # Print topics
    topics = lda_model.print_topics(num_topics=num_topics, num_words=num_words)
    for topic in topics:
        print(topic)

    return lda_model, corpus, id2word