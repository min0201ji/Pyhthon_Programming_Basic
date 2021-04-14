"""
이름 : 박민지
날짜 : 2021/04/14
내용 : 파이썬 정규표현식 실습 교재 p192

정규표현식(Regular Expression)
- 특정한 규칙을 갖는 문자열을 처리하기 위한 문법
- 일반적으로 특정 문자 검색, 매칭 여부를 확인에 사용
"""

import re
from re import findall, match

str1 = '1234 abc홍길동 ABC_555_6 부산광역시'

# 숫자검색
print(findall('1234', str1))
print(findall('[0-9]', str1))
print(findall('[0-9]{3}', str1))
print(findall('[0-9]{3,}', str1))

# 문자열 검색
print(findall('[가-힣]{3,}', str1))
print(findall('[a-z|A-Z]{3,}', str1))

str2 = 'test1abcABC 123mbc 45test'

print(findall('^test', str2))
print(findall('st$', str2))

# 단어 검색
str3 = 'test^홍길동 abc 대한*민국 123$tbc'

result = findall('\\w{3,}', str3)
print(result)

# 응용
jumin1 = '123456-1891234'
result1 = match('[0-9]{6}-[1-4][0-9]{6}', jumin1)

if result1:
    print('jumin1은 유효한 번호입니다.')
else:
    print('jumin1은 유효하지 않은 번호입니다.')