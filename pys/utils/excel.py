#! /usr/bin/python
# -*- coding: UTF-8 -*-

def create_xlsx(filename):
    fo = open(filename, 'wb')
    fo.write('123\t456')
    fo.write('456')
    fo.close()

def read_file(filename):
    fo = open(filename, 'rb')
    print(fo.readline())
    print(fo.readline())
    fo.close()

def read_excel_to_txt(read_file, write_file):
    fo = open(read_file, 'rb')
    fw = open(write_file, 'wb')
    fw.write(fo.read())
    fw.close()
    fo.close()