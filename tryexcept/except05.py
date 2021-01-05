"""
抛出异常 raise

"""

def register():
    username = input("输入用户名：")

    if len(username) != 6:
        raise Exception('用户名长度必须6位')
    else:
        print("输入的用户名是：", username)


try:
    register()
except Exception as e:
    print(e)
else:
    print("注册成功")