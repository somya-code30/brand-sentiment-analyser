import praw
import pandas as pd

def fetch_reddit_data(keyword, limit=100):
    reddit = praw.Reddit(
        client_id='lBp4XnuyvZxbwmgVE8zyIA',
        client_secret='1KekAYPEFFTobVVeAEdy3AFanDVr1g',
        user_agent='SentimentAnalyzer:v1.0 by /u/AuthorGullible640'
    )

    posts = []
    for submission in reddit.subreddit("all").search(keyword, limit=limit):
        posts.append({
            "time": submission.created_utc,
            "title": submission.title,
            "text": submission.selftext
        })

    df = pd.DataFrame(posts)
    if not df.empty:
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df['text'] = df['title'] + ' ' + df['text']
        return df[['time', 'text']]
    return pd.DataFrame(columns=["time", "text"])  

