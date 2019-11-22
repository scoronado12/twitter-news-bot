# Twitter Bot
# by Stefano C. Coronado
import tweepy as tweet
import feedparser as fp
import time
import datetime


def main():

    try:
        keyfile = open("apikeys.txt", 'r')

        keys = []
        for line in range (0,4):
            keys.append(keyfile.readline().rstrip())

        CONSUMER_KEY = keys[0]
        CONSUMER_SECRET = keys[1]
        ACCESS_KEY = keys[2]
        ACCESS_SECRET = keys[3]

        keyfile.close()

    except:
        print("An Unknown Error has occured importing the API Keys")
        print("Make sure the API Keys are properly formatted into apikeys.txt")
        exit(1)


    auth = tweet.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    twitter = tweet.API(auth ,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    formulate_npr_tweet(twitter)

    exit(0)




def formulate_npr_tweet(api):
    try:

        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M hrs")

        npr_feed = fp.parse("https://www.npr.org/rss/rss.php?id=1001")
        headlines = [] # list of strings


        for i in range(15):
            headlines.append(" - " + npr_feed.entries[i].title)


        low_range = 0
        high_range = 3

        for i in range (5):
            if i == 0:
                message = "From NPR News on " + current_date_time + "(" + str(i+1) + "/5)\n"
            else:
                message = "("+ str(i+1) + "/5)\n"

            for indeces in range(low_range, high_range):
                message += headlines[indeces] + "\n"
            time.sleep(5)
            #print(len(message))
            api.update_status(message)
            low_range += 3
            high_range += 3

    except tweet.error.TweepError:
        print("An unknown error has occured")
        exit(0)

print("Bot is running")
main()
