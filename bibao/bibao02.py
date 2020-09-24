'''
闭包案例
'''

def bibao02(a,b):
    c = 10

    def inner_bibao02():
        s = a+b+c
        print(s)
    return inner_bibao02


s2 = bibao02(1,2)  # s2就是inner_bibao02, s2 = inner_bibao02

# 调用返回的内部函数
s2()
