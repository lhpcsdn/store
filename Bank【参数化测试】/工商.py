import random
from tool import update
from tool import select

# print('''
# ***********************************************
# *                  中国工商银行                 *
# *                  账户管理系统                 *
# *                     V1.0                    *
# ***********************************************
# *                   1、开户                    *
# *                   2、存钱                    *
# *                   3、取钱                    *
# *                   4、转账                    *
# *                   5、查询                    *
# *                   6、Bye！                   *
# ***********************************************
# ''')
bank = {}
bank_name = '中国工商银行昌平支行'


# account_moneys = 0    #转账金额

# def adduser():
#     account = random.randint(10000000, 99999999)
#     username = input('请输入姓名：')
#     while True:
#         password = int(input('请输入密码：'))
#         if get_length(password) == 6:
#             break
#         else:
#             print('输入不合法！')
#     print('下面请输入地址：')
#     country = input('\t\t请输入你的国家：')
#     province = input('\t\t请输入你的省份：')
#     street = input('\t\t请输入你的街道：')
#     door = input('\t\t请输入你的门牌号：')
#     money = int(input('\t\t请输入你的初始余额：'))
#     add = bank_add(username, account, password, country, province, street, door, money)
#     if add == 1:
#         sql2 = "insert into information values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
#         param2 = [account, username, password, country, province, street, door, money, bank_name]
#         update(sql2, param2)
#         print('恭喜你添加用户成功，以下是您的账户信息：')
#         info = '''
#                             ------------个人信息------------
#                             用户名:%s
#                             账号：%s
#                             密码：*****
#                             国籍：%s
#                             省份：%s
#                             街道：%s
#                             门牌号：%s
#                             存款余额：%s
#                             开户行名称：%s
#                         '''
#         # 每个元素都可传入%
#         print(info % (username, account, country, province, street, door, money, bank_name))
#     elif add == 2:
#         print('用户已存在')
#     elif add == 3:
#         print('数据库已满，请到光之国银行开户')


def bank_add(username, account, password, country, province, street, door, money):
    if get_length(password) != 6 or get_length(account) != 8:
        return 4
    sql = "select * from information"
    param = []
    data = select(sql, param)
    if len(data) >= 100:
        return 3

    sql1 = "select * from information where username = %s"
    param1 = [username]
    data = select(sql1, param1)
    if len(data) != 0:
        return 2
    else:
        sql2 = "insert into information values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
        param2 = [account, username, password, country, province, street, door, money, bank_name]
        update(sql2, param2)
        return 1


# 计算密码长度
def get_length(password):
    password = int(password)
    length = 0
    while password != 0:
        length += 1
        password = password // 10
    return length


# 当前余额
# def select_money(accounts):
#     sal_select = "select * from information where account=%s"
#     param_select = [accounts]
#     data_select = select(sal_select, param_select)
# print('你的当前帐号余额为：', data_select[0][7])


# # 存钱
# def saving():
#     account = int(input('请输入存款账号：'))
#     state = account_is(account)
#     if state:
#         select_money(account)
#     else:
#         print('还未开户，请先开户！')


# 查找账号是否存在
def account_is(accounts, index, sa_money):
    sal = "select account from information where account=%s"
    param = [accounts]
    select.accounts = select(sal, param)
    for i in select.accounts:
        if accounts in i:
            if index == 2:  # 存钱
                # sa_money = int(input('请输入存款的金额'))
                sal_save = "update information set money = money+%s where account=%s"
                param_save = [sa_money, accounts]
                update(sal_save, param_save)
                # print('存款成功！')
                return 1
            if index == 3:
                return 1
            if index == 4:
                return 1
            if index == 5:
                return 1
    return 2


