from scrapers.htmlScraper import HtmlScraper

class xkcd_scraper(HtmlScraper):

    def parse_episode_img_download_url(self):
        img_container = self.parsed_html.find(id="comic")
        self.episode_img_download_url = "http:" + img_container.img["src"]
