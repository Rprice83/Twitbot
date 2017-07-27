#!/user/bin/env python

import html
import markovify
from twython import Twython

API_KEY = '8JbYfh5HR82XDl5dzyxcoeLM8'
API_SECRET = 'SmVLV4uN2de78otzJ4j6hIk6seZagN2qZygZlVVJnn7rvXN5Ir'
TOKEN_KEY = '890051182818930688-2ZIIpin8T9PTu8dwMESKRmBbpQcDrAn'
TOKEN_SECRET = 'XkCtYqRkKo6pCbOwhDBERaPQR9Kw5LUOj54kHCHSnJ6ab'

twitter = Twython(API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET)

def create_tweet( file ):
    with open(file, encoding="utf-8") as f:
        text = f.read()

    text_model = markovify.Text(text)
    return text_model.make_short_sentence(140)

def create_sentence( file, target ):
    with open(file, encoding="utf-8") as f:
        text = f.read()
    with open(target, encoding="utf-8") as f:
        target = f.read()

    text_model_a = markovify.Text(text)
    text_model_b = markovify.Text(target)

    model_combo = markovify.combine([text_model_a, text_model_b], [1, 1])

    return model_combo.make_sentence()


def get_user_timeline( screen_name, count=200, max_id=None ):
    user = twitter.lookup_user(screen_name=screen_name.lstrip("@"))
    if user[0]["protected"]:
        return None
    tweets = twitter.get_user_timeline(screen_name=screen_name, count=count, max_id=max_id)

    return tweets

def get_all_tweets():
    alltweets = []
    with open('twit.txt', 'w', encoding="utf-8") as f:
        tweets = get_user_timeline('realDonaldTrump', count=200)
        alltweets.extend(tweets)
        for tweet in tweets:
            f.write(tweet["text"] + '\n')

        oldest = alltweets[-1]["id"] - 1
        while len(tweets) > 0:

            tweets = get_user_timeline('realDonaldTrump', count=200, max_id=oldest)

            alltweets.extend(tweets)

            oldest = alltweets[-1]["id"] - 1

            print("%s tweets downloaded so far" % (len(alltweets)))

            for tweet in tweets:
                f.write(tweet["text"] + '\n')

for i in range(10):
    print(create_sentence("politics1.txt", "twit.txt"))