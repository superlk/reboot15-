#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
import utils
import json
import  util
from . import app

###### 工单系统 ##############

#————————————————————机房——————————————————————
table="job"
field=['id','app_name','handle_name','start','end','app_msg','handle_msg','type','status']

# 机房管理列表
@app.route("/jobadd/")
def jobadd():
    if not session:
        return redirect("/")
    if request.method=='POST':
        user={k:v[0] for k,v in dict(request.form).items()}
        field=['app_name','app_msg','type','status']
        if user['app_name']:
            data=utils.insert(table,field,user)
            return json.dumps(data)
        else:
           data={'code':1,'errmsg':'username or password is not null'}
           return json.dumps(data)
    return render_template("job_add.html",res=session)
    




'''
# 机房编辑
@app.route('/idc_info/')
def idc_info():
     if not session:
         return redirect('/')
     uid=request.args.get('id')
     data={'id':uid}
     result=utils.get_one(idc_table,idc_field,data)
     if result['code']==0:
        result=result['msg']
     return json.dumps(result)

# 机房信息更新
@app.route('/idc_update/',methods=['GET','POST'])
def idc_update():
    if not session:
       return redirect('/')
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       data=utils.update(idc_table,idc_field,user_dict)
       return  json.dumps(data)

# 编辑机房,(有个bug，机房名不重复没有判断)
@app.route('/idc_add/',methods=['GET','POST'])
def idc_add():
    if not session:
        return redirect('/')
    if request.method=='POST':
        user={k:v[0] for k,v in dict(request.form).items()}
        idc_field=['idc_name','cn_name','address','name','phone']
        if user['idc_name']:
            data=utils.insert(idc_table,idc_field,user)
            return json.dumps(data)
        else:
           data={'code':1,'errmsg':'username or password is not null'}
           return json.dumps(data)
    
    return render_template("idc_update.html",res=session)

# 删除机房   
@app.route('/idc_delete/',methods=['GET','POST'])
def idc_delete():
    if not session:
       return redirect('/')
    uid=request.args.get('id')
    data=utils.delete(idc_table,uid)
    return json.dumps(data)

#————————————————机柜——————————————————————————
cab_table="cabinet"
cab_field=['id','name','idc_id','u_num','power']

# 机柜列表
@app.route('/cabinet/')
def cabinet():
   if not session:
      return redirect('/')
   data=utils.list(cab_table,cab_field)
   print data
   result=data['msg']
   print "____________________",result
   return render_template("cabinet.html",res=session,result=result)

# 添加机柜,
@app.route('/cabinet_add/',methods=['GET','POST'])
def cabinet_add():
    if not session:
        return redirect('/')
    if request.method=='POST':
        user={k:v[0] for k,v in dict(request.form).items()}
        print 'user........',user
        cab_field=['name','idc_id','u_num','power']
        if user['name']:
            data=utils.insert(cab_table,cab_field,user)
            return json.dumps(data)
        else:
           data={'code':1,'errmsg':'username or password is not null'}
           return json.dumps(data)

# 添加机柜式选机房接口
@app.route('/idcdata/')
def idcdata():
    result=utils.list(idc_table,idc_field)
    res=result['msg']
    print 'idc-----------',res
    return json.dumps(res)

# 机柜编辑
@app.route('/cabinet_info/')
def cabinet_info():
     if not session:
         return redirect('/')
     uid=request.args.get('id')
     data={'id':uid}
     result=utils.get_one(cab_table,cab_field,data)
     idc=utils.list(idc_table,idc_field)
     idc_list=idc['msg']
     if result['code']==0:
        result=result['msg']
     return render_template("cabinet_update.html",res=session,result=result,idc=idc_list)

# 机柜信息更新
@app.route('/cabinet_update/',methods=['GET','POST'])
def cabinet_update():
    if not session:
       return redirect('/')
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       data=utils.update(cab_table,cab_field,user_dict)
       return  json.dumps(data)
    #return render_template("cabinet_update.html",res=session,result=data)
        

# 删除机房   
@app.route('/cabinet_delete/',methods=['GET','POST'])
def cabinet_delete():
    if not session:
       return redirect('/')
    uid=request.args.get('id')
    data=utils.delete(cab_table,uid)
    return json.dumps(data)

#--------------------------server---------------------------
server_table="server"
server_field=['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']

# 机柜列表
@app.route('/server/')
def server():
   if not session:
      return redirect('/')
   data=utils.list(server_table,server_field)
   result=data['msg']
   return render_template("server.html",res=session,result=result)

# 添加机柜,
@app.route('/server_add/',methods=['GET','POST'])
def server_add():
    if not session:
        return redirect('/')
    if request.method=='POST':
        user={k:v[0] for k,v in dict(request.form).items()}
        print 'user........',user
        server_field=['hostname','lan_ip','wan_ip','cabinet_id','op','phone']
        if user['hostname']:
            data=utils.insert(server_table,server_field,user)
            return json.dumps(data)
        else:
           data={'code':1,'errmsg':'username or password is not null'}
           return json.dumps(data)

# 添加服务器选机柜接口
@app.route('/serverdata/')
def serverdata():
    result=utils.list(cab_table,cab_field)
    res=result['msg']
    return json.dumps(res)

# 服务器编辑
@app.route('/server_info/')
def server_info():
     if not session:
         return redirect('/')
     uid=request.args.get('id')
     data={'id':uid}
     result=utils.get_one(server_table,server_field,data)
     server=utils.list(cab_table,cab_field)
     server_list=server['msg']
     if result['code']==0:
        result=result['msg']
     return render_template("server_update.html",res=session,result=result,server=server_list)

# 服务器信息更新
@app.route('/server_update/',methods=['GET','POST'])
def server_update():
    if not session:
       return redirect('/')
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       data=utils.update(server_table,server_field,user_dict)
       return  json.dumps(data)

# 删除服务器   
@app.route('/server_delete/',methods=['GET','POST'])
def server_delete():
    if not session:
       return redirect('/')
    uid=request.args.get('id')
    data=utils.delete(server_table,uid)
    return json.dumps(data)
'''
