import getComics
from imageDownloader import downloadImage

class ComicHandler:
    
    def getLatestCah():
        CAH = getComics.CAH_parser("https://explosm-1311.appspot.com/")
        CAH.get_latest_comic_url()
        CAH.parse_comic_html()
        downloadImage(CAH.image_url, "./comics/CAH/")
    
    def getLatestXkcd():
        xkcd = getComics.xkcd_parser("https://xkcd.com/rss.xml")
        xkcd.get_latest_comic_url()
        xkcd.parse_comic_html()
        downloadImage(xkcd.image_url, "./comics/xkcd/")

def main():
    handler = ComicHandler
    handler.getLatestCah()
    handler.getLatestXkcd()

main()
