# -*- coding: UTF-8 -*-
class SortClass:
    def __init__(self):
        print '初始化方法:'
    
    def sortValues(sort,parms):
        for i in range(0,len(parms)-1):
            for j in range(0,len(parms)-i-1):
                if parms[j] > parms[j+1]:
                    temp = parms[j]
                    parms[j] = parms[j+1]
                    parms[j+1] = temp
        return parms
    