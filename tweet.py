import tweepy
from auth import (consumer_key, consumer_secret, access_token, access_token_secret)

client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

def tweet(message):
    try:
        tweet = client.create_tweet(text=message)
        print(tweet)
    except:
        print("Error during authentication")


__all__ = ['tweet']