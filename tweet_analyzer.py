import csv
from matatu_auth import *
from file_handling import *
from textblob import TextBlob, Word
from textblob.sentiments import NaiveBayesAnalyzer
import re
import time
from datetime import datetime, timedelta

#Function that removes unnecessary info from tweets eg urls, mentions and hashtags
def clean_tweet_text(tweet_text):
    tweet_text = re.sub(r'@[A-Za-z0-9]+', '', tweet_text)
    tweet_text = re.sub(r'#', '', tweet_text)
    tweet_text = re.sub(r'https?:\/\/\S+', '', tweet_text)

    return tweet_text

#Extraction and sentimental analysis of tweets containing local words

def analyse_word_group(arrayname, row_number, last_tweet_analysed_file):#takes the name of the array to use for search, the csv row to edit and file name 
    import_list = __import__('improvedlist')#I added the list module to the path where sys is located
    word_list = getattr(import_list, arrayname, None)
    for word in word_list:
        print("\n\nTWEETS CONTAINING THE WORD " + word.upper() + "\n\n")
        last_tweet_analysed = retrieve_last_tweet_analysed(last_tweet_analysed_file)#save this as default for each file while deploying 1265598536667840514 (27th may tweet)
        keyworded_tweet = api.search(q = word, since_id = last_tweet_analysed, tweet_mode = 'extended')
        for keyworded_tweet in reversed(keyworded_tweet):
            #Check if the exact string exists in tweet text and that the tweet is not a retweet
            if word in keyworded_tweet.full_text:
                if not hasattr(keyworded_tweet, 'retweeted_status'):
                    tweet_text = keyworded_tweet.full_text
                    print("\nORIGINAL TWEET TEXT")
                    print("\nTIME: " + str(keyworded_tweet.created_at) + "   TEXT: " + tweet_text)

                    #Clean the text to improve sentiment analysis accuracy
                    print("\nCLEANED TWEET TEXT")
                    tweet_text = clean_tweet_text(tweet_text)
                    print("\n" + tweet_text)
                    tweet_text = TextBlob(tweet_text, analyzer=NaiveBayesAnalyzer())
                    print(str(tweet_text.sentiment))
                    
                    #Edit the CSV file according to the sentiment analysis result
                    polarity = tweet_text.sentiment.classification
                    if polarity == 'pos':
                        column_number = 1 #column indexed 1 in the csv file is the positive column
                    elif polarity == 'neg':
                        column_number = 3 #column indexed 3 in the csv file is the negative column
                    else:
                        column_number = 2

                    change_sentiment_values(row_number, column_number)

                    #Save the id of the last tweet we have analyzed in a file
                    store_last_tweet_analysed(keyworded_tweet.id_str, last_tweet_analysed_file)

while True:
    analyse_word_group('road_safety_and_accidents', 1, 'last_safety_tweet_analysed.txt')
    analyse_word_group('infrastructure', 2, 'last_infrastructure_tweet_analysed.txt')
    analyse_word_group('general_topics', 3, 'last_general_tweet_analysed.txt')
    print("Analyzed all tweets, going to sleep. Next analysis: " + str(datetime.now() + timedelta(minutes=5)))
    time.sleep(300) #Sleep for 5 minutes