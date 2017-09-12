from bs4 import BeautifulSoup
import requests
import feedparser
from imageDownloader import downloadImage

class ComicRssHtmlParser:
    def __init__(self, rss):
        self.rss = feedparser.parse(rss)
        self.latest_comic_url= ""
        self.parsed_html = ""
        self.image_url = ""
        self.image_id = ""

    def get_latest_comic_url(self):
        self.latest_comic_url = self.rss.entries[0].guid

    def parse_comic_html(self):
        result = requests.get(self.latest_comic_url)
        comic_html = result.content
        self.parsed_html = BeautifulSoup(comic_html, 'html.parser')
        self.find_image()

    def find_image(self):
        self.image_url = ""

    def parse_comic_id(self):
        self.image_id = self.latest_comic_url.split("/")[-2]


class CAH_parser(ComicRssHtmlParser):
    def find_image(self):
        img_html_tag = self.parsed_html.find(id="main-comic")
        self.image_url = "http:" + img_html_tag["src"]


class xkcd_parser(ComicRssHtmlParser):
    def find_image(self):
        img_container = self.parsed_html.find(id="comic")
        self.image_url = "http:" + img_container.img["src"]


def main():
    CAH = CAH_parser("https://explosm-1311.appspot.com/")
    CAH.get_latest_comic_url()
    CAH.parse_comic_html()
    downloadImage(CAH.image_url, "./comics/CAH/")

    xkcd = xkcd_parser("https://xkcd.com/rss.xml")
    xkcd.get_latest_comic_url()
    xkcd.parse_comic_html()
    downloadImage(xkcd.image_url, "./comics/xkcd/")

main()
