top10的ip，和对应出现的次数


#!/usr/bin/env python
#_*_coding:utf-8_*_
# date 2017。8.1
# mail:651002081@qq.com
# 作业要求：取日志文件前10的ip
my_list=[]
my_dict={}
my_list_sort=[]
# 打开文件
with open('access.txt') as f:
    # 遍历文件每一行
    for line in f:
        # 定义一个临时列表，元素以空格隔开
        tem=line.split(' ')
        # 把列表里第0个元素放到列表里
        tup=tem[0]
        # 把列表里的元素当key访问字典，出现次数为value
        my_dict[tup]=my_dict.get(tup,0)+1

# 把字典转为为列表        
my_list_sort=my_dict.items()
# 冒泡排序
for i in range(len(my_list_sort)-1):
    for j in range(len(my_list_sort)-1-i):
        if my_list_sort[j][1]>my_list_sort[j+1][1]:
            my_list_sort[j],my_list_sort[j+1]=my_list_sort[j+1],my_list_sort[j]
# 打印前10
for i in range(10):
    tmm=my_list_sort.pop()
    print '%s:%s'%(tmm[0],tmm[1])
