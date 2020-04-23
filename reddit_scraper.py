"""
Code for getting reddit data and cleaning it somehow (not sure what)
"""

import pandas as pd
import praw
import psraw

username, password, client_id, client_secret = [line.strip() for line in
                                                open('priv_rsc/reddit_credentials.txt', 'r').readlines()]
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='nlp content gatherer script by /u/ddxgod',
                     username=username,
                     password=password)

# Get the subreddit of r/politics and r/the_donald, see if posts concur with something (not sure what)
politics = reddit.subreddit('politics')
print(len(list(psraw.submission_search(reddit, subreddit='politics', limit=5000, after=0))))
post_list = [item.title for item in politics.top('all')]
df = pd.DataFrame(post_list)
df.to_csv('rsc/posts.csv')
