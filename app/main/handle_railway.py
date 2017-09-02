# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import pymysql

def getStuInfoByIdNumber(idNumber):
    connection = pymysql.connect(host='106.14.98.77',
                                 port=3306,
                                 user='test',
                                 password='123456',
                                 db='GongKe2017',
                                 charset='utf8')
    cursor = connection.cursor()
    cursor.execute('select stuid, name, station from 2017gk where cerid = %s', idNumber)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result is None:
        return None
    return list(result)

def getStations():
    connection = pymysql.connect(host='106.14.98.77',
                                 port=3306,
                                 user='test',
                                 password='123456',
                                 db='GongKe2017',
                                 charset='utf8')

    cursor = connection.cursor()
    cursor.execute('select station_name from stations')
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    alist = []
    for i in result:
        alist.append(i[0])
    return alist

def save_info(station_name, stuid):
    connection = pymysql.connect(host='106.14.98.77',
                                 port=3306,
                                 user='test',
                                 password='123456',
                                 db='GongKe2017',
                                 charset='utf8')


    cursor = connection.cursor()
    sql = 'update 2017gk SET station = "%s" where stuid = %d' % (station_name, stuid)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()


def get_not_fill():
    connection = pymysql.connect(host='106.14.98.77',
                                 port=3306,
                                 user='test',
                                 password='123456',
                                 db='GongKe2017',
                                 charset='utf8')

    cursor = connection.cursor()
    cursor.execute('select stuid, name from 2017gk where station = ""')
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    alist = []
    for i in result:
        alist.append({'stuid':i[0], 'name':i[1]})
    return alist
