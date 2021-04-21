"""
이름 : 박민지
날짜 : 2021/04/21
내용 : 파이썬 데이터베이스 처리 실습 교재 p295
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='54.180.160.240',
                       user='park',
                       password='1234',
                       db='park',
                       charset='utf8')

# SQL 실행객체 생성
cur = conn.cursor()

# SQL 실행
sql = "UPDATE `USER1` SET `name` = '홍길동' " # 마지막에 동' " 사이 띄어쓰기 주의!
sql += "WHERE `uid`='p101';"

cur.execute(sql)
conn.commit()

# 데이터베이스 종료
conn.close()



print('UPDATE 완료...')

