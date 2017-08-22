#! /usr/bin/env python
# _*_coding:utf-8_*_
import MySQLdb
db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="root123",db="reboot15",port=3306,charset='utf8')
db.autocommit(True)
cur=db.cursor()
#查
sql="select * from user"
#改
sql2="update user set age=101 where username='wd'"
#增
sql3="insert into user values( ' ','cc','123456',0,11,186777,'qqq@qq.com',0)"
#删
sql4="delete from user where username='cc'"
cur.execute(sql2)
cur.execute(sql3)
cur.execute(sql)
b=cur.fetchall()
print b
cur.execute(sql4)
cur.execute(sql)
a=cur.fetchall()
print '_'*10 
print a

