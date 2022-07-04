import requests
from bs4 import BeautifulSoup
from .models import Goods


def get_data(text, search='brand'):
    if search == 'brand':
        url = f'https://www.musinsa.com/brands/{text}?page='
    else:
        url = f'https://www.musinsa.com/search/musinsa/goods?q={text}&page='

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    cnt = 1
    rank = 1
    new_url = url + str(cnt)

    data = requests.get(new_url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    links = soup.find_all(attrs={"name": "goods_link", "class": "img-block"})


    while links:
        for link in links:
            new_url = link['href']
            if search == 'brand':
                new_url = 'https:' + new_url
            data2 = requests.get(new_url, headers=headers)
            soup2 = BeautifulSoup(data2.text, 'html.parser')
            link2 = soup2.find(id='bigimg')


            brand_name, goods_name = link2['alt'][:link2['alt'].find(')') + 1], link2['alt'][link2['alt'].find(')') + 1:] 
            image = link2['src']
            try:
                price = soup2.find(class_="price-del").text
            except:
                price = "???"

            goods = Goods(brand_name=brand_name, goods_name=goods_name, image=image, price=price, rank=str(rank), recommand_cnt='0')
            goods.save()

            rank += 1
        cnt += 1
        break
        print(f'{cnt} page end!')
        new_url = url + str(cnt)

        data = requests.get(new_url, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        links = soup.find_all(attrs={"name": "goods_link", "class": "img-block"})


if __name__ == "__main__":
    get_data('nike', 'brand')










