from email import header
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}

url = "https://lolchess.gg/meta"

response=requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

html_file = open("meta.html","w",encoding='UTF-8')
html_file.write(response.text)
html_file.close()
