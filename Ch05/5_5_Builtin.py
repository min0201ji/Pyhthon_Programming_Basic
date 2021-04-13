""""
이름 : 박민지
날짜 : 2021/04/12 & 2021/04/13
내용 : 파이썬 내장함수 실습 교재 p118
"""
import time as t
import math as m
import random as r
# time
t1 = t.time()
print('t1 :', t1)

t2 = t.ctime()
print('t2 :', t2)


now = t.localtime(t.time())
year = t.strftime('%Y',now)
month = t.strftime('%m',now)
date = t.strftime('%d',now)
hour = t.strftime('%H',now)
min = t.strftime('%M',now)
sec = t.strftime('%S',now)

print('%s년 %s월 %s일' % (year, month, date))
print('%s시 %s분 %s초' % (hour, min, sec))

# abs(절대값)
r1 = abs(-5)
print('r1 :', r1)

# ceil(올림)
r2 = m.ceil(1.2)
r3 = m.ceil(1.8)

print('r2 :', r2)
print('r3 :', r3)

# floor(내림)
r4 = m.floor(1.2)
r5 = m.floor(1.8)

print('r4 :', r4)
print('r5 :', r5)

# round(반올림)
r6 = round(1.2)
r7 = round(1.8)

print('r6 :', r6)
print('r7 :', r7)

# random
num1 = r.random()
print('num1 :', num1) # 0 ~ 1 사이의 실수

num2 = num1 * 10
print('num2 :', num2) # 0 ~ 10 사이의 실수

num3 = m.ceil(num2) #(num2) = (num1*10)
print('num3 :', num3) # 1 ~ 10 사이의 정수

result = m.ceil(r.random()*10)
print('result :', result)

result = m.ceil(r.random()*45) # 1 ~ 45까지의 임의의 정수
print('result :', result)