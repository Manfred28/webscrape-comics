import requests
import os

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