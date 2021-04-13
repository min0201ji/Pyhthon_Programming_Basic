from Ch06.sub1.Computer import Computer
class SmartPhone(Computer):

    def __init__(self, cpu, ram, hdd, brand, tel):
        super().__init__(cpu, ram, hdd)
        self.brand = brand
        self.tel = tel

    def call(self):
        print('%s Calling...' % self.tel)

    def info(self):
        print('-------------')
        print('모델 :', self.brand)
        print('전화번호: ', self.tel)
        print('사양1: ', self._cpu)
        print('사양2: ', self._ram)
        print('사양3: ', self._hdd)