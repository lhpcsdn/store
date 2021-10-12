# print('''
#     信息管理
# 1.统计每个人的平均薪资
# 2.统计每个人的平均年龄
# 3.增加员工
# 4.统计公司男女人数
# 5.每个部门的人数
# 6.查询所有员工信息
# 7.退出系统
# ''')
# list1 = ['曹操', '56', '男', '106', 'IBM', 500, '50']
# list2 = ['大乔', '19', '女', '230', '微软', 501, '60']
# list3 = ['小乔', '19', '女', '210', 'Oracle', 600, '60']
# list4 = ['许褚', '45', '男', '230', 'Tencent', 700, '10']
# list = [list1, list2, list3, list4]
# while True:
#     num = input("请选择操作：")
#     if num == '1':
#         total = 0
#         for i in range(0, len(list)):
#             total = list[i][5] + total
#         print('每个人的平均工资为：', total / len(list))
#     elif num == '2':
#         total2 = 0
#         for i in range(0, len(list)):
#             total2 = int(list[i][1]) + total2
#         print('每个人的平均年龄：', total2 / len(list))
#     elif num == '3':
#         name = input("请输入姓名：")
#         year = input('请输入年龄：')
#         sex = input('请输入性别：')
#         num4 = input("请输入编号：")
#         firm = input('请输入任职公司：')
#         wages = input('请输入薪资：')
#         depart = input('请输入部门编号：')
#         list.append([name, year, sex, num4, firm, wages, depart])
#         print("添加信息成功")
#         print(list[-1])
#     elif num == '4':
#         man = woman = 0
#         for i in range(0, len(list)):
#             if list[i][2] == '男':
#                 man += 1
#             else:
#                 woman += 1
#         print('公司男生%d个' % man, '女生%d个' % woman)
#     elif num == '5':
#         num1 = num2 = num3 = 0
#         for i in range(0, len(list)):
#             if list[i][6] == '50':
#                 num1 += 1
#             elif list[i][6] == '60':
#                 num2 += 1
#             elif list[i][6] == '10':
#                 num3 += 1
#         print("50部门有%d人" % num1, '60部门有%d人' % num2, '10部门有%d人' % num3)
#     elif num == '6':
#         print('  姓名   年龄 性别  编号  任职公司 薪资 部门编号')
#         for i in range(len(list)):
#             print(list[i])
#     elif num == '7':
#         break
#     else:
#         print('输入错误！！！')


# 现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。
# 但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，
# 所以大家上交作业的次数并不一致。
# [罗恩, 23 ,35 ,44]
# [哈利 ,60, 77 ,68 ,88, 90]
# [赫敏, 97 ,99 ,89 ,91, 95, 90]
# [马尔福 ,100, 85 ,90]
# 求每个人的总成绩？
# list1 = ['罗恩', 23, 35, 44]
# list2 = ['哈利', 60, 77, 68, 88, 90]
# list3 = ['赫敏', 97, 99, 89, 91, 95, 90]
# list4 = ['马尔福', 100, 85, 90]
# total = total2 = total3 = total4 = 0
# i = 1
# for i in range(1, len(list1)):
#     total = list1[i] + total
# print('罗恩的总成绩为：', total)
# for i in range(1, len(list2)):
#     total2 = list2[i] + total2
# print('哈利的总成绩为：', total2)
# for i in range(1, len(list3)):
#     total3 = list3[i] + total3
# print('赫敏的总成绩为：', total3)
# for i in range(1, len(list4)):
#     total4 = list4[i] + total4
# print('马尔福的总成绩为：', total4)

# 阅读程序并回答问题
# 1.当输入是54321时，写出下面程序的运行结果。
# num = int(input("请输入一个数："))
# while   num != 0:
#     print(num % 10) 求余数
#     num = num //10  保留整数部分
# 1
# 2
# 3
# 4
# 5
#
# 54321
#
# 1
# 5432
#
# 2
# 543
#
# 3
# 54
#
# 4
# 5
#
# 5
#

# 请对下列列表进行冒泡排序（网易测试开发笔试题）
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
#
# a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
# for b in range(len(a)):
#     for i in range(len(a) - b - 1):
#         if a[i] > a[i + 1]:
#             a[i], a[i + 1] = a[i + 1], a[i]
# print(a)
