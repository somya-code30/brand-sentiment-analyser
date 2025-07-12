import streamlit as st
from src.fetch_data import fetch_reddit_data
from src.sentiment_analysis import apply_sentiment
from src.keyword_analysis import get_top_keywords
from src.visualizations import plot_sentiment_pie, plot_time_series, detect_crisis

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")
st.title("Brand Sentiment & Trend Analyzer")

keyword = st.text_input("Enter a brand or keyword:", placeholder="e.g., Zomato, Tesla, ChatGPT")

if keyword:
    df = fetch_reddit_data(keyword)

    if df.empty or 'text' not in df.columns:
        st.warning("No posts found for the given keyword.")
    else:
        df = apply_sentiment(df)

        st.subheader("1. Sentiment Distribution")
        st.pyplot(plot_sentiment_pie(df))

        st.subheader("2. Engagement Over Time")
        st.plotly_chart(plot_time_series(df), use_container_width=True)

        st.subheader("3. Top Keywords")
        top_keywords = get_top_keywords(df['text'])
        for word, freq in top_keywords:
            st.write(f"**{word}** — {freq} mentions")

        st.subheader("4. Crisis Detection")
        if 'time' in df.columns and not df.empty:
            crisis_dates = detect_crisis(df)
            if crisis_dates:
                st.error(f" Crisis Alert Detected on: {', '.join(crisis_dates)}")
            else:
                st.success(" No crisis or negative spike detected.")
        else:
            st.warning("Crisis detection skipped: no time-series data available.")

