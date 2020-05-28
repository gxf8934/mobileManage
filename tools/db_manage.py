import psycopg2
from psycopg2.extras import DictCursor
import psycopg2.extras
from datetime import datetime


def db_time():
    localtime = datetime.now()
    return localtime


def db_connect():
    conn = psycopg2.connect(database='mobilemanage-test', host='10.8.8.123', user='postgres', password='1to6pg10',
                            port=5432)
    return conn


# 新增数据sql
def db_insert(table, **dict):
    sql = '''INSERT INTO {} (*) VALUES (*) '''
    time = db_time()
    dict.update({'"createdAt"': time})
    dict.update({'"updatedAt"': time})
    for (k, v) in dict.items():
        a = sql.split('*')
        a.insert(1, k)
        a.insert(2, ',*')
        a.insert(4, '\'' + str(v) + '\'')
        a.insert(5, ',*')
        str_tmp = ''
        for i in a:
            str_tmp += str(i)
        sql = str_tmp
        print(sql)
    sql = sql.format(table).replace(',*', '')
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(sql)
    rowcount = cur.rowcount
    print('新增受影响行数：', rowcount)
    conn.commit()
    conn.close()


# 删除数据sql
def db_delete(table, **dict):
    # sql = '''delete from {} where id={}'''
    sql = '''update {} set {} where id={}'''
    state = "{}={}".format('state', 0)
    for value in dict.values():
        print(value)
        sql = sql.format(table, state, value)
        print(sql)
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


# 编辑数据sql
def db_update(table, condition, **dict):
    time = db_time()
    dict.update({'"updatedAt"': time})
    sql = '''update {} set {} where id={}'''
    # 新建更新列表
    kvlist = []
    for k in dict:
        kvlist.append("{}={}".format(k, '\'' + str(dict[k]) + '\''))
    # 更新列表转化为字符串
    kvlist = ','.join(kvlist)
    sql = sql.format(table, kvlist, condition)
    # 连接数据库
    conn = db_connect()
    # 创建游标
    cur = conn.cursor()
    # 执行sql
    cur.execute(sql)
    # 受影响行数
    rowcount = cur.rowcount
    print('编辑受影响行数：', rowcount)
    # 提交
    conn.commit()
    # 关闭
    conn.close()



# 查询数据sql
def db_select(table, **dict):

    if (dict['state']!=None):
        sql = '''select * from {} where {}={} and {}={} '''
        sql = sql.format(table, 'state', dict['state'],'mobile_label',dict['mobile_label'])
    else:
        sql = '''select * from {} where {}={}  '''
        sql = sql.format(table, 'id', dict['id'])
    conn = db_connect()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    print(sql)
    cur.execute(sql)
    result = cur.fetchall()
    return result


class DB_Connect():
    def __init__(self):
        self.conn = psycopg2.connect(database='mobilemanage-test', host='10.8.8.123', user='postgres',
                                     password='1to6pg10',
                                     port=5432)

    def getDB(self):
        return self.conn


if __name__ == '__main__':
    # db_insert('mobile_manage', mobile_model='xiaomni', mobile_color=78, mobile_name='xiafei',owner='xiafei')
    # db_delete('mobile_manage',id=13)
    db_select('mobile_manage')
    # db_update('mobile_manage',13,mobile_model='bianji', mobile_color='red', mobile_name='vivo',owner='xiafeigao')
    # db_time()
