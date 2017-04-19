#coding:UTF-8

class varias_class(object):
    num = 10 #class varias_class 的属性, 在这里定义的都是类属性,

    #实例属性,只有用实例.属性定义的才是实例自己的属性eg:obj1.num 或者self=obj1 self.num
    #用类.属性是为类创建实例,eg:varias_class.a = 1

    #实例方法默认有一个参数self,代替实例本身, self不可省略
    #实例调用默认会将self设置成该实例
    def add_num_20(self): #class 实例方法,类不可以调用,如果要用类调用,则需要将使用的那个实例传递进去,eg: varias_class.add_num_20(obj1)
        self.num = 20 #为实例创建一个属性num

    #类方法默认一个参数cls,代替类本身,用类调用,默认会赋值给cls,类实例调用,会将实例的class赋值给cls,所以还是类的值,cls不可省略
    #类方法需要加装饰器classmethod
    @classmethod
    def class_method(cls):
        cls.num = 30 #为类创建属性
        print('class_method, num:', cls.num)
    
    #静态方法没有默认参数,所以实例和类都可以调用,但是必须要传递一个对象给self(静态方法不会默认将调用的对象赋值给第一个参数)
    #静态方法需要加装饰器static_method
    @staticmethod
    def static_method(self): #传递的self是什么就是什么,传递过来的是类,则self.num就是类属性的值,如果传递的是个实例,如果实例有num属性,就是实例的值,如果没有则还是类属性num的值
        print('static_method', self.num)

if __name__ == '__main__':
    obj1 = varias_class() #obj1不存在属性num,它获取的还是class varias_class的属性num
    obj2 = varias_class() #obj1不存在属性num,它获取的还是class varias_class的属性num

    print('obj1 property:',obj1.__dict__) #不存在属性num
    print('obj2 property:',obj2.__dict__) #不存在属性num
    print('varias_class property:',varias_class.__dict__) #存在属性num

    print('obj1.num is varias.num', obj1.num)
    print('obj2.num is varias.num', obj2.num)
    print('varias_class.num is varias.num', varias_class.num)

    #add num
    obj1.add_num_20()
    varias_class.add_num_20(obj1) #类调用实例方法,需要将所使用的实例传递进去
    varias_class.class_method()
    print('obj1.num:',obj1.num)
    obj1.class_method() #默认将obj1的类varias_class赋值给cls(class_method的第一个参数)
    varias_class.static_method(varias_class)
    varias_class.static_method(obj1) #参数赋给self, 参数是obj1
    obj1.static_method(varias_class) #参数赋值给self,参数是varias_class
    print('after add_num_20')

    print('obj1 property:', obj1.__dict__)
    print('obj2 property:', obj2.__dict__)
    print('varias_class property:', varias_class.__dict__)

    print('obj1.num is varias.num', obj1.num)
    print('obj2.num is varias.num', obj2.num)
    print('varias_class.num is varias.num', varias_class.num)

    obj1.num = obj1.num + 1 #为实例obj1设置一个属性num,先在它具有了属性,所以不用获取类varias.num的属性了

    print('为实例设置属性之后.......')
    print('obj1 property:', obj1.__dict__)
    print('obj2 property:', obj2.__dict__)
    print('varias_class property:', varias_class.__dict__)

    print('obj1.num is obj1.num', obj1.num)
    print('obj2.num is varias.num', obj2.num) #因为obj2没有设置过属性num,所以它目前获取的还是类varias的
    print('varias_class.num is varias.num', varias_class.num)

    #为类创建实例
    varias_class.a = 1
    print(varias_class.a)
    print(obj1.a)
    print(obj2.a)
    varias_class.a += 1
    print(varias_class.a)
    print(obj1.a)
    print(obj2.a)