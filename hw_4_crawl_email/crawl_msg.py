from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

import smtplib
from email.mime.text import MIMEText


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


browser = set_chrome_driver()
browser.get("https://game.naver.com/esports/record/msi/team/msi_2022")
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')
text = "---LOL Msi 순위---\n"
for i in soup.findAll('ul', class_="record_list_team__2NtZO"):
    line = i.text.split()[1:]
    cnt = 1
    for i in line:
        if '팀' in i:
            text += f"{cnt}위: {i[i.find('고') + 1: i.find('팀') - 1]}\n"
        else:
            text += f"{cnt}위: {i[i.find('고') + 1:]}\n"
        cnt += 1
print(text)

smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('아이디는 그냥 비밀입니다', '비밀번호는 비밀입니당')

msg = MIMEText(text)
msg['Subject'] = 'BACKEND - 서장준'

s.sendmail("daki403.1@gmail.com", "kit@likelion.org", msg.as_string())

s.quit()