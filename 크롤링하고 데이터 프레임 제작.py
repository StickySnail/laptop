import pandas as pd
import requests
from bs4 import BeautifulSoup

# 기간 지정
years = list(range(2010, 2019))
months = list(range(1, 13))
weeks = list(range(0, 5))

# 페이지를 담는 빈 리스트 생성
rating_pages = []

for year in years:
    for month in months:
        for week in weeks:
            # HTML 코드 받아오기
            response = requests.get("https://workey.codeit.kr/ratings/index?year=" + str(year) + "&month=" + str(
                month) + "&weekIndex=" + str(week))

            # BeautifulSoup 타입으로 변환하기
            soup = BeautifulSoup(response.text, 'html.parser')

            # "row" 클래스가 1개를 넘는 경우만 페이지를 리스트에 추가
            if len(soup.select('.row')) > 1:
                rating_pages.append(soup)

# 레코드를 담는 빈 리스트 만들기
records = []

for page in rating_pages:
    period = page.select('option[selected=selected]')[2].text
    rank = page.select('.row > .rank')[1:]
    channel = page.select('.row > .channel')[1:]
    program = page.select('.row > .program')[1:]
    rating = page.select('.row > .percent')[1:]

    for i in range(10):
        record = []
        record.append(period)
        record.append(rank[i].text)
        record.append(channel[i].text)
        record.append(program[i].text)
        record.append(rating[i].text)
        records.append(record)

df = pd.DataFrame(data=records, columns=["period", "rank", "channel", "program", "rating"])

print(df.head())
