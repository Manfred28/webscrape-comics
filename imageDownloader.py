import requests
import os

def downloadImage(url, destination):
    img_data = requests.get(url)
    if img_data.status_code == 200:
        createDestinationFolder(destination)
        createImageFile(img_data, destination)
    else:
        print("Could not download file")

def createDestinationFolder(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

def createImageFile(img_data, destination):
    img_content = img_data.content
    img_extension = img_data.headers["content-type"].split("/")[1]
    with open(destination + 'img.' + img_extension, 'wb') as handler:
        handler.write(img_content)