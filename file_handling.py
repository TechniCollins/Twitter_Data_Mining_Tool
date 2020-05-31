import csv
sentiment_file = 'sentiment_data.csv'

def retrieve_last_tweet_analysed(file_name):
	f_read = open(file_name, 'r')
	last_analysed = int(f_read.read().strip())
	f_read.close()
	return last_analysed

def store_last_tweet_analysed(last_tweet_analysed, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_tweet_analysed))
    f_write.close()
    return

#Read the number that needs to be updated, and the entire list
def read_sentiments_from_csv(row_to_update, column_to_update):
	with open(sentiment_file, mode = 'r') as read_analysis_data:
		read_data_from_file = csv.reader(read_analysis_data, delimiter=',')
		entirelist = list(read_data_from_file)#returns a list of rows from the csv file
		value_to_change = int(entirelist[row_to_update][column_to_update])
		return {'value_to_change':value_to_change, 'entirelist':entirelist}#returns two items, which we store in a dictionary

#Make changes to the csv file
def write_sentiments_to_csv(newlist):#Create Csv file if it doesn't exist
	with open(sentiment_file, mode = 'w', newline= '') as  write_analysis_data:
		write_data_to_file = csv.writer(write_analysis_data, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
		write_data_to_file.writerows(newlist)#route related tweets sentiment results

def change_sentiment_values(row_number, column_number):
	return_dict = read_sentiments_from_csv(row_number,column_number)
	value_to_change = return_dict['value_to_change']
	entirelist = return_dict['entirelist']
	newvalue = value_to_change+ 1
	entirelist[row_number][column_number] = str(newvalue)
	newlist = entirelist
	write_sentiments_to_csv(newlist)