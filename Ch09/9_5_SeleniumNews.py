"""
이름 : 박민지
날짜 : 2021/04/27
내용 : 파이썬 Selenium을 이용한 네이버 뉴스 크롤링 실습/ 웹드라이버 package
"""
from selenium import webdriver
from openpyxl import Workbook

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 뉴스 홈 이동
browser.get('https://news.naver.com/')

# 네이버 뉴스 속보 클릭
btn_sokbo = browser.find_element_by_css_selector('#lnb > ul > li:nth-child(2) > a')
btn_sokbo.click()

# IT/과학 클릭
btn_it = browser.find_element_by_css_selector('#snb > ul > li:nth-child(6) > a')
btn_it.click()

# Excel 파일 생성
workbook = Workbook()
sheet = workbook.active

# 페이지 관련 반복변수 선언
i, num = 0, 1

while True:
    try:

        # 뉴스목록 선택
        tags_a = browser.find_elements_by_css_selector('#main_content > div.list_body.newsflash_body > ul > li > dl > dt:not(.photo) > a')
        # print(tags_a)

        print('현재 페이지: ', num)
        for a in tags_a:
            print(a.text)
            sheet.append([a.text])

        # 다음 페이지 번호 리스트 선택
        pages_a = browser.find_elements_by_css_selector('#main_content > div.paging > a')
        pages_a[i].click()

        num += 1
        i += 1

        if num % 10 == 1:
            i = 1

    except:
        print('크롤링 완료')
        break


# Excel 저장
workbook.save('C:/Users/501/Desktop/News2_1.xlsx')
workbook.close()


# 브라우저 종료
browser.quit()

