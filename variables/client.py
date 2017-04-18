#coding:UTF-8

def int_value(num):
    num = num + 1
    print('int_value:', num)

def str_value(str):
    str = str + '1'
    print('str_value:', str)

def tup_value(param):
    print(param)
    print(param[0])
    print(param[1])

def tup_value(*param):
    print(param)

def tup_value1(**param):
    print(param)

if __name__ == '__main__':
    num = 1
    int_value(num)
    print('main:', num)
    str = 'a'
    str_value(str)
    print(str)
    tup_value((1,2))
    tup_value('a',1,3)
    tup_value1(x=3,y=1)
