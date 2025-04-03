import numpy as np
from intel_news import fetch_news_headlines, analyze_sentiment
from intel_social import fetch_reddit_sentiment, analyze_reddit_sentiment

def get_combined_sentiment():
    news_headlines = fetch_news_headlines()
    reddit_headlines = fetch_reddit_sentiment(["CryptoCurrency", "solana", "CryptoMarkets"])

    news_score = analyze_sentiment(news_headlines)
    reddit_score = analyze_reddit_sentiment(reddit_headlines)

    combined_score = np.mean([news_score, reddit_score])
    print(f"[SENTIMENT] News: {news_score:.3f}, Reddit: {reddit_score:.3f} → Kombiniert: {combined_score:.3f}")
    
    return combined_score, news_headlines + reddit_headlines