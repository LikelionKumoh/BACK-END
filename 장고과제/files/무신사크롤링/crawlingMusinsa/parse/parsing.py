import requests
from bs4 import BeautifulSoup
import os
import sys
sys.path.append("c:\\Users\\junbs\\OneDrive\\바탕 화면\\깃허브\\Codelion-Django\\files\\crawling\\crawlingMusinsa")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawlingMusinsa.settings")
import django
django.setup()

from parse.models import Parsed


header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}

def crawling():
    url = "https://www.musinsa.com/ranking/best?u_cat_cd="

    response=requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    items=[]
    rank_list=soup.select('li.li_box')
    for item in rank_list:
        # 이미지
        img=item.find('a',{'class':'img-block'}).find('img')
        # print(img['data-original'])
        # 랭크 크롤링
        rank=item.find('p',{'class':'n-label label-default txt_num_rank'})
        rank.find('span').decompose()
        # print(rank.text)
        # 브랜드 크롤링
        brand=item.find('p',{'class':'item_title'}).find('a')
        # 상품명
        name = item.find('p',{'class':'list_info'}).find('a')
        # 가격
        price=item.find('span',{'class':'txt_price_member'})
        # 좋아요
        like=item.find('p',{'class':'point'})
        try:
            item_obj = {
                'img': img['data-original'],
                'rank': rank.text,
                'brand': brand.text,
                'name' : name.text,
                'price' : price.text,
                'like' : like.text,
                }
            items.append(item_obj)
        except Exception as e:
            item_obj = {
                'img': img['data-original'],
                'rank': rank.text,
                'brand': None,
                'name' : name.text,
                'price' : price.text,
                'like' : None,
                }
            items.append(item_obj)
    return items

if __name__=='__main__':
    musinsa_data_dict= crawling()
    for i in musinsa_data_dict:
        Parsed.objects.create(image=i['img'],ranking=i['rank'],brand=i['brand'],item=i['name'],price=i['price'],likes=i['like']).save
