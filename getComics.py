import os
from bs4 import BeautifulSoup
import requests

def getLatestComic():
    result = requests.get("http://explosm.net/comics/latest")
    html_doc = result.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    getImageId(soup)
    img_url = getImageUrl(soup)
    return img_url

def getImageId(soup):
    img_url_with_id = soup.find(property="og:url")["content"]
    img_id = img_url_with_id.split("/")[-2]
    writeIdToConfig(img_id)

def writeIdToConfig(img_id):
    with open("config.txt", "w") as config:
        config.write(img_id)

def getImageUrl(soup):
    img_tag = soup.find(id="main-comic")
    return "http:" + img_tag["src"]


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
    latest_comic_url = getLatestComic()
    downloadImageData(latest_comic_url)

main()
