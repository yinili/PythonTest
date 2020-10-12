'''
找出列表最大值
'''


def max(iterable):
    max_number= iterable[0]
    for i in iterable:
        if i > max_number:
            max_number = i
    print('最大值是：', max_number)


list = [1,2,3,4,5]
max(list)