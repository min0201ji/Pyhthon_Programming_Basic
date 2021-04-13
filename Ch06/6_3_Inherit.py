"""
이름 : 박민지
날짜 : 2021/04/13
내용 : 파이썬 클래스 상속 실습하기 교재 p163
"""
from Ch06.sub2.StockAccount import StockAccount

from Ch06.sub2.SmartPhone import SmartPhone


kb = StockAccount('KB증권', '101-12-1222', '김유신', 100000, '삼성전자', 0, 0)
kb.buy(3, 30000)
kb.show()

kb.sell(3, 40000)
kb.show()

iphone = SmartPhone('i8', '64GB', '128GB', '아이폰12', '010-1234-5678')
iphone.calc()
iphone.call()
iphone.info()