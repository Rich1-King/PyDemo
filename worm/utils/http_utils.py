#! /usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib2

def get(url):
    print('request get url:', url)
    res_data = urllib2.urlopen(url)
    return res_data.read()

def post(url, param):
    true_param = urllib2.urlencode(param)
    req = urllib2.Request(url=url, data=true_param)
    print('request post url:', req)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res
