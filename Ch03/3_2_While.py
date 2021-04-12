"""
이름 : 박민지
날짜 : 2021/04/07
내용 : 파이썬 반복문 실습 교재 p.64
"""
# while
num1, num5 = 1, 5

while num1 <= num5:
    print('num1 :', num1)
    num1 += 1

# 1부터 10까지 합
k, sum = 1, 0

while k <= 10:
    sum += k
    k += 1

print('1부터 10까지 합:', sum)

# 1부터 10까지 짝수합
i, tot = 1, 0

while i <= 10:

    if i % 2 == 0:
        tot += i

    i += 1

print('1부터 10까지 짝수합 :', tot)

# break
num = 1

while True:

    if num % 5 == 0 and num % 7 == 0:
        #반복문 종료
        break
    #무한으로 실행 (=무한루프) but if조건으로 break 가능

    num += 1

print('5와 7의 최소공배수 :', num)

# continue
begin, total = 1, 0

while begin <= 10:

    begin += 1

    if begin % 2 == 1:
        #반복문의 상위로 이동
        continue

    total += begin

print('1부터 10까지 짝수합 :', total)

