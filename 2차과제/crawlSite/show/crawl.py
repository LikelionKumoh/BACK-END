from ast import Set
from bs4 import BeautifulSoup
import requests

def crawlSite():
    header = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }

    url = "https://www.musinsa.com/ranking/best?u_cat_cd="
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    ranks = soup.find_all("li",attrs={'class':'li_box'})
    result = []
    for rank in ranks:
        tmp = {}
        tmp['rank'] = rank.find("p",attrs={'class':'n-label label-default txt_num_rank'}).text.split()[0]
        tmp['img'] = rank.find("img",attrs={'class':'lazyload lazy'})['data-original']
        tmp['brand'] = rank.find("p",attrs={'class':'item_title'}).text.split()[0]
        tmp['item'] = rank.find("p",attrs={'class':'list_info'}).text.split()[0]
        tmp['price'] = rank.find("p",attrs={'class':'price'}).text.split()[-1]
        tmp['hearts'] = rank.find('span',attrs={'name':'count'}).text
        result.append(tmp)
    return result
