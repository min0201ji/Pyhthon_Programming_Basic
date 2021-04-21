"""
이름 : 박민지
날짜 : 2021/04/21
내용 : 파이썬 SQLite 실습 교재 p289
"""
import sqlite3

conn = sqlite3.connect('./data/sqlite_db')

cur = conn.cursor()

cur.execute("INSERT INTO `USER1` VALUES ('a101','김유신','010-1234-1001',21);")
cur.execute("INSERT INTO `USER1` VALUES ('a102','김춘추','010-1234-1002',22);")
cur.execute("INSERT INTO `USER1` VALUES ('a103','장보고','010-1234-1003',23);")
cur.execute("INSERT INTO `USER1` VALUES ('a104','강감찬','010-1234-1004',24);")
cur.execute("INSERT INTO `USER1` VALUES ('a105','이순신','010-1234-1005',25);")
conn.commit()

print('SQLite INSERT 완료...')