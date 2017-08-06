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
    x=int(raw_input('输入第一数字:').strip())
    z=raw_input('请输入加/减/乘/除:')
    y=int(raw_input('输入第二数字:').strip())
    if z=='加':
        res=jia(x, y)
    elif z=='减':
        res=jian(x, y)
    elif z=='乘':
        res=chen(x, y)
    elif z=='除':
        res=chu(x, y)
    return res

start()
