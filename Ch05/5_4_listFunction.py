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
list1_map_list = list(list1_map) # map객체(함수)를 list로 변환
print('list1_map_list :', list1_map_list)

list2 = [1.1, 2.2, 3.3, 4.4, 5.5]
list2_map = map(int, list2)
list2_map_list = list(list2_map)
print('list2_map_list :', list2_map_list)

list3 = [1, 2, 3, 4, 5]
list3_map = map(lambda x:x*2 , list3)
list3_map_list = list(list3_map)
print('list3_map_list :', list3_map_list)

list4 = ['1', '2', '3', '4', '5']
list4_map = map(int, list4)
list4_map_list = list(list4_map)
print('list4_map_list :', list4_map_list)


# input 함수의 확장
a = input('입력 :')
print('a :', a)

var1, var2, var3 = input('3개의 숫자 입력(띄어씌기 구분) : ').split()
print('var1 :', var1)
print('var2 :', var2)
print('var3 :', var3)
print('var1 +var2 + var3 :', var1 + var2 + var3)

print('num1, num2, num3 데이터 순서대로 입력(띄어쓰기 구분)')
num1, num2, num3 = map(int, input().split())
print('num1 + num2 + num3 :', num1 + num2 + num3)

print('list_data에 입력할 데이터 순서대로 입력(띄어쓰기 구분)')
list_data = list(map(int, input().split()))
print('list_data :', list_data)