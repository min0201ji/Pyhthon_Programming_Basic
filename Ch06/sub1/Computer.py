class Computer:

    # 속성
    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    # 기능
    def calc(self):
        print('Computer calc...')

    def info(self):
        print('------------')
        print('cpu :', self.cpu)
        print('ram :', self.ram)
        print('hdd :', self.hdd)