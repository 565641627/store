from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from ICBC import bank_addUser
from ICBC import bank_saveMoney
from ICBC import bank_selectUser
from ICBC import bank_takeMoney
from ICBC import bank_transformMoney
import xlrd
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
wd = xlrd.open_workbook(filename='TestICBC.xlsx', encoding_override=True)
st = wd.sheet_by_index(0)
st1 = wd.sheet_by_index(1)
st2 = wd.sheet_by_index(2)
st3 = wd.sheet_by_index(3)
st4 = wd.sheet_by_index(4)
row = st.nrows
row1 = st1.nrows
row2 = st2.nrows
row3 = st3.nrows
row4 = st4.nrows

for i in range(row):
    data1 = st.row_values(i)
    list1.append(data1)
for i in range(row1):
    data2 = st1.row_values(i)
    list2.append(data2)
for i in range(row2):
    data3 = st2.row_values(i)
    list3.append(data3)
for i in range(row3):
    data4 = st3.row_values(i)
    list4.append(data4)
for i in range(row4):
    data5 = st4.row_values(i)
    list5.append(data5)
da=list1
da2=list2
da3=list3
da4=list4
da5=list5
'''开户功能测试'''


@ddt
class TestICBC(TestCase):

    @data(*da)
    @unpack
    def testAddUser(self, a, b, c, d, e, f, g, h):
        s = bank_addUser(a, b, c, d, e, f, g)
        self.assertEqual(s, h)


'''存钱功能测试'''


@ddt
class TestICBC1(TestCase):

    @data(*da2)
    @unpack
    def testAddUser1(self, a, b, c):
        s = bank_saveMoney(a, b)
        self.assertEqual(s, c)


'''查询功能测试'''


@ddt
class TestICBC2(TestCase):

    @data(*da3)
    @unpack
    def testAddUser2(self, a, b, c):
        s = bank_selectUser(a, b)
        self.assertEqual(s, c)


'''取钱功能测试'''


@ddt
class TestICBC3(TestCase):

    @data(*da4)
    @unpack
    def testAddUser3(self, a, b, c, d):
        s = bank_takeMoney(a, b, c)
        self.assertEqual(s, d)


'''转账功能测试'''


@ddt
class TestICBC4(TestCase):

    @data(*da5)
    @unpack
    def testAddUser4(self, a, b, c, d, e):
        s = bank_transformMoney(a, b, c, d)
        self.assertEqual(s, e)
