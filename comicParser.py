from bs4 import BeautifulSoup
import requests
import feedparser


class ComicRssHtmlParser:
    def __init__(self, rss):
        self.rss = feedparser.parse(rss)
        self.comic_episode_url= ""
        self.episode_id = ""
        self.parsed_html = ""
        self.episode_img_download_url = ""
        self.comic_episodes = {}

        self.get_comic_episodes()

    def get_comic_episodes(self):
        for episode in self.rss.entries:
            self.comic_episode_url = episode.guid
            self.get_episode_id()
            self.parse_comic_html()
            self.parse_episode_img_download_url()
            self.comic_episodes[self.episode_id] = self.episode_img_download_url

    def get_episode_id(self):
        self.episode_id = self.comic_episode_url.split("/")[-2]

    def parse_comic_html(self):
        result = requests.get(self.comic_episode_url)
        comic_html = result.content
        self.parsed_html = BeautifulSoup(comic_html, 'html.parser')
        self.parse_episode_img_download_url()

    def parse_episode_img_download_url(self):
        self.episode_img_download_url = ""
