from comicParser import ComicRssHtmlParser

class xkcd_parser(ComicRssHtmlParser):
    def __init__(self):
        super().__init__("https://xkcd.com/rss.xml")

    def parse_episode_img_download_url(self):
        img_container = self.parsed_html.find(id="comic")
        self.episode_img_download_url = "http:" + img_container.img["src"]