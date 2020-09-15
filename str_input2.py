print(
    '''
    ***************
    英雄联盟
    ***************
    '''
)

role = input("输入角色:")
equipment = input("输入拥有的装备:")
upgrade_equipment = input("输入想购买的装备：")
pay = input("输入付款金额：")

equipment = upgrade_equipment

# 下面两种格式化方式都可以
# print('{}拥有{}装备，购买此装备花了{}钱'.format(role,equipment,pay))
print(f'{role}拥有{equipment}装备，购买此装备花了{pay}钱')