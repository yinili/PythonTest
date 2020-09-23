
islogin = False   # 用来判断用户登录状态，默认是没有登录


def add_shoppingcart(goodsName):
    global islogin

    if islogin:
        if goodsName:
            print(f'成功将{goodsName}添加到购物车')
        else:
            print('没有添加商品')
    else:
        answer = input('用户没有登录,是否登录？（y/n）')
        if answer == 'y':
            username = input('请输入用户名：')
            password = input('请输入密码：')
            # 同意重新登录，再来一遍登录
            # 调用login函数
            islogin = login(username,password)  # 在一个函数中，可调用另外一个函数

        else:
            print('退出购物')

def login(username, password):
    if username =='lijiaqi' and password =='123456':
        print('登录成功')
        return True
    else:
        print('登录失败')
        return False

username = input('请输入用户名：')
password = input('请输入密码：')
islogin = login(username,password)
add_shoppingcart('口红')