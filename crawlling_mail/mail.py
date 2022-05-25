from email import message
import smtplib
from email.message import EmailMessage
import re

def sendEmail(my_addr, yr_addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    
    if(re.match(reg, my_addr) and re.match(reg, yr_addr)):
        smtp.send_message(message)
        print("메일이 발송되었습니다.")
    else:
        print("유효한 email주소가 아닙니다")

title = "백엔드 전민규"
content = "현재 상영중인 영화 목록입니다 \n\n"

my_email = "###@gmail.com"
my_pwd = "####"

your_email = "###@likelion.org"

reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
print(re.match(reg, my_email))
print(re.match(reg, your_email))

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
#SMTP_PORT = 486

with open("on_the_screen.txt", "r") as text:
    text_file = text.read()
    
    for line in text_file:
        content = content + line

message = EmailMessage()
message.set_content(content)

message["Subject"] = title
message["From"] = my_email
message["To"] = your_email

message.add_attachment(text_file)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login(my_email, my_pwd)
sendEmail(my_email, your_email)
smtp.quit()
