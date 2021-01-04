"""
引入持久化保存概念
"""

# 用户注册
def register():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    repassword = input("请确认密码：")

    if password == repassword:

        # 保存用户信息
        with open(r'users.txt','a') as wstream:
            wstream.write(f'{username} {password}\n')
        print("用户保存成功！")
    else:
        print("两次输入的密码不一致！")

# 用户登录
def login():
    username = input("请输入用户名：")
    password = input("请输入密码：")

    if username and password:
        with open(r'users.txt') as rstream:
            while True:
                user = rstream.readline()
                if not user:
                    print("用户名或者密码输入有误")
                    break

                input_user = f'{username} {password}\n'

                if user == input_user:
                    print("用户登录成功！")
                    break

# 展示图书：
def show_books():
    print("------图书馆里面的图书有--------")
    with open(r'book.txt') as rstream:
        books = rstream.readlines()
        for book in books:
            print(book, end='')


# 调用
# register()
# login()
show_books()