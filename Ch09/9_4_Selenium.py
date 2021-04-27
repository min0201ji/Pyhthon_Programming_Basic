"""
이름 : 박민지
날짜 : 2021/04/27
내용 : 파이썬 Selenium 가상 브라우저 크롤링 실습
setting -> Selenium apply
chromedriver install
chrome ver 확인 -> 도움말 -> 크롬정보
"""
from selenium import webdriver

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 이동
browser.get('https://naver.com')

# 네이버 로그인 버튼 클릭
btn_login = browser.find_element_by_css_selector('#account > a')
btn_login.click()

# 네이버 아이디, 비밀번호 입력
input_id = browser.find_element_by_css_selector('#id')
input_pw = browser.find_element_by_css_selector('#pw')

input_id.send_keys('endsuqkr')
input_pw.send_keys('1234')

# 최종 로그인 버튼 클릭
input_login = browser.find_element_by_id('log.login')
input_login.click()


