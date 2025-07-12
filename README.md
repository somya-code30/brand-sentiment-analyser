# Brand Sentiment & Trend Analyzer

A real-time dashboard that fetches Reddit posts for a given keyword, analyzes sentiment, detects crisis events, and extracts trending keywords.

## Features
- Pulls Reddit posts using PRAW
- Performs sentiment analysis with VADER
- Detects spikes in negative sentiment (crisis detection)
- Displays trending keywords
- Built with Streamlit

## Folder structure
sentiment-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── src/
    ├── fetch_data.py
    ├── sentiment_analysis.py
    ├── keyword_analysis.py
    └── visualizations.py


## Setup
1. Replace your Reddit credentials in `src/fetch_data.py`
2. Run the app:
```bash
pip install -r requirements.txt
streamlit run app.py
