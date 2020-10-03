"""
Twitter interface controller between the Flask app and the Twitter APIs.
"""
import tweepy
import logging
from constants import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def post_tweet(tweet):
    logging.info("Post message on Twitter")
    return api.update_status(tweet)


def delete_tweet():
    logging.info("Delete message on Twitter")


def fetch_my_tweets():
    logging.info("Fetch tweets of user")
    return api.user_timeline(count=100)


def search_public_tweets(keyword):
    logging.info("Search keyword on Twitter")
    return api.user_timeline(keyword)
