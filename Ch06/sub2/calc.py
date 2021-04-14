def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def multi(x, y):
    return x*y

def div(x, y):
    return x/y
# 프로그램 시작점이 없는 경우
print('plus(1, 1) :', plus(1, 1))
print('minus(1, 1) :', minus(1, 1))


if __name__ == '__main__':
# 프로그램 시작점을 선언해서 의도치 않는 코드 실행을 차단
    print('plus(1, 1) :', plus(1, 1))
    print('minus(1, 1) :', minus(1, 1))
    print('multi(1, 1) :', multi(1, 1))
    print('div(1, 1) :', div(1, 1))