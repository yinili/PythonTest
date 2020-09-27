'''
装饰器带参数，需要定义三层
'''
def outer(a): # 这一层负责接收装饰器的参数
    def decorate(func): # 第二层：负责接收函数
        def wrapper(*args,**kwargs): # 第三层：负责接收函数的参数
            func(*args, **kwargs)
            print(f"------>铺地板{a}块")
        return wrapper
    return decorate


@outer(10)
def house():
    print("我是毛坯房")

house()