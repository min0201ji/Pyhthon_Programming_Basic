"""
이름 : 박민지
날짜 : 2021/04/06
내용 : 파이썬 자료구조 Dictionary 실습 교재 p.98
"""

#Dictionary(=key value) 생성
dic1 = {1: '서울', 2: '대전', 3: '대구', 4: '부산', 5: '광주'}
dic2 = {
    'A': 'Apple',
    'B': 'Banana',
    'C': 'Cherry',
}

dic3 = {
    101: [1, 2, 3, 4, 5], #list
    102: (6, 7, 8, 9, 10), #list but tuple
    103: {'한국', '미국', '중국', '일본'}, #set
    104: {'p1': '김유신', 'p2': '김춘추', 'p3': '이순신'} #dic 안에 dic
}

#dic 출력
print('dic1 type:', type(dic1))
print('dic1[1] :', dic1[1])
print('dic1[4] :', dic1[4])
print('dic1[5] :', dic1[5])

print('dic2 type:', type(dic2))
print("dic2['A'] :", dic2['A']) #안의 '를 표시하기 위해 "로 바꿈
print("dic2['B'] :", dic2['B'])
print("dic2['C'] :", dic2['C'])

print('dic3 type:', type(dic3))
print("dic3[101][0] :", dic3[101][0])
print("dic3[101][2] :", dic3[101][2])
print("dic3[102][4] :", dic3[102][4])
print("dic3[103] :", dic3[103])
print("dic3[104]['p1'] :", dic3[104]['p1'])

#dic 응용
dictionaries = [dic1, dic2, dic3] #list로 만듬

print('dictionaries type:', type(dictionaries))
print('dictionaries[0][4] :', dictionaries[0][4])
print('dictionaries[1][A] :', dictionaries[1]['A'])
print("dictionaries[2][104]['p2'] :", dictionaries[2][104]['p2'])