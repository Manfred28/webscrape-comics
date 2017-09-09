from plyer import notification
from bs4 import BeautifulSoup
import requests

result = requests.get("http://explosm.net/")
html_doc = result.content
soup = BeautifulSoup(html_doc, 'html.parser')

latestComicAnchor = soup.find(href="/comics/latest/")
latestComicUrl = "http:" + latestComicAnchor.img["src"]

print(latestComicAnchor)

''' img_data = requests.get(latestComicUrl).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data) '''



''' notification.notify(
    title='Here is the title',
    message='Here is the message',
) '''
