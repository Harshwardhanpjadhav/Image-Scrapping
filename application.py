from flask import Flask
import requests
import logging
import os
from bs4 import BeautifulSoup as bs  # For scrapping
from urllib.request import urlopen   # Requesting server

application = Flask('__main__')
app = application


@app.route('/')
def index():
    return 'Hello World!'


if '__main__' == '__name__':
    app.run()
