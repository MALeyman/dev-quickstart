import os
import requests
from bs4 import BeautifulSoup
import cv2


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
}

def saveImages(name : str, index : int, item : bytes) -> None:
    if not os.path.exists(name):
        os.mkdir(name)
    file = open(f"{name}/{index}.jpg", "wb")
    file.write(item)
    file.close()
    print("Сохранено")


def downloadImage(text : str) -> []:
    i = 0
    max_count = 50
    main_url = "https://yandex.ru/images/search?text=" + text
    result = requests.get(main_url, headers=headers)
    print(result)
    soup = BeautifulSoup(result.content, "lxml")
    links = soup.findAll("img", class_ = "serp-item__thumb justifier__thumb")
    for link in links:
        try:
            link = link.get("src")
            _img = requests.get("https:" + str(link))
            saveImages(text, i, _img.content)
            i += 1
            print(i)
            if i == max_count:
                break
        except:
            continue           

downloadImage("tiger")