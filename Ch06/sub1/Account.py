class Account:


    # 속성 (생성자 정의(__init__))
    # (나를 어떻게 코딩으로 만드는가 ex- 이름,나이,성별,몸무게...)
    def __init__(self, bank, id, name, money):
        self.bank = bank
        self.id = id
        self.name = name
        self.money = money

    # 기능 (내가 할 수 있는것 ex-잠자는것, 먹는것(동사,Action))
    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        self.money -= money

    def show(self):
        print('--------------')
        print('은행명 :', self.bank)
        print('계좌번호 :', self.id)
        print('입금주 :', self.name)
        print('현재잔액 :', self.money)


