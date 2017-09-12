from cahParser import cah_parser
from xkcdParser import xkcd_parser
from imageDownloader import downloadImage

class ComicHandler:
    def getLatestCah(self):
        CAH = cah_parser()
        downloadImage(CAH.image_url, "./comics/CAH/")

    def getLatestXkcd(self):
        xkcd = xkcd_parser()
        downloadImage(xkcd.image_url, "./comics/xkcd/")

def main():
    handler = ComicHandler()
    handler.getLatestCah()
    handler.getLatestXkcd()

main()
