import requests
import smtplib
import re
from bs4 import BeautifulSoup
from datetime import datetime
from email.message import EmailMessage

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
}

url = "http://www.akbobada.com/part_g_view.html?catCode=P&groupCode=12&n_media=27758&n_query=%ED%94%BC%EC%95%84%EB%85%B8%EC%95%85%EB%B3%B4&n_rank=1&n_ad_group=grp-a001-01-000000013807371&n_ad=nad-a001-01-000000108088051&n_keyword_id=nkw-a001-01-000002614385911&n_keyword=%ED%94%BC%EC%95%84%EB%85%B8%EC%95%85%EB%B3%B4&n_campaign_type=1&n_ad_group_type=1&NaPm=ct%3Dl3a87ogg%7Cci%3D0zm0001oESbwAq12mKWN%7Ctr%3Dsa%7Chk%3D5b3dde62b688761bef1c795113f7119829483474"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find("ul", id='piano_t_3')
date = datetime.today().strftime("%Y년 %m월 %d일의 악보바다 피아노악보 TOP5입니다.\n")

rank_file = open("piano.txt", "a", encoding='utf-8')
rank_file.write(date+results.get_text())

html_file = open("akbobada.html", "w", encoding='utf-8')
html_file.write(response.text)
html_file.close()


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-0]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


message = EmailMessage()
message.set_content("악보바다 사이트 피아노 악보 TOP5입니다.")

message["Subject"] = "크롤링해서 메일보내기[공혜연]"
message["From"] = "######@gmail.com"
message["To"] = "kit@likelion.org"

file_name='piano.txt'

with open(file_name, "rb") as txt:
    txt_file = txt.read()

message.add_attachment(txt_file, maintype='txt',subtype='txt',filename=file_name)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("######@gmail.com","######")
sendEmail("kit@likelion.org")
smtp.quit()