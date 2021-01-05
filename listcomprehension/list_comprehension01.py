"""
列表推导式
格式：[表达式 for 变量 in 旧列表]
     [表达式 for 变量 in 旧列表 if 条件]
"""

names = ['lily', 'tom', 'jack', 'steven', 'bob', 'lucy', 'mac']

# 过滤掉长度小于或者等于3的人名
new_name = [name for name in names if len(name)>3]
print(new_name)

# 将长度大于3的人名首字母大写
new_name2=[name.capitalize() for name in names if len(name)>3]
print(new_name2)

# 将1-100之间能被3整除的数字，组成一个新的列表
num_list = [i for i in range(100) if i%3 ==0]
print(num_list)

# 0-5的偶数，0-10的奇数组成一个元祖列表，例如：[(0,1),(0,3)....]
num_list2 = [(x,y) for x in range(5) if x%2==0 for y in range(10) if y%2!=0]
print(num_list2)

# list=[[1,2,3],[4,5,6],[7,8,9],[1,3,5]] 从该列表中得到新列表[3,6,9,5]
list=[[1,2,3],[4,5,6],[7,8,9],[1,3,5]]
new_list = [i[2] for i in list]
print(new_list)


# dict1 = {'name':'tom'，'salary':'5000'}
# dict2 = {'name':'lucy'，'salary':'8000'}
# dict3 = {'name':'jack'，'salary':'4500'}
# dict4 = {'name':'lily'，'salary':'3000'}
# list ={dict1,dict2,dict3,dict4} 薪资大于5000的涨薪200，小于等于5000的涨薪500
dict1 = {'name':'tom', 'salary':5000}
dict2 = {'name':'lucy', 'salary':8000}
dict3 = {'name':'jack', 'salary':4500}
dict4 = {'name':'lily', 'salary':3000}
employee_list =[dict1, dict2, dict3, dict4]
salary_list = [employee['salary']+200 if employee['salary'] > 5000 else employee['salary']+500 for employee in employee_list]
print(salary_list)
