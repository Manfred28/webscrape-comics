import os
from plyer import notification
from cahParser import cah_parser
from xkcdParser import xkcd_parser
from imageDownloader import download_image


def getLatestCah():
    CAH = cah_parser()
    destination = "./comics/CAH/"
    if not os.path.exists(destination):
        os.makedirs(destination)
    number_of_episodes_downloaded = download_image(CAH.comic_episodes, destination)
    send_notification(number_of_episodes_downloaded, "Cyanide and Happiness")

def getLatestXkcd():
    xkcd = xkcd_parser()
    destination = "./comics/xkcd/"
    if not os.path.exists(destination):
        os.makedirs(destination)
    number_of_episodes_downloaded = download_image(xkcd.comic_episodes, destination)
    send_notification(number_of_episodes_downloaded, "xkcd")

def send_notification(episodes_downloaded, comic_name):
    if episodes_downloaded > 0:
        notification.notify(
        title = comic_name,
        message = str(episodes_downloaded) + " Episode(s) Downloaded"
        )

def main():
    getLatestXkcd()
    getLatestCah()

main()
