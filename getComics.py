from bs4 import BeautifulSoup
import requests
import feedparser


class ComicRssHtmlParser:
    def __init__(self, rss):
        self.rss = feedparser.parse(rss)
        self.latest_comic_url= ""
        self.parsed_html = ""
        self.image_url = ""
        self.image_id = ""

        self.get_latest_comic_url()
        self.get_comic_id()
        self.parse_comic_html()
        self.parse_image_download_url()

    def get_latest_comic_url(self):
        self.latest_comic_url = self.rss.entries[0].guid

    def parse_comic_html(self):
        result = requests.get(self.latest_comic_url)
        comic_html = result.content
        self.parsed_html = BeautifulSoup(comic_html, 'html.parser')
        self.parse_image_download_url()

    def parse_image_download_url(self):
        self.image_url = ""

    def get_comic_id(self):
        self.image_id = self.latest_comic_url.split("/")[-2]



