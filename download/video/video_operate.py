#coding=UTF-8

import traceback

def getMp4(filename):
    try:
        print('读取文件名:'+filename)
        fileReader = open(filename, 'rb')
        try:
            content = fileReader.read()
            return content
        finally:
            fileReader.close()
    except Exception, e:
        print('读取文件发生异常,文件名:'+filename)
        raise e

def writeMp4(content, filename):
    try:
        print('写入文件,文件名:'+filename)
        with open(filename, 'wb') as fw:
            fw.write(content)
    except Exception,e:
        print('文件写入失败,文件名:'+filename)
        raise e
