#!/usr/bin/env python
#_*_coding:utf-8_*_
def jia(x,y):
    return x+y

def jian(x,y):
    return x-y

def chen(x,y):
    return x*y

def chu(x,y):
    return x/y

def start():
    x=int(raw_input('�����һ����:').strip())
    z=raw_input('�������/��/��/��:')
    y=int(raw_input('����ڶ�����:').strip())
    if z=='��':
        res=jia(x, y)
    elif z=='��':
        res=jian(x, y)
    elif z=='��':
        res=chen(x, y)
    elif z=='��':
        res=chu(x, y)
    return res

start()
