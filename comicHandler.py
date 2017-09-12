import getComics
from imageDownloader import downloadImage

class ComicHandler:
    def getLatestCah(self):
        CAH = getComics.CAH_parser()
        downloadImage(CAH.image_url, "./comics/CAH/")

    def getLatestXkcd(self):
        xkcd = getComics.xkcd_parser()
        downloadImage(xkcd.image_url, "./comics/xkcd/")

def main():
    handler = ComicHandler()
    handler.getLatestCah()
    handler.getLatestXkcd()

main()
