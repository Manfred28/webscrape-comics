import feedparser

class RssScraper:
    def __init__(self, rss_url):
        self.rss = feedparser.parse(rss_url)
        self.comic_episode_url= ""
        self.episode_id = ""
        self.latest_episodes = {}

        self.generator()


    def generator(self):
        for episode in self.rss.entries:
            self.comic_episode_url = episode.guid
            self.get_episode_id()
            self.latest_episodes[self.episode_id] = self.comic_episode_url


    def get_episode_id(self):
        self.episode_id = self.comic_episode_url.split("/")[-2]
