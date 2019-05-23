# Twitter Bot
import tweepy as tweet
import time

def main():
    
    print("Bot is running")
    try:
        keyfile = open("apikeys.txt", 'r')

        keys = []

        for line in range (0,4):
            keys.append(keyfile.readline().rstrip())


        CONSUMER_KEY = keys[0]

        CONSUMER_SECRET = keys[1]

        ACCESS_KEY = keys[2]

        ACCESS_SECRET = keys[3]
        
    except:
        print("An Unknown Error has occured importing the API Keys")
        print("Make sure the API Keys are properly formatted into apikeys.txt")
        exit(1)
        
        
    auth = tweet.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweet.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify = True)
    
    newest_mention = get_latest_tweet(api)
    
    reply_to_tweet(api, newest_mention)
    
    
    
    
def reply_to_tweet(api, newest_mention):
    
    try:
        if newest_mention.text == "@BotNeno ping":
            print("pong!")
            api.update_status('@' + newest_mention.user.screen_name + " pong", newest_mention.id)
    except tweet.error.TweepError: #try not to respond again on the next query
        print("Already responded to this!")
    
def get_latest_tweet(api):

    mentions = api.mentions_timeline() #list of all tweets where @BotNeno is mentioned
    
    newest_mention = mentions[0]
    
    print("Latest Tweet", newest_mention.id ,'-', newest_mention.text , "from" , newest_mention.user.screen_name)
    
    return newest_mention #return the entire instance to for next func to reply referencing the id
    

while True:
    main()
    time.sleep(30) #refresh every 30 seconds
