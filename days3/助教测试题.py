#!/usr/bin/env python
#_*_coding:utf-8_*_

# ���󣺰�ÿ���˵ĶԴ˳ɼ�ȡƽ��ֵ��������м��γɼ������ɼ���ߵ������
# �������������
# ['jim',98,4]
# ['lucy',69,3]
# ['tom',53,7]

# �����ļ�
def test_file():
    my_dict={}
    my_count={}
    with open('test.txt') as f:
        for line in f:
            tmp=line.split(' ')
            my_dict[tmp[0]]=my_dict.setdefault(tmp[0],0)+int(tmp[1])
            my_count[tmp[0]]=my_count.get(tmp[0],0)+1
    return my_dict,my_count       

# ͳ���������
def my_sort(my_dict,my_count):        
    a=sorted(my_dict.items(),key=lambda a:a[1],reverse=True )
    my_sort=[]
    for i in a:   
        a=list(i)
        a.append(my_count[i[0]])
        my_sort.append(a)
    return my_sort

# ���
def a():
    my_dict,my_count=test_file()
    ma=my_sort(my_dict,my_count)
    return ma

# ���Ե���
my_sort=a()
for i in my_sort:
    print i
            
        
                