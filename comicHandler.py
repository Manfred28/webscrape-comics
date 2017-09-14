import os
import notifications
from cahParser import cah_parser
from xkcdParser import xkcd_parser
from imageDownloader import download_image

#Could be a simple function...
class ComicHandler:
    def __init__(self, Comic, name, download_destination):
        self.Comic = Comic()
        self.download_destination = download_destination
        self.name = name

        if not os.path.exists(self.download_destination):
            os.makedirs(self.download_destination)
        self.filter_already_downloaded_episodes()
        self.Comic.get_episode_download_links()
        number_of_episodes_downloaded = download_image(self.Comic.episode_download_links, self.download_destination)
        notifications.send_notification(number_of_episodes_downloaded, self.name)


    def filter_already_downloaded_episodes(self):
        new_episodes = {}
        for comic_id in self.Comic.new_episodes.keys():
            episode_file_name = "img" + comic_id
            for downloaded_episodes in os.listdir(self.download_destination):
                if not episode_file_name in downloaded_episodes:
                    new_episodes[comic_id] = self.Comic.new_episodes[comic_id]
        self.Comic.new_episodes = new_episodes


def main():
    cah_handler = ComicHandler(cah_parser, "Cyanide and Happiness", "./comics/CAH/")
    xkcd_handler = ComicHandler(xkcd_parser, "xkcd", "./comics/xkcd/")

main()
