"""
이름 : 박민지
날짜 : 2021/04/15
내용 : 파이썬 클래쓰 연습문제
"""

class King:

    def __init__(self, #name, #year):
        self.name = name
        self.year = year

    def show(self):
        print('-------------')
        print('name :', self.name)
        print('year :', self.year)

if __name__ == '__main__':

    King1 = King(#'태조', 1392)
    King2 = King#('태종', 1392)
    King3 = King#('세종대왕', 1418)

    King1.show()
    King2.show()
    King3.show()