# 转账
def transfer(account_trs, password, account_money, account_in):
    # account_trs = int(input('请输入账号：'))
    state = account_is(account_trs, 4, 0)
    if state == 1:
        # password = int(input('请输入密码：'))
        sal = 'select account,password,money from information where account=%s'
        param = [account_trs]
        data = select(sal, param)
        if account_trs == data[0][0]:
            if password != data[0][1]:
                return 2
            elif password == data[0][1]:
                # print('登录成功!')
                # select_money(account_trs)
                # global account_money
                # account_money = int(input('请输入转账金额：'))
                if account_money > data[0][2]:
                    return 3
                else:
                    # account_in = int(input('请输入转账账号：'))
                    state = account_is(account_in, 4, 0)
                    if state == 1:
                        sal_trans = "update information set money = money-%s where account=%s"
                        param_trans = [account_money, account_trs]
                        update(sal_trans, param_trans)
                        sal_trans1 = "update information set money = money+%s where account=%s"
                        param_trans1 = [account_money, account_in]
                        update(sal_trans1, param_trans1)
                        # select_money(account_trs)
                        return 0
                    else:
                        return 1
    else:
        return 1


# def transfer_is():
#     state = transfer()
#     if state == 0:
#         print('转账成功')
#     elif state == 1:
#         print('还未开户，转账失败')
#     elif state == 2:
#         print('密码输入错误，转账失败')
#     else:
#         print('转账金额不能大于当前余额')


# 取款
def take_money(account_take, password, money_is):
    # account_take = int(input('请输入账号：'))
    state = account_is(account_take, 3, 0)
    if state == 1:
        # password = int(input('请输入密码：'))
        sal = 'select account,password,money from information where account=%s'
        param = [account_take]
        data = select(sal, param)
        if account_take == data[0][0]:
            if password != data[0][1]:
                return 2
            elif password == data[0][1]:
                # money_is = int(input('请输入取款金额：'))
                if money_is > data[0][2]:
                    return 3
                else:
                    sal_take = "update information set money = money-%s where account=%s"
                    param_take = [money_is, account_take]
                    update(sal_take, param_take)
                    # select_money(account_take)
                    return 0
    else:
        return 1


# def take():
#     state = take_money()
#     if state == 0:
#         print('取款成功')
#     elif state == 1:
#         print('还未开户，取款失败')
#     elif state == 2:
#         print('密码输入错误！')
#     else:
#         print('取款金额不能大于当前余额')


# 查询账号信息
def query_money(account_take, password, ):
    # account_take = int(input('请输入账号：'))
    state = account_is(account_take, 5, 0)
    if state == 1:
        # password = int(input('请输入密码：'))
        sal_select = 'select account,password from information where account=%s'
        param_select = [account_take]
        data_select = select(sal_select, param_select)
        if account_take == data_select[0][0]:
            if password != data_select[0][1]:
                return 2
            elif password == data_select[0][1]:
                # sql = "select * from  information  where account=%s"
                # param = [account_take]
                # data = select(sql, param)
                # print('\t\t\t\t\t\t\t\t\t\t\t查询成功，以下是您的账户信息：')
                # info = '''
                #                             ------------个人信息------------
                #                             用户名:%s
                #                             账号：%s
                #                             密码：*****
                #                             国籍：%s
                #                             省份：%s
                #                             街道：%s
                #                             门牌号：%s
                #                             存款余额：%s
                #                             开户行名称：%s
                #                         '''
                # # 每个元素都可传入%
                # print(info % (
                #     data[0][1], data[0][0], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7], data[0][9]))
                return 0
    else:
        return 1

# def query():
#     state_query = query_money()
#     if state_query == 0:
#         print('中国工商银行昌平支行')
#     elif state_query == 1:
#         print('该用户不存在')
#     elif state_query == 2:
#         print('密码输入错误！')

# while True:
#     index = int(input("请输入您的操作"))
#     if index == 1:
#         adduser()
#     elif index == 2:
#         saving()
#     elif index == 3:
#         take()
#     elif index == 4:
#         transfer_is()
#     elif index == 5:
#         query()
#     elif index == 6:
#         break
