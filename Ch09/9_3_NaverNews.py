"""
이름 : 박민지
날짜 : 2021/04/26
내용 : 파이썬 Naver 뉴스 크롤링 실습하기
"""
import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook #Workbook -> 엑셀

# 네이버 뉴스 요청하기
resp = req.get('https://news.naver.com/', headers={'User-Agent' : 'Mozilla/5.0'})
#print('resp.text')

# 헤드라인 뉴스 제목 5건 파싱
dom = bs(resp.text, 'html.parser')
a_tags = dom.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')
# .=class

for a in a_tags:
    print('제목 : ',a.text.strip()) #공백(=trim), strip() 함수로 없앨수 있음

# IT 뉴스 속보 1 ~ 10 페이지 크롤링 하기

# 현재 페이지 값
page = 1

# Excel 파일 생성
workbook = Workbook()
sheet = workbook.active

while True:
    url = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105&date=20210426&page='+str(page)
    html = req.get(url, headers={'User-Agent' : 'Mozilla/5.0'}).text

    dom = bs(html, 'html.parser')

    a_list = dom.select('#main_content > div.list_body.newsflash_body > ul > li > dl > dt:not(.photo) > a')

    for tit in a_list:
        #print('제목(tit) : ', tit.text.strip())
        sheet.append([tit.text.strip()])

    # 다음 페이지 값으로 증감
    page += 1

    if page > 10:
        break

    # 마지막 페이지 까지 하는방법
    # if len(a_list) < 20:
    #    break

# Excel 파일 저장
workbook.save('C:/Users/501/Desktop/News.xlsx')
workbook.close()


print("크롤링 완료...")
