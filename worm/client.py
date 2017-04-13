#! /usr/bin/python
# -*- coding: UTF-8 -*-

import utils,re

def download_get_page_to_file(url, filename):
    content = utils.http_utils.get(url)
    utils.file_utils.write_to_file(content, filename)

def download_get_page_taobao():
    url_taobao = 'https://www.taobao.com'
    filename_taobao = './taobao.txt'
    download_get_page_to_file(url_taobao, filename_taobao)

def read_taobao_find_login_url():
    filename_taobao = './taobao.txt'
    content = utils.file_utils.read_file(filename_taobao)
    patten = re.compile(r'(?<=href=\")//login.*?(?=\")')
    match = patten.findall(content)
    print('========匹配到的内容==========')
    print(match)
    print('========over=================')
    if match:
        print('获取到的login url为：', match[0])
        content = utils.http_utils.get('http:'+match[0])
        taobao_login_to_file(content, 'login.txt')
    else:
        print('没有匹配到值:',match)
        return

def taobao_login_to_file(content, filename):
    utils.file_utils.write_to_file(content, filename)

def login_url():
    filename='./login.txt'
    content = utils.file_utils.read_file(filename)
    patten = re.compile(r'(?<=action=\")/member/.*?(?=\")')
    match = patten.findall(content)
    print('========匹配到的内容==========')
    print(match)
    print('========over=================')
    if match:
        print('匹配成功')
    else:
        print('匹配到的内容为空')

def download_swf():
    url = 'http://vm.gtimg.cn/tencentvideo/script/vplay/1704011501/play.min.js'
    filename_view = './tencent.js'
    content = utils.http_utils.get(url)
    print(content)
    utils.file_utils.write_to_file(content, filename_view)

if __name__ == '__main__':
    download_swf()
