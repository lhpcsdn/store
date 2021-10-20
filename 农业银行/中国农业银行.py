import random

print('''
***********************************************
*                  中国农业银行                 *
*                  账户管理系统                 *
*                     V1.0                    *
***********************************************
*                   1、开户                    *
*                   2、存钱                    *
*                   3、取钱                    *
*                   4、转账                    *
*                   5、查询                    *
*                   6、Bye！                   *
***********************************************
''')
bank = {}
bank_name = '中国农业银行的昌平支行'


# account_moneys = 0    #转账金额

def adduser():
    account = random.randint(10000000, 99999999)
    print('''
    1、一类账户【金卡】
    2、二类账户【银卡】
    ''')
    while True:
        types = input('请选择账户类型：')
        if types == '1':
            types = '一类账户【金卡】'
            break
        elif types == '2':
            types = '二类账户【银卡】'
            break
        else:
            print('请重新选择！')
    username = input('请输入姓名：')
    while True:
        password = int(input('请输入密码：'))
        if get_length(password) == 6:
            break
        else:
            print('输入不合法！')
    print('下面请输入地址：')
    country = input('\t\t请输入你的国家：')
    province = input('\t\t请输入你的省份：')
    street = input('\t\t请输入你的街道：')
    door = input('\t\t请输入你的门牌号：')
    add = bank_add(username, account, types, password, country, province, street, door)
    if add == 1:
        print('恭喜你添加用户成功，以下是您的账户信息：')
        info = '''
                            ------------个人信息------------
                            用户名:%s
                            账号：%s
                            账户类型：%s
                            密码：*****
                            国籍：%s
                            省份：%s
                            街道：%s
                            门牌号：%s
                            存款余额：%s
                            开户行名称：%s
                        '''
        # 每个元素都可传入%
        print(info % (username, account, types, country, province, street, door, bank[username]['存款余额'], bank_name))
    elif add == 2:
        print('用户已存在')
    elif add == 3:
        print('数据库已满，请到光之国银行开户')


def bank_add(username, account, types, password, country, province, street, door):
    if username in bank:
        return 2
    elif len(bank) >= 100:
        return 3
    else:
        bank[username] = {
            '账号': account,
            '账户类型': types,
            '密码': password,
            '存款余额': 0,
            '开户行': bank_name,
            '国家': country,
            '省份': province,
            '街道': street,
            '门牌号': door
        }
        return 1


# 账户类型额度限制
def account_type(type_s, limit):
    if type_s == '一类账户【金卡】':
        if limit > 50000:
            return 1
    elif type_s == '二类账户【银卡】':
        if limit > 20000:
            return 2


# 计算密码长度
def get_length(password):
    length = 0
    while password != 0:
        length += 1
        password = password // 10
    return length


# 存钱
def saving():
    account = int(input('请输入存款账号：'))
    state = account_is(account)
    if state:
        print('存款成功！')
    else:
        print('还未开户，请先开户！')


# 查找账号是否存在
def account_is(accounts):
    for username, bank_info in bank.items():
        # print(username,bank_info)
        for key, value in bank_info.items():
            if value == accounts:
                if index == 2:  # 存钱
                    sa_money = int(input('请输入存款的金额'))
                    bank_info['存款余额'] += sa_money
                    print(bank_info)
                if index == 4:
                    print(account_money)  # 转账
                    bank_info.update({'存款余额': account_money + bank_info['存款余额']})  # 更新字典key的value，已经存在的key
                    print(bank_info)
                return True
    return False


##查找转账账号
def account_tran(account_tr):
    for username, bank_info in bank.items():
        # print(username,bank_info)
        for key, value in bank_info.items():
            if value == account_tr:
                return True
    return False


# 转账
def transfer():
    account_trs = int(input('请输入账号：'))
    state = account_tran(account_trs)
    if state:
        password = int(input('请输入密码：'))
        for username, bank_info in bank.items():
            for key, value in bank_info.items():
                if account_trs == bank_info['账号']:
                    if password != bank_info['密码']:
                        return 2
                    elif password == bank_info['密码']:
                        print('登录成功,当前余额为：', bank_info['存款余额'])
                        while True:
                            global account_money
                            account_money = int(input('请输入转账金额：'))
                            ty = account_type(bank_info['账户类型'], account_money)
                            if ty == 1:
                                print('不能超出最大限额5万！')
                            elif ty == 2:
                                print('不能超过最大限额2万！')
                            else:
                                if account_money > bank_info['存款余额']:
                                    return 3
                                else:
                                    account_in = int(input('请输入转账账号：'))
                                    state = account_is(account_in)
                                    if state:
                                        bank_info['存款余额'] -= account_money
                                        print(bank_info)
                                        return 0
                                    else:
                                        return 1
    else:
        return 1


def transfer_is():
    state = transfer()
    if state == 0:
        print('转账成功')
    elif state == 1:
        print('还未开户，转账失败')
    elif state == 2:
        print('密码输入错误，转账失败')
    else:
        print('转账金额不能大于当前余额')


# 取款
def take_money():
    account_take = int(input('请输入账号：'))
    state = account_is(account_take)
    if state:
        password = int(input('请输入密码：'))
        for username, bank_info in bank.items():
            for key, value in bank_info.items():
                if account_take == bank_info['账号']:
                    if password != bank_info['密码']:
                        return 2
                    elif password == bank_info['密码']:
                        print('登录成功,当前余额为：', bank_info['存款余额'])
                        while True:
                            money_is = int(input('请输入取款金额：'))
                            ty = account_type(bank_info['账户类型'], money_is)
                            if ty == 1:
                                print('不能超出最大限额5万！')
                            elif ty == 2:
                                print('不能超过最大限额2万！')
                            else:
                                if money_is > bank_info['存款余额']:
                                    return 3
                                else:
                                    bank_info['存款余额'] -= money_is
                                    print(bank_info)
                                    return 0
    else:
        return 1


def take():
    state = take_money()
    if state == 0:
        print('取款成功')
    elif state == 1:
        print('还未开户，取款失败')
    elif state == 2:
        print('密码输入错误！')
    else:
        print('取款金额不能大于当前余额')


# 查询账号信息
def query_money():
    account_take = int(input('请输入账号：'))
    state = account_is(account_take)
    if state:
        password = int(input('请输入密码：'))
        for username, bank_info in bank.items():
            for key, value in bank_info.items():
                if account_take == bank_info['账号']:
                    if password != bank_info['密码']:
                        return 2
                    elif password == bank_info['密码']:
                        print(bank_info)
                        return 0
    else:
        return 1


def query():
    state_query = query_money()
    if state_query == 0:
        print('查询成功')
    elif state_query == 1:
        print('该用户不存在')
    elif state_query == 2:
        print('密码输入错误！')


while True:
    index = int(input("请输入您的操作"))
    if index == 1:
        adduser()
    elif index == 2:
        saving()
    elif index == 3:
        take()
    elif index == 4:
        transfer_is()
    elif index == 5:
        query()
    elif index == 6:
        break
