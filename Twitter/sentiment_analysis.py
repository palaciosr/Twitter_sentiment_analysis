from textblob import TextBlob

from get_tweets import getTweets


#will get the sentiment for the tweets that capture 



def SentimentOnTweets():
   tweets_in_search=getTweets()
   sentiments=[]

   for i in range(len(tweets_in_search)):

      blob=TextBlob(str(tweets_in_search[i]))
      sentiments.append(blob.sentiment)
   
   return sentiments

sentiment_tweet=SentimentOnTweets()
print(sentiment_tweet)