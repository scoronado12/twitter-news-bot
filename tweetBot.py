# Twitter Bot
# by Stefano C. Coronado
import tweepy as tweet
import tswift as ts
import time

def main():
    print("Refreshing...")
    
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

    api = tweet.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    
    newest_mention, all_tweets = get_latest_tweets(api)
    #all_tweets = api.mentions_timeline()

    reply_to_tweet(api, newest_mention, all_tweets)
    
    
def song_lookup(song_lyric):
    
    song_lyric = song_lyric.split(' ', 1)[1]
    
    
    print("Song Lyrics:" , song_lyric)
    
    the_song = ts.Song.find_song(song_lyric)
    
    if the_song != None:
        #TODO find a better way to retrieve the artist

        song_artist = "That song is called " + the_song.title + " by " + the_song.artist
    else:
        song_artist = "Sorry! I don't recognize those lyrics"
    
    return song_artist
    
    
def reply_to_tweet(api, newest_mention, all_tweets):

    #load tweet ids into array

    already_replied = []

    for mention in all_tweets:
        already_replied.append(mention.id)
    if newest_mention.id not in already_replied:


        if newest_mention.text == "@NenoSong ping":
            api.update_status('@' + newest_mention.user.screen_name + " pong", newest_mention.id)
            print("pong!")
        else:
            if "\n" in newest_mention.text: #if the newest_mention contains newlines
                print("@" + newest_mention.user.screen_name +  " Didn't tweet one line")

                api.update_status('@' + newest_mention.user.screen_name + " Please write one line without line breaks", newest_mention.id)
            else:
                song_info = song_lookup(newest_mention.text)
                api.update_status('@' + newest_mention.user.screen_name + " " + song_info, newest_mention.id)
                print("Sent song info")
    else:

        print("Already responded to this tweet")



def get_latest_tweets(api):
    # try-except because mentions will return an empty list if there are no tweets to this account    
    try:
        mentions = api.mentions_timeline() #list of all tweets where NenoSong is mentioned
        newest_mention = mentions[0]
        
        print("Latest Tweet", newest_mention.id ,'-', newest_mention.text , "from" , newest_mention.user.screen_name)
    except IndexError:
        print("Tweet to this account before trying again")
        exit(1)
    return newest_mention, mentions #return the entire instance to for next func to reply referencing the id
    
    
    
print("Bot is running")
while True:
    main()
    time.sleep(60) #refresh every 60 seconds
