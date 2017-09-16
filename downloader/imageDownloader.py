import requests

def download_image(episodes, destination):
    number_of_downloaded_episodes = 0
    for file_name, url in episodes.items():
        try:
            img_data = requests.get(url)
            file_name += "." + get_extension(img_data.headers)
            create_image_file(img_data.content, destination, file_name)
            number_of_downloaded_episodes += 1
        except requests.exceptions.RequestException as e:
            print(e)
    return number_of_downloaded_episodes


def get_extension(img_data_headers):
    return img_data_headers["content-type"].split("/")[1]


def create_image_file(img_content, destination, file_name):
    with open(destination + file_name, 'wb') as handler:
        handler.write(img_content)
