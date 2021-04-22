"""
이름 : 박민지
날짜 : 2021/04/22
내용 : 코딩 테스트 - 큰 수의 법칙
"""

# n, m, k를 공백으로 구분하여 입력하기
print('n, m, k를 공백으로 구분하여 차례로 입력')
n, m, k = map(int, input().split())

# n개의 숫자를 공백으ㅡ로 구분하여 입력받기
print('n개의 숫자를 공백으로 구분하여 입력')
data = list(map(int, input().split()))

# 데이터 정렬하기
data.sort()
# 가장 큰 수 구하기
first = data[n-1]
# 두 번째로 큰 수 구하기
second = data[n-2]

result = 0

while True:
    # 가장 큰 수를 K번 더하기
    for i in range(k):

        if m == 0:
            break

        result += first
        m -= 1

    if m == 0:
        break

    result += second
    m -= 1

print(result)
