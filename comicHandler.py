from cahParser import cah_parser
from xkcdParser import xkcd_parser
from imageDownloader import download_image

class ComicHandler:
    def getLatestCah(self):
        CAH = cah_parser()
        download_image(CAH.comic_episodes, "./comics/CAH/")

    def getLatestXkcd(self):
        xkcd = xkcd_parser()
        download_image(xkcd.comic_episodes, "./comics/xkcd/")

def main():
    handler = ComicHandler()
    handler.getLatestCah()
    handler.getLatestXkcd()

main()
