import pymysql
import xlwt


def sql_to_excel(host, user, password, database, table, wb):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    sql = 'select * from ' + table
    cursor.execute(sql)
    date = cursor.fetchall()
    cc = cursor.description
    con.commit()
    cursor.close()
    con.close()
    book = xlwt.Workbook()
    new_sheet = book.add_sheet(table)
    for i in range(len(cc)):
        new_sheet.write(0, i, cc[i][0])
    x = 1
    y = 0
    n = -1
    for x in range(x, len(date)):
        n += 1
        for y in range(len(date[0])):
            new_sheet.write(x, y, date[n][y])
    book.save(wb)


sql_to_excel('localhost', 'root', '', 'company', 't_dept', 'f:/部门表.xlsx')
sql_to_excel('localhost', 'root', '', 'company', 't_employees', 'f:/员工表.xlsx')
#
# sql = 'select * from t_dept'
# date = select(sql, [])
# print(date)
# book = xlwt.Workbook()
# new_sheet = book.add_sheet('新学期')
# new_sheet.write(0,0,'新学生')
# book.save('f:/test.xlsx')
