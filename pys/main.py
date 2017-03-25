#! /usr/bin/python
# -*- coding: UTF-8 -*-

from utils import url
from utils import *
import re
def test_httpget():
    url_data = url.getUrl('http://www.baidu.com')

    data = url_data.read().decode('UTF-8')

    patten = re.compile(r'(?<=href=\"//).*?(?=\")')

    match = patten.findall(data);

    if match:
        print(match)
        print(match.__getitem__(0))
        svg_request = url.getUrl('http://'+match[0])
        fo = open('baidu.svg', 'wb')
        fo.write(svg_request.read())
        fo.close()
        print(svg_request.read().decode('UTF-8'))
        print('svg write over')
    else:
        print('match is ',match)

def test_file():
    excel.create_xlsx('1.xlsx')
    #excel.read_file('2.xlsx')
    print('method over')

def test_read_excel_to_txt():
    excel.read_excel_to_txt('a.xlsx', 'a.txt')
    print('read over')

if __name__ == '__main__':
    #test_file()
    #test_httpget()
    test_read_excel_to_txt()



