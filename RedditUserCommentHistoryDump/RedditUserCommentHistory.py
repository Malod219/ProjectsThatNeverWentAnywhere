import praw

r = praw.Reddit(user_agent='HelloIamaspecialPerson',
                client_id="0LAftlRMvddcSg",
                client_secret="awdsa",
                password="wadaws",
                username="wads"

                )
def historysearch(person):
    allmessages=[]
    user = r.redditor(person)
    loc ="C:/Users/AAZ/Desktop/Drive/Tech/Scripting/Python/FirKit/Web Recon/AllRedditCommentHistories/"
    filename=loc+person+"-RedditCommentHistory.txt"

    for comment in user.comments.new(limit=None):
        message=("[+] "+comment.body)
        allmessages.append(message)

    file=open(filename,"w+")

    for item in allmessages:
        try:
            file.write("%s\n" % item)
        except:
            pass

userlisttosearch=["names of users","other names"]
for user in userlisttosearch:
    try:
        historysearch(user)
    except:
        print("Failed to get information on "+user)
