from Address import Address
from Bank import Bank
from User import User
from welcome import Welcome
from Utils import Utils

# 初始化必要对象
welcome = Welcome()
utils = Utils()
address = Address()
user = User()
bank = Bank()


# 必要的初始化方法
# 开户方法
def addUser():
    username = utils.inputHelp("用户名")
    password = utils.check("密码")
    country = utils.inputHelp("居住地址，1.国家：")
    province = utils.inputHelp("省份")
    street = utils.inputHelp("街道")
    door = utils.inputHelp("门牌号")
    money = int(input("银行卡存款余额"))

    n = bank.bank_addUser(username, password, country, province, street, door, money)

    if n == 2:
        print("该用户已存在！")
    elif n == 3:
        print("用户库已满！请携带证件到其他地方办理！谢谢！")
    elif n == 1:
        print("注册成功！以下是您的开户信息：")
        user = bank.bank[username]
        print(bank.myinfo.format(account=user["account"],
                                 username=username,
                                 password=user["password"],
                                 country=user["country"],
                                 province=user["province"],
                                 street=user["street"],
                                 door=user["door"],
                                 money=user["money"],
                                 bank_name=user["bank_name"]
                                 ))


def saveMoney():
    account = utils.inputHelp("账号")
    while True:
        saveMoney = utils.inputHelp("存储金额")
        if saveMoney.isdigit():
            saveMoney = int(saveMoney)
            break
        else:
            print("余额输入错误，请重新输入！")
            continue
    flag = bank.bank_saveMoney(account, saveMoney)
    if flag:
        print("存储成功!")
    else:
        print("存钱失败！")


def takeMoney():
    account = utils.inputHelp("账号")
    password = utils.inputHelp("密码")
    while True:
        money = utils.inputHelp("要取金额")
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入要取金额有误，请重新输入！")
    flag = bank.bank_money(account, password, money)
    if flag == 0:
        print("取钱成功！")
    elif flag == 1:
        print("取钱失败！无此账号")
    elif flag == 2:
        print('密码错误！')
    elif flag == 3:
        print('取钱失败！金额不足！')

    # pass


def transMoney():
    account = utils.inputHelp("取款账号")
    password = utils.inputHelp("密码")
    while True:
        money = utils.inputHelp("要转账金额")
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入要取金额有误，请重新输入！")
    flag = bank.bank_money(account, password, money)
    if flag == 0:
        accounts = utils.inputHelp("收款账号")
        flag1 = bank.bank_saveMoney(accounts, money)
        if flag1:
            print('转账成功！')
        else:
            print('转账失败！无收款账号')
    elif flag == 1:
        print("转账失败！无取款账号")
    elif flag == 2:
        print('密码错误！')
    elif flag == 3:
        print('转账失败！金额不足！')


def selectUser():
    account = utils.inputHelp("账号")
    password = utils.inputHelp("密码")
    flog = bank.bank_select(account, password)
    if flog == 1:
        print("查询失败！无此账号")
    elif flog == 2:
        print('密码错误！')


while True:
    # 欢迎页面
    welcome.print_welcome()

    # 用户选择:程序入口
    chose = utils.inputHelp("选项")
    if bank.isExists(chose, bank.bank_choose):
        if chose == "1":
            addUser()
        elif chose == "2":
            saveMoney()
        elif chose == "3":
            takeMoney()
        elif chose == "4":
            transMoney()
        elif chose == "5":
            selectUser()
        elif chose == "6":
            print("Bye!欢迎下次光临！")
            break
    else:
        print("不存在该选项，被瞎弄！")
