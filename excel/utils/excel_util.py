#coding:UTF-8
import xlrd

def open(path):
    excel = xlrd.open_workbook(path)
    return excel

#获取All sheet,根据下标, 返回sheet数组
def get_sheet(excel):
    return excel.sheets()

#获取sheet,根据下标
def get_sheet_by_index(excel, index):
    return excel.sheet_by_index(index)

#获取sheet,根据名字
def get_sheet_by_name(excel, name):
    return excel.sheet_by_name(name)

#获取sheet中,某一行的所有值,返回数组
def get_sheet_row_all_value(sheet, index):
    return sheet.row_values(index)

#获取sheet中,某一列的所有值,返回数组
def get_sheet_column_all_value(sheet, index):
    return sheet.column_values(index)

#获取sheet的总行数
def get_sheet_row_num(sheet):
    return sheet.nrows

#获取sheet的总列数
def get_sheet_column_num(sheet):
    return sheet.ncols

#获取单元格的值
def get_sheet_cell_value(row, col):
    return sheet.cell(row,col).value