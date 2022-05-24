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
url="https://factchecker.or.kr/hot_issues" 

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

response = requests.get(url, headers=headers)



if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.select_one('div.pt-8')
    hot_issues = div.select('div > div > div> a')
    for hot_issues in hot_issues:
        print("실시간 이슈는 ", hot_issues.get_text())
else : 
    print(response.status_code)
    
text_file=open("factchecker.text","w",encoding='UTF-8')
text_file.write(response.text)
text_file.close()

SMTP_SEVER="smtp.gmail.com"
SMTP_PORT=465

message=EmailMessage()
message.set_content("kaggle datasets")

message["Subject"]="크롤링해서 메일보내기[진준호]"
message["From"]="junho5343@gmail.com"
message["To"]="junho5343@gmail.com"

with open("factchecker.text","rb") as text:
    text_file=text.read()

message.add_attachment(text_file, maintype='text', subtype='text', filename = text.name)

smtp = smtplib.SMTP_SSL(SMTP_SEVER, SMTP_PORT)
smtp.login("junho5343@gmail.com","~SKsk159")

sendEmail("kit@likelion.org")

smtp.quit()