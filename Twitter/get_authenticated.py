import tweepy 
from tweepy import OAuthHandler
import json
import pandas as pd 
import configparser
from textblob import TextBlob
import sqlite3




def keys():

   consumer_key=''
   consumer_secret=''
   access_token=''
   access_secret=''

   return consumer_key,consumer_secret,access_token,access_secret

def AuthTwitter():

   consumer_key,consumer_secret,access_token,access_secret = keys()
   
   auth=tweepy.OAuthHandler(str(consumer_key), str(consumer_secret))
   auth.set_access_token(str(access_token), str(access_secret))
   api=tweepy.API(auth)

   return api