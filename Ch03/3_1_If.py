"""
이름 : 박민지
날짜 : 2021/04/07
내용 : 파이썬 조건문 실습 교재 p.60
"""

#if
num1, num2 = 1, 2

if num1 > 0: #조건
    print(('num1은 0보다 크다.'))
    # if문의 명령이 실행된다.,조건이 참이면 (if문 block)실행되고 거짓이면 안나옴.
if num1 > num2:
    print('num1은 num2보다 크다')
    # if조건이 거짓이라서 실행 안됨/이 조건을 건너뛴다

#2개의 if문이 같은것
    if num1 > 0:
        if num2 > 1:
            print('num1은 0보다 크고 num2는 1보다 크다')
if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 그리고 num2는 1보다 크다')

#if ~ else
num3, num4 = 3, 4
if num3 > num4:
    print('num3이 num4보다 크다.')
    """조건이 참일때 실행 영역"""
    #pass #내용을 비워둘때 사용
else:
    print('num3이 num4보다 작다.')
    """조건이 거짓 일때 실행 영역"""
    #pass

#if ~ elif ~else
if num1 > num2:
    print('num1이 num2보다 크다')
elif num2 > num3:
    print('num2는 num3보다 크다')
elif num3 > num4:
    print('num3는 num4보다 크다.')
else:
    print('num4가 가장 크다.')

#연습문제
score = input('점수 입력 :')
score = int(score)
#score = int(input('점수 입력 : ')) 둘다 같은거
print('입력한 점수 :', score)

if score >= 90 and score <= 100:
    # score가 90점에서 100점 이면:
    print('A 입니다.')
elif score >= 80 and score <= 89:
    # 아님 score >= 80 and score <90 #score가 80점에서 89점 이면:
    print('B 입니다.')
elif 70 <= score < 80:
    # score가 70점에서 79점 이면
    print('C 입니다.')
elif 60 <= score < 70:
    # score가 60점에서 69점 이면
    print('D 입니다.')
else:
    print('F 입니다.')

#연습문제 p.63 삼항 조건문
num = 9
result = 0
if num >= 5 :
    result = num * 2
else:
    result = num + 2

print('result =', result)

result2 = num * 2 if num >= 5 else num + 2
print('result2 =', result2)