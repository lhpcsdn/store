# import xlrd
#
# # 拿到工作簿
# wb = xlrd.open_workbook(filename=r"E:\python\day07\三国集团.xlsx", encoding_override=True)
#
# # 选择一个选项卡
# st = wb.sheet_by_name("员工管理")
#
# rows = st.nrows  # 获取有多少行
# cols = st.ncols  # 获取有多少列
#
# #  平均年龄，总工资
# sal_sum = 0
# age_sum = 0
# for i in range(1, rows):
#     data = st.row_values(i)
#     sal_sum = sal_sum + data[1]
#     age_sum = age_sum + data[2]
#
# print("总工资为：", sal_sum, "，平均年龄为：", (age_sum / 3))

import xlrd

print('''
===========================
        服装管理系统
1、全年的销售总额
2、每件衣服的销售（件数）占比
3、每件衣服的月销售占比
4、每件衣服的销售额占比
5、最畅销的衣服是那种
6、每个季度最畅销的衣服
7、全年销量最低的衣服
8、退出系统
''')

wb = xlrd.open_workbook(r'E:\python\day07\任务\2020年每个月的销售情况.xlsx', encoding_override=True)


def sale():
    sal_sum = 0
    total = 0
    for month in wb.sheet_names():
        st = wb.sheet_by_name(month)
        rows = st.nrows  # 获取有多少行
        for i in range(1, rows):
            data = st.row_values(i)  # 每行的数据
            sal_sum += data[2] * data[4]  # 每月销售总额
        print(month, '销售额为：%.2f' % sal_sum)
    total += sal_sum  # 年销售总额
    print('全年的销售总额为：%.2f' % total)

#各服装的年销售量
def number():
    dress = {}  # 年各服装销售量
    sal_sum = 0
    sal_money = 0
    for month in wb.sheet_names():
        st = wb.sheet_by_name(month)
        rows = st.nrows  # 获取有多少行
        for i in range(1, rows):
            data = st.row_values(i)
            sal_sum += data[4]  # 每月销售总量
            if data[1] in dress:
                dress[data[1]] += data[4]
            else:
                dress[data[1]] = data[4]
    return dress


def sale_month():
    for month in wb.sheet_names():
        dress_month = {}  # 月各服装销售量
        sal_sum = 0
        st = wb.sheet_by_name(month)
        rows = st.nrows  # 获取有多少行
        for i in range(1, rows):
            data = st.row_values(i)
            sal_sum += data[4]  # 每月销售总量
            if data[1] in dress_month:
                dress_month[data[1]] += data[4]
            else:
                dress_month[data[1]] = data[4]
        print(month)
        print('月销售总数量', sal_sum)
        print(dress_month)
        for keys, values in dress_month.items():
            print(keys, '月销售（件数）占比为:%.2f' % ((values / sal_sum) * 100), '%')


def sale_money():
    for month in wb.sheet_names():
        dress_money = {}  # 月各服装销售额量
        sal_sum = 0
        sal_money = 0
        st = wb.sheet_by_name(month)
        rows = st.nrows  # 获取有多少行
        for i in range(1, rows):
            data = st.row_values(i)
            sal_money += data[2] * data[4]  # 每月销售总额
            if data[1] in dress_money:
                dress_money[data[1]] += data[2] * data[4]
                dress_money[data[1]] = round(dress_money[data[1]], 2)
            else:
                dress_money[data[1]] = data[2] * data[4]
                dress_money[data[1]] = round(dress_money[data[1]], 2)
        print(month)
        print('月销售总额%.2f' % sal_money)
        print(dress_money)
        for keys, values in dress_money.items():
            print(keys, '销售（件数）占比为:%.2f' % ((values / sal_money) * 100), '%')


