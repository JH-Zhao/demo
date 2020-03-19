import time
import pymysql

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")


def get_conn():
    """
    :return 连接、游标
    """
    #创建连接
    conn = pymysql.connect(host="120.55.57.80",
                           user="pxb",
                           password="pxb",
                           database="yiqing_fenxi",
                           charset="utf8")
    #创建游标
    cursor = conn.cursor(pymysql.cursors.DictCursor)  #执行完毕后返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn,cursor):
        cursor.close()
        conn.close()

def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return:返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql,args)
    res=cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_cl_data():
    """
    return大屏div id=c1部分的数据
    """
    #因为会更新多次数据，取时间戳最新的那一组
    sql="SELECT confirm,suspect,heal,dead FROM yiqing_fenxi.history WHERE ds =(select ds from yiqing_fenxi.history order by ds desc limit 1)"
    res = query(sql)
    return res[0] #第-条记录

data = get_cl_data()


if __name__=="__main__":
    pass