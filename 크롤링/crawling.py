
import datetime
from bs4 import BeautifulSoup
import urllib.request

now = datetime.datetime.now()
nowDate = now.strftime('현재 시각은 %Y년 %m월 %d일 %H시 %M분 입니다.')

print("\n       ※ Python Webcrawling Project 1 ※ \n ")
print('   환영합니다, ' + nowDate)
print('  ○>> #오늘의 #날씨 #요약 \n')
webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B5%AC%EB%AF%B8%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=hoyA8wp0J14ssBapHLRssssstIw-146624')
soup = BeautifulSoup(webpage, 'html.parser')
temperature_info = soup.find('div',"temperature_info")
print('--> 현재 구미 날씨 : ' , temperature_info.get_text(), '입니다')