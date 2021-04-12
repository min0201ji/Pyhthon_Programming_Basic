"""
이름 : 박민지
날짜 : 2021/04/06
내용 : 파이썬 자료구조 set(집합) 실습 교재 p.96
"""

#set(집합) 생성
set1 = {1, 2, 3, 4, 5, 3} #집합은 순서 없음
print('set1 type :', type(set1))
print('set1 :', set1)

set2 = set('Hello World') #저장은 'H' 'e' 'l' 'o' 'W' 'r' 'd' ' ' 이렇게 저장됨, 중복허용X
print('set2 type:', type(set2))
print("set2 :", set2)

#집합 출력(리스트 변환)
list1 = list(set1) #set을 list로 변환
print('list1[0] :', list1[0])
print('list1[1] :', list1[1])
print('list1[2] :', list1[2])

list2 = list(set2)
print('list2[0] :', list2[0])
print('list2[1] :', list2[1])
print('list2[2] :', list2[2])








