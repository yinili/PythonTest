# 记录生肖，根据年份来判断生肖

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# print(chinese_zodiac[0:4])

year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])


print('狗' not in chinese_zodiac)


