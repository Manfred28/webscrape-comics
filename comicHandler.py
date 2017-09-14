import os
import notifications
from cahParser import cah_parser
from xkcdParser import xkcd_parser
from imageDownloader import download_image


class ComicHandler:
    def __init__(self, comic, name, download_destination):
        self.comic = comic()
        self.download_destination = download_destination
        self.name = name

        if not os.path.exists(self.download_destination):
            os.makedirs(self.download_destination)
        number_of_episodes_downloaded = download_image(self.comic.comic_episodes, self.download_destination)
        notifications.send_notification(number_of_episodes_downloaded, self.name)


def main():
    cah_handler = ComicHandler(cah_parser, "Cyanide and Happiness", "./comics/CAH/")
    xkcd_handler = ComicHandler(xkcd_parser, "xkcd", "./comics/xkcd/")

main()
