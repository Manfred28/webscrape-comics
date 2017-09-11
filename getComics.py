import os
from urllib.parse import urlparse
from plyer import notification
from bs4 import BeautifulSoup
import requests

def getLatestComic():
    result = requests.get("http://explosm.net/comics/latest")
    html_doc = result.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    getImageID(soup)
    img_url = getImageUrl(soup)
    return img_url 
    ''' need to get comic id as well,  its in the header '''

def getImageID(soup):
    meta = soup.find(property="og:url")
    img_url_with_id = meta["content"]
    img_id = img_url_with_id.split("/")[-2]
    return img_id

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

''' notification.notify(
    title='Here is the title',
    message='Here is the message',
) '''
