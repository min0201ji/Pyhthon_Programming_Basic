"""
이름 : 박민지
날짜 : 2021/04/15
내용 : 파이썬 팩토리얼 함수 연습문제
"""

def factorial(n):

    if n <= 1:
        return 1

    return n * factorial(#n-1)

if __name__ == '__main__':
    print('3! =', factorial(3))
    print('4! =', factorial(4))
    print('5! =', factorial(5))