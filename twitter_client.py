import pandas as pd
import random

def fetch_user_tweets(username: str = None, max_tweets: int = 5):
    """
    Load tweets from a local CSV file.
    Ignores the `username` and just returns random samples from the file.
    """
    # Load the CSV file with sample tweets
    df = pd.read_csv("sample_tweets.csv")

    # Randomly select tweets
    sampled = df.sample(n=max_tweets).reset_index(drop=True)

    # Convert to list of dicts (same format as original)
    tweets = []
    for _, row in sampled.iterrows():
        tweets.append({
            "text": row["text"],
            "created_at": None  # Not available in sample data
        })
    return tweets
