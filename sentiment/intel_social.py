import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")

analyzer = SentimentIntensityAnalyzer()

def fetch_reddit_headlines():
    try:
        headers = {"User-Agent": "HunterBotSentiment/1.0"}
        url = "https://www.reddit.com/r/CryptoCurrency/top/.json?limit=10&t=day"
        response = requests.get(url, headers=headers)
        data = response.json()
        posts = data["data"]["children"]
        return [post["data"]["title"] for post in posts]
    except Exception as e:
        print(f"[REDDIT] Fehler beim Abrufen: {e}")
        return []

def fetch_twitter_headlines():
    try:
        # Dummy-Fallback – hier später echten Zugriff auf X/Twitter API integrieren
        return [
            "Bitcoin reaches new all-time high",
            "Solana gains traction with new dApp launches",
            "Crypto market dips amid global uncertainty",
        ]
    except Exception as e:
        print(f"[X] Fehler beim Abrufen: {e}")
        return []

def analyze_sentiment(texts):
    scores = []
    for text in texts:
        sentiment = analyzer.polarity_scores(text)
        scores.append(sentiment["compound"])
    if scores:
        return sum(scores) / len(scores)
    return 0.0

def get_latest_social_sentiment():
    reddit = fetch_reddit_headlines()
    twitter = fetch_twitter_headlines()
    all_social = reddit + twitter
    score = analyze_sentiment(all_social)
    return score, all_social