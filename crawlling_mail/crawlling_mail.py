import smtplib
from turtle import title
from urllib import response
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText

file = open("on_the_screen.txt", "w")

#IMAP 사용 설정
#

header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
}

#네이버 현재 상영작
url = 'https://movie.naver.com/movie/running/current.naver'

#src 가져오기
respons = requests.get(url, headers = header)

soup = BeautifulSoup(respons.text, 'html.parser', from_encoding='utf-8')

#copy url_html_source_code to movie.html
html_open = open("movie.html", "w", encoding='utf-8')
html_open.write(respons.text)
html_open.close()

all_movie = soup.select_one("ul.lst_detail_t1")
movie_list = all_movie.select("li")

for movie in movie_list:
    title = ""
    netisen_score = ""
    
    title_box = movie.select_one("dt")
    title = title_box.select_one("a").text
    
    score_set = movie.find("dd", "star")
    deep_score_set = score_set.find_all("dd")
    
    netisen_score = deep_score_set[0].find("span", "num").text
    
    data = title + " " + netisen_score + "\n"
    print(data)
    file.write(data)
    
file.close()

#SMTP_SERVER = "smtp.gmail.com"
#SMTP_PORT = 486
#s = smtplib.SMTP('smtp.gmail.com', 587)

#보내는분 내 lion 메일
#받는분 kit@likelion.org
#txt파일 첨부
#유효성 검사
#5월 25일까지