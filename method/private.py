#coding:UTF-8

#python的私有和公有都是对类说的，类中具有私有方法，私有属性（只能在类中被调用），私有的对象是根据名字定的，名字以__开头的。
# 而对于包而言是没有这些设定的，包中的东西都是对外公开的

class PrivateClass:
    #专有方法
    def __init__(self):
        pass
    #私有方法
    def __test(self):
        print("this is a private method")
    #公有方法
    def test(self):
        print("this is a public method")

#包里面没有私有方法，所以用private.__package()可以调用，但是不提倡这种写法，不方便读
def __package():
    print("this is a package")