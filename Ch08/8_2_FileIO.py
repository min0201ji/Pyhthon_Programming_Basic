"""
이름 : 박민지
날짜 : 2021/04/14
내용 : 파이썬 파일 입출력 실습 교재 p217
"""

# 파일 읽기(파일의 데이터)
file1 = open('C:/Users/501/Desktop/Sample.txt', 'r') #'r' = read
line = file1.readline()

print('line :', line)

file1.close()

# 여러줄 파일 읽기
file2 =open('C:/Users/501/Desktop/Sample.txt', 'r')

while True:
    line = file2.read()

    if not line:
        #읽어들일 라인이 없으면
        break

    print('line :', line)

file2.close()

# 파일쓰기
file3 = open('C:/Users/501/Desktop/Sample2.txt', 'w')
file3.write('안녕하세요.\n')
file3.write('반갑습니다.\n')
file3.write('감사합니다.\n')
file3.close()

#구구단 쓰기
gugudan = open('C:/Users/501/Desktop/gugudan.txt', 'w')

for x in range(2, 10):
    #print('%d단' % x) ↓ 바꾸기
    gugudan.write('%d단\n' % x)
    for y in range(1, 10):
        z = x * y
        #print('%d x %d = %d' % (x, y, z)) ↓ 바꾸기
        gugudan.write ('%d x %d = %d\n' % (x, y, z))

gugudan.close()