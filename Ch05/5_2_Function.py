"""
이름 : 박민지
날짜 : 2021/04/12
내용 : 파이썬 특수함수 실습하기 교재 p129
"""
# 디폴트 매개변수
def hello(name='홍길동', age=27):
    print('이름 :', name)
    print('나이 :', age)

hello()
hello('김유신')
hello('감츈츄', 25)


# 가변 매개변수
def total(*scores): #*이 가변매개 변수의미
    sum = 0

    for score in scores:
        sum += score

    return sum

r1 = total(1)
r2 = total(1, 2)
r3 = total(1, 2, 3)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)


# 하나 이상의 리턴값
def sum_and_multi(num1, num2):
    y1 = num1 + num2
    y2 = num1 * num2
    return y1, y2

rs1, rs2 = sum_and_multi(1, 2)
rs3, rs4 = sum_and_multi(3, 4)

print('rs1 :', rs1 )
print('rs2 :', rs2 )
print('rs3 :', rs3 )
print('rs4 :', rs4 )


# 변수에 저장하는 함수
def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

var1 = plus
var2 = minus

result1 = var1(2, 3) #변수 var1에 플러스 밑은 마이너스
result2 = var2(2, 3)

print('result1 :', result1)
print('result2 :', result2)

cals = [plus, minus]
res1 = cals[0](3, 4)
res2 = cals[1](5, 6)

print('res1 :', res1)
print('res2 :', res2)

# 람다함수 - 간결하게 만들때 사용하는 함수
lam_plus = lambda x, y: x + y #lam_plus 는 변수, 그리고 뒤의 함수는 익명함수다

result = lam_plus(2, 3)
print('result :', result)
