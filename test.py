# https://pydoc.net/tweepy/3.1.0/tweepy.streaming/ 
#https://djoerdhiemstra.com/wp-content/uploads/tr-ctit-15-05.pdf filtering by location
from matatu_auth import *
from file_handling import *
from textblob import TextBlob, Word
from textblob.sentiments import NaiveBayesAnalyzer
import re
from lists import localwords
import time
from datetime import datetime, timedelta

#Create a class inheriting from StreamListener
class MyStreamListener(tweepy.StreamListener):	
	#Diconnect if rate limit is reached
	def on_error(self, status_code):
		if status_code == 420:
			#returning False in on_error disconnects the stream
			print('Custom Error Message: Rate Limit Reached!!! Waiting to recconect')
			return False
			# returning non-False reconnects the stream, with backoff.
	def on_status(self, status):
		print(status.text)

#Create a stream object
myStreamListener = MyStreamListener()

#Connect to the twitter api using the stream
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#track parameter is an array of search terms to stream
#myStream.filter(track= ['javascript'], is_async=True)

#follow parameter is an array of ids - #NTSA_KENYA 2230256532 KENHAKENYA 584840125
#myStream.filter(follow=["2230256532", "584840125"])
#result = api.geo_search(query="nairobi", granularity="city")
#print(result)
#Kenya's geotag id 17ad6a68301cd28b
#Nairobi's geotag id 01b1358f7eda7605

tweet = api.user_timeline('technicollins', tweet_mode = 'extended')
for tweet in tweet:
	print(tweet.id_str + " 	:" + tweet.full_text)