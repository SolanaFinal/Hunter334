from intel_news import fetch_news_headlines, analyze_sentiment as analyze_news_sentiment
from intel_social import fetch_reddit_sentiment, analyze_reddit_sentiment

def get_combined_sentiment():
    try:
        news_headlines = fetch_news_headlines()
        reddit_headlines = fetch_reddit_sentiment(['CryptoCurrency', 'solana', 'CryptoMarkets'])

        news_score = analyze_news_sentiment(news_headlines)
        reddit_score = analyze_reddit_sentiment(reddit_headlines)

        combined_score = (news_score + reddit_score) / 2
        all_headlines = news_headlines + reddit_headlines

        return combined_score, all_headlines

    except Exception as e:
        print(f"[SENTIMENT] Fehler bei der kombinierten Sentiment-Berechnung: {e}")
        return 0.0, []