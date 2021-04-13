"""
이름 : 박민지
날짜 : 2021/04/13
내용 : 파이썬 객체지향 캡슐화 실습하기 교재 p161
"""

from Ch06.sub1.Account import Account

kb = Account('국민은행', '121-11-1234', '김유신', 10000)
kb.deposit(20000)
kb.withdraw(5000)

# 캡슐화 적용으로 취약코드를 예방한다.
# 캡슐화 방법 : 멤버변수에 __를 선언
# kb.money -= 1 -> 이렇게 해도 sub1의 account에서 __사용해서 캡슐

kb.show()