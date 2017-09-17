import os
from notifications.notifications import send_notification
from scrapers.rssScraper import RssScraper
from scrapers.cahHtmlScraper import cah_scraper
from scrapers.xkcdHtmlScraper import xkcd_scraper
from downloader.imageDownloader import download_image


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
        send_notification(len(number_of_episodes_downloaded), self.name)


    def filter_already_downloaded_episodes(self):
        new_episodes = {}
        for comic_id in self.latest_episodes.keys():
            episode_file_name = "img" + comic_id
            if not self.is_existing_file(self.download_destination, episode_file_name):
                new_episodes[episode_file_name] = self.latest_episodes[comic_id]
        self.filtered_episodes = new_episodes

    def is_existing_file(self, destination, file_name):
        for name in os.listdir(destination):
            if file_name in name:
                return True

def main():
    cah_handler = ComicHandler(cah_scraper, "https://explosm-1311.appspot.com", "Cyanide and Happiness", "./comics/CAH/")
    xkcd_handler = ComicHandler(xkcd_scraper, "https://xkcd.com/rss.xml", "xkcd", "./comics/xkcd/")

main()
