from os import replace
import smtplib
from email.message import EmailMessage
from urllib import response
import requests
from bs4 import BeautifulSoup
from soupsieve import select
import re


def sendEmail(addr):
    reg="^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다. ")
    else:
        print("유효한 이메일 주소가 아닙니다.")


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}
url="https://comic.naver.com/webtoon/weekday" 


response = requests.get(url, headers=headers)

soup=BeautifulSoup(response.text, 'html.parser')

html_file=open("webtoon.html","w",encoding='UTF-8')
html_file.write(response.text)
html_file.close()

print("월요일: mon"+'\n'+"화요일: tue"+'\n'+"수요일: wed"+'\n'+"목요일: thu"+'\n'
+"금요일: fri"+'\n'+"토요일: sat"+'\n'+"일요일: sun")
temp=input("요일을 입력하세요: ")

day=["mon","tue","wed","thu","fri","sat","sun"]
index_d=day.index(temp)
rank=soup.select("div.col_inner")[index_d]

# 쓰레기값 제거
em=soup.findAll('em')
for em in em:
     soup.em.extract()
for span in soup.findAll('span'):
    span.replace_with("")

rank_file=open("rank.txt","w+",encoding='UTF-8')
# print(rank.get_text())
result = rank.get_text()
result = re.sub("\s\s\s\s", "\n", result)
result = re.sub("\s\s+", "\n", result)

rank_file.write(result)

rank_file.close()

SMTP_SEVER="smtp.gmail.com"
SMTP_PORT=465

message=EmailMessage()
message.set_content("네이버 웹툰입니다.")

message["Subject"]="크롤링해서 메일보내기[안현진]"
message["From"]="#########@gmail.com"
message["To"]="kit@likelion.org"

with open("rank.txt","rb") as txt:
    txt_file=txt.read()

message.add_attachment(txt_file, maintype='txt', subtype='txt', filename=txt.name)

smtp = smtplib.SMTP_SSL(SMTP_SEVER, SMTP_PORT)
smtp.login("######","######")

sendEmail("kit@likelion.org")

smtp.quit()