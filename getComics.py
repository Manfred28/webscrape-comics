import os
from bs4 import BeautifulSoup
import requests

class ComicUrlParser:
    img_url = ""

    def __init__(self, url):
        self.url = url
    
    def parse_html(self):
        result = requests.get(self.url)
        html_doc = result.content
        parsed_html = BeautifulSoup(html_doc, 'html.parser')
        img_html_tag = self.parsed_html.find(id="main-comic")
        self.image_url = "http:" + img_html_tag["src"]

''' def getLatestComic():
    result = requests.get("http://explosm.net/comics/latest")
    html_doc = result.content
    soup = BeautifulSoup(html_doc, 'html.parser')

def writeIdToConfig(img_id):
    with open("config.txt", "w") as config:
        config.write(img_id)

def getImageUrl(soup):
    img_tag = soup.find(id="main-comic")
    return "http:" + img_tag["src"] '''


def downloadImageData(latest_comic_url):
    img_data = requests.get(latest_comic_url)
    if img_data.status_code == 200:
        createDestinationFolder()
        createImageFile(img_data)
    else:
        print("Could not download file")

def createDestinationFolder():
    if not os.path.exists('./comics'):
        os.makedirs("./comics")

def createImageFile(img_data):
    img_content = img_data.content
    img_extension = img_data.headers["content-type"].split("/")[1]
    with open('comics/img.' + img_extension, 'wb') as handler:
        handler.write(img_content)


def main():
    CAH_parser = ComicUrlParser("http://explosm.net/comics/latest")
    CAH_parser.parse_html()
    downloadImageData(CAH_parser.image_url)

main()
