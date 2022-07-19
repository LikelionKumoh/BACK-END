from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus

import requests
import os

## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clothes.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django

django.setup()

from clothesapp.models import Product

def parse_product():
    url = 'https://www.musinsa.com/ranking/best?u_cat_cd='
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    # file = open("musinsa.html","w",encoding='utf8')
    # file.write(response.text)
    # file.close()


    results = soup.findAll("li","li_box")
    clothes_data = []
    for result in results:
        
        name = result.find("p",{"class" : "list_info"})
        if name.strong is not None:
            name.strong.extract()
        name =  name.get_text().strip()

        rank = result.find("p",{"class" : "n-label label-default txt_num_rank"})
        if rank.span is not None:
            rank.span.extract()
        rank = rank.get_text().strip()
        
        brand = result.find("p",{"class": "item_title"})
        brand = brand.get_text().strip()

        price = result.find("p",{"class": "price"})
        delprice = result.find("del")
        if delprice is not None:
            price = delprice
        price = price.get_text().strip()

        img = result.find("img",{"class": "lazyload lazy"})['data-original']

        each_data = {}
        each_data['name'] = name
        each_data['rank'] = rank
        each_data['brand'] = brand
        each_data['price'] = price
        each_data['img'] = img

        clothes_data.append(each_data)
        

    return clothes_data

if __name__=='__main__':
    product_data_list = parse_product()
    for dict in product_data_list:#i = idx
        print( dict)
        Product(name = dict["name"],rank =  dict["rank"],img =  dict["img"],brand =  dict["brand"],price =  dict["price"]).save()