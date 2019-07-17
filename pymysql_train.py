# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pymysql
import getpass





print("输入数据库密码：")
passwd=getpass.getpass("password:")  #这种方法好像是通过脚本运行，密码才隐藏。直接在控制台输入密码，还是会看得到

conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd=passwd,db='db_demo1',charset='utf8')
               #127.0.0.1也可以写为   localhost
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)  #默认从mysql读取的数据是元祖形式，这样设置的话，返回就是字典形式
cursor.execute("select * from test_evt")
print('ok')

row_1=cursor.fetchone()  #获取db_demo1数据库中的 test_evt表的第一行数据
print(row_1)
cursor.scroll(-1,mode='relative')  #表示相对当前位置往回移动一位。如果mode='absolute'则是直接指定游标到哪个位置
row_1_back=cursor.fetchone()
print(row_1_back)
row_2=cursor.fetchone()    #获取db_demo1数据库中的 test_evt表的第二行数据
print(row_2)


#row_remain=cursor.fetchall()   #获取db_demo1数据库中的 test_evt表的除了第一第二行，剩下的数据



#print(row_remain)
conn.commit()    #提交，不然无法保存新建或者修改的数据
cursor.close()    #关闭游标
conn.close()  #关闭连接
