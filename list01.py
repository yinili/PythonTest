'''
定义一个列表：
1、给列表中插入10个随机不同的整数
2、求出列表的最大值和最小值
3、求和
4、排序

'''
import random

list = []

i = 0
while i<10:
    ran = random.randint(1,20)
    if ran not in list:
        list.append(ran)
        i +=1
print(list)

print('--------求列表最大值和最小值--------------')

maxvalue = list[0]
minvalue = list[0]

for i in list:
    if i > maxvalue:
        maxvalue = i
    if i < minvalue:
        minvalue = i

print('列表中最大值是：', maxvalue)
print('列表中最小值是：', minvalue)

print('---------求出列表中所有数字的总和--------------')


print(sum(list))

value = 0
for i in list:
    value += i
print(value)

print('-----------对列表中的数字进行排序--------------')

print(sorted(list))

for i in range(len(list)):
    for j in range(len(list)-i-1):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
print(list)
