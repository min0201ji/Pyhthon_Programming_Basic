"""
날짜 : 2021/04/28
이름 : 박민지
내용 : 파이썬 날씨 데이터 크롤링 실습
"""
from selenium import webdriver
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='54.180.160.240',
                       user='park',
                       password='1234',
                       db='park',
                       charset='utf8')
# SQL 실행객체 생성
cur = conn.cursor()

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 지역 태그 선택
tags_tr = browser.find_elements_by_css_selector('#weather_table > tbody > tr')

for tr in tags_tr:

    col1 = tr.find_element_by_css_selector('td:nth-child(1) > a').text
    col2 = tr.find_element_by_css_selector('td:nth-child(2)').text
    col3 = tr.find_element_by_css_selector('td:nth-child(3)').text
    col4 = tr.find_element_by_css_selector('td:nth-child(4)').text
    col5 = tr.find_element_by_css_selector('td:nth-child(5)').text
    col6 = tr.find_element_by_css_selector('td:nth-child(6)').text
    col7 = tr.find_element_by_css_selector('td:nth-child(7)').text
    col8 = tr.find_element_by_css_selector('td:nth-child(8)').text
    col9 = tr.find_element_by_css_selector('td:nth-child(9)').text
    col10 = tr.find_element_by_css_selector('td:nth-child(10)').text
    col11 = tr.find_element_by_css_selector('td:nth-child(11)').text
    col12 = tr.find_element_by_css_selector('td:nth-child(12)').text
    col13 = tr.find_element_by_css_selector('td:nth-child(13)').text
    col14 = tr.find_element_by_css_selector('td:nth-child(14)').text

    # print('{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14))

    # SQL 실행
    sql = "INSERT INTO `Weather` SET"
    sql += "`col1`='"+col1+"',"
    sql += "`col2`='"+col2+"',"
    sql += "`col3`='"+col3+"',"
    sql += "`col4`='"+col4+"',"
    sql += "`col5`='"+col5+"',"
    sql += "`col6`='"+col6+"',"
    sql += "`col7`='"+col7+"',"
    sql += "`col8`='"+col8+"',"
    sql += "`col9`='"+col9+"',"
    sql += "`col10`='"+col10+"',"
    sql += "`col11`='"+col11+"',"
    sql += "`col12`='"+col12+"',"
    sql += "`col13`='"+col13+"',"
    sql += "`col14`='"+col14+"',"
    sql += "`rdate` = NOW();"

    cur.execute(sql)
    conn.commit()

    print('수집 중...')
    # for end

# 데이터베이스 종료
conn.close()

# 가상브라우저 종료
browser.quit()

print('수집 완료...')