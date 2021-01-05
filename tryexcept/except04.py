"""
try-except-finally

try:
    可能出现异常的代码
except：
    如有出现异常要执行的代码
finally：
    不管是不是存在异常都要执行的代码，该模块可有可没有
"""

def func():
    stream = None

    try:
        stream = open(r'../fileandos/books.txt')
        container = stream.read()
        print(container)
        return 1
    except Exception as e:
        print(e)
        return 2
    finally:
        print("-------")
        if stream:
            stream.close()
        return 3

x = func()
print(x)