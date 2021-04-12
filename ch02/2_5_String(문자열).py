"""
이름 : 박민지
날짜 : 2021/04/06
내용 : 파이썬 표준 입출력 실습 교재 p.42
"""

#문자열 더하기
str1 = 'Hello'
str2 = 'Python'
str3 = str1 +str2

print('str3 :', str3)

#문자열 곱하기
name = '박민지'
result = name * 3
print('result :', result)

#문자열 길이 구하기
sample = 'Hello World'
print('sample 길이 :', len(sample))

#문자열 인덱스
print('sample 1번째 문자:', sample[0])
print('sample 7번째 문자', sample[6])
print('sample -1번째 문자', sample[-1])

#문자열 자르기
print('sample 0 ~ 5까지 문자 :', sample[0:5])
print('sample 0 ~ 5까지 문자 :', sample[:5]) #처음부터 5까지
print('sample World 출력 :', sample[6:11])
print('sample World 출력 :', sample[6:]) #6에서 마지막까지

#문자열 분리
people = '김유신|김춘추|장보고|강감찬|이순신'
p1, p2, p3, p4, p5 = people.split('|') #splash 구분한다는 뜻 (|)

print('p1 :', p1)
print('p2 :', p2)
print('p3 :', p3)
print('p4 :', p4)
print('p5 :', p5)

#문자열 이스케이프
print('서울\n대전\n대구\n부산\n광주')
print('한국\t미국\t일본\t중국\t호주')
print('안녕하세요. \'반갑습니다.\'')
