#!/usr/bin/env python
#_*_coding:utf-8_*_
# �������ݿ�
import MySQLdb
db=MySQLdb.connect(host="127.0.0.1",user="root",passwd='root123',db="reboot15",port=3306,charset='utf8')  
db.autocommit(True)
cur=db.cursor()


# ��ѯ���ݿ���Ϣ
def select_db():
    sql="select * from user"
    cur.execute(sql)
    user_tup=cur.fetchall()
    return user_tup


# ��������
def inster_db(username,passwd,sex,age,phone,email,role):
    sql="insert into user(username,password,sex,age,phone,email,role) values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,(username,passwd,sex,age,phone,email,role))
    return 0

# ɾ������
def delete_db(id):
    sql="delete from user where id=%s"%id
    cur.execute(sql)
    return 0


# ������
def update_db(*args):
     my_tup=args[0]
     print my_tup

     sql="update user set password='%s',sex=%d,age=%d,phone=%d,email='%s',role=%d where id=%d"%(my_tup[0],my_tup[1],my_tup[2],my_tup[3],my_tup[4],my_tup[5],my_tup[6])
     print sql
       # conditions = ["%s='%s'"%(k,my_dict[k]) for k my_dict.key
            #print conditions
            #sql = "update user SET %s where id =%d " % (','.join(conditions),args)
     cur.execute(sql)
     return 0

# ע��
def register(user,pwd):
    
    # �ж��û����Ƿ����
    user_list=[]
    user_tup=select_db()
    for i in user_tup:
        user_list.append(i[0])
    # �ж��û����Ƿ����  
    if user in user_list:
        return 1
    else:
        if len(pwd)<6:
           return 2
        else:
           return 0 
            
# ��¼
def login(user,pwd):
    user_list=[]
    pwd_list=[]
    role_list=[]
    user_tup=select_db()
    for i in user_tup:
        user_list.append(i[1])
        pwd_list.append(i[2])
        role_list.append(i[7])
    #print user_list
    #print pwd_list 
    # �ж��û����Ƿ���ں�����  
    if user not in user_list or pwd != pwd_list[user_list.index(user)]:
        return '1'
    if user in user_list and pwd==pwd_list[user_list.index(user)]:
        # �ж��Ƿ��ǹ���Ա��
        if role_list[user_list.index(user)]==1:
            return '0'
        else:
            return '2'
    
#a=login("lk","123456")
#print a
#a=update_db(("xxxxx",1,88,186000,"qqcom",0,5))
#print a

#x=select_db()
#print x

#p=delete_db(3)
#print p

#p=inster_db('admin','admin',0,22,1590111,'6510020@qq.com',1)
#print p

#sql="insert into user(username,password,sex,age,phone,email,role)  values('admin','admin',0,22,1590111,'6510020@qq.com',1)"
#cur.execute(sql)
