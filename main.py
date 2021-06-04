import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://pitchfork.com/features/lists-and-guides/9932-the-50-best-indie-rock-albums-of-the-pacific-northwest" \
      "/?page= "

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/70.0.3538.77 Safari/537.36"}

f = open("top_50.csv", 'w', newline='')
writer = csv.writer(f)
writer.writerow(['Band name', 'Album name'])

for x in range(5, 0, -1):
    result = requests.get(url + str(x) + '/', headers=headers)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        albums = soup.find_all("div", class_="list-blurb__artist-work")
        for each in reversed(albums):
            name = each.ul.li.a.text
            band = each.h2.text
            writer.writerow([band, name])

        time.sleep(15)
    else:
        print("Something went wrong")
        break
