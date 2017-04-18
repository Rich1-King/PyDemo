#coding:UTF-8
from functools import partial
from types import MethodType

class ClassDemo:
    x=0
    def __init__(self,param):
        x=param
    pass
def invoke(name,*param):
    print(__name__)
    print(name,param)

f=partial(invoke, 'say_hello')
f.__name__='say_hello'
instance1 = ClassDemo(5)
#指定None这个位置的参数是指定fc这个方法是谁的方法,None的时候是指任意实例的方法
fc=MethodType(f, None, ClassDemo) #在类外创建方法(实际是为instance这个实例创建了一个方法),如果没有设置到类变量中是不会执行的,类的实例是没有的
#setattr(instance1, 'say_hello', fc) #将方法fc加入到instance这个实例中,名字为say_hello,所以只能instance这个实例调用,其他实例不能调用
setattr(ClassDemo, 'say_hello', fc) #将方法设置到类中,类的所有实例都可以调用它
