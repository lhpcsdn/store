from datetime import datetime
from xlrd import xldate_as_tuple
import xlrd
import xlwt
import time
from xlutils.copy import copy


def get_data(excelName, sheetName):
    workbook = xlrd.open_workbook(excelName)
    # 指定sheet名读取
    stand_sheet = workbook.sheet_by_name(sheetName)
    rows = stand_sheet.nrows  # 获取有多少行
    cols = stand_sheet.ncols
    datass = []
    for row in range(1, rows):
        datas = []
        for col in range(cols):
            ctype = stand_sheet.cell(row, col).ctype  # 表格的数据类型
            cell = stand_sheet.cell_value(row, col)
            if ctype == 2 and cell % 1 == 0:  # 如果是整形
                cell = int(cell)
                cell = str(cell)
            elif ctype == 3:
                # 转成datetime对象
                date = datetime(*xldate_as_tuple(cell, 0))
                cell = date.strftime('%Y/%d/%m %H:%M:%S')
            elif ctype == 4:
                cell = True if cell == 1 else False
            datas.append(cell)
            for i in datas:
                if i == '':
                    datas.remove(i)
        datas.append(row)
        datass.append(datas)
    return datass


# 写入测试结果
def get_write(filename, name, rows, cols, values, save):
    wb = xlrd.open_workbook(filename, formatting_info=True)  # formatting_info=True 保持格式
    rb = copy(wb)
    sheet = rb.get_sheet(name)
    style = xlwt.XFStyle()
    # 边框
    borders = xlwt.Borders()
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    style.borders = borders

    # 对齐
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment

    times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    sheet.write(rows, cols, values, style)
    sheet.write(rows, 4, '张三', style)
    sheet.write(rows, 5, times, style)
    rb.save(save)
