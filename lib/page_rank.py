import urllib.request
import requests
from datetime import datetime
import psycopg2
import csv
import os
import datetime
import time
import sys 
import google
import pandas as pd
import json
from bs4 import BeautifulSoup 
import operator 
from collections import Counter
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import nltk
from nltk.stem import WordNetLemmatizer 
from pytrends.request import TrendReq


nltk.download('stopwords')
pytrends = TrendReq(hl='en-US', tz=360)


  
# Function removes any unwanted symbols 
def clean_wordlist(wordlist): 
	  
	clean_list =[] 
	for word in wordlist: 
		symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
		  
		for i in range (0, len(symbols)): 
			word = word.replace(symbols[i], '') 
			  
		if len(word) > 0: 
			clean_list.append(word) 


	en_stops = set(stopwords.words('english'))

	word_list = []
	for word in clean_list:
		if word not in en_stops:

			word_list.append(word)
	

	unique_list = []
	for x in word_list:

		if x not in unique_list:

			unique_list.append(x) 


	return unique_list
	# create_dictionary(clean_list) 


  

def get_text_from_url(url_link):

	wordlist = [] 
	html_data =  requests.get(url_link).text 
	# data = data.decode('utf-8')
	
	soup = BeautifulSoup(html_data, 'html.parser')

	# Text in given web-page is stored under 
	# the <div> tags with class <entry-content> 
	for each_text in soup.findAll('div'): 
		content = each_text.text 
  
		# use split() to break the sentence into  
		# words and convert them into lowercase  
		words = content.lower().split() 
		  
		for each_word in words: 
			wordlist.append(each_word) 
		
		clean_words =  clean_wordlist(wordlist)

	# print(clean_words)

	return clean_words




def search_trends(word_list):

	print(word_list)

	df_list = pd.DataFrame([], index = ['date'])


	for word in word_list:

		word = [word]

		pytrends = TrendReq(hl='en-US', tz=360)
		pytrends.build_payload(word, cat=0, timeframe='today 5-y', geo='', gprop='')


		interest_over_time_df = pytrends.interest_over_time()

		interest_over_time_df = interest_over_time_df.reset_index()
		interest_over_time_df = interest_over_time_df[(interest_over_time_df["date"] <= '2019-04-17') & (interest_over_time_df["date"] > '2019-03-17')]

		interest_over_time_df = interest_over_time_df.drop(["isPartial"], axis = 1)

		interest_over_time_df = interest_over_time_df.set_index('date')

		df_list = pd.concat([df_list, interest_over_time_df], axis=1)


	df_list = df_list.reset_index()

	

	# print(df_list)





def calc_page_rank(url_link):

	print("Getting word list from url")
	word_list = get_text_from_url(url_link)

	print("Getting trends data")
	search_trends(word_list)






