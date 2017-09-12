from cahParser import cah_parser
from xkcdParser import xkcd_parser
from imageDownloader import downloadImage

class ComicHandler:
    def getLatestCah(self):
        CAH = cah_parser()
        downloadImage(CAH.image_download_url, CAH.image_id, "./comics/CAH/")

    def getLatestXkcd(self):
        xkcd = xkcd_parser()
        downloadImage(xkcd.image_download_url, xkcd.image_id, "./comics/xkcd/")

def main():
    handler = ComicHandler()
    handler.getLatestCah()
    handler.getLatestXkcd()

main()
