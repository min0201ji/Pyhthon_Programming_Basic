"""
날짜 : 2021/04/28
이름 : 박민지
내용 : 파이썬 영화 리뷰 크롤링 실습
"""
from selenium import webdriver

# 수집 텍스트파일 생성
file = open('./movie_review.txt',
            mode='w',
            encoding='utf8')

# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 영화 미나리 리뷰페이지 이동
browser.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=187310&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1')

page = 1

while True:
    # 영화 리뷰 출력
    tags_span = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li > div.score_reple > p > span:last-child')

    for span in tags_span:
        #print(span.text.strip())
        file.write(span.text.strip()+'\n')

    print('%d 페이지 수집완료...' % page)

    try:
        # 다음 페이지 클릭
        btn_next = browser.find_element_by_css_selector('body > div > div > div.paging > div > a:last-child > em')
        btn_next.click()
        page += 1

    except:
        break


# 파일 닫기
file.close()

# 가상 브라우저 종료
browser.quit()

print('수집 완료...')