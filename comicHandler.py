import os
import notifications
from cahParser import cah_parser
from xkcdParser import xkcd_parser
from imageDownloader import download_image


class ComicHandler:
    def __init__(self, comic, name, destination):
        self.comic = comic()
        self.download_destination = destination
        self.comic_name = name

        if not os.path.exists(destination):
            os.makedirs(destination)
        number_of_episodes_downloaded = download_image(self.comic.comic_episodes, destination)
        notifications.send_notification(number_of_episodes_downloaded, name)




def main():
    cah_handler = ComicHandler(cah_parser, "Cyanide and Happiness", "./comics/CAH/")
    xkcd_handler = ComicHandler(xkcd_parser, "xkcd", "./comics/xkcd/")

main()
