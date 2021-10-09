'''

判断：
 单分支 if   eles
 多分支 if  elif   elif  elif ...... else
10-90这个范围里面
如果猜大了打印”猜大了“ 猜小了
最多猜3次 锁屏 time.sleep(10)
'''
from ctypes import *
import  random
rdt=random.randint(1,100)
print(rdt)
print("请输入一个1~100之间的整数,三次机会后锁屏。")
chance=1
while chance<4:
    chance+=1
    num = int(input("请输入你猜的数:"))
    if num>rdt:
        print("猜大了")
    elif num<rdt:
        print("猜小了")
    else:
        print("恭喜你猜对了")
        break
    if chance==4:
        user=windll.LoadLibrary('user32.dll')
        user.LockWorkStation()
        print("没机会了")


