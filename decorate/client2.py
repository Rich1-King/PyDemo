#coding=UTF-8

#@decore1
#@decore2
#相当于decore1(decore2())先执行括号内的，执行方法的时候不叫括号是不能执行的 

def decore1(func):
    print('hello1')
    #arg()
    return func

def decore2(func):
    print('hello2')
    #arg()
    return func

#@decore1
#@decore2
def say():
    print('function')

fun = decore1(decore2(say()))
#print(fun)
#say()
#say