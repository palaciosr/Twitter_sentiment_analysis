import tweepy 
from tweepy import OAuthHandler
import json
import pandas as pd 
import configparser
from textblob import TextBlob
import sqlite3
#includes twitter's api with tweepy library 
#http://docs.tweepy.org/en/v3.5.0/streaming_how_to.html

#textblob sentiment analysis documentation
#https://textblob.readthedocs.io/en/dev/

#this is the full script which:
#authenticates, get tweets, pulls them into 
#sqlite, and last gives setntiment

def keys():

   consumer_key='your keys'
   consumer_secret='your keys'
   access_token='your keys'
   access_secret='your keys'



def AuthTwitter():
   


   auth=tweepy.OAuthHandler(str(consumer_key), str(consumer_secret))
   auth.set_access_token(str(access_token), str(access_secret))
   api=tweepy.API(auth)

   return consumer_key,consumer_secret



def getQTweets():
   consumer_key,consumer_secret=AuthTwitter()

   auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)


   #returns the query
   api = tweepy.API(auth)
   for tweet in tweepy.Cursor(api.search, q='U.S. Economy').items(10):
      print(tweet.text)

x=getQTweets()

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

# g=getTweets()
# print(g)

def TweetsToDB():
   tweets=getTweets()

   #would include directory
   conn=sqlite3.connect('twitter.db')
   c=conn.cursor()
   # initialize table once 
   # c.execute('''CREATE TABLE TWEETS (tweet text)  ''')

   c.executemany('''INSERT INTO TWEETS VALUES (?)''',(tweets,))

#insert into the table 

   conn.commit()
   conn.close()

def QueryDB():
   conn=sqlite3.connect('twitter.db')
   c=conn.cursor()

   c.execute('''SELECT * FROM TWEETS''')

   results=c.fetchall()

   return results

def TuplesToDF():

   t=TweetsToDB()
   #returns a list of tuples 
   q=QueryDB()

   df=pd.DataFrame(q,columns=['TweetText'])
   
   x=df.head()

   return x

# data=TuplesToDF()
# print(data)



def SentimentOnTweets():
   tweets_in_search=getTweets()
   sentiments=[]

   for i in range(len(tweets_in_search)):

      blob=TextBlob(str(tweets_in_search[i]))
      sentiments.append(blob.sentiment)
   
   return sentiments

# sentiment_tweet=SentimentOnTweets()
# print(sentiment_tweet)


