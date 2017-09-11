from bs4 import BeautifulSoup
import requests
from image_downloader import downloadImageData

class ComicUrlParser:
    img_url = ""
    
    def parse_html(self, url):
        result = requests.get(url)
        html_doc = result.content
        parsed_html = BeautifulSoup(html_doc, 'html.parser')
        img_html_tag = parsed_html.find(id="main-comic")
        self.image_url = "http:" + img_html_tag["src"]


def main():
    CAH_parser = ComicUrlParser()
    CAH_parser.parse_html("http://explosm.net/comics/latest")
    downloadImageData(CAH_parser.image_url)

main()
