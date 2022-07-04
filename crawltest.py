import requests
from bs4 import BeautifulSoup

url = 'https://www.musinsa.com/brands/nike?page='
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

cnt = 1
new_url = url + str(cnt)

data = requests.get(new_url, headers=headers)
soup = BeautifulSoup(data.text, 'lxml')
links = soup.find_all(attrs={"name": "goods_link", "class": "img-block"})

while links:
    for link in links:
        data2 = requests.get('https:' + link['href'], headers=headers)
        soup2 = BeautifulSoup(data2.text, 'lxml')
        link2 = soup2.find(id='bigimg')
        print(link2['alt'])

    cnt += 1
    print(f'{cnt} page end!')
    new_url = url + str(cnt)

    data = requests.get(new_url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    links = soup.find_all(attrs={"name": "goods_link", "class": "img-block"})








