"""
이름 : 박민지
날짜 : 2021/04/15
내용 : 파이썬 클래쓰 연습문제
"""

class King:

    def __init__(self,#name(M) #name=태조, #year(M) #year=1392):
        self.name = name
        self.year = year

    def show(self):
        print('-------------')
        print('name :', self.name)
        print('year :', self.year)

if __name__ == '__main__':

    King1 = King()
    King2 = King#('태종') 뒤에 1392 써도 되고 안써도 됨! 왜냐면 위에 값이 있음 이미
    King3 = King#('세종대왕', 1418)

    King1.show()
    King2.show()
    King3.show()
