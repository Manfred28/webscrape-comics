from bs4 import BeautifulSoup
import requests
import feedparser
from imageDownloader import downloadImage

class ComicRssParser:

    def __init__(self, rss):
        self.rss = feedparser.parse(rss)
        self.latest_comic_url= ""
        self.image_url = ""

    def get_latest_comic_url(self):
        self.latest_comic_url = self.rss.entries[0].guid

    def get_image_url(self):
        result = requests.get(self.latest_comic_url)
        html_doc = result.content
        parsed_html = BeautifulSoup(html_doc, 'html.parser')
        img_html_tag = parsed_html.find(id="main-comic")
        self.image_url = "http:" + img_html_tag["src"]

def main():
    CAH_parser = ComicRssParser("https://explosm-1311.appspot.com/")
    CAH_parser.get_latest_comic_url()
    CAH_parser.get_image_url()
    downloadImage(CAH_parser.image_url, "./comics/CAH/")

main()
