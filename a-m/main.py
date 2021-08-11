import logging
import time

import tweepy
from tweepy import TweepError

from keys import keys

from datetime import datetime

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
ME = keys['me']
AT = keys['handle']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("on")
except:
    print("Error during authentication")


def cyber_attack():
    now = datetime.now()

    print("now =", now)

    tweetids = []
    for status in api.user_timeline(AT):
        # print(status.id)
        tweetids.append(status.id)

    # print(tweetids)
    first_ele = tweetids[0]

    print(first_ele)

    print('Checking to launch cyberattack')

    replies = tweepy.Cursor(api.search, q='to:{}'.format(AT),
                            since_id=first_ele, tweet_mode='extended').items()

    tweets = api.user_timeline(screen_name=AT, tweet_mode='extended', count=1)
    # print(replies)
    reply = next(replies, None)
    print(reply)

    if reply is not None:
        logging.info("reply of tweet:{}".format(reply.full_text))
        print("reply of tweet:{}".format(reply.full_text))
        print('already tweeted')

    if reply is None:
        try:

            for tweet in tweets:
                print('launching cyber attack')
                api.update_status("@" + AT + " Thank you Aidan, Very Cool", in_reply_to_status_id=first_ele)
                print('cyber attack launched')

        except TweepError:
            print('fuck you kaff')

            pass

if __name__ == "__main__":

    while True:
        cyber_attack()
        time.sleep(20)
