import requests
from bs4 import BeautifulSoup
from .models import Goods


def get_data(text, search='brand'):
    if search == 'brand':
        url = f'https://www.musinsa.com/brands/{text}?page=1'
    else:
        url = f'https://www.musinsa.com/search/musinsa/goods?q={text}&page=1'

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    rank = 1

    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    links = soup.select('#searchList .li_inner')

    for i in links:
        brand_name = i.select_one('.article_info .item_title').text.strip()
        goods_name = i.select_one('.article_info .list_info').text.strip()
        image = i.select_one('.list_img .lazyload')['data-original']
        price = i.select_one('.article_info .price').text.strip()
        recommand = i.select_one('.article_info .point .count')
        recommand = '0' if recommand is None else recommand.text

        goods = Goods(brand_name=brand_name, goods_name=goods_name, image=image, price=price, rank=str(rank), recommand_cnt=recommand)
        goods.save()

        rank += 1


if __name__ == "__main__":
    get_data('adidas', 'brand')










