#!/usr/bin/env python
#_*_coding:utf-8_*_
# �����ļ�

def open_file():
    with open('user.txt') as f:
        tem=f.readlines()
        for i in tem:
            my_list=i.split(':')
    return my_list

#д
def write_file(user_list):
    with open('user.txt','w') as f
    for i in user_list:
        f.write(''.join(i))
    return 'ok'
        

# ��
def update_file(user,pwd):
    arr=user+':'+pwd
    with open('user.txt','a+') as f:
        f.write('arr')
    

# ��
def gai_file(user,pwd):
   user_list=open_file()
   for i in user_list:
       if user == i[0]:
           user_list[i][1]=pwd
    write_file(user_list)
           
# ɾ��
def delete_file(user):
    user_list=open_file()
    for i in user_list:
       if user == i[0]:
           user_list��remove(i)
    write_file(user_list)
    
            
# ��
def select(user,pwd):
    user_list=open_file()
    if user=='admin':
        for i in user_list:
            return '%s:%s'%(i[0],i[1])
    for i in user_list:
        if user==i[0]:
            return '%s:%s'%(user,i[1])
        
         
    
        