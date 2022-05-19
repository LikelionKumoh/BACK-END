from email import header
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

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

# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 465

# message = EmailMessage()
# message.set_content("코드라이언 수업중입니다.")

# message["Subject"] = "롤토체스 추천메타 목록입니다."
# message["From"] = "redbull1171@gmail.com"
# message["To"] = "junbs1498@naver.com"

# smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
# smtp.login("redbull1171@gmail.com","dlsrksdlsrk11")
# smtp.send_message(message)
# smtp.quit()
