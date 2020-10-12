'''
字符串内建函数
'''


message = 'zhaorui is a beautiful girl'

msg = message.capitalize() # 将字符串第一个字符串的首字母大写

print(msg)

msg = message.title()  # 字符串每个单词首字符大写
print(msg)

msg = message.istitle()  # 判断字符串中每个单词首字母是否都大写
print(msg)

msg = message.upper()  # 将字符串每个字符都大写
print(msg)

msg = message.lower()  # 将字符串每个字符都小写
print(msg)

s = 'index lucy lucky goods'
print(s.find('d'))
