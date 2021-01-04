"""
复制文件，封装成函数

src、target都是文件夹，不是文件
"""


import os

def copy(src,target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)

        for file in filelist:
            path = os.path.join(src,file)
            with open(path,'rb') as rstream:
                container = rstream.read()

                path1 = os.path.join(target,file)
                with open(path1,'wb') as wstream:
                    wstream.write(container)
        else:
            print('复制完成')
