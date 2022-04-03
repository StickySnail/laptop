from bs4 import BeautifulSoup
import requests
respone = requests.get('https://workey.codeit.kr/orangebottle/index#')

html_code = respone.text

soup = BeautifulSoup(html_code, 'html.parser')

soup_tags = soup.select('.branch .phoneNum')

phone_numbers = []

for li in soup_tags :
    phone_numbers.append(li.text.strip())

print(phone_numbers)
print(soup_tags)