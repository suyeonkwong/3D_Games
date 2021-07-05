import requests
from bs4 import BeautifulSoup
URL = 'http://localhost:8090/HELLO/hello.jsp' 
response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
tds = soup.select('td')

for idx,td in enumerate(tds):
    if idx > 2:
        print(td.text)
