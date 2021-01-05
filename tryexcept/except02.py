"""
扩展2：不知道是哪种错误的时候：
try:
    可能出现异常的代码
except Exception：
    如有出现异常要执行的代码

务必注意：
多个except时，Exception要放在所有异常最后

若想根据Exception知道具体的错误原因，格式如下：

try:
    可能出现异常的代码
except Exception as e：
    如有出现异常要执行的代码
    print (e)

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

    except Exception as e:
        print("出错啦", e)

calc()