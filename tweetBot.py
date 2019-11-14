# Twitter Bot
# by Stefano C. Coronado
import tweepy as tweet
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

    while True:
        #TODO more logic
        time.sleep(20) #seconds
        message = "Live from NPR News in Washington this is is @BotNeno"
        print("sending a ping to the account")
        twitter.update_status("pong") #send the word pong



print("Bot is running")
main()
