#coding:UTF-8
#python默认逗号分割的变量为元组,元组不可改变
def set_tup():
    x,y=1,2
    a=x,y #a为一个元组,元组中的值不可改变,但是变量可以改变
    print(a[0])
    print(a[1])
    x=4
    print(a)
    print(x)
    print(y)
    print(x,y)
    print((x,y))

def set_tup2():
    a=(c,d)=(1,2)
    print(c,d) #1,2
    c=c+1 #2
    print(c,d) #2,2
    print(c) #2
    print(d) #2
    print(a) #1,2
    print((c,d)) #2,2

if __name__ == '__main__':
    #set_tup()
    set_tup2()