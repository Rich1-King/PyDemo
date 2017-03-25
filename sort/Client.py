# -*- coding: UTF-8 -*-
import SortClass

def sort(parms):
    sortClass = SortClass.SortClass()
    return sortClass.sortValues(parms)

def client():
    parms = [10,2,1,4,3,5,1,2,8]
    print sort(parms)
    print '排序结束.'

client()