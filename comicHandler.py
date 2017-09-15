import os
import notifications
from rssScraper import RssScraper
from cahParser import cah_parser
from xkcdParser import xkcd_parser
from imageDownloader import download_image

#Could be a simple function...
class ComicHandler:
    def __init__(self, Comic, rss_feed, name, download_destination):
        self.latest_episodes = RssScraper(rss_feed).latest_episodes
        self.filtered_episodes = {}
        self.Comic = Comic()
        self.download_destination = download_destination
        self.name = name

        self.generator()


    def generator(self):
        if not os.path.exists(self.download_destination):
            os.makedirs(self.download_destination)
        self.filter_already_downloaded_episodes()
        self.Comic.get_episode_download_links(self.filtered_episodes)
        number_of_episodes_downloaded = download_image(self.Comic.episode_download_links, self.download_destination)
        notifications.send_notification(number_of_episodes_downloaded, self.name)


    def filter_already_downloaded_episodes(self):
        new_episodes = {}
        for comic_id in self.latest_episodes.keys():
            episode_file_name = "img" + comic_id
            for downloaded_episodes in os.listdir(self.download_destination):
                if not episode_file_name in downloaded_episodes:
                    new_episodes[episode_file_name] = self.latest_episodes[comic_id]
        self.filtered_episodes = new_episodes


def main():
    cah_handler = ComicHandler(cah_parser, "https://explosm-1311.appspot.com", "Cyanide and Happiness", "./comics/CAH/")
    xkcd_handler = ComicHandler(xkcd_parser, "https://xkcd.com/rss.xml", "xkcd", "./comics/xkcd/")

main()
