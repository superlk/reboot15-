#!/usr/bin/env python
#_*_coding:utf-8_*_
# дһ��ע�ắ����һ����½����

# ���ļ�
def read_file():
    user_dict={}
    with open('user.txt') as f:
        for line in f:
            tmp=line.split(':')
            user_dict[tmp[0]]=tmp[1].split()[0]
    return user_dict
        
# д�ļ�
def write_file(user_dict):
    with open('user.txt','w') as f:
        for k,v in user_dict.items():
            data="%s:%s\n"%(k,v)
            f.write(data)
        return 'ע��ɹ�'

# ���������ļ�    
def read_lock_file():
    lock_list=[]
    with open('lock.txt') as f:
        for line in f:
            lock_list.append(line.split('\n')[0])
    return lock_list

# д��������ļ�
def write_lock_file(user):
    with open('lock.txt','a+') as f:
            f.writelines("%s\n"%user)
            return '�˻����������'
# ע��
def register():
    user=raw_input('��������û�����')
    # �û���Ϊ���˳�
    if len(user)==0:
        return '�û�������Ϊ��'
    
    # �ж��û��Ƿ�����˺�����
    lock_list=read_lock_file()
    #print lock_list
    if user in lock_list:
        return  '���û��Ѽ��������'
    
    # �ж��û����Ƿ����
    user_dict=read_file()
    user_list=[]
    pwd_list=[]
    for k,v in user_dict.items():
        user_list.append(k)
        pwd_list.append(v)
    #print pwd_list    
    if user in user_list:
        return '�û��Ѵ���'
    else:
        pwd=raw_input('�������룺')
        # �û�������С��6λ
        if len(pwd)<6:
            return '���벻��С��6λ'
        else:
            # ���û���������д���ļ�
            user_list.append(user)
            pwd_list.append(pwd)
            #print user_list
            new_user_dict={}
            for i in range(len(user_list)):
                new_user_dict[user_list[i]]=pwd_list[i]
            #print new_user_dict
            write_file(new_user_dict)
            return 'ע��ɹ�'


#a=register()
#print a            
            
# ��¼
def login():
    user=raw_input('��������û�����')
    
    # �û���Ϊ���˳�
    if len(user)==0:
        return '�û�������Ϊ��'
    
    # �ж��û��Ƿ��ں�����
    lock_list=read_lock_file()
    #print lock_list
    if user in lock_list:
        return  '���û��Ѽ��������'
    
    #�ж��û����Ƿ���ڣ������������룬�������˳�
    user_dict=read_file()
    user_list=[]
    pwd_list=[]
    for k,v in user_dict.items():
        user_list.append(k)
        pwd_list.append(v)
    #print pwd_list    
    if user not in user_list:
        return '�û�������'
    else:
        count=0
        while True:
            count+=1
            pwd=raw_input('��������:')
            
            # ������������������������������û��ļ�ͬʱɾ����Ӧ�û���������
            if count>=3:
                write_lock_file(user)
                user_dict.pop(user)
                write_file(user_dict)
                return '���������'
            
            # �������볤�Ȳ���С��6λ
            if len(pwd)<6:
                print '���볤�Ȳ���С��6λ'
                continue 
            
            # �ж������Ƿ���ȷ
            if pwd==pwd_list[user_list.index(user)]:
                return '��¼�ɹ�'    
            else:
                print '�������'
                continue
    
# ��¼����
#a=login()
#print a




