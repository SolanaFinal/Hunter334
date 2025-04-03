import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="HunterBot"
)

analyzer = SentimentIntensityAnalyzer()

def fetch_reddit_sentiment(subreddits, post_limit=20):
    all_headlines = []
    for sub in subreddits:
        subreddit = reddit.subreddit(sub)
        for post in subreddit.hot(limit=post_limit):
            if not post.stickied:
                all_headlines.append(post.title)
    return all_headlines

def analyze_reddit_sentiment(headlines):
    scores = [analyzer.polarity_scores(title)['compound'] for title in headlines]
    return np.mean(scores) if scores else 0.0