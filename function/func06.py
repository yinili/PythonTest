'''
用户登录
输入用户名
输入密码
输入验证码----》封装成函数
'''
import random


# 定义验证码
def generate_checkcode(n):
    s='0123456789qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
    code = ''
    for i in range(n):
        ran = random.randint(0,len(s)-1)
        code += s[ran]
    return code

# 定义登录函数
def login():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    code = generate_checkcode(5)
    print('验证码是：', code)
    code1 = input('请输入验证码：')

    # 验证登录
    if code.lower()==code1.lower():
        #验证码输入正确
        if username =='lijiaqi' and password == '123456':
            print('用户登录成功')
        else:
            print('用户名或密码有误')
    else:
        print("验证码输入错误")

# 调用函数
login()
