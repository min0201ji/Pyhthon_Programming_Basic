"""
이름 : 박민지
날짜 : 2021/04/07
내용 : 파이썬 반복문 for 실습 교재 p.70
"""

#for
for i in range(5):
    print('i :', i)

for j in range(10, 20):
    print('j :', j)

for k in range(10, 0, -1):
    print('k :', k)

# 1부터 10까지의 합
sum1 = 0

for k in range(11):
    sum1 += k

print('1부터 10까지 합 :', sum1)

# 1부터 10까지 짝수합
sum2 = 0
for k in range(11):

    if k % 2 == 0:
        sum2 += k

print('1부터 10까지 짝수합 :', sum2)

# 중첩 for
for a in range(3):
    print('a :', a)
    for b in range(4):
        print('b :', b)

# 구구단
for x in range(2, 10):

    print('%d단 :', x)

    for y in range(1, 10):

        z = x * y
        print('%d x %d = %d' % (x, y, z))

# 별삼각형
for a in range(1, 10):

    for b in range(a):

        print('☆', end='')

    #print('\n')
    print() # -> \n이랑 같음

for i in range(10):
    print('★'*i)

# 역별삼각형
for a in range(10, 0, -1):

    for b in range(a):

        print('☆', end='')

    #print('\n')
    print() # -> \n이랑 같음


# list를 이용한 for / list가 for이랑 제일 많이 쓰임
nums = [1, 2, 3, 4, 5]

for num in nums:
    print('num :', num)

for person in ['김유신', '김춘추', '이순신']:
    print('person :', person)

scores = [62, 86, 72, 74, 96]
total = 0

for score in scores:
    total += score

print('scores의 총합: ', total)

#리스트의 index와 value 출력
for index, value in enumerate(scores):
    print('{},{}'. format(index, value))

# 튜플 반복문
for num in (10, 20, 30):
    print('num :', num)

# 리스트안(list)안에서 for문
list = [1, 2, 3, 4, 5]

result = [num * 3 for num in list]
result2 = [num * 3 for num in list if num % 2 == 1]

print('result :', result)
print('result2: ', result2)