'''
打印直角三角形
*
**
***
****
*****
分析：
1、层数明确
2、发现规律 层数=*个数
3、用什么表示层、用什么表示*的个数
'''

ceng = 1

while ceng <=5:
    # 第一种方式：采用python独有打印*
    # print('*'*ceng)
    # 第二种实现方式：采用嵌套循环
    count =1
    while count<=ceng:
        print('*', end='')
        count+=1
    ceng +=1
    print()

