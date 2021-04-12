"""
이름 : 박민지
날짜 : 2021/04/12
내용 : 파이썬 모듈 패키지 실습 교재 p114 (or ch6)
"""
import Ch05.sub.calc as calc
import Ch05.sub.calc as cal2
#module 선언

r1 = calc.plus(1, 2)
r2 = calc.minus(1, 2)
r3 = cal2.multi(1, 2)
r4 = cal2.div(1, 2)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)