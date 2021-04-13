from Ch06.sub1.Account import Account

class StockAccount(Account):
    def __init__(self, bank, id, name, money, stock, amount, price):
        # 부모클래스(Account)생성자 실행, 자식클래스(StockAccount)
        super().__init__(bank, id, name, money)
        self.stock = stock
        self.amount = amount
        self.price = price
        
    def sell(self, amount, price):
        self.amount -= amount
        self._money += (self.amount * self.price)
        
    def buy(self, amount, price):
        self.amount += amount
        self._money -= (self.amount * self.price)
        
    def show(self):
        super().show()
        print('주식종목 :', self.stock)
        print('주식수량 :', self.amount)
        print('주식가격 :', self.price)