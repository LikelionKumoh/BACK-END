from cgitb import html
from urllib import response
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import imghdr

header = {
    'User-Agent' : 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
}

url = "https://www.google.com/search?q=최예나"

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
html_file = open('crawling.txt', "w", encoding='utf-8')
html_file.write(response.text)
html_file.close()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("최예나 smiley 넘 좋아요")
message["Subject"] = "크롤링해서 메일보내기[이은빈]"
message["From"] = "kit@likelion.org"
message["To"]= "leeeunbin001122@gmail.com"

with open('crawling.txt', 'rb') as f:
    message.add_attachment(f.read(), maintype='text', subtype="plain", filename=f.name)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("leeeunbin001122@gmail.com", "Eunbin0881**")
smtp.send_message(message)
smtp.quit()


# with open('codelion.png', 'rb') as image:
#     image_file = image.read()
# image_type = imghdr.what('codelion', image_file)
# message.add_attachment(image_file, maintype='image', subtype=image_type)

