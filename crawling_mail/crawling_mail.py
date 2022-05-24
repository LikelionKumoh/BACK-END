from email import header
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import re

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}

url = "https://lolchess.gg/meta?hl=ko-KR"

response=requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

metas = soup.findAll('div','guide-meta__deck__column name mr-3')
for item in metas:
    soup.span.extract()
for item in metas:
    soup.span.extract()
num=1
text_file = open("tft_meta.txt","w",encoding="UTF-8")
text_file.write("롤토체스 추천 덱 목록입니다.\n\n")
for meta in metas:
    text_file.write(str(num)+". "+meta.get_text()+"\n")
    print(num,"위 : ",meta.get_text(),"\n")
    num += 1
text_file.close()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일주소가 아닙니다.")


message = EmailMessage()
message.set_content("롤토체스 추천 덱 목록을 크롤링 한 결과 입니다.")

message["Subject"] = "전용현 크롤링 과제입니다."
message["From"] = "#######@likelion.org"
message["To"] = "kit@likelion.org"

with open("tft_meta.txt","rb") as txt_file:
    txt=txt_file.read()

message.add_attachment(txt,maintype='txt', subtype='txt', filename= txt_file.name)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("#######@likelion.org","#######")
sendEmail(message["To"])
smtp.quit()
