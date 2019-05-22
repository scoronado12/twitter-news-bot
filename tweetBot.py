# Twitter Bot
import tweepy as tweet
import time

def main():
    print("Bot is running")
    keyfile = open("apikeys.txt", 'r')

    keys = []

    for line in range (0,4):
        keys.append(keyfile.readline().rstrip())


    CONSUMER_KEY = keys[0]

    CONSUMER_SECRET = keys[1]

    ACCESS_KEY = keys[2]

    ACCESS_SECRET = keys[3]

    auth = tweet.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweet.API(auth)

    mentions = api.mentions_timeline()

    for mention in mentions:
        print(str(mention.id)+ ' ' + mention.text)
        add_to_known_mentions(mention.id)
    print("EOF")

def add_to_known_mentions(mention_id):

    known_mentions_file = open("known_mentions.txt", 'r+')




while True:
    main()
    time.sleep(60)
