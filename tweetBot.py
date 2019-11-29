# Twitter Bot
# by Stefano C. Coronado
import tweepy as tweet
import feedparser as fp
import time


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
    time.sleep(10)
    formulate_bbc_tweet(twitter)
    time.sleep(10)
    formulate_nytimes_tweet(twitter)
    exit(0)

def formulate_nytimes_tweet(api):
    print("Attempting to send NY Times Headlines")
    try:
        nytimes_feed = fp.parse("https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml")

        headlines = []
        for i in range(len(nytimes_feed.entries)):
            headlines.append(" - " + nytimes_feed.entries[i].title)

        #for headline in headlines:
            #print(headline)

        low_range = 0
        high_range = 2
        for i in range(5):
            message = "From the NY Times (" + str(i+1)+ "/5)\n"

            for indeces in range(low_range, high_range):
                message += headlines[indeces] + "\n"

            time.sleep(5)
            print(message)
            api.update_status(message)
            low_range += 2
            high_range += 2

    except tweet.error.TweepError:
            print("An unknown error has occured")
            exit(0)

def formulate_bbc_tweet(api):
    '''This function aggregates the BBC world news feed and splits the headlines'''

    print("Attempting to Send BBC Headlines")

    try:

        #TODO send 7 tweets of four headlines
        bbc_feed = fp.parse("http://feeds.bbci.co.uk/news/world/rss.xml#")

        headlines = []

        for i in range(len(bbc_feed.entries)):
           headlines.append(" -  " + bbc_feed.entries[i].title)

        low_range = 0
        high_range = 4

        for i in range (7):

            message = "("+ str(i+1) + "/7) BBC News\n"

            for indeces in range(low_range, high_range):
                message += headlines[indeces] + "\n"
            time.sleep(5) # eliminate possibility of getting ratelimited
            print(message)
            api.update_status(message)
            low_range += 4
            high_range += 4




    except tweet.error.TweepError:
            print("An unknown error has occured")
            exit(0)



def formulate_npr_tweet(api):

    '''This function aggregates the NPR RSS Feed and splits the headlines into
                a series of five tweets'''
    print("Attempting to send NPR Headlines")

    try:


        npr_feed = fp.parse("https://www.npr.org/rss/rss.php?id=1001")
        headlines = [] # list of strings


        for i in range(15):
            headlines.append(" - " + npr_feed.entries[i].title)


        low_range = 0
        high_range = 3

        for i in range (5):
            message = "From NPR News (" + str(i+1) + "/5)\n"

            for indeces in range(low_range, high_range):
                message += headlines[indeces] + "\n"
            time.sleep(5) # eliminate possibility of getting ratelimited
            print(message)
            api.update_status(message)
            low_range += 3
            high_range += 3

    except tweet.error.TweepError:
        print("An unknown error has occured")
        exit(0)

print("Bot is running")
main()
