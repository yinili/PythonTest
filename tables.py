ceng = 1

while ceng <=9:
    # 第一种方式：采用python独有打印*
    # print('*'*ceng)
    # 第二种实现方式：采用嵌套循环
    count =1
    while count<=ceng:
        print('{}*{}={}  '.format(count,ceng,count*ceng), end='')
        count+=1
    ceng +=1
    print()