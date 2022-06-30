
import requests
from bs4 import BeautifulSoup

url="https://www.musinsa.com/ranking/best?u_cat_cd="

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")
elements = soup.select("#goodsRankList > li")
print(elements)
info = []

for element in elements:
    list = []
    rank = element.select_one("#goodsRankList > li > p").text
    pic = element.select_one("#goodsRankList > li > div.li_inner > div.list_img > a > img")['data-original']
    print(pic)
    brand = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.item_title > a").text
    name = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.list_info > a")["title"]
    price = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p.price").text
    # count = element.select_one("#goodsRankList > li > div.li_inner > div.article_info > p:nth-child(7)")["count"]
    list.append(rank)
    list.append(pic)
    list.append(brand)
    list.append(name)            
    list.append(price)
    # list.append(count)
    # newlist = print(rank," ", "브랜드: ", brand, "제품명: ", name, "가격 : ", price, "좋아요 개수: ", count)
    info.append(list)
print(info)

# text_file=open("musinsa.text","w",encoding='UTF-8')
# text_file.write(response.text)
# text_file.close()