"""
날짜 : 2021/04/29
이름 : 홍길동
내용 : 코딩 테스트 - 상하좌우
"""

# n값 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

"""# 이동 계획을 하나씩 확인
for plan in plans:
    if plan == 'R':
        if y == n:
            continue
        else:
            y += 1
            
    if plan == 'D':
        if x == n:
            continue
        else:
            x += 1
            
    if plan == 'L':
        if y == n:
            continue
        else:
            y -= 1
            
    if plan == 'U':
        if x == n:
            continue
        else:
            x += 1"""

for plan in plans:

    nx = ny = 0

    for i in range(len(move_types)):

        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny


# 최종 좌표 출력
print(x, y)