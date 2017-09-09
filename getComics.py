from plyer import notification
from bs4 import BeautifulSoup
import requests


result = requests.get("http://explosm.net/")
html_doc = result.content
soup = BeautifulSoup(html_doc, 'html.parser')

latestComicAnchor = soup.find(href="/comics/latest/")
latestComicUrl = "http:" + latestComicAnchor.img["src"]



img_data = requests.get(latestComicUrl)
img_content = img_data.content
img_extension = img_data.headers["content-type"].split("/")[1]
with open('../comics/img.' + img_extension, 'wb') as handler:
    handler.write(img_content) 



''' notification.notify(
    title='Here is the title',
    message='Here is the message',
) '''
