"""
날짜 : 2021/05/10
이름 : 박민지
내용 : 1이 될 때까지
"""

n, k = map(int, input().split())
result = 0

while True:

    if n == 1:
        break

    if n % k == 0:
        n /= k
    else:
        n -= 1

    result += 1

print(result) # result = 횟수