'''
    1.数据类：
        只准备数据部分：不参与任何操作。
    任务1：
        将这个框架的数据源集中写到excel表里，使用xlrd读取
        xlrd参数化，mysql的参数化。
'''

'''
#xlrd参数化

import xlrd
wk=xlrd.open_workbook(filename='HKR.xlsx',encoding_override=True)
st=wk.sheet_by_index(0)
st1=wk.sheet_by_index(1)
row=st.nrows
row1=st1.nrows
list1=[]
list=[]
for i in range(1,row):
    row=st.row_values(i)
    if isinstance(row[1],float):
        row[1]=int(row[1])
    dict={'username':row[0],'password':row[1],'expect':row[2]}
    list.append(dict)

for y in range(1,row1):
    row1=st1.row_values(y)
    if isinstance(row1[1],float):
        row1[1]=int(row1[1])
    dict1={'username':row1[0],'password':row1[1],'expect':row1[2]}
    list1.append(dict1)
'''
import pymysql
list=[]
list1=[]
con = pymysql.connect(host="localhost", user="root", password="root", database="hkrtest",charset='utf8')
cursor = con.cursor()
sql = "select * from test_data"
cursor.execute(sql)
date = cursor.fetchall()
for i in range(len(date)):
    dict = {'username': date[i][0], 'password': date[i][1], 'expect': date[i][2]}
    list.append(dict)

sql1 = "select * from error"
cursor.execute(sql1)
date1 = cursor.fetchall()
for i in range(len(date1)):
    dict1 = {'username': date1[i][0], 'password': date1[i][1], 'expect': date1[i][2]}
    list1.append(dict1)

con.commit()
cursor.close()
con.close()
class  InitPage:

    login_success_data =list

    login_error_data =list1

















