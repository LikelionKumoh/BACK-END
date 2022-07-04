import requests
from bs4 import BeautifulSoup
import os

## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musinsa.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django

django.setup()

from musinsaapp.models import Product
    
def data_musinsa():
    url="https://www.musinsa.com/ranking/best?u_cat_cd="

    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36' }

    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.select("#goodsRankList > li")
    data=[]
    
    for element in elements:        
        rank = element.select_one("#goodsRankList > li > p").get_text().strip()
        img = element.select_one("#goodsRankList > li > div.li_inner > div.list_img > a > img")['data-original']
        brand = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.item_title > a").get_text().strip()
        name = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.list_info > a").get_text().strip()
        price = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.price").get_text().strip()
        # count = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p:nth-child(7) > span").get_text().strip()
        list = {}
        list['name'] = name
        list['rank'] = rank
        list['brand'] = brand
        list['price'] = price
        list['img'] = img 
        data.append(list)
    return data
        

if __name__=='__main__':
    data_musinsa_dict = data_musinsa()
    for dict in data_musinsa_dict:
        Product(name = dict["name"],rank =  dict["rank"],img =  dict["img"],brand =  dict["brand"],price =  dict["price"]).save()
        