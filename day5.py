# # dict = {"k1":"v1","k2":"v2","k3":"v3"}
# # 1、请循环遍历出所有的key
# # 2、请循环遍历出所有的value
# # 3、请在字典中增加一个键值对,"k4":"v4"
#
# dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
#
# print('''
# 1、请循环遍历出所有的key
# 2、请循环遍历出所有的value
# 3、请在字典中增加一个键值对,"k4":"v4"
# 0、退出系统
# ''', dict)
# while True:
#     num = int(input("请选择操作："))
#     if num == 1:
#         for k in dict.keys():
#             print(k)
#     elif num == 2:
#         for v in dict.values():
#             print(v)
#     elif num == 3:
#         dict["k4"] = "v4"
#         print(dict)
#     elif num == 0:
#         break
#     else:
#         print('输入错误！')
#
# # 小明去超市购买水果，账单如下
# # 苹果  32.8
# # 香蕉  22
# # 葡萄  15.5
# # 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
# # 用水果名称做key，金额做value，创建一个字典
# # info = {
# #     '苹果':32.8,
# #     '香蕉': 22,
# #     '葡萄': 15.5
# # }
#
# print("==================水果商城=================")
# info = {'苹果': '32.8', '香蕉': '22', '葡萄': '15.5'}
# while True:
#     fruit = input('请输入要查询的水果：')
#     if fruit in info:
#         print(info[fruit])
#     else:
#         print('无查询结果！')
#
# # 小明，小刚去超市里购买水果
# # 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，
# # 请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
# # 以姓名做key，value仍然是字典
# # Friuts = {
# # 	‘苹果’：12.3，  # 水果和单价
# # 	‘草莓’：4.5，
# #        ‘香蕉’：6.3，
# #        ‘葡萄’：5.8，
# #        ‘橘子’：6.4，
# #        ‘樱桃’：15.8
# # }
# # info = {
# #     '小明': {
# #         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
# #         'money': ??
# #     },
# #     '小刚': {
# #         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
# #         'money': ??
# #     }
# # }   49.2  58.5  63 （170.7）  110.2  76.8  474  （661）
# Friuts = {
#     '苹果': 12.3,
#     '草莓': 4.5,
#     '香蕉': 6.3,
#     '葡萄': 5.8,
#     '橘子': 6.4,
#     '樱桃': 15.8}
# info = {
#     '小明': {
#         'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
#     },
#     '小刚': {
#         'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
#     }
# }
# money = 0
# list_1 = []
# list_2 = []
# while True:
#     name = input('请输入名字：')
#     if name == '小明':
#         if len(list_1) == 0:
#             for key_1 in Friuts:
#                 for key_2 in info[name]['fruits']:
#                     if key_1 == key_2:
#                         money = Friuts[key_1] * info[name]['fruits'][key_2]
#                         list_1.append(money)
#                         info[name]['money'] = sum(list_1)
#                     else:
#                         pass
#         else:
#             pass
#         print(info[name])
#         print(info)
#     elif name == '小刚':
#         if len(list_2) == 0:
#             for key_1 in Friuts:
#                 for key_2 in info[name]['fruits']:
#                     if key_1 == key_2:
#                         money = Friuts[key_1] * info[name]['fruits'][key_2]
#                         list_2.append(money)
#                         info[name]['money'] = sum(list_2)
#                         break
#                     else:
#                         pass
#         else:
#             pass
#         print(info[name])
#         print(info)
#     else:
#         print('输入错误！')
#
#
# # 编写一个函数，传入一个列表，并统计每个数字出现的次数。
# # 返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
# # [1,2,5,6,4,2,1,3,5]
# # def statistics(list_1):
# #     count_1 = {}
# #     for c in list_1:
# #         count_1[c] = count_1.get(c, 0) + 1
# #     return count_1
# #
# #
# # list_2 = list(map(str, input().split()))
# # print(statistics(list_2))
#
# # print(count(info))
#
# def statistics(list_1):
#     count_1 = {}
#     for i in list_1:
#         if i in count_1:
#             count_1[i] += 1
#         else:
#             count_1[i] = 1
#     return count_1
#
#
# list_2 = list(map(str, input("请输入一组数据并用空格隔开").split()))
# print(statistics(list_2))
#
# # 有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# # # 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# # names = [
# #     ["刘备","56","男","106","IBM", 500 ,"50"],
# #     ["大乔","19","女","230","微软", 501 ,"60"],
# #     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
# #     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# # ]
#
# names = [
#     ["刘备", "56", "男", "106", "IBM", 500, "50"],
#     ["大乔", "19", "女", "230", "微软", 501, "60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700, "10"]
# ]
#
# dict = {}
# for i in names:
#     dict[i[0]] = {
#         '年龄': i[1],
#         '性别': i[2],
#         '编号': i[3],
#         '任职公司': i[4],
#         '薪资': i[5],
#         '部门编号': i[6]
#     }
# print(dict)
#
#
# '''
#  Frank的商城：
#         1.准备商品
#         2.空的购物车
#         3.钱包初始化金钱
#         4.最后打印购物小条
#     1.业务：
#         看到商品：
#             商品存在
#                 看金钱够：
#                     成功加入购物车。
#                     余额减去对应价格。
#                 不够：
#                     穷鬼，去买其他商品。
#             商品不存在：
#                 输入错误。
#             输入Q或q，退出并结算。打印小条。
# 任务：优惠券加上随机获得一张优惠券（9折10，5折3，免费的1：单个商品打折9折10，5折3，免费的1）
# '''
# # 准备商品
# import random
# print("====Frank的商城===")
# shop = [
#     #     0   ,   1
#     ["戴尔", 19999],  # 0
#     ["电磁炉", 199],  # 1
#     ["A4纸", 9.9],  # 2
#     ["华为P50 4G", 5000],  # 3
#     ["冰箱", 2000],
#     ["液晶电视", 2999],
#     ["平板电脑", 1999],
#     ["三体", 99],
#     ["滑板鞋", 199],
#     ["篮球", 99],
#     ["电话手表", 399],
#     ["投影仪", 999],
# ]
# # 初始化余额
# money = input("请输入您的余额")
# money = int(money)
# # 准备一个购物车
# mycart = []
# coupons = [['九折', 100, 0.9], ['八折', 50, 0.8], ['五折', 10, 0.5], ['三折', 5, 0.3], ['一折', 1, 0.1]]
# while True:
#     # 展示商品
#     for index, value in enumerate(shop):
#         print(index, ":", value)
#     chose = input("请输入商品编号")  # 输入的还是str
#     if chose.isdigit():  # 判断是否是数字
#         chose = int(chose)
#         if chose > len(shop):
#             print("这里没有您需要的商品")
#         else:
#             #   余额满足的条件
#             total = 0
#             count = int(input('请选择数量：'))
#             if count > 0:
#                 if money > shop[chose][1] * count:
#                     mycart.append(shop[chose])
#                     mycart.append(count)
#                     money = money - shop[chose][1] * count
#                     print("恭喜你，加入购物车", count, "件", mycart[total][0], "您的余额为：", round(money, 2))
#                     total += 1
#                     num = 166
#                     if num > 0:
#                         num += -1
#                         print("恭喜你获取一次抽奖机会")
#                         attend = int(input("请输入1：参与，输入其他不参与。 "))
#                         if attend == 1:
#                             reward = random.randint(0, len(coupons) - 1)
#                             coupons[reward][1] += -1
#                             if coupons[reward][1] == -1:
#                                 coupons.pop(reward)
#                                 pass
#                             else:
#                                 money = money + shop[chose][1] * (1 - coupons[reward][2])
#                                 print("恭喜你获得", coupons[reward][0], "优惠卷")
#                                 print("你的余额为：", round(money, 2))
#                         else:
#                             pass
#                     else:
#                         pass
#                 # 不满足
#                 else:
#                     print("余额不足！")
#             else:
#                 print("添加失败！")
#
#     elif chose == "q" or chose == "Q":
#         #    打印购物小条
#         print("=====================")
#         for k in mycart:
#             print(k)
#         print("您的余额还剩:", round(money, 2))
#         break
#     else:  # 不是数字
#         print("输入错误")
