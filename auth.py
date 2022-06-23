import os
from dotenv import load_dotenv

load_dotenv()
consumer_key=os.getenv('API_KEY')
consumer_secret=os.getenv('API_KEY_SECRET')
access_token=os.getenv('ACCESS_TOKEN')
access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')

__all__ = ['consumer_key', 'consumer_secret', 'access_token', 'access_token_secret']