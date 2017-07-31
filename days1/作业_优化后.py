
#!/usr/bin/env python
#_*_coding:utf-8_*_
# 作业：实现用户名密码登陆验证
# 1：判断用户名密码是否正确，正确则打印欢迎信息，错误则输出具体错误原因信息
# 2：用户可以连续输入三次密码。超过三次则锁定用户
# 3：密码位数必须超过6位
# @name：用户名
# @password：用户密码
# 用户名错误，一致循环
while True: 
    # 用户输入用户名
    name=raw_input('\033[32m请输入用户名:\033[0m')
    # 判断如何用户名是否正确 
    if name=='lk':
         # 只能输入3次 
        for i in range(3):
            # 打印还有几次机会
            print '\033[31m你还有%s次机会输入密码\033[0m'%(3-i)
            # 输入密码
            password=raw_input('\033[32m请输入密码:\033[0m')
            # 判断密码是否大于等于6位
            if len(password)<6:
                print '\033[31m请输入6位以上密码\033[0m'
                continue
            # 判断密码是否正确
            if password=='123456':
                print '\033[5;32m登录成功\033[0m '
                print '\033[5;32m欢迎%s\033[0m'%name
                break
            # 错误3次锁定用户
            elif i==2:
                print '\033[5;30;45m密码已锁定，请联系管理员\033[0m'
                break
            # 密码错误，提示错误
            else:
                print '\033[31m密码错误\033[0m'
        break 
    #  用户名输入exit，整个程序退出              
    elif name=='exit':
        print '\033[32m欢迎下次登录\033[0m'
        break
    # 用户名不正确，提示错误
    else:
        print '\033[31m对不起，%s不存在,请重新输入\033[0m'%name
        print '\033[1;30;41m输入exit退出程序\033[0m'