#coding=UTF-8

def decorate_1(func):
    print('decorate_1')
    def printFunc():
        print('param:')
        func()
        print('end')
    return printFunc

def decorate_2(func):
    print('decorate_2')
    def printFunc():
        print('param2')
        func()
        print('end2')
    return printFunc

def decorate_3(func):
    print('decorate_3')
    func()

@decorate_1
@decorate_2
def testMethod():
    print('this is testMethod')

#@decorate_3
def testMethod2():
    print('testMethod2')

#testMethod()
#testMethod2 = decorate_2(testMethod2)
#testMethod2()