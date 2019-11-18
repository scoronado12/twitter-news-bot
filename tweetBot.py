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



    while True:

        formulate_npr_tweet(twitter)

        time.sleep(3600) #one hour. Make sure you run this on the 30th minute or on the 00th minute 




def formulate_npr_tweet(api):
    #We will post the latest four headlines
    try:
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M hrs")

        message = current_date_time + " Live from NPR News in Washington (1/4)\n"

        npr_feed = fp.parse("https://www.npr.org/rss/rss.php?id=1001")
        #TODO optimize later 15 headlines will go out in a series of five tweets

        for i in range(0,3):
            message += " - " + npr_feed.entries[i].title + "\n"

        print(message)
        api.update_status(message)

        message = "(2/4)\n"

        for i in range(4,7):
            message += " - " + npr_feed.entries[i].title + "\n"

        print(message)
        api.update_status(message)

        message = "(3/4)\n"


        for i in range(8,11):
            message += " - " + npr_feed.entries[i].title + "\n"

        print(message)
        api.update_status(message)


        message = "(4/4)\n"

        for i in range(12,15):
            message +=  " - " + npr_feed.entries[i].title + "\n"

        #detect that the last dash has been printed
        message += "END OF LINE\n For more details, please visit https://npr.org/"
        print(message)

        api.update_status(message)
    except tweet.error.TweepError:
        print("ERROR One of these statuses have been run already")

print("Bot is running")
main()
