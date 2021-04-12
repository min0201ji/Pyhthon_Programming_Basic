""""
이름 : 박민지
날짜 : 2021/04/12
내용 : 파이썬 내장함수 실습 교재 p118
"""
import time as t

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

# abs
# ceil
# floor
# round
# random
