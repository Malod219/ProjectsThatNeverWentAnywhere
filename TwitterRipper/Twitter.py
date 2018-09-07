import tweepy

auth = tweepy.OAuthHandler('wasd,
                           'wasd')
auth.set_access_token('wasd',
                      'wasd')

def tweetCheck(user,number):
    loc ="C:/Users/[yourname]/Desktop/Drive/[location]/"
    filename=loc+user+"-TweetHistory.txt"
    tweets=api.user_timeline(screen_name=user,count=number,tweet_mode="extended")
    alltweets=[]
    alltweets.extend(tweets)

    file=open(filename,"w+")

    for item in alltweets:
        try:
            file.write("[+]%s\n" % item.full_text)
        except:
            pass
    


api=tweepy.API(auth)
tweetCheck("TwitterAccountHandle",3200)

