
import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def fetch_news_headlines(query="crypto", count=5):
    url = f"https://gnews.io/api/v4/search?q={query}&lang=en&max={count}&token=756f91534fdcea39047d244e537851cc"
    try:
        response = requests.get(url)
        data = response.json()
        headlines = [article["title"] for article in data.get("articles", [])]
        return headlines
    except Exception as e:
        print(f"[NEWS] Fehler beim Abrufen von News: {e}")
        return []

def analyze_sentiment(headlines):
    sid = SentimentIntensityAnalyzer()
    if not headlines:
        return 0.0, []

    scores = [sid.polarity_scores(h)["compound"] for h in headlines]
    avg_score = sum(scores) / len(scores)
    return round(avg_score, 3), headlines
