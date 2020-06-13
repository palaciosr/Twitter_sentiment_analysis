import tweepy 
from tweepy import OAuthHandler
import json
import pandas as pd 
import configparser
from textblob import TextBlob
import sqlite3

from get_authenticated import keys, AuthTwitter

def getQTweets():
   consumer_key,consumer_secret,access_token,access_secret=keys()

   auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)


   #returns the query
   api = tweepy.API(auth)
   for tweet in tweepy.Cursor(api.search, q='U.S. Economy').items(10):
      print(tweet.text)

# x=getQTweets()

#get sentiment on this 

def getTweets():
   api=AuthTwitter()

   name = "bitcoin"
   # Number of tweets to pull
   tweetCount = 6
   # Calling the user_timeline function with our parameters
   results = api.user_timeline(id=name, count=tweetCount)


   #create the tuples for the DB table to input data into
   tweets_in_search=()
   tweets_list_tuples=[]
   for tweet in results:
      # print(tweet.text)
      tweets_in_search=tweet.text
      tweets_list_tuples.append(tweets_in_search)

   return tweets_list_tuples

# save_tweets= getTweets()