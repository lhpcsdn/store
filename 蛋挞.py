import time
from threading import Thread

seconds = time.time()
total = 0


class Cook(Thread):
    username = ''
    money = 0
    count = 0

    def run(self):
        global total
        while True:
            if time.time() - seconds <= 3:
                if total < 500:
                    total = total + 1
                    self.count = self.count + 1
                    print(self.username, '造了', self.count, '个蛋挞。')
                    self.money = self.count * 1.5
                    print(self.username, '的总工资为', self.money, '元')
                    if total == 500:
                        time.sleep(3)
            else:
                break


class Customer(Thread):
    customer = ''
    save = 3000
    num = 0

    def run(self) -> None:
        global total
        while True:
            if total > 0 and self.save > 0:
                self.num = self.num + 1
                total = total - 1
                self.save = self.save - 3 * self.num
                print(self.customer, '买了', self.num, '个蛋挞', '还剩', self.save)
                if self.save == 0:
                    break
            elif total == 0:
                time.sleep(2)


p1 = Cook()
p2 = Cook()
p3 = Cook()

p1.username = '张三'
p2.username = '李四'
p3.username = '王五'

p1.start()
p2.start()
p3.start()

c1 = Customer()
c2 = Customer()
c3 = Customer()
c4 = Customer()
c5 = Customer()
c6 = Customer()

c1.customer = '小明'
c2.customer = '小兰'
c3.customer = '小红'
c4.customer = '小蓝'
c5.customer = '李青'
c6.customer = '赵信'

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
