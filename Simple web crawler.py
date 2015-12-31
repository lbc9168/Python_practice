import requests
from bs4 import BeautifulSoup

def stepashka_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://columbus-oh.auto.com/cars-for-sale/less-than-5000-dollars?page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for resoult in soup.findAll("div", {"class": "header col-xs-12"}):
            a_tag = resoult.a

            print(a_tag["href"])
            print(a_tag["title"])
            get_single_item_data(a_tag["href"])

        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_price in soup.findAll('span', {"class": "car-price"}):
        print(item_price.string)


stepashka_spider(2)