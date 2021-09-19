import xlrd
from function import update
wd = xlrd.open_workbook(filename='sales.xlsx', encoding_override=True)
sql = 'insert into cs%s values(%s,%s,%s,%s,%s)'
param = []

n=0
for i in range(12):
    st = wd.sheet_by_index(i)
    row = st.nrows
    n+=1
    for y in range(1, row):
        date = st.row_values(y)
        # print(n)
        param = [n,date[0], date[1], date[2], date[3], date[4]]
        update(sql, param)
