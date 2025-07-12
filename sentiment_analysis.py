from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def apply_sentiment(df):
    analyzer = SentimentIntensityAnalyzer()

    def get_sentiment(text):
        score = analyzer.polarity_scores(str(text))['compound']
        return 'positive' if score > 0.05 else 'negative' if score < -0.05 else 'neutral'

    df['sentiment'] = df['text'].apply(get_sentiment)
    return df
