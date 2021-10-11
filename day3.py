# 任务一：
# 实现输入10个数字，并打印10个数的求和结果
# num=input('请输入十个数，空格隔开：').split()
# list=[]
# for i in num:
#     list.append(float(i))
# avg=sum(list)/len(list)
# print('这十个数的平均数为：',round(avg,2))

# 任务二：
# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# num=input('请输入十个数，空格隔开：').split()
# list=[]
# for i in num:
#     list.append(float(i))
# avg=sum(list)/len(list)
# print('这十个数的最大值为：',max(list))
# print('这十个数的和为：',sum(list))
# print('这十个数的平均数为：',round(avg,2))

# 任务三：
# 使用random模块，如何产生 50~150之间的数？
# import random
# rdt=random.randint(50,150)
# print(rdt)

# 任务四：
# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# a,b,c=map(int,input("输入任意三边").split())
# if a+b>c and a+c>b and b+c>a:
#     if a==b==c:
#         print("构成等边三角形")
#     elif a==b or b==c or a==c:
#         print("构成等腰三角形")
#     elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#         print("构成直角三角形")
#     else:
#         print("构成普通三角形")
# else:
#     print("不能形成三角形")

# 任务五：
# 有以下两个数，使用+，-号实现两个数的调换。
# A=56
# B=78
# 实现效果：
# A=78
# B=56

# A=56
# B=78
# sum=A+B
# B=sum-B
# A=sum-B
# print("A=",A,"B=",B)

# 任务六：
# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# for i in range(3):
#     user = input('请输入用户名：')
#     password = input('请输入密码：')
#     if user!='root' and password!='admin':
#         print("密码输入错误")
# print("三次用户名密码输入错误！锁定账户！")

# 任务七：
# 编程实现下列图形的打印
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
# * * * * * * *
#
# for i in range(1,8):
#     for j in range(1,8-i):
#         print(end=" ")
#     for k in range(8-i,8):
#         print("*",end=" ")
#     print("")

# 任务八：
# 使用while循环实现99乘法表的打印。
#
# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print('%d*%d=%d'%(j,i,i*j),end=' ')
#         j+=1
#     print()
#     i+=1
#
# 任务九：
# 编程实现99乘法表的倒叙打印
# i=9
# while i>=1:
#     j=1
#     while j<=i:
#         print('%d*%d=%d'%(j,i,i*j),end=' ')
#         j+=1
#     print()
#     i-=1

# 任务十：
# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
#
# h=20
# i=0
# a=0
# while True:
#     i+=1
#     a=i*3-i*2
#     if a==h-3:
#         break
# print(i+1)

# 任务十一：
# 判断下列变量命名是否合法
# 标识符	是否合法	标识符	是否合法
# char	是	Cy%ty	否
# Oax_li	是	$123	否
# fLul	是	3_3 	否
# BYTE	是	T_T	是

# 任务十二：
# 继续完成上午的猜数字游戏的需求功能。
# 1.添加计数打印功能
# 2.添加次数金币功能和锁定系统功能。
#
# import random
# rdt=random.randint(50,150)
# print(rdt)
# count=0
# while True:
#     count+=1
#     if count==6:
#         print('没有机会了！')
#         break
#     num=int(input("请输入一个50~150之间的整数:"))
#     if num==rdt:
#         print("恭喜你用了%d次猜对了！"%count)
#         break
#     else:
#         print('再想想，已经猜了%d次'%count)

# 任务十三：
# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# s=1
# list=[]
# for i in range(1,21):
#     s=i*s
#     list.append(s)
#     print(sum(list))
