from datetime import datetime
from xlrd import xldate_as_tuple
import xlrd, xlwt
from xlutils.copy import copy


def get_data(excelName, sheetName):
    workbook = xlrd.open_workbook(excelName)
    # 指定sheet名读取
    stand_sheet = workbook.sheet_by_name(sheetName)
    rows = stand_sheet.nrows  # 获取有多少行
    datas = []
    for i in range(1, rows):
        datas.append(stand_sheet.row_values(i))
        datas[i - 1].append(i)
    return datas


# 写入测试结果
def get_write(filename, name, rows, cols, values, save):
    wb = xlrd.open_workbook(filename)
    rb = copy(wb)
    sheet = rb.get_sheet(name)
    sheet.write(rows, cols, values)
    rb.save(save)
