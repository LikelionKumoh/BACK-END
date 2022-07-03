import os
from unittest import result
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "ClothingSearch.settings")
import django

django.setup()
from crawler.models import ClothingData

def clothing_data():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
    }

    url = "https://www.musinsa.com/ranking/best?u_cat_cd="

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    rank = []
    image = []
    brand = []
    price = []
    product = []
    #like = []
    result = []
    item_list = soup.findAll("li", "li_box")

    for item in item_list:

        #순위
        rank_box = item.find("p", "n-label label-default txt_num_rank").get_text().split()
        if len(rank_box) == 1:
            rank.append(rank_box[0])
        elif len(rank_box) == 2:
            rank.append(rank_box[0])
        elif len(rank_box) == 3:
            rank.append(rank_box[0])

        #이미지
        image_box = item.find("div", "list_img").find("img")["data-original"]
        image.append(image_box)

        #브랜드
        brand_box = item.find("p", "item_title").find("a").get_text().split()
        brand.append(brand_box)

        #제품명
        product_box = item.find("p", "list_info").find("a")["title"]
        product.append(product_box.strip())

        #가격
        price_box = item.find("p", "price").get_text().split()
        if len(price_box) == 1:
            price.append(price_box[0])
        elif len(price_box) == 2:
            price.append(price_box[1])
        
        #좋아요 개수
        #like_box = item.find()
        #like.append(like_box)

        item_obj = {
            'rank' : rank,
            'image' : image,
            'brand' : brand,
            'product' : product,
            'price' : price,
            #'like' : like,
        }

        result.append(item_obj)
    return result

if __name__=='__main__':
    musinsa_data = clothing_data()
    for data in musinsa_data:
        ClothingData(rank = data['data'], image = data['image'], brand = data['brand'], product = data['product'], price = data['price']).save()
