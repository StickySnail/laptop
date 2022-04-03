import requests
from bs4 import BeautifulSoup as bs

rating_pages = []

for year in range(2010, 2019):
    for month in range(1, 13):
        for week in range(0, 5):
            respone = requests.get('https://workey.codeit.kr/ratings/index?year=' + str(year) +
                                   '&month=' + str(month) +
                                   '&weekIndex=' + str(week))
            html_soup = bs(respone.text, 'html.parser')

            if len(html_soup.select('.row')) > 1:
                rating_pages.append(respone.text)

# 테스트 코드
print(len(rating_pages))  # 가져온 총 페이지 수
print(rating_pages[0])  # 첫 번째 페이지의 HTML 코드
