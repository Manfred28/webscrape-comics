from comicParser import ComicRssHtmlParser

class cah_parser(ComicRssHtmlParser):
    def __init__(self):
        super().__init__()


    def parse_episode_img_download_url(self):
        img_html_tag = self.parsed_html.find(id="main-comic")
        self.episode_img_download_url = "http:" + img_html_tag["src"]
