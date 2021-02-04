import os
import praw

client_id = os.getenv('PRAW_CLIENT_ID')
client_secret = os.getenv('PRAW_CLIENT_SECRET')
user_agent = os.getenv('PRAW_USER_AGENT')
username = os.getenv('PRAW_USERNAME')
password = os.getenv('PRAW_PASSWORD')

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent, username=username, password=password)
subreddit = reddit.subreddit('emojipasta')
top_posts = subreddit.top(limit=1000)
for submission in top_posts:
	if submission.selftext != "": print(submission.selftext)
