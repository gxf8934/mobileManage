from flask import Flask, jsonify, render_template, request
from tools.db_manage import db_connect,db_insert,db_update,db_delete,db_select
from tools.time_conversion import date_to_timestamp,timestamp_to_date

app = Flask(__name__)


@app.route('/')
def tem():
    return render_template('tem.html')
@app.route('/add_mobile')
def add_tem():
    return  render_template('add_tem.html')
@app.route('/update_mobile')
def update_tem():
    return  render_template('update_mobile.html')

# 查询数据
@app.route('/select',methods=['post'])
def select_mobile():
    print('1111')
    mobile={
        'id':'',
        'state':'',
        'mobile_label':''
    }
    mobile.update({'id':request.form.get('id')})
    mobile.update({'state':request.form.get('state')})
    mobile.update({'mobile_label':request.form .get('mobile_label')})
    print('2222')
    rows=db_select('mobile_manage',**mobile)
    print(rows)
    for i in rows:
        # print(i.get('createdAt'))
        i.update({'createdAt':str(i.get('createdAt'))[:-7],'updatedAt':str(i.get('updatedAt'))[:-7]})
        print(i)
    print(rows)
    return jsonify({'code':0,'result':rows})

#新增数据
@app.route('/add',methods=['post'])
def addMobile():
    mobile={
        'mobile_model':'',
        'mobile_name':'',
        'mobile_color':'',
        'mobile_price':'',
        'owner':'',
        'state':'',
        'mobile_label':''
    }
    mobile.update({'mobile_model':request.form.get('model')})
    mobile.update({'mobile_name':request.form.get('name')})
    mobile.update({'mobile_color':request.form.get('color')})
    mobile.update({'mobile_price':request.form.get('price')})
    mobile.update({'owner':request.form.get('owner')})
    mobile.update({'mobile_label':request.form.get('label')})
    mobile.update({'state':1})
    db_insert('mobile_manage',**mobile)
    return '添加成功'


#删除数据
@app.route('/delete',methods=['post'])
def deleteMobile():
    mobile={
        'id':''
    }
    mobile.update({'id':request.form.get('id')})
    db_delete('mobile_manage',**mobile)
    return '成功'

#编辑数据
@app.route('/update',methods=['post'])
def updateMobile():
    id=request.form.get('id')
    print(id)
    mobile={
        'mobile_model':'',
        'mobile_name':'',
        'mobile_color':'',
        'mobile_price':'',
        'owner':'',
        'mobile_label':''
    }
    mobile.update({'mobile_model':request.form.get('model')})
    mobile.update({'mobile_name':request.form.get('name')})
    mobile.update({'mobile_color':request.form.get('color')})
    mobile.update({'mobile_price':request.form.get('price')})
    mobile.update({'owner':request.form.get('owner')})
    mobile.update({'mobile_label':request.form.get('label')})
    db_update('mobile_manage',id,**mobile)
    return '成功'




if __name__ == '__main__':
    app.run()
