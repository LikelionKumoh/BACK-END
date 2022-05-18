import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
}

url = "http://www.akbobada.com/part_g_view.html?catCode=P&groupCode=12&n_media=27758&n_query=%ED%94%BC%EC%95%84%EB%85%B8%EC%95%85%EB%B3%B4&n_rank=1&n_ad_group=grp-a001-01-000000013807371&n_ad=nad-a001-01-000000108088051&n_keyword_id=nkw-a001-01-000002614385911&n_keyword=%ED%94%BC%EC%95%84%EB%85%B8%EC%95%85%EB%B3%B4&n_campaign_type=1&n_ad_group_type=1&NaPm=ct%3Dl3a87ogg%7Cci%3D0zm0001oESbwAq12mKWN%7Ctr%3Dsa%7Chk%3D5b3dde62b688761bef1c795113f7119829483474"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')


a = soup.find_all("ul", "list", {"id":"piano_t_3"})
b= a.find_all("strong")
print(b)

html_file = open("akbobada.html", "w", encoding='utf-8')

html_file.write(response.text)
html_file.close()



