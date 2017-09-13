import requests
import os

def download_image(url, comic_id, destination):
    try: 
        img_data = requests.get(url)
        create_destination_folder(destination)
        file_name = create_file_name(img_data.headers, comic_id)
        create_image_file(img_data.content, destination, file_name)
    except requests.exceptions.RequestException as e:
        print(e)

def create_destination_folder(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

def create_file_name(img_data_headers, comic_id):
    img_extension = img_data_headers["content-type"].split("/")[1]
    return "img" + comic_id + "." + img_extension

def create_image_file(img_content, destination, file_name):
    with open(destination + file_name, 'wb') as handler:
        handler.write(img_content)