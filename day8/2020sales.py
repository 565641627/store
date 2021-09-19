'''
任务1：
    把2020年的所有数据统计分析并打印出来
'''
import xlrd

# 打开Excel表
wd = xlrd.open_workbook(filename='sales.xlsx', encoding_override=True)
shell = 0  # Excel表的shell角码
n = 1  # 循环次数
s = 0  # 年销售额
yrf = 0
yrfs = 0
nzk = 0
nzks = 0
fy = 0
fys = 0
pc = 0
pcs = 0
tx = 0
txs = 0
mj = 0
mjs = 0
xxz = 0
xxzs = 0
xpy = 0
xpys = 0
cs = 0
css = 0
wy = 0
wys = 0
my = 0
mys = 0
qbk = 0
qbks = 0
xxk = 0
xxks = 0
num = 0  # 年总件数

# lit = []
while n < 13:  # 循环12次
    st = wd.sheet_by_index(shell)  # 操作shell
    col = st.ncols  # 列数
    row = st.nrows  # 行数
    sum = 0  # 月销售额
    shell += 1
    for i in range(1, row):  # 年销售额
        date = st.row_values(i)
        sum = sum + date[2] * date[4]
    n += 1
    s += sum
    for y in range(1, row):  # 年件数循环
        date1 = st.row_values(y)
        num += date1[4]
    for x in range(1, row):  # 遍历服装名称
        name = st.cell_value(x, 1)
        date3 = st.row_values(x)
        # print(name)
        # print(date)
        if name == '羽绒服':
            yrf += date3[4]  # 2020羽绒服的销售数量
            yrfs += date3[2] * date3[4]  # 2020羽绒服的销售总额
        elif name == '牛仔裤':
            nzk += date3[4]
            nzks += date3[2] * date3[4]
        elif name == '风衣':
            fy += date3[4]
            fys += date3[2] * date3[4]
        elif name == '皮草':
            pc += date3[4]
            pcs += date3[2] * date3[4]
        elif name == 'T血':
            tx += date3[4]
            txs += date3[2] * date3[4]
        elif name == '马甲':
            mj += date3[4]
            mjs += date3[2] * date3[4]
        elif name == '小西装':
            xxz += date3[4]
            xxzs += date3[2] * date3[4]
        elif name == '皮衣':
            xpy += date3[4]
            xpys += date3[2] * date3[4]
        elif name == '衬衫':
            cs += date3[4]
            css += date3[2] * date3[4]
        elif name == '卫衣':
            wy += date3[4]
            wys += date3[2] * date3[4]
        elif name == '棉衣':
            my += date3[4]
            mys += date3[2] * date3[4]
        elif name == '铅笔裤':
            qbk += date3[4]
            qbks += date3[2] * date3[4]
        elif name == '休闲裤':
            xxk += date3[4]
            xxks += date3[2] * date3[4]
# lit.extend([yrf, nzk, fy, pc, tx, mj, xxz, xpy, cs, wy, my, qbk, xxk, ])
#每件衣服的年销售数量字典
dict = {'羽绒服': yrf, '牛仔裤': nzk, '风衣': fy, '皮草': pc, 'T血': tx, '马甲': mj, '小西装': xxz, '皮衣': xpy, '衬衫': cs, '卫衣': wy,
        '棉衣': my, '铅笔裤': qbk, '休闲裤': xxk}
#每件衣服的年销售额字典
dict1 = {'羽绒服': yrfs, '牛仔裤': nzks, '风衣': fys, '皮草': pcs, 'T血': txs, '马甲': mjs, '小西装': xxzs, '皮衣': xpys, '衬衫': css,
         '卫衣': wys, '棉衣': mys, '铅笔裤': qbks, '休闲裤': xxks}
print('---------------------年总销售额-------------------------')
print('2020全年销售总额为：', round(s, 2), '￥')
print('---------------------年销售量占比------------------------')
for i in dict.items():
    i[1] / num
    print(i[0], '的年销售数量占总的年销售数量的', format(i[1] / num, '.2%'), sep='')
print('---------------------年销售额占比------------------------')
for i in dict1.items():
    i[1] / s
    print(i[0], '的年销售额占比为：', format(i[1] / s, '.2%'), sep='')
sl = list(dict.values())  # 取出dict的值放到列表
sl_max = max(sl)  # dict值得最大值
sl_min = min(sl)  # dict值得最小值
# 得到dict最大值的键
for i in dict.items():
    if sl_max == i[1]:
        hot = i[0]
# 得到dict最小值的键
for i in dict.items():
    if sl_min == i[1]:
        dh = i[0]
print('---------------------最畅销的衣服------------------------')
print('2020年最畅销的衣服是', hot, '，卖了', sl_max, '件', sep='')
print('---------------------最冷门的衣服------------------------')
print('2020年最冷门的衣服是', dh, '，卖了', sl_min, '件', sep='')
