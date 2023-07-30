from flask import Flask, jsonify, request, render_template, send_file
import requests
import zipfile
import logging
import os
import shutil
from bs4 import BeautifulSoup as bs  # For scrapping
from urllib.request import urlopen   # Requesting server

# Logging basic Information
logging.basicConfig(filename='scrapper.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

logging.info("APP started Running")

# Object of flask
application = Flask(__name__)
app = application

# Home page route
@app.route('/', methods=["POST", "GET"])
def search():
    '''
    This function is used to search images from google and save it in folder
    return: index.html
    '''
    if request.method == "POST":

        # Creating Directory if not exist
        try:
            save_dir = "images/"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
                logging.info("Success in creating Folder")
        except Exception as e:
            logging.error(f'Unable to create folder {e}')

        # Fetching query from User
        try:
            query = str(request.form.get('query'))
            logging.info("Success in Query Fetch")
        except Exception as e:
            logging.error("Cannot Fetch Query")

        # Checking Response of URL
        try:
            url = f"https://www.google.com/search?q={query}&tbm=isch&ved=2ahUKEwjG1vSQy7WAAxUr5zgGHY97DeQQ2-cCegQIABAA&oq=harry+potter&gs_lcp=CgNpbWcQDFAAWABgAGgAcAB4AIABAIgBAJIBAJgBAKoBC2d3cy13aXotaW1n&sclient=img&ei=FubFZMbzH6vO4-EPj_e1oA4&bih=821&biw=1440&rlz=1C5CHFA_enIN981IN981"
            respone = requests.get(url)
            logging.info(f"Response status{respone}")
        except Exception as e:
            logging.error(f"Unable to get response {e}")

        # Scrapping all images with image tag
        try:
            content = bs(respone.content, "html.parser")
            image_tag = content.find_all("img")
            logging.info("Success in images scrapping")
        except Exception as e:
            logging.error(f"Unable to scrap images {e}")

        # Deleting first image
        try:
            del image_tag[0]
            logging.info("First image deleted")
        except Exception as e:
            logging.error(f"Unable to delete first image {e}")

        # Saving images in folder
        try:
            for i in image_tag:
                img = i['src']
                images = requests.get(img).content
                with open(os.path.join(save_dir, f"{query}{image_tag.index(i)}.jpg"), "wb") as f:
                    f.write(images)
            logging.info("Images saved in folder")
        except Exception as e:
            logging.error(f"Unable to save images in folder {e}")
            
    return render_template("index.html")



















if __name__ == '__main__':
    app.run()
