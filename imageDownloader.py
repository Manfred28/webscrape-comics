import requests
import os

def downloadImage(url, comic_id, destination):
    try: 
        img_data = requests.get(url)
        createDestinationFolder(destination)
        file_name = createFileName(img_data.headers, comic_id)
        createImageFile(img_data.content, destination, file_name)
    except requests.exceptions.RequestException as e:
        print(e)

def createDestinationFolder(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

def createFileName(img_data_headers, comic_id):
    img_extension = img_data_headers["content-type"].split("/")[1]
    return "img" + comic_id + "." + img_extension

def createImageFile(img_content, destination, file_name):
    with open(destination + file_name, 'wb') as handler:
        handler.write(img_content)