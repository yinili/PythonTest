'''
闭包
1、闭包是在函数中提出的概念

条件：
1、外部函数中定义了内部函数
2、外部函数有返回值
3、返回值是内部函数名，不能加()
4、内部函数引用了外部函数的变量

格式：
def 外部函数()：
    ...
    def 内部函数()：
    ...
    return 内部函数

'''

def bibao01():
    a = 100

    def inner_bibao01():
        b = 99
        print(a,b)

    return inner_bibao01

x = bibao01()
x()
print(x)