def sell_well(dress_bests):
    dress_list = []  # 销售各件数放入列表从小到大排列
    for values in dress_bests.values():
        dress_list.append(values)
    for i in range(len(dress_list)):
        for j in range(len(dress_list) - i - 1):
            if dress_list[j] > dress_list[j + 1]:
                dress_list[j], dress_list[j + 1] = dress_list[j + 1], dress_list[j]
    if choose == 5 or choose == 6:
        for names, number_dress in dress_bests.items():
            if number_dress == dress_list[-1]:
                return names, dress_list[-1]  # 最畅销的衣服名称和数量
            else:
                continue
    elif choose == 7:
        for name_dress, number_dre in dress_bests.items():
            if number_dre == dress_list[0]:
                return name_dress, dress_list[0]  # 销量最低的衣服名称和数量
            else:
                continue


def quarter():
    dress_quarter = {}
    dress_quarter1 = {}
    dress_quarter2 = {}
    dress_quarter3 = {}
    for month in wb.sheet_names():
        dress_month = {}  # 月各服装销售量
        sal_sum = 0
        st = wb.sheet_by_name(month)
        rows = st.nrows  # 获取有多少行
        for i in range(1, rows):
            data = st.row_values(i)
            sal_sum += data[4]  # 每月销售总量
            if data[1] in dress_month:
                dress_month[data[1]] += data[4]
            else:
                dress_month[data[1]] = data[4]
        if month == '2月' or month == '3月' or month == '4月':
            for names, numb in dress_month.items():
                if names in dress_quarter:
                    dress_quarter[names] += numb
                else:
                    dress_quarter[names] = numb
        if month == '5月' or month == '6月' or month == '7月':
            for names, numb in dress_month.items():
                if names in dress_quarter1:
                    dress_quarter1[names] += numb
                else:
                    dress_quarter1[names] = numb
        if month == '8月' or month == '9月' or month == '10月':
            for names, numb in dress_month.items():
                if names in dress_quarter2:
                    dress_quarter2[names] += numb
                else:
                    dress_quarter2[names] = numb
        if month == '11月' or month == '12月' or month == '1月':
            for names, numb in dress_month.items():
                if names in dress_quarter3:
                    dress_quarter3[names] += numb
                else:
                    dress_quarter3[names] = numb
    print('第一季度的各服装销售件数：\n', dress_quarter)
    well, lot = sell_well(dress_quarter)
    print('第一季度最畅销的衣服是：', well, lot, '\n')
    print('第二季度的各服装销售件数：\n', dress_quarter1)
    well2, lot2 = sell_well(dress_quarter1)
    print('第二季度最畅销的衣服是：', well2, lot2, '\n')
    print('第三季度的各服装销售件数：\n', dress_quarter2)
    well3, lot3 = sell_well(dress_quarter2)
    print('第三季度最畅销的衣服是：', well3, lot3, '\n')
    print('第四季度的各服装销售件数：\n', dress_quarter3)
    well4, lot4 = sell_well(dress_quarter3)
    print('第四季度最畅销的衣服是：', well4, lot4, '\n')


while True:
    choose = int(input('请选择操作：'))
    if choose == 1:
        sale()
    elif choose == 2:
        art = number()
        print(art)
        total_number = 0
        for name, numbers in art.items():
            total_number += numbers
        print('年服装销售总量：', total_number)
        for key, value in art.items():
            print(key, '年销售（件数）占比为:%.2f' % ((value / total_number) * 100), '%')
    elif choose == 3:
        sale_month()
    elif choose == 4:
        sale_money()
    elif choose == 5:
        dress_well = number()
        name_s, num_s = sell_well(dress_well)
        print('全年最畅销的衣服是', name_s, num_s)
        print(dress_well)
    elif choose == 6:
        quarter()
    elif choose == 7:
        dress_Well = number()
        name_ss, num_ss = sell_well(dress_Well)
        print('全年销量最低的衣服是', name_ss, num_ss)
        print(dress_Well)
    elif choose == 8:
        break
    else:
        print('输入错误！请重新输入：')
