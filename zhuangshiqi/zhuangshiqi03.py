'''
装饰器应用：登录验证
'''
import time

islogin = False # 默认没有登录


# 定义登录函数
def login():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == 'admin' and password =='123456':
        return True
    else:
        return False


# 定义一个装饰器，判断登录状态
def login_required(func):
    def wrapper(*args, **kwargs):
        global islogin
        print('----付款------')
        if islogin:
            func(*args, **kwargs)
        else:
            # 跳转到登录页面
            print('用户没有登录，不能付款')
            islogin = login()
            print(islogin)
    return wrapper


# 定义一个付款函数
@login_required
def pay(money):
    print(f"正在付款，付款金额是{money}元")
    print("付款中....")
    time.sleep(2)
    print('付款成功！')

pay(100)
pay(200)