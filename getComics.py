from plyer import notification
from bs4 import BeautifulSoup
import requests


def getImageUrl():
    result = requests.get("http://explosm.net/")
    html_doc = result.content
    soup = BeautifulSoup(html_doc, 'html.parser')

    latest_comic_anchor = soup.find(href="/comics/latest/")

    return "http:" + latest_comic_anchor.img["src"];




def downloadImageData(latest_comic_url):
    img_data = requests.get(latest_comic_url)
    if img_data.status_code == 200: 
        createImageFile(img_data)
    else: 
        print("Could not download file")

def createImageFile(img_data):
    img_content = img_data.content
    img_extension = img_data.headers["content-type"].split("/")[1]
    with open('comics/img.' + img_extension, 'wb') as handler:
        handler.write(img_content) 


def main():
    latest_comic_url = getImageUrl()
    downloadImageData(latest_comic_url)

main()

''' notification.notify(
    title='Here is the title',
    message='Here is the message',
) '''
