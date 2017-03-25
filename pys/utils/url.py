#! /usr/bin/python
#_*_ coding:UTF-8 _*_

import urllib

def getUrl(url):
    print('request url:', url)
    return urllib.urlopen(url)