'''
装饰器
特点：
1、函数A是作为参数出现的，函数B就接受函数A作为参数
2、要有闭包的特点出现
3、多层装饰器时，谁距离函数最近就优先使用谁
'''

# 定义装饰器
def decorate(func):
    a = 100

    def wrapper(*args,**kwargs):
        print('---------11111')
        func(*args,**kwargs)
        print('---------22222')

    return wrapper

# 使用装饰器
@decorate
def house():
    print('我是毛坯房')

house()
