# 날짜 : 2021/04/28
# 이름 : 박민지
# 내용 : 파이썬 크롤링 날씨 테이블
CREATE TABLE `Weather` (
	`seq` INT AUTO_INCREMENT PRIMARY KEY,
	`col1` VARCHAR(20) COMMENT '지역',
	`col2` VARCHAR(20) COMMENT '현재일기',
	`col3` VARCHAR(20) COMMENT '시정',
	`col4` TINYINT COMMENT '운량',
	`col5` TINYINT COMMENT '중하운량',
	`col6` DOUBLE COMMENT '현재기온',
	`col7` DOUBLE COMMENT '이슬점온도',
	`col8` TINYINT COMMENT '불쾌지수',
	`col9` DOUBLE COMMENT '일강수',
	`col10` DOUBLE COMMENT '적설',
	`col11` TINYINT COMMENT '습도',
	`col12` VARCHAR(10) COMMENT '풍향',
	`col13` DOUBLE COMMENT '풍속',
	`col14` DOUBLE COMMENT '해면기압',
	`rdate` DATETIME
);





