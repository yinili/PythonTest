'''
内部函数

特点：
1、内部函数可以访问外部函数的变量
2、内部函数可以修改外部函数可变类型变量，比如：列表
3、内部函数默认不可以修改外部函数非可变类型变量
   若想修改，需要在内部函数第一行增加生命：nonlocal 变量名
'''

def func():
    n = 100
    list = [1,2,3,4]

    # 声明内部函数
    def inner_func():
        nonlocal n
        # 对list中每个元素进行+5操作
        for index,i in enumerate(list): #enumerate()用来把列表中元素位置信息和元素值枚举出来
            list[index] = i+n
        list.sort()

        # 修改n
        n += 10


    # 调用一下内部函数，单纯声明没有意义
    inner_func()

    print(list)
    print(n)

# 调用函数
func()