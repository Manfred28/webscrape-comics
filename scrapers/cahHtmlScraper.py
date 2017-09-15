from scrapers.htmlScraper import HtmlScraper

class cah_scraper(HtmlScraper):

    def parse_episode_img_download_url(self):
        img_html_tag = self.parsed_html.find(id="main-comic")
        self.episode_img_download_url = "http:" + img_html_tag["src"]
