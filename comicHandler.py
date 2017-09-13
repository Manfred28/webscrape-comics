from cahParser import cah_parser
from xkcdParser import xkcd_parser
from imageDownloader import download_image

class ComicHandler:
    def getLatestCah(self):
        CAH = cah_parser()
        download_image(CAH.image_download_url, CAH.image_id, "./comics/CAH/")

    def getLatestXkcd(self):
        xkcd = xkcd_parser()
        download_image(xkcd.image_download_url, xkcd.image_id, "./comics/xkcd/")

def main():
    handler = ComicHandler()
    handler.getLatestCah()
    handler.getLatestXkcd()

main()
