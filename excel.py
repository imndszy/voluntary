# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from openpyxl import Workbook
from openpyxl.compat import range
import pymysql
import time

while True:
    try:
        conn = pymysql.connect(host='localhost',port=3306,user='szy',passwd='123456',db='voluntary',charset='utf8')
        cur = conn.cursor()
        cur.execute("select `stuid`,`service_time`,`service_time_a`,`service_time_b` from users")
        result = cur.fetchall()

        cur.close()
        conn.close()
    except:
        print 'access database wrong'
        time.sleep(30)
        continue

    result = [list(x) for x in result]

    wb = Workbook()
    dest_filename = '/home/ubuntu/www/voluntary/info.xlsx'
    ws1 = wb.active
    ws1.title = "data"
    info=[u'学号',u'总志愿时长',u'A类志愿服务时长',u'B类志愿服务时长']
    i = 0
    ws1.append(info)
    for row in range(2,len(result)+2):
        ws1.append(result[i])
        i += 1

    wb.save(filename=dest_filename)
    time.sleep(30)
