"""
Twitter Flask app to render web UI based on user interactions.
"""
from flask import Flask
from flask import render_template
from flask import request
from tweepy import TweepError

import twitter_controller as tc

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html",
        active_tab='home')


@app.route("/timeline")
def timeline():
    my_tweets = tc.search_public_tweets(None)
    return render_template(
        "timeline.html",
        my_tweets=my_tweets,
        active_tab='timeline')


@app.route("/post_tweet")
def post_tweet():
    try:
        status = "yet_to_post"
        tweet = request.args.get('tweet_text')
        if tweet:
            if tc.post_tweet(tweet):
                status = "posted"
        return render_template(
            "post_tweet.html",
            active_tab='post_tweet',
            status=status)
    except TweepError as e:
        handle_exception(e)


@app.route("/delete_tweet")
def delete_tweet():
    try:
        return render_template(
            "delete_tweet.html",
            active_tab='delete_tweet')
    except TweepError as e:
        handle_exception(e)


@app.route("/search_tweets")
def search_tweets():
    try:
        keyword = request.args.get('search_key')
        public_tweets = tc.search_public_tweets(keyword)
        return render_template(
            "search_tweets.html",
            public_tweets=public_tweets,
            active_tab='search_tweets')
    except TweepError as e:
        handle_exception(e)


def handle_exception(e):
    return render_template("error.html", message=e.message)


if __name__ == "__main__":
    app.run(debug=True)
