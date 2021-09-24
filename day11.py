from threading import Thread
import time

basket = 0


class chef(Thread):
    names = ''

    def run(self) -> None:
        global basket
        while True:
            if basket == 500:
                time.sleep(3)
                continue
            else:
                basket = basket + 1
                print(f'{self.name}做了第{basket}个蛋挞')


class client(Thread):
    names = ''
    money = 3000
    count = 0

    def run(self) -> None:
        global basket
        while True:
            if self.money==0:
                print(f'{self.name}买了{self.count}个蛋挞')
                break
            elif basket > 0:
                self.money -= 2
                self.count += 1
                basket -= 1
                print(f'{self.name}买到一个蛋挞')

            elif basket == 0:
                time.sleep(2)
                continue


c1 = chef()
c2 = chef()
c3 = chef()
c1.setDaemon(True)
c2.setDaemon(True)
c3.setDaemon(True)
c1.name = '李奇明'
c2.name = '熊鑫'
c3.name = '关欣'
ct1 = client()
ct2 = client()
ct3 = client()
ct4 = client()
ct5 = client()
ct6 = client()
ct1.name = '凯南'
ct2.name = '提莫'
ct3.name = '维嘉'
ct4.name = '兰博'
ct5.name = '露露'
ct6.name = '崔丝塔娜'
c1.start()
c2.start()
c3.start()
ct1.start()
ct2.start()
ct3.start()
ct4.start()
ct5.start()
ct6.start()
