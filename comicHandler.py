import getComics
from imageDownloader import downloadImage

class ComicHandler:
    
    def getLatestCah():
        CAH = getComics.CAH_parser()
        CAH.get_latest_comic_url()
        CAH.parse_comic_html()
        downloadImage(CAH.image_url, "./comics/CAH/")
    
    def getLatestXkcd():
        xkcd = getComics.xkcd_parser()
        xkcd.get_latest_comic_url()
        xkcd.parse_comic_html()
        downloadImage(xkcd.image_url, "./comics/xkcd/")

def main():
    handler = ComicHandler
    handler.getLatestCah()
    handler.getLatestXkcd()

main()
