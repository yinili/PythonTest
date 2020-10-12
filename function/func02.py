# 定义函数：产生自定义个随机数
# 带参函数

import random


def generate_random(x):
    for i in range(x):
        ran = random.randint(1,20)
        print(ran, end=' ')


# 调用函数：函数名()
generate_random(3)