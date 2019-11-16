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

    #while True:
        #time.sleep(20) #seconds
        #print("sending a ping to the account")
        #twitter.update_status("pong") #send the word pong
    print(formulate_npr_tweet(twitter)) 

def formulate_npr_tweet(api):
    #We will post the latest four headlines

    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M hrs")

    message = current_date_time + " Live from NPR News in Washington\n\n"

    npr_feed = fp.parse("https://www.npr.org/rss/rss.php?id=1001")

    for i in range(3):
        message += " - " + npr_feed.entries[i].title + "\n"

    print("Length of tweet " + str(len(message)))

    #TODO

    return message

    #TODO add in the other


print("Bot is running")
main()
