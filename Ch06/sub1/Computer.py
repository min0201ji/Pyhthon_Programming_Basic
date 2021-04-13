class Computer:

    # 속성
    def __init__(self, cpu, ram, hdd):
        self._cpu = cpu
        self._ram = ram
        self._hdd = hdd

    # 기능
    def calc(self):
        print('Computer calc...')

    def info(self):
        print('------------')
        print('cpu :', self._cpu)
        print('ram :', self._ram)
        print('hdd :', self._hdd)