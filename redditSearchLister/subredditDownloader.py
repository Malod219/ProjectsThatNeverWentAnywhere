import praw

#Create a reddit instance with relevant information
reddit = praw.Reddit(
	client_id = 'clientID',
	client_secret = 'clientSecret',
	user = 'username',
	password = 'password',
	user_agent = 'userAgent'
	)

#Select subreddit
subreddit = reddit.subreddit('UnknownTradeCo')
#Gather list of posts
posts = subreddit.search("title:THE EMPIRE - The Company's Official News Source",sort='new',limit=2000)
#Declare string variable
longstr=""

#Loop posts to get the count, title and URL of that post
for count ,post in enumerate(posts):
	longstr += str(count) + " : (" + post.title + ")[" + post.url + "]\n"

#Write it all to a text file
with open("Empires.txt","w+") as file:
	file.write(longstr)
