""""
이름 : 박민지
날짜 : 2021/04/13
내용 : 파이썬 클래스 실습하기 교재 p148
"""
from Ch06.sub1.Account import Account
# 객체 생성
kb = Account('국민은행', '121-12-1111', '김유신', 10000)
wr = Account('우리은행', '112-12-1919', '김춘추', 20000)

kb.deposit(40000)
kb.withdraw(5000)
kb.show()

wr.deposit(10000)
wr.withdraw(7000)
wr.show()