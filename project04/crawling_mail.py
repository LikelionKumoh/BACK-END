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

url = "https://search.naver.com/search.naver?query=최예나"

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.select_one('#main_pack > section.sc_new.cs_common_module.case_normal._au_people_content_wrap.color_5 > div.cm_content_wrap > div:nth-child(4) > div > div.cm_info_box.scroll_img_album._tab_content > div > div > div > ul > li:nth-child(1) > div > div > strong > a').get_text()
print(title)
txt_file = open('crawling.txt', "w", encoding='utf-8')
txt_file.write(title)
txt_file.close()


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465


message = EmailMessage()
message.set_content("최예나 smiley 넘 좋아요")
message["Subject"] = "크롤링해서 메일보내기[이은빈]"
message["From"] = "leeeunbin001122@gmail.com"
message["To"]= "kit@likelion.org"

with open('crawling.txt', 'rb') as f:
    message.add_attachment(f.read(), maintype='text', subtype="plain", filename=f.name)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("leeeunbin001122@gmail.com", "냠냠")
smtp.send_message(message)
smtp.quit()


# with open('codelion.png', 'rb') as image:
#     image_file = image.read()
# image_type = imghdr.what('codelion', image_file)
# message.add_attachment(image_file, maintype='image', subtype=image_type)

