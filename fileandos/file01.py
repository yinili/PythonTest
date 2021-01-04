"""
打开文件：open()

读取文件：
read()  读取所有内容
readline() 每次读取一行内容
readlines() 读取所有行，保存在列表里
readable()  判读是否可读


with open: 可以帮助我们自动释放资源
"""

# 复制文件
with open(r'file01','r') as stream:
    container = stream.read()

    with open(r'file02','w') as wstream:
        wstream.write(container)

print("文件复制完成！")