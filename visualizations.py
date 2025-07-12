import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

def plot_sentiment_pie(df):
    sentiment_counts = df['sentiment'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%')
    ax.axis('equal')
    return fig

def plot_time_series(df):
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)

    # Group by day and sentiment
    daily_sentiment = df.groupby([pd.Grouper(freq='D'), 'sentiment']).size().unstack().fillna(0)

    # Create interactive Plotly chart
    fig = go.Figure()

    for sentiment in ['positive', 'neutral', 'negative']:
        if sentiment in daily_sentiment.columns:
            fig.add_trace(go.Scatter(
                x=daily_sentiment.index,
                y=daily_sentiment[sentiment],
                mode='lines+markers',
                name=sentiment.capitalize()
            ))

    fig.update_layout(
        title='Engagement & Sentiment Over Time',
        xaxis_title='Date',
        yaxis_title='Number of Posts',
        hovermode='x unified',
        template='plotly_white',
        legend_title_text='Sentiment'
    )

    return fig

def detect_crisis(df):
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    neg_counts = df[df['sentiment'] == 'negative'].resample('D').size()
    zscores = (neg_counts - neg_counts.mean()) / neg_counts.std()
    crisis_dates = zscores[zscores > 2].index.strftime('%Y-%m-%d').tolist()
    return crisis_dates
