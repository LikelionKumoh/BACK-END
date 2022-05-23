from cgitb import html
from urllib import response
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage


header = {
    'User-Agent' : 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
}

url = "https://book.naver.com/"

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
html_file = open('books.html', "w", encoding='utf-8')
html_file.write(response.text)
html_file.close()

# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 465
# smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# smtp = smtp.starttls()
# smtp.login("leeeunbin001122@gmail.com", "Eunbin0881**")

# message = EmailMessage()
# message.set_content("니용")
# message["Subject"] = "제목"
# message["From"] "wpahr"
# message["To"] "wpahr"