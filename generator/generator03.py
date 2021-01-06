"""
生成器方法：
__next__():获取下一个元素
send(value):向每次生成器调用中传值，注意：第一次调用时需要send(None)
"""
def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp',temp)
        i += 1
    return '没有更多的数据了'


g = gen()
print(g.send(None))
print(g.send('呵呵'))
print(g.send('哈哈'))