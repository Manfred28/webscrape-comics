import requests
import os

def downloadImage(url, comic_id, destination):
    try: 
        img_data = requests.get(url)
        createDestinationFolder(destination)
        createImageFile(img_data, comic_id, destination)
    except requests.exceptions.RequestException as e:
        print(e)

def createDestinationFolder(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

def createImageFile(img_data, comic_id, destination):
    img_content = img_data.content
    img_extension = img_data.headers["content-type"].split("/")[1]
    with open(destination + 'img' + comic_id + "." + img_extension, 'wb') as handler:
        handler.write(img_content)