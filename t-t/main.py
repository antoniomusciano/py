import time
import schedule
import matplotlib.pyplot as plt
import numpy as np
import tweepy
from datetime import date

from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
AT = keys['handle']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


class Error(Exception):
    pass


class Unverified(Error):
    pass


try:
    api.verify_credentials()
    print("on")
except Unverified:
    print("Error during authentication")


def gathering():
    plt.style.use('seaborn')
    list_of_date_times = []
    final = []
    tweet_ids = []

    for status in api.user_timeline(AT):
        tweet_ids.append(str(status.id))
    for status in api.user_timeline(AT):
        list_of_date_times.append(str(status.created_at))  # time is in UTC

    for dates in list_of_date_times:
        times = dates.split()[-1]
        final.append(times)

    plotting(final, tweet_ids)


def plotting(times, tweets):
    # Line length so the IDS aren't covered
    levels = np.tile([-5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(times) / 6)))[:len(times)]

    # Create figure and plot a stem plot with the times
    fig, ax = plt.subplots(figsize=(15, 5), constrained_layout=True)
    ax.set(title="Menace Activity")
    marker_line, stem_line, baseline = ax.stem(times, levels,
                                               linefmt="C3-", basefmt="k-",
                                               use_line_collection=True)

    # Getting the vert
    plt.setp(marker_line, mec="k", mfc="w", zorder=3)
    marker_line.set_ydata(np.zeros(len(times)))
    vert = np.array(['bottom', 'top'])[(levels > 0).astype(int)]

    # Annotating the Stems
    for d, l, r, va in zip(times, levels, tweets, vert):
        ax.annotate(r, xy=(d, l), xytext=(60, np.sign(l) * 15),
                    textcoords="offset points", va=va, ha="right")

    # Remove y axis labels
    ax.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)

    # Show and export graph
    fig1 = plt.gcf()
    plt.show()
    plt.draw()
    fig1.savefig('menace' + str(date.today()) +'.png', dpi=100)
    print('Graph Exported.')


if __name__ == "__main__":
    schedule.every().day.at("menace time").do(gathering) # Set to the time you want this to run

    while True:
        schedule.run_pending()
        time.sleep(1)



