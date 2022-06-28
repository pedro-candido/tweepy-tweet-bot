import tweepy
from auth import (consumer_key, consumer_secret,
                  access_token, access_token_secret)
from random import random


client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,
                       access_token=access_token, access_token_secret=access_token_secret)


def generate_random_tweet():
    firstWordsList = ['O Fernando ', 'O Rafael ',
                      'O Diego ', 'O Robson ', 'O Pedro ']
    secondWordsList = ['é bonito', 'é cheirador de maconha',
                       'é fedido', 'é cuzão', 'é foda', 'tem pedra', 'tem cabeça de caixa d`agua']

    randomFirstWord = firstWordsList[int(random() * len(firstWordsList))]
    randomSecondWord = secondWordsList[int(random() * len(secondWordsList))]

    return randomFirstWord + randomSecondWord


def tweet(message):
    try:
        tweet = client.create_tweet(text=message)
        print(tweet)
    except:
        print("Error during authentication")


def retweet(tweet_id):
    try:
        tweet = client.retweet(tweet_id)
        print(tweet)
    except:
        print("Error during authentication")


def get_bookmarks():
    try:
        bookmarks = client.bookmarks()
        print(bookmarks)
    except:
        print("Error during authentication")


__all__ = ['get_bookmarks', 'retweet', 'tweet']


def __main__():
    randomPhrase = generate_random_tweet()
    print(randomPhrase)
    # tweet(randomPhrase)


__main__()
