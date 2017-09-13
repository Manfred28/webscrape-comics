import os
import requests

def download_image(episodes, destination):
    number_of_downloaded_episodes = 0
    for comic_id, url in episodes.items():
        file_name = "img" + comic_id
        if not already_downloaded(destination, file_name):
            try:
                img_data = requests.get(url)
                ''' if not already_downloaded()(destination):
                    os.makedirs(destination) '''
                file_name += get_extension(img_data.headers)
                create_image_file(img_data.content, destination, file_name)
                number_of_downloaded_episodes += 1
            except requests.exceptions.RequestException as e:
                print(e)
    return number_of_downloaded_episodes


def already_downloaded(destination, file_name):
    for name in os.listdir(destination):
        if file_name in name:
            return True


def get_extension(img_data_headers):
    return img_data_headers["content-type"].split("/")[1]


def create_image_file(img_content, destination, file_name):
    with open(destination + file_name, 'wb') as handler:
        handler.write(img_content)
