#定义函数：随机数的产生

import random


def generate_random():
    for i in range(10):
        ran = random.randint(1,20)
        print(ran, end=' ')


# 调用函数：函数名()
generate_random()