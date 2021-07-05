import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import requests
client_id = "mkmd96FqCiDGqWSBDR_1"
client_secret = "cvqsZMNpfA"
encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText # json 결과
response = requests.get(url)
html = response.text
# url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

soup = BeautifulSoup(html, 'html.parser')
tds = soup.select('item')

for idx,td in enumerate(tds):
    if idx > 2:
        print(td.text)


if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)