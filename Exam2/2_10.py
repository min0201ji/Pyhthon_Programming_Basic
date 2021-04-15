"""
이름 : 박민지
날짜 : 2021/04/15
내용 : 파이썬 가위, 바위, 보 게임
"""
import random

def game():
    words = ['가위', '바위', '보']
    while True:
        you_word = input('가위, 바위, 보 입력 : ')
        try:
            if you_word not in words:
                raise ValueError
        except ValueError:
            print('잘못 입력 하셨습니다.')
            #
        else:
            #
    
    com_word = random.choice(words)
    print('컴퓨터 결과 :', com_word)
    
    if com_word == '가위' and you_word == '가위':
        print('무승부')
    if com_word == '가위' and you_word == '바위':
        print('당신의 승리!')
    if com_word == '가위' and you_word == '보':
        print('컴퓨터 승리!')
    if com_word == '바위' and you_word == '가위':
        print('컴퓨터 승리!')
    if com_word == '바위' and you_word == '바위':
        print('무승부')
    if com_word == '바위' and you_word == '보':
        print('당신의 승리!')
    if com_word == '보' and you_word == '가위':
            print('당신의 승리!')
    if com_word == '보' and you_word == '바위':
        print('컴퓨터 승리!')
    if com_word == '보' and you_word == '보':
        print('무승부')

while True:
    #
    print('0:종료, 1:한번 더하기')
    again = int(input('입력 : '))

    if again == 0:
        break

print('게임종료...')