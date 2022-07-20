import requests
from bs4 import BeautifulSoup
from crawler.models import ClothingData

def clothing_data():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
    }

    url = "https://www.musinsa.com/ranking/best?u_cat_cd="

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    item_list = soup.find_all("li", "li_box")
    result = []
    
    for item in item_list:

        #순위
        rank = item.find("p", "n-label label-default txt_num_rank").get_text().split()[0]

        #이미지
        image = item.find("div", "list_img").find("img")["data-original"]
        
        #브랜드
        brand= item.find("p", "item_title").get_text().strip()

        #제품명
        product = item.find("p", "list_info").find("a")["title"].strip()

        #가격
        price = item.find("p", "price").get_text().split()[0]

 
        item_obj = {
                'rank' : rank,
                'image' : image,
                'brand' : brand,
                'product' : product,
                'price' : price,
            }

        result.append(item_obj)
    return result
