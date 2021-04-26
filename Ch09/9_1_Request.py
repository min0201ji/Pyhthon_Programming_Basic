"""
이름 : 박민지
날짜 : 2021/04/26
내용 : 파이썬 HTML Request 실습하기 교재 p255
"""
import requests as req
from bs4 import BeautifulSoup as bs

# naver HTML 페이지 요청하기
html = req.get('https://news.naver.com/main/home.nhn', headers={'User-Agent': 'Mozilla/5.0'}).text
#print(html)

# HTML 파싱(HTML에서 특정 데이터 추출)
dom = bs(html, 'html.parser')
tag_tit = dom.select_one('#today_main_news > div.hdline_news > ul > li:nth-child(1) > div.hdline_article_tit > a') # #=id, >=child(자식)

print(tag_tit.text)
