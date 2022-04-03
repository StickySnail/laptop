import requests
from bs4 import BeautifulSoup as bs

respone = requests.get('https://workey.codeit.kr/music/index')
html_code= respone.text

html_soup = bs(html_code, 'html.parser')

html_tags = html_soup.select('.rank__order .list')

results = []

for i in html_tags:
   results.append(i.text.strip().split(" ")[2])

print(results)