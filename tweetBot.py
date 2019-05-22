# Twitter Bot
import tweepy as tweet

keyfile = open("apikeys.txt", 'r')

keys = []



for _ in range (0,4):
    keys.append(keyfile.readline())


CONSUMER_KEY = keys[0]

CONSUMER_SECRET = keys[1]

ACCESS_KEY = keys[2]

ACCESS_SECRET = keys[3]

print(CONSUMER_KEY)
print(CONSUMER_SECRET)
print(ACCESS_KEY)
print(ACCESS_SECRET)
#auth = tweet.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
