def getValue(filename):
    datas = []
    dict = {}
    f = open(file=filename, mode='r', encoding='utf-8')
    data = f.readlines()
    for line in data:
        datas.append(line.split()[0])
    for value in datas:
        if value in dict:
            dict[value] += 1
        else:
            dict[value] = 1
    return dict


def writeValue(dict):
    f = open(file='统计.txt', mode='w', encoding='utf-8')
    f.write('访问信息统计\n')
    for key, values in dict.items():
        f.writelines([key, ':', str(values), '次', '\n'])


dict = getValue('baidu_x_system.log')
writeValue(dict)
