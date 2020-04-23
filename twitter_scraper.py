"""
Twitter tweet data collector
"""

import tweepy
import csv
import pandas as pd


# Initialize twitter credentials
credentials = open('priv_rsc/twitter_credentials.txt', 'r').readlines()
consumer_key = credentials[0].split('=')[1].strip()
consumer_secret = credentials[1].split('=')[1].strip()
access_token = credentials[2].split('=')[1].strip()
access_token_secret = credentials[3].split('=')[1].strip()
# print(consumer_key, consumer_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Create csv file to append data
csvfile = open('rsc/covid19_twitter_data.csv', 'w')
csvwriter = csv.writer(csvfile)


"""
# Some max retries exceeded errors, can't get specificed amount
for tweet in tweepy.Cursor(api.search, q='#COVID19', lang='en', since='2020-01-15').items(100000):
    print(tweet.created_at, tweet.text)
    csvwriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
"""