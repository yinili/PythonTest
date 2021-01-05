"""
异常处理

try:
    可能出现异常的代码
except：
    如有出现异常要执行的代码
finally：
    不管是不是存在异常都要执行的代码，该模块可有可没有

扩展1：
try:
    可能出现异常的代码
except 异常类型1：
    如有出现异常要执行的代码
except 异常类型2：
    如有出现异常要执行的代码
...
except 异常类型n
    如有出现异常要执行的代码

扩展2：不知道是哪种错误的时候：
try:
    可能出现异常的代码
except Exception：
    如有出现异常要执行的代码
"""

def calc():
    try:
         n1 = int(input("请输入第一个数字："))
         n2 = int(input("请输入第二个数字："))
         opera = input("请输入运算符号：")

         result = 0

         if opera == '+':
             result = n1 + n2
         elif opera == '-':
             result = n1 - n2
         elif opera == '*':
             result = n1 * n2
         elif opera == '/':
             result = n1 / n2
         print("结果是：", result)

    except ZeroDivisionError:
        print("除数不要为0")
    except ValueError:
        print("必须输入数字！")
calc()