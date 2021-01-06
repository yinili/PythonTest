g = (x*3 for x in range(10))

while True:
    try:
        e = next(g)
        print(e)
    except:
        print("没有更多元素了")
        break

"""
定义生成器的方式二：借助函数完成
只要函数中出现了yield关键字，说明函数就不是函数了，变成生成器
步骤：
1、定义一个函数，函数使用yield关键字
2、调用函数，接受调用的结果
3、得到的结果就是生成器
4、借助于next()或者__next__()得到想要的元素部分

"""


def fun():
    n = 0
    while True:
        n += 1
        yield n


g = fun()
print(next(g))


