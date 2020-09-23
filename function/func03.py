'''
定义一个登录函数，参数是：username, password
函数体：
判断参数传过来的username，password是否正确，如果正确则登陆成功，否则打印登录失败
'''

def login(username,password):
    # 相当于数据库注册的用户名和密码
    uname = 'admin'
    pwd = '123'

    for i in range(3):
        if username == uname and password == pwd:
            print("登录成功")
            break
        else:
            print("登录失败")
            username = input("请输入用户名：")
            password = input("请输入密码：")
    else:
        print("账户锁定")


username = input("请输入用户名：")
password = input("请输入密码：")
login(username,password)