from flask import Flask, jsonify, request, render_template
import requests
import logging
import os
from bs4 import BeautifulSoup as bs  # For scrapping
from urllib.request import urlopen   # Requesting server

# Logging basic Information
logging.basicConfig(filename='scrapper.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

logging.info("APP started Running")
application = Flask(__name__)
app = application


@app.route('/')
def index():
    
    return render_template('index.html')


if __name__ == '__main__':
	app.run()
