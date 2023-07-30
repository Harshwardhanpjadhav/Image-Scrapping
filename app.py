import requests
import logging
import os
from bs4 import BeautifulSoup as bs  # For scrapping
from urllib.request import urlopen   # Requesting server

save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)