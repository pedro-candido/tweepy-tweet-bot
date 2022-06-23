import tweepy
import os
from dotenv import load_dotenv

load_dotenv()
consumer_key=os.getenv('API_KEY')
consumer_secret=os.getenv('API_KEY_SECRET')
access_token=os.getenv('ACCESS_TOKEN')
access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

try:
    tweet = client.create_tweet(text='Hello World!')
    print(tweet)
except:
    print("Error during authentication")