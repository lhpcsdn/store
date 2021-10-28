-- 创建一个银行数据库
CREATE DATABASE bank CHARACTER SET utf8;
-- 创建表
CREATE TABLE `information`(
		account INT(10) PRIMARY KEY,  
		username CHAR(15),
		PASSWORD INT(15) NOT NULL,
		country CHAR(20),
		province CHAR(20),
		street	 CHAR(20),
		door     CHAR(20),
		money    INT(20),
		registerDate DATETIME,
		bankname  CHAR(20)	
);

