
import snscrape.modules.twitter as sntwitter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def fetch_twitter_sentiment(query="solana", limit=50):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        tweets.append(tweet.content)

    sentiments = [sia.polarity_scores(t)["compound"] for t in tweets]
    avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0.0
    return avg_sentiment, tweets

def get_latest_social_sentiment():
    try:
        return fetch_twitter_sentiment()
    except Exception as e:
        print("[SOCIAL ERROR]", e)
        return 0.0, []

if __name__ == "__main__":
    score, tweets = get_latest_social_sentiment()
    print("[TWITTER] Avg Sentiment:", score)
    for t in tweets[:5]:
        print("📝", t)
