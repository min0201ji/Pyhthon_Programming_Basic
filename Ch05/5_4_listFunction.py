""""
이름 : 박민지
날짜 : 2021/04/12
내용 : 파이썬 리스트 내장함수 실습 교재 p115
"""

# 리스트 내장함수
dataset = [1, 4, 3]
print('1,dataset :', dataset)

# 리스트 원소추가
dataset.append(2)
dataset.append(5)
print('2,dataset :', dataset)

# 리스트 원소 정렬(오름차순)
dataset.sort()
print('3,dataset :', dataset)

# 리스트 원소 정렬(내림차순)
dataset.sort(reverse=True)
print('4,dataset :', dataset)

# 리스트 원소 뒤집기
dataset.reverse()
print('5,dataset :', dataset)

# 리스트 원소 삽입
dataset.insert(2, 6) #2번자리에 '6' 삽입
print('6,dataset :', dataset)

# 리스트 원소 삭제
dataset.remove(6)
print('7,dataset :', dataset)

# ↑위에것들 활용 빈도 매우 높음!

# map 함수
# -리스트 원소를 지정된 함수로 일괄 처리해주는 함수
# - 여러개의 데이터를 한번에 다른 형태로 변환할때 많이 사용
def plus10(n):
    return n+10

list1 = [1, 2, 3, 4, 5]
list1_map = map(plus10, list1)
print('list1_map :', list1_map) # 함수를 list로 변환 안해서 그럼
list1_map_list = list(list1_map) # map함수를 list로 변환
print('list1_map_list :', list1_map_list)

# input 함수

