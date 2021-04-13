"""
이름 : 박민지
날짜 : 2021/04/12
내용 : 파이썬 함수 실습하기 교재 p114
"""

#함수정의 : 일련의 코드로직을 모듈화한 코드블럭
def f(x):
    y = 2 * x + 3
    return y

#함수호출(실행)
r1 = f(1) #(1)이 return이 되는것
r2 = f(2)
r3 = f(3)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)

#함수유형
#함수유형 type 1 - 매개변수 O, return값 O
def type1(x, y):
    z = x + y
    return z

rs1 = type1(1, 2)
rs2 = type1(2, 3)

print('rs1 :', rs1)
print('rs2 :', rs2)

#함수유형 type 2 - 매개변수 O, return값 X
def type2(items):
    sum = 0

    for item in items:
        sum += item

    print('items 합: ', sum)

type2([1,2,3,4,5]) #리턴이 없어서 대입연산자(=) 필요x
type2([6,7,8,9,10])

#함수유형 type 3 - 매개변수 X, return값 O
def type3():

    sum =  0

    for i in range(11):
        sum += i

    return sum

result = type3() #type3() #매개변수 없어서 입력할 값 없음
print('result :', result)

#함수유형 type 4 - 매개변수 X, return값 X
def type4():

    result = type3()
    print('type4 result :', result)

type4()


#연습문제

"""def gugudan(num):
    print('%d단' % num)
    print('%d x %d = %d' % (num, 1, num * 1))
    print('%d x %d = %d' % (num, 2, num * 2))
    print('%d x %d = %d' % (num, 3, num * 3))
    print('%d x %d = %d' % (num, 4, num * 4))
    print('%d x %d = %d' % (num, 5, num * 5))
    print('%d x %d = %d' % (num, 6, num * 6))
    print('%d x %d = %d' % (num, 7, num * 7))
    print('%d x %d = %d' % (num, 8, num * 8))
    print('%d x %d = %d' % (num, 9, num * 9))
"""
def gugudan(num):
    print('%d단' % num)
    for i in range(1, 10):
        print('%d x %d = %d' % (num, i, num * i))


gugudan(2)
gugudan(3)
gugudan(5)
gugudan(7)