'''
输入两个字符串，从第一个字符串中删除第二个字符串中所有的字符
例如，输入'They are students' 和'aeiou'
则删除之后的第一个字符串变成'Thy r stdnts
'''

s1 = 'They are students'
s2 = 'aeiou'

# 第一种方法
# s3 = ''
# for i in s1:
#   if i not in s2 :
#     s3 += i
# print(s3)

#第二种方法：
for i in s2:
    s1 = s1.replace(i,'')
print(s1)


