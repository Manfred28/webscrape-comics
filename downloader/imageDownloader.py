import requests


def download_image(episodes, destination):
    downloaded_episodes = []
    for file_name, url in episodes.items():
        try:
            img_data = requests.get(url)
            path = destination + file_name + "." + get_extension(img_data.headers)
            create_image_file(img_data.content, path)
            downloaded_episodes.append(path)
        except requests.exceptions.RequestException as e:
            print(e)
    return downloaded_episodes


def get_extension(img_data_headers):
    return img_data_headers["content-type"].split("/")[1]


def create_image_file(img_content, path):
    with open(path, 'wb') as handler:
        handler.write(img_content)
    