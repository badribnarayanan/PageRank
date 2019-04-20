from flask import Flask
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
from flask import Response
from lib import page_rank


app = Flask(__name__)
flask_port = 8000


@app.route('/')
def hello():
	"""Return a friendly HTTP greeting."""
	print(google.__path__)
	return 'Welcome to Webpage!'




@app.route('/page_rank')
def main():

	url_link = input()
	
	page_rank.calc_page_rank(url_link)

	return "Fetched Words"




if __name__ == '__main__':
	# This is used when running locally only. When deploying to Google App
	# Engine, a webserver process such as Gunicorn will serve the app. This
	# can be configured by adding an `entrypoint` to app.yaml.
	#app.run(host='0.0.0.0', port=flask_port, debug=True)
	app.run(host='0.0.0.0', port=flask_port, debug=True)
	
# [END gae_python37_app]


