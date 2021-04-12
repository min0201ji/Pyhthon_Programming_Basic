"""
이름 : 박민지
날짜 : 2021/04/06
내용 : 파이썬 자료구조 튜플 실습 교재 p.92
- 튜플 : 고정 리스트(추가,삭제, 수정 불가능)
"""

#튜플 생성
tuple1 = (1, 2, 3, 4, 5)
print('tuple1 type :', type(tuple1))
print('tuple1[0] :', tuple1[0])
print('tuple1[4] :', tuple1[4])
print('tuple1[0] : %d' % tuple1[0])
print('tuple1[4] : %d' % tuple1[4])

tuple2 = ('서울', '대전', '대구', '부산', '광주')
print('tuple2 type :', type(tuple2))
print('tuple2[0] : %s' % tuple2[0])
print('tuple2[4] : %s' % tuple2[4])

#tuple 수정, 추가, 삭제
nums = (1, 2, 3, 4, 5) #튜플은 ()생략 가능 nums = 1,2,3,4,5 가능
#nums[0] = 6
#nums[4] = []
#당연히 수정 추가 삭제 불가능 하기에 오류뜸
