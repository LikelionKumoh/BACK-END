from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup
import smtplib
import re

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

header = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

url = "https://finance.naver.com/sise/sise_quant.naver"

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')

team = soup.find_all("td",attrs={'class':'number'})
title = soup.find_all("a", attrs={'class':'tltle'})
result = []
result.append(['순위','종목명','현재가','전일비','등락률','거래량','거래대금','매수호가','매도호가','시가총액','PER','ROE'])
for i in title:
    result.append([i.text])
index = 0

for i,j in enumerate(team):
    print(i)
    if i % 10 == 0:
        index += 1
    result[index].append(re.sub('[\\n\\t]','',j.text))
print(result)

html_file = open('stock.txt',"w")
html_file.write('주식 차트 100!!' + '\n')
for i,stock in enumerate(result):
    if(i == 0):
        html_file.write(' '.join(stock) + '\n')
        continue
    html_file.write(str(i) + ' ' + ' '.join(stock) + '\n')
html_file.close()



SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

message = EmailMessage()
message.set_content('주식 정보를 알려드립니다!!')
message['Subject'] = '크롤링해서 메일보내기[김성은]'
message['From'] = '###@likelion.org'
message['To'] = '###@likelion.org'

with open('stock.txt', 'rb') as f:
    message.add_attachment(f.read(), maintype = "text",subtype="plain",filename="stock.txt")

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login('###@likelion.org','###')
sendEmail('###@likelion.org')
smtp.quit()


    
    


#gmail 설정 해야함

# 제목: 크롤링해서 메일보내기[김성은]
# 내용: 각자의 관심사에 대한 간단한 설명
# 보내는 분 = 개인의 google 이메일
# 받는 분 = kit@likelion.org
# 텍스트 파일 첨부하기
# 유효성 검사하기
# 개인정보는 #으로 변경하여 깃헙 과제에 제출한다.