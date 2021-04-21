"""
이름 : 박민지
날짜 : 2021/04/21
내용 : 파이썬 데이터베이스 처리 실습 교재 p295
file -> setting -> project workplace -> python interpreter -> + -> PyMySql 추가
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
sql = "INSERT INTO `USER1` VALUES ('p101','김유신','010-1234-1001',25);"
cur.execute(sql)
conn.commit()

# 데이터베이스 접속종료
conn.close()

print('INSERT 완료...')
