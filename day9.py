'''水杯对象'''

# class cup:
#     __h = 0
#     __v = 0
#     c = ''
#     m = ''
#
#     def seth(self, h):
#         if h <= 0:
#             print('输入非法')
#         else:
#             self.__h = h
#
#     def setv(self, v):
#         if v <= 0:
#             print('输入非法')
#         else:
#             self.__v = v
#
#     def dep(self):
#         print('一个', self.c, '的', self.m, '水杯杯有', self.__h, 'cm高，可以装', self.__v, 'ml的水', sep='')
#
#
# c = cup()
# c.seth(int(input('杯子多高')))
# c.setv(int(input('多能装？（ml）')))
# c.c = (input('杯子的颜色：'))
# c.m = (input('啥子材质：'))
# c.dep()

'''笔记本对象'''


class computar:
    __scrsize = 14.5
    __price = 0
    cpu = ('i5_5300', 'i5_10500', 'i7_5300', 'i7_9300', 'i9_10500')
    __icpu = ''
    it = (4, 6, 8, 16)

    __its = 0
    __time = 0

    def seticpu(self, icpu):
        if icpu <= 0 or icpu > 4:
            print('我不明白你要什么?')
        else:
            self.__icpu = icpu

    def giticpu(self):
        return self.__icpu

    def setsccrsize(self, scrsize):
        if scrsize < 14 or scrsize > 30:
            print('没有这型号的屏幕诶')
        else:
            self.__scrsize = scrsize

    def setprice(self, price):
        if price <= 0:
            print('不要钱的电脑给我也安排一台')
        else:
            self.__price = price
    def gitprice(self):
        return self.__price

    def setits(self, its):
        if its not in c.it:
            print('咱这没有你这么大的内存啊？')
        else:
            self.__its = its

    def gittits(self):
        return self.__its

    def settime(self, time):
        # if time <= 0:
        #     print('电脑正在运行')
        # else:
        self.__time = time

    def python(self):
        print('学完python后电脑已经待机了', self.__time,sep='')

    def game(self, its):
        if c.cpu[g] == c.cpu[4] and its == 16:
            print('您这台电脑的配置价值',c.gitprice(),'元！恭喜你可以体验赛博朋克2077！')
        elif c.cpu[g] in c.cpu[1:4] and its in c.it[1:4]:
            print('您这台电脑的配置价值',c.gitprice(),'元！你可以喊上你的小伙伴一起开黑打LOL')
        elif c.cpu[g] == c.cpu[0] and its in c.it[0:2]:
            print('您这台电脑的配置价值',c.gitprice(),'元！开始外比巴卜吧！')
        else:
            print('啥玩意?没有！')

    def video(self, its):
        if c.cpu[g] in c.cpu[4] and its == 16:
            print('它内存非常强大，可以同时运行50个程序！')
        elif c.cpu[g] in c.cpu[1:4] and its in c.it[1:4]:
            print('它可以同时运行多开五个账号搬砖')
        elif c.cpu[g] in c.cpu[0] and its in c.it[0:2]:
            print('它同时打开多个程序会卡顿噢~尽快升级内存把！')
        else:
            print('啥玩意?咱没有！')


c = computar()
c.setsccrsize(float(input('屏幕尺寸(14-30寸):')))
# c.setprice(int(input('电脑价格￥:')))
for k, v in enumerate(c.cpu):
    print(k, v)
g = input('CPU型号：')
m = 0
if g.isdigit():
    g = int(g)
    if g == 0:
        m += 5000
    elif g == 1:
        m += 5500
    elif g == 2:
        m += 6000
    elif g == 3:
        m += 6500
    elif g == 4:
        m += 7000
c.setprice(m)
c.seticpu(g)
print(c.it)
c.setits(int(input('内存大小:')))
c.settime('2个小时噢~')
c.python()
c.game(c.gittits())
c.video(c.gittits())
