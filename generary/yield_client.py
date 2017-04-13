#coding:UTF-8

def testYield():
    print('方法开始')
    for i in range(10):
        print('this is ',i)
        yield i

#testYield() #直接调用是没有任何效果的,因为它是生成器,所以只有调用next方法的时候才会执行
for i in testYield():
    print('value', i)