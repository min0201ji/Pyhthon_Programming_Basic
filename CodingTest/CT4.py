"""
날짜 : 2021/05/10
이름 : 박민지
내용 : 파이썬 코딩테스트 - 왕실의 나이트
"""

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

print('row : %d, column : %d' % (row, column))
result = 0

# 오른쪽 2칸, 위쪽 1칸
next_row = row + 2
next_column = column - 1

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8: # 하나라도 틀리면 거짓
    result += 1 # result => 경우의 수

# 오른쪽 2칸, 아래쪽 1칸
next_row = row + 2
next_column = column + 1

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 왼쪽 2칸, 위쪽 1칸
next_row = row - 2
next_column = column - 1

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 왼쪽 2칸, 아래쪽 1칸
next_row = row - 2
next_column = column + 1

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 위쪽 2칸, 오른쪽 1칸
next_row = row + 1
next_column = column - 2

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 위쪽 2칸, 왼쪽 1칸
next_row = row - 1
next_column = column - 2

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 아래쪽 2칸, 오른쪽 1칸
next_row = row + 2
next_column = column + 2

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 아래쪽 2칸, 왼쪽 1칸
next_row = row + 2
next_column = column - 1

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)


