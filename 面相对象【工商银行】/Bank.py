import random
from Utils import Utils


class Bank():
    # 个人信息模板
    myinfo = '''
    \033[0;32;40m
    ------------账户信息------------
    账号：{account}
    姓名：{username}
    密码：{password}
    地址：
        国家：{country}
        省份：{province}
        街道：{street}
        门牌号：{door}
    账户余额：{money}
    注册银行名：{bank_name}
    -------------------------------
    \033[0m
    '''
    bank = {}  # 银行数据库

    __bank_name = "中国工商银行昌平支行"  # 银行名称

    bank_choose = {"1": "开户", "2": "存钱", "3": "取钱", "4": "转账", "5": "查询", "6": "Bye!"}  # 银行业务选项

    # 银行的名称是建立时就定下来的，不存在用户来设置其名称

    def getBankName(self):
        return self.__bank_name

    # 判断是否在某个范围之内
    def isExists(self, chose, data):
        if chose in data:
            return True
        return False

    # 银行开户逻辑
    def bank_addUser(self, username, password, country, province, street, door,
                     money):

        if len(self.bank) >= 100:
            return 3
        elif username in self.bank:
            return 2
        else:
            self.bank[username] = {"account": Utils().getRandom(),
                                   "password": password,
                                   "country": country,
                                   "province": province,
                                   "street": street,
                                   "door": door,
                                   "money": money,
                                   "bank_name": self.__bank_name}
            return 1

    # 银行存钱逻辑
    def bank_saveMoney(self, account="0", saveMoney=0):
        # 获取所有账号
        values = self.bank.values()
        for i in values:
            if account == i['account']:
                i["money"] = i["money"] + saveMoney
                print(i)
                return True
        return False

    # 银行取钱逻辑
    def bank_money(self, account="0", password='0', money=0):
        # 获取所有账户
        values = self.bank.values()
        for i in values:
            if account == i['account']:
                if password != i['password']:
                    return 2
                if money < i["money"]:
                    i["money"] = i["money"] - money
                    return 0
                else:
                    return 3
        return 1

    def bank_select(self, account="0", password='0'):
        # 获取所有账户
        values = self.bank.values()
        for i in values:
            if account == i['account']:
                if password != i['password']:
                    return 2
                else:
                    print('\t\t\t\t\t\t\t\t\t\t\t\t查询成功，以下是您的账户信息：')
                    info = '''
                                                ------------个人信息------------
                                                账号：%s
                                                密码：%s
                                                国籍：%s
                                                省份：%s
                                                街道：%s
                                                门牌号：%s
                                                存款余额：%s
                                                注册银行名：%s
                                            '''
                    # 每个元素都可传入%
                    print(info % (
                        i['account'], i['password'], i['country'], i['province'], i['street'],
                        i['door'], i['money'], i['bank_name']))
                    return 3
        return 1
