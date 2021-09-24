# class human:
#     age = 0
#     sex = ''
#     name = ''
#
#
# class worker(human):
#     def work(self, job):
#         print(f'今年{self.age}岁的{self.name}正在{job}')
#
#
# class student(human):
#     studentnumber = 0
#
#     def learn(self, sub):
#         print(f'今年{self.age}岁的{self.name}正在学习{sub}')
#
#     def sing(self, music):
#         print(f'{self.name}是个{self.sex}孩,喜欢唱{music}')
#
#
# w = worker()
# w.name='麦迪'
# w.age=22
# w.sex='男'
# w.work('搬砖')
# s=student()
#
# s.name='佐伊'
# s.age=108
# s.sex='女'
# s.learn('虫洞的运用')
# s.sing('周杰伦的歌')

# class cooker:
#     __name = ''
#     __age = 0
#
#     def setname(self, name):
#         self.__name = name
#
#     def getname(self):
#         return self.__name
#
#     def setage(self, age):
#         self.__age = age
#
#     def getage(self):
#         return self.__age
#
#     def sr(self):
#         None
#
#
# class chef(cooker):
#     def sf(self):
#         None
#
#
# class sschef(chef):
#     def zf(self):
#         super().sr()
#         print('蒸饭')
#
#     def cc(self):
#         super().sf()
#         print('炒菜')
#
#
# s = sschef()
# s.setname('海绵宝宝')
# s.setage(18)
# print(s.getname(), s.getage(), '岁')
# s.zf()
# s.cc()
import time


class Oldphone:
    __brand = ''
    def setbrand(self,brand):
        self.__brand=brand
    def getbrand(self):
        return self.__brand
    def call(self, number):
        print(f'正在给打{number}电话')
        for i in range(6):
            print('.', end='')
            time.sleep(1)
        print('已接通')
class newphone(Oldphone):
    def dial(self,number):
        print('语音拨号中...')
        super().call(number)
    def sow(self):
        print(f'品牌为{self.getbrand()}的手机很好用')


n=newphone()
n.setbrand('vivo')
n.dial(input('请输入要拨打的电话号码'))
n.sow()
