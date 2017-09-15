from bs4 import BeautifulSoup
import requests


class ComicRssHtmlParser:
    def __init__(self):
        self.parsed_html = ""
        self.comic_episode_url = ""
        self.episode_img_download_url = ""
        self.episode_download_links = {}


    def get_episode_download_links(self, new_episodes):
        for episode in new_episodes.keys():
            self.comic_episode_url = new_episodes[episode]
            self.parse_comic_html()
            self.parse_episode_img_download_url()
            self.episode_download_links[episode] = self.episode_img_download_url


    def parse_comic_html(self):
        result = requests.get(self.comic_episode_url)
        comic_html = result.content
        self.parsed_html = BeautifulSoup(comic_html, 'html.parser')


    def parse_episode_img_download_url(self):
        self.episode_img_download_url = ""
