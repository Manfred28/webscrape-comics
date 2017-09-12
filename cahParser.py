from getComics import ComicRssHtmlParser

class cah_parser(ComicRssHtmlParser):
    def __init__(self):
        super().__init__("https://explosm-1311.appspot.com/")

    def parse_image_download_url(self):
        img_html_tag = self.parsed_html.find(id="main-comic")
        self.image_url = "http:" + img_html_tag["src"]