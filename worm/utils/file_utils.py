#! /usr/bin/python
# -*- coding: UTF-8 -*-

#写内容到文件中
def write_to_file(content, filename):
    fo = open(filename, 'wb')
    #fo.write(content.decode('gbk').encode('utf8'))
    fo.write(content)
    fo.close()

#从文件中读取内容，并返回
def read_file(filename):
    fo = open(filename, 'rb')
    content = fo.read();
    fo.close();
    return content;
