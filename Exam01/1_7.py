"""
이름 : 박민지
날짜 : 2021/04/08
내용 : 파이썬 연습문제 3. 피보나치 수열
"""

n1 = 1
n2 = 2

print(n1, end=',')
print(n2, end=',')

for i in range(1, 10):
    n3 = n1 + n2
    print(n3, end=',')

    n1 = n2 #자리교환
    #n2 = n3