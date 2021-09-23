'''空调类'''
#
#
# class acdr:
#     __brand = ''
#     __price = 0
#     __time = 0
#
#     def settime(self, time):
#         if time <= 0:
#             print('giao')
#         else:
#             self.__time = time
#
#     def setbrand(self, brand):
#         self.__brand = brand
#
#     def setprice(self, price):
#         if price <= 0:
#             print('不要钱的空调给我也安排一下')
#         else:
#             self.__price = price
#
#     def start(self):
#         print('价值', self.__price, '的', self.__brand, '空调开机了...')
#
#     def stop(self):
#         print('空调将在', self.__time, '分钟后自动关闭')
#
#
# a = acdr()
# a.setbrand(input('空调品牌：'))
# a.setprice(int(input('空调价格：')))
# a.settime(int(input('关机时间：')))
# a.start()
# a.stop()
#
# '''学生类'''
#
#
# class student:
#     __name = None
#     __age = 0
#
#     def setname(self, name):
#         self.__name = name
#
#     def getname(self):
#         return self.__name
#
#     def setage(self, age):
#         if age < 0:
#             print('你还在娘胎呢')
#         else:
#             self.__age = age
#
#     def getage(self):
#         return self.__age
#
#     def toinmsf(self):
#         print('大家好，我叫', self.__name, '今年', self.__age, '岁了！')
#
#     def difvl(self, student):
#         if self.__age > student.getage():
#             return print('我叫', self.__name, '我比同桌', student.getname(), '大', (self.__age - student.getage()), '岁！')
#         elif self.__age < student.__age:
#             return print('我叫', self.__name, '我比同桌', student.getname(), '小', (student.getage() - self.__age), '岁！')
#         else:
#             return print('我和同桌一样大！')
#
#
# s = student()
# s.setname('拉克丝')
# s.setage(18)
#
# s1 = student()
# s1.setname('佐伊')
# s1.setage(618)
#
# s.toinmsf()
# s1.difvl(s)
# s.difvl(s1)
'''
i.定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。
行为：学习（要求参数传入学习的时间）
玩游戏（要求参数传入游戏名）
编程（要求参数传入写代码的行数）
数的求和（要求参数用变长参数来做，返回求和结果）
'''

# class students:
#     def __init__(self, sn, name, age, sex, high, weight, sc, arr, pn):
#         self.sn = sn
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.high = high
#         self.weight = weight
#         self.sc = sc
#         self.arr = arr
#         self.pn = pn
#
#     def learn(self, time):
#         print(self.name, '在家里已经学习了', time, '个小时噢~太棒了', sep='')
#
#     def py(self, row):
#         print('用python打了', row, '行代码针不戳诶~', sep='')
#
#     def play(self, game):
#         print('要劳逸结合噢', self.name, ',来玩会', game, '吧！', sep='')
#
#     def love(self, girl):
#         print('悄悄告诉你一个秘密~', girl, '喜欢你哟!,告诉她你的全部信息吧！', '\n我的学号是', self.sn, ',我叫', self.name, ',今年', self.age,
#               '岁', ',是个帅气的', self.sex, '生,我身高', self.high,
#               ',体重', self.weight, '斤,高考成绩', self.sc, '分,住在', self.arr, ',我的电话号码是', self.pn, sep='')
#
#     def nsum(self, *a):
#         c = sum(a)
#         print(c)
#         return c


# s = students(1910, 'ezreal', 18, '男', 181, 130, 630, '战争学院魔法城1栋9层', 627641)
# s.learn(int(input('今天自律了吗?：')))
# s.py(input('打了多少行代码呢?：'))
# s.play(input('你喜欢玩什么游戏呀'))
# s.love('佐伊')
# s.nsum(500, 20)


'''ii.车类：属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。
功能：跑（要求参数传入车的具体功能，比如越野，赛车）
创建：法拉利，宝马，铃木，五菱，拖拉机对象'''


# class car:
#     def __init__(self, carmds, carnb, carcol, carwt, ftk):
#         self.carmds = carmds
#         self.carnb = carnb
#         self.carcol = carcol
#         self.carwt = carwt
#         self.ftk = ftk
#
#     def run(self, ft):
#         print(f'{self.carcol}的{self.carmds},可以{ft}')


# f = car('法拉利F40', 4, '红色', '1200kg', '600L')
# BMW = car('宝马740', 4, '黑色', '1600kg', '600L')
# Suzuki = car('GSX-R600机车', 2, '蓝色', '300kg', '200L')
# wuling = car('MINIEV', 4, '白色', '400kg', '200L')
# tlj = car('东方红拖拉机', 4, '红色', '4000kg', '1200L')
# f.run('去秋名山来一场刺激的赛车')
# BMW.run('去接待客户')
# Suzuki.run('一脚油门不见尾气')
# wuling.run('接孩子放学')
# tlj.run('拖很多货')

class computer:
    def __init__(self, mds, time, col, wt, cpu, ils, hdsize):
        self.mds = mds
        self.time = time
        self.col = col
        self.wt = wt
        self.cpu = cpu
        self.ils = ils
        self.hdszie = hdsize

    def playgames(self, gamename):
        print(f'{self.col}色{self.mds}的CPU是{self.cpu}，内存有{self.ils}!玩{gamename}可以同时多开5个账户同时搬砖!')

    def work(self):
        print(f'电脑有{self.wt},{self.hdszie}的硬盘，可以存很多工作文件,休息的时候电脑在{self.time}分钟后会自动待机喔~')


c = computer('华硕天选2', 5, '蓝白', '13kg', 'i7_9500', '16G', '1T')
c.playgames('DNF')
c.work()


class monkey:
    def __init__(self, kind, sex, col, wt):
        self.kind = kind
        self.sex = sex
        self.col = col
        self.wt = wt

    def playgames(self, gamename):
        print(f'{self.col}的{self.sex}{self.kind}正在用{gamename}生火!')

    def work(self, *thing):
        print(f'{self.col}的{self.sex}{self.kind}在学习{thing}')


m = monkey('六耳猕猴', '雄性', '金色', '46kg')
m.playgames('打火机')
m.work('python' ' java' ' c++')
