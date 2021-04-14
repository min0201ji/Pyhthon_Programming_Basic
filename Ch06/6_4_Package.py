"""
이름 : 박민지
날짜 : 2021/04/14
내용 : 파이썬 패키지와 모듈 실습 교재 p175
"""

import Ch06.sub2.calc as calc
from Ch06.sub1.Account import Account
#from Ch06.sub2.calc import *(plus minus multi div) 도 가능

r1 = calc.plus(1, 2)
r2 = calc.minus(1, 2)
r3 = calc.multi(2, 3)
r4 = calc.div(4, 2)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)

