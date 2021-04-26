"""
이름 : 박민지
날짜 : 2021/04/26
내용 : 파이썬 HTML Selector 실습하기 교재 p263
"""
import requests as req
from bs4 import BeautifulSoup as bs

# 페이지 요청하기
resp = req.get('http://chhak.kr/py/test1.html')
resp.encoding = 'utf-8'
#print(resp.text)

# HTML 파싱
dom = bs(resp.text, 'html.parser')

tit = dom.html.body.h1.text
txt = dom.select_one('#txt').text
li1_txt = dom.select_one('ul > li:first-child').text
li2_txt = dom.select_one('ul > li:nth-child(2)').text
li5_txt = dom.select_one('ul > li:last-child')
li_tags = dom.select('ul > li')


print('tit : ', tit)
print('txt : ', txt)
print('li1_txt: ', li1_txt)
print('li2_txt: ', li2_txt)
print('li5_txt: ', li5_txt.text)
print('li_tags: ', li_tags)

for li in li_tags:
    print('li.text : ', li.text) #개별적으로 text를 위해서 for문 필요!