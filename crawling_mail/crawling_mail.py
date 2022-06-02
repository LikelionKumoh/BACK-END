import requests
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
import re

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}
url = "https://www.melon.com/"
response = requests.get(url,headers=header)
soup = BeautifulSoup(response.text,'html.parser')

html_file = open("melonchart.html","w",encoding='UTF-8')
html_file.write(response.text)
html_file.close()
results = soup.findAll('a','ellipsis mlog')
rank = 1

music_rank_file = open("rankresult.txt","w",encoding="UTF-8")



for result in results:
    music_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),'\n')
    rank+=1

music_rank_file.close()

#메일 보내기
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("20191168 최영민")

#유효성검사
def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


message["Subject"] = "크롤링해서 메일보내기[최영민]."
message["From"] = "########@gmail.com"
message["To"] = "kit@likelion.org"


with open('rankresult.txt',"rb") as txt:
    txt_file = txt.read()
    
message.add_attachment(txt_file,maintype='txt', subtype = 'plain', filename = txt.name)


smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("#######@gmail.com","#######")

#유효성검사함수
sendEmail("kit@likelion.org")


smtp.quit()
#print(soup.find())