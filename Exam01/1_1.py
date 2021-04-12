"""
이름 : 박민지
날짜 : 2021/04/08
내용 : 파이썬 연습문제 1. 연산자
"""
x = 4
y = -2#

z = x + y
print('연산1 : x + y =', z)

z = x - y
print('연산2 : x - y =', z)

z = x * y
print('연산3 : x * y =', z)

z = x / y
print('연산4 : x / y =', z)

z = (x + y) * (x - y)
print('연산5 : (x + y) * (x - y) =', z)

z = (x * y) + (x / y)
print('연산5 : (x * y) + (x / y) =', z)

z = x * y #y**2
print('연산7 : %d x %d = %d' %(4#x, 4 #y**2, 16 #z))

z = x * y #y**3
print('연산8 : %d x %d = %d' %(4#x, -8 #y**3, -32 #z))

z = x * y #y**4
print('연산9 : %d x %d = %d' %(4#x, 16 #y**4, 64 #z))

z = x * y #y**5
print('연산10 : %d x %d = %d' %(4#x, 32 #y**5, -128 #z))