import os

print(os.path)

path = os.path.dirname(__file__) #获取当前文件所在的目录(绝对路径)
print(path)
print(type(path))

path = os.getcwd() #当前文件所在工作目录，类似os.path.dirname(__file__)

# 复制文件改写
with open(r'file01','r') as stream:
    container = stream.read()
    file = stream.name
    filename = file[file.rfind('\\')+1:]


    path1 = os.path.dirname(__file__)
    path2 = os.path.join(path1,filename)

    with open(path2,'w') as wstream:
        wstream.write(container)

print("文件复制完成！")